from langchain_openai import ChatOpenAI
from ..prompts import EXECUTIVE_SUMMARY_PROMPT_WITH_CONTEXT
from .financial_analysis_chain import FinancialAnalysisChain
from .technical_analysis_chain import TechnicalAnalysisChain
from .risk_analysis_chain import RiskAnalysisChain
from ..core.config import config


class ComprehensiveAnalysisChain:
    """Chain para análise abrangente combinando múltiplas análises"""
    
    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )
        
        self.fundamental_chain = FinancialAnalysisChain()
        self.technical_chain = TechnicalAnalysisChain()
        self.risk_chain = RiskAnalysisChain()
    
    def analyze_stock(self, ticker: str) -> dict:
        """Executa análise abrangente de uma ação"""
        try:
            # Executar análises individuais
            fundamental_result = self.fundamental_chain.analyze_stock(ticker)
            technical_result = self.technical_chain.analyze_stock(ticker)
            risk_result = self.risk_chain.analyze_stock(ticker)
            
            # Verificar se alguma análise falhou
            if (fundamental_result["status"] == "error" or 
                technical_result["status"] == "error" or 
                risk_result["status"] == "error"):
                return {
                    "ticker": ticker,
                    "analysis_type": "análise abrangente",
                    "error": "Uma ou mais análises falharam",
                    "status": "error"
                }
            
            # Criar resumo executivo com contexto
            summary_chain = EXECUTIVE_SUMMARY_PROMPT_WITH_CONTEXT | self.llm
            summary_result = summary_chain.invoke({
                "ticker": ticker,
                "current_price": "Preço não disponível",
                "detailed_analysis": fundamental_result["detailed_analysis"],
                "market_context": f"Análise técnica: {technical_result['technical_analysis']}. Análise de risco: {risk_result['risk_analysis']}"
            })
            
            return {
                "ticker": ticker,
                "analysis_type": "análise abrangente",
                "fundamental_analysis": fundamental_result["detailed_analysis"],
                "technical_analysis": technical_result["technical_analysis"],
                "risk_analysis": risk_result["risk_analysis"],
                "contextual_summary": summary_result.content,
                "status": "success"
            }
        except Exception as e:
            return {
                "ticker": ticker,
                "analysis_type": "análise abrangente",
                "error": str(e),
                "status": "error"
            }
