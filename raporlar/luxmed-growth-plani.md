# LUXMED PROTEZ — BÜYÜME PLANI v1
**Hazırlayan:** Steps On Clouds / Marka Bulutu OS — Growth Ajanı
**Tarih:** 10 Haziran 2026 | **Statü:** Kademe 2 — Ayhan onayı bekliyor
**Skor:** B (İyi) — Belge kalitesi

---

> **KAPSAM UYARISI:** Nesa exclusive meselesi kapsam dışı. O karar netleşmeden Nesa ile ilgili hiçbir karşılaştırma/konumlandırma başlatılmaz.
> **VERİ UYARISI:** Tüm sayısal hedefler "varsayım" etiketli — HTTP 403 çözümü + GSC bağlantısı sonrası kalibre edilir.

---

## BÖLÜM 1 — SEO / AI-SEO ÖNCELİK LİSTESİ

### 1.1 Teknik Taban — HTTP 403 Çözümü (Öncelik 0)

1. **Cloudflare WAF:** Bot fight mode / challenge passage → Googlebot User-Agent kural istisnasına ekle
2. **Cloudflare IP Access Rules:** Türkiye dışı engel açık mı? (Uluslararası hasta için kritik)
3. **Hosting (.htaccess / Nginx):** `deny from all` + selektif allow yapısı var mı?
4. **Test:** `curl -A "Googlebot" https://luxmedprotez.com/` → 200 dönüyor mu?
5. **GSC Search Inspect:** URL inspection → crawl test → teyit

403 düşmeden hiçbir SEO yatırımı anlam taşımaz.

### 1.2 Lokal SEO — Hedef Kelimeler

| Kelime | Intent | Hamle |
|---|---|---|
| Ottobock İstanbul | Markalı, yüksek niyet | Ürün sayfası + GMB kategori |
| Össur Türkiye / İstanbul | Markalı | Ürün alt sayfası + SSS |
| Protez ortez Fatih | Lokal | GMB + yerel içerik |
| İstanbul protez klinik | Genel lokal | Blog + GMB + schema |
| Bacak / kol protezi İstanbul | Ürün bazlı | Alt sayfa |

**Hamle paketi:** Her ürün kategorisi için ayrı alt sayfa + `MedicalBusiness` + `FAQPage` schema. GMB'de "Prosthetist" + "Orthotics & Prosthetics Service" kategorisi. NAP tutarlılığı tüm dizinlerde.

### 1.3 Uluslararası SEO — İlk 5 Hedef Kelime

| Öncelik | Kelime | Dil |
|---|---|---|
| 1 | "prosthetics Istanbul" | EN |
| 2 | "Ottobock authorized center Istanbul" | EN |
| 3 | "протез Стамбул" | RU |
| 4 | "prosthesis Istanbul medical tourism" | EN |
| 5 | "أطراف اصطناعية إسطنبول" | AR |

⚠️ hreflang (/en/ /ru/ /ar/) zorunlu. Native speaker doğrulaması olmadan RU/AR sayfa yayınlanmaz.

### 1.4 AI Overview Fırsat Soruları

- "SGK protez kapsamı 2026" → Blog + FAQPage schema
- "Ottobock ile Össur arasındaki fark nedir?" → Karşılaştırma içeriği
- "İstanbul'da protez kliniği nasıl seçilir?" → Seçim rehberi
- "Protez alımından önce nelere dikkat edilmeli?" → Pre-consultation rehberi

**GEO format zorunluluğu:** Her içerikte H2 soru formatı + liste + uzman imzası + güncelleme tarihi + FAQPage schema.

### 1.5 Schema Markup Öncelik Sırası

1. `MedicalBusiness` (klinik bilgileri)
2. `Physician` (uzman profili + dil kapasitesi)
3. `FAQPage` (her ürün sayfasına min. 3-4 SSS)
4. `AggregateRating` (4.7/5, 190 yorum)
5. `MedicalProcedure` (uygulama süreci)

---

