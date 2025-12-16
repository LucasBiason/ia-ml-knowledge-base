"""
Exercício 1: Criar um Assistente de Culinária

Referência: 01-conversa-basica.ipynb - Exercício 1

Descrição:
Crie um assistente especializado em receitas culinárias. Faça uma pergunta sobre 
como fazer um prato específico.

Dica: Use role: "system" para definir o contexto do assistente.

Explicação:

Uso da role 'system' para criar um assistente especializado.

Pontos importantes:

1. Role 'system': Define o contexto e comportamento do assistente
   - Neste caso, configurado como 'chef de cozinha profissional'
   - Isso faz o modelo responder sempre no contexto culinário

2. Especificidade do contexto:
   - Quanto mais específico o contexto, melhor a resposta
   - Características: 'profissional', 'especializado', 'detalhado'

3. Parâmetros utilizados:
   - temperature=0.7: Equilíbrio entre criatividade e precisão
   - max_tokens=500: Limita o tamanho da resposta

4. Aplicação prática:
   - Este padrão pode ser usado para qualquer especialidade
   - Basta mudar o contexto do 'system' para outro domínio
   - Exemplos: médico, advogado, programador, professor, etc.
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
print("EXERCÍCIO 1: Assistente de Culinária")
print("=" * 60)
print()

# Criar assistente especializado em culinária usando role "system"
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "Você é um chef de cozinha profissional especializado em receitas culinárias. "
                       "Forneça receitas detalhadas, dicas de preparo e informações sobre ingredientes. "
                       "Seja claro, didático e sempre mencione dicas importantes de preparo."
        },
        {
            "role": "user",
            "content": "Como fazer um risotto de cogumelos? Me dê a receita completa."
        }
    ],
    temperature=0.7,
    max_tokens=500
)

print("Resposta do Assistente de Culinária:")
print("-" * 60)
print(response.choices[0].message.content)

