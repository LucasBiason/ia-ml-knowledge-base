import os
from dotenv import load_dotenv

load_dotenv()

def test_step1():
    """Testando a primeira etapa de construção, estrutura inicial dos
    prompts, cliente LangChain e configurações"""

    print("🧪 Testando Passo 1: Configuração e Cliente Básico")
    print("=" * 50)

    try:
        # Teste 1: Configurações
        print("\n�� Teste 1: Configurações")
        from src.core.config import config
        config.validate()
        print("✅ Configurações funcionando!")

        # Teste 2: Cliente LangChain
        print("\n🤖 Teste 2: Cliente LangChain")
        from src.core.langchain_client import LangChainClient
        client = LangChainClient()
        print("✅ Cliente criado com sucesso!")

        # Teste 3: Consulta simples
        print("\n💬 Teste 3: Consulta Simples")
        resposta = client.simple_query("O que é análise fundamentalista?")
        print(f"✅ Resposta obtida: {resposta[:100]}...")

        # Teste 4: Prompts
        print("\n📝 Teste 4: Prompts")
        from src.prompts.financial_prompts import STOCK_ANALYSIS_PROMPT
        prompt = STOCK_ANALYSIS_PROMPT.format(
            ticker="PETR4",
            analysis_type="análise fundamentalista"
        )
        print("✅ Prompt criado com sucesso!")
        print(f"📄 Primeiras 200 letras: {prompt[:200]}...")

        print("\n�� Todos os testes do Passo 1 passaram!")

    except Exception as e:
        print(f"❌ Erro durante o teste: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_step1()
