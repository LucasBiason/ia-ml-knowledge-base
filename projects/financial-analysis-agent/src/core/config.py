import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configurações centralizadas do projeto"""

    # OpenAI
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.7"))

    # Validações
    @classmethod
    def validate(cls):
        """Valida se as configurações estão corretas"""
        if not cls.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não encontrada!")

        print("✅ Configurações validadas com sucesso!")
        return True

config = Config()
