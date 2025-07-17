# Ultralytics kütüphanesinden YOLO sınıfı içe aktarılır
from ultralytics import YOLO

# YOLOv8'in nano modeli seçilir (hafif, hızlı, başlangıç için ideal)
if __name__ == '__main__':
    model = YOLO("yolov8n.pt")  # Bu satır ilk çalıştığında ağırlığı indirir

    # Model eğitimi başlatılır
    results = model.train(
        data="veriseti/data.yaml",   # YAML dosyasının yolu
        epochs=50,                   # Toplam eğitim turu
        imgsz=640,                   # Resim boyutu (YOLO için önerilen değer)
        batch=8,                     # Her iterasyonda eğitilecek resim sayısı
        name="yuz_modelim",          # Sonuçların kayıt edileceği klasör ismi
    )
