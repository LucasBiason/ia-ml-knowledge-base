"""
Exercício 2: Agente de Análise Financeira

Referência: 02-agentes-especializados.ipynb - Exercício 2

Descrição:
Crie um agente que analisa dados financeiros. Simule dados de receitas e despesas.

Explicação:

Como criar um agente especializado em análise de dados financeiros.

Pontos importantes:

1. Estrutura de Dados Clara:
   - Dados organizados em categorias (Receitas, Despesas, Resultado)
   - Totais e percentuais facilitam a análise
   - Formato tabular facilita compreensão

2. Contexto Especializado:
   - O agente é configurado como 'analista financeiro experiente'
   - Tipo de análise esperada é especificado
   - Orientações sobre o que considerar na análise

3. Parâmetros Ajustados:
   - temperature=0.5: Análises financeiras precisam ser precisas
   - max_tokens=500: Espaço suficiente para análise detalhada
   - Modelo adequado para análise de dados estruturados

4. Casos de Uso Reais:
   - Análise mensal/trimestral de resultados
   - Relatórios financeiros automatizados
   - Alertas sobre despesas elevadas
   - Recomendações de otimização

5. Melhorias Possíveis:
   - Integrar com planilhas Excel ou sistemas contábeis
   - Comparar períodos (mês anterior, mesmo período ano passado)
   - Adicionar gráficos e visualizações
   - Criar alertas automáticos para despesas acima do esperado

6. Dados em Produção:
   - Em produção, dados viriam de banco de dados ou APIs
   - Poderia usar pandas para processar dados de CSV/Excel
   - Integração com sistemas ERP ou contábeis
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
print("EXERCÍCIO 2: Agente de Análise Financeira")
print("=" * 60)
print()

# Dados financeiros simulados
dados_financeiros = """
Análise Financeira - Trimestre Q1 2025

RECEITAS:
- Vendas de Produtos: R$ 450.000
- Serviços Prestados: R$ 180.000
- Receitas de Investimentos: R$ 12.000
- Outras Receitas: R$ 8.000
Total de Receitas: R$ 650.000

DESPESAS:
- Salários e Benefícios: R$ 280.000
- Aluguel e Utilidades: R$ 45.000
- Marketing e Publicidade: R$ 75.000
- Fornecedores e Matérias-Primas: R$ 120.000
- Tecnologia e Software: R$ 25.000
- Outras Despesas Operacionais: R$ 35.000
Total de Despesas: R$ 580.000

RESULTADO:
- Lucro Líquido: R$ 70.000
- Margem de Lucro: 10,8%
"""

# Criar agente especializado em análise financeira
response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
        {
            'role': 'system',
            'content': f'''Você é um analista financeiro experiente especializado em análise de dados contábeis.
            Você analisa receitas, despesas, lucros e fornece insights acionáveis para tomada de decisão.
            Sempre identifique pontos de atenção, oportunidades de melhoria e tendências.
            
            Dados financeiros para análise:
            {dados_financeiros}
            
            Ao analisar, considere:
            - Proporções entre receitas e despesas
            - Categorias que consomem mais recursos
            - Margem de lucro e rentabilidade
            - Oportunidades de otimização
            - Alertas sobre despesas elevadas
            '''
        },
        {
            'role': 'user',
            'content': 'Analise esses dados financeiros e me dê os principais insights e recomendações.'
        }
    ],
    temperature=0.5,  # Menor temperatura para análises mais precisas
    max_tokens=500
)

print("Análise do agente especializado em finanças:")
print("-" * 60)
print(response.choices[0].message.content)

