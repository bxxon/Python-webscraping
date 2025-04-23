import cv2
import numpy as np

# Kamera aç
cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Renk aralığını belirle (örn. kırmızı hedef için)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Maske ile hedefi ayırt et
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuç göster
    cv2.imshow('frame', result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

