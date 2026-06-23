# MBOS Moda Edisyonu — Görsel Kanıt Paketi
*Satış paketinin "pazarlama dilini görsel dil ile sentezliyorum" vaadini GÖSTERİMLE kanıtlayan 2 görsel.*

**Üreten:** Branding Ajanı (Fox filosu) · **20 Haziran 2026**
**Neden:** Denetmen Bulgu 5 / EK C — paket vaadi sözle vardı, gösterimle yoktu. Bu iki görsel o açığı kapatır.
**Standart:** `marka-bulutu-os-gorsel-uretim-standardi.md` + `fox-gorsel-parmak-izi.md` + `marka-bulutu-os-moda-sektor-bagi.md` (A.1 lüks kodlar) uygulandı. Render-and-review yapıldı.

---

## ÇIKTI 1 — MERAKÎ · Örnek Marka Görsel Dil Sistemi
**Dosya:** `cikti1-meraki-gorsel-dil.png` (kaynak: `.html`)

- **Ne:** Kurgusal-ama-gerçekçi bir contemporary kadın markası (MERAKÎ) için tek sayfalık görsel dil sistemi — konum cümlesi + atmosfer/mood panelleri + renk paleti (hex) + tipografi + görsel dil ilkeleri.
- **Etiket:** Sağ üstte **"Konsept · Örnek Çalışma"** damgası — sahte müşteri vakası DEĞİL, açıkça örnek.
- **Marka kurgusu:** MERAKÎ ("merak eden") — emerging contemporary kadın giyimi, 28–42 yaş, "az ama iyi", Anadolu zanaatı + modern editorial, sınırlı üretim / indirim yok (lüks kod, moda-sektor-bagi A.1).
- **Estetik:** Ayhan'ın görsel parmak izi — sıcak chiaroscuro, figür özne, malzeme dokusu, cömert boşluk, film-still hissi. **SOC mavisi DEĞİL** — markanın kendi estetiği.
- **Palet (kasıtlı imza):** Terracotta #8C3A2B (imza kızıl) · Derin Kızıl #5E261C · Taş Grisi #6E6A60 · Pirinç #A88A57 · Kemik #E9E2D4 · Mürekkep #211C18. **Bej-tuzağından kaçış:** imza kızıl + soğuk taş grisi kontrastı (sadece sıcak/bej değil — standart §11.B premium palet tuzağı).
- **Tipografi:** Didot (display, editorial serif — bilinçli karar, "serif=premium refleksi" değil) + Optima (humanist sans gövde).

## ÇIKTI 2 — Marka Bulutu OS · Moda Edisyonu · Paket Görsel Kimliği
**Dosya:** `cikti2a-kapak.png` (kapak) + `cikti2b-kimlik.png` (kimlik/sentez sayfası) (kaynak: tek `.html`)

- **Ne:** Satış paketinin/CMM sunumunun görsel kimliği — kapak + sentez diyagramı + renk sistemi + tipografi sistemi.
- **Register:** **Ayhan Erden (iş) — ayhan-premium.** Siyah #1A1C22 / Altın #A8814B / Krem #F4F1EA. marka-kiti.md "İş Register". **Salt yaratıcı güç** — motivasyon/süs estetiği YOK; editorial otorite. Misyon/ampüte ekseni yok (paket kararı).
- **Kalp kavram görselleşti:** "Pazarlama Dili" (sol beyin) + altın "&" düğümü ("Tek Yaratıcı Zihin") + "Görsel Dil" (sağ beyin) → tek imzada yakınsama. Sonuç: *"Ne 'güzel ama satmayan', ne 'satan ama çirkin'."* Bu, konumlandırma 1.0'ın doğrudan görsel karşılığı.
- **Fontlar:** Didot (display) + Avenir Next (gövde) — ayhan-premium standardı.

---

## ARAÇ
- **HTML + Chrome headless screenshot** (`--force-device-scale-factor=2`, retina/2x). Seçim nedeni: tam editorial dizgi kontrolü, gerçek sistem fontları (Didot/Optima/Avenir — hepsi Türkçe-tam), AI-slop'tan uzak el-yapımı kompozisyon, render'ın doğal screenshot vermesi (render-and-review için ideal). Canva'dan kaçınıldı (17 Haz dersi: paraphrase + Türkçe İ bozma riski).
- **PNG çözünürlük:** 3200×4100 (ÇIKTI 1) ve 3200×4000/sayfa (ÇIKTI 2).

## RENDER-AND-REVIEW — Ne gördüm, ne düzelttim
1. **Wordmark "MERAKÎ" sağa kayık + sağ kenarda kesiliyordu** (`text-indent` + letter-spacing hatası). → `text-indent` kaldırıldı, son-harf harf-aralığı negatif margin ile geri alındı; sola hizalı temiz hâl.
2. **Eyebrow ile wordmark "Î" aksanı hafif örtüşüyordu** ("ATÖLYE" sıkışık). → eyebrow'a alt boşluk eklendi.
3. **Atmosfer panelleri "boş/jenerik gradient" hissindeydi** (AI-slop riski!). → SVG fractalNoise film-grain + chiaroscuro vinyet katmanı eklendi; "amaçlı mood" hissine taşındı.
4. **ÇIKTI 1 panel 04 (Kemik) neredeyse görünmezdi.** → koyulaştırıldı, doku ve etiket okunur oldu.
5. **ÇIKTI 2 renk-barı açıklaması cılızdı** (stone, küçük). → koyu mürekkep tonuna + biraz büyüğe çekildi.
6. **CSS bug:** ÇIKTI 1'de bozuk hex (`#C9BFA d` boşluklu). → düzeltildi.

