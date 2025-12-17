"""
Exercício 1: Agente de Recomendações
Referência: Tutorial 02 - Agentes Especializados

Script que configura um agente especializado em cinema para recomendar filmes
com base no perfil do usuário. O diferencial é o uso da role 'system' para
estabelecer uma personalidade e base de conhecimento específica.

Principais características:
1. Personalidade de crítico de cinema definida.
2. Uso de contexto estruturado para guiar as sugestões.
3. Explicação didática do porquê de cada recomendação.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def recomendar_filmes(gosto_usuario):
    # Contexto simulado de filmes disponíveis
    catalogo = "Duna (Ficção Científica), Oppenheimer (Drama), Top Gun: Maverick (Ação), Soul (Animação)"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": f"Você é um crítico de cinema experiente. Seu catálogo atual é: {catalogo}. Sempre seja cordial e justifique suas escolhas."
            },
            {"role": "user", "content": f"Gosto de filmes assim: {gosto_usuario}. O que você me sugere?"}
        ],
        temperature=0.7
    )
    
    return response.choices[0].message.content

if __name__ == "__main__":
    preferencia = "filmes de drama históricos que prendem a atenção"
    print(f"Usuário: {preferencia}")
    print(f"Crítico: {recomendar_filmes(preferencia)}")

