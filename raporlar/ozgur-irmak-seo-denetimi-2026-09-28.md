# SEO Denetimi — Özgür Irmak Protez ve Ortez (ozgurprotez.com)
*Growth Ajanı · 28 Eylül 2026 · Canlı site üzerinde doğrudan tarayıcı denetimi*

**Kaynaklar:** `sablonlar/ozgur-irmak-marka-context.md` · `marka-bulutu-os-medikal-protez-bagi.md` · `raporlar/ozgur-irmak-wix-yasal-risk-analizi-2026-09-12.md` · `raporlar/ozgur-irmak-kanit-ucgeni.md` · `raporlar/ozgur-irmak-web-semasi.md` · `marka-bulutu-os-puanlama-rubrigi.md` (Bölüm 0.1, Bölüm 2 Kategori 3, Bölüm 4)
**Denetlenen yüzey:** ozgurprotez.com ana sayfa + kategori sayfaları (Bacak Protezleri, Tüm Ürünler) + 1 ürün sayfası detaylı (genium-x3, örneklem) + 4 blog yazısı + Hakkımızda + Sertifikalar + KVKK + robots.txt + sitemap.xml. Denetlenemeyen: Core Web Vitals/PageSpeed (Google PageSpeed Insights API anahtarsız erişimde 429 verdi — araç erişimi yok, uydurma sayı verilmedi), GSC/GA4 panel içi veri (hesap erişimi bu oturumda yok — yalnız sayfa kaynağından iz sürüldü), 115+ ürünün tamamı (örneklem denetimi).

---

## 🔴 ÖNCE BUNU OKU — durum ve kapsam notu

Fox'un durum dosyası (14 Eylül tarihli) siteyi "Draft, 404, YENİLENİYORUZ" olarak kaydetmişti; 12 Eylül'deki yasal risk denetimi de bunun üzerine "maruziyet şu an sıfır" demişti. Bu oturumda doğrulandı: **site artık canlı (Published)**, gerçek içerikle açılıyor, robots.txt "Allow: /" diyor. Aşağıda Bulgu #1'de detaylandırıldığı gibi **her sayfada `<meta name="robots" content="noindex">` etiketi var.**

**Denetmen düzeltmesi (28 Eylül):** `noindex` yalnızca Google'ın **indekslemesini** engeller, siteye **HTTP erişimini** kısıtlamaz — herhangi biri, hiçbir kimlik doğrulama olmadan, doğrudan URL ile siteyi zaten görüntüleyebiliyor (Denetmen bağımsız tarayıcı testiyle doğruladı). 12 Eylül yasal risk raporunun kendi eşiği de "yayın"dır, indeksleme değil: *"Yayın öncesi kapatılırsa maruziyet sıfır; yayından sonra kapatılırsa her biri fiilî ihlal."* Site şu an **Published** — yayın eşiği geçilmiş durumda. Bu yüzden **12 Eylül'ün 4 DUR maddesinin (mağaza formatı, rakip klinik adı sızıntısı, üretici marka adı sızıntısı, KVKK aydınlatma/rıza eksikliği) tümü, noindex'ten bağımsız olarak şu an fiilen kamuya açık ve muhtemelen ihlal aşamasında** — "korunuyor" değil. Bu SEO denetimi teknik/on-page bulguları raporlar; DUR bulguların yasal risk yeniden değerlendirmesi Denetmen'in işi — burada yalnızca SEO merceğinden yeni ve teyit edici bulgular not edilir. **Ayrıca bilinmiyor:** siteyi kim, ne zaman Draft'tan Published'a aldı — maruziyetin başlangıç tarihi belirsiz.

---

## METODOLOJİ NOTU (§0.1 uyumu)

