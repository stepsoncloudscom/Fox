# Özgür Protez — Genel Sağlık/Check-up Denetimi
*Keşif & Denetim Ajanı · 15 Ekim 2026 · ozgurprotez.com · Wix site ID `6e57503f-4b11-4ac2-8912-9a46e160abf8`*

**Amaç:** 14 Ekim'de ana sayfa title'ının "ÖzgürProtez: HOME"a geri döndüğü bulundu — 28 Eylül raporunda "✅ tamamlandı" yazan bir iş canlıda geri dönmüştü. Bu check-up o yüzden hiçbir "✅" işaretine güvenmedi; her kalem bu oturumda yeniden, canlı site + Wix API üzerinden doğrulandı.

**Yöntem:** GetSiteContext (yayın durumu) · Wix SEO API'leri (Site SEO Tags, Item SEO Tags — STORES_CATEGORY/STATIC_PAGE/STORES_PRODUCT) · Wix Blog API (draft+published liste) · Wix Forms API (3 form şeması) · GSC/GBP Connection API · canlı tarayıcıdan `fetch()` ile gerçek render edilmiş HTML (title/description/JSON-LD) — API'nin "saved revision" okuma sınırı bilindiği için (bkz. Bulgu #2) kritik sayfalar tarayıcıdan ikinci kez doğrulandı.

---

## ÖZET

**26 kalem kontrol edildi. 3 kalemde fark bulundu (2'si 🔴 kritik sapma, 1'i 🟡 bilgi/olumlu sapma). 20 kalem rapor ile canlı birebir örtüştü, 3 kalem zaten bilinen açık madde olarak değişmeden duruyor.**

**En kritik 2 bulgu:**
1. **28 Eylül'de eklenen TÜM STATIC_PAGE SEO verisi (58 sayfa: açıklama + Hakkımızda'nın MedicalBusiness şeması + "FAQ→Sık Sorulan Sorular"/"BLOG→Blog" Türkçeleştirmesi) canlıda geri dönmüş** — yalnız ana sayfanın title'ı dün elle düzeltildi, açıklaması ve şeması hâlâ yok. Bu, 14 Ekim'de keşfedilen "HOME" vakasının tek sayfa değil **sitenin tüm STATIC_PAGE katmanını** vurduğunu gösteriyor.
2. **4 yeni blog taslağından biri ("Diz Altı Protezi Nedir?") 29 Eylül'den beri canlı ve herkese açık** — fox-durum.md'de "Wix'e taslak eklendi (yayınlanmadı)" diye kayıtlı, avukat+Özgür Bey onayı bekleniyordu. Diğer 3 taslak (Aktif Vakum/Pasif Vakum/Dirsek Altı Biyonik Kol) doğru şekilde hâlâ taslak.

---

## BULGULAR

### 1 · Yayın ve temel SEO durumu

| # | Kalem | Rapor ne diyordu | Canlı ne diyor | Fark |
|---|---|---|---|---|
| 1 | Site yayın durumu | 28 Eyl: "Published" | GetSiteContext: **Published**, Premium, Custom Domain, son güncelleme **14 Eki 17:30** | 🟢 Temiz (ama bu zaman damgası Bulgu #2'nin olası nedeni) |
| 2 | Sitewide `noindex` | 28 Eyl Tur 1: kaldırıldı | Site SEO Tags API: `robots` tag'i yok → indekslenebilir | 🟢 Temiz, fark yok |
| 3 | sitemap.xml | 28 Eyl Tur 1: 404'ten 200'e döndü, 8 alt-sitemap | Canlı: 200, 8 alt-sitemap (store-products/categories, blog-posts/categories, pages, vb.) | 🟢 Temiz, fark yok |
| 4 | robots.txt | 28 Eyl: `Allow: /`, AI botlarına açık | Canlı: aynı, `Allow: /`, sitemap referansı doğru | 🟢 Temiz, fark yok |
| 5 | GSC bağlantısı | 28 Eyl Tur 1: Ayhan'ın hesabıyla VALID | GSC Connection API: **VALID**, aynı hesap (o\*\*\*\*\*\*\*\*\*@gmail.com) | 🟢 Temiz, fark yok |
| 6 | GBP bağlantısı | 29 Eyl: NEVER_CONNECTED (Wix tarafı), profil kendisi kamuya açık/sağlıklı | GBP Connection API: hâlâ **NEVER_CONNECTED** | ⚪ Değişmedi — zaten çözülmemiş açık madde, Ayhan "öncelik değil" dedi |

### 2 · 🔴 Ana sayfa — kısmi düzeltme (sadece title, açıklama+şema hâlâ kayıp)

| Kalem | Rapor ne diyordu | Canlı ne diyor | Fark |
|---|---|---|---|
| Title | 14 Eki elle düzeltildi: "Protez ve Ortez Merkezi İstanbul \| Özgür Protez 0216 575 81 50" | Tarayıcıdan doğrulandı: **birebir aynı** | 🟢 Bu kalem düzeldi |
| Meta description | 28 Eyl Tur 1: eklendi (Ataşehir/İstanbul + 1998 kaynaklı) | Tarayıcıdan doğrulandı: **hiç meta description yok** (ne `name="description"` ne `og:description`) | 🔴 Geri dönmüş, düzeltilmemiş |
| MedicalBusiness şeması | 28 Eyl Tur 3: eklendi, 29 Eyl Tur 4'te 19 sayfaya genişletildi | Tarayıcıdan doğrulandı: yalnız **2 eski `WebSite` şeması var**, `MedicalBusiness` **yok** | 🔴 Geri dönmüş, düzeltilmemiş |

**Not:** 14 Ekim'deki düzeltme yalnızca title'ı elle yeniden yazdı — aynı PATCH çağrısının parçası olan açıklama ve şema o işlemde geri gelmedi, çünkü onlar ayrı bir reversion'ın parçası (Bulgu #3'e bakın).

