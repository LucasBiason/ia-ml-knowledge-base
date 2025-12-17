"""
Exercício 1: Criar Função de Busca
Referência: Tutorial 02 - Function Calling

Este script demonstra como implementar uma função de busca em um catálogo de produtos 
utilizando Function Calling da OpenAI. O modelo identifica a intenção de busca do usuário
e extrai os parâmetros necessários para consultar uma base de dados simulada.

Pontos principais:
1. Definição clara do JSON Schema para a função 'buscar_produtos'.
2. Tratamento do retorno da função para gerar uma resposta natural ao usuário.
3. Demonstração de como o modelo lida com consultas que exigem filtros específicos.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Base de dados simulada de produtos
CATALOGO = [
    {"id": 1, "nome": "Notebook Dell Inspiron", "categoria": "Informática", "preco": 4500.00, "estoque": 10},
    {"id": 2, "nome": "Mouse Logitech MX Master", "categoria": "Periféricos", "preco": 450.00, "estoque": 25},
    {"id": 3, "nome": "Monitor LG 27 UltraGear", "categoria": "Monitores", "preco": 1800.00, "estoque": 5},
    {"id": 4, "nome": "Teclado Mecânico Keychron", "categoria": "Periféricos", "preco": 850.00, "estoque": 15},
]

def buscar_produtos(termo=None, categoria=None):
    """Simula busca no banco de dados."""
    resultados = CATALOGO
    if categoria:
        resultados = [p for p in resultados if p['categoria'].lower() == categoria.lower()]
    if termo:
        resultados = [p for p in resultados if termo.lower() in p['nome'].lower()]
    return json.dumps(resultados)

def executar_busca_inteligente(pergunta):
    mensagens = [{"role": "user", "content": pergunta}]
    
    tools = [
        {
            "type": "function",
            "function": {
                "name": "buscar_produtos",
                "description": "Busca produtos no catálogo por nome ou categoria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "termo": {"type": "string", "description": "Termo de busca para o nome do produto"},
                        "categoria": {"type": "string", "description": "Categoria específica (ex: Informática, Periféricos)"}
                    }
                }
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=mensagens,
        tools=tools,
        tool_choice="auto"
    )

    response_message = response.choices[0].message
    tool_calls = response_message.tool_calls

    if tool_calls:
        mensagens.append(response_message)
        for tool_call in tool_calls:
            args = json.loads(tool_call.function.arguments)
            resultado = buscar_produtos(**args)
            mensagens.append({
                "tool_call_id": tool_call.id,
                "role": "tool",
                "name": "buscar_produtos",
                "content": resultado,
            })
        
        segunda_resposta = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens
        )
        return segunda_resposta.choices[0].message.content
    
    return response_message.content

if __name__ == "__main__":
    print("Iniciando assistente de vendas...")
    resposta = executar_busca_inteligente("Vocês têm algum monitor para games ou mouses da Logitech?")
    print(f"\nAssistente: {resposta}")

