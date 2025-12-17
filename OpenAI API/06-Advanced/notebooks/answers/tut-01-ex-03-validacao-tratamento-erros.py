"""
Exercício 3: Validação e Tratamento de Erros
Referência: Tutorial 01 - Advanced (Extração de Dados JSON)

Este script implementa uma camada de segurança sobre a extração de dados JSON,
incluindo validação de schema para garantir que o modelo retornou todas as chaves
necessárias e tratamento de exceções para falhas de rede ou formatos inválidos.

Recursos implementados:
1. Validação básica de chaves obrigatórias no dicionário retornado.
2. Bloco try-except para capturar erros de decodificação JSON.
3. Lógica de re-tentativa ou fallback em caso de erro.
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def extrair_com_validacao(texto, chaves_obrigatorias):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            response_format={"type": "json_object"},
            messages=[
                {"role": "system", "content": "Você é um extrator de dados rigoroso. Responda apenas JSON."},
                {"role": "user", "content": f"Extraia os dados deste texto: {texto}. Obrigatório conter: {', '.join(chaves_obrigatorias)}"}
            ]
        )
        
        dados = json.loads(response.choices[0].message.content)
        
        # Validar presença das chaves
        faltantes = [c for c in chaves_obrigatorias if c not in dados]
        if faltantes:
            return {"erro": f"Campos obrigatórios faltantes: {faltantes}", "dados_parciais": dados}
            
        return dados

    except json.JSONDecodeError:
        return {"erro": "O modelo não retornou um JSON válido."}
    except Exception as e:
        return {"erro": f"Erro inesperado: {str(e)}"}

if __name__ == "__main__":
    texto_vago = "O cliente ligou querendo saber do status do pedido."
    chaves = ["nome_cliente", "numero_pedido", "status"]
    
    print("Iniciando extração com validação...")
    resultado = extrair_com_validacao(texto_vago, chaves)
    
    if "erro" in resultado:
        print(f"⚠️ Alerta: {resultado['erro']}")
    else:
        print("✅ Extração bem-sucedida!")
        
    print(json.dumps(resultado, indent=2, ensure_ascii=False))

