# Özgür Irmak — Growth Turu
*Growth Ajanı · 3 Kasım 2026 · Salt-okuma + plan. Hiçbir şey yayınlanmadı, site değiştirilmedi, mail atılmadı.*

**Devralınan:** `sablonlar/ozgur-irmak-marka-context.md` · `marka-bulutu-os-medikal-protez-bagi.md` · `raporlar/ozgur-irmak-growth-gelistirme-2026-10-15.md` · `raporlar/ozgur-irmak-blog-icerik-takvimi-v4-ortez-taramasi.md` · `fox-durum.md` · `raporlar/ozgur-irmak-kanit-ucgeni.md`.
**Statü:** Denetmen'den GEÇMEDİ. Ayhan'a gitmeden önce Denetmen turu gerekli (bkz. sondaki Hazırlık Notu).
**Bilinçli dışarıda bırakılan:** 12 Eylül yasal risk maddeleri (Ayhan talimatı), hasta görseli/hasta-içerik (S11 cevapsız), GBP (Ayhan kararı "C").

---

## 0 · VERİ ÇEKİLDİ Mİ? — Evet (Tip A, kaynak: Wix GSC Site Readiness API + Item SEO Tags API + canlı sayfa SSR, 3 Kas)

Bağlantı `VALID`, site hazırlığı `READY`. Olay kaydı: hesap bağlama, doğrulama, property ekleme, sitemap gönderimi ve indeksleme talebi hepsi 28 Eylül'de yapılmış, sonra tekrarlanmamış. Apps listesinde **Google Analytics hâlâ yok**; GA4 bağlanmamış, bugün tekrar doğrulandı.

### 0.1 Toplam arama performansı

| Pencere | Tıklama | Gösterim | CTR | Ort. pozisyon |
|---|---|---|---|---|
| 15 Eyl–12 Eki (28 gün, 15 Eki referansı — bugün yeniden çekildi, aynı çıktı) | 69 | 2.078 | %3,3 | 5,28 |
| **6 Eki–2 Kas (28 gün)** | **109** | **3.872** | %2,8 | 8,03 |
| 13 Eki–2 Kas (21 gün, yalnız 15 Eki sonrası) | 94 | 3.322 | %2,8 | 8,37 |