## AI-SLOP / GLYPH ÖZ-KONTROL — SONUÇ: TEMİZ
- **AI-slop kara listesi (her iki çıktı):** dekoratif başlık-altı çizgisi YOK · amaçsız renk bloğu YOK · full-width bar YOK · şablon kart dizilimi YOK · gradient abuse YOK (panel gradyanları grain+vinyetle amaçlı mood) · merkeze yığılmış metin YOK (gövde sola hizalı; yalnız sentez sonuç cümlesi tek-manifesto olarak ortalı) · düşük kontrast YOK · jenerik kurumsal estetik YOK · Lila/AI-glow YOK · Inter/slate-900 default YOK.
- **Premium palet tuzağı (§11.B):** ÇIKTI 1'de imza kızıl, ÇIKTI 2'de altın aksan — sadece-bej refleksinden kaçıldı.
- **Glyph/Türkçe:** İ ı ş ğ ç ö ü — render'da tek tek doğrulandı, kutu YOK (ATÖLYE, ÇALIŞMA, GÖRSEL DİL SİSTEMÎ, Çığır/Şükran/Düğüm/İğne, "kendini tanıyan"). **Bebas KULLANILMADI** (uppercase İ riski yok — Didot/Optima/Avenir hepsi Türkçe-tam). **₺ hiç kullanılmadı** (tuzak yok).
- **Onur & temsil:** Bu paket iş register'ı; ampüte/onur ekseni yok. Figür temsili soyut mood (gerçek kişi/AI yüz yok) — temsil etiği riski yok.

## EKSİK / FOX'A NE LAZIM
- **Eksik yok** — her iki çıktı tam, render edildi, denetlendi, teslim edilebilir.
- **Not (opsiyonel zenginleştirme, Fox/Ayhan kararı):** Atmosfer panelleri şu an renk+ışık+grain ile *mood tarifi* (amaçlı soyut). Pakete gerçek editorial fotoğraf konacaksa, bu paneller Ayhan'ın gerçek portföy karelerinin (Towdoo editorial / kampanya işleri) yerleştirileceği "placeholder mood" olarak da okunabilir — gerçek görsel gelince doku katmanı korunarak değiştirilir. Bu bir eksik değil, yükseltme yolu.
- **Denetmen'e:** Bu iki görsel, satış paketi v0'daki "vaat sözle, gösterimle değil" açığını (EK C) kapatma amaçlı. Pakete eklenmeden önce Denetmen 7 mercek (özellikle kalite tabanı/görsel + register tutarlılığı + Türkçe) re-check edebilir.

---

## MARKA KİMLİĞİ OLGUNLUK SKORU
*Rubrik Bölüm 5. Bu bir görsel-kanıt çıktısı (brand book değil); kategoriler bu kapsama göre değerlendirildi. Bölüm 0.1: müşteri verisi olmayan kalemler normalize edildi.*

| Kategori | Ağırlık | Skor | Gerekçe |
|---|---|---|---|
| Sözel Kimlik | %25 | 21/25 | Konum cümleleri + ses (ÇIKTI 2 vaadin kalbi, ÇIKTI 1 marka cümlesi) net. Tam brand book sözel katmanı değil (kapsam dışı) → tam puan değil. |
| Görsel Kimlik | %25 | 24/25 | Palet (hex) + tipografi (gerekçeli) + görsel dil + editorial ruh + grain/atmosfer. Slop yok, glyph temiz. |
| Brand Book Tamlığı | %20 | — (normalize) | Kapsam dışı: bu görsel kanıt, tam brand book değil. Rubrik §0.1 — skora katılmadı, diğer kategoriler normalize edildi. |
| Kanal-Arası Tutarlılık | %20 | 18/20 | İki çıktı içi tutarlılık kilitleri (renk/şekil/font) sağlam. Çok-kanal kanıtı (sosyal/web uygulaması) bu kapsamda yok. |
| Onur & Temsil (görsel) | %10 | 10/10 | İş register; ampüte ekseni yok. Soyut mood, AI yüz yok, temsil etiği riski yok. |

**Ağırlıklı (Brand Book kategorisi normalize edilerek, kalan %80 üzerinden):** **≈ 91/100 — A**
- SOC özel kontrol: **iki register ayrımı korundu** — ÇIKTI 1 bağımsız marka (kendi estetiği, SOC mavisi değil), ÇIKTI 2 ayhan-premium iş register (marka-kiti.md ile çelişki yok). ✅
- Eksik veri (Brand Book tamlığı) → Bölüm 0.1 uyarınca skora katılmadı, normalize edildi (sahte kesinlik yok).

---
*Branding Ajanı · Marka Bulutu OS · Görsel kanıt v1 · 20 Haziran 2026 · Render-and-review tamamlandı · Denetmen re-check'e hazır.*
