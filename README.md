# 🤖 Kendi Yüzümü Tanıyan Yapay Zeka Projesi

Bu proje, yalnızca benim yüzümü tanıyabilen özgün bir yapay zeka modeli geliştirmeyi amaçlamaktadır. Model, YOLOv8 algoritmasıyla eğitilmiş ve gerçek zamanlı çalışan bir masaüstü uygulamasıyla desteklenmiştir. Uygulama, kameradan gelen görüntüde yalnızca benim yüzümü algılar ve kutu içine alarak adımı gösterir.

---

## 🎯 Proje Hedefleri

- 📸 Kendi yüzümden oluşan özgün bir veri seti oluşturmak
- 🏷️ Roboflow ile fotoğrafları etiketlemek ve YOLOv8 formatında dışa aktarmak
- 🧠 YOLOv8 mimarisiyle yüz algılama modeli eğitmek
- 💻 Gerçek zamanlı kamera görüntüsü ile yüz tanıma uygulaması geliştirmek

---

## 🧪 Kullanılan Teknolojiler

| Teknoloji       | Açıklama                          |
|----------------|-----------------------------------|
| Python         | Ana programlama dili              |
| OpenCV         | Görüntü işleme kütüphanesi        |
| PyQt5          | Masaüstü arayüz (GUI) kütüphanesi |
| Roboflow       | Veri etiketleme ve dışa aktarma   |
| Ultralytics YOLOv8 | Yüz tanıma modeli              |

---

## 📷 Veri Seti ve Etiketleme

- 127 adet kendi yüz fotoğrafım farklı ışık, ifade ve arka plan koşullarında çekildi.
- Roboflow üzerinden bounding box ile yüzler işaretlendi.
- Etiketli veri seti YOLOv8 formatında dışa aktarıldı.

---

## 🧠 Model Eğitimi

- Eğitilen model: `YOLOv8n` (lightweight model)
- Epoch sayısı: 50
- Eğitim sonrası .pt formatında model elde edildi
- mAP ve loss değerleri takip edildi.
- VS Code kullanıldı.

---

## 🖥️ Uygulama Arayüzü (PyQt5)

- Kullanıcı arayüzü PyQt5 ile geliştirildi.
- "Kamerayı Başlat" butonuna tıklandığında model çalışmaya başlar.
- Kameradan gelen görüntüde yalnızca benim yüzüm algılanır ve etiketlenir.
- Algılama yoksa terminalde bilgi mesajı gösterilir.

---
## ✨ Öğrendiklerim
- Kendi verimle model eğitmenin püf noktaları
- Gerçek zamanlı görüntü işleme
- Etiketleme araçlarının önemi
- PyQt5 ile GUI tasarımı
- Git & GitHub ile proje yönetimi

