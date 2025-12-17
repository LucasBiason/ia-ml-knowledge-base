# Chat Multimodal - Projeto Completo

Projeto completo de chat multimodal integrando texto, imagens e áudio usando OpenAI API.

## Arquitetura

### Backend (FastAPI)
- **Framework**: FastAPI
- **Arquitetura**: Pseudo 3-tier (api → services → repositories)
- **Autenticação**: JWT
- **Banco de Dados**: PostgreSQL (usuários e histórico)
- **Cache**: Redis (sessões)
- **Streaming**: Server-Sent Events (SSE)

### Frontend (Next.js)
- **Framework**: Next.js 14+ (App Router)
- **TypeScript**: Strict mode
- **Estilização**: TailwindCSS
- **Estado**: React Query (server) + Zustand (client)
- **Componentes**: Shadcn/ui

## Funcionalidades

### Chat de Texto
- Conversas com contexto
- Histórico de mensagens
- Streaming de respostas

### Upload de Imagens
- Análise com GPT-4 Vision
- OCR (extração de texto)
- Descrição de imagens

### Upload de Áudio
- Transcrição com Whisper
- Análise de conteúdo
- Conversão para texto

### Autenticação
- Registro e login
- JWT tokens
- Refresh tokens
- Proteção de rotas

## Estrutura do Projeto

```
chat-multimodal/
├── backend/
│   ├── app/
│   │   ├── api/          # Routers (endpoints)
│   │   ├── services/     # Business logic
│   │   ├── repositories/ # Data access
│   │   ├── schemas/      # Pydantic models
│   │   ├── models/       # Database models
│   │   ├── core/         # Config, deps
│   │   └── middleware/   # Auth, logging
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── app/          # App Router
│   │   ├── components/  # React components
│   │   ├── hooks/        # Custom hooks
│   │   ├── services/     # API client
│   │   └── types/        # TypeScript types
│   └── package.json
└── docker-compose.yml
```

## Setup

### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Frontend
```bash
cd frontend
npm install
```

## Status

🚧 **Em desenvolvimento**

---

**Próximos passos:**
- Implementar backend FastAPI
- Implementar frontend Next.js
- Integração completa OpenAI
- Testes e documentação





