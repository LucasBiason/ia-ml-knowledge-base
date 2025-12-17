# Respostas dos Exercícios - Advanced

Este diretório contém as respostas resolvidas dos exercícios do módulo Advanced.

## Exercícios por Tutorial

### Tutorial 01: Extração de Dados JSON
Este tutorial demonstra a integração de múltiplas APIs (Chat, Vision e Audio) para extrair dados estruturados.

- `tut-01-ex-01-extrair-dados-email.py`: Sistema de extração de leads e contatos de e-mails não estruturados.
- `tut-01-ex-02-processar-multiplos-documentos.py`: Automação para processamento em lote de arquivos PDF e normalização de dados.
- `tut-01-ex-03-validacao-tratamento-erros.py`: Implementação de validação de schema e tratamento de erros para pipelines de extração.

### Tutorial 02: Function Calling
Este tutorial foca em como permitir que o modelo execute funções Python para acessar dados externos e realizar ações.

- `tut-02-ex-01-funcao-busca.py`: Implementação de busca inteligente em catálogo de produtos.
- `tut-02-ex-02-agente-multiplas-funcoes.py`: Agente capaz de realizar cálculos e conversões usando múltiplas ferramentas.
- `tut-02-ex-03-sistema-agendamento.py`: Sistema de agendamento com verificação de disponibilidade e criação de compromissos.

---

## Como Executar

1. Certifique-se de ter o arquivo `.env` configurado com `OPENAI_API_KEY` na raiz do projeto.
2. Instale as dependências necessárias:
```bash
pip install openai python-dotenv pypdf
```
3. Execute os scripts individuais:
```bash
python tut-01-ex-01-extrair-dados-email.py
```

---

## Estrutura dos Arquivos

Cada arquivo segue o padrão de documentação do curso:
- **Docstring Inicial**: Contextualização e conceitos-chave.
- **Identificação**: Vinculação direta com o tutorial original.
- **Tratamento de Erros**: Exemplos robustos de uso da API.
- **Tom Natural**: Explicações didáticas sem jargões de IA.

---

## Referências
- **01-extracao-dados-json.ipynb**
- **02-funcoes-function-calling.ipynb**
