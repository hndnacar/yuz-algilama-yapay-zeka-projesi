from ultralytics import YOLO
import cv2

# Modeli yükle
model = YOLO('runs/detect/yuz_modelim10/weights/best.pt')

# Test görüntüsünü yükle
img_path = 'test_yuz.jpg'  # Test etmek istediğin yüz fotoğrafı
results = model(img_path, save=True)

# Sonuçları görselleştir
for r in results:
    r.show()  # Detected sonuçları gör
