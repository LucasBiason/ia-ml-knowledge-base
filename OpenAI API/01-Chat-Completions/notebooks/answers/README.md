# Respostas dos Exercícios - Chat Completions

Este diretório contém as respostas resolvidas dos exercícios dos tutoriais de Chat Completions.

## Tutoriais Disponíveis

### 01 - Conversa Básica
Exercícios sobre fundamentos da API de Chat Completions.

### 02 - Agentes Especializados
Exercícios sobre criação de agentes especializados com contexto.

## Exercícios Disponíveis

### Exercício 1: Criar Agente de Recomendações
**Arquivo:** `exercicio-01-agente-recomendacoes.py`

Cria um agente especializado em recomendar filmes, incluindo uma lista de filmes populares organizados por gênero no contexto.

**Conceitos abordados:**
- Criação de contexto rico com dados estruturados
- Organização de informações por categorias
- Instruções específicas para o agente
- Personalização de recomendações

---

### Exercício 2: Agente de Análise Financeira
**Arquivo:** `exercicio-02-analise-financeira.py`

Cria um agente que analisa dados financeiros simulados (receitas e despesas), fornecendo insights e recomendações.

**Conceitos abordados:**
- Análise de dados financeiros estruturados
- Uso de temperatura baixa para análises precisas
- Identificação de padrões e oportunidades
- Geração de insights acionáveis

---

### Exercício 3: Integração com Dados Reais
**Arquivo:** `exercicio-03-integracao-dados-reais.py`

Mostra como ler dados de um arquivo CSV real e usar como contexto para o agente, criando um sistema de análise de produtos.

**Conceitos abordados:**
- Leitura de arquivos CSV com pandas
- Formatação de dados para contexto
- Integração completa: dados → processamento → agente → análise
- Aplicação prática em gestão de produtos

---

### Tutorial 03: Parâmetros Avançados

### Exercício 1: Otimizar para Tarefa Específica
**Arquivo:** `exercicio-01-otimizar-titulos.py`

Cria uma requisição otimizada para gerar títulos de artigos (curtos, criativos, sem repetição), mostrando como combinar parâmetros para uma tarefa específica.

**Conceitos abordados:**
- Combinação de parâmetros (temperature, penalties, top_p)
- Otimização para tarefas específicas
- Uso de frequency_penalty e presence_penalty para evitar repetição
- Geração de múltiplas opções (n=5)

---

### Exercício 2: Comparar Configurações
**Arquivo:** `exercicio-02-comparar-configuracoes.py`

Testa a mesma pergunta com diferentes combinações de parâmetros (conservadora, criativa, balanceada) e compara os resultados.

**Conceitos abordados:**
- Impacto de diferentes configurações de temperatura
- Efeito de penalties nas respostas
- Trade-offs entre precisão e criatividade
- Quando usar cada tipo de configuração

---

### Exercício 3: Controlar Custos
**Arquivo:** `exercicio-03-controlar-custos.py`

Usa max_tokens para limitar respostas a 150 tokens e compara o custo antes e depois, mostrando economia significativa.

**Conceitos abordados:**
- Controle de custos com max_tokens
- Cálculo de custos da API
- Trade-off entre qualidade e custo
- Impacto em escala (1.000+ requisições)
- Estratégias de otimização de custos

---

## Como Executar

1. Certifique-se de ter o arquivo `.env` configurado com `OPENAI_API_KEY`
2. Instale as dependências necessárias:
```bash
# Opção 1: Instalar do requirements.txt do módulo
pip install -r ../requirements.txt

# Opção 2: Instalar manualmente
pip install openai python-dotenv pandas
```
3. Execute cada arquivo Python:

```bash
# Exercício 1
python exercicio-01-agente-recomendacoes.py

# Exercício 2
python exercicio-02-analise-financeira.py

# Exercício 3
python exercicio-03-integracao-dados-reais.py
```

**Nota:** O Exercício 3 usa o arquivo `assets/produtos.csv` que já está disponível na pasta assets.

---

## Estrutura dos Arquivos

Cada arquivo de exercício contém:
- **Descrição**: O que o exercício pede
- **Referência**: Link para o notebook original
- **Resposta**: Código completo resolvendo o exercício
- **Explicação**: Análise detalhada dos conceitos abordados
- **Melhorias Possíveis**: Sugestões para expandir o exercício

---

## Dependências

- `openai`: Cliente da API OpenAI
- `python-dotenv`: Carregamento de variáveis de ambiente
- `pandas`: Processamento de dados (Exercício 3)

---

### 03 - Parâmetros Avançados
Exercícios sobre otimização de parâmetros e controle de custos.

---

## Exercícios por Tutorial

### Tutorial 01: Conversa Básica
- `exercicio-01-assistente-culinaria.py` - Criar assistente especializado
- `exercicio-02-comparar-modelos.py` - Comparar GPT-3.5 vs GPT-4
- `exercicio-03-controlar-tamanho-resposta.py` - Controlar tamanho com max_tokens

### Tutorial 02: Agentes Especializados
- `exercicio-01-agente-recomendacoes.py` - Agente de recomendações de filmes
- `exercicio-02-analise-financeira.py` - Agente de análise financeira
- `exercicio-03-integracao-dados-reais.py` - Integração com dados CSV reais

### Tutorial 03: Parâmetros Avançados
- `exercicio-01-otimizar-titulos.py` - Otimizar para gerar títulos criativos
- `exercicio-02-comparar-configuracoes.py` - Comparar diferentes configurações
- `exercicio-03-controlar-custos.py` - Controlar custos com max_tokens

---

## Referências

Todos os exercícios são baseados nos tutoriais:
- **01-conversa-basica.ipynb** - Seção "Exercícios Práticos"
- **02-agentes-especializados.ipynb** - Seção "Exercícios Práticos"
- **03-parametros-avancados.ipynb** - Seção "Exercícios Práticos"

---

## Próximos Passos

Após completar estes exercícios, você pode:
- Adaptar os exemplos para seus próprios casos de uso
- Integrar com suas próprias fontes de dados
- Criar agentes especializados para diferentes domínios
- Explorar o tutorial 03 (Parâmetros Avançados) para otimizar seus agentes
