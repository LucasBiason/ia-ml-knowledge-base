"""
Agente financeiro avançado que combina chains e tools.

Este módulo implementa um agente inteligente que coordena diferentes
tipos de análise financeira, combinando chains especializadas com
ferramentas de obtenção de dados.
"""

from typing import Dict, Any, List
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
    """
    Agente financeiro avançado que combina chains e tools.

    Este agente coordena diferentes tipos de análise financeira,
    mantém memória de conversas e fornece uma interface unificada
    para análise de ações.
    """

    def __init__(self) -> None:
        """
        Inicializa o agente financeiro avançado.

        Configura o modelo de linguagem, ferramentas, chains
        especializadas e memória de conversa.
        """
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

        # Ferramentas para obtenção de dados
        self.tools = [
            StockPriceTool(),
            MarketIndexTool()
        ]

        # Chains especializadas para diferentes tipos de análise
        self.fundamental_chain = FinancialAnalysisChain()
        self.technical_chain = TechnicalAnalysisChain()
        self.risk_chain = RiskAnalysisChain()
        self.comprehensive_chain = ComprehensiveAnalysisChain()

        # Memória para manter histórico de conversas
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )

        # Agente principal que coordena tools e memória
        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            memory=self.memory,
            verbose=True,
            handle_parsing_errors=True,
            max_iterations=3
        )

    def analyze_fundamental(self, ticker: str) -> Dict[str, Any]:
        """
        Executa análise fundamentalista de uma ação.

        Args:
            ticker: Código da ação (ex: PETR4, VALE3)

        Returns:
            Dict com resultado da análise fundamentalista
        """
        return self.fundamental_chain.analyze_stock(ticker)

    def analyze_technical(self, ticker: str) -> Dict[str, Any]:
        """
        Executa análise técnica de uma ação.

        Args:
            ticker: Código da ação

        Returns:
            Dict com resultado da análise técnica
        """
        return self.technical_chain.analyze_stock(ticker)

    def analyze_risk(
        self,
        ticker: str,
        company_info: str = ""
    ) -> Dict[str, Any]:
        """
        Executa análise de risco de uma ação.

        Args:
            ticker: Código da ação
            company_info: Informações adicionais da empresa (opcional)

        Returns:
            Dict com resultado da análise de risco
        """
        return self.risk_chain.analyze_stock(ticker, company_info)

    def analyze_comprehensive(self, ticker: str) -> Dict[str, Any]:
        """
        Executa análise abrangente de uma ação.

        Combina análise fundamental, técnica e de risco
        em uma única análise completa.

        Args:
            ticker: Código da ação

        Returns:
            Dict com resultado da análise abrangente
        """
        return self.comprehensive_chain.analyze_stock(ticker)

    def ask_question(self, question: str) -> str:
        """
        Faz uma pergunta geral ao agente.

        Args:
            question: Pergunta sobre mercado financeiro

        Returns:
            str: Resposta do agente
        """
        return self.agent.run(question)

    def get_conversation_history(self) -> List[Any]:
        """
        Retorna o histórico de conversas.

        Returns:
            Lista com mensagens da conversa
        """
        return self.memory.buffer

    def clear_memory(self) -> None:
        """
        Limpa o histórico de conversas.
        """
        self.memory.clear()

    def get_available_tools(self) -> List[str]:
        """
        Retorna as ferramentas disponíveis.

        Returns:
            Lista com nomes das ferramentas disponíveis
        """
        return [tool.name for tool in self.tools]