## BÖLÜM 2 — BOOKİMED BÜYÜME PLANI

### 2.1 YMYL Uyum Kontrolü (Önce)

Bookimed'e yüklenmeden önce:
- "En iyi", "garantili", "kesin iyileşme" → yok
- Nesa karşılaştırması → yok
- Hasta fotoğrafı → KVKK yazılı izni olmadan yok

### 2.2 Profil Optimizasyon Kontrol Listesi

- [ ] Klinik adı: "Luxmed Prosthetics and Orthotics — Istanbul"
- [ ] EN açıklama (120-150 kelime): Ottobock+Össur yetkisi (belge doğrulandıktan sonra), konum, dil, lojistik. Sonuç vaadi yok.
- [ ] RU açıklama: native speaker doğrulamalı
- [ ] Fotoğraflar: gerçek klinik (dış + karşılama + uygulama birimi), stok yasak
- [ ] Uzman profili: ad + yeterlilik + dil
- [ ] Hizmet listesi: bacak/kol protezi, ortez (her biri ayrı satır)
- [ ] Fiyat: "Bilgi için iletişime geçin"
- [ ] WhatsApp + e-posta + telefon
- [ ] Ottobock/Össur yetkili belge görseli (IP onayı alındıktan sonra)

### 2.3 Yorum Talep + Yanıt Protokolü

Taburcu 24-48 saat sonra WhatsApp: "[Ad], Bookimed profilimize deneyiminizi yazabilirsiniz — [link]"
Yanıt protokolü: 24-48 saat, tıbbi detay yok, olumsuz yoruma çözüm odaklı yanıt + doğrudan iletişim daveti.

---

## BÖLÜM 3 — SOSYAL MEDYA BÜYÜME PLANI

### 3.1 Kanal Tekleştirme Protokolü

1. Birincil Instagram seç (@luxmedprosthetic veya @luxmedprotez — Luxmed kararı)
2. Diğer hesap: "Hesabımız taşındı: @[birincil]" son gönderi → 30 gün → kapatma kararı Luxmed'e
3. Facebook: aynı mantık, biri Business Page, diğeri arşiv

**Bu karar verilmeden kanal yatırımı başlatılmaz.**

### 3.2 Biyografi Yapısı (Birincil Hesap)

```
Luxmed Prosthetics & Orthotics – Istanbul
Ottobock & Össur Authorized Center
TR | EN | RU | AR
[WhatsApp linki] | [web linki]
```

### 3.3 Dil Kapsam Genişletme

- TR: her zaman birincil — haftada min. 3 gönderi
- EN: TR caption'a paralel dil olarak eklenir
- RU + AR: yüksek değerli içeriklere eklenir; native speaker doğrulaması zorunlu

### 3.4 Reels Format Önerileri

| Format | Değer |
|---|---|
| "Ürün nasıl çalışır" (product demo) | E-E-A-T yüksek |
| Klinik turu (atmosfer) | Güven + mekan teyidi |
| SSS yanıtı (uzman konuşuyor) | E-E-A-T + AI Overview |
| Hasta günlük an (KVKK izinli) | Onur merkezli |
| "İstanbul'a nasıl gelirsiniz" | Uluslararası hasta |

**Onur kuralı tüm Reels için geçerlidir.**

### 3.5 Google My Business Yorum Büyütme

Mevcut: 190 yorum, 4.7/5 (Tip A) | Hedef: 350 yorum / 12 ay (varsayım)

**Şablon (TR):**
"Sayın [Ad], sizinle çalışmak bizim için değerliydi. Deneyiminizi Google'da paylaşmanız, bize ulaşmayı düşünen hastalara yardımcı olur. [link]"

**EN:** "Thank you for choosing Luxmed. If you'd like to share your experience: [link]"

Kurallar: baskı yok, indirim karşılığı yok (Google politika ihlali). Negatif yoruma tıbbi detay paylaşmadan yanıt.

---

## BÖLÜM 4 — ULUSLARARASI HASTA DÖNÜŞÜM HUNİSİ

