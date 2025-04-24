import cv2
import numpy as np
from PIL import Image
import os

# Görselin tam yolunu belirtin
img_path = r"C:\Users\askan\Desktop\gezegenler\gezegenler.jpg"
img = cv2.imread(img_path)

# Eğer görsel yüklenemezse hata ver
if img is None:
    print("Görsel bulunamadı. Lütfen dosya yolunu kontrol edin.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Eşikleme yap (Beyaz arka planı belirlemek için)
_, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)

# Konturları Bul
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Çıkış klasörü oluştur
output_folder = r"C:\Users\askan\Desktop\gezegenler\gezegenler_transparent"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Her bir gezegeni kes ve şeffaf hale getir
for i, contour in enumerate(contours):
    x, y, w, h = cv2.boundingRect(contour)
    planet = img[y:y+h, x:x+w]

    # Maske oluştur (şeffaf alan için)
    mask = np.zeros((h, w), dtype=np.uint8)
    cv2.drawContours(mask, [contour - [x, y]], -1, 255, thickness=cv2.FILLED)

    # PNG formatında kaydetmek için PIL kullanımı
    planet_pil = Image.fromarray(cv2.cvtColor(planet, cv2.COLOR_BGR2RGBA))
    alpha = Image.fromarray(mask)
    planet_pil.putalpha(alpha)

    # Gezegenleri kaydet
    planet_pil.save(f"{output_folder}/gezegen_{i + 1}.png")

print("Gezegenler başarıyla ayrıldı!")
