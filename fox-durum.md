# Fox — DURUM / Kaldığımız Yer
*Yeni oturumda İLK okunan belge. "Şu an neredeyiz" — tek bakışta devral. Her önemli gelişmede güncellenir.*

**Son güncelleme:** 5 Haziran 2026 · **Statü:** Çırak / Filo Modu (Denetmen + orkestrasyon aktif)

---

## ŞU AN NEREDEYİZ (özet)
5 Haziran: Marka Bulutu OS'u **SOC'nin kendi markasına uyguladık** (canlı referans + öz-geliştirme). Teslim Zinciri çalıştı: Keşif & Denetim → SOC marka denetim raporu (40/100, D — baseline). Denetmen turu tam yapıldı, 5 bulgu düzeltildi. İki büyük sistem kuruldu: **Puanlama Rubriği v1** (ölçüm dili) + **Görsel Üretim Standardı v1** (görsel kalite). pdf-motoru v3'e çıktı (iki register teması). Lookalike içerik metodolojisi dış skill'den güvenle uyarlandı.

**KRİTİK DERS (5 Haz):** İlk SOC denetim PPTX'i marka fontunu ihlal etti + editorial ruh taşımadı + AI-slop + ₺ kutu — ve Fox denetiminden geçti. Ayhan yakaladı. Kök neden: Fox'un görsel kalite merceği zayıftı. Kapatıldı: öz-denetim 8. soru (görsel) + render-and-review zorunlu + Görsel Üretim Standardı.

## FİLO (aktif)
Fox (orkestratör) · Denetmen (7 mercek) · Keşif&Denetim · Strateji · İçerik · Growth · Branding.
**Yok:** İş Katmanı (Satış/Finans/Hukuk/Operasyon), Görev Ajanı, Kendi Markan Ajanı.

## YENİ SİSTEMLER (5 Haz — tüm ajanlar kullanır)
- **Puanlama Rubriği** (`marka-bulutu-os-puanlama-rubrigi.md`): her ajanın kendi rubriği + 5 sektör bağlamı + kaynaklı benchmark. Eksik veri kuralı (Bölüm 0.1) keyfi skoru yasaklar. v2: 5 Eyl.
- **Görsel Üretim Standardı** (`marka-bulutu-os-gorsel-uretim-standardi.md`): ZORUNLU. Register, marka fontu, editorial ruh, AI-slop kara listesi, glyph/Türkçe, render-and-review.
- **Lookalike İçerik** (`marka-bulutu-os-lookalike-icerik.md`): performans-temelli üretim, güvenlik-uyarlanmış (Perplexity→WebSearch, onur filtresi).
- **pdf-motoru v3** (`sablonlar/pdf-motoru.py`): iki tema → `soc-mavi` (Bebas/Comfortaa/Phthalo, marka/misyon) + `ayhan-premium` (Didot/Avenir/altın, iş). Fontlar: `assets/fonts/`.

## AÇIK İŞLER — Ayhan'ın masasında
1. **SOC denetim raporu → PDF** — md hazır, SEO Excel onaylı (Keşif). Yeni standartla (soc-mavi, pdf-motoru v3) İçerik Ajanı tam PDF üretmeli. Eski yanlış-standart PPTX silindi.
2. **Darya takip maili** — taslak hazır (Gmail draft), gönderim Ayhan'da
3. **gmail-personal** (stepsonclouds@) — OAuth yarım
4. **Scheduled task'lar** — bir kez "Run now" ile onayla
5. **Canva brand kit** — manuel kurulum
6. **Nesa/Luxmed** — çıkar çatışması, sözleşme öncesi stratejik karar
7. **Çırak→Kalfa terfisi** — Ayhan zamanı gelince

## SOC PİLOT — Teslim Zinciri durumu
- ✅ **Faz 1 Keşif & Denetim:** rapor (`raporlar/soc-marka-denetim-raporu.md`, 40/100 D) + SEO Excel (`soc-seo-kritik.xlsx`, Keşif onaylı). SOC context: `sablonlar/soc-marka-context.md`.
- ⏳ **PDF üretimi:** raporun premium PDF hali (soc-mavi) bekliyor.
- ⬜ **Faz 2 Strateji** (konumlandırma çatallanması çöz) → Faz 3 Branding → Faz 4 İçerik → Faz 5 Growth.

## YAKLAŞAN TAKVİM
- **Pazar 7 Haz:** 07:30-14:00 Empati Koşusu
- **Pzt 8 Haz:** 10:00 Enes/Luxmed araması

## RİSK BAYRAKLARI
- Nesa↔Luxmed çatışması · SOC kendi tracking'i yok (GSC bağlanmalı — meta/Instagram baseline ölçülemedi)
- **Görsel kalite:** her görsel çıktı render-and-review'den geçmeli (5 Haz dersi) — Fox tek başına "renk doğru" demekle yetinmez.

## SIRADAKİ BÜYÜK ADIM (öneri)
SOC denetim raporunu yeni standartla PDF'e dök (İçerik Ajanı → Keşif onay → Denetmen+Fox → Ayhan). Sonra Faz 2 Strateji: SOC konumlandırma çatallanmasını çöz.

## DETAY HARİTASI (lazım oldukça oku)
- Kim/vizyon: `fox-kuzey-yildizi.md` · Kişiler: `fox-iliski-hafizasi.md`
- Kararlar: `fox-karar-gunlugu.md` · Ses: `fox-ses-parmak-izi.md` · Görsel: `fox-gorsel-parmak-izi.md` + `fox-estetik-mufredati.md`
- Ajan tanımları: `.claude/agents/*.md`
- ⭐ Ortak sistemler: puanlama rubriği · görsel üretim standardı · lookalike içerik
- Üretim: `sablonlar/pdf-motoru.py` (v3, iki tema), `assets/fonts/`, `sablonlar/araclar/marka_analiz.py`
- Müşteri context şablonu: `sablonlar/musteri-marka-context-sablonu.md`
- Protokoller: hafıza, orkestrasyon, öz-denetim/nöbet (8 soru) · Müfredatlar: gelişim, büyüme, estetik
- Notion pano data source: `f4c97159-9c85-4766-b122-760b00b9c321`

## SÜREKLİLİK & GİT
- **SSH push kurulu** (ed25519, github.com:stepsoncloudscom/Fox) — `git push origin main` doğrudan çalışır.
- **Checkpoint emri:** Context dolunca/oturum biterken → bu dosyayı güncelle + commit + push (izin bekleme).
- **Ses kuralı:** Ayhan'a motivasyon/övgü cümlesi YOK — doğrudan işe geç.

---
*Disiplin: Her oturum sonu bu dosyayı güncel tut + commit + push. Yeni Fox bunu + CLAUDE.md okuyunca tam devralır.*
