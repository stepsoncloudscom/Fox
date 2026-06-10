# Fox — Teklif & Sözleşme Motoru
*Tekrarlanabilir şablonlar. Yeni müşteriye dakikalar içinde markalı, Türkçe-doğru, Marka Bulutu standardında çıktı.*

## Klasör İçeriği

| Dosya | Ne için |
|---|---|
| `mail-marka-elciligi-TR.md` | Markalara marka elçiliği / iş birliği teklif maili (Ayhan'ın sesiyle) |
| `mail-takip-EN.md` | İngilizce müşteri takip maili |
| `teklif-marka-bulutu-TR.md` | Aylık danışmanlık teklif yapısı |
| `pdf-motoru.py` | v3 — iki temalı PDF motoru (soc-mavi / ayhan-premium), marka fontlu, Türkçe-doğru |
| `ala-print-materyaller.py` | Ala B2B baskı materyalleri üreticisi (hang tag, shelf talker, poster, QR kart) |
| `musteri-marka-context-sablonu.md` | ⭐ Her müşteri için tek kaynak doğruluk belgesi — tüm ajanlar referans alır |
| `luxmed-marka-context.md` · `soc-marka-context.md` · `towdoo-marka-context.md` (arşiv) | Doldurulmuş müşteri context'leri |
| `run-for-empathy-etkinlik-context.md` | RFE etkinlik context'i (5 Tem 2026) |
| `SOC_2026_Pazarlama_Plani.xlsx` | Yıllık pazarlama planı (Drive native Sheets ile sync) |
| `araclar/` | marka_analiz.py · rakip_tarama.py · rapor_pdf.py |

*Not: Eski Model A/B sözleşme şablonları (konsinyasyon/barter) kaldırıldı — Ala iş modeli 4 Haz'da değişti (bedelsiz alan + ortak içerik), şablonlar geçersizleşti.*

## Kullanım Disiplini

1. **Değişkenler köşeli parantezde:** `[MÜŞTERİ]`, `[TUTAR]`, `[TARİH]`. Üretirken hepsini doldur — boş `[...]` bırakma.
2. **Ses:** Mail şablonları Ayhan'ın ses parmak izine dayanır (bkz. `../fox-ses-parmak-izi.md`). Taklit et, içeriği uydurma.
3. **Rakam asla uydurulmaz:** Fiyat/taahhüt Ayhan'dan gelir veya gerçek kaynaktan.
4. **PDF kuralı:** Tüm PDF üretimi `pdf-motoru.py` üzerinden — register seç (`soc-mavi` / `ayhan-premium`), marka fontu zorunlu (Bebas/Comfortaa veya Didot/Avenir; `../assets/fonts/`). Arial Unicode yalnızca Türkçe-güvenli yedek. Ayrıntı: `../marka-bulutu-os-gorsel-uretim-standardi.md`.
5. **Öz-denetim:** Çıktıdan önce `../fox-oz-denetim-ve-nobet.md` 8 sorusunu uygula (görsel çıktıda §8 render-and-review dahil).
6. **Kademe 2:** Hiçbir teklif/sözleşme onaysız gönderilmez/imzalanmaz. Hazırla, Ayhan'a sun.

## Logolar
- Steps On Clouds: `/Users/ayhanerden/Desktop/Steps On Clouds/Legal/assets/soc_logo.png`
- Partner logoları müşteriye göre eklenir.

---
*Sürüm: v2 · 11 Haziran 2026 · Fox · v2: dosya listesi gerçek klasör içeriğiyle eşitlendi, PDF kuralı v3 motora güncellendi.*
