from langchain.prompts import PromptTemplate


STOCK_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker", "analysis_type"],
    template="""
    Você é um analista financeiro especializado em ações brasileiras.

    Analise a ação: {ticker}
    Tipo de análise: {analysis_type}

    Forneça uma análise clara e educativa em português, incluindo:
    1. Visão geral da empresa
    2. Análise do setor
    3. Principais indicadores
    4. Recomendação (COMPRAR, MANTER ou VENDER)
    5. Justificativa da recomendação

    Seja objetivo e use linguagem acessível para investidores iniciantes.
    """
)


EXECUTIVE_SUMMARY_PROMPT = PromptTemplate(
    input_variables=["detailed_analysis"],
    template="""
    Com base na análise financeira fornecida, crie um resumo executivo conciso:

    {detailed_analysis}

    Resumo executivo (máximo 3 parágrafos):
    """
)


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


TECHNICAL_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker", "price_data"],
    template="""
    Você é um analista técnico especializado em ações brasileiras.

    Analise técnica da ação: {ticker}
    Dados de preço: {price_data}

    Forneça uma análise técnica incluindo:
    1. Tendência atual (alta, baixa, lateral)
    2. Suporte e resistência principais
    3. Indicadores técnicos relevantes
    4. Sinais de compra/venda
    5. Recomendação técnica

    Use linguagem técnica mas acessível.
    """
)


RISK_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=["ticker", "company_info"],
    template="""
    Você é um analista de risco especializado em ações brasileiras.

    Análise de risco da ação: {ticker}
    Informações da empresa: {company_info}

    Avalie os riscos incluindo:
    1. Riscos específicos da empresa
    2. Riscos do setor
    3. Riscos macroeconômicos
    4. Nível de risco geral (baixo, médio, alto)
    5. Recomendações de mitigação

    Seja objetivo e quantitativo quando possível.
    """
)
