# OpenAI API - Base de Conhecimento Completa

Base de conhecimento completa e didática sobre a API da OpenAI, consolidando materiais de cursos (FIAP, PyCodeBR, Udemy, Alura) em tutoriais estruturados e profissionais.

---

## 📚 Estrutura do Conteúdo

![Infográfico: Arquitetura Geral da OpenAI API](assets/imagens/tutorials/arquitetura-openai-api.png)

### 00 - Fundamentos
Documentação teórica sobre OpenAI, arquitetura da API e conceitos fundamentais.

**Conteúdo:**
- Introdução à OpenAI
- Arquitetura da API
- Autenticação e Segurança

---

### 01 - Chat Completions
Tutoriais completos sobre a API de Chat Completions (GPT-3.5, GPT-4).

**Tutoriais:**
1. [Conversa Básica](01-Chat-Completions/notebooks/01-conversa-basica.ipynb) - Fundamentos
2. [Agentes Especializados](01-Chat-Completions/notebooks/02-agentes-especializados.ipynb) - Role system e contexto
3. [Parâmetros Avançados](01-Chat-Completions/notebooks/03-parametros-avancados.ipynb) - Temperature, max_tokens, etc.
4. [Function Calling](01-Chat-Completions/notebooks/04-funcoes-function-calling.ipynb) - Integração com funções (Em breve)

**Nota:** Para extração de dados JSON integrando múltiplas APIs, veja [06-Advanced/01-Extração de Dados JSON](06-Advanced/notebooks/01-extracao-dados-json.ipynb).

**Ver:** [README da Seção](01-Chat-Completions/README.md)

---

### 02 - Image Generation
Tutoriais sobre geração de imagens com DALL-E.

**Tutoriais:**
1. [DALL-E Básico](02-Image-Generation/notebooks/01-dalle-basico.ipynb) - Geração básica
2. [Variações de Imagem](02-Image-Generation/notebooks/02-dalle-variacoes.ipynb) - Múltiplas imagens
3. [Edição de Imagens](02-Image-Generation/notebooks/03-dalle-edicao.ipynb) - Editar imagens (Em breve)

**Ver:** [README da Seção](02-Image-Generation/README.md)

---

### 03 - Audio
Tutoriais sobre Text-to-Speech e Speech-to-Text.

**Tutoriais:**
1. [Text-to-Speech](03-Audio/notebooks/01-text-to-speech.ipynb) - Converter texto em áudio
2. [Speech-to-Text](03-Audio/notebooks/02-speech-to-text.ipynb) - Transcrever áudio
3. [Tradução de Áudio](03-Audio/notebooks/03-traducao-audio.ipynb) - Transcrever e traduzir

**Ver:** [README da Seção](03-Audio/README.md)

---

### 04 - Embeddings
Tutoriais sobre vetorização de texto e busca semântica.

**Tutoriais:**
1. [Vetorização de Texto](04-Embeddings/notebooks/01-vetorizacao-texto.ipynb) - Criar embeddings
2. [Busca Semântica](04-Embeddings/notebooks/02-busca-semantica.ipynb) - Buscar documentos similares (Em breve)

**Ver:** [README da Seção](04-Embeddings/README.md)

---

### 05 - Vision
Tutoriais sobre análise de imagens com GPT-4 Vision.

**Tutoriais:**
1. [Análise de Imagens](05-Vision/notebooks/01-analise-imagens.ipynb) - GPT-4 Vision (Em breve)
2. [Extração de Texto](05-Vision/notebooks/02-extracao-texto-imagens.ipynb) - OCR com Vision (Em breve)

---

### 06 - Advanced
Tópicos avançados e integração de múltiplas APIs.

**Tutoriais:**
1. [Extração de Dados JSON](06-Advanced/notebooks/01-extracao-dados-json.ipynb) - Integração Chat + Vision + Audio
2. [Streaming de Respostas](06-Advanced/notebooks/02-streaming-responses.ipynb) - Respostas em tempo real (Em breve)
3. [Processamento em Lote](06-Advanced/notebooks/03-batch-processing.ipynb) - Batch processing (Em breve)
4. [Fine-Tuning](06-Advanced/notebooks/04-fine-tuning.ipynb) - Fine-tuning de modelos (Em breve)

