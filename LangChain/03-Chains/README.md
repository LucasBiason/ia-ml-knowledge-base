# Chains - Tutoriais Completos

Esta seção contém tutoriais completos sobre criação de chains (cadeias de processamento) usando LCEL (LangChain Expression Language).

## Tutoriais Disponíveis

### 01 - LCEL Básico - Tradutor Inteligente
**Arquivo:** `notebooks/01-lcel-basico-tradutor.ipynb`

Aprenda os fundamentos do LCEL criando um tradutor inteligente:
- Como usar o operador `|` para conectar componentes
- Criar chains elegantes e funcionais
- Usar ChatPromptTemplate com LCEL
- Implementar Output Parsers

**Pré-requisitos:** 
- Tutorial 01-LLMs-Basicos: Introdução aos LLMs
- Tutorial 02-Prompts: ChatPromptTemplate (recomendado)

---

### 02 - Chains Sequenciais - Gerador de Startup
**Arquivo:** `notebooks/02-chains-sequenciais-startup.ipynb`

Domine a criação de múltiplas chains que trabalham em sequência:
- Criar múltiplas chains interconectadas
- Execução sequencial com funções customizadas
- Validação e refinamento de dados
- Sistemas de geração de conteúdo estruturado

**Pré-requisitos:** Tutorial 01

---

### 03 - Chains Condicionais
**Arquivo:** `notebooks/03-chains-condicionais.ipynb`

Aprenda a criar chains com lógica condicional:
- Chains que mudam baseado no input
- Lógica condicional em LCEL
- Roteamento de dados
- Casos de uso práticos

**Pré-requisitos:** Tutorial 01 e 02

---

## Ordem Recomendada de Estudo

1. **01 - LCEL Básico** (Fundamentos)
2. **02 - Chains Sequenciais** (Aplicação prática)
3. **03 - Chains Condicionais** (Avançado)

---

## Conceitos-Chave

### LCEL (LangChain Expression Language)
- Sintaxe moderna usando operador `|`
- Código mais limpo e legível
- Facilita manutenção
- Substitui sintaxe antiga de chains

### Chains
- Sequência de componentes conectados
- Cada componente processa e passa para o próximo
- Permite criar pipelines complexos
- Reutilizáveis e modulares

### Output Parsers
- StrOutputParser: String simples
- PydanticOutputParser: Objeto estruturado
- JSONOutputParser: JSON válido
- Custom Parsers: Personalizados

---

## Recursos Adicionais

- [Documentação - LCEL](https://python.langchain.com/docs/expression_language/)
- [Documentação - Chains](https://python.langchain.com/docs/modules/chains/)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain-cookbook)

---

## Próximas Seções

- **04-Memory**: Gerenciamento de memória e contexto
- **05-Agents**: Agents que usam ferramentas
- **06-RAG**: Retrieval-Augmented Generation