### 4.1 Yolculuk Haritası

```
Discovery (Google RU/EN/AR / Bookimed / tavsiye)
  ↓ [Sürtünme: dil bariyeri]
Araştırma → EN/RU/AR landing page + Bookimed profil
  ↓ [Sürtünme: güven + lojistik belirsizliği]
Karar → WhatsApp iletişim
  ↓ [Sürtünme: vize, konaklama, ulaşım]
Planlama → havalimanı karşılama + konaklama yönlendirme
  ↓
Tedavi
  ↓
Takip: 2. hafta / 3. ay / 1. yıl (kendi dilinde)
```

### 4.2 WhatsApp CTA A/B Test Planı

| Varyant | Metin | Hedef |
|---|---|---|
| A | "Randevu Al" | Yüksek niyet, doğrudan |
| B | "Bilgi Al — Ücretsiz" | Araştırma aşaması |
| C | "Ücretsiz Değerlendirme Talep Et" | Güven + uzmanlık algısı |

Ölçüm: min. 100 tıklama / varyant; UTM parametreli WhatsApp link. Karar: 200 toplam tıklama sonrası.
⚠️ A/B test için önce HTTP 403 çözümü şart.

### 4.3 Bookimed → WhatsApp Akışı

Bookimed CTA → WhatsApp açılır → karşılama mesajı:
"Merhaba, Luxmed'e hoş geldiniz. TR / EN / RU / AR — hangi dilde iletişim kurmak istersiniz?"
→ Dil seçimi → "Randevu / Ürün bilgisi / Fiyat sorgusu / Diğer"
→ 4 saat içinde yanıt (iş saati)

RU + AR versiyonları native speaker doğrulama gerektiriyor.

---

## BÖLÜM 5 — DOKTOR REFERRAL PROGRAMI (PİLOT)

### 5.1 Hedef Klinik Taraması

Bölge: Fatih, Aksaray, Laleli, Beyazıt, Çapa, Haseki
Uzmanlıklar: Ortopedi, Fizik Tedavi, Nöroloji, Vasküler Cerrahi
Arama protokolü: Google Maps → "Fatih ortopedi kliniği", "Aksaray fizik tedavi"
Hedef: 15-20 klinik/muayenehane listesi

Bu tarama Kademe 1. Gerçek temas Kademe 2 (Ayhan onayı).

### 5.2 Yaklaşım Paketi

- A5 klinik tanıtım kartı: konum, hizmet, iletişim, Ottobock/Össur (belge doğrulandıktan sonra)
- Ürün referans sayfası: hekim için teknik özet (endikasyonlar, ürün türleri)
- Referral izleme: "Bize nasıl ulaştınız?" sorusu tüm hastalara

Temas sırası: kliniği ziyaret → materyal bırak → 2 hafta sonra takip.
**Ticari komisyon değil** — "ortak hasta takibi" ilişkisi.

---

## BÖLÜM 6 — ELDE TUTMA / CRM PİLOT

### 6.1 Google Sheets Pilot Şablonu

| Alan | İçerik |
|---|---|
| Hasta ID (anonim) | P001, P002... |
| Uygulama tarihi | gg.aa.yyyy |
| Ürün türü / modeli | Bacak/Kol/Ortez + Ottobock X / Össur Y |
| Tahmini değişim tarihi | uygulama + 4 yıl (varsayım) |
| Dil tercihi | TR/EN/RU/AR |
| WhatsApp onayı (KVKK) | Evet/Hayır |
| Son / Sonraki temas tarihi | |

### 6.2 Yıllık Kontrol Şablonu (11. Ay)

**TR:** "Merhaba [Ad], [ürün] cihazınızın 12. ay kontrolü yaklaşıyor. Randevu için: [WhatsApp]"
**EN:** "Hello [Name], your annual check-up is approaching. To schedule: [WhatsApp link]"

### 6.3 Uluslararası Hasta Takip Şablonu

