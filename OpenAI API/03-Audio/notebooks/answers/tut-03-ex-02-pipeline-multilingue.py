"""
Exercicio 2: Pipeline de Traducao Multilingue
Referencia: Tutorial 03 - Traducao de Audio

Este script implementa um pipeline completo que transcreve um áudio e gera traduções 
simultâneas para múltiplos idiomas utilizando uma combinação de Whisper e GPT.

Pontos principais:
1. Transcricao no idioma original com Whisper.
2. Traducao em lote para diferentes linguas via Chat Completions.
3. Consolidacao de resultados em um relatorio textual.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def pipeline_multilingue(caminho_audio, idiomas_alvo):
    # Passo 1: Transcricao
    print("Transcrevendo audio original...")
    with open(caminho_audio, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            response_format="text"
        )

    # Passo 2: Traducao via GPT
    for idioma in idiomas_alvo:
        print(f"Traduzindo para {idioma}...")
        res_trad = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Voce e um tradutor especialista em {idioma}."},
                {"role": "user", "content": f"Traduza o seguinte texto para {idioma}: {transcription}"}
            ]
        )
        
        print(f"[{idioma}]: {res_trad.choices[0].message.content}")
        print("-" * 30)

if __name__ == "__main__":
    path_audio = Path("../assets/cadastro_cliente.wav")
    idiomas = ["Frances", "Alemao", "Japones"]
    
    if path_audio.exists():
        pipeline_multilingue(path_audio, idiomas)
    else:
        print("Arquivo de teste nao encontrado.")

