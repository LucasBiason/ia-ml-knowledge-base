"""
Exercício 2: Processar Múltiplos Documentos
Referência: Tutorial 01 - Advanced (Extração de Dados JSON)

Este script automatiza o processamento de uma pasta contendo arquivos PDF,
extraindo o texto de cada um e utilizando a API da OpenAI para estruturar os dados
em uma lista de objetos JSON.

Conceitos aplicados:
1. Iteração sobre arquivos no sistema de arquivos local.
2. Uso da biblioteca pypdf para extração de texto de PDFs.
3. Orquestração de múltiplas chamadas à API para normalização de dados.
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def processar_pasta_pdfs(diretorio_assets):
    resultados = []
    caminho_pasta = Path(diretorio_assets)
    
    if not caminho_pasta.exists():
        return "Diretório não encontrado."

    for arquivo in caminho_pasta.glob("*.pdf"):
        print(f"Processando: {arquivo.name}...")
        
        # 1. Extrair texto do PDF
        reader = PdfReader(str(arquivo))
        texto_completo = ""
        for page in reader.pages:
            texto_completo += page.extract_text()
            
        # 2. Estruturar com GPT
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Você extrai dados de fichas cadastrais em PDF para JSON."},
                {"role": "user", "content": f"Extraia nome, documento e data de nascimento em JSON deste texto:\n{texto_completo}"}
            ]
        )
        
        dados = json.loads(response.choices[0].message.content)
        dados["arquivo_origem"] = arquivo.name
        resultados.append(dados)
        
    return resultados

if __name__ == "__main__":
    # Nota: Certifique-se de que a pasta assets contém PDFs
    assets_dir = Path(__file__).parent.parent / "assets"
    
    if any(assets_dir.glob("*.pdf")):
        processados = processar_pasta_pdfs(assets_dir)
        print("\nResultado do processamento em lote:")
        print(json.dumps(processados, indent=2, ensure_ascii=False))
    else:
        print(f"Nenhum arquivo PDF encontrado em {assets_dir}")

