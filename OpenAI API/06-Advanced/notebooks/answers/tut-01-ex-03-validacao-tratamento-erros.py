"""
Exercício 3: Validação e Tratamento de Erros

Referência: 01-extracao-dados-json.ipynb - Exercício 3

Descrição:
Implemente validação de schema JSON e tratamento de erros robusto para um sistema de extração de dados.

Explicação:

Sistema robusto de extração com validação de schema e tratamento completo de erros.

Pontos importantes:

1. Validação de Schema:
   - Define estrutura esperada dos dados
   - Valida tipos de dados (string, number, date)
   - Verifica campos obrigatórios
   - Garante consistência dos dados extraídos

2. Tratamento de Erros:
   - Erros de API (rate limits, timeouts)
   - Erros de parsing JSON
   - Erros de validação de schema
   - Erros de arquivo (não encontrado, corrompido)
   - Retry automático para erros temporários

3. Estrutura de Resposta:
   - Retorna resultado ou erro de forma estruturada
   - Facilita logging e debugging
   - Permite decisões baseadas no status

4. Aplicação Prática:
   - Sistemas de produção que precisam de confiabilidade
   - Processamento de documentos críticos
   - Integração com sistemas externos
   - Automação que precisa de garantias

5. Melhorias Possíveis:
   - Usar biblioteca jsonschema para validação mais robusta
   - Implementar retry com backoff exponencial
   - Adicionar métricas de sucesso/falha
   - Cache de resultados para evitar reprocessamento
   - Notificações de erros críticos
"""

import os
import json
import time
from typing import Dict, Optional, Any, Tuple
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Schema esperado para validação
SCHEMA_ESPERADO = {
    'name': str,
    'document_id': str,
    'birth_date': str,
    'city': str
}

def validar_schema(dados: Dict[str, Any], schema: Dict[str, type]) -> Tuple[bool, Optional[str]]:
    """
    Valida se os dados extraídos correspondem ao schema esperado.
    
    Args:
        dados: Dados extraídos em formato dict
        schema: Schema esperado com tipos de dados
    
    Returns:
        tuple: (valido, mensagem_erro)
    """
    if not isinstance(dados, dict):
        return False, "Dados não são um dicionário"
    
    for campo, tipo_esperado in schema.items():
        if campo not in dados:
            return False, f"Campo obrigatório ausente: {campo}"
        
        valor = dados[campo]
        if valor is not None and not isinstance(valor, tipo_esperado):
            return False, f"Campo '{campo}' tem tipo incorreto. Esperado: {tipo_esperado.__name__}, Recebido: {type(valor).__name__}"
    
    return True, None

def chat_to_json_com_retry(system_prompt: str, user_content, max_retries: int = 3):
    """
    Extrai dados em JSON com retry automático para erros temporários.
    
    Args:
        system_prompt: Prompt do sistema
        user_content: Conteúdo do usuário
        max_retries: Número máximo de tentativas
    
    Returns:
        dict: Dados extraídos ou None em caso de falha
    """
    for tentativa in range(max_retries):
        try:
            completion = client.chat.completions.create(
                model='gpt-4o-mini',
                response_format={'type': 'json_object'},
                messages=[
                    {'role': 'system', 'content': system_prompt},
                    {'role': 'user', 'content': user_content},
                ],
            )
            return json.loads(completion.choices[0].message.content)
        
        except json.JSONDecodeError as e:
            if tentativa == max_retries - 1:
                raise ValueError(f"Erro ao fazer parse do JSON após {max_retries} tentativas: {e}")
            time.sleep(1)
        
        except Exception as e:
            if tentativa == max_retries - 1:
                raise
            time.sleep(2 ** tentativa)
    
    return None

