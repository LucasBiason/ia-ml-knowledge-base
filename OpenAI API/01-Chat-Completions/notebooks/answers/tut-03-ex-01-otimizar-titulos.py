"""
Exercício 1: Otimizar Títulos de Artigos
Referência: Tutorial 03 - Parâmetros Avançados

Este script utiliza o parâmetro 'temperature' e 'n' para gerar múltiplas variações
de títulos para um artigo técnico, permitindo escolher a melhor opção entre
diferentes níveis de criatividade.

Configurações:
- temperature=0.8 para maior variedade.
- n=3 para gerar três opções distintas.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def gerar_titulos(tema):
    prompt = f"Gere um título atraente e profissional para um artigo sobre: {tema}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um redator especializado em tecnologia e SEO."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.8,
        n=3
    )
    
    return [choice.message.content for choice in response.choices]

if __name__ == "__main__":
    tema = "As vantagens de utilizar Function Calling na API da OpenAI"
    opcoes = gerar_titulos(tema)
    
    print(f"Sugestões de títulos para: {tema}\n")
    for i, titulo in enumerate(opcoes, 1):
        print(f"{i}. {titulo}")

