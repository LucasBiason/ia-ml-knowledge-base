"""
Exercício 3: Integração com Dados Reais

Referência: 02-agentes-especializados.ipynb - Exercício 3

Descrição:
Leia dados de um arquivo CSV ou Excel e use como contexto para o agente.

Explicação:

Como integrar dados reais de arquivos CSV com agentes especializados.

Pontos importantes:

1. Leitura de Dados Reais:
   - Uso de pandas para ler arquivo CSV
   - Dados podem vir de qualquer fonte (CSV, Excel, banco de dados)
   - Processamento automático dos dados

2. Formatação para Contexto:
   - Dados estruturados são transformados em texto legível
   - Informações relevantes são mantidas
   - Formato claro para processamento

3. Integração Completa:
   - Fluxo: Dados reais → Processamento → Contexto → Agente → Análise
   - Fluxo completo de dados para insights
   - Aplicável a qualquer tipo de dados estruturados

4. Casos de Uso Reais:
   - Análise de vendas e estoque
   - Relatórios financeiros automatizados
   - Análise de dados de clientes
   - Processamento de logs e métricas

5. Melhorias Possíveis:
   - Ler de múltiplos arquivos ou pastas
   - Integrar com APIs externas
   - Processar dados em tempo real
   - Adicionar validação e tratamento de erros
   - Cache de dados para melhor performance

6. Exemplo com Excel:
   - pd.read_excel('arquivo.xlsx') para ler Excel
   - Mesmo processo de formatação
   - Suporta múltiplas planilhas

7. Exemplo com Banco de Dados:
   - Usar SQLAlchemy ou pandas.read_sql()
   - Consultas SQL diretas
   - Dados sempre atualizados
"""

import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 3: Integração com Dados Reais de CSV")
print("=" * 60)
print()

# Ler dados do arquivo CSV
csv_path = 'assets/produtos.csv'
df = pd.read_csv(csv_path)

print("Dados carregados do CSV:")
print(df.to_string(index=False))
print()

# Formatar dados para o contexto do agente
dados_formatados = []
dados_formatados.append("Catálogo de Produtos:\n")

for _, row in df.iterrows():
    produto = row['Produto']
    categoria = row['Categoria']
    preco = f"R$ {row['Preco']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
    estoque = int(row['Estoque'])
    vendas = int(row['Vendas_Mes'])
    dados_formatados.append(
        f"- {produto} ({categoria}): {preco} | Estoque: {estoque} | Vendas do mês: {vendas}"
    )

contexto_produtos = "\n".join(dados_formatados)

print("Dados formatados para o contexto:")
print(contexto_produtos)
print()

# Criar agente especializado em gestão de produtos
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': f'''Você é um assistente especializado em gestão de produtos e estoque.
            Você analisa dados de produtos, estoque e vendas para fornecer insights e recomendações.
            
            Dados dos produtos:
            {contexto_produtos}
            
            Ao analisar, considere:
            - Produtos com estoque baixo que precisam de reposição
            - Produtos com alta demanda (vendas)
            - Oportunidades de otimização de estoque
            - Produtos que podem estar com preço inadequado
            - Sugestões de compra baseadas em vendas e estoque atual
            '''
        },
        {
            'role': 'user',
            'content': 'Analise os dados dos produtos e me diga quais produtos precisam de reposição urgente e quais têm boa performance de vendas.'
        }
    ],
    temperature=0.6,
    max_tokens=400
)

print("Análise do agente com dados reais do CSV:")
print("-" * 60)
print(response.choices[0].message.content)

