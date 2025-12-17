# Image Generation - DALL-E

Esta secao apresenta tutoriais sobre a utilizacao da API DALL-E para geracao, variacao e edicao de imagens atraves de modelos de inteligencia artificial.

---

## Tutoriais Disponiveis

### 1. DALL-E Basico
**Arquivo:** [01-dalle-basico.ipynb](notebooks/01-dalle-basico.ipynb)

Fundamentos da geracao de imagens:
- Requisicao simples com DALL-E 3
- Parametros de configuracao (model, size, quality, style)
- Persistencia de imagens localmente

---

### 2. Variacoes de Imagem
**Arquivo:** [02-dalle-variacoes.ipynb](notebooks/02-dalle-variacoes.ipynb)

Exploracao de diversidade visual:
- Geracao de multiplas versoes com DALL-E 2
- Criacao de variacoes a partir de arquivos locais
- Analise comparativa entre versoes do modelo

---

### 3. Edicao de Imagens (Inpainting)
**Arquivo:** [03-dalle-edicao.ipynb](notebooks/03-dalle-edicao.ipynb)

Tecnicas avancadas de modificacao:
- Edicao de regioes especificas usando mascaras
- Adicao e remocao de elementos em imagens existentes
- Casos de uso para design e prototipagem

---

## Modelos Disponiveis

![Infográfico: Geração de Imagens com DALL-E](../assets/imagens/tutorials/dalle-generation-flow.png)

### DALL-E 3
- Modelo de ultima geracao com alta fidelidade.
- Restricao de uma imagem por chamada.
- Entendimento semantico superior para prompts complexos.
- Dimensoes suportadas: 1024x1024, 1792x1024 (Wide), 1024x1792 (Tall).
- Niveis de qualidade: standard e hd.

### DALL-E 2
- Modelo anterior, otimizado para velocidade e custo.
- Capacidade de gerar ate 10 imagens simultaneas.
- Dimensoes: 256x256, 512x512, 1024x1024.
- Recomendado para variacoes e edicoes rapidas.

---

## Engenharia de Prompt para Imagens

1. Especificidade: Descrever estilo artistico, iluminacao e composicao (ex: "cinematic light", "isometric 3D", "oil painting").
2. Concisao: Evitar textos redundantes; o DALL-E 3 ja realiza um refinamento automatico dos prompts.
3. Qualidade: Indicar explicitamente o acabamento desejado (ex: "high definition", "professional photography").

---

## Estrutura de Custos

- DALL-E 3 Standard: $0.04 por imagem (1024x1024).
- DALL-E 3 HD: $0.08 por imagem (1024x1024).
- DALL-E 2: $0.02 por imagem (1024x1024).

---

## Referencias Tecnicas

- Documentacao Oficial - DALL-E
- API Reference - Images
- Guia de Prompt Engineering para Imagens
