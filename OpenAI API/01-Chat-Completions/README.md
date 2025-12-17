# Chat Completions - Tutoriais Completos

Esta seção contém tutoriais completos sobre a API de Chat Completions da OpenAI, que permite criar conversas com modelos de linguagem como GPT-3.5-turbo e GPT-4.

## Tutoriais Disponíveis

### 01 - Conversa Básica
**Arquivo:** `notebooks/01-conversa-basica.ipynb`

Aprenda os fundamentos da API de Chat Completions:
- Como fazer uma requisição básica
- Entender os diferentes roles (system, user, assistant)
- Configurar parâmetros básicos (model, temperature, max_tokens)

---

### 02 - Agentes Especializados
**Arquivo:** `notebooks/02-agentes-especializados.ipynb`

Domine a criação de agentes especializados:
- Uso avançado da role `system`
- Integração de dados como contexto
- Casos de uso práticos

---

### 03 - Parâmetros Avançados
**Arquivo:** `notebooks/03-parametros-avancados.ipynb`

Explore todos os parâmetros da API:
- `temperature`: Controla criatividade
- `max_tokens`: Limita tamanho da resposta
- `top_p`: Nucleus sampling
- `frequency_penalty`: Reduz repetição
- `presence_penalty`: Incentiva novos tópicos
- `n`: Múltiplas respostas
- `stop`: Sequências de parada

---

## Ordem Recomendada de Estudo

1. **01 - Conversa Básica** (Fundamentos)
2. **02 - Agentes Especializados** (Aplicação prática)
3. **03 - Parâmetros Avançados** (Otimização)

**Nota:** Temas avançados como **Function Calling** e **Extração de Dados JSON** integrando múltiplas APIs (Chat + Vision + Audio) estão localizados no módulo **06-Advanced**.

---

## Conceitos-Chave

![Infográfico: Fluxo de Chat Completions](../assets/imagens/tutorials/chat-completions-flow.png)

### Roles (Papéis)
- **system**: Define contexto e comportamento do assistente
- **user**: Mensagens do usuário final
- **assistant**: Respostas anteriores (para manter contexto)

### Modelos Disponíveis
- `gpt-3.5-turbo`: Rápido e econômico
- `gpt-4`: Mais poderoso, melhor qualidade
- `gpt-4-turbo`: Versão otimizada do GPT-4

### Casos de Uso
- Chatbots e assistentes virtuais
- Análise de dados e relatórios
- Extração de informações
- Geração de conteúdo
- Tradução e sumarização

---

## Dependências

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

**Dependências principais:**
- `openai`: Cliente da API OpenAI
- `python-dotenv`: Carregamento de variáveis de ambiente
- `pandas`: Processamento de dados (para exercícios com CSV)

---

## Recursos Adicionais

- [Documentação Oficial - Chat Completions](https://platform.openai.com/docs/guides/text-generation)
- [API Reference](https://platform.openai.com/docs/api-reference/chat)
- [Modelos Disponíveis](https://platform.openai.com/docs/models)
- [Best Practices](https://platform.openai.com/docs/guides/prompt-engineering)



