# Face Detection com Webcam (OpenCV + FER)

## 🎯 Objetivo
Guia rápido para:

1. Abrir a webcam via OpenCV.
2. Detectar rostos em tempo real com Haar Cascade.
3. Identificar a emoção dominante usando o modelo pré-treinado da biblioteca `fer`.

Os scripts foram pensados para rodar com a Logitech C922, mas incluem detecção automática do índice da câmera, então funcionam com qualquer webcam compatível com V4L2.

---

## 📁 Estrutura do diretório
```
01-face-detection-webcam/
├── README.md                 # Este guia
├── requirements.txt          # Dependências do ambiente
├── face_detection_basic.py   # Script 1: somente detecção de rosto
└── face_emotion_detection.py # Script 2: detecção + emoção dominante
```

---

## ⚙️ Preparando o ambiente
Crie e ative um ambiente virtual (opcional, mas recomendado):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Dependências principais:
- `opencv-python`: captura da webcam e Haar Cascade.
- `fer`: reconhecimento de emoções via modelo pré-treinado (usa TensorFlow/torch por baixo, mas o pacote já traz tudo necessário).

---

## ▶️ 1. Detectar rostos (`face_detection_basic.py`)

```bash
python3 face_detection_basic.py
```

O script:
- Procura automaticamente um dispositivo de vídeo funcional (prioriza o índice 32 para a Logitech C922).
- Define a resolução para 1280x720 a 30 fps.
- Espelha o frame horizontalmente (experiência natural).
- Usa o Haar Cascade `haarcascade_frontalface_default.xml` para detectar rostos.
- Desenha retângulos verdes sobre cada rosto.

Pressione `q` para encerrar a janela.

---

## 😃 2. Detectar rostos + emoção (`face_emotion_detection.py`)

```bash
python3 face_emotion_detection.py
```

Além do comportamento anterior, este script:
- Extrai o rosto detectado.
- Usa `FER()` para identificar a emoção dominante.
- Exibe o rótulo da emoção com a confiança em cima do retângulo (ex.: `happy (0.87)`).

Emoções suportadas pelo modelo: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`.

> Observação: o modelo precisa de iluminação razoável e rostos relativamente grandes no frame. Se a confiança vier baixa, ajuste a distância da câmera ou a iluminação.

---

## 🧪 Dicas de uso
- Ajuste as constantes `FRAME_WIDTH`, `FRAME_HEIGHT` e `FRAME_RATE` para equilibrar performance vs. qualidade.
- O Haar Cascade funciona melhor com faces frontais. Para cenários mais complexos, considere modelos DNN (ex.: MediaPipe, YOLO face).
- Para outras webcams, caso o índice não seja encontrado automaticamente, sobrescreva `preferred_index` em `find_camera_index`.

---

## 🧹 Encerramento
Para liberar a webcam ao final do teste:
- Pressione `q` na janela.
- Caso o terminal fique pendurado, `Ctrl+C` força o desligamento.

---

## 📚 Referências
- OpenCV Haar Cascades: https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html
- FER (Facial Emotion Recognition): https://github.com/justinshenk/fer

---

Qualquer ajuste ou melhoria (ex.: suportar múltiplas câmeras simultâneas, logs, testes automatizados) pode ser incrementado antes de integrar à base principal. Ainda **não faça commit** — o conteúdo será revisado antes.



