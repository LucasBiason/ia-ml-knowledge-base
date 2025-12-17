"""
Exercício 3: Controlar Custos

Referência: 03-parametros-avancados.ipynb - Exercício 3

Descrição:
Use max_tokens para limitar respostas a 150 tokens e compare o custo antes e depois.

Explicação:

Como controlar custos usando max_tokens.

Pontos importantes:

1. Impacto do max_tokens:
   - Limita o número de tokens na resposta (completion)
   - Não afeta tokens do prompt
   - Redução direta nos custos de saída

2. Cálculo de Custos:
   - GPT-3.5-turbo: ~$0.50/1M tokens entrada, ~$1.50/1M tokens saída
   - GPT-4: Mais caro, verifique preços atualizados
   - Tokens de saída são mais caros que entrada

3. Trade-off: Qualidade vs. Custo:
   - Respostas mais curtas = menor custo
   - Pode perder detalhes importantes
   - Encontrar equilíbrio é crucial

4. Quando Limitar max_tokens:
   - Respostas curtas (títulos, tags, resumos)
   - Chatbots com respostas concisas
   - Aplicações com alto volume de requisições
   - Quando custo é crítico

5. Quando NÃO Limitar:
   - Análises detalhadas
   - Documentação completa
   - Explicações técnicas profundas
   - Quando qualidade > custo

6. Estratégias de Otimização:
   - Use max_tokens apropriado para cada caso
   - Monitore uso de tokens em produção
   - Ajuste conforme feedback
   - Considere modelos mais baratos quando possível

7. Escala e Impacto:
   - Em escala, pequenas economias se multiplicam
   - 1.000 requisições: economia significativa
   - 1.000.000 requisições: economia massiva
   - Sempre calcule ROI de otimizações

8. Monitoramento:
   - Use logs para rastrear uso de tokens
   - Configure alertas para custos elevados
   - Revise regularmente e otimize
   - Documente decisões de max_tokens
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 3: Controlar Custos com max_tokens")
print("=" * 60)
print()

pergunta = "Explique os principais conceitos de programação orientada a objetos."

print(f"Pergunta: {pergunta}\n")

# ANTES: Sem limite de tokens (ou limite alto)
print("=" * 60)
print("ANTES: Sem Limite de Tokens (max_tokens=500)")
print("=" * 60)
print()

response_antes = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user',
            'content': pergunta
        }
    ],
    max_tokens=500  # Limite alto
)

print(response_antes.choices[0].message.content)
print()

tokens_antes = response_antes.usage.completion_tokens
tokens_prompt_antes = response_antes.usage.prompt_tokens
tokens_total_antes = response_antes.usage.total_tokens

print(f"Tokens usados:")
print(f"  - Prompt: {tokens_prompt_antes}")
print(f"  - Completion: {tokens_antes}")
print(f"  - Total: {tokens_total_antes}")
print()

# Calcular custo estimado (GPT-3.5-turbo: ~$0.50/1M entrada, ~$1.50/1M saída)
custo_entrada_antes = (tokens_prompt_antes / 1_000_000) * 0.50
custo_saida_antes = (tokens_antes / 1_000_000) * 1.50
custo_total_antes = custo_entrada_antes + custo_saida_antes

print(f"Custo estimado (GPT-3.5-turbo):")
print(f"  - Entrada: ${custo_entrada_antes:.6f}")
print(f"  - Saída: ${custo_saida_antes:.6f}")
print(f"  - Total: ${custo_total_antes:.6f}")
print()

# DEPOIS: Com limite de 150 tokens
print("=" * 60)
print("DEPOIS: Com Limite de 150 Tokens")
print("=" * 60)
print()

response_depois = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user',
            'content': pergunta
        }
    ],
    max_tokens=150  # Limite baixo para controlar custos
)

print(response_depois.choices[0].message.content)
print()

tokens_depois = response_depois.usage.completion_tokens
tokens_prompt_depois = response_depois.usage.prompt_tokens
tokens_total_depois = response_depois.usage.total_tokens

print(f"Tokens usados:")
print(f"  - Prompt: {tokens_prompt_depois}")
print(f"  - Completion: {tokens_depois}")
print(f"  - Total: {tokens_total_depois}")
print()

# Calcular custo estimado
custo_entrada_depois = (tokens_prompt_depois / 1_000_000) * 0.50
custo_saida_depois = (tokens_depois / 1_000_000) * 1.50
custo_total_depois = custo_entrada_depois + custo_saida_depois

print(f"Custo estimado (GPT-3.5-turbo):")
print(f"  - Entrada: ${custo_entrada_depois:.6f}")
print(f"  - Saída: ${custo_saida_depois:.6f}")
print(f"  - Total: ${custo_total_depois:.6f}")
print()

# COMPARAÇÃO
print("=" * 60)
print("COMPARAÇÃO: ANTES vs DEPOIS")
print("=" * 60)
print()

reducao_tokens = tokens_antes - tokens_depois
reducao_percentual = (reducao_tokens / tokens_antes) * 100
reducao_custo = custo_total_antes - custo_total_depois
reducao_custo_percentual = (reducao_custo / custo_total_antes) * 100

print(f"Redução de Tokens:")
print(f"  - Antes: {tokens_antes} tokens")
print(f"  - Depois: {tokens_depois} tokens")
print(f"  - Redução: {reducao_tokens} tokens ({reducao_percentual:.1f}%)")
print()

print(f"Redução de Custo:")
print(f"  - Antes: ${custo_total_antes:.6f}")
print(f"  - Depois: ${custo_total_depois:.6f}")
print(f"  - Economia: ${reducao_custo:.6f} ({reducao_custo_percentual:.1f}%)")
print()

print(f"Economia em escala (por 1.000 requisições):")
print(f"  - Economia total: ${reducao_custo * 1000:.2f}")

