# Glossário - Termos Técnicos OpenAI

Glossário completo de termos técnicos relacionados à OpenAI e suas APIs.

---

## A

### API Key
Chave de autenticação única fornecida pela OpenAI para acessar as APIs. Deve ser mantida em segredo e nunca commitada em repositórios públicos.

### Attention Mechanism
Mecanismo que permite ao modelo focar em partes relevantes do input durante o processamento. Fundamental na arquitetura Transformer.

---

## B

### Batch Processing
Processamento de múltiplas requisições em lote, mais eficiente e econômico que requisições individuais.

---

## C

### Chat Completions
Endpoint da API OpenAI para conversas com modelos de linguagem. Suporta múltiplas mensagens e contexto de conversa.

### Context Window
Número máximo de tokens que um modelo pode processar em uma única requisição. Inclui tanto input quanto output.

---

## D

### DALL-E
Modelo de geração de imagens da OpenAI que cria imagens a partir de descrições textuais (prompts).

### Decoder
Parte da arquitetura Transformer responsável por gerar a saída. GPT usa apenas decoder (decoder-only).

---

## E

### Embedding
Representação vetorial densa de texto que captura significado semântico. Permite busca e comparação semântica.

### Encoder
Parte da arquitetura Transformer responsável por processar o input. Usado em modelos como BERT.

---

## F

### Few-Shot Learning
Capacidade de um modelo aprender com poucos exemplos (3-5) sem necessidade de fine-tuning.

### Fine-Tuning
Processo de ajustar um modelo pré-treinado para uma tarefa ou domínio específico usando dados customizados.

### Frequency Penalty
Parâmetro que penaliza tokens que aparecem com frequência no texto, reduzindo repetição.

---

## G

### GPT (Generative Pre-trained Transformer)
Família de modelos de linguagem da OpenAI baseados na arquitetura Transformer.

---

## H

### Hallucination (Alucinação)
Fenômeno onde o modelo gera informações que parecem plausíveis mas são incorretas ou inventadas.

---

## I

### Image Generation
Processo de criar imagens a partir de descrições textuais usando modelos como DALL-E.

---

## J

### JSON Mode
Modo especial da API que força respostas em formato JSON válido, útil para extração estruturada de dados.

---

## L

### LLM (Large Language Model)
Modelo de linguagem de grande escala treinado em vastas quantidades de texto para entender e gerar linguagem natural.

---

## M

### max_tokens
Parâmetro que limita o número máximo de tokens na resposta, útil para controlar custos e tamanho.

### Model
Versão específica de um algoritmo de IA (ex: gpt-3.5-turbo, gpt-4, dall-e-3).

---

## N

### n (Number of Completions)
Parâmetro que especifica quantas respostas diferentes gerar para a mesma pergunta.

### Nucleus Sampling (top_p)
Método de amostragem que considera apenas tokens com probabilidade acumulada até um threshold.

---

## O

### OpenAI
Empresa de pesquisa em IA fundada em 2015, criadora dos modelos GPT, DALL-E, Whisper, etc.

---

## P

### Presence Penalty
Parâmetro que penaliza tokens baseado em se já apareceram no texto, incentivando novos tópicos.

### Prompt
Texto de entrada fornecido ao modelo, contendo instruções, contexto ou perguntas.

### Prompt Engineering
Arte e ciência de criar prompts efetivos para obter melhores resultados dos modelos.

---

## R

### Rate Limit
Limite de requisições por minuto/hora imposto pela API para prevenir abuso e garantir estabilidade.

### Role
Papel de uma mensagem na conversa: `system` (contexto), `user` (usuário), `assistant` (modelo).

---

## S

### Speech-to-Text (STT)
Conversão de áudio em texto usando modelos como Whisper.

### Stop Sequence
Sequência de texto que faz o modelo parar a geração quando encontrada.

### Streaming
Modo de receber respostas em tempo real, token por token, em vez de esperar resposta completa.

---

## T

### Temperature
Parâmetro que controla aleatoriedade na geração (0.0 = determinístico, 2.0 = muito criativo).

### Text-to-Speech (TTS)
Conversão de texto em áudio usando síntese de voz neural.

### Token
Unidade básica de texto processada pelo modelo. Aproximadamente 4 caracteres = 1 token.

### Tokenization
Processo de converter texto em tokens que o modelo pode processar.

### Transformer
Arquitetura de rede neural introduzida em 2017, base de todos os modelos GPT.

---

## V

### Vision
Capacidade de modelos como GPT-4 de analisar e entender imagens.

---

## W

### Whisper
Modelo de transcrição de áudio da OpenAI, suporta 99 idiomas e múltiplos formatos.

---

## Z

### Zero-Shot Learning
Capacidade de um modelo realizar uma tarefa sem exemplos prévios, apenas com instruções.

---

## Exemplos Práticos

### Exemplo: Token
```
Texto: "Hello world"
Tokens: ["Hello", " world"]
Total: 2 tokens
```

### Exemplo: Temperature
```python
temperature=0.0  # Sempre mesma resposta
temperature=0.7  # Equilíbrio (recomendado)
temperature=1.5  # Muito criativo
```

### Exemplo: Roles
```python
messages=[
    {"role": "system", "content": "Você é um assistente útil."},
    {"role": "user", "content": "O que é Python?"},
    {"role": "assistant", "content": "Python é uma linguagem..."}
]
```

---

**Última atualização:** Dezembro 2025





