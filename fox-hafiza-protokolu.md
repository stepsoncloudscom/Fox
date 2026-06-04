# Fox Hafıza Protokolü — Yaşayan Ayhan Modeli
*Çok kademeli hafıza + kendini güncelleyen yapı + yansıtmalı yönetim. Tüm hafıza dosyalarını yöneten üst-katman.*
*Kaynak ilhamı: MemOS, LD-Agent persona modeling, Reflective Memory Management (ACL 2025).*

Bu protokol, Fox'un dağınık dosyalarını **tek bir yaşayan Ayhan modeline** dönüştürür. Hafıza artık pasif depo değil — kapsamlı, kendini güncelleyen, ne tutacağını bilen bir katman.

---

## 1 · ÇOK KADEMELİ KAPSAM (Multi-Scope)

Her bilgi parçası bir **kapsam** taşır. Hangi dosyaya, ne kalıcılıkla yazılacağını bu belirler.

| Kapsam | Ne | Nerede | Kalıcılık |
|---|---|---|---|
| **Çekirdek** | Ayhan'ın değerleri, kimliği, kırmızı çizgileri | CLAUDE.md, ilişki-hafizasi (çekirdek) | Asla silinmez |
| **Proje** | Müşteriler, kararlar, açık işler | karar-gunlugu, Notion panosu, ilişki-hafizasi | Proje bitince arşivlenir |
| **Oturum** | Bugünkü konuşma, geçici bağlam | Context (uçucu) | Oturum sonu özetlenir |
| **Filo** | Ajan tanımları, gelişim, koordinasyon | denetmen.md, gelisim-mufredati, orkestrasyon | Yaşayan |

**Kural:** Yeni bilgi geldiğinde önce kapsamını belirle, sonra doğru dosyaya yaz. Oturum-kapsamı bilgiyi kalıcı dosyaya yazma (gürültü). Çekirdek-kapsamı bilgiyi asla oturumda bırakma (kayıp riski).

---

## 2 · KENDİNİ GÜNCELLEYEN HAFIZA (Self-Evolving)

MemOS katmanları, Fox'a uyarlanmış:

- **L1 — İz:** Ham gözlem. "Ayhan Cuma görüşmesinde gergindi."
- **L2 — Politika:** Tekrarlayan izden çıkan kural. "Tuğba görüşmeleri hassas — önce insani bağ."
- **L3 — Dünya Modeli:** Ayhan'ın bütünsel resmi. "Ayhan ilişkiyi işin önüne koyar; bu bir değer, taktik değil."
- **Kristalleşmiş Beceri:** Artık otomatik olan. "Türkçe PDF = Arial Unicode" gibi.

**Akış:** İz birikir → tekrar ederse politikaya yükselir → politikalar dünya modelini günceller → kanıtlanmış politika kristalleşir (kurala döner, `Çözülenler Arşivi`).

---

## 3 · YANSITMALI YÖNETİM (Reflective — Ne Tutulur, Ne Unutulur)

Her şeyi tutmak hafızayı zehirler. Düzenli yansıma:

**Tut:** Tekrar eden örüntü, değer, ilişki dokusu, karar gerekçesi, kanıtlanmış ders.
**Unut/Arşivle:** Tek seferlik ayrıntı, çözülmüş geçici sorun, eskiyen proje verisi.
**Çelişki çıkarsa:** Yeni bilgi eskisiyle çelişiyorsa — eskiyi silme, **güncelle ve tarihle.** ("Önce X'ti, 4 Haz'da Y oldu, çünkü...")

**Yansıma ritmi:** Her oturum sonu (oturum→kalıcı süzme) · Aylık review (politika gözden geçir) · Çeyreklik (dünya modeli + arşiv).

---

## 4 · YAŞAYAN AYHAN MODELİ

Tüm hafıza dosyaları tek bir soruya hizmet eder: **"Ayhan kim ve şu an neye ihtiyacı var?"**

Bileşenler (hepsi canlı, her etkileşimde güncellenebilir):
- **Değerler & kırmızı çizgiler** → CLAUDE.md §0, §11
- **Ses & ifade** → fox-ses-parmak-izi.md
- **İlişkiler & hassasiyetler** → fox-iliski-hafizasi.md
- **Kararlar & gerekçeler** → fox-karar-gunlugu.md
- **Örüntüler & öngörüler** → bu dosya (L2/L3) + nöbet protokolü

**Disiplin:** Bir etkileşimde Ayhan'a dair yeni bir şey öğrenirsem (tercih, tepki, örüntü) — ilgili dosyaya işle. Model donuk kalırsa gölge soluklaşır.

---

*Sürüm: v1 · 4 Haziran 2026 · Fox · Faz 1 derinleştirme + User Modeling entegrasyonu*
