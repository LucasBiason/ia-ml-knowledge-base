import os
from dotenv import load_dotenv

load_dotenv()

def test_step2():
    """Testando a segunda parte apos a criação de
    Chains e Tools pra pesquisa das ações."""

    print("🧪 Testando Passo 2: Chains e Tools")
    print("=" * 50)

    try:
        # Teste 1: Chain de Análise
        print("\n�� Teste 1: Financial Analysis Chain")
        from src.chains.analysis_chain import FinancialAnalysisChain

        chain = FinancialAnalysisChain()
        print("✅ Chain criada com sucesso!")

        analysis_types = chain.get_analysis_types()
        print(f"📋 Tipos de análise disponíveis: {', '.join(analysis_types)}")

        # Teste 2: Análise Real
        print("\n💹 Teste 2: Análise de PETR4")
        resultado = chain.analyze_stock("PETR4", "análise fundamentalista")

        if resultado["status"] == "success":
            print("✅ Análise executada com sucesso!")
            print(f" Ticker: {resultado['ticker']}")
            print(f" Tipo: {resultado['analysis_type']}")
            print(f"📄 Análise detalhada (primeiras 200 letras):")
            print(f"   {resultado['detailed_analysis'][:200]}...")
            print(f"�� Resumo executivo (primeiras 200 letras):")
            print(f"   {resultado['executive_summary'][:200]}...")
        else:
            print(f"❌ Erro na análise: {resultado['error']}")

        # Teste 3: Tools
        print("\n🔧 Teste 3: Stock Price Tool")
        from src.tools.stock_tools import StockPriceTool

        price_tool = StockPriceTool()
        preco = price_tool._run("PETR4")
        print(f"✅ {preco}")

        # Teste 4: Market Index Tool
        print("\n📈 Teste 4: Market Index Tool")
        from src.tools.stock_tools import MarketIndexTool

        index_tool = MarketIndexTool()
        indice = index_tool._run("IBOV")
        print(f"✅ {indice}")

        print("\n✅✅ Todos os testes do Passo 2 passaram!")

    except Exception as e:
        print(f"❌ Erro durante o teste: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_step2()
