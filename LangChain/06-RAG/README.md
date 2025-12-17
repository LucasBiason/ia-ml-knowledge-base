# RAG (Retrieval-Augmented Generation) - Tutoriais Completos

Esta seção contém tutoriais completos sobre RAG: recuperação de informações e geração aumentada com LangChain.

## Tutoriais Disponíveis

### 01 - Document Loaders - Leitor de PDF
**Arquivo:** `notebooks/01-document-loaders-pdf.ipynb`

Aprenda a carregar documentos de diferentes fontes:
- PyPDFLoader: Carregar PDFs
- DirectoryLoader: Carregar múltiplos arquivos
- TextLoader: Carregar arquivos de texto
- WebBaseLoader: Carregar conteúdo de websites

**Pré-requisitos:** 
- Tutorial 01-LLMs-Basicos: Introdução aos LLMs
- Tutorial 02-Prompts: ChatPromptTemplate

---

### 02 - Text Splitters
**Arquivo:** `notebooks/02-text-splitters.ipynb`

Domine estratégias de divisão de documentos:
- RecursiveCharacterTextSplitter: Divisor inteligente
- CharacterTextSplitter: Divisor por caracteres
- TokenTextSplitter: Divisor por tokens
- Estratégias de chunking otimizadas

**Pré-requisitos:** Tutorial 01

---

### 03 - Vector Stores
**Arquivo:** `notebooks/03-vector-stores.ipynb`

Aprenda a armazenar e buscar embeddings:
- Criar vector stores
- Armazenar documentos como embeddings
- Busca semântica
- Integração com diferentes vector DBs

**Pré-requisitos:** Tutorial 01 e 02

---

### 04 - RAG Completo
**Arquivo:** `notebooks/04-rag-completo.ipynb`

Construa um sistema RAG completo:
- Pipeline completo: Load → Split → Embed → Store → Retrieve
- Integração com LLMs
- Sistema de Q&A sobre documentos
- Otimização e melhoria

**Pré-requisitos:** Todos os tutoriais anteriores

---

## Ordem Recomendada de Estudo

1. **01 - Document Loaders** (Carregar documentos)
2. **02 - Text Splitters** (Dividir documentos)
3. **03 - Vector Stores** (Armazenar embeddings)
4. **04 - RAG Completo** (Sistema completo)

---

## Conceitos-Chave

### Document Loaders
- Carregam documentos de diferentes fontes
- Suportam múltiplos formatos (PDF, TXT, HTML, etc.)
- Integração com APIs e bancos de dados
- Processamento em lote

### Text Splitters
- Dividem documentos em chunks menores
- Estratégias de chunking otimizadas
- Preservam contexto entre chunks
- Configuráveis (tamanho, sobreposição)

### Vector Stores
- Armazenam documentos como embeddings
- Permitem busca semântica
- Integração com diferentes DBs
- Escaláveis e eficientes

### RAG Pipeline
1. **Load**: Carregar documentos
2. **Split**: Dividir em chunks
3. **Embed**: Criar embeddings
4. **Store**: Armazenar em vector store
5. **Retrieve**: Buscar documentos relevantes
6. **Generate**: Gerar resposta com contexto

---

## Recursos Adicionais

- [Documentação - Document Loaders](https://python.langchain.com/docs/modules/data_connection/document_loaders/)
- [Documentação - Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/text_splitters/)
- [Documentação - Vector Stores](https://python.langchain.com/docs/modules/data_connection/vectorstores/)
- [RAG Tutorial](https://python.langchain.com/docs/use_cases/question_answering/)

---

## Próximas Seções

- **05-Agents**: Agents que usam ferramentas
- **07-Projects**: Projetos completos





