# Projects - Casos de Uso Reais e Integracoes

Esta secao consolida o conhecimento adquirido nos modulos anteriores atraves da construcao de projetos de ponta a ponta. O foco e a aplicacao pratica das APIs da OpenAI em arquiteturas de software modernas, integrando backends robustos e frontends interativos.

---

## Projetos Disponiveis

### 1. Chat Multimodal (Next.js + FastAPI)
**Diretorio:** `chat-multimodal/`

Um sistema de chat completo que permite a interacao via texto, imagem e audio.
- **Backend**: FastAPI com suporte a streaming (SSE) e persistencia em PostgreSQL.
- **Frontend**: Next.js 14 com TailwindCSS e componentes Shadcn/ui.
- **Integracoes**: GPT-4o (Chat/Vision) e Whisper (Audio).

---

### 2. Agente de Agendamento Inteligente (FastAPI + Function Calling)
**Diretorio:** `meeting-room-agent/` (Em implementacao)

Uma API especializada no gerenciamento de salas de reuniao atraves de linguagem natural.
- **Core**: Uso intensivo de **Function Calling** para interacao com banco de dados.
- **Backend**: FastAPI com SQLAlchemy para persistencia de reservas.
- **Interface**: Chat minimalista para realizacao de consultas e agendamentos.
- **Diferencial**: Lógica de verificacao de conflitos de horario via LLM e Python.

---

## Sugestoes de Expansao (Roadmap)

1. **Analisador de Documentos Fiscais (Vision + Embeddings)**:
   - Pipeline para extrair dados de notas fiscais e realizar busca semantica sobre o historico de gastos.
2. **Assistente de Suporte RAG (Embeddings + Vector DB)**:
   - Implementacao de uma base de conhecimento local (markdown) consultada por similaridade vetorial antes da geracao de resposta.
3. **Automacao de Atas de Reuniao (Whisper + GPT-4)**:
   - Sistema que recebe o audio de uma reuniao, identifica locutores e gera um resumo estruturado com tarefas atribuidas.

---

## Padroes de Desenvolvimento

Todos os projetos nesta pasta seguem as melhores praticas de engenharia de software:
- **Modularizacao**: Separacao clara entre lógica de negocio, schemas e rotas.
- **Seguranca**: Uso de variaveis de ambiente e validacao de inputs.
- **Escalabilidade**: Preparado para execucao via Docker e conteinerizacao.

