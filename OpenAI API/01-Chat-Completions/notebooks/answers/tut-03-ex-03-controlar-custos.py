"""
Exercício 3: Controlar Custos
Referência: Tutorial 03 - Parâmetros Avançados

Este exercício foca no parâmetro 'max_tokens' para controlar rigorosamente o uso
de recursos e custos da API, evitando que o modelo gere respostas excessivamente
longas que consumam créditos desnecessários.

Conceitos:
- Uso de max_tokens para truncamento seguro.
- Estimativa de uso de tokens.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def consulta_economica(pergunta):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": pergunta}],
        max_tokens=50 # Limite severo para economia
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    pergunta = "Descreva a história da inteligência artificial desde 1950."
    print("Enviando pergunta longa com limite de tokens...")
    print(f"\nResposta truncada:\n{consulta_economica(pergunta)}")

