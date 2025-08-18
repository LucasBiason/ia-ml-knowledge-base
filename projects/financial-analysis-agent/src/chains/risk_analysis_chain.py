from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from ..prompts.financial_prompts import RISK_ANALYSIS_PROMPT
from ..core.config import config


class RiskAnalysisChain:
    """Chain específica para análise de risco"""

    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

    def analyze_stock(self, ticker: str, company_info: str = "") -> dict:
        """Executa análise de risco de uma ação"""
        try:
            # Se não foi fornecido company_info, criar um básico
            if not company_info:
                company_info = f"Análise de risco para {ticker}"

            # Executar análise de risco
            risk_chain = RISK_ANALYSIS_PROMPT | self.llm
            risk_result = risk_chain.invoke({
                "ticker": ticker,
                "company_info": company_info
            })
            return {
                "ticker": ticker,
                "analysis_type": "análise de risco",
                "company_info": company_info,
                "risk_analysis": risk_result,
                "status": "success"
            }

        except Exception as e:
            print(f"Erro durante análise de risco: {str(e)}")
            return {
                "ticker": ticker,
                "analysis_type": "análise de risco",
                "error": str(e),
                "status": "error"
            }
