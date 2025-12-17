"""
Exercicio 2: Fluxo de Refinamento (DALL-E 3 para DALL-E 2)
Referencia: Tutorial 02 - Variacoes de Imagem

Este script implementa um fluxo de trabalho onde uma imagem base e gerada em alta qualidade
com o DALL-E 3 e, em seguida, sao criadas variacoes visuais utilizando o DALL-E 2.

Pontos principais:
1. Geracao inicial com DALL-E 3.
2. Download e preparacao do arquivo para o endpoint de variacoes.
3. Geracao de multiplas versoes inspiradas na base original.
"""

import os
import requests
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

OUTPUT_DIR = Path('../outputs')
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def fluxo_refinamento():
    # Passo 1: Gerar base com DALL-E 3
    print("Gerando imagem base com DALL-E 3...")
    base_prompt = "Um robo jardineiro cuidando de plantas fluorescentes em uma cupula em Marte."
    
    res_base = client.images.generate(
        model="dall-e-3",
        prompt=base_prompt,
        size="1024x1024"
    )
    
    url_base = res_base.data[0].url
    img_bytes = requests.get(url_base).content
    
    path_base = OUTPUT_DIR / "base_refinamento.png"
    path_base.write_bytes(img_bytes)
    print(f"Base salva em: {path_base}")

    # Passo 2: Gerar variacoes com DALL-E 2
    print("\nGerando variacoes com DALL-E 2...")
    with open(path_base, "rb") as image_file:
        res_variations = client.images.create_variation(
            model="dall-e-2",
            image=image_file,
            n=2,
            size="1024x1024"
        )
    
    for idx, data in enumerate(res_variations.data):
        var_bytes = requests.get(data.url).content
        path_var = OUTPUT_DIR / f"variacao_refinada_{idx+1}.png"
        path_var.write_bytes(var_bytes)
        print(f"Variacao {idx+1} salva em: {path_var}")

if __name__ == "__main__":
    fluxo_refinamento()

