# Embeddings - Vetorização e Busca Semântica

Esta seção aborda a utilização de Embeddings para representação vetorial de textos, permitindo a implementação de busca semântica, recomendação de conteúdo e agrupamento de dados.

---

## Tutoriais Disponíveis

### 1. Vetorização de Texto
**Arquivo:** [01-vetorizacao-texto.ipynb](notebooks/01-vetorizacao-texto.ipynb)

Fundamentos da criação de vetores numéricos:
- Funcionamento dos modelos `text-embedding-3-small` e `text-embedding-3-large`
- Estrutura de vetores e dimensões
- Casos de uso básicos e normalização

---

### 2. Busca Semântica Avançada
**Arquivo:** [02-busca-semantica.ipynb](notebooks/02-busca-semantica.ipynb)

Implementação de sistemas de recuperação de informação:
- Cálculo de similaridade coseno
- Ranking de resultados por relevância
- Redução de dimensionalidade para economia de recursos
- Integração teórica com bancos de dados vetoriais (Vector DBs)

---

## Modelos Disponíveis

![Infográfico: Busca Semântica com Embeddings](../assets/imagens/tutorials/embeddings-semantic-search.png)

### text-embedding-3-small
- Vetores de 1536 dimensões.
- Otimizado para latência e baixo custo.
- Ideal para sistemas de larga escala com restrição de memória.

### text-embedding-3-large
- Vetores de ate 3072 dimensões.
- Melhor desempenho em tarefas complexas de compreensão semântica.
- Suporta truncamento de dimensões mantendo alta precisao.

---

## Aplicações Práticas

1. **Busca Semântica**: Recuperação de documentos baseada no significado, não apenas em palavras-chave.
2. **Sistemas de Recomendação**: Sugestão de produtos ou conteúdos com base na similaridade vetorial.
3. **Agrupamento (Clustering)**: Identificação de padrões e grupos em grandes volumes de texto.
4. **Classificação de Texto**: Categorização baseada na proximidade com vetores de referência.

---

## Especificações Técnicas

- **Entrada Máxima**: 8191 tokens por requisição.
- **Saída**: Vetores normalizados (comprimento 1), facilitando o cálculo de similaridade via produto escalar.
- **Dimensionalidade Flexível**: Modelos v3 permitem reduzir as dimensões via parâmetro `dimensions` sem perda linear de precisão.

---

## Referências Técnicas

- [Documentação Oficial - Embeddings](https://platform.openai.com/docs/guides/embeddings)
- [API Reference - Embeddings](https://platform.openai.com/docs/api-reference/embeddings)
- [Guia de Similaridade Coseno](https://en.wikipedia.org/wiki/Cosine_similarity)
