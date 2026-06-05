# Fox — DURUM / Kaldığımız Yer
*Yeni oturumda İLK okunan belge. "Şu an neredeyiz" — tek bakışta devral. Her önemli gelişmede güncellenir.*

**Son güncelleme:** 5 Haziran 2026 (Towdoo Faz 2 sonu) · **Statü:** Çırak / Filo Modu (Denetmen + orkestrasyon aktif)

---

## ŞU AN NEREDEYİZ (özet)
**Towdoo gerçek ilk müşteri pilotu** — Teslim Zinciri canlı çalışıyor. Faz 1 Keşif & Denetim (49/100 D, Moda/Perakende) ✅ + Faz 2 Strateji (Olgunluk 80/100 B) ✅ tamam. Strateji Denetmen'in tam 7-mercek denetiminden + 4 düzeltme + re-check'ten geçti; Fox+Denetmen konsensüs sağlandı. **Ayhan'ın masasında: strateji onayı** (Kademe 2). Onay sonrası Faz 3 İçerik devralır.

Daha önce (5 Haz): Marka Bulutu OS'u **SOC'nin kendi markasına uyguladık** (öz-pilot + öz-geliştirme). İki büyük sistem kuruldu: **Puanlama Rubriği v1** (ölçüm dili) + **Görsel Üretim Standardı v1** (görsel kalite). pdf-motoru v3'e çıktı (iki register teması). Lookalike içerik metodolojisi dış skill'den güvenle uyarlandı.

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
1. **⭐ Towdoo strateji onayı** — Faz 2 Strateji (`raporlar/towdoo-strateji.md`) konsensüs onaylı, Ayhan'ın son onayı bekliyor (Kademe 2). Onay → müşteriye teslim + Faz 3 İçerik başlar. İstenirse premium PDF'e dökülebilir.
2. **SOC denetim raporu → PDF** — md hazır, SEO Excel onaylı (Keşif). Yeni standartla (soc-mavi, pdf-motoru v3) İçerik Ajanı tam PDF üretmeli. Eski yanlış-standart PPTX silindi.
3. **Darya takip maili** — taslak hazır (Gmail draft), gönderim Ayhan'da
4. **gmail-personal** (stepsonclouds@) — OAuth yarım
5. **Scheduled task'lar** — bir kez "Run now" ile onayla
6. **Canva brand kit** — manuel kurulum
7. **Nesa/Luxmed** — çıkar çatışması, sözleşme öncesi stratejik karar
8. **Çırak→Kalfa terfisi** — Ayhan zamanı gelince

## ⭐ TOWDOO PİLOT — gerçek ilk müşteri (Teslim Zinciri)
Sürdürülebilir/vegan moda (cupro/vegan ipek), towdoo.com. Context: `sablonlar/towdoo-marka-context.md`.
- ✅ **Faz 1 Keşif & Denetim:** `raporlar/towdoo-marka-denetim-raporu.md` — 49/100 D (Moda/Perakende §2.2-B). Denetmen onaylı.
- ✅ **Faz 2 Strateji:** `raporlar/towdoo-strateji.md` — Olgunluk 80/100 B. Konumlandırma: **"erişilebilir vegan lüks"** (niLuu'nun terk ettiği TL/yerel alan). North Star: kendi kanal (web+email), Trendyol değil. Denetmen tam denetim + 4 düzeltme + re-check ✅. **Ayhan onayı bekliyor.**
- ⬜ **Faz 3 İçerik** → Faz 4 Growth (→ Branding gerekirse).
- **Denetmen kısıtları (devam eden):** (1) VTP "patent" iddiası doğrulanmadı — konumlandırmada YOK, sadece V-Label; müşteri belge sunarsa eklenir. (2) Greenwashing sınırı — çevresel iddia abartılmaz, vegan/etik ayağa ağırlık. (3) Verbatim müşteri sesi yok — mesaj mimarisi `[VARSAYIM]`, Faz 3'te 619 yorum analizi + verbatim toplantısıyla kalibre edilecek.
- **Açık veri eksiği:** GSC/Analytics yok → sayısal trafik hedefi verilemedi (dürüst N/A). Fiyat alt sınırı 119 TL (müşteri teyidi bekliyor).
- **Köprü hipotezi (🟡 izlenecek):** aksesuar→giyim "yükseltme" varsayımı kanıtlanmadı; Faz 4'te ölçülecek (§8.8).

## SOC ÖZ-PİLOT — Teslim Zinciri durumu (öğrenme amaçlı)
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
**Ayhan Towdoo stratejisini onaylayınca → Faz 3 İçerik Ajanı.** İlk görev net (strateji §9 devir notu): 619 Trendyol yorumunun sistematik analizi → mesaj mimarisini gerçek verbatim'le kalibre et (`[VARSAYIM]` etiketlerini gerçek müşteri diliyle değiştir). Sonra koleksiyon hikâye kopyası + materyal eğitimi içeriği + Dialogue editorial serisi. İstenirse strateji belgesi premium PDF'e (ayhan-premium veya marka teması) dökülebilir.

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
