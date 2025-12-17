"""
Exercicio 2: Tradutor Visual de Menus
Referencia: Tutorial 01 - Analise de Imagem Basica

Este script demonstra como utilizar a API de Visao para ler o conteudo de uma imagem 
(ex: menu de restaurante) e traduzir as informacoes para o Portugues.

Pontos principais:
1. Envio de imagem via URL.
2. Instrucoes de traducao contextualizada.
3. Extracao de texto e significado simultaneamente.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def tradutor_visual():
    # URL de exemplo: Menu de cafe da manha em Ingles
    url_menu = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Breakfast_menu_at_the_Wayside_Inn.jpg/800px-Breakfast_menu_at_the_Wayside_Inn.jpg"

    print("Analisando e traduzindo menu...\n")

    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": "Identifique os itens deste menu e traduza-os para o Portugues brasileiro. "
                                    "Apresente o resultado em uma lista formatada."
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": url_menu}
                        }
                    ]
                }
            ],
            max_tokens=500
        )

        print("Menu Traduzido:")
        print("-" * 30)
        print(response.choices[0].message.content)

    except Exception as e:
        print(f"Erro no processamento visual: {e}")

if __name__ == "__main__":
    tradutor_visual()

