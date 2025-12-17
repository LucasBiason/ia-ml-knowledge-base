"""
Exercício 1: Criar Agente de Recomendações

Referência: 02-agentes-especializados.ipynb - Exercício 1

Descrição:
Crie um agente especializado em recomendar filmes. Inclua uma lista de filmes populares no contexto.

Explicação:

Como criar um agente especializado com contexto de dados.

Pontos importantes:

1. Contexto Rico:
   - Lista de filmes organizada por gênero
   - Cada filme tem descrição breve para o agente entender o contexto
   - Permite recomendações mais precisas e personalizadas

2. Instruções Específicas:
   - Papel do agente definido claramente (crítico de cinema)
   - Critérios de recomendação especificados
   - Agente orientado a explicar suas escolhas

3. Estrutura do Contexto:
   - Filmes organizados por gênero para facilitar busca
   - Informações relevantes incluídas (ano, gênero, descrição)
   - Formato claro e estruturado

4. Aplicação Prática:
   - Este padrão pode ser usado para qualquer tipo de recomendação
   - Produtos, restaurantes, livros, músicas, etc.
   - Basta adaptar o contexto e as instruções

5. Melhorias Possíveis:
   - Adicionar mais informações (avaliações, elenco, diretor)
   - Ler dados de um banco de dados ou API
   - Incluir histórico de preferências do usuário
   - Adicionar filtros (ano, gênero, duração)
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
print("EXERCÍCIO 1: Agente de Recomendações de Filmes")
print("=" * 60)
print()

# Lista de filmes populares para incluir no contexto
filmes_populares = """
Filmes Populares Disponíveis:

Ação/Aventura:
- Duna: Parte Dois (2024) - Ficção científica épica
- Oppenheimer (2023) - Drama histórico
- Top Gun: Maverick (2022) - Ação aérea
- Spider-Man: No Way Home (2021) - Super-herói

Drama:
- Everything Everywhere All at Once (2022) - Drama/Fantasia
- The Fabelmans (2022) - Drama autobiográfico
- CODA (2021) - Drama familiar
- Nomadland (2020) - Drama independente

Comédia:
- The Menu (2022) - Thriller/Comédia
- Glass Onion (2022) - Mistério/Comédia
- Free Guy (2021) - Comédia/Ação
- Palm Springs (2020) - Comédia romântica

Terror/Suspense:
- Nope (2022) - Terror/Suspense
- Get Out (2017) - Thriller psicológico
- Hereditary (2018) - Terror psicológico
- The Invisible Man (2020) - Thriller de ficção científica
"""

# Criar agente especializado em recomendar filmes
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': f'''Você é um crítico de cinema especializado em recomendar filmes.
            Você conhece profundamente diferentes gêneros, estilos e preferências de público.
            Sempre recomende filmes baseado no gosto do usuário, explicando por que aquele filme
            é adequado para ele.
            
            Base de filmes disponíveis:
            {filmes_populares}
            
            Quando o usuário pedir uma recomendação, considere:
            - Gêneros preferidos
            - Humor do momento
            - Preferências de estilo (ação, drama, comédia, etc.)
            - Se quer algo novo ou clássico
            '''
        },
        {
            'role': 'user',
            'content': 'Estou procurando um filme para assistir hoje à noite. Gosto de suspense e filmes que me fazem pensar. O que você recomenda?'
        }
    ],
    temperature=0.7,
    max_tokens=300
)

print("Recomendação do agente especializado:")
print("-" * 60)
print(response.choices[0].message.content)

