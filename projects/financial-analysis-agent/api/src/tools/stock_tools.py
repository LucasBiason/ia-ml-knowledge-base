"""
Módulo de ferramentas para obtenção de dados financeiros.

Este módulo contém as ferramentas (tools) utilizadas pelo LangChain
para obter informações sobre preços de ações e índices de mercado.
"""

import random
from langchain.tools import BaseTool


class StockPriceTool(BaseTool):
    """
    Ferramenta para obter preços de ações.

    Simula a obtenção de preços reais de ações do mercado brasileiro.
    Em produção, deve ser integrada com APIs financeiras reais.
    """

    name: str = "stock_price"
    description: str = (
        "Obtém o preço atual de uma ação. "
        "Use quando precisar do preço de uma ação específica."
    )

    def _run(self, ticker: str) -> str:
        """
        Executa a obtenção do preço de uma ação de forma síncrona.

        Args:
            ticker: Código da ação (ex: PETR4, VALE3)

        Returns:
            str: String formatada com o preço da ação
        """
        # Simulação - em produção, integrar com API real
        base_prices = {
            "PETR4": 35.50,
            "VALE3": 68.20,
            "ITUB4": 32.15,
            "BBDC4": 16.80,
            "ABEV3": 12.45
        }

        if ticker in base_prices:
            variation = random.uniform(-0.05, 0.05)
            price = base_prices[ticker] * (1 + variation)
            return f"Preço atual de {ticker}: R$ {price:.2f}"
        else:
            simulated_price = random.uniform(10, 100)
            return f"Preço simulado de {ticker}: R$ {simulated_price:.2f}"

    def _arun(self, ticker: str) -> str:
        """
        Executa a obtenção do preço de uma ação de forma assíncrona.

        Args:
            ticker: Código da ação

        Returns:
            str: String formatada com o preço da ação
        """
        return self._run(ticker)


class MarketIndexTool(BaseTool):
    """
    Ferramenta para obter informações sobre índices de mercado.

    Simula a obtenção de dados de índices como Ibovespa, IFIX, etc.
    Em produção, deve ser integrada com APIs financeiras reais.
    """

    name: str = "market_index"
    description: str = (
        "Obtém informações sobre índices de mercado. "
        "Use para contexto macroeconômico."
    )

    def _run(self, index_name: str = "IBOVESPA") -> str:
        """
        Executa a obtenção de dados de índice de mercado de forma síncrona.

        Args:
            index_name: Nome do índice (padrão: IBOVESPA)

        Returns:
            str: String formatada com o valor do índice
        """
        # Simulação - em produção, integrar com API real
        base_values = {
            "IBOVESPA": 120000,
            "IFIX": 2800,
            "IDIV": 1500,
            "SMLL": 25000
        }

        if index_name in base_values:
            variation = random.uniform(-0.02, 0.02)
            value = base_values[index_name] * (1 + variation)
            return f"{index_name}: {value:.0f} pontos"
        else:
            simulated_value = random.uniform(1000, 200000)
            return f"Índice {index_name}: {simulated_value:.0f} pontos"

    def _arun(self, index_name: str = "IBOVESPA") -> str:
        """
        Executa a obtenção de dados de índice de mercado de forma assíncrona.

        Args:
            index_name: Nome do índice

        Returns:
            str: String formatada com o valor do índice
        """
        return self._run(index_name)
