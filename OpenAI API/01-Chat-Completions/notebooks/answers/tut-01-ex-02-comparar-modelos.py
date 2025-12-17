"""
Exercício 2: Comparar Modelos
Referência: Tutorial 01 - Conversa Básica

Este script compara a saída de diferentes modelos da OpenAI para a mesma pergunta, 
permitindo visualizar as diferenças de estilo, detalhamento e custo entre versões.

Conceitos:
- Uso de diferentes nomes de modelos (gpt-3.5-turbo, gpt-4).
- Análise de respostas multimodais.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def comparar_modelos(pergunta):
    modelos = ["gpt-3.5-turbo", "gpt-4"]
    resultados = {}
    
    for modelo in modelos:
        print(f"Consultando modelo: {modelo}...")
        response = client.chat.completions.create(
            model=modelo,
            messages=[{"role": "user", "content": pergunta}]
        )
        resultados[modelo] = response.choices[0].message.content
        
    return resultados

if __name__ == "__main__":
    pergunta = "Explique brevemente o que é computação quântica."
    respostas = comparar_modelos(pergunta)
    
    for modelo, resposta in respostas.items():
        print(f"\n[{modelo.upper()}]:\n{resposta}\n" + "-"*30)

