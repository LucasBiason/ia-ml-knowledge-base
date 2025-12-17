"""
Face detection + emoção dominante usando OpenCV e FER.

Execute:
    python3 face_emotion_detection.py

Pressione 'q' para encerrar a janela.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional, Tuple

import cv2
from fer import FER

# Configurações padrão (Logitech C922 priorizada em /dev/video32)
PREFERRED_INDEX = 32
MAX_INDEX = 40
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FRAME_RATE = 30
MIN_EMOTION_CONFIDENCE = 0.5


def find_camera_index(preferred_index: int = PREFERRED_INDEX, max_index: int = MAX_INDEX) -> Optional[int]:
    """Retorna o primeiro índice de webcam funcional encontrado."""
    candidates = [preferred_index] + [idx for idx in range(max_index) if idx != preferred_index]

    for idx in candidates:
        cap = cv2.VideoCapture(idx, cv2.CAP_V4L2)
        if not cap.isOpened():
            cap.release()
            continue

        ret, _ = cap.read()
        cap.release()

        if ret:
            return idx

    return None


def create_capture(camera_index: int) -> cv2.VideoCapture:
    """Inicializa o objeto de captura com resolução e FPS configurados."""
    cap = cv2.VideoCapture(camera_index, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, FRAME_RATE)
    return cap


def load_face_detector() -> cv2.CascadeClassifier:
    """Carrega o Haar Cascade frontal padrão do OpenCV."""
    cascade_path = Path(cv2.data.haarcascades) / "haarcascade_frontalface_default.xml"
    detector = cv2.CascadeClassifier(str(cascade_path))
    if detector.empty():
        raise RuntimeError(f"Não foi possível carregar o Haar Cascade em {cascade_path}")
    return detector


def extract_dominant_emotion(emotions: Dict[str, float]) -> Optional[Tuple[str, float]]:
    """Retorna a emoção dominante (label, score) se ultrapassar o threshold mínimo."""
    if not emotions:
        return None
    label, score = max(emotions.items(), key=lambda item: item[1])
    if score < MIN_EMOTION_CONFIDENCE:
        return None
    return label, score


def main() -> None:
    """Loop principal: detecta rostos e exibe a emoção dominante."""
    camera_index = find_camera_index()
    if camera_index is None:
        print("❌ Não foi possível encontrar uma webcam funcional.")
        return

    cap = create_capture(camera_index)
    if not cap.isOpened():
        print(f"❌ Erro ao acessar a webcam no índice {camera_index}.")
        return

    detector = load_face_detector()
    emotion_detector = FER(mtcnn=False)

    print("✅ Webcam iniciada (com emoções). Pressione 'q' para encerrar.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Falha ao capturar frame. Encerrando...")
                break

            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(80, 80),
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

                face_roi = frame[y : y + h, x : x + w]
                face_rgb = cv2.cvtColor(face_roi, cv2.COLOR_BGR2RGB)

                prediction = emotion_detector.detect_emotions(face_rgb)
                if prediction:
                    emotions = prediction[0]["emotions"]
                    dominant = extract_dominant_emotion(emotions)
                    if dominant:
                        emotion_label, score = dominant
                        label = f"{emotion_label} ({score:.2f})"
                        cv2.putText(
                            frame,
                            label,
                            (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            0.7,
                            (255, 255, 255),
                            2,
                            cv2.LINE_AA,
                        )

            cv2.imshow("Face Detection + Emotion - Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()



