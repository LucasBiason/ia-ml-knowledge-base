"""
Exercício 3: Sistema de Agendamento

Referência: 04-funcoes-function-calling.ipynb - Exercício 3

Descrição:
Implemente um sistema que permite ao modelo agendar eventos, verificando disponibilidade e criando compromissos.

Explicação:

Sistema de agendamento inteligente que permite ao modelo verificar disponibilidade e criar eventos.

Pontos importantes:

1. Gerenciamento de Estado:
   - Armazena eventos agendados
   - Verifica conflitos de horário
   - Mantém calendário organizado

2. Funções Múltiplas:
   - Verificar disponibilidade
   - Criar evento
   - Listar eventos
   - Cancelar evento

3. Aplicação Prática:
   - Assistente de agendamento
   - Sistema de reservas
   - Calendário inteligente
   - Agendamento de reuniões

4. Melhorias Possíveis:
   - Persistência em banco de dados
   - Notificações de eventos
   - Integração com calendários (Google, Outlook)
   - Validação de horários
   - Recorrência de eventos
"""

import os
import json
from datetime import datetime, timedelta
from typing import List, Dict
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Armazenamento de eventos (em produção, usar banco de dados)
eventos_agendados: List[Dict] = []

def verificar_disponibilidade(data: str, hora: str) -> str:
    """
    Verifica se há disponibilidade em uma data e hora específicas.
    
    Args:
        data: Data no formato YYYY-MM-DD
        hora: Hora no formato HH:MM
    
    Returns:
        str: Status da disponibilidade
    """
    horario_solicitado = f"{data} {hora}"
    
    for evento in eventos_agendados:
        if evento["data"] == data and evento["hora"] == hora:
            return f"Horário ocupado. Já existe evento '{evento['titulo']}' neste horário."
    
    return f"Horário disponível em {data} às {hora}"

def criar_evento(titulo: str, data: str, hora: str, descricao: str = "") -> str:
    """
    Cria um novo evento no calendário.
    
    Args:
        titulo: Título do evento
        data: Data no formato YYYY-MM-DD
        hora: Hora no formato HH:MM
        descricao: Descrição opcional do evento
    
    Returns:
        str: Confirmação de criação
    """
    # Verificar disponibilidade
    disponivel = verificar_disponibilidade(data, hora)
    if "ocupado" in disponivel.lower():
        return disponivel
    
    evento = {
        "titulo": titulo,
        "data": data,
        "hora": hora,
        "descricao": descricao
    }
    
    eventos_agendados.append(evento)
    return f"Evento '{titulo}' agendado para {data} às {hora}"

def listar_eventos(data: str = None) -> str:
    """
    Lista eventos agendados, opcionalmente filtrados por data.
    
    Args:
        data: Data para filtrar (opcional, formato YYYY-MM-DD)
    
    Returns:
        str: Lista de eventos formatada
    """
    eventos_filtrados = eventos_agendados
    
    if data:
        eventos_filtrados = [e for e in eventos_agendados if e["data"] == data]
    
    if not eventos_filtrados:
        if data:
            return f"Nenhum evento agendado para {data}"
        return "Nenhum evento agendado"
    
    resultado = f"Eventos agendados{' em ' + data if data else ''}:\n\n"
    for evento in eventos_filtrados:
        resultado += f"- {evento['titulo']}\n"
        resultado += f"  Data: {evento['data']} às {evento['hora']}\n"
        if evento.get('descricao'):
            resultado += f"  Descrição: {evento['descricao']}\n"
        resultado += "\n"
    
    return resultado.strip()

# Definir funções para o modelo
funcoes_agendamento = [
    {
        "type": "function",
        "function": {
            "name": "verificar_disponibilidade",
            "description": "Verifica se um horário está disponível para agendamento",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "Data no formato YYYY-MM-DD (ex: 2025-12-20)"
                    },
                    "hora": {
                        "type": "string",
                        "description": "Hora no formato HH:MM (ex: 14:30)"
                    }
                },
                "required": ["data", "hora"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "criar_evento",
            "description": "Cria um novo evento no calendário",
            "parameters": {
                "type": "object",
                "properties": {
                    "titulo": {
                        "type": "string",
                        "description": "Título do evento"
                    },
                    "data": {
                        "type": "string",
                        "description": "Data no formato YYYY-MM-DD"
                    },
                    "hora": {
                        "type": "string",
                        "description": "Hora no formato HH:MM"
                    },
                    "descricao": {
                        "type": "string",
                        "description": "Descrição opcional do evento"
                    }
                },
                "required": ["titulo", "data", "hora"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "listar_eventos",
            "description": "Lista eventos agendados, opcionalmente filtrados por data",
            "parameters": {
                "type": "object",
                "properties": {
                    "data": {
                        "type": "string",
                        "description": "Data para filtrar eventos (opcional, formato YYYY-MM-DD)"
                    }
                },
                "required": []
            }
        }
    }
]

mapeamento_agendamento = {
    "verificar_disponibilidade": verificar_disponibilidade,
    "criar_evento": criar_evento,
    "listar_eventos": listar_eventos
}

def processar_function_call(mensagens, funcoes, mapeamento_funcoes, max_iteracoes=5):
    """Processa function calls automaticamente."""
    iteracoes = 0
    
    while iteracoes < max_iteracoes:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            tools=funcoes,
            tool_choice="auto"
        )
        
        mensagem = response.choices[0].message
        mensagens.append(mensagem)
        
        if not mensagem.tool_calls:
            return mensagem.content
        
        for tool_call in mensagem.tool_calls:
            nome_funcao = tool_call.function.name
            argumentos = json.loads(tool_call.function.arguments)
            tool_call_id = tool_call.id
            
            if nome_funcao in mapeamento_funcoes:
                funcao = mapeamento_funcoes[nome_funcao]
                try:
                    resultado = funcao(**argumentos)
                except Exception as e:
                    resultado = f"Erro ao executar função: {e}"
            else:
                resultado = f"Função '{nome_funcao}' não encontrada"
            
            mensagens.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": nome_funcao,
                "content": str(resultado)
            })
        
        iteracoes += 1
    
    return "Número máximo de iterações atingido"

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 3: Sistema de Agendamento")
print("=" * 60)
print()

mensagens = [
    {
        "role": "system",
        "content": "Você é um assistente de agendamento que ajuda a gerenciar eventos e compromissos."
    },
    {
        "role": "user",
        "content": "Verifique se tenho disponibilidade amanhã às 14:00. Se sim, agende uma reunião de equipe para esse horário."
    }
]

# Usar data de amanhã (exemplo)
amanha = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

# Substituir "amanhã" pela data real
mensagens[1]["content"] = mensagens[1]["content"].replace("amanhã", amanha)

resposta = processar_function_call(
    mensagens=mensagens,
    funcoes=funcoes_agendamento,
    mapeamento_funcoes=mapeamento_agendamento
)

print(">> Resposta do assistente:")
print("-" * 60)
print(resposta)
print()

# Listar eventos criados
print(">> Eventos agendados:")
print("-" * 60)
print(listar_eventos())

