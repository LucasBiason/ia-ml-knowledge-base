"""
Exercício 3: Sistema de Agendamento
Referência: Tutorial 02 - Function Calling

Demonstração de um sistema de agendamento automatizado onde o modelo interage com funções
para verificar disponibilidade e confirmar horários. Este padrão é essencial para criar
agentes de atendimento que realizam ações reais em sistemas externos.

Destaques:
1. Verificação de conflitos de horário.
2. Persistência simulada de compromissos.
3. Respostas contextuais baseadas no estado do calendário.
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Agenda simulada
AGENDA = [
    {"data": "2025-12-20", "hora": "14:00", "descricao": "Reunião de Equipe"},
    {"data": "2025-12-20", "hora": "16:00", "descricao": "Mentoria IA"}
]

def verificar_disponibilidade(data, hora):
    for compromisso in AGENDA:
        if compromisso['data'] == data and compromisso['hora'] == hora:
            return json.dumps({"disponivel": False, "mensagem": "Horário já ocupado."})
    return json.dumps({"disponivel": True, "mensagem": "Horário livre."})

def agendar_compromisso(data, hora, descricao):
    disponibilidade = json.loads(verificar_disponibilidade(data, hora))
    if disponibilidade['disponivel']:
        novo_evento = {"data": data, "hora": hora, "descricao": descricao}
        AGENDA.append(novo_evento)
        return json.dumps({"status": "sucesso", "evento": novo_evento})
    return json.dumps({"status": "erro", "mensagem": "Não foi possível agendar."})

def processar_agendamento(texto_usuario):
    mensagens = [
        {"role": "system", "content": "Você é um assistente de agendamentos. Hoje é 17 de Dezembro de 2025."},
        {"role": "user", "content": texto_usuario}
    ]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "verificar_disponibilidade",
                "description": "Verifica se um horário está disponível na agenda",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {"type": "string", "description": "Data no formato AAAA-MM-DD"},
                        "hora": {"type": "string", "description": "Hora no formato HH:MM"}
                    },
                    "required": ["data", "hora"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "agendar_compromisso",
                "description": "Cria um novo compromisso na agenda",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "data": {"type": "string", "description": "Data no formato AAAA-MM-DD"},
                        "hora": {"type": "string", "description": "Hora no formato HH:MM"},
                        "descricao": {"type": "string", "description": "Título do compromisso"}
                    },
                    "required": ["data", "hora", "descricao"]
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
        tools=tools
    )

    msg = response.choices[0].message
    if msg.tool_calls:
        mensagens.append(msg)
        for call in msg.tool_calls:
            args = json.loads(call.function.arguments)
            if call.function.name == "verificar_disponibilidade":
                res = verificar_disponibilidade(**args)
            else:
                res = agendar_compromisso(**args)
            
            mensagens.append({
                "tool_call_id": call.id,
                "role": "tool",
                "name": call.function.name,
                "content": res
            })
        
        final = client.chat.completions.create(model="gpt-3.5-turbo", messages=mensagens)
        return final.choices[0].message.content
    
    return msg.content

if __name__ == "__main__":
    print(processar_agendamento("Gostaria de agendar um café com o Lucas no dia 20 de dezembro às 15:00."))