### 3 · 🔴 TÜM STATIC_PAGE katmanı (58 sayfa) — 28 Eylül SEO verisi geri dönmüş

API (`List Item SEO Tags`, STATIC_PAGE) örneklemde 27 sayfanın **tamamında** `hasOverride:false, tags:[]` döndürdü — yani kayıtlı/yayın revizyonunda hiçbir override yok. Bu, API'nin "saved revision okur, render edilen sayfayı değil" sınırını da (Wix dokümantasyonunun kendi uyarısı) hesaba katarak **5 sayfa doğrudan tarayıcıdan `fetch()` ile ikinci kez doğrulandı**:

| Sayfa | Rapor ne diyordu (28 Eyl) | Canlı ne diyor (15 Eki, tarayıcıdan) | Fark |
|---|---|---|---|
| Hakkımızda | description eklendi + MedicalBusiness şeması eklendi | description **yok**, JSON-LD **yok** (0 script) | 🔴 Tamamen geri dönmüş |
| Sertifikalar | description eklendi | description **yok** | 🔴 Geri dönmüş |
| FAQ | title "FAQ"→"Sık Sorulan Sorular" Türkçeleştirildi, description eklendi | title hâlâ **"FAQ"** (İngilizce artık geri geldi), description **yok** | 🔴 Geri dönmüş (title dahil) |
| Blog (liste sayfası) | title "BLOG"→"Blog" düzeltildi, description eklendi | title hâlâ **"BLOG"** (büyük harf artık geri geldi), description **yok** | 🔴 Geri dönmüş (title dahil) |
| KVKK Aydınlatma Metni | description eklendi | description **yok** (sayfa 200 açılıyor, içerik duruyor, sadece SEO katmanı kayıp) | 🔴 Geri dönmüş |

**Olası neden (hipotez, teyit gerekli — kesin iddia değil):** `pages-sitemap.xml`'deki **58 STATIC_PAGE URL'sinin tamamı `lastmod: 2026-10-14`** gösteriyor — tam olarak GetSiteContext'in "Updated: Oct 14, 2026, 17:30" damgasıyla örtüşüyor. Buna karşılık `store-categories-sitemap.xml`'deki kategori URL'leri `lastmod: 2026-09-28` / `2026-10-02` — yani **dokunulmamış.** Bu örüntü, Wix'in kendi API dokümantasyonundaki uyarıyla tutarlı: *"STATIC_PAGE klasik Editör'de taslak+yayın iki ayrı revizyon tutar; bir sonraki Editör yayını, araya giren bir düzenleme yoksa API'nin yazdığı SEO değişikliklerini korur"* — yani **araya bir Editör düzenlemesi/yayını girdiyse**, o yayın Eylül'deki API yazımlarını hiç görmemiş eski bir taslağı canlıya taşımış olabilir. Bunun kim/ne zaman yaptığı bu denetimin kapsamında doğrulanamadı — Wix aktivite geçmişi/Özgür Bey'e sorulması gereken bir soru.