def extrair_dados_pdf_robusto(pdf_path: Path, schema_descricao: str) -> Dict[str, Any]:
    """
    Extrai dados de um PDF com validação e tratamento completo de erros.
    
    Args:
        pdf_path: Caminho do arquivo PDF
        schema_descricao: Descrição do schema JSON desejado
    
    Returns:
        dict: Resultado com status, dados ou erro
    """
    resultado = {
        'status': 'sucesso',
        'arquivo': str(pdf_path),
        'dados': None,
        'erro': None
    }
    
    # Verificar se arquivo existe
    if not pdf_path.exists():
        resultado['status'] = 'erro'
        resultado['erro'] = f"Arquivo não encontrado: {pdf_path}"
        return resultado
    
    # Verificar tamanho do arquivo (limite de 10MB)
    tamanho_mb = pdf_path.stat().st_size / (1024 * 1024)
    if tamanho_mb > 10:
        resultado['status'] = 'erro'
        resultado['erro'] = f"Arquivo muito grande: {tamanho_mb:.2f}MB (limite: 10MB)"
        return resultado
    
    try:
        # Extrair texto do PDF
        reader = PdfReader(str(pdf_path))
        pdf_text = '\n'.join(
            page.extract_text().strip()
            for page in reader.pages
            if page.extract_text()
        )
        
        if not pdf_text.strip():
            resultado['status'] = 'erro'
            resultado['erro'] = "PDF não contém texto extraível"
            return resultado
        
        # Extrair dados com retry
        dados = chat_to_json_com_retry(
            system_prompt='Você normaliza documentos em JSON válido.',
            user_content=f"{schema_descricao}\n\nConteúdo do documento:\n{pdf_text}"
        )
        
        # Validar schema
        valido, mensagem_erro = validar_schema(dados, SCHEMA_ESPERADO)
        
        if not valido:
            resultado['status'] = 'erro_validacao'
            resultado['erro'] = f"Schema inválido: {mensagem_erro}"
            resultado['dados'] = dados
            return resultado
        
        resultado['dados'] = dados
        return resultado
    
    except ValueError as e:
        resultado['status'] = 'erro'
        resultado['erro'] = f"Erro de processamento: {str(e)}"
        return resultado
    
    except Exception as e:
        resultado['status'] = 'erro'
        resultado['erro'] = f"Erro inesperado: {str(e)}"
        return resultado

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 3: Validação e Tratamento de Erros")
print("=" * 60)
print()

# Schema para extração
schema_cadastro = (
    'Extraia informações de fichas cadastrais. Retorne apenas JSON válido '
    'com as chaves: name (nome completo), document_id (CPF/CNPJ), birth_date (data de nascimento), '
    'city (cidade). Use null para campos ausentes.'
)

# Testar com arquivo existente
pdf_path = Path('assets/ficha_cadastro.pdf')
resultado = extrair_dados_pdf_robusto(pdf_path, schema_cadastro)

print(f"Arquivo processado: {resultado['arquivo']}")
print(f"Status: {resultado['status']}")
print()

if resultado['status'] == 'sucesso':
    print("✅ Dados extraídos e validados com sucesso:")
    print(json.dumps(resultado['dados'], indent=2, ensure_ascii=False))
elif resultado['status'] == 'erro_validacao':
    print("⚠️  Dados extraídos mas schema inválido:")
    print(f"Erro: {resultado['erro']}")
    print(f"Dados recebidos: {json.dumps(resultado['dados'], indent=2, ensure_ascii=False)}")
else:
    print(f"❌ Erro no processamento:")
    print(f"Erro: {resultado['erro']}")

print()
print("=" * 60)
print("Testando com arquivo inexistente (tratamento de erro):")
print("=" * 60)
print()

pdf_inexistente = Path('assets/arquivo_inexistente.pdf')
resultado_erro = extrair_dados_pdf_robusto(pdf_inexistente, schema_cadastro)

print(f"Arquivo: {resultado_erro['arquivo']}")
print(f"Status: {resultado_erro['status']}")
print(f"Erro: {resultado_erro['erro']}")

