"""
Face detection básico usando OpenCV + Haar Cascade.

Execute:
    python3 face_detection_basic.py

Pressione 'q' para encerrar a janela.
"""

from __future__ import annotations

from pathlib import Path
from typing import Optional

import cv2

# Configurações padrão (Logitech C922 priorizada em /dev/video32)
PREFERRED_INDEX = 32
MAX_INDEX = 40
FRAME_WIDTH = 1280
FRAME_HEIGHT = 720
FRAME_RATE = 30


def find_camera_index(preferred_index: int = PREFERRED_INDEX, max_index: int = MAX_INDEX) -> Optional[int]:
    """
    Procura o primeiro índice de webcam funcional.

    Tenta primeiro o índice preferido (útil quando sabemos que a C922 é /dev/video32)
    e, em seguida, itera pelos demais índices até encontrar um que abra e capture um frame válido.
    """
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
    """Cria o objeto de captura configurando resolução e taxa de quadros."""
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


def main() -> None:
    """Loop principal: abre a webcam, detecta rostos e exibe em tempo real."""
    camera_index = find_camera_index()
    if camera_index is None:
        print("❌ Não foi possível encontrar uma webcam funcional.")
        return

    cap = create_capture(camera_index)
    if not cap.isOpened():
        print(f"❌ Erro ao acessar a webcam no índice {camera_index}.")
        return

    detector = load_face_detector()

    print("✅ Webcam iniciada. Pressione 'q' para encerrar.")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("⚠️ Falha ao capturar frame. Encerrando...")
                break

            frame = cv2.flip(frame, 1)  # Espelha horizontalmente (experiência natural)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            faces = detector.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(80, 80),
            )

            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.imshow("Face Detection - Webcam", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

