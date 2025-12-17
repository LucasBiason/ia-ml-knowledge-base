# Respostas dos Exercicios - Image Generation

Este diretorio contem as solucoes para os exercicios propostos nos tutoriais de geracao de imagens com DALL-E.

---

## Solucoes por Tutorial

### Tutorial 01: DALL-E Basico
- [tut-01-ex-01-gerar-thumbnail.py](tut-01-ex-01-gerar-thumbnail.py): Geracao de imagens em formato panorâmico para capas de artigos.

### Tutorial 02: Variacoes de Imagem
- [tut-02-ex-02-fluxo-refinamento.py](tut-02-ex-02-fluxo-refinamento.py): Pipeline completo de criacao (DALL-E 3) e variacao (DALL-E 2).

### Tutorial 03: Edicao de Imagens
- [tut-03-ex-03-gerar-mascara-pillow.py](tut-03-ex-03-gerar-mascara-pillow.py): Script utilitario para geracao programatica de mascaras de edicao.

---

## Como Executar

1. Instale as dependencias necessarias:
```bash
pip install openai python-dotenv pillow requests
```
2. Configure sua `OPENAI_API_KEY` no arquivo `.env`.
3. Execute o script desejado a partir deste diretorio:
```bash
python tut-01-ex-01-gerar-thumbnail.py
```
