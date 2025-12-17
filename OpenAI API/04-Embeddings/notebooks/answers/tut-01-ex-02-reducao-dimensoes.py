"""
Exercicio 2: Reducao de Dimensoes (Matryoshka Embeddings)
Referencia: Tutorial 01 - Vetorizacao de Texto

Este script demonstra como utilizar o recurso nativo de reducao de dimensionalidade dos 
modelos v3 da OpenAI, mantendo a eficiencia e reduzindo custos de armazenamento.

Pontos principais:
1. Uso do parametro 'dimensions' no endpoint de embeddings.
2. Comparacao de tamanho entre vetores originais e reduzidos.
3. Verificacao da estrutura do vetor resultante.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def comparar_dimensoes():
    texto = "Implementacao de busca semantica em sistemas de larga escala."
    modelo = "text-embedding-3-small"

    print(f"Texto: {texto}\n")

    # Caso 1: Dimensoes padrao (1536 para o small)
    emb_full = client.embeddings.create(
        model=modelo,
        input=texto
    ).data[0].embedding

    # Caso 2: Reducao para 256 dimensoes
    emb_reduced = client.embeddings.create(
        model=modelo,
        input=texto,
        dimensions=256
    ).data[0].embedding

    print(f"Dimensoes Original: {len(emb_full)}")
    print(f"Dimensoes Reduzido: {len(emb_reduced)}")
    print(f"Taxa de compactacao: {(1 - len(emb_reduced)/len(emb_full))*100:.1f}%")
    
    print("\nPrimeiros 5 valores (Reduzido):")
    print(emb_reduced[:5])

if __name__ == "__main__":
    comparar_dimensoes()

