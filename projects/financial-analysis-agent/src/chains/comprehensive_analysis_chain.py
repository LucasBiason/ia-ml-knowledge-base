from langchain_openai import ChatOpenAI
from ..prompts.financial_prompts import EXECUTIVE_SUMMARY_PROMPT_WITH_CONTEXT
from ..chains.analysis_chain import FinancialAnalysisChain
from ..chains.technical_analysis_chain import TechnicalAnalysisChain
from ..chains.risk_analysis_chain import RiskAnalysisChain
from ..core.config import config


class ComprehensiveAnalysisChain:
    """Chain para análise completa combinando todas as outras"""

    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

        # Criar instâncias das outras chains
        self.fundamental_chain = FinancialAnalysisChain()
        self.technical_chain = TechnicalAnalysisChain()
        self.risk_chain = RiskAnalysisChain()

    def analyze_stock(self, ticker: str) -> dict:
        """Executa análise completa combinando todas as chains"""
        try:
            # Passo 1: Obter preço atual
            from ..tools.stock_tools import StockPriceTool
            price_tool = StockPriceTool()
            current_price = price_tool._run(ticker)

            # Passo 2: Análise fundamentalista
            fundamental_result = self.fundamental_chain.analyze_stock(ticker)
            if fundamental_result["status"] == "error":
                return fundamental_result

            # Passo 3: Análise técnica
            technical_result = self.technical_chain.analyze_stock(
                ticker, current_price
            )
            if technical_result["status"] == "error":
                return technical_result

            # Passo 4: Análise de risco
            risk_result = self.risk_chain.analyze_stock(ticker)
            if risk_result["status"] == "error":
                return risk_result

            # Passo 5: Obter contexto de mercado
            from ..tools.stock_tools import MarketIndexTool
            market_tool = MarketIndexTool()
            market_context = market_tool._run("IBOV")

            # Passo 6: Gerar resumo executivo com contexto
            context_summary_chain = EXECUTIVE_SUMMARY_PROMPT_WITH_CONTEXT | self.llm
            context_summary = context_summary_chain.invoke({
                "ticker": ticker,
                "current_price": current_price,
                "detailed_analysis": fundamental_result['detailed_analysis'],
                "market_context": market_context
            })
            return {
                "ticker": ticker,
                "current_price": current_price,
                "fundamental_analysis": fundamental_result,
                "technical_analysis": technical_result,
                "risk_analysis": risk_result,
                "market_context": market_context,
                "contextual_summary": context_summary.content,
                "status": "success"
            }

        except Exception as e:
            print(f"Erro durante análise completa: {str(e)}")
            return {
                "ticker": ticker,
                "error": str(e),
                "status": "error"
            }
