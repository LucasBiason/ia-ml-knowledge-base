from ..core.config import config
from ..prompts import RISK_ANALYSIS_PROMPT
from langchain_openai import ChatOpenAI


class RiskAnalysisChain:
    """Chain para análise de risco"""
    
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
            analysis_chain = RISK_ANALYSIS_PROMPT | self.llm
            analysis_result = analysis_chain.invoke({
                "ticker": ticker,
                "company_info": company_info
            })
            
            return {
                "ticker": ticker,
                "analysis_type": "análise de risco",
                "risk_analysis": analysis_result.content,
                "status": "success"
            }
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": "análise de risco",
                "error": str(e),
                "status": "error"
            }
