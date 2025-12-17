"""
Exercicio 1: Calculadora de Tokens de Visao
Referencia: Tutorial 03 - Configuracoes de Detalhamento

Este script implementa a lógica oficial da OpenAI para o cálculo de tokens consumidos 
por imagens nos modos 'low' e 'high' resolution.

Pontos principais:
1. Calculo do modo 'low' (custo fixo).
2. Algoritmo de tiling para o modo 'high'.
3. Estimativa de custo baseada na resolucao (Largura x Altura).
"""

import math

def calcular_tokens_visao(largura, altura, detalhe="high"):
    if detalhe == "low":
        return 85

    # 1. Redimensionar para caber em 2048x2048 (mantendo aspect ratio)
    if largura > 2048 or altura > 2048:
        proporcao = 2048 / max(largura, altura)
        largura = int(largura * proporcao)
        altura = int(altura * proporcao)

    # 2. Redimensionar o lado menor para 768
    proporcao_menor = 768 / min(largura, altura)
    largura = int(largura * proporcao_menor)
    altura = int(altura * proporcao_menor)

    # 3. Calcular numero de tiles de 512x512
    tiles_largura = math.ceil(largura / 512)
    tiles_altura = math.ceil(altura / 512)
    total_tiles = tiles_largura * tiles_altura

    # 4. Custo total = (170 * numero de tiles) + 85 (custo base)
    total_tokens = (170 * total_tiles) + 85
    return total_tokens

if __name__ == "__main__":
    # Teste com diferentes resolucoes
    testes = [
        (1024, 1024),  # Padrao
        (1920, 1080),  # Full HD
        (4096, 2160),  # 4K
    ]

    print("Estimativa de Custo em Tokens (Modo High):\n")
    for w, h in testes:
        tokens = calcular_tokens_visao(w, h)
        print(f"Resolucao {w}x{h} px -> {tokens} tokens")
    
    print(f"\nQualquer resolucao no modo 'low' -> {calcular_tokens_visao(800, 600, 'low')} tokens")

