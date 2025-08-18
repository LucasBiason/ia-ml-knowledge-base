"""
Criando um agente financeiro avançado que combina chains e tools.
Combina chains e tools de forma inteligente,
executa análises completas com preço + análise + contexto,
mantém memória da conversa, fornece múltiplas interfaces
para diferentes tipos de análise.
"""
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from ..tools.stock_tools import StockPriceTool, MarketIndexTool
from ..chains import (
    FinancialAnalysisChain,
    TechnicalAnalysisChain,
    RiskAnalysisChain,
    ComprehensiveAnalysisChain
)
from ..core.config import config


class AdvancedFinancialAgent:
    """Agente financeiro avançado que combina chains e tools"""

    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

        self.tools = [
            StockPriceTool(),
            MarketIndexTool()
        ]

        self.fundamental_chain = FinancialAnalysisChain()
        self.technical_chain = TechnicalAnalysisChain()
        self.risk_chain = RiskAnalysisChain()
        self.comprehensive_chain = ComprehensiveAnalysisChain()

        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3
        )

    def analyze_fundamental(self, ticker: str) -> dict:
        """Análise fundamentalista"""
        return self.fundamental_chain.analyze_stock(ticker)

    def analyze_technical(self, ticker: str) -> dict:
        """Análise técnica"""
        return self.technical_chain.analyze_stock(ticker)

    def analyze_risk(self, ticker: str, company_info: str = "") -> dict:
        """Análise de risco"""
        return self.risk_chain.analyze_stock(ticker, company_info)

    def analyze_comprehensive(self, ticker: str) -> dict:
        """Análise completa"""
        return self.comprehensive_chain.analyze_stock(ticker)

    def ask_question(self, question: str) -> str:
        """Pergunta geral"""
        return self.agent.run(question)

    def get_conversation_history(self) -> list:
        return self.memory.buffer

    def clear_memory(self):
        self.memory.clear()
