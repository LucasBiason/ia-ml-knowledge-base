"""
Exercício 3: Controlar Tamanho da Resposta
Referência: Tutorial 01 - Conversa Básica

Demonstração de como utilizar instruções no prompt e parâmetros simples para 
limitar a verbosidade do modelo, garantindo respostas diretas e concisas.

Prática:
- Instruções de sistema para restrição de tamanho.
- Uso de mensagens 'system' para definir o tom da conversa.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def responder_conciso(tema):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um assistente que responde tudo em no máximo 2 frases curtas."},
            {"role": "user", "content": f"Explique o que é: {tema}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    tema = "Fotossíntese"
    print(f"Tema: {tema}")
    print(f"Resposta: {responder_conciso(tema)}")

