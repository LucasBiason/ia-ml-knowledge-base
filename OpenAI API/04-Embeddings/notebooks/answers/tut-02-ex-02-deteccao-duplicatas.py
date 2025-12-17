"""
Exercicio 2: Deteccao de Duplicatas Semânticas
Referencia: Tutorial 02 - Busca Semantica Avançada

Este script identifica frases que possuem o mesmo significado, mesmo utilizando palavras 
diferentes, através do cálculo de similaridade coseno entre embeddings.

Pontos principais:
1. Geracao de embeddings para um conjunto de sentencas.
2. Calculo de produto escalar (dot product) para similaridade (vetores ja normalizados).
3. Identificacao de pares com similaridade superior a um limiar definido (ex: 0.9).
"""

import os
import numpy as np
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def detectar_duplicatas():
    frases = [
        "O dia esta muito bonito hoje.",
        "Hoje o tempo esta maravilhoso.",
        "O mercado financeiro caiu 2%.",
        "As acoes tiveram queda de 2 por cento na bolsa.",
        "Receita de pao caseiro simples.",
        "Como fazer pao em casa de forma facil."
    ]

    print("Gerando embeddings e analisando similaridades...\n")

    # 1. Gerar embeddings
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=frases
    )
    
    embeddings = [data.embedding for data in response.data]
    limiar = 0.85
    pares_encontrados = []

    # 2. Comparar todos os pares
    for i in range(len(embeddings)):
        for j in range(i + 1, len(embeddings)):
            # Similaridade coseno via produto escalar (OpenAI v3 ja normaliza)
            sim = np.dot(embeddings[i], embeddings[j])
            
            if sim > limiar:
                pares_encontrados.append((frases[i], frases[j], sim))

    # 3. Exibir resultados
    if not pares_encontrados:
        print("Nenhuma duplicata semantica encontrada.")
    else:
        print(f"Pares com similaridade > {limiar}:")
        for f1, f2, score in pares_encontrados:
            print(f"- [{score:.4f}]")
            print(f"  A: {f1}")
            print(f"  B: {f2}\n")

if __name__ == "__main__":
    detectar_duplicatas()

