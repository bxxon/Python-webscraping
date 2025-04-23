import cv2
import numpy as np
from sort import Sort  # SORT kütüphanesi lazım (pip install sort)

# SORT nesnesi
tracker = Sort()

# Video girişi
video_path = "video.mp4"  # Kendi video dosyanızın yolunu yazın
cap = cv2.VideoCapture(video_path)

# Tespit edilen nesneleri simüle etmek için YOLO'dan gelen rastgele veriler
def fake_yolo_detections(frame):
    h, w, _ = frame.shape
    return [
        [w * 0.2, h * 0.2, w * 0.4, h * 0.4, 0.9],  # [x1, y1, x2, y2, confidence]
        [w * 0.6, h * 0.5, w * 0.8, h * 0.7, 0.8],
    ]

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Nesne tespitlerini al (YOLO ile değiştirebilirsin)
    detections = fake_yolo_detections(frame)

    # SORT için numpy dizisine çevir
    detections_array = np.array(detections)

    # SORT ile takip
    tracks = tracker.update(detections_array)

    # Tespit edilen nesneleri çizin
    for track in tracks:
        x1, y1, x2, y2, track_id = track
        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 2)
        cv2.putText(frame, f"ID: {int(track_id)}", (int(x1), int(y1) - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # Ekranda göster
    cv2.imshow("SORT Tracking", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
