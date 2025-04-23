import cv2
import numpy as np

# YOLO modelini yükle
net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

# Hedef sınıfları yükle
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]

# Sadece tespit edilmesi istenilen sınıf (örneğin: 'person')
target_class = "qrcode"  # Bu kısmı istediğin sınıfla değiştir ('car', 'dog' vb.)

# Kamera aç (0: varsayılan kamera)
cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    height, width, channels = img.shape

    # YOLO için resim ön işleme
    blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # Nesneleri filtrele ve çiz (belirli bir sınıfa göre)
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]

            # Tespit edilen sınıf hedef sınıfa eşitse ve güven skoru yeterince yüksekse
            if confidence > 0.5 and classes[class_id] == target_class:
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Dikdörtgen çerçeve çiz
                cv2.rectangle(img, (center_x - w // 2, center_y - h // 2), (center_x + w // 2, center_y + h // 2), (0, 255, 0), 2)
                cv2.putText(img, f"{classes[class_id]} ({confidence:.2f})", (center_x - w // 2, center_y - h // 2 - 10), cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 2)

    # Görüntüyü göster
    cv2.imshow("Image", img)

    # 'q' tuşuna basıldığında çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
