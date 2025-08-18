from langchain_openai import ChatOpenAI
from ..prompts.financial_prompts import TECHNICAL_ANALYSIS_PROMPT
from ..core.config import config


class TechnicalAnalysisChain:
    """Chain específica para análise técnica"""

    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

    def analyze_stock(self, ticker: str, price_data: str = "") -> dict:
        """Executa análise técnica de uma ação"""
        try:
            # Se não foi fornecido price_data, usar ferramenta para obter
            if not price_data:
                from ..tools.stock_tools import StockPriceTool
                price_tool = StockPriceTool()
                price_data = price_tool._run(ticker)

            # Executar análise técnica
            technical_chain = TECHNICAL_ANALYSIS_PROMPT | self.llm
            technical_result = technical_chain.invoke({
                "ticker": ticker,
                "price_data": price_data
            })
            return {
                "ticker": ticker,
                "analysis_type": "análise técnica",
                "price_data": price_data,
                "technical_analysis": technical_result,
                "status": "success"
            }

        except Exception as e:
            print(f"Erro durante análise técnica: {str(e)}")
            return {
                "ticker": ticker,
                "analysis_type": "análise técnica",
                "error": str(e),
                "status": "error"
            }
