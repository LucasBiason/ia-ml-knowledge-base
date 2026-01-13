# IA/ML Knowledge Base

**Inteligência Artificial e Machine Learning aplicados, documentados a partir de estudo prático e projetos reais.**

Este repositório faz parte da iniciativa **Engineering Knowledge Base**. O objetivo não é criar um "mega banco de conhecimento", mas documentar estudos aplicados, decisões técnicas e casos práticos de IA e Machine Learning.

O conteúdo reflete experimentação real, projetos desenvolvidos e aprendizado incremental.

---

## Sobre este repositório

Este repositório documenta minha prática contínua em Inteligência Artificial e Machine Learning, focando em aplicação real, não em teoria abstrata.

**Este repositório não é:**
- Um curso completo de IA/ML
- Material gerado automaticamente
- Uma coleção de tutoriais genéricos
- Um "mega banco de conhecimento" promocional

**Este repositório é:**
- Documentação de estudos aplicados
- Casos práticos de projetos reais
- Decisões técnicas justificadas
- Base de referência para consulta

---

## Objetivo

Consolidar conhecimento sobre IA e ML através de:

- Projetos práticos desenvolvidos com padrões profissionais
- Documentação técnica especializada
- Integrações reais com APIs e serviços
- Casos de uso documentados

---

## O que você vai encontrar aqui

### Machine Learning
- Algoritmos clássicos de ML (scikit-learn)
- Pipelines de treinamento e avaliação
- Projetos práticos

### Deep Learning
- Redes neurais profundas
- TensorFlow/PyTorch
- Arquiteturas e otimizações

### LLMs (Large Language Models)
- Integração com OpenAI API
- Integração com Gemini API
- Prompts catalogados e testados
- Casos de uso práticos

### LangChain
- Framework para construção de aplicações com LLMs
- Agentes e chains
- RAG (Retrieval-Augmented Generation)

### Computer Vision
- Processamento de imagens
- Detecção de objetos
- Aplicações práticas

### NLP (Natural Language Processing)
- Processamento de linguagem natural
- Análise de texto
- Casos práticos

### OpenAI API
- Integrações completas
- Documentação técnica
- Exemplos práticos

### AWS ML Services
- Serviços AWS para Machine Learning
- Integrações e casos de uso

### MLOps
- Deploy e monitoramento de modelos
- Pipelines de produção
- Boas práticas

---

## O que você NÃO vai encontrar

- Conteúdo gerado automaticamente
- Tutoriais genéricos de "aprenda ML do zero"
- Promessas de "200+ páginas" ou números inflados
- Material sem contexto ou justificativa técnica

---

## Estrutura

```
ia-ml-knowledge-base/
├── Machine Learning/          # ML tradicional
│   ├── notebooks/
│   ├── tutorials/
│   └── projects/
│
├── Deep Learning/             # Redes neurais profundas
│   ├── notebooks/
│   └── projects/
│
├── LLMs/                     # Large Language Models
│   ├── notebooks/
│   └── prompts/
│
├── LangChain/                # Framework para LLMs
│   ├── notebooks/
│   └── projects/
│
├── Computer Vision/          # Visão computacional
│   ├── notebooks/
│   └── projects/
│
├── NLP/                      # Processamento de linguagem natural
│   ├── notebooks/
│   └── projects/
│
├── OpenAI API/                # Integrações OpenAI
│   ├── notebooks/
│   ├── docs/
│   └── examples/
│
├── AWS ML Services/          # Serviços AWS
│   └── notebooks/
│
├── MLOps/                    # Deploy e monitoramento
│   ├── notebooks/
│   └── projects/
│
├── docs/                     # Documentação adicional
│   └── roadmap.md
│
└── templates/                # Templates
    └── notebook-template.ipynb
```

---

## Público-alvo

- Engenheiros de software interessados em IA aplicada
- Desenvolvedores trabalhando com LLMs
- Profissionais de produto explorando IA
- Estudantes consolidando conhecimentos práticos

---

## Como este conteúdo é produzido

- **Escrita manual e incremental:** Cada notebook é escrito manualmente
- **Projetos reais:** Conteúdo baseado em projetos desenvolvidos
- **Decisões documentadas:** Justificativas técnicas explícitas
- **Evolução contínua:** Conteúdo cresce ao longo do tempo

---

## Relação com o Ecossistema

Este repositório faz parte do **Engineering Knowledge Base**.

- **Base teórica para:** Hackathon Threat Modeling (YOLO, visão computacional)
- **Conecta com:**
  - Data Science KB (pré-requisito para ML)
  - Programming KB (algoritmos fundamentais)
  - Microservices KB (ML em produção, MLOps)
- **Aplica em:**
  - Hackathon FIAP Fase 5 (YOLO para detecção de componentes)
  - Projetos de portfólio (ML Sales Forecasting, ML Spam Classifier)

---

## Como usar

### Instalação

```bash
# Clone o repositório
git clone https://github.com/LucasBiason/ia-ml-knowledge-base.git
cd ia-ml-knowledge-base

# Crie um ambiente virtual
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# ou
.venv\Scripts\activate  # Windows

# Instale as dependências
pip install -r requirements.txt
```

### Executar Notebooks

```bash
# Inicie o Jupyter
jupyter notebook

# Ou use JupyterLab
jupyter lab
```

---

## Stack Utilizada

### Tecnologias Principais
- **Python 3.9+** - Linguagem principal
- **FastAPI** - Framework web para APIs
- **Docker & Docker Compose** - Containerização
- **PostgreSQL** - Banco de dados
- **Redis** - Cache e filas

### Machine Learning & IA
- **scikit-learn** - Algoritmos de ML
- **TensorFlow/PyTorch** - Deep Learning
- **LangChain** - Framework para LLMs
- **OpenAI API** - Integração com GPT
- **Gemini API** - Integração com Gemini

### Qualidade & Testes
- **pytest** - Framework de testes
- **Black** - Formatação de código
- **isort** - Organização de imports
- **flake8** - Linting

---

## Status

**Em desenvolvimento contínuo.**

Conteúdo é adicionado incrementalmente conforme projetos e estudos avançam.

---

## Outros repositórios da Knowledge Base

- **[Engineering Knowledge Base](../engineering-knowledge-base/)** - Hub central do ecossistema
- **[Programming Knowledge Base](../programming-knowledge-base/)** - Fundamentos algorítmicos
- **[Data Science Knowledge Base](../data-science-knowledge-base/)** - Manipulação e análise de dados
- **[Microservices Knowledge Base](../microservices-knowledge-base/)** - Arquitetura de sistemas distribuídos

---

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

---

*Desenvolvido por Lucas Biason para consolidar conhecimentos em IA/ML e criar uma base de referência prática.*
