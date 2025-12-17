# Respostas dos Exercícios - Chat Completions

Este diretório contém as respostas resolvidas dos exercícios dos tutoriais de Chat Completions.

## Estrutura de Nomenclatura
Os arquivos seguem o padrão `tut-[número]-ex-[número]-[nome].py` para facilitar a identificação de qual tutorial o exercício pertence.

## Exercícios por Tutorial

### Tutorial 01: Conversa Básica
Exercícios sobre fundamentos da API de Chat Completions.
- `tut-01-ex-01-assistente-culinaria.py` - Criar assistente especializado
- `tut-01-ex-02-comparar-modelos.py` - Comparar GPT-3.5 vs GPT-4
- `tut-01-ex-03-controlar-tamanho-resposta.py` - Controlar tamanho com max_tokens

### Tutorial 02: Agentes Especializados
Exercícios sobre criação de agentes especializados com contexto.
- `tut-02-ex-01-agente-recomendacoes.py` - Agente de recomendações de filmes
- `tut-02-ex-02-analise-financeira.py` - Agente de análise financeira
- `tut-02-ex-03-integracao-dados-reais.py` - Integração com dados CSV reais

### Tutorial 03: Parâmetros Avançados
Exercícios sobre otimização de parâmetros e controle de custos.
- `tut-03-ex-01-otimizar-titulos.py` - Otimizar para gerar títulos criativos
- `tut-03-ex-02-comparar-configuracoes.py` - Comparar diferentes configurações
- `tut-03-ex-03-controlar-custos.py` - Controlar custos com max_tokens

### Tutorial 04: Function Calling
Exercícios sobre integração de funções externas e agentes inteligentes.
- `tut-04-ex-01-funcao-busca.py` - Criar função de busca de produtos
- `tut-04-ex-02-agente-multiplas-funcoes.py` - Agente com múltiplas capacidades
- `tut-04-ex-03-sistema-agendamento.py` - Sistema de agendamento com verificação

## Como Executar

1. Certifique-se de ter o arquivo `.env` configurado com `OPENAI_API_KEY` na raiz do projeto.
2. Instale as dependências necessárias:
```bash
pip install openai python-dotenv pandas
```
3. Execute o exercício desejado:
```bash
python tut-01-ex-01-assistente-culinaria.py
```

**Nota:** O exercício `tut-02-ex-03-integracao-dados-reais.py` utiliza o arquivo `assets/produtos.csv`.

---

## Referências
Todos os exercícios são baseados nos notebooks:
- `01-conversa-basica.ipynb`
- `02-agentes-especializados.ipynb`
- `03-parametros-avancados.ipynb`
- `04-funcoes-function-calling.ipynb`
