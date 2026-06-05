# Fox — DURUM / Kaldığımız Yer
*Yeni oturumda İLK okunan belge. "Şu an neredeyiz" — tek bakışta devral. Her önemli gelişmede güncellenir.*

**Son güncelleme:** 6 Haziran 2026 (Sahte-kesinlik düzeltmesi + gstack öğrenimi) · **Statü:** Çırak / Filo Modu (Denetmen + orkestrasyon aktif)

---

## ŞU AN NEREDEYİZ (özet)
**Towdoo (Tuğba Hanım'ın markası) — ilk gerçek müşteri, teklif aşamasında.** Notion durumu "Teklif Gönderildi" (45k TL/ay, 6 ay). Teslim Zinciri çalıştı: Faz 1 Keşif & Denetim (Baseline: Zayıf ağırlıklı niteliksel profil, Moda) ✅ + Faz 2 Strateji (Olgunluk 80/100 B — belge kalitesi) ✅. Strateji Denetmen tam denetim + 4 düzeltme + re-check'ten geçti; Fox+Denetmen konsensüs. **KARAR (5 Haz): iç çalışma, beklet.** Teklif imzalanmadan müşteriye verilmeyecek (bedava iş riski, §11.3). Faz 3'e geçilmedi. Belgeler dosyada hazır; teklif netleşince teslim + Faz 3 devam.
> ⚠️ **İlişki hassas:** Tuğba = Ayhan'ın zor döneminde ~1 yıl yanında duran kişi (anne figürü, annesini kaybetti). Kızı Sanem + ekip arka planda Ayhan aleyhine referans. Towdoo işinde Sanem faktörü hesaba katılır. Detay: `fox-iliski-hafizasi.md`.

Daha önce (5 Haz): Marka Bulutu OS'u **SOC'nin kendi markasına uyguladık** (öz-pilot + öz-geliştirme). İki büyük sistem kuruldu: **Puanlama Rubriği v1** (ölçüm dili) + **Görsel Üretim Standardı v1** (görsel kalite). pdf-motoru v3'e çıktı (iki register teması). Lookalike içerik metodolojisi dış skill'den güvenle uyarlandı.

**KRİTİK DERS (5 Haz):** İlk SOC denetim PPTX'i marka fontunu ihlal etti + editorial ruh taşımadı + AI-slop + ₺ kutu — ve Fox denetiminden geçti. Ayhan yakaladı. Kök neden: Fox'un görsel kalite merceği zayıftı. Kapatıldı: öz-denetim 8. soru (görsel) + render-and-review zorunlu + Görsel Üretim Standardı.

**KRİTİK DERS 2 (5-6 Haz) — Sahte Kesinlik:** Towdoo denetiminde gerçek performans verisi (CVR/trafik) olmadan kategorilere sayısal puan (Dönüşüm 42/100, genel 49/100) verildi — gözlem, ölçüm gibi sunuldu. Hata Denetmen + konsensüsten geçti; **Ayhan yakaladı** ("kabul edilemez"). Kök neden: Rubrik §0.1 "veri" derken gözlem ile performansı ayırmıyordu. Kapatıldı → **Rubrik §0.1 v1.1 İki Katman Kanıt** (Tip A ölçülmüş→sayısal / Tip B gözlem→niteliksel band). Towdoo + SOC raporları niteliksel profile çevrildi, strateji hedefi band ilerlemesine döndü, Denetmen 8. mercek "Sahte Kesinlik Kontrolü" eklendi, Keşif Ajanı metodolojisi güncellendi.

## FİLO (aktif)
Fox (orkestratör) · Denetmen (7 mercek) · Keşif&Denetim · Strateji · İçerik · Growth · Branding.
**Yok:** İş Katmanı (Satış/Finans/Hukuk/Operasyon), Görev Ajanı, Kendi Markan Ajanı.

## YENİ SİSTEMLER (5 Haz — tüm ajanlar kullanır)
- **Puanlama Rubriği v1.1** (`marka-bulutu-os-puanlama-rubrigi.md`): her ajanın kendi rubriği + 5 sektör bağlamı + kaynaklı benchmark. **§0.1 İki Katman Kanıt (Tip A ölçülmüş→sayısal / Tip B gözlem→niteliksel band)** — gözlemi performans gibi sayısallaştırmayı yasaklar (5-6 Haz sahte-kesinlik düzeltmesi). v2: 5 Eyl.
- **Görsel Üretim Standardı** (`marka-bulutu-os-gorsel-uretim-standardi.md`): ZORUNLU. Register, marka fontu, editorial ruh, AI-slop kara listesi, glyph/Türkçe, render-and-review.
- **Lookalike İçerik** (`marka-bulutu-os-lookalike-icerik.md`): performans-temelli üretim, güvenlik-uyarlanmış (Perplexity→WebSearch, onur filtresi).
- **pdf-motoru v3** (`sablonlar/pdf-motoru.py`): iki tema → `soc-mavi` (Bebas/Comfortaa/Phthalo, marka/misyon) + `ayhan-premium` (Didot/Avenir/altın, iş). Fontlar: `assets/fonts/`.

## AÇIK İŞLER — Ayhan'ın masasında
1. **⭐ Towdoo teklif sonucu** — Strateji (`raporlar/towdoo-strateji.md`) konsensüs onaylı ama **iç çalışma olarak bekletiliyor** (karar 5 Haz: teklif imzalanmadan teslim yok). Teklif kapanınca → premium PDF + müşteriye teslim + Faz 3 İçerik. Şu an Ayhan'dan beklenen: teklif/sunum sonucu.
2. **SOC denetim raporu → PDF** — md hazır, SEO Excel onaylı (Keşif). Yeni standartla (soc-mavi, pdf-motoru v3) İçerik Ajanı tam PDF üretmeli. Eski yanlış-standart PPTX silindi.
3. **Darya takip maili** — taslak hazır (Gmail draft), gönderim Ayhan'da
4. **gmail-personal** (stepsonclouds@) — OAuth yarım
5. **Scheduled task'lar** — bir kez "Run now" ile onayla
6. **Canva brand kit** — manuel kurulum
7. **Nesa/Luxmed** — çıkar çatışması, sözleşme öncesi stratejik karar
8. **Çırak→Kalfa terfisi** — Ayhan zamanı gelince

## ⭐ TOWDOO — ilk gerçek müşteri (teklif aşaması, Teslim Zinciri)
Sürdürülebilir/vegan moda (cupro/vegan ipek), towdoo.com. **Sahibi: Tuğba Hanım** (hassas ilişki — yukarı bak). Notion: "Teklif Gönderildi", 45k TL/ay × 6 ay, Öncelik Yüksek, İlgili: Tuğba + Furkan. Context: `sablonlar/towdoo-marka-context.md`.
- ✅ **Faz 1 Keşif & Denetim:** `raporlar/towdoo-marka-denetim-raporu.md` — **Baseline: Zayıf ağırlıklı niteliksel profil** (Moda/Perakende §2.2-B). Sayısal genel skor YOK (§0.1 v1.1 — Tip A verisi yok); tek Tip A = Trendyol 4.3/5. Gerçek performans baseline'ı GSC bağlanınca. Denetmen onaylı (sahte-kesinlik düzeltmesi sonrası).
- ✅ **Faz 2 Strateji:** `raporlar/towdoo-strateji.md` — Olgunluk 80/100 B (belge kalitesi, marka performansı değil). Konumlandırma: **"erişilebilir vegan lüks"** (niLuu'nun terk ettiği TL/yerel alan). North Star: kendi kanal (web+email), Trendyol değil. 12-ay hedefi niteliksel band ilerlemesi (sayısal skor değil — §0.1 v1.1). Denetmen tam denetim + 4 düzeltme + re-check ✅.
- ⏸️ **BEKLEMEDE (karar 5 Haz):** Strateji iç çalışma — teklif imzalanmadan müşteriye verilmeyecek (§11.3). Faz 3'e geçilmedi.
- ⬜ **Faz 3 İçerik** (teklif kapanınca) → Faz 4 Growth (→ Branding gerekirse). İlk görev: 619 yorum verbatim analizi → mesaj mimarisi kalibrasyonu.
- **Denetmen kısıtları (devam eden):** (1) VTP "patent" iddiası doğrulanmadı — konumlandırmada YOK, sadece V-Label; müşteri belge sunarsa eklenir. (2) Greenwashing sınırı — çevresel iddia abartılmaz, vegan/etik ayağa ağırlık. (3) Verbatim müşteri sesi yok — mesaj mimarisi `[VARSAYIM]`, Faz 3'te 619 yorum analizi + verbatim toplantısıyla kalibre edilecek.
- **Açık veri eksiği:** GSC/Analytics yok → sayısal trafik hedefi verilemedi (dürüst N/A). Fiyat alt sınırı 119 TL (müşteri teyidi bekliyor).
- **Köprü hipotezi (🟡 izlenecek):** aksesuar→giyim "yükseltme" varsayımı kanıtlanmadı; Faz 4'te ölçülecek (§8.8).

## SOC ÖZ-PİLOT — Teslim Zinciri durumu (öğrenme amaçlı)
- ✅ **Faz 1 Keşif & Denetim:** rapor (`raporlar/soc-marka-denetim-raporu.md`, **Baseline: Kritik açık ağırlıklı niteliksel profil** — §0.1 v1.1, sayısal skor yok) + SEO Excel (`soc-seo-kritik.xlsx`, Keşif onaylı). SOC context: `sablonlar/soc-marka-context.md`.
- ⏳ **PDF üretimi:** raporun premium PDF hali (soc-mavi) bekliyor.
- ⬜ **Faz 2 Strateji** (konumlandırma çatallanması çöz) → Faz 3 Branding → Faz 4 İçerik → Faz 5 Growth.

## YAKLAŞAN TAKVİM
- **Pazar 7 Haz:** 07:30-14:00 Empati Koşusu
- **Pzt 8 Haz:** 10:00 Enes/Luxmed araması

## RİSK BAYRAKLARI
- Nesa↔Luxmed çatışması · SOC kendi tracking'i yok (GSC bağlanmalı — meta/Instagram baseline ölçülemedi)
- **Görsel kalite:** her görsel çıktı render-and-review'den geçmeli (5 Haz dersi) — Fox tek başına "renk doğru" demekle yetinmez.

## SIRADAKİ BÜYÜK ADIM (öneri)
**Towdoo beklemede** (teklif sonucu) — o gelene kadar Towdoo'da aksiyon yok. Teklif kapanırsa: premium PDF + Faz 3 İçerik (619 yorum verbatim → mesaj kalibrasyonu, strateji §9 devir notu). Bu arada ilerletilebilir öncelikler: **SOC öz-pilotu** (denetim raporu premium PDF → Faz 2 Strateji) veya Ayhan'ın gündemi. Towdoo'da proaktif iş yapma — teklif netleşmeden token/efor harcanmaz.

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
