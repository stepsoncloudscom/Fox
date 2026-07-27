# Brand Book Yapısal Şablonu
*Branding'in müşteriye sunduğu marka kılavuzunun sabit yapısı + tamlık kapısı. **Kilitli Kimlik Kaydı'ndan (KKK) TÜRETİLİR** — kaynak değil, sunum. Kilitli değerler KKK'dan gelir, şablon default'undan değil (Özgür Irmak kök sebep).*

---

## ÜRETİM KURALI
- **Önce KKK.** `sablonlar/kilitli-kimlik-kaydi-sablonu.md` doldurulmadan brand book üretilmez. Her renk/font/ses değeri **KKK'dan birebir** kopyalanır.
- **🅿️ PARK öğe → "üretim aşamasında" tut, doldurma** (park logo sayfası boş kalır, placeholder konmaz).
- **🅰️ ADAY öğe → "öneri" etiketiyle sun**, kilitliymiş gibi gösterme.
- **Format:** `sablonlar/pdf-motoru.py` (premium belge — PPTX değil). Register müşteriye göre. Görsel üretim → `marka-bulutu-os-gorsel-uretim-standardi.md`.

---

## SABİT BÖLÜM YAPISI (her bölümde tamlık kontrolü)

**0 · Kapak** — marka adı, "Marka Kimliği / Brand Guidelines", tarih, versiyon. ☐ placeholder künye YOK (sahte isim/site/telefon).

**1 · Marka Özü** — konumlandırma cümlesi (Strateji'den), vizyon/misyon, değerler, kişilik + arketip. ☐ vizyon/misyon BOŞ değil (lorem ipsum yasağı).

**2 · Sözel Kimlik** — marka sesi, ton, **kilitli ses kuralları (KKK §3 birebir)**, kelime yap/yapma, copywriting kuralları (başlık/CTA/açıklama kalıpları, yasak kelimeler). ☐ kişilik sıfatları KKK ile birebir (drift yok).

**3 · Görsel Kimlik**
- Logo: kullanım, temiz alan, min boyut, yanlış kullanım. ☐ park logo "üretim aşamasında".
- Renk: her renk **hex + kullanım rolü (KKK §1 birebir)**. ☐ şablon default'u DEĞİL.
- Tipografi: font + **lisans (KKK §2)** + hiyerarşi. ☐ drift font yok.
- Görsel dil / fotoğraf yönü: atmosfer, örnekler. ☐ üçüncü taraf telifli görsel yok (Össur tipi).

**4 · Ayırt Edici Varlıklar** — *[#3 geliştirmesinde açılacak — şimdilik başlık placeholder; boş bırakılırsa "sonraki fazda" not düş, lorem koyma]*

**5 · Uygulama Örnekleri** — doğru/yanlış kullanım (sosyal, kartvizit, ambalaj vb.). ☐ gerçek örnek, RIMBERIO/Acme yok.

**6 · Onur & Temsil** — insan-merkezli markada: acıma yok, ilham pornosu yok; güç/fail/gündelik. AI yüz yasağı (gerçek prodüksiyon).

**7 · Legal & Usage Rights** — logo/varlık kullanım izinleri, IP sahipliği/devir (sözleşmeyle senkron), üçüncü taraf kullanım koşulları, font lisansları. ☐ sözleşme IP maddesiyle ÇELİŞMİYOR.

**8 · Kilitli Kimlik Kaydı özeti** — KKK'nın referansı (iç; müşteri versiyonunda özet renk/font/ses tablosu).

---

## TAMLIK KAPISI (teslimden önce — Branding çalıştırır, geçmeden teslim YOK)
`fox-oz-denetim-ve-nobet.md` Bölüm 4 Branding görsel-kalite kapısının genişlemesi:

1. ☐ **Tüm bölümler dolu** — hiçbir bölüm lorem ipsum / "[devam]" / boş değil (park hariç, o "üretim aşamasında").
2. ☐ **Placeholder taraması** — RIMBERIO / Acme / John Doe / reallygreatsite.com / +123-456-7890 / sahte künye YOK.
3. ☐ **KKK birebir uyumu** — her renk (hex) / font / ses kuralı / kişilik sıfatı Kilitli Kimlik Kaydı ile birebir. Şablon default'u sızmadı.
4. ☐ **Statü doğruluğu** — 🅿️ park öğeler boş/"üretim aşamasında"; 🅰️ aday öğeler "öneri" etiketli; hiçbir aday kilitliymiş gibi gösterilmiyor.
5. ☐ **IP & telif** — üçüncü taraf telifli görsel yok; logo özgünlük/marka-yakınlığı taramasından geçti (#2); Legal & Usage sözleşmeyle çelişmiyor.
6. ☐ **Glyph/Türkçe** — ğ/ü/ş/ı/ö/ç doğru, İ noktalı, ₺ kutu değil.
7. ☐ **Render-and-review** — belge görsele çevrildi, gözle bakıldı; marka fontu (yedek değil), slop yok, editorial ruh (§7).

---
*Brand Book Şablonu v1 · Marka Bulutu OS · 28 Temmuz 2026 · Fox · KKK'dan türetilir; tamlık kapısı Özgür Irmak placeholder/renk/font hatalarını kapatır*