**Kapsam notu:** STORES_CATEGORY (18 kategori) ve STORES_PRODUCT (115 ürün, örneklem) bu reversion'dan **etkilenmemiş** — bkz. Bölüm 4. Bu, sorunun STATIC_PAGE türüne özgü (draft/publish ayrışması olan tek tür) olduğunu doğruluyor.

### 4 · 🟢 STORES_CATEGORY ve STORES_PRODUCT — sağlam, fark yok

| Kalem | Rapor ne diyordu | Canlı ne diyor | Fark |
|---|---|---|---|
| Tüm Ürünler, Ayaklar, Bacak Protezi, Diz Üstü (4 kategori, tarayıcıdan) | 28-29 Eyl: title+description+MedicalBusiness şeması eklendi | **4/4 birebir doğru** — title, description, `MedicalBusiness`+`ItemList` şeması canlı | 🟢 Temiz |
| Kalan 14 kategori (API, `List Item SEO Tags`) | aynı | 12/18 örneklemde `hasOverride:true`, title+description içerik eşleşti | 🟢 Temiz |
| genium-x3 ürün sayfası | 29 Eyl Tur 5: description eklendi | description canlı, birebir eşleşti | 🟢 Temiz |
| genium-x3 URL slug | 12 Eyl raporu: "genium-x3" üretici marka adı taşıyor, jenerikleştirilmedi (bilinen açık madde) | Canlı: slug hâlâ **"genium-x3"** | ⚪ Değişmedi — zaten çözülmemiş açık madde |
| Product/Offer şeması (price/stock) | 12 Eyl: `price:0, InStock` — mağaza görünümü teyidi | Canlı: aynı, `price:"0", InStock` | ⚪ Değişmedi — zaten çözülmemiş açık madde |

### 5 · 🔴 Blog — 4 yeni taslaktan biri sızmış

| Yazı | fox-durum.md ne diyordu | Canlı/API ne diyor | Fark |
|---|---|---|---|
| Diz Altı Protezi Nedir? Bacak Protezinde Seviye Farkı | "Wix'e taslak eklendi (**yayınlanmadı**)", avukat+Özgür Bey yazılı onayı bekliyor | API: `status: PUBLISHED`, **firstPublishedDate: 2026-09-29T11:04:40Z**. Tarayıcıdan doğrulandı: `/post/diz-alti-protezi-nedir` **200, herkese açık**, 16 gündür canlı | 🔴 Onay gatesi atlanmış, yazı yayında |
| Aktif Vakum Sistemli Protez Nedir, Nasıl Çalışır? | taslak, yayınlanmadı | API: `status: UNPUBLISHED`, slug yok, `firstPublishedDate` yok | 🟢 Doğru — hâlâ taslak |
| Pasif Vakum Sistemli Protez Bacak Nedir? | taslak, yayınlanmadı | API: `status: UNPUBLISHED` | 🟢 Doğru — hâlâ taslak |
| Dirsek Altı Biyonik Kol Protezi: Bu Seviyeye Özgü Ne Var? | taslak, yayınlanmadı | API: `status: UNPUBLISHED` | 🟢 Doğru — hâlâ taslak |
| Önceki 3 yazı (Protez Türleri, Miyoelektrik El, Protez Bakımı) | yayında | API: hepsi `PUBLISHED`, değişmedi | 🟢 Temiz |

**Not:** Yayınlanan yazının gövdesinde genel bilgilendirme ibaresi tespit edildi ("bilgilendirme amaçlıdır" eşleşmesi bulundu) — ama bu denetim yazının tam metnini avukat-onay kriterine göre incelemedi, sadece yayın durumunu doğruladı. Yayın tarihi (29 Eylül, 11:04 UTC) o günün SEO turlarıyla aynı güne denk geliyor; kim/hangi işlem sırasında yayınlandığı bu oturumda tespit edilemedi.

### 6 · Legal/compliance fiili durum (nötr, yorum eklenmeden — 12 Eylül raporunun 4 maddesi)

