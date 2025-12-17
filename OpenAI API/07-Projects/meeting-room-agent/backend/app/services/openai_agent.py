import json
from openai import OpenAI
from app.core.config import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_room_management_tools():
    """
    Retorna a definicao das ferramentas disponiveis para o assistente.
    """
    return [
        {
            "type": "function",
            "function": {
                "name": "listar_salas",
                "description": "Retorna uma lista de todas as salas de reuniao disponiveis no escritorio e suas capacidades.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "reservar_sala",
                "description": "Cria uma reserva de sala de reuniao para um usuario em um horario especifico.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sala": {"type": "string", "description": "Nome da sala (ex: Alpha, Beta, Gamma)"},
                        "data": {"type": "string", "description": "Data no formato AAAA-MM-DD"},
                        "hora_inicio": {"type": "string", "description": "Horario de inicio (HH:MM)"},
                        "duracao_minutos": {"type": "integer", "description": "Duracao da reuniao em minutos"},
                        "usuario": {"type": "string", "description": "Nome do solicitante"}
                    },
                    "required": ["sala", "data", "hora_inicio", "duracao_minutos", "usuario"]
                }
            }
        }
    ]

async def process_chat_message(messages):
    """
    Processa uma mensagem do usuario utilizando Function Calling.
    """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=get_room_management_tools(),
        tool_choice="auto"
    )
    
    return response.choices[0].message

