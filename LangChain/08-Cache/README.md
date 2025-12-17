# Cache - Tutoriais Completos

Esta seção contém tutoriais completos sobre cacheamento no LangChain, essencial para reduzir custos e melhorar performance em aplicações com LLMs.

## Tutoriais Disponíveis

### 01 - Cache Básico - InMemory e SQLite
**Arquivo:** `notebooks/01-cache-basico.ipynb`

Aprenda os fundamentos do cache no LangChain:
- O que é cache e por que usar
- Implementar cache em memória (InMemoryCache)
- Implementar cache persistente (SQLiteCache)
- Comparar performance e economia de custos

**Pré-requisitos:** 
- Tutorial 01-LLMs-Basicos: Introdução aos LLMs

---

### 02 - Cache Redis
**Arquivo:** `notebooks/02-cache-redis.ipynb`

Domine o cache distribuído com Redis:
- Quando usar Redis para cache
- Configurar Redis para cache do LangChain
- Implementar cache distribuído
- Comparar performance com outros tipos

**Pré-requisitos:** 
- Tutorial 01
- Redis instalado e rodando

---

### 03 - Cache PostgreSQL
**Arquivo:** `notebooks/03-cache-postgres.ipynb`

Use PostgreSQL como cache para produção:
- Quando usar PostgreSQL para cache
- Configurar PostgreSQL para cache do LangChain
- Implementar cache persistente em produção
- Comparar com outros tipos de cache

**Pré-requisitos:** 
- Tutorial 01
- PostgreSQL instalado e rodando

---

## Ordem Recomendada de Estudo

1. **01 - Cache Básico** (Fundamentos)
2. **02 - Cache Redis** (Distribuído)
3. **03 - Cache PostgreSQL** (Produção)

---

## Conceitos-Chave

### Por que usar Cache?

**Vantagens:**
- **Economia de custos**: Não paga pela mesma chamada duas vezes
- **Performance**: Respostas instantâneas do cache
- **Desenvolvimento**: Ideal para testes e iterações
- **Consistência**: Mesma resposta para mesma entrada

### Tipos de Cache

**InMemoryCache:**
- Muito rápido
- Volátil (perde ao reiniciar)
- Não compartilhado
- Uso: Desenvolvimento local, testes

**SQLiteCache:**
- Persistente
- Simples de usar
- Não precisa servidor
- Não compartilhado
- Uso: Aplicações pequenas/médias

**RedisCache:**
- Muito rápido
- Distribuído (compartilhado)
- Escalável
- Precisa servidor Redis
- Uso: Aplicações distribuídas, alta performance

**PostgresCache:**
- Persistente e confiável
- Integração com PostgreSQL existente
- Pode fazer queries
- Mais lento que Redis/InMemory
- Precisa servidor PostgreSQL
- Uso: Aplicações que já usam PostgreSQL

---

## Casos de Uso

### Desenvolvimento
- Use **InMemoryCache** para testes rápidos
- Use **SQLiteCache** para persistência local

### Produção
- Use **RedisCache** para alta performance e distribuição
- Use **PostgresCache** se já usa PostgreSQL

### Escolha do Cache

**Escolha InMemory se:**
- Desenvolvimento local
- Testes rápidos
- Não precisa persistência

**Escolha SQLite se:**
- Aplicação pequena/média
- Precisa persistência simples
- Não precisa compartilhar

**Escolha Redis se:**
- Aplicação distribuída
- Alta performance necessária
- Precisa compartilhar cache

**Escolha PostgreSQL se:**
- Já usa PostgreSQL
- Precisa persistência confiável
- Quer simplificar infraestrutura

---

## Recursos Adicionais

- [Documentação - Cache](https://python.langchain.com/docs/modules/model_io/caching/)
- [Redis Documentation](https://redis.io/docs/)
- [PostgreSQL Documentation](https://www.postgresql.org/docs/)

---

## Próximas Seções

- **04-Memory**: Gerenciamento de memória em conversas
- **05-Agents**: Agents com cache otimizado
- **06-RAG**: RAG com cache otimizado





