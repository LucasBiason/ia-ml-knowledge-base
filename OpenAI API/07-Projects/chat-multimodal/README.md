# Chat Multimodal - Projeto de Integracao

Este projeto consiste em um sistema de comunicacao multimodal que integra capacidades de processamento de texto, imagem e audio utilizando a API da OpenAI. A arquitetura e composta por um backend escalavel em FastAPI e um frontend moderno em Next.js.

---

## Arquitetura do Sistema

### Backend (FastAPI)
- **Framework**: FastAPI (Python 3.10+).
- **Padrao de Projeto**: Pseudo 3-tier (API -> Services -> Repositories).
- **Autenticacao**: Implementacao de JWT (JSON Web Token).
- **Banco de Dados**: PostgreSQL para armazenamento de usuarios e historico de conversas.
- **Cache**: Redis para gerenciamento de sessoes e estados temporarios.
- **Streaming**: Uso de Server-Sent Events (SSE) para respostas em tempo real.

### Frontend (Next.js)
- **Framework**: Next.js 14 (App Router).
- **Linguagem**: TypeScript em modo estrito.
- **Estilizacao**: TailwindCSS para design responsivo.
- **Gerenciamento de Estado**: React Query (servidor) e Zustand (cliente).
- **Componentes**: Interface construida com Shadcn/ui.

---

## Funcionalidades Implementadas

1. **Comunicacao Textual**: Conversas contextuais com persistencia de historico e streaming de tokens.
2. **Processamento Visual**: Upload de imagens para analise via GPT-4o, incluindo OCR e descricao de cenarios.
3. **Processamento de Audio**: Transcricao de arquivos de voz utilizando o modelo Whisper-1.
4. **Seguranca**: Fluxo completo de registro, login e protecao de rotas via middleware de autenticacao.

---

## Estrutura de Diretorios

```text
chat-multimodal/
├── backend/
│   ├── app/
│   │   ├── api/          # Definição de endpoints (v1)
│   │   ├── services/     # Lógica de negócio e integração OpenAI
│   │   ├── repositories/ # Camada de acesso a dados
│   │   ├── schemas/      # Modelos Pydantic para validação
│   │   ├── models/       # Modelos SQLAlchemy (ORM)
│   │   ├── core/         # Configurações globais e segurança
│   │   └── middleware/   # Filtros de autenticação e logs
│   ├── tests/            # Testes unitários e de integração
│   └── requirements.txt  # Dependências do backend
├── frontend/
│   ├── src/
│   │   ├── app/          # Páginas e rotas (App Router)
│   │   ├── components/   # Componentes React reutilizáveis
│   │   ├── hooks/        # Hooks customizados
│   │   ├── services/     # Cliente de integração com a API
│   │   └── types/        # Definições de tipos TypeScript
│   └── package.json      # Dependências do frontend
└── docker-compose.yml    # Orquestração de containers (App, DB, Redis)
```

---

## Instrucoes de Configuracao

### Backend
1. Navegue ate o diretorio `backend`.
2. Crie e ative um ambiente virtual: `python -m venv .venv && source .venv/bin/activate`.
3. Instale as dependencias: `pip install -r requirements.txt`.
4. Configure as variaveis de ambiente no arquivo `.env`.

### Frontend
1. Navegue ate o diretorio `frontend`.
2. Instale as dependencias: `npm install`.
3. Inicie o servidor de desenvolvimento: `npm run dev`.

---

## Referencias Tecnicas

- Documentacao FastAPI
- Next.js Documentation
- OpenAI API Reference
