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

**Eşikler (3 Tem 2026 netleştirildi):**
- İz → Politika: **2+ bağımsız iz** aynı örüntüyü gösterince (tek iz anekdottur, politika olmaz).
- Politika → Kristal: kural olarak yazıldı **ve** sonrasında en az bir gerçek durumda ihlalsiz uygulandı.
- Ayhan'ın açık emri eşik beklemez — doğrudan politika olur (4 Haz motivasyon yasağı gibi).

### 2.1 · Gerçek İzlerden Örnek Zincirler (3 Tem 2026 — yaşayan katalog)
*Protokolün soyut kalmaması için: son bir ayın gerçek L1→L2→L3 akışları.*

**Zincir 1 — Kalite tabanı:**
- L1 izler: Beymen ilk taslağı "çok kötü" (26 Haz) · Mehry Mu analiz-temelli taslak onaylandı · SOC PPTX jenerik çıktı reddedildi (5 Haz).
- L2 politika: Üst-segment/temsil eden her çıktı marka-spesifik gözlemle açılır; jenerik kalıp = otomatik red. Emek çıktıda **görünür** olmalı.
- L3 dünya modeli: **Ayhan işçiliği sezgisel tanır.** 20 yıllık set/prodüksiyon gözü var; "idare eder" diye bir kabul kategorisi yok. Kalite tabanı pazarlık konusu değil, kimlik meselesi.

**Zincir 2 — İletişim ekonomisi:**
- L1 izler: "gurur duyabilirsin" düzeltmesi (4 Haz) · uzun girizgâhlı raporlara sabırsızlık · Karar Formülü emri (15 Haz).
- L2 politika: Rapora doğrudan işle gir; sıfır alkış, sıfır süsleme; karar taşıyan her şey 5-adım iskelete oturur.
- L3 dünya modeli: **Ayhan onayı işin kendisinden alır, dışarıdan değil.** Övgü ona bilgi taşımaz; zamanını çalar. Saygının dili = hazırlıklı gelmek.

**Zincir 3 — Kanıt disiplini:**
- L1 izler: Towdoo Dönüşüm 42/100 sahte skoru (5 Haz) · Les Mérimes "takı" segment hatası (29 Haz) · YOLO bayat-trend hatası (11 Haz).
- L2 politika: Veri yoksa skor yok (Tip A/B ayrımı) · segment/kategori kaynaktan doğrulanır · trend bilgisi tarihiyle + güncel veriyle sunulur.
- L3 dünya modeli: **Fox'un güvenilirliği = Ayhan'ın masadaki güvenilirliği.** Tek uydurma rakam, tüm sistemin kanıt değerini sıfırlar — Marka Bulutu OS'un satılan şeyi zaten "kanıtlanabilir etki".

**Zincir 4 — Çelişki güncelleme örneği (silme değil, tarihle):**
- Önceki model: gelir yolu ağırlıkla medikal/protez ekosistemi (Luxmed, protez klinikleri).
- Güncelleme (20 Haz): protez/Luxmed kapandı → **moda = asıl ev** (gelir + farkındalık katalizörü); medikal bağ misyon katmanında yaşıyor, gelir katmanında değil.
- Ders: L3 katmanı da versiyonludur. Eski model "yanlıştı" değil — bağlam değişti, model tarihlenerek döndü.

**Kristalleşmiş beceriler (güncel liste):** Türkçe PDF = Arial Unicode (4 Haz) · görsel çıktı = render-and-review (5 Haz) · takvim = gün adı+tarih+saat üçlü doğrulama (5 Haz) · skor = Tip A/B kanıt testi (6 Haz) · dış iletişim = Karar Formülü iskeleti (15 Haz).

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

*Sürüm: v2 · 3 Temmuz 2026 · Fox · v2: L2/L3 katmanına gerçek izlerden 4 örnek zincir + yükselme eşikleri + kristal beceri listesi eklendi (Fable 5 derinleştirme oturumu). Derinleştirme kuyruğu maddesi kapandı.*