**Ver:** [README da Seção](06-Advanced/README.md)

---

### 07 - Projects
Projetos completos integrando múltiplas APIs.

**Projetos:**
- [Chat Multimodal](07-Projects/chat-multimodal/) - Chat completo com texto, imagens e áudio (Em desenvolvimento)

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
pip install openai python-dotenv
```

### 2. Configurar API Key

Crie um arquivo `.env` na raiz desta pasta:

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
2. **01-Chat-Completions/01** - Conversa básica
3. **01-Chat-Completions/02** - Agentes especializados
4. **02-Image-Generation/01** - DALL-E básico
5. **03-Audio/01** - Text-to-Speech

### Intermediário
6. **01-Chat-Completions/03** - Parâmetros avançados
7. **03-Audio/02** - Speech-to-Text
8. **04-Embeddings/01** - Vetorização de texto
9. **06-Advanced/01** - Extração de dados JSON (integração múltiplas APIs)

### Avançado
10. **01-Chat-Completions/04** - Function Calling (Em breve)
11. **05-Vision** - Análise de imagens
12. **06-Advanced** - Tópicos avançados
13. **07-Projects** - Projetos completos

---

## 📚 Documentação Teórica

- [Artigo Teórico Completo](docs/ARTIGO_TEORICO_OPENAI.md) - Visão geral completa sobre OpenAI
- [Infográficos](docs/INFOGRAFICOS/) - Diagramas e visualizações
- [Glossário](docs/GLOSSARIO.md) - Termos técnicos explicados

---

## 🎯 Casos de Uso Práticos

### Chat Completions
- Chatbots e assistentes virtuais
- Análise de dados e relatórios
- Extração de informações
- Geração de conteúdo
- Tradução e sumarização

### Image Generation
- Criação de imagens para marketing
- Ilustrações para conteúdo
- Geração de thumbnails
- Prototipagem visual

### Audio
- Narração de conteúdo
- Assistente de voz
- Acessibilidade (texto para fala)
- Transcrição de reuniões
- Legendagem automática

### Embeddings
- Busca semântica
- FAQ inteligente
- Recomendação de conteúdo
- Clustering de texto

---

## 💰 Custos e Limitações

### Chat Completions
- **GPT-3.5-turbo**: ~$0.50 por 1M tokens de entrada, ~$1.50 por 1M tokens de saída
- **GPT-4**: Mais caro, verifique preços atualizados

### Image Generation
- **DALL-E 3 Standard**: $0.04 por imagem (1024x1024)
- **DALL-E 3 HD**: $0.08 por imagem (1024x1024)
- **DALL-E 2**: $0.02 por imagem (1024x1024)

### Audio
- **TTS-1**: $15 por milhão de caracteres
- **TTS-1-HD**: $30 por milhão de caracteres
- **Whisper**: $0.006 por minuto de áudio

### Embeddings
- **text-embedding-3-small**: $0.02 por 1M tokens
- **text-embedding-3-large**: $0.13 por 1M tokens

**Nota:** Preços podem variar. Consulte [pricing oficial](https://openai.com/pricing) para valores atualizados.

---

## 🔗 Referências

### Documentação Oficial
- [OpenAI Platform](https://platform.openai.com/)
- [API Reference](https://platform.openai.com/docs/api-reference)
- [Guia de Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)

### Recursos Adicionais
- [OpenAI Cookbook](https://cookbook.openai.com/)
- [Community Forum](https://community.openai.com/)

---

## 📝 Contribuindo

Este é um projeto de conhecimento pessoal consolidando materiais de cursos. Sinta-se livre para usar e adaptar conforme necessário.

---

## 📄 Licença

Este projeto faz parte do repositório [ia-ml-knowledge-base](https://github.com/LucasBiason/ia-ml-knowledge-base) e está licenciado sob MIT.

---

**Última atualização:** Dezembro 2025
**Status:** Em desenvolvimento ativo
