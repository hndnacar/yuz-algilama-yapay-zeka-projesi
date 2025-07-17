# 📅 Yüz Algılama Projesi - Gelişim Günlüğü

Bu dosya, kendi yüzümü algılayan yapay zeka projesinin aşamalarını gün gün nasıl ilerlettiğimi ve neler öğrendiğimi belgeliyor.

---
## 🟢 1. Gün - Proje Analizi ve Planlama
📆 Tarih: 14 Temmuz 2025 Pazartesi
✅ Yapılanlar:
- Proje dokümanı detaylı olarak incelendi.
- Proje aşamaları ve yapılacaklar listelendi.
- Roboflow Universe platformuna göz atıldı.
- Fotoğraf çekimi için telefon ve kamera hazırlandı.

---

## 🟢 2. Gün - Veri Toplama
📆 Tarih: 15 Temmuz 2025  Salı
✅ Yapılanlar:
- Farklı ışık, arka plan ve açılardan toplam 85 adet kendi yüz fotoğrafım çekildi.
- Fotoğraflarda mimikler, gözlük, başörtüsü gibi çeşitli detaylara dikkat edildi.
- Veriler Roboflow’a yüklenmek üzere organize edildi.

---

## 🟢 3. Gün - Roboflow Üzerinde Etiketleme
📆 Tarih: 16 Temmuz 2025  Çarşamba
✅ Yapılanlar:
- Roboflow Universe üzerinden yeni proje oluşturuldu.
- Tüm yüz fotoğrafları yüklenerek bounding box ile etiketleme işlemi yapıldı.
- Veri artırımı uygulanmadı. Fotoğraflar farklı açılardan,arka plan veya mimiklerle oluşturuldu. Veri setimizi özgün bir şekilde hazırlayabilmemiz için herhangi bir veri artımı yaptırılmadı.
- Veri seti `YOLOv8` formatında dışa aktarıldı.
-Githuba projenin son hali yüklendi.

---

## 🟢 4. Gün - Model Eğitimi Başlangıcı
📆 Tarih: 17 Temmuz 2025  Perşembe
✅ Yapılanlar:
- `ultralytics` kütüphanesi kuruldu.
- YOLOv8n modeli seçildi (hafif model).
- Eğitim için gerekli konfigürasyon dosyası oluşturuldu.
- Eğitim süreci başlatıldı (50 epoch).
- Eğitim sırasında loss değerleri, mAP ve doğruluklar gözlemlendi.
- PyQt5 ile basit bir arayüz hazırlandı.
- Kamera butonu ile gerçek zamanlı yüz algılama aktif edildi.
- Sadece kendi yüzüm başarılı şekilde tanındı.
- Diğer yüzlerde düşük doğruluk gözlemlendi (istenen sonuç).
- GitHub reposu oluşturularak proje yüklendi.

---

## 🟢 5. Gün - Gerçek Zamanlı Uygulama ve PyQt5 Arayüzü
📆 Tarih: 18 Temmuz 2025 Cuma
✅ Yapılanlar:
- Eğitim tamamlandı, `.pt` modeli elde edildi.
- Uygulama farklı açılardan test edildi.
- GUI üzerinde iyileştirmeler yapıldı (fotoğraf yükleme, hata mesajı vb.).
- Proje klasörü düzenlendi.
- Proje anlatım videosu için senaryo hazırlandı.
- Ekran görüntüleri alındı, video kaydı hazırlandı.
- Video çekildi ve düzenlendi.

## ✨ Öğrendiklerim
- Gerçek zamanlı görüntü işleme için OpenCV + PyQt5 entegrasyonu
- Roboflow ile etiketleme 
- YOLOv8 kullanarak özel veri ile model eğitimi
- Git ve GitHub üzerinden proje sürüm kontrolü
