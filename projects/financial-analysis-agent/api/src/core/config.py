"""
Módulo de configuração centralizada da aplicação.

Este módulo gerencia todas as variáveis de ambiente e configurações
necessárias para o funcionamento do Financial Analysis Agent.
"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Classe de configuração centralizada da aplicação.

    Gerencia variáveis de ambiente e validações necessárias
    para o funcionamento correto do sistema.
    """

    OPENAI_API_KEY: Optional[str] = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    TEMPERATURE: float = float(os.getenv("TEMPERATURE", "0.7"))

    def validate(self) -> bool:
        """
        Valida se as configurações obrigatórias estão definidas.

        Returns:
            bool: True se todas as configurações estão válidas

        Raises:
            ValueError: Se OPENAI_API_KEY não estiver definida
        """
        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não definida")
        print("✅ Configurações validadas com sucesso!")
        return True


# Instância global da configuração
config = Config()
