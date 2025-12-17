"""
Exercício 2: Comparar Modelos

Referência: 01-conversa-basica.ipynb - Exercício 2

Descrição:
Teste a mesma pergunta com gpt-3.5-turbo e gpt-4 e compare as respostas.

Explicação:

Diferenças entre os modelos:

1. GPT-3.5-turbo:
   - Mais rápido e econômico
   - Adequado para a maioria dos casos de uso
   - Respostas boas, mas podem ser menos detalhadas
   - Custo: ~$0.50/1M tokens entrada, ~$1.50/1M tokens saída

2. GPT-4:
   - Mais poderoso e preciso
   - Melhor compreensão de contexto complexo
   - Respostas mais detalhadas e elaboradas
   - Mais caro que GPT-3.5-turbo
   - Melhor para tarefas que exigem raciocínio profundo

3. Quando usar cada um:
   - GPT-3.5-turbo: Chatbots, respostas rápidas, maioria dos casos
   - GPT-4: Análise complexa, raciocínio, tarefas que exigem precisão

4. Observações:
   - Ambos os modelos podem dar respostas excelentes
   - A escolha depende do caso de uso e orçamento
   - Para produção, comece com GPT-3.5-turbo e avalie se precisa do GPT-4
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Pergunta que será testada em ambos os modelos
pergunta = "Explique o conceito de programação orientada a objetos de forma clara e didática."

print("=" * 60)
print("EXERCÍCIO 2: Comparar Modelos")
print("=" * 60)
print()
print(f"Pergunta: {pergunta}")
print()

# RESPOSTA DO EXERCÍCIO - GPT-3.5-turbo
print("=" * 60)
print("RESPOSTA 1: GPT-3.5-turbo")
print("=" * 60)
print()

response_gpt35 = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ],
    temperature=0.7,
    max_tokens=300
)

print(response_gpt35.choices[0].message.content)
print()
print(f"Tokens usados: {response_gpt35.usage.total_tokens}")
print(f"  - Prompt: {response_gpt35.usage.prompt_tokens}")
print(f"  - Resposta: {response_gpt35.usage.completion_tokens}")
print()

# RESPOSTA DO EXERCÍCIO - GPT-4
print("=" * 60)
print("RESPOSTA 2: GPT-4")
print("=" * 60)
print()

response_gpt4 = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "user",
            "content": pergunta
        }
    ],
    temperature=0.7,
    max_tokens=300
)

print(response_gpt4.choices[0].message.content)
print()
print(f"Tokens usados: {response_gpt4.usage.total_tokens}")
print(f"  - Prompt: {response_gpt4.usage.prompt_tokens}")
print(f"  - Resposta: {response_gpt4.usage.completion_tokens}")
print()

# COMPARAÇÃO
print("=" * 60)
print("COMPARAÇÃO")
print("=" * 60)
print()

tamanho_gpt35 = len(response_gpt35.choices[0].message.content)
tamanho_gpt4 = len(response_gpt4.choices[0].message.content)

print(f"Tamanho da resposta GPT-3.5-turbo: {tamanho_gpt35} caracteres")
print(f"Tamanho da resposta GPT-4: {tamanho_gpt4} caracteres")
print()
print(f"Tokens GPT-3.5-turbo: {response_gpt35.usage.total_tokens}")
print(f"Tokens GPT-4: {response_gpt4.usage.total_tokens}")

