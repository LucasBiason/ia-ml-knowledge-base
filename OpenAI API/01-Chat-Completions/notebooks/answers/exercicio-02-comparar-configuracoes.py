"""
Exercício 2: Comparar Configurações

Referência: 03-parametros-avancados.ipynb - Exercício 2

Descrição:
Teste a mesma pergunta com diferentes combinações de parâmetros e compare os resultados.

Explicação:

Como diferentes configurações afetam as respostas.

Análise das Configurações:

1. Configuração Conservadora (temperature=0.3):
   - Respostas mais previsíveis e técnicas
   - Menos variação entre execuções
   - Ideal para: documentação, explicações técnicas, fatos
   - Desvantagem: Pode ser muito formal ou genérica

2. Configuração Criativa (temperature=0.9 + penalties):
   - Respostas mais variadas e criativas
   - Penalties evitam repetição
   - Ideal para: conteúdo criativo, brainstorming, variações
   - Desvantagem: Pode ser menos precisa ou consistente

3. Configuração Balanceada (temperature=0.7 + penalties leves):
   - Equilíbrio entre precisão e criatividade
   - Penalties leves evitam repetição excessiva
   - Ideal para: maioria dos casos de uso, chatbots
   - Desvantagem: Pode não ser otimizada para casos específicos

4. Quando Usar Cada Uma:
   - Conservadora: Quando precisão é crítica (médico, jurídico)
   - Criativa: Quando variação é desejada (marketing, conteúdo)
   - Balanceada: Uso geral (chatbots, assistentes)

5. Impacto nos Custos:
   - Tokens podem variar ligeiramente
   - Configurações criativas podem usar mais tokens
   - Sempre monitore uso de tokens em produção

6. Teste e Ajuste:
   - Sempre teste diferentes configurações
   - Meça qualidade vs. custo
   - Ajuste conforme feedback dos usuários
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
print("EXERCÍCIO 2: Comparar Diferentes Configurações")
print("=" * 60)
print()

pergunta = "Explique o que é machine learning de forma clara e didática."

print(f"Pergunta: {pergunta}\n")

# Configuração 1: Conservadora (baixa temperatura, sem penalties)
print("=" * 60)
print("CONFIGURAÇÃO 1: Conservadora")
print("=" * 60)
print("Parâmetros: temperature=0.3, sem penalties, max_tokens=200")
print()

response_1 = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user',
            'content': pergunta
        }
    ],
    temperature=0.3,
    max_tokens=200
)

print(response_1.choices[0].message.content)
print()
print(f"Tokens: {response_1.usage.total_tokens} (prompt: {response_1.usage.prompt_tokens}, completion: {response_1.usage.completion_tokens})")
print()

# Configuração 2: Criativa (alta temperatura, penalties)
print("=" * 60)
print("CONFIGURAÇÃO 2: Criativa")
print("=" * 60)
print("Parâmetros: temperature=0.9, frequency_penalty=0.5, presence_penalty=0.3, max_tokens=200")
print()

response_2 = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user',
            'content': pergunta
        }
    ],
    temperature=0.9,
    frequency_penalty=0.5,
    presence_penalty=0.3,
    max_tokens=200
)

print(response_2.choices[0].message.content)
print()
print(f"Tokens: {response_2.usage.total_tokens} (prompt: {response_2.usage.prompt_tokens}, completion: {response_2.usage.completion_tokens})")
print()

# Configuração 3: Balanceada (temperatura média, penalties leves)
print("=" * 60)
print("CONFIGURAÇÃO 3: Balanceada")
print("=" * 60)
print("Parâmetros: temperature=0.7, frequency_penalty=0.2, presence_penalty=0.1, max_tokens=200")
print()

response_3 = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'user',
            'content': pergunta
        }
    ],
    temperature=0.7,
    frequency_penalty=0.2,
    presence_penalty=0.1,
    max_tokens=200
)

print(response_3.choices[0].message.content)
print()
print(f"Tokens: {response_3.usage.total_tokens} (prompt: {response_3.usage.prompt_tokens}, completion: {response_3.usage.completion_tokens})")
print()

# COMPARAÇÃO
print("=" * 60)
print("COMPARAÇÃO DAS CONFIGURAÇÕES")
print("=" * 60)
print()

comparacao = {
    "Configuração 1 (Conservadora)": {
        "tokens": response_1.usage.completion_tokens,
        "caracteres": len(response_1.choices[0].message.content),
        "caracteristicas": "Resposta mais previsível, técnica, menos variação"
    },
    "Configuração 2 (Criativa)": {
        "tokens": response_2.usage.completion_tokens,
        "caracteres": len(response_2.choices[0].message.content),
        "caracteristicas": "Resposta mais variada, criativa, pode ser menos precisa"
    },
    "Configuração 3 (Balanceada)": {
        "tokens": response_3.usage.completion_tokens,
        "caracteres": len(response_3.choices[0].message.content),
        "caracteristicas": "Equilíbrio entre precisão e criatividade"
    }
}

for config, dados in comparacao.items():
    print(f"{config}:")
    print(f"  - Tokens: {dados['tokens']}")
    print(f"  - Caracteres: {dados['caracteres']}")
print(f"  - Características: {dados['caracteristicas']}")

