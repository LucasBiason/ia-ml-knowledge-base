"""
Exercício 1: Assistente de Culinária
Referência: Tutorial 01 - Conversa Básica

Primeiro contato com a API de Chat Completions. Este script implementa um assistente 
básico que responde dúvidas de culinária, utilizando o modelo GPT para transformar 
ingredientes simples em sugestões de receitas.

Objetivo:
- Entender a estrutura básica de uma requisição de chat.
- Praticar o envio de mensagens 'user'.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def pedir_receita(ingredientes):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um chef de cozinha criativo que ajuda iniciantes."},
            {"role": "user", "content": f"Tenho estes ingredientes: {ingredientes}. O que posso cozinhar?"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    ingredientes = "ovos, queijo, pão e tomate"
    print(f"Ingredientes: {ingredientes}\n")
    print(f"Chef: {pedir_receita(ingredientes)}")

