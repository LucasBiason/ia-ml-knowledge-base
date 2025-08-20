"""
Controller para operações de análise financeira.

Este módulo implementa a lógica de negócio para diferentes tipos
de análise financeira, delegando a execução para o agente especializado.
"""

from typing import Dict, Any
from src.agents.advanced_financial_agent import AdvancedFinancialAgent


class AnalysisController:
    """
    Controller para operações de análise financeira.

    Coordena diferentes tipos de análise financeira, fornecendo
    uma interface unificada para o sistema de análise.
    """

    def __init__(self) -> None:
        """
        Inicializa o controller de análise.

        Cria uma instância do agente financeiro avançado
        para executar as análises.
        """
        self.agent = AdvancedFinancialAgent()

    def analyze_fundamental(
        self,
        ticker: str,
        analysis_type: str
    ) -> Dict[str, Any]:
        """
        Executa análise fundamentalista de uma ação.

        Args:
            ticker: Código da ação (ex: PETR4, VALE3)
            analysis_type: Tipo de análise fundamentalista

        Returns:
            Dict com resultado da análise ou erro
        """
        try:
            result = self.agent.analyze_fundamental(ticker)
            return result
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": analysis_type,
                "error": str(e),
                "status": "error"
            }

    def analyze_technical(self, ticker: str) -> Dict[str, Any]:
        """
        Executa análise técnica de uma ação.

        Args:
            ticker: Código da ação

        Returns:
            Dict com resultado da análise técnica ou erro
        """
        try:
            result = self.agent.analyze_technical(ticker)
            return result
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": "análise técnica",
                "error": str(e),
                "status": "error"
            }

    def analyze_risk(
        self,
        ticker: str,
        company_info: str
    ) -> Dict[str, Any]:
        """
        Executa análise de risco de uma ação.

        Args:
            ticker: Código da ação
            company_info: Informações adicionais da empresa

        Returns:
            Dict com resultado da análise de risco ou erro
        """
        try:
            result = self.agent.analyze_risk(ticker, company_info)
            return result
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": "análise de risco",
                "error": str(e),
                "status": "error"
            }

    def analyze_comprehensive(self, ticker: str) -> Dict[str, Any]:
        """
        Executa análise abrangente de uma ação.

        Combina análise fundamental, técnica e de risco
        em uma única análise completa.

        Args:
            ticker: Código da ação

        Returns:
            Dict com resultado da análise abrangente ou erro
        """
        try:
            result = self.agent.analyze_comprehensive(ticker)
            return result
        except Exception as e:
            return {
                "ticker": ticker,
                "error": str(e),
                "status": "error"
            }
