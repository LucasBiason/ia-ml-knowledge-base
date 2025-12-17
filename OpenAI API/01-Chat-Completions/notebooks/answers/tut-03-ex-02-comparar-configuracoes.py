"""
Exercício 2: Comparar Configurações
Referência: Tutorial 03 - Parâmetros Avançados

Script experimental para testar o efeito da 'temperature' e 'top_p' na geração de texto.
Comparamos um texto altamente determinístico (baixa temperature) com um texto 
criativo e imprevisível.

Variáveis testadas:
- Caso 1: temperature=0 (Fatos, precisão).
- Caso 2: temperature=1.5 (Criatividade, poesia).
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def testar_configuracoes(tema):
    configs = [
        {"name": "Determinístico", "temp": 0.0},
        {"name": "Criativo", "temp": 1.2}
    ]
    
    for conf in configs:
        print(f"\n--- Modo: {conf['name']} (Temp: {conf['temp']}) ---")
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Escreva um parágrafo sobre: {tema}"}],
            temperature=conf['temp']
        )
        print(response.choices[0].message.content)

if __name__ == "__main__":
    testar_configuracoes("A vida em Marte no futuro")

