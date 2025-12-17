# Vision - Analise Visual e OCR

Esta secao apresenta tutoriais sobre as capacidades multimodais da OpenAI, permitindo o processamento e a compreensao de informacoes visuais atraves de modelos como o GPT-4o.

---

## Tutoriais Disponiveis

### 1. Analise de Imagem Basica e OCR
**Arquivo:** [01-analise-imagem-basica.ipynb](notebooks/01-analise-imagem-basica.ipynb)

Fundamentos da visao computacional com LLMs:
- Requisicoes multimodais (texto + imagem)
- Extracao de texto de documentos e placas (OCR)
- Descricao detalhada de cenarios e objetos

---

### 2. Multiplas Imagens e Comparacao Visual
**Arquivo:** [02-multiplas-imagens-comparacao.ipynb](notebooks/02-multiplas-imagens-comparacao.ipynb)

Analise correlacionada de multiplos ativos:
- Envio de multiplas imagens em um unico payload
- Comparacao entre objetos e racas
- Analise de sequencias temporais (antes e depois)

---

### 3. Configuracoes de Detalhamento e Custos
**Arquivo:** [03-configuracoes-detalhamento.ipynb](notebooks/03-configuracoes-detalhamento.ipynb)

Otimizacao de performance e recursos:
- Modos de detalhamento: `low`, `high` e `auto`
- Calculo de custos em tokens para imagens
- Tecnicas de redimensionamento e economia de contexto

---

## Modelos Suportados

![Infográfico: Análise de Visão com GPT-4](../../assets/imagens/tutorials/vision-analysis-flow.png)

### GPT-4o (Omni)
- Modelo nativamente multimodal com suporte superior a visao.
- Mais rapido e economico que versoes anteriores.
- Recomendado para a maioria dos casos de uso de visao.

### GPT-4 Turbo with Vision
- Modelo anterior que introduziu o suporte a visao.
- Ainda util para comparacao e legados.

---

## Especificacoes Tecnicas

### Formatos Suportados
- Imagens em: png, jpeg, webp e gif nao animado.
- Metodos de envio: URL publica ou Base64 (codificacao binaria).

### Limites e Restricoes
- Tamanho maximo por imagem: 20MB.
- As imagens sao redimensionadas automaticamente para caber em um quadrado de 2048px se o modo `high` estiver ativo.

---

## Referencias Tecnicas

- [Documentacao Oficial - Vision](https://platform.openai.com/docs/guides/vision)
- [API Reference - Vision](https://platform.openai.com/docs/api-reference/chat/create#chat-create-messages)
- [Guia de Custos de Visao](https://platform.openai.com/docs/guides/vision/calculating-costs)