Bu denetimde **tek bir bileşik sayısal SEO skoru verilmiyor.** Gerekçe: rubriğin Kategori 3 (Görünürlük/SEO) bantları teknik sağlık skoru (Semrush/TrackSEO), PageSpeed (Lighthouse) ve organik trafik gibi **Tip A** araçlara dayanıyor — bu oturumda hiçbirine erişim yok (GSC/GA4 zaten bağlı değil — `ozgur-irmak-kanit-ucgeni.md`'de tescilli; PageSpeed API rate-limit verdi). Tek doğrulanmış **Tip A gerçek** (ölçülmüş, tahmin değil): **indeksleme durumu = noindex, sitewide.** Bu bulgu HTTP/HTML kaynağından doğrudan okundu, varsayım değil.

Geri kalan her şey **Tip B** (gözlem/altyapı): Güçlü / Orta / Zayıf / Kritik açık olarak, somut kanıtla birlikte raporlanıyor — sayısal puana çevrilmiyor.

---

## 1 · TEKNİK SEO

### 🔴 Bulgu — İndeksleme tamamen kapalı (Tip A, doğrulanmış)
Denetlenen **her** sayfa tipinde (ana sayfa, kategori, ürün, blog listesi, blog yazısı, Hakkımızda, Sertifikalar, KVKK) HTML kaynağında:
```html
<meta name="robots" content="noindex">
```
Bu, robots.txt'nin `Allow: /` izninin **üzerine geçer** — Google bir sayfayı tarayabilir ama noindex gördüğü an SERP'ten çıkarır/hiç sokmaz. Muhtemel neden: Wix'in "site arama motorlarında görünsün mü" global anahtarı (Site Ayarları → SEO Araçları) henüz açılmamış — Draft/geliştirme döneminden kalma varsayılan. **Sonuç: site bugün gerçek içerikle canlı olsa da Google'da sıfır görünürlüğe sahip; bu, teknik SEO'nun önündeki tek ve en büyük engel.** Diğer tüm bulgular bu kapatılana kadar teorik kalır.

### 🔴 Bulgu — sitemap.xml 404 (Tip A, doğrulanmış — Ayhan'ın ilk gözlemiyle örtüşüyor)
`https://www.ozgurprotez.com/sitemap.xml` → 404. robots.txt bu URL'i sitemap olarak referans alıyor (`Sitemap: https://www.ozgurprotez.com/sitemap.xml`) ama dosya yok. Noindex kapatılsa bile bu, Google'ın yeni sayfaları keşfetme hızını yavaşlatır. Genelde Wix'te otomatik üretilir — bunun 404 vermesi, sitenin arama motoru entegrasyonu tarafında da yarım kaldığına işaret. (Wix SEO panelinden "sitemap'i etkinleştir" kontrolü gerekir.)

### Diğer teknik gözlemler (Tip B)
| Alan | Durum | Kanıt |
|---|---|---|
| HTTPS | ✅ Temiz | `https://www.ozgurprotez.com`, geçerli sertifika, tarayıcı uyarısı yok |
| Kanonik URL'ler | ✅ Temiz | Her denetlenen sayfada `<link rel="canonical">` kendine referans veriyor, tek host (`www`) tutarlı |
| Mobil uyum | ✅ Temiz | 375px genişlikte render edildi — düzen bozulmuyor, metin okunur, CTA erişilebilir |
| Google Search Console doğrulaması | ⚠️ İz yok | `<meta name="google-site-verification">` etiketi bulunamadı. DNS/dosya yöntemiyle bağlanmış olabilir — bu, meta etiket taramasıyla ekarte edilemez; Wix panelinden teyit gerekir. `kanit-ucgeni.md`'deki "GSC bağlı değil" bulgusuyla tutarlı. |
| GA4/GTM | ⚠️ İz yok | `dataLayer` yalnızca çerez rızası (Usercentrics) olayı taşıyor; GA4 config/measurement ID'ye rastlanmadı. Aynı tutarlılık. |
| Core Web Vitals / PageSpeed | ❌ Ölçülemedi | Google PageSpeed Insights API bu oturumda anahtarsız erişimde 429 (rate limit) döndü. Uydurma sayı verilmedi (§0.1). **Sıradaki adım:** pagespeed.web.dev üzerinden manuel ölçüm veya API anahtarıyla tekrar deneme. |
| Dil ayarı | Tip B — bilinçli, açık bayrak | `html lang="tr"`, hreflang etiketi yok. Bu bir eksik değil — `ozgur-irmak-web-semasi.md`'deki açık revizyon bayrağı gereği EN/AR/RU yayını Sağlık Hizmetlerinde Tanıtım Yönetmeliği M.8 avukat teyidine kadar donduruldu. Yani uluslararası SEO/GEO görünürlüğü (healthcare AI Overview ~%88 kapsama — sektör bağı §B.3) şu an **kasıtlı olarak sıfır**, ihmalden değil. |
| URL/slug Unicode hijyeni | 🟡 Küçük ama gerçek | `/kvkk-aydinlatma-metni̇` ve `/çerez-cookie-poli̇ti̇kasi` slug'larında son "i" harfi normal "i" değil, **birleşik nokta işaretli Unicode karakter** (`i̇` = U+0069 + U+0307, muhtemelen Wix'in Türkçe büyük "İ"yi otomatik slug'a çevirirken ürettiği bir kalıntı). Tarayıcıda çalışıyor ama link paylaşımında/elle yazımda kırılma riski taşıyor; küçük bir temizlik kalemi. |
| Site hızı (izlenim, Lighthouse değil) | Tip B, ölçülemez etiketiyle | Wix Thunderbolt altyapısı, sayfa başına 1000+ ağ isteği gözlemlendi (bloblar, tag-manager çağrıları dahil — bu ham istek sayısı, Lighthouse skoru değildir, salt bir izlenimdir). Gerçek hız verisi PageSpeed/Lighthouse olmadan iddia edilemez. |

---

## 2 · ON-PAGE SEO

### 🔴 Bulgu — `<meta name="description">` sitewide eksik (Tip A, doğrulanmış)
Denetlenen **hiçbir** sayfada (ana sayfa, kategori, ürün, blog listesi, blog yazısı) gerçek `<meta name="description">` etiketi yok. Blog yazılarında yalnızca `og:description`/`twitter:description` var (sosyal paylaşım için); diğer sayfa tiplerinde (ana sayfa, kategori, ürün) bu bile yok. **Sonuç:** Google, SERP snippet'ini otomatik sayfa içeriğinden üretecek — mesaj/CTA kontrolü elden çıkar, tıklama oranı (CTR) optimizasyonu imkânsız hale gelir. Wix'in "SEO ayarları" panelinde sayfa başına açıklama alanı büyük olasılıkla boş bırakılmış.

### 🟡 Bulgu — Title etiketleri tutarsız, bazıları İngilizce şablon artığı
| Sayfa | Title | Değerlendirme |
|---|---|---|
| Ana sayfa | `HOME \| ÖzgürProtez` | ❌ İngilizce, anahtar kelime yok, "Protez", "İstanbul", "Ortez" gibi arama niyeti taşıyan hiçbir kelime içermiyor |
| Tüm Ürünler | `All Products \| ÖzgürProtez` | ❌ İngilizce şablon artığı — sayfanın kendi H1'i Türkçe ("Tüm Ürünler") ama title İngilizce kalmış |
| Bacak Protezleri | `Bacak Protezleri \| ÖzgürProtez` | ✅ Temiz |
| Hakkımızda / Sertifikalar / Blog yazıları | Türkçe, sayfa konusunu yansıtıyor | ✅ Temiz |

Şablon/kategori tarafı İngilizce kalmış, içerik tarafı (Hakkımızda, blog, kategori sayfaları) Türkçeleştirilmiş — yarım kalmış bir yerelleştirme izlenimi veriyor.

### 🟡 Bulgu — Başlık hiyerarşisi (H1) tutarsız
- **Bacak Protezleri kategori sayfası:** H1 **hiç yok** (yalnız H2'ler: " Protez ve Ortez Uygulama Merkezi", "Bacak Protezleri", "Protez Bacağın Temel Parçaları"). Sayfanın konusunu tanımlayan tek bir H1 eksik.
- **Sertifikalar sayfası:** **3 ayrı H1** var ("Sertifikalarımız", "Yetkinlik Sertifikaları", "Sertifikalar") — bir sayfada tek H1 kuralı ihlal ediliyor.
- **Ana sayfa, Hakkımızda, ürün sayfaları, blog yazıları:** tek ve doğru H1 — temiz.

### 🟡 Bulgu — Alt text kalitesi karışık
- Ürün sayfasında (genium-x3 örneklemi) alt text'ler temiz ve Türkçe ("Mikroişlemcili Diz Eklemi (Su Geçirmez)", "Küçük resim: ...") — 14 Eylül'deki üretici-marka temizliğiyle uyumlu, üretici adı sızıntısı **bu sayfada görülmedi.**
- **Bacak Protezleri kategori sayfasında** ise görsellerin alt text'i literal AI-üretim dosya adları: *"ChatGPT Image Sep 5, 2026, 07_44_33 PM.png"* gibi 5 görsel. Bu, hem SEO açısından anlamsız (arama motoruna hiçbir bilgi taşımıyor) hem erişilebilirlik açısından değersiz (ekran okuyucu kullanıcısına dosya adını okur) hem de görsel üretim standardının (AI-slop kara listesi) atladığı bir iz — İçerik/Branding'e de bildirilmesi gereken bir bulgu.

### 🔴 Bulgu — Üretici marka adı hâlâ URL slug'ında (SEO + yasal kesişim)
`https://www.ozgurprotez.com/product-page/genium-x3` — sayfa **başlığı ve gövde metni** 14 Eylül temizliğiyle marka adından arındırılmış ("Mikroişlemcili Diz Eklemi (Su Geçirmez)"), ama **URL slug'ının kendisi hâlâ "genium-x3"** (Ottobock'un tescilli ürün adı) ve bu URL, sayfanın kendi kanonik adresi (`<link rel="canonical" href=".../genium-x3">`). 12 Eylül yasal risk denetiminin Madde 3'ünde listelenen **15** slug'dan biri hâlâ canlı (Denetmen tarafından sayıldı — rapor önceki sürümünde "14" yazıyordu, düzeltildi) — temizlik açıklama/alt-text seviyesinde yapılmış, slug seviyesinde yapılmamış. **SEO açısından ayrıca zararlı:** noindex kalkıp bu URL indekslenirse, "Genium X3" arayan kişi Ottobock'un resmî kanallarını değil bu sayfayı bulabilir — yanlış niyetli trafik + marka hakkı riski aynı anda. **Aksiyon önceliği:** noindex kaldırılmadan ÖNCE tüm marka-adı-taşıyan slug'lar (12 Eylül raporundaki 14 slug listesi) jenerikleştirilmeli, 301 ile yönlendirilmeli.

---

## 3 · YAPISAL VERİ (schema.org)

| Sayfa tipi | Bulunan şema | Değerlendirme |
|---|---|---|
| Ana sayfa | `WebSite` (2 kayıt, biri SearchAction ile) | Temel, doğru ama medikal işletme kimliği taşımıyor |
| Blog yazısı | `BlogPosting` — `author.name: "stepsonclouds"` | 🔴 Bkz. Bölüm 4 — yazar kimliği ajans hesabı, Özgür Irmak değil |
| Ürün sayfası | `Product` + `Offer` (`priceCurrency: TRY`, `price: "0"`, `availability: InStock`) | 🔴 **Kritik çapraz bulgu** — aşağıda |
| Hiçbir sayfa | `MedicalOrganization` / `MedicalBusiness` / `LocalBusiness` / `Physician` / `FAQPage` yok | ❌ Sektör bağının (§C) açıkça istediği şema seti hiç kurulmamış |

### 🔴 Çapraz bulgu — Product/Offer şeması, 12 Eylül yasal denetimin Madde 1 ve Madde 10'unu bağımsız doğruluyor
Ürün sayfasındaki JSON-LD, `"@type":"Offer","priceCurrency":"TRY","price":"0","availability":"https://schema.org/InStock"` içeriyor. Bu, sayfanın görsel arayüzünden bağımsız olarak **makine-okunur seviyede** "bu bir ₺0 fiyatlı, stokta olan satılık üründür" diyor — 12 Eylül raporunun Madde 1 (mağaza formatı) ve Madde 10 ("stokta var" beyanı ısmarlama üretimle çelişiyor) bulgularının aynısını, farklı bir katmanda (yapısal veri) teyit ediyor. **Önemi:** noindex kalkarsa bu şema Google Shopping / ürün zengin sonuçlarına aday olabilir — yani mağaza görünümü yalnız kullanıcı arayüzünde değil, arama motoruna doğrudan beyan edilen bir veri katmanında da var. Mağaza→bilgilendirme dönüşümü (yasal risk raporunun önerilen sırasının 3. maddesi) tamamlanmadan noindex kaldırılırsa, risk yalnız sayfada değil şema seviyesinde de yayılır.

### 🟡 Fırsat — MedicalOrganization/Physician şeması yok
Sektör bağı (§C) bunu açıkça istiyor: MedicalOrganization/MedicalClinic + Physician + FAQPage şeması, GEO/AI-görünürlük taktikleriyle (6 Haziran öğrenmesi — healthcare AI Overview kapsaması ~%88) doğrudan bağlantılı. Şu an sıfır. Hakkımızda sayfasındaki güçlü E-E-A-T içeriği (Özgür Irmak, 1998, Trakya Üniversitesi, öğretim görevliliği) hiçbir yapısal veriye bağlanmamış — bu içerik Google'a "bu bir gerçek uzman" sinyalini **şema seviyesinde** vermiyor, yalnızca düz metin olarak duruyor.

---

## 4 · İÇERİK / SEO FIRSATI

### ✅ Olumlu — Blog büyüyor, arama niyetiyle örtüşüyor
4 yazı canlı (12 Eylül'deki denetimden 1 fazla — 12 Eylül'de "Bacak ve Kol Protez Türleri" eklenmiş): protez türleri, diz üstü protez, miyoelektrik el, günlük bakım. Haftalık kadans korunmuş görünüyor. Konular gerçek arama niyetiyle örtüşüyor ("diz üstü protez nedir" tipi bilgi arayışı) — search-intent uyumu (rubrik notu: keyword density değil, intent esas) bu tarafta güçlü.

### 🔴 Bulgu — YMYL/E-E-A-T: blog yazarı gerçek uzmanla bağlı değil
Her blog yazısının `BlogPosting` şemasında `author.name: "stepsonclouds"` (ajans hesabı) yazıyor — Özgür Irmak değil. Hakkımızda sayfasında gerçek, doğrulanabilir bir uzman kimliği var ("Kurucumuz Sayın Özgür Irmak; Trakya Üniversitesi Protez ve Ortez Bölümü 1998 mezunu... çeşitli üniversitelerde öğretim görevlisi") ama bu kimlik **blog içeriğine hiçbir şekilde bağlanmamış.** Sektör bağı §C bunu doğrudan uyarıyor: *"Anonim 'blog yazısı' bu sektörde işe yaramaz."* Bu, tespit edilen en yüksek kaldıraçlı, en ucuz düzeltilebilir E-E-A-T açığı: Wix Blog yazar profilini "stepsonclouds"tan "Özgür Irmak" (veya görünür bir "Uzman Görüşü: Özgür Irmak" künyesi) olarak değiştirmek, hem şemaya hem görünür metne yansır.

### 🟡 Not — Tıbbi sorumluluk reddi ve teyitsiz iddia (yasal denetimle çakışan, SEO/güven açısından da geçerli)
12 Eylül raporunun Madde 6'sı hâlâ canlı: "Diz Üstü Protezlere Detaylı Bakış" yazısı bu oturumda tekrar okundu, sonunda tıbbi sorumluluk reddi **hâlâ yok**, ve *"merkezimizde kullanılan biyomekanik analiz ve ayarlama sistemi"* ifadesi hâlâ teyitsiz iddia olarak duruyor. Bu SEO denetiminin kapsamı değil (yasal/Denetmen konusu) ama not ediliyor çünkü E-E-A-T'nin "Trustworthiness" bileşenini (Google'ın en kritik gördüğü E-E-A-T alt bileşeni) doğrudan etkiliyor — güven sinyali zayıfladıkça YMYL içeriğin sıralanma potansiyeli de zayıflar.

### 🟡 Fırsat — Ürün kataloğu SEO derinliği ölçülmedi
~115-120 ürünlük (örneklem: 2 sayfa/20 sayfa) geniş bir katalog var ama örneklem dışı ürünlerin başlık/açıklama/alt-text kalitesi bu denetimde taranmadı (kapsam dışı — tam katalog taraması ayrı bir iş kalemi). 12 Eylül raporunun Madde 9'u (tekrarlı ürün adları, şablon artığı slug'lar: `camo-backpack`, `i-m-a-product-11`) hâlâ geçerli olabilir; bu SEO denetimi onu yeniden doğrulamadı, sadece hatırlatıyor.

---

## 5 · ÇOK DİLLİLİK VE ULUSLARARASI GÖRÜNÜRLÜK

Yalnız `tr`. Bu bir **bilinçli bekletme**, ihmal değil: `ozgur-irmak-web-semasi.md`'deki açık revizyon bayrağı, EN/AR/RU yayınını Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Yönetmeliği M.8'in avukat teyidine bağlamış durumda. SEO açısından somut sonucu: sektör bağının vurguladığı GEO/AI-görünürlük fırsatı (healthcare AI Overview kapsaması ~%88, "prosthetic clinic Istanbul" tipi sorgular) şu an **erişilemiyor** — bu, döviz/yurtdışı hasta hedefinin (Kuzey Yıldızı #3) SEO ayağının fiilen donmuş olduğu anlamına geliyor. Avukat kapısı açılınca bu bölüm yeniden değerlendirilmeli; şimdilik "eksik" değil "bekliyor" olarak işaretleniyor.

---

## BÜYÜME HAZIRLIK SKORU — yalnızca SEO Uygulama Kalitesi dilimi

Bu teslim tam bir Growth denetimi değil, salt bir SEO incelemesi — bu yüzden rubriğin Bölüm 4 (Growth Ajanı Rubriği) 5 kategorisinden yalnızca **SEO Uygulama Kalitesi (%25 ağırlık)**'na dair kanıt üretildi. Dönüşüm Optimizasyonu, Email & Lead, Kanal Stratejisi, Ölçüm & Tracking bu denetimin kapsamı dışında — **bileşik bir Growth skoru verilmiyor** (§0.1: eksik kategoriler skora girmez).

**SEO Uygulama Kalitesi — sayısal skor verilmiyor (§0.1).** Gerekçe: kategori tanımı "teknik+içerik+intent uyumu, benchmark-bağlı hedef" gerçek trafik/sıralama verisine (Tip A) dayanıyor; bu veri yok (GSC bağlı değil). Onun yerine niteliksel bant:

**Bant: Kritik açık (rubrik Kategori 3'ün 0-39 F tanımına yakın ama birebir değil)** — gerekçe: *"Site indekslenmiyor"* kriteri harfiyen karşılanıyor (noindex sitewide), ama *"yapısal SEO yok, içerik yok"* kriteri karşılanmıyor — tam tersine, canonical/schema/title/H1 altyapısının önemli bir kısmı kurulu ve 4 yazılık büyüyen bir içerik tabanı var. **Bu yüzden site "sıfırdan inşa" durumunda değil, "iyi bir temel + tek kritik anahtarın kilitli olması" durumunda.** Noindex kalkar kalkmaz (ve slug/şema temizliği yapılırsa) bant hızla C/B bandına sıçrayabilir — bu nadir görülen, ucuza çözülebilir bir konum.

---

## SONUÇ — TEMİZ / DİKKAT / DUR

**Denetmen düzeltmesi:** Aşağıdaki liste yalnız *SEO merceğinden* "noindex kaldırma ön koşulları"nı kapsar — 12 Eylül yasal risk raporunun **4 DUR maddesinin tamamı** (mağaza formatı, rakip klinik adı sızıntısı [61+ görsel, bu SEO denetiminde teyit edilmedi], üretici marka slug'ları, KVKK aydınlatma/rıza) noindex'ten **bağımsız olarak** ve **indeksleme durumuna bakılmaksızın** şu an fiilen açık/kamuya erişilebilir durumda (bkz. "ÖNCE BUNU OKU"). Bu SEO sonuç listesi o 4 maddenin yerine geçmez, onları tekrarlamaz — 12 Eylül raporu kendi başına, acil, ayrı takip edilmeli.

### 🔴 DUR — noindex kaldırılmadan önce mutlaka kapanmalı (SEO'ya özgü ön koşullar)
1. **Sitewide `noindex` meta etiketi** — tek başına tüm SEO çabasını sıfırlıyor. Wix SEO panelinden kaldırılmalı — ama **yalnızca** aşağıdaki 2 ve 3 kapandıktan **ve** 12 Eylül'ün 4 DUR maddesi (yukarı bkz.) çözüldükten sonra.
2. **Üretici marka adı taşıyan URL slug'ları** (`genium-x3` doğrulandı, 12 Eylül raporunda 15 slug listeli) — jenerikleştirilip 301 ile yönlendirilmeden noindex kaldırılırsa hem SEO hem marka hakkı riski birlikte yayına çıkar (görünürlüğü artırarak mevcut riski büyütür).
3. **Product/Offer şeması** (`price: 0`, `InStock`) — mağaza→bilgilendirme mimarisi dönüşümü (12 Eylül raporunun önerilen sırasının 3. maddesi) tamamlanmadan bu şema canlı kalırsa, noindex kalktığında Google'a doğrudan "satılık ürün" beyanı gider.

### 🟡 DİKKAT — indeksleme açıldıktan hemen sonra önceliklendirilmeli
4. **`<meta name="description">` sitewide eksik** — SERP mesaj kontrolü elde yok; Wix SEO panelinden sayfa başına açıklama girilmeli (öncelik: ana sayfa, kategori sayfaları, en çok trafik alması beklenen 4 blog yazısı).
5. **Blog yazarı "stepsonclouds" — "Özgür Irmak" değil** — en ucuz, en yüksek kaldıraçlı E-E-A-T düzeltmesi. Wix Blog yazar profili adı + görünür künye değişimi tek oturumluk iş.

### ✅ TEMİZ — sorun çıkmadı
- HTTPS, kanonik URL tutarlılığı, mobil render, ürün sayfası alt-text/marka temizliği (örneklem), blog yayın kadansı ve arama-niyeti uyumu.

---

## ÖNERİLEN SIRADAKİ ADIM

1. **Bu rapor Denetmen'e devredilir** — özellikle DUR bulgular (2 ve 3), 12 Eylül yasal risk raporuyla çapraz okunmalı; ikisi birlikte "noindex kaldırma" kararının ön koşul listesini oluşturur.
2. Denetmen onayından sonra Ayhan'a **tek karar sorusu** net: *"Site şu an noindex sayesinde korunuyor — mağaza dönüşümü + slug temizliği + KVKK formları tamamlanmadan noindex kaldırılmayacak. Bu sırayı onaylıyor musun?"*
3. Teknik SEO kalemleri (sitemap.xml, meta description, GSC bağlantısı, MedicalOrganization/Physician şeması) noindex kaldırma kararından **bağımsız** olarak şimdiden hazırlanabilir — hazır beklerler, noindex kalkar kalkmaz devreye girerler. Bu, Growth'un bir sonraki iş kalemi.
4. PageSpeed/Core Web Vitals ölçümü — API anahtarı ile veya pagespeed.web.dev üzerinden manuel — ayrı, küçük bir takip görevi.

---
*Growth Ajanı · 28 Eylül 2026 · Kademe 1 (araştırma-özet, iç rapor) — dışarı gönderim yok. Denetmen devrine hazır.*
