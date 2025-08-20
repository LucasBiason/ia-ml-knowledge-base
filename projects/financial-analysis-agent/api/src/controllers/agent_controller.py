from typing import Dict, Any
from src.agents.advanced_financial_agent import AdvancedFinancialAgent

class AgentController:
    """Controller para operações gerais do agente"""

    def __init__(self):
        self.agent = AdvancedFinancialAgent()

    def ask_question(self, question: str) -> str:
        """Faz uma pergunta geral para o agente"""
        try:
            return self.agent.ask_question(question)
        except Exception as e:
            return f"Erro ao processar pergunta: {str(e)}"

    def get_available_tools(self) -> list:
        """Retorna as ferramentas disponíveis"""
        try:
            return self.agent.get_available_tools()
        except Exception as e:
            return []

    def get_agent_status(self) -> Dict[str, Any]:
        """Retorna o status do agente"""
        try:
            # Verificar se o agente está funcionando
            tools = self.agent.get_available_tools()
            return {
                "status": "healthy",
                "agent": "available",
                "tools_count": len(tools)
            }
        except Exception as e:
            return {
                "status": "unhealthy",
                "error": str(e)
            }
