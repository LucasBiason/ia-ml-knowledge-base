# Agente de Agendamento Inteligente - Meeting Room Agent

Este projeto demonstra a criacao de um assistente virtual especializado no agendamento e gerenciamento de salas de reuniao utilizando **Function Calling**. O sistema permite que usuarios consultem disponibilidade e reservem espacos atraves de linguagem natural.

---

## Arquitetura e Tecnologias

### Backend (FastAPI)
- **Engine**: FastAPI para alta performance e documentacao automatica.
- **ORM**: SQLAlchemy para interacao com o banco de dados SQLite/PostgreSQL.
- **LLM Integracao**: OpenAI SDK com foco em definicao de ferramentas (`tools`).
- **Logica de Negocio**: Camada de servicos para validacao de horarios e regras de reserva.

### Frontend (Next.js)
- **Interface**: Chat minimalista focado na experiencia do usuario.
- **Framework**: Next.js 14 com App Router.
- **Estilizacao**: TailwindCSS.

---

## Fluxo de Funcionamento (Function Calling)

1. O usuario digita: *"Quero reservar a Sala Alpha para amanha as 14h por uma hora"*.
2. O backend envia a mensagem para a OpenAI junto com a definicao da funcao `reservar_sala`.
3. O modelo identifica os parametros: `sala="Alpha"`, `data="2025-12-18"`, `hora="14:00"`, `duracao=60`.
4. O backend executa a funcao Python, verifica conflitos no banco de dados e retorna o status.
5. O modelo gera uma confirmacao amigavel para o usuario.

---

## Estrutura de Ferramentas (Tools)

O agente possui acesso as seguintes capacidades:
- `listar_salas()`: Retorna os nomes e capacidades das salas disponiveis.
- `verificar_disponibilidade(sala, data)`: Consulta horarios livres para uma sala especifica.
- `reservar_sala(sala, data, hora, duracao)`: Cria um novo registro de reserva no sistema.
- `cancelar_reserva(reserva_id)`: Remove um agendamento existente.

---

## Estrutura do Projeto

```text
meeting-room-agent/
├── backend/
│   ├── app/
│   │   ├── api/v1/       # Endpoints de chat e salas
│   │   ├── core/         # Configurações e cliente OpenAI
│   │   ├── models/       # Modelos de dados (Room, Booking)
│   │   ├── schemas/      # Schemas Pydantic
│   │   └── services/     # Lógica de agendamento e Tool Calls
│   └── main.py           # Ponto de entrada da aplicação
├── frontend/
│   └── src/              # Interface de chat
└── README.md
```

---

## Proximos Passos de Implementacao

1. Definicao dos modelos de banco de dados (SQLAlchemy).
2. Implementacao do wrapper de Function Calling no backend.
3. Criacao da interface de chat no frontend.
4. Testes de integracao com cenarios de conflito de horario.

