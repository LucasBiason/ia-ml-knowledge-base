# Audio - Text-to-Speech e Speech-to-Text

Esta secao apresenta tutoriais sobre o processamento de sinais de audio utilizando as APIs da OpenAI, cobrindo desde a sintese de voz ate a transcricao e traducao automatica.

---

## Tutoriais Disponiveis

### 1. Text-to-Speech (TTS)
**Arquivo:** [01-text-to-speech.ipynb](notebooks/01-text-to-speech.ipynb)

Fundamentos da conversao de texto em audio:
- Modelos tts-1 e tts-1-hd
- Catalogo de vozes (alloy, echo, fable, onyx, nova, shimmer)
- Controle de velocidade e formatos de saida (mp3, opus, aac, flac)

---

### 2. Speech-to-Text (Whisper)
**Arquivo:** [02-speech-to-text.ipynb](notebooks/02-speech-to-text.ipynb)

Transcricao de audio para texto:
- Utilizacao do modelo Whisper-1
- Formatos de entrada suportados e limites de tamanho
- Diferentes formatos de resposta (json, text, srt, vtt)
- Melhoria de precisao atraves de prompts de contexto

---

### 3. Traducao de Audio
**Arquivo:** [03-traducao-audio.ipynb](notebooks/03-traducao-audio.ipynb)

Processamento multimodal de audio:
- Transcricao no idioma original vs Traducao direta para ingles
- Estrategias para traducao em outros idiomas via Chat Completions
- Fluxo de trabalho para revisao de documentos de audio

---

## Modelos Disponiveis

![Infográfico: Pipeline do Whisper e TTS](../assets/imagens/tutorials/whisper-pipeline.png)

### Text-to-Speech (Sintese)
- **tts-1**: Otimizado para baixa latencia e aplicacoes em tempo real.
- **tts-1-hd**: Otimizado para alta fidelidade e qualidade de estudio.

### Speech-to-Text (Transcricao)
- **whisper-1**: Modelo de reconhecimento de fala multilingue com suporte a diversos sotaques e ruidos de fundo.

---

## Especificacoes Tecnicas

### Formatos Suportados
- **Saida (TTS)**: mp3, opus, aac, flac.
- **Entrada (Whisper)**: mp3, mp4, mpeg, mpga, m4a, wav, webm (Limite de 25MB).

### Casos de Uso Comuns
- Automação de narração para blogs e artigos.
- Desenvolvimento de assistentes de voz personalizados.
- Transcrição de reuniões e geração automática de atas.
- Criação de legendas para conteúdo em vídeo.

---

## Referencias Tecnicas

- [Documentacao Oficial - Text-to-Speech](https://platform.openai.com/docs/guides/text-to-speech)
- [Documentacao Oficial - Speech-to-Text](https://platform.openai.com/docs/guides/speech-to-text)
- [API Reference - Audio](https://platform.openai.com/docs/api-reference/audio)
