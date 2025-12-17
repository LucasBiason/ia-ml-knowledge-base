"""
Exercicio 1: Extracao de Dados de E-mail
Referencia: Tutorial 01 - Extracao de Dados JSON

Este script demonstra como processar o conteudo de um e-mail nao estruturado para extrair 
informacoes estruturadas em formato JSON, como dados de contato e intencao do cliente.

Pontos principais:
1. Definicao de um prompt de sistema para estruturacao de dados.
2. Uso do modo JSON da API (response_format={'type': 'json_object'}).
3. Captura automatica de leads para sistemas CRM.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def extrair_dados_email(corpo_email):
    prompt_sistema = (
        "Voce e um assistente especializado em processamento de leads. "
        "Sua tarefa e extrair informacoes de e-mails de clientes e retornar um JSON estruturado. "
        "Campos obrigatorios: nome, assunto, mensagem_resumo, email_contato, telefone_contato (se houver)."
    )

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt_sistema},
                {"role": "user", "content": corpo_email}
            ],
            response_format={"type": "json_object"}
        )

        return json.loads(response.choices[0].message.content)
    except Exception as e:
        return {"erro": str(e)}

if __name__ == "__main__":
    email_exemplo = (
        "Assunto: Orcamento para novo projeto\n\n"
        "Ola, meu nome e Carlos Alberto e gostaria de um orcamento para o desenvolvimento "
        "de um aplicativo mobile. Podem entrar em contato comigo pelo e-mail carlos.a@empresa.com "
        "ou pelo telefone (11) 97777-6655. No aguardo."
    )

    print("Processando e-mail de lead...")
    dados = extrair_dados_email(email_exemplo)
    print(json.dumps(dados, indent=4, ensure_ascii=False))

