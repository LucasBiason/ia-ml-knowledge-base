"""
Módulo de prompts financeiros para análise de ações.

Este módulo contém todos os templates de prompts utilizados pelo
LangChain para gerar análises financeiras especializadas.
"""

from langchain.prompts import PromptTemplate

# Prompt para análise fundamentalista de ações
STOCK_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker", "analysis_type"],
    template="""
    Analise a ação {ticker} com foco em {analysis_type}.

    Considere:
    - Indicadores financeiros
    - Crescimento da empresa
    - Setor e concorrência
    - Perspectivas futuras

    Forneça uma análise detalhada e objetiva.
    """
)

# Prompt para resumo executivo básico
EXECUTIVE_SUMMARY_PROMPT = PromptTemplate(
    input_variables=["detailed_analysis"],
    template="""
    Com base na análise detalhada abaixo, crie um resumo executivo conciso:

    {detailed_analysis}

    Resumo executivo (máximo 3 parágrafos):
    """
)

# Prompt para resumo executivo com contexto de mercado
EXECUTIVE_SUMMARY_PROMPT_WITH_CONTEXT = PromptTemplate(
    input_variables=["ticker", "current_price", "detailed_analysis", "market_context"],
    template="""
    Com base na análise financeira e no contexto de mercado, crie um resumo executivo:

    AÇÃO: {ticker}
    PREÇO ATUAL: {current_price}
    ANÁLISE DETALHADA: {detailed_analysis}
    CONTEXTO DE MERCADO: {market_context}

    Resumo executivo final (máximo 4 parágrafos):
    """
)

# Prompt para análise técnica
TECHNICAL_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker"],
    template="""
    Analise tecnicamente a ação {ticker}.

    Considere:
    - Médias móveis
    - Indicadores de momentum
    - Suporte e resistência
    - Volume de negociação
    - Padrões de gráfico

    Forneça uma análise técnica detalhada.
    """
)

# Prompt para análise de risco
RISK_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker", "company_info"],
    template="""
    Analise os riscos da ação {ticker}.

    Informações da empresa: {company_info}

    Considere:
    - Riscos operacionais
    - Riscos financeiros
    - Riscos de mercado
    - Riscos regulatórios
    - Mitigações de risco

    Forneça uma análise de risco detalhada.
    """
)
