"""
Exercicio 2: Detector de Idioma Automático
Referencia: Tutorial 02 - Speech-to-Text (Whisper)

Este script utiliza o modelo Whisper para identificar automaticamente o idioma de um 
arquivo de áudio e extrair metadados técnicos sobre a gravação.

Pontos principais:
1. Uso do formato 'verbose_json' para obter metadados detalhados.
2. Identificacao do idioma detectado pelo modelo.
3. Extracao da duracao total do arquivo.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def detectar_idioma_audio(caminho_audio):
    if not os.path.exists(caminho_audio):
        print(f"Erro: Arquivo {caminho_audio} nao localizado.")
        return

    try:
        with open(caminho_audio, "rb") as audio_file:
            response = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="verbose_json"
            )

        print(f"Resultado para: {os.path.basename(caminho_audio)}")
        print(f"- Idioma detectado: {response.language}")
        print(f"- Duracao total: {response.duration:.2f} segundos")
        print(f"- Texto capturado: {response.text[:100]}...")

    except Exception as e:
        print(f"Falha no processamento: {e}")

if __name__ == "__main__":
    # Caminho do audio na pasta assets do modulo
    path_audio = Path("../assets/cadastro_cliente.wav")
    detectar_idioma_audio(path_audio)

