# Marka Bulutu OS — Görsel Üretim Standardı
*Görsel üreten her ajanın (İçerik, Branding) ZORUNLU uyacağı kurallar. Estetik müfredatı + görsel parmak izi + marka kiti'nin somut uygulama katmanı. Puanlama rubriği gibi ortak standart.*

**Sürüm:** v1 · **Yürürlük:** 5 Haziran 2026 · **Sonraki revizyon:** 5 Eylül 2026
**Tetikleyici olay:** 5 Haz — SOC denetim PPTX'i marka fontunu ihlal etti, editorial ruh taşımadı, AI-slop sinyalleri verdi ve Fox denetiminden geçti. Bu standart o açığı kapatır.

---

## 0 · NEDEN BU BELGE VAR — Beş Hatanın Anatomisi

5 Haziran'da üretilen SOC denetim sunumu "müşteriye sunulabilir" onayı aldı. Estetik mercekle bakınca beş hata görüldü. **Bu beş hata bir daha hiçbir çıktıdan geçmeyecek:**

1. **Tipografi ihlali:** Marka fontu Bebas Neue + Comfortaa iken Arial Black + Calibri kullanıldı. → *Tipografi = ses tonu. Yanlış font yanlış marka.*
2. **Editorial ruh yok:** Ayhan'ın imzası sıcak/atmosferik/sinematik/editorial iken çıktı düz kurumsal "PowerPoint" oldu.
3. **AI-slop sinyalleri:** Her başlık yanında dekoratif çizgi, kapakta amaçsız renk bloğu, şablon kartlar.
4. **Register karışıklığı:** Hangi marka kimliği kullanılacağı (iş mi misyon mu) belirsizdi.
5. **Glyph körlüğü:** ₺ sembolü Comfortaa'da yok — kutu olarak çıkıyor (sonradan yakalandı).

**Kök ders:** Görsel kalite "renk doğru, Türkçe temiz" yüzeyselliğiyle değil; tipografi sadakati + editorial ruh + slop yokluğu + glyph bütünlüğü ile ölçülür.

---

## 1 · REGISTER SEÇİMİ (her işin ilk kararı)

Marka kiti (marka-kiti.md §"İKİ REGISTER") iki görsel kimlik tanımlar. **Üretime başlamadan önce hangisinde olduğunu belirle.**

| Register | Ne zaman | Font | Palet | pdf-motoru tema |
|---|---|---|---|---|
| **Steps On Clouds — Misyon/Marka** | SOC marka sunumları, denetim raporu, kampanya, sosyal, topluluk, ampüte içerik | Bebas Neue (başlık) + Comfortaa (gövde) | Phthalo Blue #040D7E · Sky Blue #72CBDF · White · Midnight #101010 · Mist #EAF6EB | `"tema": "soc-mavi"` |
| **Ayhan Erden — İş** | Teklif, sözleşme, kurumsal belge, müşteri markası öne çıkan iş | Didot (başlık) + Avenir Next (gövde) | Siyah #1A1C22 · Altın #A8814B · Krem #F4F1EA | `"tema": "ayhan-premium"` (varsayılan) |

