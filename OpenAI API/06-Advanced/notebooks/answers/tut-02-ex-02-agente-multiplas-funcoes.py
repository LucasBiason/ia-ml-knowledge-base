"""
Exercício 2: Agente com Múltiplas Funções
Referência: Tutorial 02 - Function Calling

Este script implementa um agente capaz de lidar com múltiplas ferramentas em uma única interação.
O assistente pode realizar cálculos matemáticos e converter moedas simultaneamente, escolhendo
as ferramentas corretas baseadas na ferramentas corretas baseadas na necessidade do usuário.

Fluxo implementado:
1. Definição de ferramentas para cálculo e conversão.
2. Lógica de processamento sequencial de chamadas de função.
3. Integração de resultados para uma resposta final consolidada.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def calcular(expressao):
    try:
        # Nota: Em produção, use um parser seguro em vez de eval
        return str(eval(expressao))
    except Exception as e:
        return f"Erro no cálculo: {str(e)}"

def converter_moeda(valor, de="USD", para="BRL"):
    taxas = {"USD": 1.0, "BRL": 5.0, "EUR": 0.92}
    if de in taxas and para in taxas:
        resultado = valor * (taxas[para] / taxas[de])
        return f"{valor} {de} equivale a {resultado:.2f} {para}"
    return "Taxa de conversão não disponível."

def processar_solicitacao_complexa(pergunta):
    mensagens = [{"role": "user", "content": pergunta}]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "calcular",
                "description": "Realiza operações matemáticas",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "expressao": {"type": "string", "description": "Expressão matemática (ex: 2 + 2)"}
                    },
                    "required": ["expressao"]
                }
            }
        },
        {
            "type": "function",
            "function": {
                "name": "converter_moeda",
                "description": "Converte valores entre moedas (USD, BRL, EUR)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "valor": {"type": "number", "description": "Valor numérico"},
                        "de": {"type": "string", "description": "Moeda de origem"},
                        "para": {"type": "string", "description": "Moeda de destino"}
                    },
                    "required": ["valor"]
                }
            }
        }
    ]

    mapeamento = {
        "calcular": calcular,
        "converter_moeda": converter_moeda
    }

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
        tools=tools
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        mensagens.append(response_message)
        for tool_call in tool_calls:
            nome_funcao = tool_call.function.name
            funcao = mapeamento.get(nome_funcao)
            args = json.loads(tool_call.function.arguments)
            
            resultado = funcao(**args)
            mensagens.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": nome_funcao,
                "content": resultado,
            })
        
        final_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens
        )
        return final_response.choices[0].message.content
    
    return response_message.content

if __name__ == "__main__":
    pergunta = "Quanto é 1500 + 350? E quanto esse total seria em Euros se o valor original for em Dólares?"
    print(f"Usuário: {pergunta}")
    print(f"Agente: {processar_solicitacao_complexa(pergunta)}")

