from langchain_openai import ChatOpenAI
from ..prompts import TECHNICAL_ANALYSIS_PROMPT
from ..core.config import config


class TechnicalAnalysisChain:
    """Chain para análise técnica"""
    
    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )
    
    def analyze_stock(self, ticker: str) -> dict:
        """Executa análise técnica de uma ação"""
        try:
            analysis_chain = TECHNICAL_ANALYSIS_PROMPT | self.llm
            analysis_result = analysis_chain.invoke({"ticker": ticker})
            
            return {
                "ticker": ticker,
                "analysis_type": "análise técnica",
                "technical_analysis": analysis_result.content,
                "status": "success"
            }
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": "análise técnica",
                "error": str(e),
                "status": "error"
            }
