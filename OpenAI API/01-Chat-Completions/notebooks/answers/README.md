# Respostas dos Exercícios - Chat Completions

Este diretório contém as respostas resolvidas dos exercícios dos tutoriais de Chat Completions.

## Exercícios por Tutorial

### Tutorial 01: Conversa Básica
- `tut-01-ex-01-assistente-culinaria.py` - Criar assistente especializado em culinária.
- `tut-01-ex-02-comparar-modelos.py` - Comparar GPT-3.5 vs GPT-4.
- `tut-01-ex-03-controlar-tamanho-resposta.py` - Controlar tamanho da resposta com max_tokens.

### Tutorial 02: Agentes Especializados
- `tut-02-ex-01-agente-recomendacoes.py` - Agente de recomendações de filmes com contexto rico.
- `tut-02-ex-02-analise-financeira.py` - Agente de análise financeira com dados estruturados.
- `tut-02-ex-03-integracao-dados-reais.py` - Integração completa com arquivos CSV reais.

### Tutorial 03: Parâmetros Avançados
- `tut-03-ex-01-otimizar-titulos.py` - Otimização de parâmetros para geração de títulos criativos.
- `tut-03-ex-02-comparar-configuracoes.py` - Comparação entre diferentes combinações de parâmetros.
- `tut-03-ex-03-controlar-custos.py` - Estratégias de controle de custos e uso de tokens.

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
# Exemplo: Tutorial 02, Exercício 3
python tut-02-ex-03-integracao-dados-reais.py
```

**Nota:** O Exercício 3 do Tutorial 02 (`tut-02-ex-03-integracao-dados-reais.py`) usa o arquivo `assets/produtos.csv` que já está disponível na pasta assets.

---

## Estrutura dos Arquivos

Cada arquivo de exercício contém:
- **Descrição**: O que o exercício pede.
- **Referência**: Link para o tutorial original.
- **Resposta**: Código completo resolvendo o exercício.
- **Explicação**: Análise detalhada dos conceitos abordados (em docstring).
- **Melhorias Possíveis**: Sugestões para expandir o exercício.

---

## Referências

Todos os exercícios são baseados nos tutoriais:
- **01-conversa-basica.ipynb**
- **02-agentes-especializados.ipynb**
- **03-parametros-avancados.ipynb**

*Nota: O tutorial de Function Calling e seus exercícios foram movidos para a pasta `06-Advanced` devido à sua natureza avançada de integração.*