**Karar verildi (5 Haz, Ayhan):** Marka Bulutu OS müşteri sunum/raporları → **`soc-mavi`** register.
**Müşteri markası için iş:** O müşterinin kendi marka kimliği esastır (context'inden); SOC imzası geride durur.

---

## 2 · FORMAT HİYERARŞİSİ — Hangi araçla üretilir

**Karar verildi (5 Haz, Ayhan):** Premium belgeler **PDF** olarak üretilir, PPTX değil.

| Çıktı türü | Araç | Neden |
|---|---|---|
| **Denetim raporu, teklif, strateji belgesi, brand book** | **`sablonlar/pdf-motoru.py`** (ZORUNLU) | Editorial dizgi, tam tasarım kontrolü, marka fontu, Türkçe-doğru. Slop riski düşük. |
| Canlı sunum (yüz yüze/ekran) | PDF (tam ekran) veya gerçekten gerekiyorsa PPTX | PPTX jenerik "PowerPoint" hissine kayar — son çare. |
| Sosyal görsel, kampanya | Canva (marka kiti) / AI brief + gerçek prodüksiyon | Görsel parmak izi briefiyle. |

**KURAL:** Sıfırdan PPTX/Python-slayt üretme dürtüsüne DİREN. Önce `pdf-motoru.py` kullanılabilir mi diye sor. Motor yetmiyorsa motoru geliştir — jenerik bir slayt üretme.

---

## 3 · TİPOGRAFİ — Pazarlık Konusu Değil

- **Marka fontu ZORUNLU.** soc-mavi: Bebas Neue + Comfortaa. ayhan-premium: Didot + Avenir Next. Arial/Calibri/Helvetica yalnızca **Türkçe-güvenli yedek** (font yüklenemezse) — asla birincil seçim değil.
- Fontlar repo'da: `assets/fonts/` (BebasNeue-Regular, Comfortaa-Regular, Comfortaa-Bold). pdf-motoru bunları otomatik yükler.
- **Hiyerarşi:** başlık çok büyük (Bebas kompakt → 40pt+), gövde 9pt Comfortaa (geniş font), net ölçek farkı. Estetik müfredatı Disiplin 2.
- **Bebas all-caps** display fonttur — uzun gövde metni İÇİN KULLANMA, sadece başlık.

---

## 4 · EDİTORIAL RUH (görsel parmak izi → tasarıma)

Ayhan'ın imzası (fox-gorsel-parmak-izi.md): sıcak, atmosferik, editorial/anlatısal, güçlü kompozisyon, negatif alan ustalığı, sinematik. Belge tasarımına çevirisi:

- **Cömert boşluk.** Negatif alan korkutmuyor, nefes aldırıyor. Her santimi doldurma. (Estetik müfredatı: "boşluk = nefes".)
- **Güçlü hiyerarşi.** Göz nereye gitsin? Büyük başlık → alt başlık → gövde net ayrışsın. Boyut + renk + boşlukla yönlendir.
- **Az ama anlamlı vurgu.** Bir sayfada bir odak. Her şey vurguluysa hiçbir şey vurgulu değil.
- **Tutarlılık anlatıya çevirir.** Aynı aksan, aynı ızgara, aynı ritim — izole sayfaları bir bütüne bağlar (art direction ilkesi).
- **Sıcaklık/karakter.** Steril değil. soc-mavi'de Mist yüzeyler + Sky aksan canlılık verir; ayhan-premium'da krem + altın sıcaklık.

---

## 5 · AI-SLOP KARA LİSTESİ (ASLA)

Bunlar "yapay zekâ üretimi" parmak izidir — müşteriye gitmez:

- ❌ **Her başlığın altına/yanına dekoratif çizgi.** (PPTX rehberi bile: *"NEVER use accent lines under titles."*) Aksan amaçlı ve tutarlı olmalı (örn. bölüm başlığında tek ince Sky çizgi) — her yere serpilmiş süs değil.
- ❌ **Amaçsız dekoratif renk blokları/şeritler.** Kapağa "dolu dursun" diye konan yarım bloklar.
- ❌ **Full-width renkli header/footer barları** (kullanıcı açıkça istemedikçe).
- ❌ **Şablon hissi veren tekdüze kart dizilimleri** — her slayt aynı kalıp.
- ❌ **Gradient abuse, gereksiz gölge, 3D efekt, clipart.**
- ❌ **Merkeze yığılmış metin blokları** (gövde metni sola hizalı; yalnızca başlık ortalanır).
- ❌ **Düşük kontrast** (açık zeminde açık metin, koyu zeminde koyu ikon).
- ❌ **Stok/jenerik kurumsal estetik** — "herhangi bir şirkete uyar" görünüm.

---

## 6 · GLYPH & TÜRKÇE BÜTÜNLÜĞÜ

- **Türkçe karakterler:** İ ı ş ç ğ ö ü Ş Ğ İ Ö Ç Ü — her fontta doğrulanmış olmalı. (Bebas/Comfortaa/Arial: ✓ doğrulandı 5 Haz.)
- **₺ TUZAĞI:** Comfortaa Türk Lirası simgesini (₺ U+20BA) TAŞIMAZ → kutu çıkar. Para yazımında **"TL"** kullan (pdf-motoru otomatik ₺→TL çevirir; yine de TL yaz). Aynı dikkat: nadir semboller (™, ℠, özel ok/işaretler) font'ta var mı?
- **Kural:** Standart dışı her karakter (para simgesi, özel işaret, emoji) için "bu fontta render oluyor mu?" sorusu — render-and-review'de kontrol et.

---

## 7 · ZORUNLU GÖRSEL ÖZ-DENETİM (her teslimde)

Hiçbir görsel çıktı bu checklist'ten geçmeden teslim edilmez. İçerik Ajanı kendi uygular; Keşif/Denetmen/Fox onayda tekrar sorar.

**A. Üretim ÖNCESİ:**
- [ ] Register belirlendi mi? (soc-mavi / ayhan-premium / müşteri kimliği)
- [ ] Doğru araç mı? (premium belge → pdf-motoru; PPTX değil)
- [ ] Marka fontu kullanılıyor mu?

**B. Teslim ÖNCESİ — RENDER-AND-REVIEW (zorunlu):**
- [ ] Çıktıyı GÖRSELE çevirdim mi? (PDF → `qlmanage -t -s 1400 -o . dosya.pdf`; çok sayfalıysa her sayfa)
- [ ] **Gözümle baktım mı?** Kod doğru ≠ görsel doğru. Mutlaka render'a bak.
- [ ] Tipografi marka fontu mu? (yedek font'a düşmüş mü?)
- [ ] Türkçe + özel karakterler (₺, İ) doğru mu, kutu var mı?
- [ ] AI-slop kara listesinden bir şey var mı? (dekoratif çizgi, amaçsız blok, şablon)
- [ ] Hiyerarşi net mi, boşluk dengeli mi, taşma/üst üste binme var mı?
- [ ] Editorial ruh var mı, yoksa jenerik mi duruyor?
- [ ] Skor/rakam/veri kaynakla tutarlı mı? (§11.5 — uydurma yok)

**C. Onur içeriğinde ek:** Acıma/ilham pornosu yok; güç/fail/gündelik gerçeklik; protez ne saklı ne fetiş; gerçek prodüksiyon (AI yüz yok).

---

## 8 · ONUR & TEMSİL (görsel) — kritik

Ampüte/engelli/sosyal etki görselinde (Anayasa §9, görsel parmak izi):
- Acıma YOK, ilham pornosu YOK. Güç, fail (özne olma), gündelik gerçeklik.
- Protez/farklılık saklanmaz da fetişleştirilmez — doğal, güçlü, var.
- Aynı editorial kalite — "engelli içeriği" diye kalite düşmez.
- **Gerçek kişi/medikal içerikte AI yüz KULLANILMAZ** — güven meselesi. Gerçek prodüksiyon.

---

## 9 · ÖĞRENME DÖNGÜSÜ

- Bu standart yaşayan. Her yeni görsel hata → buraya kural olarak eklenir (5 Haz'ın beş hatası gibi).
- Ayhan "şu kareyi beğenmedim / şu iyi" dedikçe görsel parmak izi + bu standart keskinleşir.
- pdf-motoru yeni ihtiyaçta geliştirilir (yeni bölüm tipi, yeni tema) — jenerik kaçış üretilmez.
- v2 (5 Eyl): saha çıktılarıyla kalibre; Branding Ajanı olgunlaştıkça derinleşir.

---

## 10 · KALİTE = İÇERİK AJANI PUANI

Bu standart, İçerik Ajanı'nın Puanlama Rubriği (Bölüm 6) "Görsel Yön Kalitesi" + "Teknik" kategorilerinin somut ölçütüdür. Görsel çıktı bu standardı ihlal ediyorsa → o kategoriler otomatik düşük puan → Keşif onaylamaz → Denetmen bayraklar.

---
*Görsel Üretim Standardı v1 · 5 Haziran 2026 · Fox · Zemin: marka-kiti + görsel parmak izi + estetik müfredatı + 5 Haz hata analizi · Yaşayan belge.*
