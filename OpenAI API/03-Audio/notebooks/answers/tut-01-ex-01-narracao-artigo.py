"""
Exercicio 1: Criar Narracao de Artigo
Referencia: Tutorial 01 - Text-to-Speech (TTS)

Este script demonstra como converter um texto longo em áudio de alta qualidade utilizando
o modelo tts-1-hd e a voz 'nova'.

Pontos principais:
1. Utilizacao do modelo de alta definicao (tts-1-hd).
2. Configuracao de voz feminina (nova).
3. Salvamento do arquivo resultante para uso em podcasts ou blogs.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def narrar_artigo():
    texto_artigo = (
        "A inteligencia artificial generativa esta redefinindo as fronteiras da criatividade humana. "
        "Ao integrar modelos de linguagem com ferramentas de geracao de imagem e audio, desenvolvedores "
        "podem criar experiencias multimodais sem precedentes. Este tutorial explora como a API de "
        "audio da OpenAI pode ser utilizada para dar voz a conteudos textuais de forma natural."
    )

    try:
        response = client.audio.speech.create(
            model="tts-1-hd",
            voice="nova",
            input=texto_artigo
        )

        output_path = Path("artigo_narrado.mp3")
        response.stream_to_file(output_path)
        print(f"Narracao gerada com sucesso: {output_path.resolve()}")

    except Exception as e:
        print(f"Erro na sintese de voz: {e}")

if __name__ == "__main__":
    narrar_artigo()