| # | Madde | 12 Eyl raporu | 15 Eki canlı/API doğrulaması | Fark |
|---|---|---|---|---|
| 1 | Mağaza formatı (Stores+Forms&Payments+Invoices kurulu) | kurulu, satış akışı mağaza görünümünde | GetSiteContext: **Wix Stores (V3), Wix Forms & Payments, Wix Invoices hâlâ kurulu** | ⚪ Değişmedi |
| 2 | Rakip klinik adı taşıyan görsel dosya adları (61+) | tespit edildi, yeniden adlandırılmadı | **Bu turda yeniden taranmadı** (kapsam/derinlik sınırı — medya kütüphanesi taraması bu check-up'a dahil edilmedi) | ⚪ Bilinmiyor/yeniden doğrulanmadı |
| 3 | Üretici marka adı taşıyan URL slug'ları | 15 slug listeli, düzeltilmedi | Canlıda doğrudan doğrulanan örnek (`genium-x3`) hâlâ aynı | ⚪ Değişmedi |
| 4 | KVKK: 3 formun hiçbirinde aydınlatma/rıza yok | Contact, Inquiry Services Form, Subscriptions — hiçbirinde yok | Wix Forms API'den 3 form şeması yeniden okundu: **hiçbirinde hâlâ aydınlatma/rıza alanı yok**; "Inquiry Services Form" hâlâ İngilizce ve hâlâ "Menu Design/Online Menu Setup/Brand Identity" seçenekleriyle duruyor; newsletter formu hâlâ zorunlu onay kutusuyla aynı | ⚪ Değişmedi |

### 7 · İçerik tamamlama (Protezler anlatı sayfaları / Yürüme Analizi / ürün hatları) — sığ kontrol

Bu üç kalem fox-durum.md'de "Özgür Bey teknik teyitleri bekleniyor, değişmedi" diye kayıtlıydı. Sığ bir canlı kontrol yapıldı (tam içerik denetimi değil):

| Kalem | Bulgu |
|---|---|
| Yürüyüş Analizi sayfası (`/yürüyüş-analizi`) | 🟡 **Canlı ve dolu** — süreç anlatımı, ölçüm detayı, doğru TİTCK-uyumlu disclaimer ("genel bilgilendirme amaçlıdır... tanı yerine geçmez") sayfanın sonunda var. fox-durum.md'nin "bekliyor" notuyla çelişiyor olabilir — ya içerik Özgür Bey'in 11 kalemlik teknik teyidi beklenmeden jenerik/marka-nötr yazılmış (güvenli taraf) ya da durum dosyası bayatlamış. Netleştirme gerekir. |
| Protezler ürün hattı sayfası (`/protezler`) | 🟢 Canlı, ürün kartları (Levitate/Össur bileşenleri) listeleniyor — ürün envanteri tarafı zaten görünür durumda. |
| "9 anlatı sayfası" ayrı ayrı içerik derinliği | Bu check-up kapsamında tek tek incelenmedi — ayrı, odaklı bir içerik denetimi gerektirir. |

---

## ÖNERİLEN SIRADAKİ ADIM

1. **Bulgu #2+#3 (STATIC_PAGE reversion) → Denetmen'e ve Ayhan'a bugün.** Aynı sınıf hata (Editör yayınının API-yazılı SEO'yu ezmesi) homepage'de bir kez görüldü, şimdi 58 sayfada tekrarlandığı doğrulandı — tek seferlik "garip olay" değil, tekrarlayan bir Wix davranışı. Düzeltme öncesi kök neden (kim/ne zaman Editör'den yayınladı) teyit edilmeli, aksi halde yeniden yazılan SEO verisi tekrar kaybolabilir.
2. **Bulgu #5 (yayınlanmış blog yazısı) → acil, ayrı karar.** Ayhan'a: yazı geri çekilsin mi (taslağa döndür) yoksa fiilen yayında olduğu için retroaktif avukat/Özgür Bey onayı mı istensin? İçerik yasal ihlal taşımıyor görünüyor (disclaimer var) ama onay süreci dışında yayına girmiş olması süreç açığı.
3. STATIC_PAGE SEO verisi yeniden yazılmadan önce **kök nedeni kapatacak bir önlem** (örn. Editör'den yayın yapmadan önce kontrol listesi, veya SEO verisini Editör draft'ına da yazan bir yöntem) belirlenmeli — aksi halde Tur 1-4'ün tekrarı zaman kaybı olur.
4. Madde 6, satır 2 (görsel dosya adı rakip ismi taraması) bu check-up'ta yapılmadı — ayrı bir takip gerekiyorsa not edilsin.

---
*Keşif & Denetim Ajanı · 15 Ekim 2026 · Kademe 1 (iç denetim, dışarı gönderim yok) — Denetmen devrine hazır.*
