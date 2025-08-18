from langchain_openai import ChatOpenAI
from ..prompts.financial_prompts import STOCK_ANALYSIS_PROMPT, EXECUTIVE_SUMMARY_PROMPT
from ..core.config import config


class FinancialAnalysisChain:
    """Chain simples para análise financeira"""

    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

    def analyze_stock(self, ticker: str,
                      analysis_type: str = "análise fundamentalista"):
        """Analisa uma ação e retorna análise + resumo"""
        try:
            analysis_chain = STOCK_ANALYSIS_PROMPT | self.llm
            analysis_result = analysis_chain.invoke({
                "ticker": ticker,
                "analysis_type": analysis_type
            })
            summary_chain = EXECUTIVE_SUMMARY_PROMPT | self.llm
            summary_result = summary_chain.invoke({
                "detailed_analysis": analysis_result
            })
            return {
                "ticker": ticker,
                "analysis_type": analysis_type,
                "detailed_analysis": analysis_result,
                "executive_summary": summary_result,
                "status": "success"
            }

        except Exception as e:
            print(f"Erro durante a análise: {str(e)}")
            return {
                "ticker": ticker,
                "analysis_type": analysis_type,
                "error": str(e),
                "status": "error"
            }

    def get_analysis_types(self):
        """Retorna os tipos de análise disponíveis"""
        return [
            "análise fundamentalista",
            "análise técnica",
            "análise de setor",
            "análise de risco",
            "análise de valor"
        ]