- **2. Hafta:** "Tedavinizin ardından 2. haftadayız. Cihazınızda uyum sorunu var mı? [WhatsApp]"
- **3. Ay:** "Cihazınızı günlük hayatta rahat kullanabiliyor musunuz? Yanıt için bekliyoruz."
- **1. Yıl:** "Yıllık kontrol veya ürün güncellemesi için İstanbul'a tekrar gelmek ister misiniz?"

Mesajlar hastanın dilinde. Tıbbi tanı/tavsiye içeremez. Luxmed hekimi onaylar.

### 6.4 CRM Araç Sırası

- **0-6 ay:** Google Sheets (ücretsiz, Fox şablon hazırlar)
- **6-12 ay değerlendirme:** HubSpot Free veya Zoho TR (KVKK: lokal sunucu tercih edilmeli)
- **Geçiş kriteri:** Aylık 50+ aktif hasta veya otomasyon ihtiyacı

---

## AARRR HAMLELERİ — ÖNCELIK SIRALI

| Hamle | AARRR | Sahip | Süre | Önkoşul |
|---|---|---|---|---|
| HTTP 403 çözümü | ACQ | Luxmed IT + Fox | Hemen | — |
| GSC kurulumu | ACQ | Luxmed + Fox | Hemen | 403 sonrası |
| Schema markup (Medical + FAQ + Rating) | ACQ | Fox brief → Luxmed dev | Haf 1-2 | 403 sonrası |
| GMB profil güncelle | ACQ | Luxmed + Fox | Haf 1-2 | — |
| Kanal tekleştirme kararı + uygulama | ACQ | Luxmed karar → Fox | Haf 1-2 | Luxmed karar |
| WhatsApp CTA A/B (3 varyant) | ACT | İçerik Ajanı → Luxmed | Haf 3-4 | 403 sonrası |
| EN landing page | ACQ+ACT | İçerik Ajanı → Luxmed dev | Haf 3-4 | — |
| Bookimed profil denetim + güncelle | ACQ | Fox + Luxmed | Haf 3-4 | YMYL uyum önce |
| GMB yorum talep akışı | ACT+REF | Fox şablon → Luxmed | Haf 5-8 | — |
| Blog: 2 TR + 1 EN SEO yazısı | ACQ | İçerik Ajanı | Haf 5-8 | — |
| Doktor referral listesi tarama | REF | Fox araştırma | Haf 5-8 | — |
| RU landing page (native doğrulamalı) | ACQ+ACT | İçerik Ajanı | Ay 2 | Native doğrulama |
| WhatsApp A/B sonuç analizi | ACT | Fox | Ay 3 | Min. 200 tıklama |
| CRM pilot (Sheets şablonu) | RET | Fox → Luxmed | Ay 3 | KVKK rıza formu |
| Doktor referral temas (materyal + ziyaret) | REF | Ayhan koordinasyon | Ay 3-4 | Materyal hazır |
| Hasta hikayesi içeriği (KVKK izinli) | REF | İçerik Ajanı + Ayhan | Ay 3 | Yazılı izin |
| AR landing page (native doğrulamalı) | ACQ | İçerik Ajanı | Ay 3-4 | Native doğrulama |
| 90 gün değerlendirme raporu | Tüm | Fox | Ay 3 | GSC + GMB + klinik veri |

---

## AYHAN'A BAYRAKLAR (4 Madde)

1. **Nesa exclusive:** Kapsam dışı — netleşince rekabet analizi eklenir
2. **Çok dilli kapasite:** RU/AR başlatılmadan native speaker operasyonel onayı gerekiyor
3. **Ottobock/Össur IP:** Yetkili uygulayıcı belgesi temin edilmeden marka adı merkezi konumlandırmaya alınmaz
4. **KVKK rıza altyapısı:** CRM + yorum akışı KVKK formu olmadan başlatılmaz

---

*Luxmed Protez Büyüme Planı v1 · Marka Bulutu OS · 10 Haziran 2026*
