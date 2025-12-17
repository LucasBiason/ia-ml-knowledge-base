"""
Exercício 2: Processar Múltiplos Documentos

Referência: 01-extracao-dados-json.ipynb - Exercício 2

Descrição:
Crie uma função que processa uma pasta de PDFs e extrai dados de todos, retornando uma lista de JSONs.

Explicação:

Sistema de processamento em lote de documentos PDF com extração estruturada.

Pontos importantes:

1. Processamento em Lote:
   - Processa múltiplos arquivos de uma vez
   - Retorna lista de resultados estruturados
   - Facilita automação de processos documentais

2. Estrutura de Dados:
   - Cada documento gera um JSON independente
   - Lista permite processamento sequencial ou paralelo
   - Facilita armazenamento em banco de dados

3. Tratamento de Arquivos:
   - Verifica existência de arquivos antes de processar
   - Trata erros de leitura de PDF
   - Ignora arquivos inválidos sem quebrar o processo

4. Aplicação Prática:
   - Digitalização de documentos em massa
   - Processamento de contratos
   - Extração de dados de fichas cadastrais
   - Normalização de documentos legais

5. Melhorias Possíveis:
   - Processamento paralelo com threading/multiprocessing
   - Barra de progresso para grandes volumes
   - Validação de schema antes de retornar
   - Logging detalhado de erros
   - Suporte a outros formatos (DOCX, TXT)
   - Cache de resultados processados
"""

import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Função auxiliar para extrair dados em JSON
def chat_to_json(system_prompt: str, user_content):
    """
    Extrai dados estruturados em JSON usando a API de Chat Completions.
    """
    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        response_format={'type': 'json_object'},
        messages=[
            {'role': 'system', 'content': system_prompt},
            {'role': 'user', 'content': user_content},
        ],
    )
    return json.loads(completion.choices[0].message.content)

def processar_pasta_pdfs(pasta_pdfs: str, schema_descricao: str):
    """
    Processa todos os PDFs de uma pasta e extrai dados estruturados.
    
    Args:
        pasta_pdfs: Caminho da pasta contendo os PDFs
        schema_descricao: Descrição do schema JSON desejado
    
    Returns:
        list: Lista de dicionários com dados extraídos de cada PDF
    """
    pasta = Path(pasta_pdfs)
    resultados = []
    
    if not pasta.exists():
        print(f"Pasta não encontrada: {pasta_pdfs}")
        return resultados
    
    # Buscar todos os arquivos PDF na pasta
    arquivos_pdf = list(pasta.glob('*.pdf'))
    
    if not arquivos_pdf:
        print(f"Nenhum arquivo PDF encontrado em: {pasta_pdfs}")
        return resultados
    
    print(f"Encontrados {len(arquivos_pdf)} arquivo(s) PDF para processar")
    print()
    
    for i, pdf_path in enumerate(arquivos_pdf, 1):
        print(f"[{i}/{len(arquivos_pdf)}] Processando: {pdf_path.name}")
        
        try:
            # Extrair texto do PDF
            reader = PdfReader(str(pdf_path))
            pdf_text = '\n'.join(
                page.extract_text().strip()
                for page in reader.pages
                if page.extract_text()
            )
            
            if not pdf_text.strip():
                print(f"  ⚠️  Arquivo vazio ou sem texto extraível")
                continue
            
            # Extrair dados estruturados
            dados = chat_to_json(
                system_prompt='Você normaliza documentos em JSON válido.',
                user_content=f"{schema_descricao}\n\nConteúdo do documento:\n{pdf_text}"
            )
            
            # Adicionar nome do arquivo aos dados
            dados['arquivo_origem'] = pdf_path.name
            resultados.append(dados)
            
            print(f"  ✅ Dados extraídos com sucesso")
            
        except Exception as e:
            print(f"  ❌ Erro ao processar {pdf_path.name}: {e}")
            continue
    
    return resultados

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 2: Processar Múltiplos Documentos PDF")
print("=" * 60)
print()

# Definir schema para extração
schema_cadastro = (
    'Extraia informações de fichas cadastrais. Retorne apenas JSON válido '
    'com as chaves: name (nome completo), document_id (CPF/CNPJ), birth_date (data de nascimento), '
    'city (cidade). Use null para campos ausentes.'
)

# Processar pasta de PDFs (usando a pasta assets como exemplo)
pasta_assets = Path('assets')
resultados = processar_pasta_pdfs(pasta_assets, schema_cadastro)

print()
print("=" * 60)
print(f"RESULTADO: {len(resultados)} documento(s) processado(s)")
print("=" * 60)
print()

# Exibir resultados
for i, dados in enumerate(resultados, 1):
    print(f"Documento {i}: {dados.get('arquivo_origem', 'N/A')}")
    print(json.dumps(dados, indent=2, ensure_ascii=False))
    print()

