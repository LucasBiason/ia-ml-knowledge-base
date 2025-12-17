# Prompts - Tutoriais Completos

Esta seção contém tutoriais completos sobre criação e gerenciamento de prompts com LangChain.

## Tutoriais Disponíveis

### 01 - PromptTemplate Básico
**Arquivo:** `notebooks/01-prompt-template-basico.ipynb`

Aprenda os fundamentos de criação de prompts:
- Como criar prompts simples
- Usar variáveis em prompts
- Formatação básica de texto

**Pré-requisitos:** Nenhum

---

### 02 - ChatPromptTemplate
**Arquivo:** `notebooks/02-chat-prompt-template.ipynb`

Domine a criação de prompts conversacionais:
- Diferença entre PromptTemplate e ChatPromptTemplate
- Usar roles (system, human, assistant)
- Melhor controle sobre contexto

**Pré-requisitos:** Tutorial 01

---

### 03 - Few-Shot Prompts
**Arquivo:** `notebooks/03-few-shot-prompts.ipynb`

Aprenda a criar prompts com exemplos:
- Incluir exemplos no prompt
- Melhorar qualidade das respostas
- Casos de uso práticos

**Pré-requisitos:** Tutorial 02

---

### 04 - Output Parsers - Extrator de Email
**Arquivo:** `notebooks/04-output-parsers-email.ipynb`

Domine a estruturação de saídas:
- StrOutputParser: String simples
- PydanticOutputParser: Objeto estruturado
- JSONOutputParser: JSON válido
- Validação de dados com Pydantic

**Pré-requisitos:** Tutorial 02

---

## Ordem Recomendada de Estudo

1. **01 - PromptTemplate Básico** (Fundamentos)
2. **02 - ChatPromptTemplate** (Prompts conversacionais)
3. **03 - Few-Shot Prompts** (Prompts com exemplos)
4. **04 - Output Parsers** (Estruturação de saídas)

---

## Conceitos-Chave

### PromptTemplate vs ChatPromptTemplate
- **PromptTemplate**: Para modelos de texto simples
- **ChatPromptTemplate**: Para modelos conversacionais
- **Diferença**: ChatPromptTemplate inclui roles
- **Vantagem**: Melhor controle sobre contexto

### Output Parsers
- **StrOutputParser**: Converte em string simples
- **PydanticOutputParser**: Converte em objeto estruturado
- **JSONOutputParser**: Converte em JSON válido
- **Custom Parsers**: Parsers personalizados

### Few-Shot Learning
- Incluir exemplos no prompt
- Melhorar qualidade das respostas
- Reduzir necessidade de fine-tuning
- Casos de uso específicos

---

## Recursos Adicionais

- [Documentação - Prompts](https://python.langchain.com/docs/modules/model_io/prompts/)
- [Documentação - Output Parsers](https://python.langchain.com/docs/modules/model_io/output_parsers/)
- [Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)

---

## Próximas Seções

- **03-Chains**: Criação de chains com LCEL
- **04-Memory**: Gerenciamento de memória
- **05-Agents**: Agents e ferramentas





