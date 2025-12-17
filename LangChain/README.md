# LangChain - Base de Conhecimento Completa

Base de conhecimento completa e didática sobre LangChain, framework para desenvolvimento de aplicações com modelos de linguagem (LLMs). Tutoriais estruturados e profissionais consolidando materiais de cursos e práticas.

---

## 📚 Estrutura do Conteúdo

### 00 - Fundamentos
Documentação teórica sobre LangChain, arquitetura, conceitos fundamentais e vantagens.

**Conteúdo:**
- Introdução ao LangChain
- Arquitetura e componentes
- Vantagens sobre uso direto da API
- Quando usar LangChain

---

### 01 - LLMs Básicos
Tutoriais sobre integração básica com diferentes LLMs usando LangChain.

**Tutoriais:**
1. [Introdução aos LLMs](01-LLMs-Basicos/notebooks/01-introducao-llms.ipynb) - Configuração básica
2. [ChatOpenAI](01-LLMs-Basicos/notebooks/02-chat-openai.ipynb) - Integração com OpenAI
3. [Múltiplos Provedores](01-LLMs-Basicos/notebooks/03-multiplos-provedores.ipynb) - Trocar entre LLMs (Em breve)

**Ver:** [README da Seção](01-LLMs-Basicos/README.md)

---

### 02 - Prompts
Tutoriais sobre criação e gerenciamento de prompts com LangChain.

**Tutoriais:**
1. [PromptTemplate Básico](02-Prompts/notebooks/01-prompt-template-basico.ipynb) - Prompts simples
2. [ChatPromptTemplate](02-Prompts/notebooks/02-chat-prompt-template.ipynb) - Prompts conversacionais
3. [Few-Shot Prompts](02-Prompts/notebooks/03-few-shot-prompts.ipynb) - Prompts com exemplos (Em breve)
4. [Output Parsers](02-Prompts/notebooks/04-output-parsers.ipynb) - Estruturar saídas (Em breve)

**Ver:** [README da Seção](02-Prompts/README.md)

---

### 03 - Chains
Tutoriais sobre criação de chains (cadeias de processamento) com LCEL.

**Tutoriais:**
1. [LCEL Básico](03-Chains/notebooks/01-lcel-basico.ipynb) - LangChain Expression Language
2. [Chains Sequenciais](03-Chains/notebooks/02-chains-sequenciais.ipynb) - Múltiplas chains
3. [Chains Condicionais](03-Chains/notebooks/03-chains-condicionais.ipynb) - Lógica condicional (Em breve)

**Ver:** [README da Seção](03-Chains/README.md)

---

### 04 - Memory
Tutoriais sobre gerenciamento de memória e contexto em conversas.

**Tutoriais:**
1. [Memory Básico](04-Memory/notebooks/01-memory-basico.ipynb) - Manter contexto (Em breve)
2. [ConversationBufferMemory](04-Memory/notebooks/02-buffer-memory.ipynb) - Buffer de conversa (Em breve)
3. [ConversationSummaryMemory](04-Memory/notebooks/03-summary-memory.ipynb) - Memória resumida (Em breve)

**Ver:** [README da Seção](04-Memory/README.md)

---

### 05 - Agents
Tutoriais sobre criação de agents que podem usar ferramentas.

**Tutoriais:**
1. [Agents Básicos](05-Agents/notebooks/01-agents-basicos.ipynb) - Introdução a agents (Em breve)
2. [Tools e Toolsets](05-Agents/notebooks/02-tools-toolsets.ipynb) - Criar ferramentas (Em breve)
3. [Agents Avançados](05-Agents/notebooks/03-agents-avancados.ipynb) - Agents complexos (Em breve)

**Ver:** [README da Seção](05-Agents/README.md)

---

### 06 - RAG (Retrieval-Augmented Generation)
Tutoriais sobre RAG: recuperação de informações e geração aumentada.

**Tutoriais:**
1. [Document Loaders](06-RAG/notebooks/01-document-loaders-pdf.ipynb) - Carregar documentos
2. [Text Splitters](06-RAG/notebooks/02-text-splitters.ipynb) - Dividir documentos em chunks (Em breve)
3. [Vector Stores](06-RAG/notebooks/03-vector-stores.ipynb) - Armazenar embeddings (Em breve)
4. [RAG Completo](06-RAG/notebooks/04-rag-completo.ipynb) - Sistema RAG completo (Em breve)

**Ver:** [README da Seção](06-RAG/README.md)

---

### 07 - Projects
Projetos completos integrando múltiplos componentes do LangChain.

**Projetos:**
- [Tradutor Inteligente](07-Projects/tradutor-inteligente/) - Sistema de tradução multi-idioma (Em breve)
- [Leitor de PDF](07-Projects/leitor-pdf/) - Análise inteligente de PDFs (Em breve)
- [Extrator de Email](07-Projects/extrator-email/) - Processamento de emails (Em breve)
- [Gerador de Startup](07-Projects/gerador-startup/) - Geração de conteúdo estruturado (Em breve)

