"""
Criando um agente financeiro simples e funcional.
Vamos criar um agente que pode usar multiplas ferramentas,
coordenar ações para preço e indices, mantem o contexto da conversa
e fornece Interface Simples para fazer perguntas.
"""

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
from langchain.memory import ConversationBufferMemory
from ..tools.stock_tools import StockPriceTool, MarketIndexTool
from ..core.config import config


def create_simple_financial_agent():
    """Cria um agente financeiro simples e funcional"""
    config.validate()

    llm = ChatOpenAI(
        api_key=config.OPENAI_API_KEY,
        model_name=config.OPENAI_MODEL,
        temperature=config.TEMPERATURE
    )

    tools = [
        StockPriceTool(),
        MarketIndexTool()
    ]

    # Memória para manter contexto da conversa
    memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

    # Criar agente
    agent = initialize_agent(
        tools=tools,  # Lista de ferramentas
        llm=llm,  # Modelo de linguagem
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Tipo de agente
        memory=memory,  # Memória para contexto
        verbose=True,  # Mostra processo de decisão
        handle_parsing_errors=True,  # Trata erros automaticamente
        max_iterations=5  # Máximo de 5 ações por pergunta
    )

    return agent


class FinancialAgent:
    """Classe wrapper para o agente financeiro"""

    def __init__(self):
        self.agent = create_simple_financial_agent()
        self.memory = self.agent.memory

    def ask(self, question: str) -> str:
        """Faz uma pergunta para o agente"""
        try:
            response = self.agent.run(question)
            return response

        except Exception as e:
            error_msg = f"Erro durante a execução: {str(e)}"
            print(f"Erro:{error_msg}")
            return error_msg

    def get_conversation_history(self) -> list:
        """Retorna o histórico da conversa"""
        return self.memory.buffer

    def clear_memory(self):
        """Limpa a memória da conversa"""
        self.memory.clear()
        print("Memória limpa!")

    def get_available_tools(self) -> list:
        """Retorna as ferramentas disponíveis"""
        return [tool.name for tool in self.agent.tools]
