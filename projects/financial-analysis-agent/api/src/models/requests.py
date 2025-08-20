"""
Modelos de requisição para a API.

Este módulo define os modelos Pydantic para validação
e serialização de requisições da API.
"""

from pydantic import BaseModel, Field
from typing import Optional


class StockAnalysisRequest(BaseModel):
    """
    Modelo para requisição de análise de ações.

    Valida e estrutura os dados de entrada para análises
    financeiras de ações específicas.
    """

    ticker: str = Field(
        ...,
        description="Código da ação (ex: PETR4, VALE3)",
        min_length=1,
        max_length=10
    )
    analysis_type: str = Field(
        default="análise fundamentalista",
        description="Tipo de análise a ser executada"
    )
    company_info: Optional[str] = Field(
        default="",
        description="Informações adicionais da empresa (opcional)"
    )


class QuestionRequest(BaseModel):
    """
    Modelo para requisição de pergunta geral.

    Valida e estrutura perguntas gerais sobre
    mercado financeiro para o agente de IA.
    """

    question: str = Field(
        ...,
        description="Pergunta sobre mercado financeiro",
        min_length=1,
        max_length=1000
    )
