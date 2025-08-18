from langchain.tools import BaseTool
from typing import Optional, Any
import json


class StockPriceTool(BaseTool):
    """Ferramenta para obter preços de ações (simulado)"""

    name: str = "stock_price"
    description: str = """Obtém o preço atual de uma ação.
    Use quando precisar do preço de uma ação específica."""

    def _run(self, ticker: str) -> str:
        """Executa a ferramenta de forma síncrona"""
        # Simulação simples - integrar com APIs reais depois
        simulated_prices = {
            "PETR4": {"price": "R$ 32,50", "change": "+2.1%", "volume": "45.2M"},
            "VALE3": {"price": "R$ 68,20", "change": "-1.3%", "volume": "23.1M"},
            "ITUB4": {"price": "R$ 28,90", "change": "+0.8%", "volume": "18.7M"},
            "BBDC4": {"price": "R$ 15,75", "change": "-0.5%", "volume": "12.3M"},
            "ABEV3": {"price": "R$ 12,45", "change": "+1.2%", "volume": "8.9M"}
        }

        ticker_upper = ticker.upper()
        if ticker_upper in simulated_prices:
            data = simulated_prices[ticker_upper]
            return f"""Preço atual de {ticker_upper}:
        {data['price']} | Variação: {data['change']} | Volume: {data['volume']}"""
        else:
            return f"""Preço não disponível para {ticker_upper}.
            Ações disponíveis: {', '.join(simulated_prices.keys())}"""

    def _arun(self, ticker: str) -> Any:
        """Versão assíncrona (implementação futura)"""
        return self._run(ticker)


class MarketIndexTool(BaseTool):
    """Ferramenta para obter índices de mercado (simulado)"""

    name: str = "market_index"
    description: str = """Obtém informações sobre índices de mercado como
    Ibovespa, S&P 500, etc."""

    def _run(self, index_name: str = "IBOV") -> str:
        """Executa a ferramenta de forma síncrona"""
        # Simulação simples - integrar com APIs reais depois
        simulated_indices = {
            "IBOV": {"value": "128.450", "change": "+1.2%", "status": "Alta"},
            "SP500": {"value": "4.850", "change": "+0.8%", "status": "Alta"},
            "NASDAQ": {"value": "15.200", "change": "-0.3%", "status": "Baixa"},
            "DOW": {"value": "38.500", "change": "+0.5%", "status": "Alta"}
        }

        index_upper = index_name.upper()
        if index_upper in simulated_indices:
            data = simulated_indices[index_upper]
            return f"""Índice {index_upper}:
        {data['value']} | Variação: {data['change']} | Status: {data['status']}"""
        else:
            return f"""Índice {index_upper} não disponível.
        Índices disponíveis: {', '.join(simulated_indices.keys())}"""

    def _arun(self, index_name: str) -> Any:
        """Versão assíncrona (implementação futura)"""
        return self._run(index_name)
