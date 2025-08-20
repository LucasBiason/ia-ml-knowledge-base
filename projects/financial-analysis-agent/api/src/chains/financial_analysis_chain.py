"""
Chain para análise fundamentalista de ações.

Este módulo implementa a análise fundamentalista básica de ações,
combinando análise detalhada e resumo executivo.
"""

from typing import Dict, Any
from ..core.config import config
from ..prompts import STOCK_ANALYSIS_PROMPT, EXECUTIVE_SUMMARY_PROMPT
from langchain_openai import ChatOpenAI


class FinancialAnalysisChain:
    """
    Chain para análise fundamentalista básica de ações.

    Esta chain executa análises fundamentalistas completas, incluindo
    análise detalhada e geração de resumo executivo.
    """

    def __init__(self) -> None:
        """
        Inicializa a chain de análise fundamentalista.

        Valida as configurações e inicializa o modelo de linguagem.
        """
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

    def analyze_stock(
        self,
        ticker: str,
        analysis_type: str = "análise fundamentalista"
    ) -> Dict[str, Any]:
        """
        Executa análise fundamentalista de uma ação.

        Args:
            ticker: Código da ação (ex: PETR4, VALE3)
            analysis_type: Tipo de análise (padrão: análise fundamentalista)

        Returns:
            Dict contendo:
                - ticker: Código da ação
                - analysis_type: Tipo de análise executada
                - detailed_analysis: Análise detalhada
                - executive_summary: Resumo executivo
                - status: Status da operação ("success" ou "error")
                - error: Mensagem de erro (se status for "error")
        """
        try:
            # Análise detalhada
            analysis_chain = STOCK_ANALYSIS_PROMPT | self.llm
            analysis_result = analysis_chain.invoke({
                "ticker": ticker,
                "analysis_type": analysis_type
            })

            # Resumo executivo
            summary_chain = EXECUTIVE_SUMMARY_PROMPT | self.llm
            summary_result = summary_chain.invoke({
                "detailed_analysis": analysis_result.content
            })

            return {
                "ticker": ticker,
                "analysis_type": analysis_type,
                "detailed_analysis": analysis_result.content,
                "executive_summary": summary_result.content,
                "status": "success"
            }
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": analysis_type,
                "error": str(e),
                "status": "error"
            }

