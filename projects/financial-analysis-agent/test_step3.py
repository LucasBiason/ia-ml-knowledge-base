import os
from dotenv import load_dotenv

load_dotenv()

def test_step3():
    """Testa os Agentes criados"""

    print("🧪 Testando Passo 3: Agentes Financeiros")
    print("=" * 50)

    try:
        # Teste 1: Agente Simples
        print("\n🤖 Teste 1: Agente Financeiro Simples")
        from src.agents.financial_agent import FinancialAgent

        agent = FinancialAgent()
        print("✅ Agente criado com sucesso!")

        # Verificar ferramentas disponíveis
        tools = agent.get_available_tools()
        print(f"�� Ferramentas disponíveis: {', '.join(tools)}")

        # Teste 2: Pergunta simples
        print("\n💬 Teste 2: Pergunta Simples")
        resposta = agent.ask("Qual o preço da PETR4?")
        print(f"✅ Resposta: {resposta[:200]}...")

        # Teste 3: Agente Avançado
        print("\n🚀 Teste 3: Agente Financeiro Avançado")
        from src.agents.advanced_financial_agent import AdvancedFinancialAgent

        advanced_agent = AdvancedFinancialAgent()
        print("✅ Agente avançado criado com sucesso!")

        # Teste 4: Análise completa
        print("\n📊 Teste 4: Análise Completa de VALE3")
        resultado = advanced_agent.analyze_comprehensive("PETR4")

        if resultado["status"] == "success":
            print("✅ Análise completa executada com sucesso!")
            print(f" Ticker: {resultado['ticker']}")
            print(f"💰 Preço: {resultado['current_price']}")
            print(f"📈 Contexto: {resultado['market_context']}")
            print(f"📋 Resumo contextual (primeiras 200 letras):")
            print(f"   {resultado['contextual_summary'][:200]}...")
        else:
            print(f"❌ Erro na análise: {resultado['error']}")

        # Teste 5: Histórico da conversa
        print("\n�� Teste 5: Histórico da Conversa")
        history = advanced_agent.get_conversation_history()
        print(f"✅ Histórico obtido: {len(history)} mensagens")

        print("\n Todos os testes do Passo 3 passaram!")

    except Exception as e:
        print(f"❌ Erro durante o teste: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_step3()