---

### 08 - Cache
Tutoriais completos sobre cacheamento no LangChain para reduzir custos e melhorar performance.

**Tutoriais:**
1. [Cache Básico](08-Cache/notebooks/01-cache-basico.ipynb) - InMemory e SQLite
2. [Cache Redis](08-Cache/notebooks/02-cache-redis.ipynb) - Cache distribuído
3. [Cache PostgreSQL](08-Cache/notebooks/03-cache-postgres.ipynb) - Cache persistente em produção

**Ver:** [README da Seção](08-Cache/README.md)

**Projetos:**
- [Tradutor Inteligente](07-Projects/tradutor-inteligente/) - Sistema de tradução multi-idioma
- [Leitor de PDF](07-Projects/leitor-pdf/) - Análise inteligente de PDFs
- [Extrator de Email](07-Projects/extrator-email/) - Processamento de emails
- [Gerador de Startup](07-Projects/gerador-startup/) - Geração de conteúdo estruturado

---

## 🚀 Quick Start

### 1. Configuração do Ambiente

```bash
# Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instalar dependências
pip install -r ../requirements.txt
```

### 2. Configurar API Key

Crie um arquivo `.env` na raiz do projeto:

```env
OPENAI_API_KEY=sua_chave_aqui
```

### 3. Executar Notebooks

```bash
# Iniciar Jupyter
jupyter notebook

# Ou JupyterLab
jupyter lab
```

**Kernel recomendado:** `IA ML Knowledge` (registrado via `python -m ipykernel install --user --name ia-ml-knowledge`)

---

## 📖 Ordem Recomendada de Estudo

### Iniciante
1. **00-Fundamentos** - Conceitos básicos
2. **01-LLMs-Basicos/01** - Introdução aos LLMs
3. **02-Prompts/01** - PromptTemplate básico
4. **02-Prompts/02** - ChatPromptTemplate
5. **03-Chains/01** - LCEL básico

### Intermediário
6. **03-Chains/02** - Chains sequenciais
7. **06-RAG/01** - Document Loaders
8. **06-RAG/02** - Text Splitters
9. **04-Memory/01** - Memory básico

### Avançado
10. **05-Agents** - Agents e Tools
11. **06-RAG/03-04** - Vector Stores e RAG completo
12. **07-Projects** - Projetos completos

---

## 📚 Documentação Teórica

- [Artigo Teórico Completo](docs/ARTIGO_TEORICO_LANGCHAIN.md) - Visão geral completa sobre LangChain (Em breve)
- [Infográficos](docs/INFOGRAFICOS/) - Diagramas e visualizações (Em breve)
- [Glossário](docs/GLOSSARIO.md) - Termos técnicos explicados (Em breve)

---

## 🎯 Casos de Uso Práticos

### Chains
- Sistemas de tradução
- Processamento de documentos
- Geração de conteúdo estruturado
- Pipelines de processamento

### Agents
- Assistentes que usam ferramentas
- Automação de tarefas
- Integração com APIs externas
- Sistemas de decisão

### RAG
- Chatbots com conhecimento específico
- Sistemas de Q&A sobre documentos
- Busca semântica
- Análise de documentos

### Memory
- Conversas contextuais
- Assistentes com histórico
- Sistemas de recomendação
- Chatbots persistentes

---

## 💰 Custos e Limitações

### LangChain
- **Overhead mínimo**: LangChain adiciona pouco overhead
- **Cache integrado**: Reduz custos em desenvolvimento
- **Abstração**: Facilita trocar de provedor (custos diferentes)

### Modelos
- Custos dependem do provedor escolhido
- OpenAI: Ver [pricing oficial](https://openai.com/pricing)
- Anthropic: Ver [pricing oficial](https://www.anthropic.com/pricing)
- Outros: Consultar documentação do provedor

**Nota:** LangChain não adiciona custos, apenas facilita o uso dos LLMs.

---

## 🔗 Referências

### Documentação Oficial
- [LangChain Python](https://python.langchain.com/)
- [LangChain API Reference](https://api.python.langchain.com/)
- [LangChain Cookbook](https://github.com/langchain-ai/langchain-cookbook)

### Recursos Adicionais
- [LangChain GitHub](https://github.com/langchain-ai/langchain)
- [Community Forum](https://github.com/langchain-ai/langchain/discussions)
- [LangChain Blog](https://blog.langchain.dev/)

---

## 📝 Contribuindo

Este é um projeto de conhecimento pessoal consolidando materiais de cursos. Sinta-se livre para usar e adaptar conforme necessário.

---

## 📄 Licença

Este projeto faz parte do repositório [ia-ml-knowledge-base](https://github.com/LucasBiason/ia-ml-knowledge-base) e está licenciado sob MIT.

---

**Última atualização:** Dezembro 2025  
**Status:** Em desenvolvimento ativo

