# Arquitetura da API OpenAI

**Referência:** Seção 00 - Fundamentos

---

## Visão Geral

A API da OpenAI é uma API REST que permite acesso programático aos modelos de IA da empresa. A arquitetura é baseada em requisições HTTP padrão, facilitando integração com qualquer linguagem de programação.

## Estrutura de Requisições

### Endpoint Base
```
https://api.openai.com/v1/
```

### Formato de Requisição
- **Método**: POST (maioria dos endpoints)
- **Headers**: 
  - `Authorization: Bearer {API_KEY}`
  - `Content-Type: application/json`
- **Body**: JSON com parâmetros específicos do endpoint

### Formato de Resposta
- **Status Code**: 200 (sucesso) ou códigos de erro HTTP padrão
- **Body**: JSON com dados da resposta
- **Estrutura**: Varia por endpoint, mas geralmente inclui:
  - Dados principais (resposta, imagem, etc.)
  - Metadados (tokens usados, modelo, etc.)

## Endpoints Principais

### 1. Chat Completions
**Endpoint:** `POST /v1/chat/completions`

**Uso:** Conversas com modelos de linguagem

**Estrutura de Requisição:**
```json
{
  "model": "gpt-3.5-turbo",
  "messages": [
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
  ],
  "temperature": 0.7,
  "max_tokens": 500
}
```

**Estrutura de Resposta:**
```json
{
  "id": "chatcmpl-...",
  "object": "chat.completion",
  "created": 1234567890,
  "model": "gpt-3.5-turbo",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 20,
    "total_tokens": 30
  }
}
```

### 2. Image Generation
**Endpoint:** `POST /v1/images/generations`

**Uso:** Gerar imagens a partir de texto

**Estrutura de Requisição (DALL-E 3):**
```json
{
  "model": "dall-e-3",
  "prompt": "...",
  "size": "1024x1024",
  "quality": "standard",
  "style": "vivid"
}
```
**Nota:** DALL-E 3 sempre gera 1 imagem por requisição (parâmetro `n` não disponível). Para múltiplas imagens, use DALL-E 2.

**Estrutura de Requisição (DALL-E 2):**
```json
{
  "model": "dall-e-2",
  "prompt": "...",
  "size": "1024x1024",
  "n": 1,
  "response_format": "url"
}
```

**Estrutura de Resposta:**
```json
{
  "created": 1234567890,
  "data": [
    {
      "url": "https://...",
      "revised_prompt": "..."
    }
  ]
}
```

### 3. Audio (TTS)
**Endpoint:** `POST /v1/audio/speech`

**Uso:** Converter texto em áudio

**Estrutura de Requisição:**
```json
{
  "model": "tts-1",
  "input": "...",
  "voice": "alloy",
  "response_format": "mp3",
  "speed": 1.0
}
```

**Vozes disponíveis:** `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`

**Resposta:** Arquivo de áudio binário (não JSON)

### 4. Audio (Transcription)
**Endpoint:** `POST /v1/audio/transcriptions`

**Uso:** Transcrever áudio em texto

**Formato:** multipart/form-data (não JSON)
- Campo `file`: arquivo de áudio (obrigatório)
- Campo `model`: "whisper-1" (obrigatório)
- Campo `language`: código do idioma (opcional, ex: "pt", "en")
- Campo `prompt`: contexto adicional (opcional)
- Campo `response_format`: "json", "text", "srt", "verbose_json", "vtt" (padrão: "json")
- Campo `temperature`: 0.0 a 1.0 (opcional)

### 5. Embeddings
**Endpoint:** `POST /v1/embeddings`

**Uso:** Criar vetores de texto

**Estrutura de Requisição:**
```json
{
  "model": "text-embedding-3-small",
  "input": "texto ou array de textos",
  "encoding_format": "float",
  "dimensions": 1536
}
```

**Estrutura de Resposta:**
```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [0.1, 0.2, ...],
      "index": 0
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}
```

## Fluxo de Comunicação

### 1. Autenticação
```
Cliente → API
Headers: Authorization: Bearer {API_KEY}
```

