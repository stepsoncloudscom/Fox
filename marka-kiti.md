# Steps On Clouds — Marka Kiti
*Fox'un her görsel/tasarım üretiminde uyacağı marka kimliği. Brandbook v1.0'dan çıkarıldı.*

Bu dosya, üretilen her tasarımın (PDF, Canva, sosyal içerik) markaya uygun çıkması için zemindir. Canva prompt'larında, PDF motorunda ve görsel ekibinin briefinde referans alınır.

---

## RENK PALETİ

| Renk | Hex | Kullanım |
|---|---|---|
| **Phthalo Blue** | `#040D7E` | Ana marka rengi. Güven, derinlik, profesyonellik. |
| **Sky Blue** | `#72CBDF` | Taze, optimist. Vurgular ve destekleyici aksanlar. |
| **White Cloud** | `#FFFFFF` | Ana arka plan. Açıklık, aydınlık. |
| **Midnight Black** | `#101010` | Metin ve güçlü kontrast. Denge ve hassasiyet. |
| **Mist** | `#EAF6EB` | Yumuşak destek. Arka plan, kart, yüzey. |

**Önerilen denge:** %60 White Cloud · %20 Phthalo Blue · %10 Sky Blue · %10 Midnight Black
**Kural:** Mavi tonlar vurgu ve marka imzası için kullanılır.

---

## TİPOGRAFİ

**Başlık — Bebas Neue**
Kalın, kısa, BÜYÜK HARF. (Headline)
- H1: Bebas Neue Bold, 72pt, All Caps
- H2: Bebas Neue Bold, 36pt

**Gövde — Comfortaa**
Basit, okunabilir, yumuşak.
- Body: Comfortaa Regular, 18pt, %150 satır aralığı
- Caption: Comfortaa Regular, 8.5pt, %140 satır aralığı

---

## SES & TON (Görsel Metin)
Örnek marka cümleleri (Steps On Clouds register'ı):
- "BIG DREAMS START WITH SMALL STEPS."
- "Every Step Toward The Sky Matters."
- "Reaching the sky is not one giant leap. It is built through small, steady steps. Move forward with confidence and let your steps carry you higher."

Slogan: **"Take a Step Into The Sky"**

---

## İKİ REGISTER (Anayasa §9)

**1. Steps On Clouds — Misyon Register'ı**
Marka renkleri (Phthalo/Sky Blue), Bebas Neue + Comfortaa. Sosyal içerik, kampanya, topluluk, ampüte hikâyeleri. Onur merkezli — acıma yok, ilham pornosu yok.

**2. Ayhan Erden — İş Register'ı**
Premium, nötr estetik (siyah/altın — #1a1a1a + #A8814B). Teklif, sözleşme, kurumsal belge. PDF motorunun varsayılan teması bu. Müşteri markasının kimliği öne çıkar, Steps On Clouds imzası geride durur.

---

## LOGO
- Birincil logo: `/Users/ayhanerden/Desktop/Steps On Clouds/Legal/assets/soc_logo.png`
- Brandbook: `/Users/ayhanerden/Desktop/Steps On Clouds/Brandbook /`
- Logo etrafında temiz alan: logo yüksekliği kadar boşluk bırak.
- Yanlış kullanım: germe, döndürme, efekt, düşük kontrast, marka dışı renk.

---

## CANVA'DA MARKA KİTİ (Manuel Kurulum Gerekli)
⚠️ Canva API'si programatik brand kit oluşturmaya izin vermiyor. Steps On Clouds brand kit'i Canva arayüzünden bir kez kurulmalı:
- Brand Kit → renkleri ekle (yukarıdaki 5 hex)
- Fontları yükle (Bebas Neue, Comfortaa)
- Logoyu yükle
Kurulduktan sonra Fox `list-brand-kits` ile erişip tüm Canva tasarımlarında otomatik uygular.

**O zamana kadar:** Fox her Canva prompt'una bu paleti ve fontları açıkça yazar.

---

## MÜŞTERİ MARKA KİTLERİ
Her müşteri için ayrı kit buraya eklenecek (renk, font, ses). Şu an:
- **Luxmed — KİMLİK HAZIR ✅** → `raporlar/luxmed-branding-kimlik.md` (Faz 3 Branding çıktısı, 10 Haz: tagline B finali, marka sesi 5 nitelik, sözel kimlik; Ayhan onayı sonrası müşteriye sunulacak)
- **Ala Skateboards — aktif** — siyah/beyaz, kaykay kültürü, ä logosu (B2B materyaller: `raporlar/ala-materyaller/`)
- *Arşiv (iş kapandı, referans değeri):* Towdoo — cupro, sürdürülebilir lüks, editorial (`sablonlar/towdoo-marka-context.md`) · Darya Dental — kit çıkarılmadı

---
*Sürüm: v1 · 4 Haziran 2026 · Fox · Kaynak: Steps On Clouds Brand Identity Guide v1.0*
