"""
Exercício 1: Otimizar para Tarefa Específica

Referência: 03-parametros-avancados.ipynb - Exercício 1

Descrição:
Crie uma requisição otimizada para gerar títulos de artigos (curtos, criativos, sem repetição).

Explicação:

Como otimizar parâmetros para uma tarefa específica.

Parâmetros otimizados para gerar títulos:

1. temperature=0.9 (Alta Criatividade):
   - Títulos precisam ser criativos e únicos
   - Alta temperatura gera mais variação
   - Evita títulos genéricos e repetitivos

2. max_tokens=100 (Eficiência):
   - Títulos são curtos (10-15 palavras)
   - 100 tokens é suficiente para 5 títulos
   - Reduz custos desnecessários

3. top_p=0.95 (Diversidade Controlada):
   - Nucleus sampling para variar vocabulário
   - Mantém qualidade enquanto aumenta diversidade
   - Evita títulos muito similares

4. frequency_penalty=0.8 (ALTA - Evitar Repetição):
   - Penaliza palavras que aparecem frequentemente
   - Força o modelo a usar termos diferentes
   - Crítico para gerar títulos únicos

5. presence_penalty=0.6 (Incentivar Novos Termos):
   - Penaliza tópicos já mencionados
   - Incentiva explorar novos ângulos
   - Complementa frequency_penalty

6. n=5 (Múltiplas Opções):
   - Gera 5 títulos diferentes de uma vez
   - Permite escolher o melhor
   - Útil para A/B testing

7. Comparação com Configuração Padrão:
   - Padrão: temperature=1.0, sem penalties
   - Resultado: Títulos mais genéricos e repetitivos
   - Otimizado: Títulos únicos, criativos e variados

8. Casos de Uso Similares:
   - Gerar slogans publicitários
   - Criar nomes de produtos
   - Sugerir hashtags
   - Gerar variações de conteúdo
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
print("EXERCÍCIO 1: Otimizar para Gerar Títulos de Artigos")
print("=" * 60)
print()

# Requisição otimizada para gerar títulos
# Objetivos: curtos, criativos, sem repetição
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': 'Você é um especialista em criar títulos de artigos. Crie títulos curtos, criativos e impactantes.'
        },
        {
            'role': 'user',
            'content': 'Gere 5 títulos de artigos sobre inteligência artificial aplicada ao desenvolvimento de software.'
        }
    ],
    # Parâmetros otimizados para títulos
    temperature=0.9,  # Alta criatividade para títulos únicos
    max_tokens=100,   # Títulos são curtos, não precisa de muitos tokens
    top_p=0.95,       # Nucleus sampling para diversidade
    frequency_penalty=0.8,  # ALTA penalidade de frequência para evitar repetição
    presence_penalty=0.6,   # Penalidade de presença para incentivar novos termos
    n=5  # Gerar 5 títulos diferentes
)

print("Títulos gerados (otimizados para criatividade e sem repetição):")
print("-" * 60)
for i, choice in enumerate(response.choices, 1):
    print(f"{i}. {choice.message.content.strip()}")
print()

print(f"Tokens usados: {response.usage.total_tokens}")
print(f"  - Prompt: {response.usage.prompt_tokens}")
print(f"  - Resposta: {response.usage.completion_tokens}")

