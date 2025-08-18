from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from .config import config


class LangChainClient:
    """Cliente simplificado para consultas básicas a LLM OpenAI"""

    def __init__(self):
        config.validate()
        self.llm = ChatOpenAI(
            api_key=config.OPENAI_API_KEY,
            model_name=config.OPENAI_MODEL,
            temperature=config.TEMPERATURE
        )

    def simple_query(self, prompt: str) -> str:
        """Consulta simples sem contexto"""
        try:
            response = self.llm.invoke(prompt)
            return response.content
        except Exception as e:
            return f"Erro na consulta: {str(e)}"

    def contextual_query(self, system_prompt: str, user_prompt: str) -> str:
        """Consulta com contexto de sistema"""
        try:
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(content=user_prompt)
            ]
            response = self.llm.invoke(messages)
            return response.content
        except Exception as e:
            return f"Erro na consulta: {str(e)}"
