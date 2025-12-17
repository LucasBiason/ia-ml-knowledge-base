"""
Exercício 3: Integração com Dados Reais
Referência: Tutorial 02 - Agentes Especializados

Demonstração de como carregar um arquivo externo (CSV) e injetar seu conteúdo 
no contexto da mensagem 'system' para que o agente possa responder dúvidas 
específicas sobre uma base de conhecimento dinâmica.

Pontos principais:
1. Leitura de arquivo local (assets/produtos.csv).
2. Transformação de dados tabulares em texto para o contexto.
3. Agente de atendimento baseado em inventário real.
"""

import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI
from pathlib import Path

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def carregar_dados_produtos():
    caminho_csv = Path(__file__).parent.parent / "assets" / "produtos.csv"
    if not caminho_csv.exists():
        return "Catálogo vazio ou não encontrado."
    
    df = pd.read_csv(caminho_csv)
    return df.to_string(index=False)

def consultar_vendedor(pergunta):
    contexto = carregar_dados_produtos()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": f"Você é um vendedor de loja de hardware. Use este estoque para responder:\n{contexto}"
            },
            {"role": "user", "content": pergunta}
        ]
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    pergunta = "Quais mouses vocês têm disponíveis e quais os preços?"
    print(f"Dúvida: {pergunta}\n")
    print(f"Vendedor: {consultar_vendedor(pergunta)}")

