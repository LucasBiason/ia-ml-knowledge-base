"""
Exercício 2: Agente com Múltiplas Funções

Referência: 04-funcoes-function-calling.ipynb - Exercício 2

Descrição:
Crie um agente que pode fazer cálculos, converter moedas e buscar informações, escolhendo a função adequada automaticamente.

Explicação:

Agente inteligente com múltiplas capacidades que escolhe automaticamente a função mais adequada para cada tarefa.

Pontos importantes:

1. Múltiplas Funções:
   - Cada função tem propósito específico
   - Modelo escolhe qual usar baseado no contexto
   - Pode chamar múltiplas funções em sequência

2. Escolha Automática:
   - Descrições claras ajudam o modelo a decidir
   - Modelo entende quando cada função é apropriada
   - Flexibilidade para diferentes tipos de perguntas

3. Aplicação Prática:
   - Assistentes virtuais completos
   - Agentes de atendimento
   - Sistemas de automação
   - Integração com múltiplos serviços

4. Melhorias Possíveis:
   - Adicionar mais funções (buscar notícias, clima, etc.)
   - Integrar com APIs externas
   - Adicionar memória de conversa
   - Implementar validação de permissões
"""

import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Função 1: Cálculos
def calcular(expressao: str) -> str:
    """Calcula o resultado de uma expressão matemática."""
    try:
        resultado = eval(expressao)
        return f"Resultado: {resultado}"
    except Exception as e:
        return f"Erro no cálculo: {e}"

# Função 2: Conversão de moeda
def converter_moeda(valor: float, de: str, para: str) -> str:
    """Converte valor entre moedas."""
    taxas = {
        "BRL": {"USD": 0.20, "EUR": 0.18},
        "USD": {"BRL": 5.00, "EUR": 0.90},
        "EUR": {"BRL": 5.55, "USD": 1.11}
    }
    
    if de == para:
        return f"{valor} {de}"
    
    taxa = taxas.get(de, {}).get(para)
    if not taxa:
        return f"Conversão de {de} para {para} não disponível"
    
    resultado = valor * taxa
    return f"{valor} {de} = {resultado:.2f} {para}"

# Função 3: Informações gerais
def obter_informacao(topic: str) -> str:
    """Obtém informações sobre um tópico."""
    informacoes = {
        "python": "Python é uma linguagem de programação de alto nível, interpretada e de propósito geral.",
        "openai": "OpenAI é uma empresa de pesquisa em IA que desenvolve modelos como GPT-4 e DALL-E.",
        "function calling": "Function Calling permite que modelos de linguagem chamem funções Python definidas pelo usuário."
    }
    
    topic_lower = topic.lower()
    for key, value in informacoes.items():
        if key in topic_lower or topic_lower in key:
            return value
    
    return f"Informações sobre '{topic}' não disponíveis no momento."

# Definir todas as funções
funcoes_agente = [
    {
        "type": "function",
        "function": {
            "name": "calcular",
            "description": "Calcula o resultado de uma expressão matemática",
            "parameters": {
                "type": "object",
                "properties": {
                    "expressao": {
                        "type": "string",
                        "description": "Expressão matemática a calcular (ex: '2 + 2', '10 * 5')"
                    }
                },
                "required": ["expressao"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "converter_moeda",
            "description": "Converte valor entre diferentes moedas (BRL, USD, EUR)",
            "parameters": {
                "type": "object",
                "properties": {
                    "valor": {"type": "number", "description": "Valor a ser convertido"},
                    "de": {"type": "string", "description": "Moeda de origem (BRL, USD, EUR)", "enum": ["BRL", "USD", "EUR"]},
                    "para": {"type": "string", "description": "Moeda de destino (BRL, USD, EUR)", "enum": ["BRL", "USD", "EUR"]}
                },
                "required": ["valor", "de", "para"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "obter_informacao",
            "description": "Obtém informações sobre um tópico específico",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Tópico sobre o qual obter informações"
                    }
                },
                "required": ["topic"]
            }
        }
    }
]

mapeamento_agente = {
    "calcular": calcular,
    "converter_moeda": converter_moeda,
    "obter_informacao": obter_informacao
}

def processar_function_call(mensagens, funcoes, mapeamento_funcoes, max_iteracoes=5):
    """Processa function calls automaticamente."""
    iteracoes = 0
    
    while iteracoes < max_iteracoes:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            tools=funcoes,
            tool_choice="auto"
        )
        
        mensagem = response.choices[0].message
        mensagens.append(mensagem)
        
        if not mensagem.tool_calls:
            return mensagem.content
        
        for tool_call in mensagem.tool_calls:
            nome_funcao = tool_call.function.name
            argumentos = json.loads(tool_call.function.arguments)
            tool_call_id = tool_call.id
            
            if nome_funcao in mapeamento_funcoes:
                funcao = mapeamento_funcoes[nome_funcao]
                try:
                    resultado = funcao(**argumentos)
                except Exception as e:
                    resultado = f"Erro ao executar função: {e}"
            else:
                resultado = f"Função '{nome_funcao}' não encontrada"
            
            mensagens.append({
                "role": "tool",
                "tool_call_id": tool_call_id,
                "name": nome_funcao,
                "content": str(resultado)
            })
        
        iteracoes += 1
    
    return "Número máximo de iterações atingido"

# RESPOSTA DO EXERCÍCIO
print("=" * 60)
print("EXERCÍCIO 2: Agente com Múltiplas Funções")
print("=" * 60)
print()

mensagens = [
    {
        "role": "system",
        "content": "Você é um assistente versátil que pode fazer cálculos, converter moedas e fornecer informações."
    },
    {
        "role": "user",
        "content": "Me fale sobre Python, depois calcule 25 * 4 e converta 50 dólares para reais."
    }
]

resposta = processar_function_call(
    mensagens=mensagens,
    funcoes=funcoes_agente,
    mapeamento_funcoes=mapeamento_agente
)

print(">> Resposta do assistente:")
print("-" * 60)
print(resposta)

