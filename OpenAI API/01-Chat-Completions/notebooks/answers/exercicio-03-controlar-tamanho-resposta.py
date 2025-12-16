"""
Exercício 3: Controlar Tamanho da Resposta

Referência: 01-conversa-basica.ipynb - Exercício 3

Descrição:
Use max_tokens para limitar a resposta a 50 tokens e depois a 500 tokens. 
Observe a diferença.

Explicação:

O parâmetro max_tokens controla o tamanho máximo da resposta:

1. O que são tokens?:
   - Tokens são unidades de texto processadas pelo modelo
   - Aproximadamente 4 caracteres = 1 token
   - Exemplo: 'Hello world' = 2 tokens

2. Como funciona max_tokens:
   - Limita o número de tokens na RESPOSTA (não inclui o prompt)
   - Se a resposta exceder o limite, ela é cortada
   - Útil para controlar custos e tamanho

3. Valores recomendados:
   - 50-100 tokens: Respostas muito curtas, títulos, tags
   - 200-500 tokens: Respostas médias, parágrafos
   - 1000+ tokens: Respostas longas, artigos, análises detalhadas

4. Impacto nos custos:
   - Cada token de saída tem um custo
   - Limitar max_tokens reduz custos significativamente
   - Exemplo: 50 tokens vs 500 tokens = 10x diferença no custo

5. Boas práticas:
   - Use max_tokens apropriado para cada caso de uso
   - Para chatbots: 200-300 tokens geralmente suficiente
   - Para análises: 500-1000 tokens
   - Sempre monitore o uso de tokens em produção

6. Observação importante:
   - Respostas cortadas podem parecer incompletas
   - Se a resposta for cortada, aumente max_tokens
   - Ou divida a pergunta em partes menores
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Pergunta que será testada com diferentes limites de tokens
pergunta = "Explique o que é Machine Learning e suas principais aplicações."

print("=" * 60)
print("EXERCÍCIO 3: Controlar Tamanho da Resposta")
print("=" * 60)
print()
print(f"Pergunta: {pergunta}")
print()

# RESPOSTA DO EXERCÍCIO - 50 tokens
print("=" * 60)
print("RESPOSTA 1: max_tokens=50 (Resposta Curta)")
print("=" * 60)
print()

response_50 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ],
    temperature=0.7,
    max_tokens=50  # Limite muito curto
)

print(response_50.choices[0].message.content)
print()
print(f"Tokens usados: {response_50.usage.completion_tokens} (limite: 50)")
print(f"Caracteres: {len(response_50.choices[0].message.content)}")
print()

# RESPOSTA DO EXERCÍCIO - 500 tokens
print("=" * 60)
print("RESPOSTA 2: max_tokens=500 (Resposta Longa)")
print("=" * 60)
print()

response_500 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ],
    temperature=0.7,
    max_tokens=500  # Limite maior
)

print(response_500.choices[0].message.content)
print()
print(f"Tokens usados: {response_500.usage.completion_tokens} (limite: 500)")
print(f"Caracteres: {len(response_500.choices[0].message.content)}")
print()

# COMPARAÇÃO
print("=" * 60)
print("COMPARAÇÃO")
print("=" * 60)
print()

print(f"Resposta curta (50 tokens):")
print(f"  - Tokens: {response_50.usage.completion_tokens}")
print(f"  - Caracteres: {len(response_50.choices[0].message.content)}")
print(f"  - Característica: Resposta cortada, incompleta")
print()
print(f"Resposta longa (500 tokens):")
print(f"  - Tokens: {response_500.usage.completion_tokens}")
print(f"  - Caracteres: {len(response_500.choices[0].message.content)}")
print(f"  - Característica: Resposta completa e detalhada")