**Yöntem notu:** İki 28 günlük pencere 6–12 Ekim'de 7 gün çakışıyor; Google'ın son 1-2 günü eksik (günlük veri 31 Ekim'de bitiyor). Fark büyük olduğu için okuma değişmiyor. Tablo iki pencerenin ham karşılaştırmasıdır, bir "+%86" iddiası taşımaz.

**Günlük kırılma (Tip A):** 15 Eyl–18 Eki arası günlük gösterim 32–118 bandında. **19 Ekim'den itibaren 116–299 bandına çıkıyor** ve orada kalıyor. Bu, 15-16 Ekim'de canlıya giren blog partisinin Google'da görünmeye başladığı tarihle örtüşüyor. Nedensellik kanıtı değil, zaman örtüşmesi (Tip B yorum).

**Ortalama pozisyon neden kötüleşti (5,28 → 8,03):** Marka-dışı sorgularda yeni gösterimler alt sıralardan geliyor ve ortalamayı aşağı çekiyor; bu kapsam genişlemesine işaret ediyor. (Tip B yorum — sorgu kırılımı aşağıda bunu destekliyor.)

### 0.2 Marka vs marka-dışı (sorgu düzeyi — Google'ın anonimleştirdiği sorgular hariç)

| | 15 Eyl–12 Eki | 6 Eki–2 Kas |
|---|---|---|
| Marka sorguları (özgür/ırmak içeren) | 44 tık · 313 gösterim · 17 sorgu | 32 tık · 275 gösterim · 15 sorgu |
| Marka-dışı sorgular | **2 tık** · 618 gösterim · 101 sorgu | **2 tık** · 1.201 gösterim · 190 sorgu |

**Okuma:** Marka-dışı görünürlük (gösterim + sorgu çeşitliliği) yaklaşık iki katına çıktı; **marka-dışı tıklama yerinde saydı.** 15 Ekim'deki "yalnız marka adıyla bulunuyoruz" teşhisi yarı yarıya değişti: artık bulunuyoruz, tıklanmıyoruz. Bir sonraki darboğaz **tıklanma (snippet) ve sıralama derinliği.**
Marka tıklamasındaki düşüş (44 → 32) küçük örneklem ve anonimleştirme payı içinde; yorumlanmadı.

### 0.3 Sayfa düzeyi — 60 yazının durumu

| Sayfa grubu | 15 Eyl–12 Eki | 6 Eki–2 Kas |
|---|---|---|
| Blog yazıları (/post/) | 1 sayfa · 27 gösterim · 0 tık | **32 sayfa · 1.490 gösterim · 16 tık** |
| Ürün sayfaları | 7 sayfa · 26 gösterim · 0 tık | 46 sayfa · 512 gösterim · 18 tık |
| Ana sayfa | 1.905 gösterim · 68 tık | 1.842 gösterim · 71 tık |

**60 canlı yazının 32'si Google'da gösterim alıyor** (gösterim almak indekste olmayı gerektirir → bu 32'si için indeks Tip A). **Kalan 28'in indeks durumu bilinmiyor:** büyük kısmı 28 Ekim ve 2 Kasım partileri, yani Google'ın taraması için henüz çok erken. Bunu tahminle doldurmadım.
- Sitemap'lerin `indexedCount` alanı tüm sitemap'lerde "0" dönüyor (blog sitemap'i 60 gönderim). Bu alan gösterim alan sayfalarla çelişiyor; **güvenilir bir indeks ölçüsü olarak kullanılmadı.** Kesin cevap URL Inspection ile alınır (Google kotası harcar, sonucu sitede saklar — bu turda çalıştırılmadı, istenirse 28 yazı için yapılır).
- `member-profiles_p_first-chunk-sitemap.xml`: 1 hata. Düşük öncelik.

**En çok gösterim alıp tıklanmayan yazılar (6 Eki–2 Kas, Tip A):**

| Yazı | Gösterim | Tık | Pozisyon |
|---|---|---|---|
| Ortez Nedir, Protezden Farkı Ne? AFO ve KAFO | 348 | 0 | 8,7 |
| SGK Protez ve Ortez Bedelini Karşılıyor mu? | 141 | 3 | 6,0 |
| Protez Ayak Çeşitleri | 121 | 2 | 9,3 |
| CPM Cihazı Nedir? | 105 | 0 | 8,7 |
| Omuz Dezartikülasyonu Protezi | 77 | 0 | 7,7 |
| Protez Bacak ve Ayak Seçerken Hangi Faktörler | 66 | 0 | 16,7 |
| Protez Bacağın Bileşenleri | 64 | 0 | 6,3 |
| Karbon Fiber Protez Ayak | 57 | 0 | 7,3 |
| Diz Altı Protezi Nedir? | 55 | 0 | 37,1 |

**İlk sayfaya yakın marka-dışı sorgular:** "kafo" (63 gösterim, poz 13) · "kafo ortez" (39, poz 10,9) · "dezartikülasyon nedir" (51, poz 7,8) · "diz dezartikülasyonu" (25, poz 8,1) · "protez bacak" (120, poz 9,2) · "silikon liner diz altı protez" (20, poz 4,3). Baş terimler hâlâ uzakta: "diz altı protez" poz 52, "silikon liner" poz 30,9, "protez el" poz 38,5.

**Ülke:** 3.872 gösterimin 3.783'ü Türkiye. Uluslararası görünürlük pratikte yok (site tek dil).

### 0.4 Bu turda yeni bulunan teknik gerçekler (Tip A)

1. **60 canlı yazının yalnız 6'sında `<meta name="description">` var.** 54'ünde yalnız og/twitter açıklaması var. Google arama snippet'i için standart açıklama etiketini okur; olmadığında metni kendisi seçer. Yukarıdaki "gösterim var, tık yok" tablosunun olası nedenlerinden biri (neden-sonuç teyitsiz — Tip B).
2. **İç linkleme fiilen sıfır.** Hizmet sayfaları (/diz-altı-protezler, /ortezler, /bacak-protezleri) bloga **0** link veriyor. Örneklenen yazıda bloga-dışı linklerin tamamı menü/footer linki; metin içinde hizmet sayfasına bağlam linki yok. Takvimdeki pillar–hub mimarisi (`-blog-icerik-takvimi.md` §1) kâğıtta duruyor, canlıda kurulmamış.
3. **54 yazı "Özgür Irmak" yazar adıyla yayında** (BlogPosting `author: Person "Özgür Irmak"` + `article:author`). **Kalan 6 yazı kamuya "stepsonclouds" yazarlı:** aktif-vakum, diz-üstü-protezler, diz-altı-protezi-nedir, protez-bacak-ve-kol-bakımı, dirsek-altı-biyonik-kol, pasif-vakum. Meta description taşıyan 6 yazı tam olarak bunlar — farklı bir yayın yolundan geçmişler; bu, H1'deki API yönteminin (açıklama alanını yazmanın) çalıştığına kanıt. Physician şeması 0 yazıda. → E-E-A-T sinyali kısmen var; aynı zamanda dış onayı alınmamış ~53 yazının bir kısmı Özgür Bey'in adıyla imzalı olabilir (örtüşme kontrol edilmedi — bkz. Risk).
4. **FAQPage şeması — iki kaynak, iki sayı:** canlı SSR'da 32 yazıda görünüyor; API'de 30 yazı `isAiGenerated: true` (Wix otomatik üretimi) olarak işaretli. Örneklenen iki yazıda cevaplar ihtiyatlı ("teknik sorumlunuz belirler"). Ama bu metinler ne Denetmen'den ne avukattan geçti; şema yazının görünür metnine sadık değilse Google politikası açısından da sorun olur. Dikkat seviyesi, DUR değil.
5. **Şablon artığı sayfalar Google'da gösterim alıyor:** `/group/traveling-in-australia/discussion` (2), `/group/traveling-to-india/discussion` (6), `/members` (11), `/portfolio` (28), `/portfolio/landscape-magazine` (8) — hepsi 200 dönüyor, 6 Eki–2 Kas'ta toplam **55 gösterim**. `/portfolio`, `/members` ve `/group/*` pages-sitemap'te de listeli; iki `/group/` sayfası `robots: index` taşıyor. Bir protez-ortez merkezinin sitesinde "Traveling to India" tartışma sayfası YMYL güven sinyali açısından kötü bir iz.
   **Ayrı kalem — slug hijyeni:** `/product-page/i-m-a-product-*` (12 adet) şablon artıklarından ayrı tutuldu: bunlar gerçek ürün başlıklı sayfalar (örn. "Pasif Fonksiyonel Parmak Protezi"), yalnız slug demo adı taşıyor. Slug değişirse eski URL'den 301 yönlendirme şart; bu sayfalar gösterim alıyor.
6. **Ana sayfa SEO verisi bugün yerinde:** title, description ve MedicalBusiness şeması SSR'da görünüyor. 3. bir reversiyon ana sayfada yok. (59 sayfanın tamamını kontrol etmedim; o işi haftalık `ozgur-protez-seo-recheck` yapıyor.)
7. **STATIC_PAGE okuma notu (Tip B, Wix dokümantasyonu):** Item SEO Tags API'nin `STATIC_PAGE` okuması kaydedilmiş revizyonu döndürür, yayındakini değil. `ozgur-protez-seo-recheck` API'de eksik bulduğunda zaten canlı HTML'e bakıyor; kalan kör nokta ters yönde: **API "var" derken canlıda olmaması.** Bu bilgi "API ile yazdık, Editör yayını üstüne bastı" hipoteziyle uyumlu, kanıtı değil; teyit Özgür Bey'in cevabına bağlı.

---

## 1 · 15 EKİM PAKETİNİN DURUMU

Kanıt kaynağı: git geçmişi (15 Eki–3 Kas), fox-durum, bugünkü API okuması. "Kayıt yok", "yapılmadı" anlamına gelmez; yapıldıysa repo'ya işlenmemiş demektir.

| # | 15 Eki hamlesi | Durum (3 Kas) | Dayanak |
|---|---|---|---|
| 1 | Özgür Bey'e Editör yayın sorusu (kök neden) | 🔴 **Açık.** Gönderildiğine dair kayıt yok | Repo'da gönderim/cevap izi yok |
| 2 | Blog Hf2-5 batch (Protez Çeşitleri/Miyoelektrik/Silikon Liner/Mikroişlemcili Diz) | ✅ **Yapıldı ve aşıldı.** 4'ü de canlı, GSC'de gösterim alıyor; blog 60 yazıya çıktı | Sayfa kırılımı §0.3 |
| 3 | Author/Physician schema + künye | 🟡 **Kısmen ve kontrolsüz.** Yazar adı 54 yazıda var (Wix varsayılanı), Physician şeması yok, künye belgesi (ders verilen üniversite) hâlâ bekliyor | §0.4 madde 3 |
| 4 | H1 + STATIC_PAGE tek koordineli geçiş | 🔴 **Açık,** hâlâ Madde 1'e koşullu | — |
| 5 | GA4 bağlantısı | 🔴 **Açık.** Apps listesinde yok | GetSiteContext, 3 Kas |
| 6 | B2B hekim yönlendirme listesi | 🔴 **Açık, başlamadı** | Repo'da liste yok |
| 7 | Teknik Ortopedi Fulya aylık kontrol | ⏳ Vadesi gelmedi (~28 Kas) | — |
| 8 | GBP erişimi | ⏸ Bekliyor (Ayhan kararı, yeniden açılmadı) | — |
| 9 | IG lansman serisi | ⏸ Bekliyor (S11) | — |

**Geçersizleşen öncül:** 15 Ekim'in "içerik hacmi tek çözüm" tespiti **geçerliliğini yitirdi.** Hacim adımı atıldı ve gösterimde karşılığını verdi (§0.2-0.3). Bundan sonra eklenecek her yeni yazının getirisi, mevcut 60 yazının tıklanma ve iç bağlantı sorunu çözülmeden düşük kalır. Öncelik hacimden **verime** kaydı.

---

## 2 · ÖNÜMÜZDEKİ 30 GÜN — 5 HAMLE (öncelik sırasıyla)

Kanıt tipi: **Tip A** = bu turda ölçüldü · **Tip B** = gözlem/genel SEO bilgisi, bu sitede ölçülmedi. Sayısal etki tahmini verilmedi (§0.1); her hamlenin ölçüsü GSC'de sayfa/sorgu bazında T+28 okunur.

### H0 — Ön koşul: GA4 bağlantısı
- **AARRR:** Ölçüm · **Kanıt:** Tip A (Apps listesinde Google Analytics yok, 3 Kas).
- **Neden önce:** GSC yalnız arama tarafını ölçer. GA4 olmadan H1–H5'in hiçbirinin danışma talebine (form/WhatsApp/telefon) etkisi okunamaz; Kanıt Üçgeni T0 kapanışı ve T+90 sayacı başlamaz.
- **Efor:** Düşük · **Kimde:** Ayhan (Wix paneli, kendi Google hesabı) · **Blokaj:** Yalnız Ayhan'ın zamanı.

### H1 — Yüksek-gösterimli yazılarda snippet onarımı (meta description + title)
- **AARRR:** Edinim · **Kanıt:** Sorun Tip A (54/60 yazıda meta description yok; 9 yazı toplam ~1.000 gösterim, çoğu 0 tık). Çözümün CTR etkisi Tip B (Google snippet'i yine kendi yazabilir).
- **Kapsam:** Önce §0.3 tablosundaki 9 yazı. Sonra kalan 45 yazı için tek partide açıklama.
- **Efor:** Düşük-orta. Açıklama metni Metin Yazarı (Model A), yazım Wix Blog SEO alanına API ile (blog yazısı, STATIC_PAGE değil; bilinen reversiyon katmanı bu değil).
- **Kimde:** Fox hazırlar (Metin Yazarı + Denetmen) → **Ayhan onaylar (Kademe 2, canlı değişiklik).**
- **Blokaj:** Yok. Yalnız Ayhan onayı. TİTCK dili: açıklamalarda vaat/üstünlük/fiyat yok ("silikon liner fiyatları" sorgusu fiyat içeriğiyle kovalanmaz).

### H2 — İç linkleme + "Protez Süreci" ankor sayfası
- **AARRR:** Edinim (sıralama derinliği) + Aktivasyon (okurdan danışma talebine yol) · **Kanıt:** Sorun Tip A (hizmet sayfalarından bloga 0 link, yazı içinde bağlam linki yok, /protez-sureci 404). Etkisi Tip B.
- **Kapsam:** (a) Taslağı hazır olan Protez Süreci metniyle (`-blog-protez-sureci-v02.md`, KÜNYESİZ) ankor sayfayı yayına almak; (b) takvim §1'deki pillar–hub haritasına göre her yazıya 1-2 bağlam linki (ilgili hizmet sayfası + pillar yazısı); (c) her hizmet sayfasına 2-3 ilgili yazı linki. Öncelik: "kafo" ve "dezartikülasyon" sorgularının ilk sayfaya yakın durduğu kümeler (/afo ↔ Ortez Nedir yazısı; /diz-dezartikülasyon sayfası ↔ dezartikülasyon yazıları).
- **Efor:** Orta. (b) Blog API ile yapılabilir; (a) ve (c) **Editör'den elle** (Wix'te sayfa/menü API'si yok).
- **Kimde:** Fox link haritasını hazırlar; blog içi linkler Kademe 2 (Ayhan onayı); sayfa tarafı **Ayhan, Editör'de.**
- **Blokaj:** Editör'den her yayın, bilinen STATIC_PAGE reversiyon riskini tetikleyebilir. **Bu yüzden H2'nin Editör kısmı Özgür Bey sorusuyla (15 Eki Madde 1) aynı pencerede yapılmalı** ve yayından hemen sonra canlı SSR kontrolü koşulmalı (§0.4 madde 7).

### H3 — v4 ortez adaylarından 4'lü alt küme
- **AARRR:** Edinim · **Kanıt:** Kapsam eşleşmesi Tip A (canlı `/soft-ortezler` sayfası el bileği, ayak bileği, diz, bel, boyun, dirsek ve omuz **soft** ortezlerini merkezin hizmeti olarak listeliyor). Talep sinyali **yok:** bu 8 konunun hiçbirinde GSC'de henüz gösterim yok, çünkü içerik yok. Arama hacmi beklentisi Tip B.
- **Seçim — v4'ün (b) seçeneğinin farklı bir alt kümesi.** Ölçüt: başlığın kapsamı canlı sitede merkezin hizmeti olarak görünüyor mu? Bu ölçüt AL listesine de uygulandı:
  - **AL (temiz):** #1 Ayak bileği burkulmasında ortez — sitedeki ayak bileği soft ortezleriyle birebir.
  - **AL, ama kapsam daraltılarak ya da teyitle:**
    - #4 Diz bağı (ACL/MCL): sitede yalnız soft dizlik var. Başlık "Diz bağı zorlanmasında soft dizlik ne işe yarar?" çerçevesine çekilir **ya da** Özgür Bey'den rijit/ligament diz ortezi uyguladıkları teyidi alınır.
    - #7 Bel korsesi "sert mi yumuşak mı": sitede sert bel ortezi yok. Başlık soft bel desteğine çekilir ya da sert ortez teyidi ön koşul olur.
    - #8 Bilek ateli (karpal tünel): "karpal" sitede geçmiyor. Başlık "El bileği soft ortezi ne zaman kullanılır?" çerçevesine çekilir ya da teyit alınır.
  - **BEKLET:** #2 Gece ateli, #3 Yürüteç botu, #5 Unloader diz ortezi. Bu ürün grupları sitede görünmüyor. v4 kendi notunda pediatrik/nörolojik konuları "kapsam teyitsiz" gerekçesiyle dışlamıştı; aynı ölçü bunlara da uygulanıyor.
  - **BEKLET:** #6 Boyunluk. Soft boyun ortezi sitede var, ama v4 başlığı travma/acil boyunluk çerçevesinde kurulmuş. Yüksek-YMYL; çerçeve soft ortez kullanımına çekilmeden üretilmemeli.
- **Neden 8 değil 4:** Ana gerekçe: H1+H2 kapanmadan eklenen yazı aynı tıklanmama sorununa girer. İkincil gerekçe: dış onayı olmayan yazı sayısını büyütmek, açık geriye-dönük onay riskini büyütür. 4'lü parti test görevi de görür: 28 gün sonra GSC'de gösterim alıyorlarsa kalan adaylar açılır.
- **Efor:** Orta (Metin Yazarı + Denetmen, EN SIKI tıbbi ihtiyat çerçevesi, marka/üretici adı yok).
- **Kimde:** Fox/Metin Yazarı üretir → Denetmen → **Ayhan onayı (Kademe 2).**
- **Blokaj:** Ayhan'ın v4 kararı. #4/#7/#8 dar (soft) çerçevede yazılmayacaksa Özgür Bey teyidi ön koşul.

### H4 — Güven katmanı (E-E-A-T / GEO): şablon artıklarını temizle, yazar ve şema katmanını sahiplen
- **AARRR:** Edinim (YMYL güven + AI cevap motorlarında kaynak olma) · **Kanıt:** Şablon artıkları Tip A (5 sayfa, 55 gösterim). AI görünürlüğü **ölçülmedi.** Elimde ChatGPT/Perplexity/AI Overview atıf ölçüm aracı yok; "AI'da görünüyoruz/görünmüyoruz" iddiası kurmuyorum. Genel GEO mekaniği (yapısal veri + uzman imzası + tutarlılık) Tip B.
- **Kapsam (30 gün içinde yapılabilir olan):**
  1. `/group/traveling-*`, `/portfolio`, `/portfolio/landscape-magazine`, `/members` → indeksten çıkar ya da kaldır, **ve pages-sitemap'ten de çıkar** (iki `/group/` sayfası şu an `robots: index`). Wix Groups ve Portfolio uygulamaları kullanılmıyorsa uygulamayı kaldırmak da seçenek. Ayhan, Editör/panel.
  2. Slug hijyeni: 12 `/product-page/i-m-a-product-*` sayfasına gerçek başlığa uygun slug, **eski URL'den 301 yönlendirmeyle**. Ayrı kalem, düşük öncelik.
  3. FAQPage şemasını Denetmen'den geçir (canlı SSR'da 32 yazı; API'de 30'u Wix otomatik üretimi): görünür metne sadık mı, TİTCK diline uygun mu. Uymayan kapatılır.
  4. Physician şeması ve künye spec'i hazır (15 Eki §2.3). **Yayını blokajlı** (aşağıda).
- **Efor:** Düşük (1, 3) / Düşük-orta (2) / Düşük ama blokajlı (4).
- **Kimde:** 1 → Ayhan (Editör) · 2 → Fox hazırlar (slug+yönlendirme listesi), Ayhan onaylar (Kademe 2) · 3 → Fox + Denetmen · 4 → Özgür Bey teyidi, sonra Fox.
- **Blokaj:** Künye ve Physician şeması **iki şeye** bağlı: ders verilen üniversite belgesi, ve Özgür Bey'in adıyla duran yazıların geriye-dönük onayı. Onaysız yazılara uzman şeması eklemek, imzası olmayan içeriği ona daha güçlü biçimde atfetmek olur. Bu adım bilerek ileri atılmadı.

### H5 — B2B hekim yönlendirme hedef listesi
- **AARRR:** Tavsiye · **Kanıt:** Kanal etkinliği bu müşteride Tip B (Luxmed'de yöntem çalıştı, burada ölçülmedi). Medikal-bağ'a göre meslek mensubuna tanıtım tüketici reklam yasağının dışında (avukat teyidiyle kesinleşir).
- **Kapsam:** Ataşehir/Kadıköy/Ümraniye çevresinde ortopedi, fizik tedavi ve nöroloji uzmanlarının kamuya açık kaynaklardan hedef listesi. Yanında outreach sırası ve takip ritmi taslağı. Bu tur Gelişim Yol Haritası #2'nin (tekrarlanabilir referral şablonu) ilk somut uygulaması olur.
- **Efor:** Orta (tek odaklı araştırma turu).
- **Kimde:** Fox (liste + yaklaşım, Kademe 1) → temas **Ayhan/Özgür Bey (Kademe 2)** — Fox kimseye yazmaz.
- **Blokaj:** Liste için yok. Temas için Özgür Bey'in bu kanala istekli olması ve kendi mevcut hekim ilişkilerini paylaşması gerekiyor, ki zaten tanıdığı bir hekime dışarıdan çıkarılmış listeyle soğuk yazılmasın.

**Bu 5'in dışında kalan ve bilerek öne alınmayanlar:** yeni yazı hacmi (v4'ün kalanı, #26 Lookalike), uluslararası dil sürümleri (önce TR verimi), GBP, IG serisi.

---

## 3 · AÇIK BLOKAJLAR

| Blokaj | Neyi tutuyor | Kimde |
|---|---|---|
| **GA4 bağlı değil** | Hiçbir hamlenin dönüşüm etkisi (form/WhatsApp/telefon) ölçülemiyor; Kanıt Üçgeni T0 kapanışı ve T+90 sayacı başlamıyor. GSC yalnız arama tarafını ölçer | Ayhan (Wix paneli, kendi hesabı) |
| **Özgür Bey'e Editör yayın sorusu** (15 Eki §2.1 taslağı hazır) | STATIC_PAGE/H1 düzeltmesi, H2'nin Editör kısmı | Ayhan (gönderim) |
| **Geriye-dönük içerik onayı** (~53 yazı, 54'ü Özgür Bey adıyla imzalı) | H4-3 (künye/Physician), H3'ün ölçeklenmesi | Ayhan → Özgür Bey/avukat |
| Künye belgesi (ders verilen üniversite) | Physician şeması | Özgür Bey |
| v4 kararı (8 / 4 / 0) | H3 | Ayhan |
| S11 (avukat) | IG ve her hasta-içerik — bu planın dışında tutuldu | Ayhan |

---

## 4 · RİSK / BAYRAK

- ⚠️ **Dikkat (orta güven):** Yazar alanı
  - **Talep:** Geriye-dönük onay kararı H3'ten önce Ayhan'ın gündemine alınsın.
  - **Bağlam:** 54 canlı yazı "Özgür Irmak", 6 yazı "stepsonclouds" yazarlı. Dış onayı alınmamış ~53 yazı var; **bu 53 ile 54 Özgür-yazarlı yazının ne kadar örtüştüğü kontrol edilmedi.** Örtüşme yüksekse, onaysız tıbbi bilgilendirme içeriği ilişkinin en hassas kişisinin adını taşıyor demektir.
  - **Seçenekler ve bedelleri:**
    - (a) Özgür Bey'e toplu okuma listesi. Bedel: onun zamanı (60 yazı); cevap gecikirse risk o süre boyunca açık kalır.
    - (b) Geçici olarak tüm 60 yazıda yazarı kurum adına ("Özgür Irmak Protez ve Ortez Merkezi") çekmek — 6 "stepsonclouds" yazısı da dahil, çünkü ajans adı tıbbi içerikte yazar olarak durmamalı. Bedel: uzman-imza E-E-A-T sinyali düşer; 60 yazıda canlı değişiklik (Kademe 2).
    - (c) Mevcut hâliyle bırakıp yalnız yeni yazıları onaylatmak. Bedel: mevcut riski olduğu gibi bırakır.
  - **Önerim:** (a). Örtüşme önce kontrol edilir (Fox, Kademe 1), ve liste yalnız onaysız olanlarla gönderilir. Cevap 2 haftada gelmezse (b) devreye girer.
  - **Termin:** H3 üretiminden önce; H4-4 (künye/Physician) buna bağlı.
- ⚠️ **Dikkat (orta güven):** FAQPage şeması denetimsiz (canlı SSR 32 / API 30 otomatik — §0.4 madde 4).
- ⚠️ **Dikkat (orta güven):** Haftalık SEO oto-kontrolü, API "var" dediğinde canlı HTML'e bakmıyorsa, API'de var olup canlıda olmayan veriyi kaçırır (§0.4 madde 7). Önerilen hamle: kontrolü her durumda canlı SSR ile karşılaştıracak hâle getirmek (zamanlanmış görevi değiştirmek kalıcı ayar olduğu için Ayhan'a sorulur).

---

## 5 · BÜYÜME HAZIRLIK SKORU (nitel — rubrik Bölüm 4; sayısal toplam verilmedi, §0.1)

| Kategori | 15 Eki | 3 Kas | Not |
|---|---|---|---|
| SEO Uygulama (%25) | 🟡 kararsız | 🟡 **hacim iyi, verim zayıf** | 32 yazı gösterimde; ama meta description 6/60, iç link 0, ankor 404 |
| Dönüşüm Optimizasyonu (%25) | — | — normalize | GA4 yok |
| Email & Lead (%20) | — | — normalize | Kapsam dışı |
| Kanal Stratejisi (%15) | 🟢 | 🟢 | Tek kanal (organik) disiplinli; B2B kolu hâlâ boş |
| Ölçüm & Tracking (%15) | 🔴 | 🔴 | GSC sağlam, GA4 yok, SEO kontrolünün neyi ölçtüğü teyitsiz |

---

## 6 · DENETMEN'E HAZIRLIK NOTU
- **Doğrulanacak rakamlar:** §0.1–0.3'teki tüm sayılar 3 Kasım API çekimi; çağrılar salt-okuma, aynı pencerelerle tekrarlanabilir. 15 Eyl–12 Eki penceresi bugün yeniden çekildi ve 15 Eki raporuyla birebir aynı (69/2.078).
- **Tip B'ye özellikle bak:** 19 Ekim kırılmasının nedeni, pozisyon düşüşünün yorumu, meta description–CTR ilişkisi, STATIC_PAGE saved-revision ipucu. Dördü de iddia değil yorum olarak yazıldı.
- **Kapsam/onay:** Hiçbir taahhüt, fiyat ya da söz yok. Yayın gerektiren her hamle Kademe 2 işaretli. 12 Eylül maddeleri ve hasta-içerik açılmadı. GBP yeniden sorulmadı.
- **Olası itiraz:** H3'te v4'ün kendi önerisinden (8'i birden) ayrıldım. Gerekçe §2 H3'te; Denetmen v4'le çelişkiyi tartmalı.
- **Atlanmış soru:** Wix Groups / Portfolio / Hotels / Members uygulamalarının sitede bilinçli olarak mı durduğu bilinmiyor. H4-1'den önce Ayhan'a sorulmalı.

---
*Growth Ajanı · 3 Kasım 2026 · Ölçüm araçları: Wix GSC Site Readiness API (connection, site-readiness, events, sitemaps, search-analytics), Item SEO Tags API (BLOG_POST), GetSiteContext, canlı sayfa SSR (curl). Hiçbir yazma çağrısı yapılmadı. Denetmen turu bekliyor.*
