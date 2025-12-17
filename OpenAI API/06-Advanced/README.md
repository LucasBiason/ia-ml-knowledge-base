# 06 - Advanced

Tópicos avançados e integração de múltiplas APIs da OpenAI.

---

## Tutoriais Disponíveis

### 01 - Extração de Dados JSON
**Arquivo:** `notebooks/01-extracao-dados-json.ipynb`

Aprenda a extrair dados estruturados integrando múltiplas APIs:
- Usar `response_format={'type': 'json_object'}` no Chat Completions
- Extrair dados de texto livre
- Processar imagens de documentos com Vision API
- Transcrever áudio com Whisper e estruturar em JSON
- Extrair dados de PDFs e normalizar

**Pré-requisitos:**
- Tutorial 01-Chat-Completions: Conversa Básica
- Tutorial 02-Chat-Completions: Agentes Especializados (recomendado)
- Conhecimento básico de JSON

**Conceitos abordados:**
- Integração de múltiplas APIs (Chat + Vision + Audio)
- Estruturação de dados com JSON
- Processamento de diferentes tipos de mídia
- Normalização de dados de diferentes fontes

---

### 02 - Streaming de Respostas
**Arquivo:** `notebooks/02-streaming-responses.ipynb` (Em breve)

Respostas em tempo real usando streaming:
- Implementar streaming de respostas
- Melhorar UX com respostas progressivas
- Processar tokens conforme chegam

---

### 03 - Processamento em Lote
**Arquivo:** `notebooks/03-batch-processing.ipynb` (Em breve)

Processar múltiplas requisições de forma eficiente:
- Batch processing API
- Otimização de custos
- Processamento assíncrono

---

### 04 - Fine-Tuning
**Arquivo:** `notebooks/04-fine-tuning.ipynb` (Em breve)

Ajuste fino de modelos para casos específicos:
- Preparar dados para fine-tuning
- Treinar modelos customizados
- Deploy de modelos fine-tuned

---

## Ordem Recomendada de Estudo

1. **01 - Extração de Dados JSON** - Integração de múltiplas APIs
2. **02 - Streaming de Respostas** - Respostas em tempo real
3. **03 - Processamento em Lote** - Otimização de custos
4. **04 - Fine-Tuning** - Customização de modelos

---

## Conceitos-Chave

### Integração de APIs
- Combinar Chat Completions com outras APIs
- Processar diferentes tipos de mídia
- Normalizar dados de múltiplas fontes

### Otimização
- Streaming para melhor UX
- Batch processing para eficiência
- Fine-tuning para casos específicos

---

## Referências

- [Documentação - Chat Completions](https://platform.openai.com/docs/guides/text-generation)
- [Documentação - Vision API](https://platform.openai.com/docs/guides/vision)
- [Documentação - Whisper API](https://platform.openai.com/docs/guides/speech-to-text)
- [Documentação - Fine-Tuning](https://platform.openai.com/docs/guides/fine-tuning)

