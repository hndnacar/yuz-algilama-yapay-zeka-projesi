# bu kodla roboflowa resimleri yüklemeden önce resim boyutlarını eşitledim. bütün resimlerin artık boyutları aynıdır.
import os
import cv2

input_folder = 'resimlerim'
output_folder = 'boyutlandirilmis_resimler'
os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is not None:
            resized = cv2.resize(img, (640, 640))
            cv2.imwrite(os.path.join(output_folder, filename), resized)
        else:
            print(f"❌ Görüntü okunamadı: {filename}")
    else:
        print(f"⚠️ Desteklenmeyen dosya: {filename}")

print("✅ İşlem tamamlandı. Resimler images_resized klasörüne kaydedildi.")
