"""
Exercicio 1: Gerar Thumbnail de Artigo
Referencia: Tutorial 01 - DALL-E Basico

Este script demonstra como gerar uma imagem em formato wide (1792x1024) para ser utilizada
como capa de um artigo tecnico sobre Inteligencia Artificial.

Pontos principais:
1. Configuracao de proporcao (size='1792x1024').
2. Uso de estilo detalhado no prompt para contexto de IA.
3. Persistencia automatica do resultado.
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

def gerar_thumbnail_artigo():
    prompt = (
        "Uma ilustracao digital futurista e minimalista para a capa de um blog de tecnologia. "
        "O tema e a evolucao da Inteligencia Artificial, mostrando conexoes neurais brilhantes, "
        "circuitos integrados e uma paleta de cores azul e violeta. "
        "Estilo limpo, alta definicao, cinematico."
    )

    try:
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size="1792x1024",
            quality="standard",
            n=1
        )

        image_url = response.data[0].url
        img_data = requests.get(image_url).content
        
        output_path = OUTPUT_DIR / "thumbnail_artigo_ia.png"
        output_path.write_bytes(img_data)
        print(f"Thumbnail gerada e salva em: {output_path}")

    except Exception as e:
        print(f"Falha na geracao da imagem: {e}")

if __name__ == "__main__":
    gerar_thumbnail_artigo()

