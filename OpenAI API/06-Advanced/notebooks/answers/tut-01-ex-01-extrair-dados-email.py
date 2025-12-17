"""
Exercício 1: Extrair Dados de E-mail

Referência: 01-extracao-dados-json.ipynb - Exercício 1

Descrição:
Crie um sistema que extrai informações de e-mails de contato (nome, assunto, mensagem, contato) e estrutura em JSON.

Explicação:

Sistema de extração de dados de e-mails usando response_format JSON.

Pontos importantes:

1. Schema JSON Definido:
   - Estrutura clara com campos específicos (nome, assunto, mensagem, contato)
   - Uso de null para campos ausentes
   - Facilita integração com sistemas de CRM ou banco de dados

2. Processamento de Texto:
   - Extrai informações mesmo de formatos variados de e-mail
   - Identifica nome do remetente de diferentes formatos
   - Extrai assunto e mensagem principal
   - Captura informações de contato (e-mail, telefone)

3. Aplicação Prática:
   - Automação de atendimento ao cliente
   - Processamento de formulários de contato
   - Integração com sistemas de ticket
   - Análise de feedback de clientes

4. Melhorias Possíveis:
   - Processar e-mails reais via IMAP/POP3
   - Detectar sentimento da mensagem
   - Classificar tipo de solicitação
   - Extrair anexos e processar
   - Integrar com banco de dados
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Função auxiliar para extrair dados em JSON
def chat_to_json(system_prompt: str, user_content):
    """
    Extrai dados estruturados em JSON usando a API de Chat Completions.
    
    Args:
        system_prompt: Prompt do sistema definindo o contexto
        user_content: Conteúdo do usuário (texto do e-mail)
    
    Returns:
        dict: Dados extraídos em formato JSON
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

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 1: Extrair Dados de E-mail")
print("=" * 60)
print()

# E-mail de exemplo
email_exemplo = """
De: joao.silva@empresa.com.br
Para: contato@minhaempresa.com
Assunto: Solicitação de Orçamento

Olá,

Meu nome é João Silva e trabalho na empresa Tech Solutions.
Gostaria de solicitar um orçamento para desenvolvimento de um sistema.

Você pode entrar em contato comigo pelo telefone (11) 98765-4321 ou 
responder este e-mail.

Atenciosamente,
João Silva
"""

print("E-mail original:")
print("-" * 60)
print(email_exemplo)
print()

# Definir schema JSON
schema_email = (
    'Extraia as seguintes informações do e-mail e retorne apenas JSON válido '
    'com as chaves: name (nome do remetente), subject (assunto), message (mensagem principal), '
    'email (e-mail de contato), phone (telefone se mencionado). '
    'Use null para campos ausentes.'
)

# Extrair dados do e-mail
dados_email = chat_to_json(
    system_prompt='Você extrai informações estruturadas de e-mails de contato e responde somente JSON válido.',
    user_content=f"{schema_email}\n\nE-mail:\n{email_exemplo}"
)

print("Dados extraídos em JSON:")
print("-" * 60)
print(json.dumps(dados_email, indent=2, ensure_ascii=False))