### 2. Requisição
```
Cliente → API
POST /v1/{endpoint}
Body: JSON com parâmetros
```

### 3. Processamento
```
API → Modelo Interno
- Validação de requisição
- Processamento pelo modelo
- Geração de resposta
```

### 4. Resposta
```
API → Cliente
Status: 200 OK
Body: JSON com resultado
```

## Rate Limits

### Limites por Tipo de Conta
- **Free Tier**: Limites mais restritivos
- **Paid Tier**: Limites maiores
- **Enterprise**: Limites customizados

### Tipos de Limites
- **RPM** (Requests Per Minute): Requisições por minuto
- **RPD** (Requests Per Day): Requisições por dia
- **TPM** (Tokens Per Minute): Tokens processados por minuto

### Tratamento de Rate Limits
- Status Code: 429 (Too Many Requests)
- Header `Retry-After`: Tempo em segundos para retry
- Implementar retry com backoff exponencial

## Tokens e Context Window

### O que são Tokens?
- Unidades de texto processadas pelo modelo
- Aproximadamente 4 caracteres = 1 token (varia por idioma e tipo de texto)
- Tokens podem ser palavras completas ou partes de palavras
- Exemplo: "Hello world" = 2 tokens
- Em português, a relação pode variar (palavras mais longas geram mais tokens)

### Context Window
- Número máximo de tokens que o modelo pode processar
- Inclui tanto input (prompt) quanto output (resposta)
- **GPT-3.5-turbo**: 16,385 tokens (16k)
- **GPT-4 Turbo**: 128,000 tokens (128k)
- **GPT-4**: 8,192 tokens (8k)

### Cálculo de Tokens
- Tokens de entrada: contados do prompt
- Tokens de saída: contados da resposta gerada
- Total: soma de entrada + saída
- Custo baseado em tokens usados

## Códigos de Status HTTP

### Sucesso
- **200 OK**: Requisição bem-sucedida

### Erros do Cliente (4xx)
- **400 Bad Request**: Requisição inválida
- **401 Unauthorized**: API key inválida ou ausente
- **403 Forbidden**: Sem permissão para acessar recurso
- **404 Not Found**: Endpoint não encontrado
- **429 Too Many Requests**: Rate limit excedido

### Erros do Servidor (5xx)
- **500 Internal Server Error**: Erro interno da OpenAI
- **502 Bad Gateway**: Problema de infraestrutura
- **503 Service Unavailable**: Serviço temporariamente indisponível

## Estrutura de Erros

### Formato Padrão
```json
{
  "error": {
    "message": "Descrição do erro",
    "type": "invalid_request_error",
    "param": "model",
    "code": "model_not_found"
  }
}
```

### Tipos de Erro
- `invalid_request_error`: Requisição inválida
- `authentication_error`: Problema de autenticação
- `rate_limit_error`: Rate limit excedido
- `api_error`: Erro interno da API
- `server_error`: Erro do servidor

## Boas Práticas de Arquitetura

### 1. Tratamento de Erros
- Sempre verificar status code
- Implementar retry logic para erros temporários
- Logar erros para debugging
- Tratar rate limits adequadamente

### 2. Otimização de Requisições
- Usar streaming quando possível
- Batch processing para múltiplas requisições
- Cache de respostas quando apropriado
- Limitar max_tokens para controlar custos

### 3. Segurança
- Nunca expor API keys no código
- Usar variáveis de ambiente
- Validar inputs antes de enviar
- Implementar rate limiting no lado do cliente

### 4. Monitoramento
- Rastrear uso de tokens
- Monitorar custos
- Alertas para erros
- Métricas de performance

## Próximos Passos

Após entender a arquitetura da API, o próximo tópico fundamental é:
- **Autenticação e Segurança** - Como configurar e proteger seu acesso

---

## Referências

- [API Reference](https://platform.openai.com/docs/api-reference)
- [Rate Limits](https://platform.openai.com/docs/guides/rate-limits)
- [Error Handling](https://platform.openai.com/docs/guides/error-codes)

