# Respostas dos Exercicios - Advanced

Este diretorio contem as solucoes estruturadas para os exercicios propostos no modulo Advanced. Os scripts seguem padroes de codificacao limpa e tratamento de erros robusto.

---

## Solucoes por Tutorial

### Tutorial 01: Extracao de Dados em JSON
Solucoes focadas em transformar informacoes heterogeneas em estruturas padronizadas.

- [tut-01-ex-01-extrair-dados-email.py](tut-01-ex-01-extrair-dados-email.py): Extrator de leads a partir de corpos de e-mail nao estruturados.
- [tut-01-ex-02-processar-multiplos-documentos.py](tut-01-ex-02-processar-multiplos-documentos.py): Pipeline para leitura e consolidacao de multiplos arquivos PDF.
- [tut-01-ex-03-validacao-tratamento-erros.py](tut-01-ex-03-validacao-tratamento-erros.py): Implementacao de schemas de validacao e logs de processamento.

---

### Tutorial 02: Function Calling
Solucoes demonstrando a integracao do modelo com funcoes Python externas.

- [tut-02-ex-01-funcao-busca.py](tut-02-ex-01-funcao-busca.py): Agente de consulta em catalogo de inventario.
- [tut-02-ex-02-agente-multiplas-funcoes.py](tut-02-ex-02-agente-multiplas-funcoes.py): Implementacao de agente capaz de alternar entre ferramentas de calculo e conversao.
- [tut-02-ex-03-sistema-agendamento.py](tut-02-ex-03-sistema-agendamento.py): Logica de agendamento com verificacao de conflitos de horario.

---

## Instrucoes de Execucao

1. Certifique-se de que o arquivo `.env` esta configurado na raiz do projeto.
2. Instale as dependencias especificadas no modulo raiz ou individualmente via pip.
3. Os scripts sao independentes e podem ser executados diretamente:
```bash
python tut-01-ex-01-extrair-dados-email.py
```

---

## Padroes de Codificacao

- **Docstrings**: Todos os scripts incluem documentacao inicial sobre o proposito e conceitos aplicados.
- **Tratamento de Erros**: Uso de blocos try-except para lidar com falhas de rede e erros de parsing JSON.
- **Identificacao**: Cada arquivo possui uma referencia direta ao tutorial correspondente no notebook.
