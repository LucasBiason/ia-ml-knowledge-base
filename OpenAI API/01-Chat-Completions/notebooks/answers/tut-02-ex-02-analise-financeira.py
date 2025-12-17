"""
Exercício 2: Análise Financeira
Referência: Tutorial 02 - Agentes Especializados

Criação de um analista financeiro virtual que interpreta indicadores básicos 
de uma empresa e fornece um parecer técnico resumido.

Destaques:
- Persona de analista de investimentos.
- Processamento de dados numéricos via prompt.
- Saída estruturada com recomendações.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def analisar_empresa(dados):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Você é um analista financeiro sênior. Forneça análises rápidas e objetivas."},
            {"role": "user", "content": f"Analise estes dados: {dados}"}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    dados = "Empresa X - Receita: 1M, Lucro: 200k, Dívida: 50k. Tendência de crescimento de 5% ao ano."
    print("Iniciando análise financeira...")
    print(f"\nParecer:\n{analisar_empresa(dados)}")

