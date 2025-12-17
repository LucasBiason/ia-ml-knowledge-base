"""
Exercício 1: Criar Função de Busca

Referência: 04-funcoes-function-calling.ipynb - Exercício 1

Descrição:
Crie uma função que busca informações sobre produtos em um catálogo e integre com Function Calling.

Explicação:

Sistema de busca de produtos usando Function Calling para permitir que o modelo consulte informações de um catálogo.

Pontos importantes:

1. Estrutura de Dados:
   - Catálogo de produtos organizado
   - Busca por nome, categoria ou preço
   - Retorna informações estruturadas

2. Function Calling:
   - Modelo decide quando buscar produtos
   - Pode fazer perguntas sobre produtos
   - Integra busca com conversa natural

3. Aplicação Prática:
   - Assistente de vendas
   - Sistema de recomendação
   - Consulta de catálogo
   - E-commerce com IA

4. Melhorias Possíveis:
   - Busca por múltiplos critérios
   - Ordenação de resultados
   - Integração com banco de dados
   - Cache de buscas frequentes
   - Busca semântica com embeddings
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Catálogo de produtos
catalogo_produtos = [
    {"nome": "Notebook Dell", "categoria": "Informática", "preco": 3500.00, "estoque": 15},
    {"nome": "Mouse Logitech", "categoria": "Periféricos", "preco": 89.90, "estoque": 45},
    {"nome": "Teclado Mecânico", "categoria": "Periféricos", "preco": 299.90, "estoque": 28},
    {"nome": "Monitor LG", "categoria": "Monitores", "preco": 899.90, "estoque": 12},
    {"nome": "Webcam HD", "categoria": "Periféricos", "preco": 199.90, "estoque": 30},
    {"nome": "SSD 1TB", "categoria": "Componentes", "preco": 399.90, "estoque": 25},
    {"nome": "Memória RAM 16GB", "categoria": "Componentes", "preco": 249.90, "estoque": 40},
]

def buscar_produto(termo: str) -> str:
    """
    Busca produtos no catálogo por nome ou categoria.
    
    Args:
        termo: Termo de busca (nome do produto ou categoria)
    
    Returns:
        str: Lista de produtos encontrados formatada
    """
    resultados = []
    termo_lower = termo.lower()
    
    for produto in catalogo_produtos:
        nome_match = termo_lower in produto["nome"].lower()
        categoria_match = termo_lower in produto["categoria"].lower()
        
        if nome_match or categoria_match:
            resultados.append(produto)
    
    if not resultados:
        return f"Nenhum produto encontrado para '{termo}'"
    
    # Formatar resultados
    resultado_formatado = f"Produtos encontrados para '{termo}':\n\n"
    for produto in resultados:
        resultado_formatado += (
            f"- {produto['nome']} ({produto['categoria']})\n"
            f"  Preço: R$ {produto['preco']:.2f}\n"
            f"  Estoque: {produto['estoque']} unidades\n\n"
        )
    
    return resultado_formatado.strip()

# Definir função para o modelo
funcoes_busca = [
    {
        "type": "function",
        "function": {
            "name": "buscar_produto",
            "description": "Busca produtos no catálogo por nome ou categoria",
            "parameters": {
                "type": "object",
                "properties": {
                    "termo": {
                        "type": "string",
                        "description": "Termo de busca (nome do produto ou categoria)"
                    }
                },
                "required": ["termo"]
            }
        }
    }
]

mapeamento_busca = {
    "buscar_produto": buscar_produto
}

def processar_function_call(mensagens, funcoes, mapeamento_funcoes, max_iteracoes=5):
    """Processa function calls automaticamente."""
    iteracoes = 0
    
    while iteracoes < max_iteracoes:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            tools=funcoes,
            tool_choice="auto"
        )
        
        mensagem = response.choices[0].message
        mensagens.append(mensagem)
        
        if not mensagem.tool_calls:
            return mensagem.content
        
        for tool_call in mensagem.tool_calls:
            nome_funcao = tool_call.function.name
            argumentos = json.loads(tool_call.function.arguments)
            tool_call_id = tool_call.id
            
            if nome_funcao in mapeamento_funcoes:
                funcao = mapeamento_funcoes[nome_funcao]
                try:
                    resultado = funcao(**argumentos)
                except Exception as e:
                    resultado = f"Erro ao executar função: {e}"
            else:
                resultado = f"Função '{nome_funcao}' não encontrada"
            
            mensagens.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": nome_funcao,
                "content": str(resultado)
            })
        
        iteracoes += 1
    
    return "Número máximo de iterações atingido"

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 1: Função de Busca de Produtos")
print("=" * 60)
print()

mensagens = [
    {
        "role": "system",
        "content": "Você é um assistente de vendas que ajuda clientes a encontrar produtos no catálogo."
    },
    {
        "role": "user",
        "content": "Quais produtos de periféricos vocês têm disponíveis?"
    }
]

resposta = processar_function_call(
    mensagens=mensagens,
    funcoes=funcoes_busca,
    mapeamento_funcoes=mapeamento_busca
)

print(">> Resposta do assistente:")
print("-" * 60)
print(resposta)

