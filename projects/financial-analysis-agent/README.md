# 🤖 Financial Analysis Agent

> **Agente Inteligente de Análise Financeira usando IA e LangChain**

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)](https://streamlit.io)
[![Docker](https://img.shields.io/badge/Docker-20.10+-blue.svg)](https://docker.com)
[![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)](https://langchain.com)

## 📋 Índice

- [🎯 Sobre o Projeto](#-sobre-o-projeto)
- [🚀 Funcionalidades](#-funcionalidades)
- [🏗️ Arquitetura](#️-arquitetura)
- [🛠️ Tecnologias](#️-tecnologias)
- [📦 Pré-requisitos](#-pré-requisitos)
- [⚡ Instalação Rápida](#-instalação-rápida)
- [🔧 Configuração](#-configuração)
- [📖 Como Usar](#-como-usar)
- [🔌 API Endpoints](#-api-endpoints)
- [🌐 Interface Web](#-interface-web)
- [🐳 Docker](#-docker)
- [📁 Estrutura do Projeto](#-estrutura-do-projeto)
- [🧪 Testes](#-testes)
- [🚀 Deploy](#-deploy)
- [🤝 Contribuição](#-contribuição)
- [📄 Licença](#-licença)

## 🎯 Sobre o Projeto

O **Financial Analysis Agent** é um sistema inteligente de análise financeira que combina a potência da IA (OpenAI GPT) com ferramentas especializadas para fornecer análises abrangentes de ações do mercado financeiro.

### ✨ Características Principais

- **Análise Fundamentalista**: Avaliação de indicadores financeiros e perspectivas de crescimento
- **Análise Técnica**: Análise de padrões gráficos, médias móveis e indicadores técnicos
- **Análise de Risco**: Identificação e avaliação de riscos operacionais e de mercado
- **Análise Abrangente**: Combinação de todas as análises com contexto de mercado
- **Interface Web Intuitiva**: Dashboard Streamlit para fácil utilização
- **API REST Completa**: Endpoints para integração com outros sistemas
- **Arquitetura Modular**: Código organizado e escalável

## 🚀 Funcionalidades

### 📊 Análises Disponíveis

| Tipo | Descrição | Endpoint |
|------|-----------|----------|
| **Fundamentalista** | Indicadores financeiros, crescimento, setor | `/analyze/fundamental` |
| **Técnica** | Padrões gráficos, médias móveis, momentum | `/analyze/technical` |
| **Risco** | Riscos operacionais, financeiros e de mercado | `/analyze/risk` |
| **Abrangente** | Combinação de todas as análises | `/analyze/comprehensive` |

### 🧠 Recursos de IA

- **Processamento de Linguagem Natural** com GPT-3.5-turbo
- **Análise Contextual** de mercado
- **Resumos Executivos** automatizados
- **Recomendações Inteligentes** baseadas em dados

## 🏗️ Arquitetura

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Streamlit     │    │   FastAPI       │    │   LangChain     │
│   Web UI        │◄──►│   REST API      │◄──►│   AI Agent      │
│   (Porta 8501)  │    │   (Porta 8000)  │    │   + OpenAI      │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### 🔄 Fluxo de Dados

1. **Usuário** interage com interface Streamlit
2. **Streamlit** envia requisições para API FastAPI
3. **FastAPI** processa e roteia para controllers apropriados
4. **Controllers** chamam o agente LangChain
5. **LangChain** executa chains específicas e consulta OpenAI
6. **Resposta** retorna pela mesma cadeia até o usuário

## 🛠️ Tecnologias

### Backend
- **Python 3.11+** - Linguagem principal
- **FastAPI** - Framework web moderno e rápido
- **LangChain** - Framework para aplicações de IA
- **OpenAI GPT-3.5-turbo** - Modelo de linguagem

### Frontend
- **Streamlit** - Framework para aplicações web de dados
- **HTML/CSS/JavaScript** - Interface responsiva

### Infraestrutura
- **Docker** - Containerização
- **Docker Compose** - Orquestração de containers
- **Nginx** - Proxy reverso (opcional)

### Dependências Principais
```python
fastapi>=0.104.0
uvicorn>=0.24.0
langchain>=0.1.0
langchain-openai>=0.0.5
streamlit>=1.28.0
python-dotenv>=1.0.0
pydantic>=2.5.0
```

## 📦 Pré-requisitos

- **Docker** 20.10+
- **Docker Compose** 2.0+
- **Git** para clonar o repositório
- **Chave da API OpenAI** válida

## ⚡ Instalação Rápida

### 1. Clone o Repositório
```bash
git clone <seu-repositorio>
cd financial-analysis-agent
```

### 2. Configure as Variáveis de Ambiente
```bash
cp .env.example .env
# Edite o arquivo .env com sua chave da OpenAI
```

### 3. Execute o Deploy
```bash
chmod +x deploy.sh
./deploy.sh
```

### 4. Acesse as Aplicações
- **API**: http://localhost:8000
- **Web UI**: http://localhost:8501
- **Documentação API**: http://localhost:8000/docs

## 🔧 Configuração

### Arquivo .env
```bash
# OpenAI Configuration
OPENAI_API_KEY=sua_chave_api_aqui
OPENAI_MODEL=gpt-3.5-turbo
TEMPERATURE=0.7

# API Configuration
API_PORT=8000
API_HOST=0.0.0.0

# Web Configuration
WEB_PORT=8501
WEB_HOST=0.0.0.0

# Docker Network
NETWORK_NAME=financial-network
API_URL=http://financial-agent-api:8000
```

### Variáveis Importantes
- **`OPENAI_API_KEY`**: Sua chave da API OpenAI (obrigatória)
- **`TEMPERATURE`**: Criatividade das respostas (0.0 - 1.0)
- **`API_URL`**: URL da API para comunicação entre containers

## 📖 Como Usar

### 🌐 Interface Web (Recomendado)

1. Acesse http://localhost:8501
2. Selecione o tipo de análise desejado
3. Digite o código da ação (ex: PETR4, VALE3)
4. Clique em "Executar Análise"
5. Visualize os resultados detalhados

### 🔌 API REST

#### Análise Fundamentalista
```bash
curl -X POST "http://localhost:8000/analyze/fundamental" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "PETR4", "analysis_type": "análise fundamentalista"}'
```

#### Análise Técnica
```bash
curl -X POST "http://localhost:8000/analyze/technical" \
  -H "Content-Type: application/json" \
  -d '{"ticker": "VALE3"}'
```

#### Perguntas Gerais
```bash
curl -X POST "http://localhost:8000/agent/ask" \
  -H "Content-Type: application/json" \
  -d '{"question": "Como está o mercado hoje?"}'
```

## 🔌 API Endpoints

### 📊 Análises
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/analyze/fundamental` | Análise fundamentalista |
| `POST` | `/analyze/technical` | Análise técnica |
| `POST` | `/analyze/risk` | Análise de risco |
| `POST` | `/analyze/comprehensive` | Análise abrangente |

### 🤖 Agente
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `POST` | `/agent/ask` | Perguntas gerais |
| `GET` | `/agent/tools` | Ferramentas disponíveis |

### 🏥 Sistema
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| `GET` | `/health` | Status da API |
| `GET` | `/` | Informações do sistema |

## 🌐 Interface Web

### 🎨 Características
- **Interface Responsiva** para desktop e mobile
- **Dashboard Intuitivo** com métricas visuais
- **Múltiplos Tipos de Análise** em uma única interface
- **Histórico de Conversas** com o agente
- **Exportação de Resultados** (futuro)

### 📱 Seções Disponíveis
1. **Configurações** - Tipo de análise e parâmetros
2. **Análise de Ações** - Interface principal para análises
3. **Perguntas Gerais** - Chat com o agente de IA
4. **Resultados** - Visualização detalhada das análises

## 🐳 Docker

### 🏗️ Estrutura de Containers

```yaml
services:
  financial-agent-api:    # API FastAPI
    ports: "8000:8000"
    networks: financial-network

  financial-agent-web:    # Interface Streamlit
    ports: "8501:8500"
    networks: financial-network
    depends_on: financial-agent-api
```

### 🚀 Comandos Docker

```bash
# Iniciar todos os serviços
docker compose up -d

# Ver logs em tempo real
docker compose logs -f

# Parar todos os serviços
docker compose down

# Reconstruir containers
docker compose up -d --build

# Ver status dos serviços
docker compose ps
```

### 🔧 Comandos Úteis

```bash
# Acessar container da API
docker exec -it financial-agent-api bash

# Acessar container do Web
docker exec -it financial-agent-web bash

# Ver logs específicos
docker compose logs financial-agent-api
docker compose logs financial-agent-web
```

## 📁 Estrutura do Projeto

```
financial-analysis-agent/
├── 📁 api/                          # Serviço da API
│   ├── 📁 src/                      # Código fonte
│   │   ├── 📁 agents/               # Agentes de IA
│   │   ├── 📁 chains/               # Chains do LangChain
│   │   ├── 📁 controllers/          # Lógica de negócio
│   │   ├── 📁 core/                 # Configurações e cliente
│   │   ├── 📁 models/               # Modelos Pydantic
│   │   ├── 📁 prompts/              # Prompts do LangChain
│   │   ├── 📁 routers/              # Rotas da API
│   │   ├── 📁 tools/                # Ferramentas do agente
│   │   └── main.py                  # Aplicação principal
│   ├── 📁 tests/                    # Testes automatizados
│   ├── Dockerfile                   # Container da API
│   ├── docker-compose.yml           # Configuração Docker da API
│   └── requirements.txt             # Dependências Python
├── 📁 web/                          # Interface web
│   ├── 📁 src/                      # Código Streamlit
│   ├── Dockerfile                   # Container do Web
│   ├── docker-compose.yml           # Configuração Docker do Web
│   └── requirements.txt             # Dependências Python
├── 📁 docs/                         # Documentação
├── .env                             # Variáveis de ambiente
├── .gitignore                       # Arquivos ignorados pelo Git
├── docker-compose.yml               # Docker Compose principal
├── deploy.sh                        # Script de deploy
├── Makefile                         # Comandos úteis
└── README.md                        # Este arquivo
```

## 🧪 Testes

### 🚀 Executar Testes

```bash
# Testar configuração básica
python api/test_step1.py

# Testar chains e tools
python api/test_step2.py

# Testar agentes
python api/test_step3.py

# Testar API completa
curl http://localhost:8000/health
```

## 🚀 Deploy

### 🐳 Deploy Local com Docker

```bash
# Deploy completo
./deploy.sh

# Deploy manual
docker compose up -d --build
```

### ☁️ Deploy em Produção

1. **Configure variáveis de ambiente** para produção
2. **Ajuste configurações de segurança** (CORS, rate limiting)
3. **Configure domínio e SSL** se necessário
4. **Monitore logs e métricas** de performance

## 🤝 Contribuição

### 🚀 Como Contribuir

1. **Fork** o projeto
2. **Crie uma branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra um Pull Request**

### 📋 Padrões de Código

- **Python**: PEP 8, type hints, docstrings
- **Commits**: Conventional Commits
- **Documentação**: Markdown com exemplos
- **Testes**: Cobertura mínima de 80%

## 📄 Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<div align="center">

**⭐ Se este projeto te ajudou, considere dar uma estrela! ⭐**

*Desenvolvido com ❤️ e ☕*

</div>
