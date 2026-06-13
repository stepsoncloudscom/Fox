# MARKA DENETİM RAPORU — v2 (Tam Tur)
## Luxmed Protez

**URL:** https://www.luxmedprotez.com
**Denetim Tarihi:** 13 Haziran 2026
**Denetleyen:** Keşif & Denetim Ajanı — Marka Bulutu OS
**Sektör Bağlamı:** Klinik / Sağlık (Rubrik §2.2-A) — YMYL
**Durum:** Baseline — Tam tur (teslim zincirinin ilk halkası; sıfırdan taze değerlendirme)
**Önceki çıktılar:** `luxmed-marka-denetim-raporu.md` (10 Haz baseline) + `luxmed-denetim-guncelleme-13haz.md` (13 Haz tazeleme). Bu rapor o ikisinin yerini almaz; üstüne taze, eksiksiz değerlendirme kurar.

---

## ⚠️ KANIT KISITI (en başta okunmalı — raporun tüm okuması buna bağlı)

**Site doğrudan erişime KAPALI (HTTP 403 — Cloudflare).** Bu, bu turda Keşif Ajanı tarafından **birinci elden yeniden test edilmiştir** (13 Haz, WebFetch → `HTTP 403 Forbidden`). Fox da aynı gün ayrı test etti, aynı sonuç. 13 Haz tazeleme turunda 4 farklı istemci kimliğiyle (normal tarayıcı, GPTBot, ClaudeBot, kimliksiz) yapılan curl testleri de tümü 403 döndürdü; `cf-ray` header'ı Cloudflare'i doğruladı.

**Sonuç:** JavaScript çalıştırmayan / Cloudflare challenge'ı geçemeyen hiçbir otomatik istemci sitenin içeriğine giremiyor. Gerçek tarayıcı erişimi, **Google Search Console, Google Analytics, Lighthouse/PageSpeed, Ahrefs/Moz erişimi YOK.**

**Bu raporun dayandığı kaynaklar:**
- Google SERP gözlemi (sayfa başlıkları, snippet'ler, indeks tazeliği)
- 3. taraf platformlar: Bookimed, Yandex Maps, Trustpilot, Şikayetvar, Zavis, LinkedIn
- Sosyal medya kamuya açık profil verisi (Instagram, YouTube, TikTok, Facebook)
- 9 Haz Enes Ammar Altun görüşme notları + müşteri context belgesi

> **Bunun puanlamaya etkisi (Rubrik §0.1 — İki Katman Kanıt, ZORUNLU):** Tek **Tip A** (ölçülmüş/doğrulanmış) kanıt sınıfı, bağımsız platform puanlarıdır (Google Maps 4.7/5–190, Yandex 4.9/5–24). Sitenin kendi performans metrikleri (CVR, organik trafik, DA, CWV) **ölçülemedi**. Dolayısıyla **genel sayısal skor VERİLMEZ.** 7 kategori niteliksel bantla değerlendirilir: **Kritik Açık · Zayıf · Orta · İyi · Güçlü.** Gözlem sayısallaştırılmaz — sahte kesinlik üretilmez (Towdoo dersi).

---

## GENEL MARKA OLGUNLUK PROFİLİ

**Baseline — Karma niteliksel profil (1 Tip A güven kategorisi güçlü; kalan kategoriler Tip B gözlem)**

| Olgunluk Dağılımı | Sayı |
|---|---|
| 🔴 Kritik Açık | 1 (Dijital Altyapı) |
| 🟠 Zayıf | 2 (Kimlik & Konumlandırma, Görsel Kimlik) |
| 🟡 Orta | 3 (Mesaj & İçerik, İçerik & SEO, SEO/Görünürlük) |
| 🟢 İyi | 1 (Marka & Güven / Sosyal Kanıt) |

**Tek cümle:** Luxmed, sahada kanıtlanmış güçlü bir klinik (4.7/5–190 Google, 4.9/5 Yandex, A.Ş. yapısı, 2010'dan uzman kurucu, 30+ ülkeden hasta beyanı) — ama bu güç dijital kapıya taşınamamış; teknik altyapı (403), dağınık kanal kimliği ve YMYL-riskli "garantili" dili bu değeri törpülüyor.

> **Neden sayısal genel skor yok:** Yukarıdaki kanıt kısıtı (§0.1). Gerçek performans baseline'ı GSC + Analytics + Lighthouse bağlandığında kurulacak. Bugünkü çıktı: **niteliksel olgunluk haritası + doğrulanmış güven metrikleri.**

---

## YÖNETİCİ ÖZETİ

Luxmed Protez, Türkiye'nin medikal protez-ortez sahasında gerçek klinik yetkinliği ve güçlü bağımsız sosyal kanıtı olan bir merkez. Google Maps'te **4.7/5 (190 yorum)**, Yandex Maps'te **4.9/5 (24 yorum)** — iki ayrı bağımsız platformda üst segment güven sinyali. Kurucu ortak **Enes Ammar Altun** 2010'dan beri ortez-protez uzmanı; klinik 2016 kuruluşlu, **Luxmed Protez Medikal Turizm Sanayi A.Ş.** tüzel yapısıyla faaliyet gösteriyor. Ottobock ve Össur uygulama yetkinliği, 24/7 çok dilli tercüman kadrosu (Rusça/Arapça/İngilizce/Fransızca), havalimanı karşılama + konaklama altyapısı ve "30+ ülkeden hasta" beyanı, bu markayı saf yerel rakiplerden ayıran gerçek bir sağlık turizmi kaldıracı sağlıyor.

Temel sorun değişmedi: **bu klinik güç dijital varlığa yeterince taşınmamış.** Web sitesi bugün de HTTP 403 (Cloudflare) döndürüyor; siteye gerçek tarayıcı dışı hiçbir otomatik istemci giremiyor. İndeksleme korunuyor (Şubat–Mart 2026 tarihli sayfalar SERP'te taze görünüyor → Googlebot IP-doğrulamasıyla geçiyor) — ama AI asistan crawler'ları (GPTBot, ClaudeBot) **test edildi, blokta.** Bu, AI çağında görünmezlik riski demek: uluslararası hasta "best prosthetic clinic Istanbul"u giderek AI'ya soruyor; healthcare aramalarının **%88'i Google AI Overview ile karşılanıyor** (BrightEdge, Aralık 2025) ve site AI'ya kapalıyken anlatının kaynağı kendi sitesi olamıyor, 3. taraf kayıtlarına (bayat Bookimed) kalıyor.

İki yeni kritik bulgu bu turda öne çıktı. **Birincisi — YMYL dil riski:** Luxmed'in KENDİ sayfası "**Garantili** Protez Bacak Yapan Firmalar" başlığını taşıyor (`/protez-bacak-yapan-firmalar`). Sağlıkta "garantili sonuç" dili Reklam Kurulu / RDTDK açısından riskli iddiadır. 13 Haz turunda bu dil bir rakipte (protezayak.com) flag'lenmişti; bu turda **Luxmed'in kendisinde tespit edildi** — düzeltme ve öncelikli risk. **İkincisi — gizli büyüme vektörü:** Luxmed, "kliniğini açmak isteyen girişimcilere ortaklık" + "tıbbi turizm şirketleriyle B2B iş birliği" modeli sunuyor (LinkedIn/3. taraf). Bu, raporun önceki turlarında yakalanmamış gerçek bir genişleme/lisanslama kapısı — strateji için önemli.

Marka kimliği hâlâ dağınık: en az 2 Instagram (@luxmedprosthetic 14K / @luxmedprotez 1.521), birden çok Facebook (Arapça /luxmedprotez.ar dahil), TikTok, YouTube, ve KVKK metnine göre ek olarak **Telegram + Snapchat** kanalları. Soru "neden 2 hesap" değil; "bu çok-kanallı dağılım bilinçli bir dil-pazar mimarisi mi, yoksa plansız çoğalma mı?" — görüşmede netleşmeli.

**En kritik 3 hamle:** (1) **HTTP 403 / bot koruması yapılandırmasını gözden geçir** — özellikle AI crawler erişimi; YMYL sitede AI görünürlüğü artık döviz hastasının ilk temas katmanı. (2) **"Garantili" dilini temizle** — Reklam Kurulu/RDTDK riski; yerine "uyumlu + kanıtlı güven" konumlandırması ile ayrış (rakiplerin riskli dile kaçtığı yerde Luxmed güvenle ayrışır). (3) **Kanal kimliğini tekleştir + uluslararası vitrini tazele** — Bookimed profili 15 ay bayat (29.03.2025), 190 yorumun yalnızca 5'ini gösteriyor; Yandex 4.9 kaldıraçlanmamış; tek net marka sesi + güncel vitrin döviz hastasının ilk izlenimini düzeltir.

---

## 7 BOYUTLU OLGUNLUK TABLOSU

*Rubrik §2.2-A (Klinik/Sağlık) — YMYL ağırlıkları. Tip A = ölçülmüş/doğrulanmış → sayısal olabilir; Tip B = gözlem → niteliksel band.*

| # | Kategori | YMYL Ağırlık | Kanıt Tipi | Olgunluk Bandı | Bulgu Özeti |
|---|---|---|---|---|---|
| 1 | **Marka & Güven** | %25 | **Tip A** (puanlar) + Tip B (görsel) | 🟢 **İyi** | Google 4.7/190 + Yandex 4.9/24 + A.Ş. + KVKK sayfası + ücretsiz garanti/bakım modeli. Güçlü güven tabanı. Açık: çift kanal görsel tutarsızlığı, doktor profili görünmüyor. |
| 2 | **Dönüşüm** | %25 | Tip B | 🟡 **Orta** | Fiyat/SGK şeffaflığı VAR (güç), WhatsApp + Telegram + canlı destek aktif. CTA akışı/CVR ölçülemedi (403). "Neden hemen ben" motivasyonu net kurulmamış. |
| 3 | **Mesaj & İçerik** | %20 | Tip B | 🟡 **Orta** | Blog geniş (SGK, ünlüler, ürün rehberi, güdük bakımı, biyonik el). /en aktif. ⚠️ "Garantili" dili + iç tutarsız hasta sayısı (2.000+ vs "yüzlerce"). |
| 4 | **Görünürlük (SEO)** | %15 | Tip B | 🟡 **Orta** | Çok sayıda terimde 1. sayfa; indeks taze. ✅ snippet işaretleri bilinçli SEO. AI crawler blokta → GEO riski. DA/trafik ölçülemedi. |
| 5 | **Konumlandırma** | %10 | Tip B | 🟠 **Zayıf** | "Neden Luxmed?" net değil. Ottobock farkı zayıflıyor (Proklinik = resmi Ottobock partneri). Gerçek açık alan: uluslararası + modern klinik kimliği — kullanılmıyor. |
| — | **Görsel Kimlik** *(alt boyut)* | (Marka&Güven içinde) | Tip B | 🟠 **Zayıf** | Çift kanal tutarsızlığı; "Lux" (lüks) çağrışımı görsel kimliğe işlenmemiş; standart klinik dil. Doğrudan erişilemedi (403). |
| 6 | **Büyüme & Strateji** | %5 | Tip B | 🟡 **Orta** | YENİ: B2B/franchise ortaklık modeli + sağlık turizmi B2B. Fiyat şeffaf. Açık: kanal dağınık, sadakat/CRM görünmüyor, model dijitalde öne çıkarılmamış. |

> **Onur & Temsil** YMYL bağlamında ağırlık olarak Marka & Güven'e dahildir (Rubrik §2.2-A). Ancak insan-merkezli marka olduğundan **ayrı bir mercek olarak** Kategori Bulguları'nda ve Açık #6'da değerlendirildi (acıma/ilham pornosu riski).

**Doğrulanmış Tip A metrikler:** Google Maps **4.7/5 (190 yorum)** · Yandex Maps **4.9/5 (24 yorum)**. Her ikisi de sektör güven bandının üstünde (Benchmark §8: ideal 4.2–4.5).

> **⚠️ Anchor kırılganlık notu (Denetmen Z4):** Bu iki metrik bu turda platformdan **doğrudan okunmadı** — Google puanı 3. taraf dizin (Zavis) üzerinden alındı; Yandex tabloda 24, metinde "13 Haz'da 25" (dalgalanma, gürültü içinde). Tüm sayısal güven mimarisi bu iki anchor'a dayandığından, GSC + doğrudan Maps erişimi açılınca **birincil teyit** yapılmalı.

---

## KATEGORİ BULGULARI (Detay)

### 1. MARKA & GÜVEN — 🟢 İyi (Tip A puanlar + Tip B görsel/altyapı)

**Doğrulanmış güven sinyalleri (Tip A):**
- **Google Maps 4.7/5 — 190 yorum.** Sektörde üst segment. Invespcro: 5+ yorum = %270 satın alma etkisi; 190 yorum bu etkiyi katlar.
- **Yandex Maps 4.9/5 — 24 yorum.** Stratejik açıdan kritik: Yandex = Rusya/BDT pazarının arama motoru. 48 fotoğraf, tam erişilebilirlik beyanı (rampa, erişilebilir tuvalet/otopark), panorama, ödeme yöntemleri. Rus hastanın doğal arama yolunda 4.9 hazır duruyor.

**Bu turda doğrulanan ek güven sinyalleri (Tip B):**
- **Tüzel yapı:** "Luxmed Protez Medikal Turizm Sanayi Anonim Şirketi" — KVKK aydınlatma metninde geçiyor. A.Ş. yapısı kurumsal güven sinyali (E-E-A-T Trustworthiness).
- **KVKK / veri koruma sayfası mevcut** (`/kvkk`). Baseline'da "güven sinyalleri görülemedi" denmişti; **düzeltme: KVKK politikası yayında.**
- **Ücretsiz garanti/bakım modeli:** Protez ömrü boyunca ücretsiz kontrol randevusu; soket değişimi/onarım. Şikayetvar yorumlarında somut örnek ("soket sorununu 1 haftada çözdüler, 2 aydır ağrısız yürüyorum"). Bu güçlü bir retention + güven unsuru — baseline'da yoktu.
- **Kurucu kimliği:** Enes Ammar Altun, ortez-protez uzmanı, 2010'dan beri, kurucu ortak, enes@luxmedprotez.com.

**Açıklar:**
- **Çift kanal görsel tutarsızlığı** (aşağıda Görsel Kimlik).
- **Doktor/uzman bireysel profili görünmüyor:** Bookimed "3 doktor" diyor ama bireysel bio yok. E-E-A-T Expertise için uzman kadrosunun isim+özgeçmiş+sertifika ile görünür olması beklenir. (Site içinde var mı, 403 mü engelliyor, yoksa yok mu — teyit gerek.)
- **Sertifika/akreditasyon (CE, Ottobock/Össur resmi yetki belgesi) görünürlüğü teyitsiz.**

---

### 2. DÖNÜŞÜM — 🟡 Orta (Tip B)

**Güçler:**
- **Fiyat/SGK şeffaflığı VAR** (10 Haz baseline'ının "fiyat yok" ifadesi hatalıydı; 13 Haz'da düzeltildi, bu turda teyit edildi):
  - `/protez-bacak-fiyatlari` — "2026 Protez Bacak Fiyatları (Mart Teklifi)" (güncel)
  - `/guncel-sgk-protez-odemeleri` — "[Şubat 2026]" (güncel)
  - Somut rakamlar: SGK ödeme aralığı 14.200–115.000 TL (2025); biyonik kol 950.000 TL'den (sitenin kendi beyanı). YMYL'de fiyat şeffaflığı güven + AI Overview'a uygun yapı.
- **Çoklu iletişim kanalı aktif:** WhatsApp Business (+90 537 349 84 03), Telegram, canlı destek (site beyanı: "canlı destek ekibi en hızlı şekilde ulaşır").

**Açıklar:**
- **CTA akışı / form sürtünmesi / CVR ölçülemedi** (403). Sağlık CVR benchmarkı %2–4 (Invespcro); gerçek oran bilinmiyor.
- **"Neden hemen, neden ben" motivasyonu:** Sağlık turizminde hasta karşılaştırma yapar; net bir aciliyet + farklılaştırıcı + tek birincil CTA kurulmamışsa ayrılıyor. Gözlemlenebilir kadarıyla mesaj "bize ulaşın" düzeyinde.
- **Kanal bolluğu sürtünme de olabilir:** WhatsApp + Telegram + Snapchat + telefon + form — hasta için çok kapı, marka için dağınık takip.

---

### 3. MESAJ & İÇERİK — 🟡 Orta (Tip B)

**Güçler:**
- **Geniş, güncel blog/rehber içeriği:** SGK ödeme rehberi, ünlü protez kullanıcıları, protez bacak/ayak kapsamlı rehber ("5 Uzmandan Rehber"), biyonik el, çocuk protezi, protez güdük bakımı, protez kol nasıl çalışır, üst ekstremite protezleri. Rakiplerin çoğunun ötesinde içerik hacmi.
- **/en İngilizce versiyon aktif:** "Prosthetic Limbs in Istanbul", "Below-Knee Prosthetic Leg", "Bionic Above-Knee" — search-intent uyumlu uluslararası sayfalar.

**Açıklar / Riskler:**
- ⚠️ **"Garantili" dili (YMYL RİSKİ — bu turun en kritik içerik bulgusu):** `/protez-bacak-yapan-firmalar` sayfası "**Garantili** Protez Bacak Yapan Firmalar" başlığını taşıyor. Sağlıkta "garantili sonuç/tedavi" dili Reklam Kurulu (Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği) ve RDTDK açısından **riskli iddia**. 13 Haz turunda bu dil rakip protezayak.com'da görülüp "Luxmed özenmemeli" denmişti — bu turda **Luxmed'in kendisinde** tespit edildi. Acil revizyon adayı.
  - **⚠️ Önemli ayrım (Denetmen Z2):** İki tür "garanti" karıştırılmamalı. (a) **Ürün/cihaz garantisi meşrudur ve korunur** — ör. "C-Leg 4 — 3 yıl garanti" üreticinin warranty beyanıdır, silinmemeli. (b) **Sonuç/tedavi garantisi risklidir** — sayfa başlığındaki "Garantili Protez Bacak..." ifadesi sonuç-garantisi çağrışımı taşır; RDTDK riski budur. İçerik Ajanı yalnızca (b)'yi düzeltmeli, (a)'yı korumalı (aşırı düzeltme tuzağı).
- **İç tutarsız hasta sayısı:** Bazı sayfalarda "2.000+ hasta", kurucu bio'sunda "yüzlerce hastaya başarıyla uyguladı", "300+ biyonik el". Beyanlar birbirini doğrulamalı; tutarsızlık güven aşındırır. (Hepsi Luxmed beyanı — 3. taraf teyidi yok; raporda "beyan" etiketli.)
- **Verbatim hasta sesi sınırlı:** Snippet'lerde "sağlık ve memnuniyet odaklı" gibi standart ifadeler. Hasta kendi cümlesiyle (Şikayetvar yorumları hariç) site içeriğine az taşınmış.

---

### 4. GÖRÜNÜRLÜK (SEO) — 🟡 Orta (Tip B)

**Güçler:**
- **Organik görünürlük güçlü:** "protez bacak firmalar", "İstanbul ortez protez", "protez bacak fiyatları", "Össur protez bacak", "biyonik el" gibi terimlerde 1. sayfa / üst sıra.
- **İndeks taze:** Şubat–Mart 2026 tarihli sayfa başlıkları SERP'te güncel → Googlebot erişimi korunuyor (403 seçici; IP-doğrulanmış Googlebot geçiyor).
- **Bilinçli SEO:** Snippet başlıklarında ✅ işareti (CTR optimizasyonu), tarih damgalı başlıklar (tazelik sinyali).

**Açıklar / Riskler:**
- ⚠️ **AI görünürlüğü (GEO) riski — birinci elden test edilmiş:** GPTBot + ClaudeBot dahil AI crawler'ları 403 (13 Haz curl testi). Healthcare aramalarının **%88'i Google AI Overview** ile karşılanıyor (BrightEdge, Aralık 2025; başka analizler %82+ ve "~%60" da veriyor — aralık geniş ama hepsi "yüksek ve büyüyen"). Site AI'ya kapalıyken AI özetinin kaynağı kendi sitesi değil, 3. taraf (bayat Bookimed) oluyor.
- **DA / organik trafik / CWV ölçülemedi** (araç erişimi yok).
- **Hreflang (TR/EN) yapısı belirsiz:** /en sayfalar var ama TR/EN hreflang doğru kurulu mu bilinmiyor. Yanlışsa Google dilleri çakıştırabilir.
- **Sayfa tazeliği tutarsızlığı (R1):** `/protez-kol-fiyatlari` başlığı 2025 Nisan'da kalmış; kardeş `/protez-bacak-fiyatlari` 2026 Mart. Bayat başlık CTR + güven kaybı. (Hızlı kazanım.)

---

### 5. KONUMLANDIRMA — 🟠 Zayıf (Tip B)

**Durum:** "Luxmed nedir, Nesa'dan / Teknik Ortopedi'den / Proklinik'ten farkı nedir?" sorusu net cevaplanmıyor.

**Rekabet manzarası (bu turda genişledi):**
- **Nesa Ortopedi:** Köklü (1976), İstanbul-Tekirdağ-Kocaeli; Luxmed'in en hassas rakibi (exclusive clause riski — context).
- **Teknik Ortopedi:** İzmir merkezli, **kuruluş 1979 (≈45 yıl — "60. yıl" ibaresi varsa hatalı)**; İzmir + Gaziantep + İstanbul. **Düzeltme (Z3):** baseline "uluslararası hasta hedeflemiyor" demişti — uluslararası geçmişi var ama dikkatli çerçevele: *kurucu* Almanya'da eğitim aldı (1971–80, tarihsel); şirketin yurtdışı **operasyonu Çin'de (2004'ten)**. Yani "Almanya'da şube var" değil — yine de saf-yerel değil, uluslararası deneyimli oyuncu.
- **Proklinik:** **Resmi Ottobock Türkiye partneri** + kendini "**Türkiye'nin en büyük protez-ortez merkezi**" konumluyor (~35 çalışan, 2006'dan, Kıbrıs operasyonu — Z5). ⚠️ Çift dezavantaj: hem "resmi partner" unvanı hem **ölçek + ağ** Proklinik'te. Luxmed'in "Ottobock uygulama noktası" farkı zayıf; "yetkili uygulayıcı" konumunu netleştirmeli, "resmi partner" izlenimi vermemeli.
- **Diğer:** Özgür Irmak, Hedef Protez (Sağlık Bakanlığı lisanslı + SGK), Sena Ortopedi (2010), Alsan Ortopedi (2006), Kariyer Ortopedi — kalabalık alan.

**Luxmed'in gerçek açık alanı (kullanılmıyor):** **Uluslararası hasta + modern klinik marka kimliği + kanıtlı güven (4.7/4.9) + çok dilli sağlık turizmi operasyonu.** Tek tek rakipler bunların bir kısmına sahip; bütününe sahip görünen yok. Dunford 5 bileşen: değer kanıtı güçlü (4.7/4.9, 2K+), rekabet alternatifi kısmen net, ama benzersiz özellik + hedef hasta önceliği + kategori keskinliği eksik.

---

### Görsel Kimlik (alt boyut) — 🟠 Zayıf (Tip B)

Siteye doğrudan erişilemedi (403). Sosyal medyada standart klinik görsel dil: ürün fotoğrafı, hasta videosu, bilgi grafiği. @luxmedprosthetic İngilizce ağırlıklı, medikal-steril ton. "Lux" = lüks çağrışımı görsel kimliğe işlenmemiş görünüyor. Asıl sorun: **çift/çoklu kanal görsel tutarsızlığı** marka hafızasını bölüyor.

---

### 6. BÜYÜME & STRATEJİ — 🟡 Orta (Tip B)

**Bu turun yeni stratejik bulgusu:**
- ⭐ **B2B / franchise / ortaklık modeli:** Luxmed, "kliniğini açmak isteyen girişimcilere ortaklık desteği" (ekip kurma, kendi ülkesinde klinik kurma, bazı ülkelerde ortaklık) + "tıbbi turizm şirketleriyle B2B iş birliği" sunuyor (LinkedIn / 3. taraf profil). **Bu gerçek bir genişleme/lisanslama vektörü** — önceki turlarda yakalanmamıştı. Strateji için önemli: marka yalnızca hasta değil, ortak/franchise de hedefliyor.

**Diğer güçler:** Fiyat şeffaflığı, sağlık turizmi operasyonu (havalimanı + konaklama + 24/7 tercüman), Bookimed kanalı.

**Açıklar:** Kanal dağınık; sadakat/CRM mekanizması görünmüyor (protez değişim döngüsü 2–3 yıl — hatırlatma sistemi fırsatı); B2B/franchise modeli dijitalde öne çıkarılmamış (gizli kalmış değer).

---

## GÜÇLÜ YANLAR (max 5)

1. **İki bağımsız platformda üst-segment güven (Tip A):** Google 4.7/5 (190) + Yandex 4.9/5 (24). Yandex özellikle RU/BDT pazarı için hazır kaldıraç. Sektör ideal bandının (4.2–4.5) üstünde.
2. **Kurumsal + yasal güven altyapısı:** A.Ş. tüzel yapısı, KVKK sayfası, ücretsiz garanti/bakım modeli (ömür boyu kontrol, soket değişimi), 2010'dan uzman kurucu. YMYL'de E-E-A-T tabanı.
3. **Sağlık turizmi operasyonu + uluslararası erişim:** 24/7 çok dilli tercüman (RU/AR/EN/FR), havalimanı karşılama + konaklama, "30+ ülkeden hasta" (beyan), Bookimed kanalı. Yerel rakiplerin çoğunda yok.
4. **İçerik + fiyat/SGK şeffaflığı:** Geniş güncel blog + indeksli fiyat/SGK sayfaları (Şubat–Mart 2026). Organik 1. sayfa görünürlüğü bunun çıktısı; AI Overview'a uygun yapı.
5. **B2B/franchise genişleme modeli:** Ortaklık + tıbbi turizm B2B — markayı tek-lokasyon klinikten ölçeklenebilir modele taşıyan gerçek bir büyüme vektörü.

---

## KRİTİK AÇIKLAR (öncelik sıralı, numaralı)

**1. [Öncelik 1 — Teknik/AI Görünürlük] HTTP 403 / AI crawler bloğu.**
Site Cloudflare ile JS çalıştırmayan tüm istemcilere kapalı; AI crawler'ları (GPTBot, ClaudeBot) birinci elden test edildi → blokta. İndeksleme korunuyor ama AI çağında görünmezlik + 3. taraf platform senkronunun bozulması (Bookimed bayat) gerçek maliyet. **Aksiyon:** bot koruması yapılandırmasını gözden geçir — verified AI crawler'lara seçici izin; ardından GSC + Analytics bağla (sayısal baseline'ın ön koşulu).

**2. [Öncelik 2 — YMYL Hukuki] "Garantili" dili (ürün ≠ sonuç).**
Luxmed'in kendi sayfası "Garantili Protez Bacak Yapan Firmalar" başlığını taşıyor — bu **sonuç-garantisi** çağrışımıdır, Reklam Kurulu/RDTDK riski. **Ayrım (Z2):** cihaz/ürün warranty'si (ör. "C-Leg 4 — 3 yıl garanti") meşrudur, korunur; risk yalnızca sonuç/tedavi garantisi dilindedir. **Aksiyon:** sayfa başlığı/sonuç dilini "uyumlu, kanıtlı, güvenceli süreç/bakım" gibi mevzuata uygun dile çevir; ürün garanti beyanlarına dokunma. Rakipler riskli dile kaçarken Luxmed uyumla ayrışır.

**3. [Öncelik 3 — Kimlik] Çok-kanallı dağılım.**
En az 2 IG (14K EN / 1.521 TR) + çoklu FB (Arapça /luxmedprotez.ar dahil) + TikTok + YouTube + KVKK'ya göre Telegram + Snapchat. Hasta hangi kanalın "ana" olduğunu bilemiyor; sinyal + marka hafızası bölünüyor. **Aksiyon:** ana kanal mimarisi belirle (dil-pazar bazlı bilinçli yapı mı, tekleştirme mi — görüşme sorusu); tutarlı görsel + ses.

**4. [Öncelik 4 — Uluslararası Vitrin] Bookimed profili bayat/yarım.**
Son güncelleme 29.03.2025 (~15 ay); 190 yorumun yalnızca 5'ini gösteriyor; doktor bireysel profili yok; 5 fotoğraf (Yandex'te 48). "Bone Fracture Treatment" kalemi protez merkezine yabancı (platform oto-kategorisi olabilir). Uluslararası hastanın ilk temas noktasında zayıf izlenim. **Aksiyon:** profil tazele (güncel fiyat, yorum senkronu, doktor bio, fotoğraf), "verified" rozeti al. Düşük efor/yüksek etki.

**5. [Öncelik 5 — Konumlandırma] "Neden Luxmed?" yanıtsız + Ottobock farkı zayıflıyor.**
Kalabalık rakip alanında (Nesa=köklü/1976, Teknik Ortopedi=uluslararası deneyimli, **Proklinik=resmi Ottobock partneri + "Türkiye'nin en büyüğü" iddiası/~35 çalışan**, Sena, Alsan…) Luxmed'in farkı net değil. "Ottobock uygulama noktası" zayıf farklılaştırıcı. **⚠️ Strateji uyarısı (Z5):** "modern uluslararası klinik" açık-alanı fazla rahat varsayılmamalı — Proklinik ölçek+ağ, Teknik Ortopedi uluslararası deneyim taşıyor. Luxmed'in gerçek ayrışması **kanıtlı güven (4.7/4.9) + çok dilli sağlık turizmi operasyonu + onur-merkezli marka** bileşimidir; tek tek değil bütünüyle. **Aksiyon:** bu bütünü tek konumlandırma cümlesine çevir; "resmi partner" değil "yetkili uygulayıcı" dilini netleştir.

**6. [Öncelik 6 — Onur & Temsil] Klinik-kahraman çerçevesi riski.**
YouTube Shorts'larda acıma dili yok (olumlu) ama yer yer klinik-kahraman çerçevesi ("hastamıza yeni bir başlangıç sunduk") — özne kurum, hasta değil. Onur-merkezli üretimde özne hastaya kaymalı (güç, fail, gündelik gerçeklik — Nielsen 2024). Inspiration-porn tuzağı medikal/protez içerikte yüksek risk. **Aksiyon:** tüm hasta içeriği bu mercekten geçsin; mevcut malzeme "ham" değerli, çerçeve hastaya çevrilmeli.

**7. [Öncelik 7 — SEO Teknik + Tazelik] Hreflang belirsiz + bayat başlık.**
/en hreflang yapısı teyitsiz (dil çakışması riski); `/protez-kol-fiyatlari` başlığı 2025'te kalmış. **Aksiyon:** GSC hreflang raporu (403 çözülünce); bayat başlıkları 2026'ya güncelle (hızlı kazanım).

**8. [Öncelik 8 — E-E-A-T] Uzman/sertifika görünürlüğü teyitsiz.**
Kurucu adı var ama uzman kadrosunun bireysel bio + sertifika + Ottobock/Össur yetki belgesi görünürlüğü doğrulanamadı (403). Bookimed'de doktorlar profilsiz. YMYL'de Expertise sinyali kritik + Nesa/Teknik'e karşı farklılaştırıcı olabilir. **Aksiyon:** uzman bio + sertifika sayfası (varsa öne çıkar, yoksa oluştur).

---

## RİSK & FIRSAT KAYITLARI

**Fırsatlar:**
- **F1 — Yandex 4.9/24 kaldıraçlanmamış:** RU/BDT hasta yolculuğunun arama katmanında güçlü kanıt hazır; site RU içeriğiyle desteklenince zincir tamamlanır.
- **F2 — Bookimed hasta-kaynak beyanı:** "BDT, Balkan, Arap Ligi" — uluslararası konumlandırma için platform-doğrulamalı dayanak.
- **F3 — Fiyat/SGK şeffaflık içeriği:** Güncel + AI Overview'a uygun. 403 (özellikle AI crawler) çözülürse AI görünürlüğünde erken davranma şansı.
- **F4 — B2B/franchise modeli:** Tek-klinikten ölçeklenebilir modele; dijitalde öne çıkarılınca ortak/yatırımcı kanalı açar.
- **F5 — Uyum ile ayrışma:** Rakipler "garantili" riskli dile kaçarken (protezayak.com + Luxmed'in kendi sayfası), mevzuata uygun + kanıtlı güven dili güçlü ayrıştırıcı olabilir (Luxmed önce kendi dilini düzeltirse).

**Riskler:**
- **R1 — AI çağında görünmezlik:** AI crawler bloğu + healthcare AI Overview ~%89. Döviz hastası AI'ya soruyor; anlatının kaynağı 3. taraf (bayat) kalıyor.
- **R2 — "Garantili" dili:** Reklam Kurulu/RDTDK; Luxmed'in kendi sayfasında. Hukuki + itibar riski.
- **R3 — Bookimed bayatlığı:** 15 aylık fiyat + 5/190 yorum + profilsiz doktor → ilk temasta zayıf izlenim.
- **R4 — İç tutarsız beyan:** "2.000+" vs "yüzlerce" vs "300+ biyonik el". Tutarsızlık + 3. taraf teyit yokluğu güven aşındırır.
- **R5 — Şikayetvar görünürlüğü teyitsiz:** Profil sayfası var; şikayet hacmi/yanıt oranı doğrudan doğrulanamadı (sayfa fetch erişimine kapalı). Olumsuz yorum varsa marka yönetimi/yanıt durumu kontrol edilmeli. **[açık doğrulama — düşük güven]**
- **R6 — Ottobock "resmi partner" karışıklığı:** Resmi partner Proklinik; Luxmed "resmi" izlenimi verirse hem yanıltıcı hem rakip-karşıtı zemin.

---

## BASELINE METRİKLERİ

| Metrik | Değer | Kaynak | Kanıt Tipi | Not |
|---|---|---|---|---|
| Google Maps Puanı | **4.7/5** | Google Maps (bağımsız) | **Tip A** | 190 yorum — doğrulanmış |
| Google Maps Yorum | **190** | Google Maps | **Tip A** | Haziran 2026 |
| Yandex Maps Puanı | **4.9/5** | Yandex Maps (bağımsız) | **Tip A** | 24 yorum (13 Haz'da 25 — dalgalanma, gürültü içinde) |
| Yandex Yorum | **24** | Yandex Maps | **Tip A** | 48 fotoğraf, erişilebilirlik beyanı |
| Trustpilot | 7 yorum | Trustpilot | Tip B | Skor fetch'le doğrulanamadı (Trustpilot kendi bot koruması); içerik olumlu |
| Bookimed Puanı | 4.6/5 (Google kaynaklı, 5 yorum gösterimi) | Bookimed | Tip B | Profil 29.03.2025'ten bayat |
| IG @luxmedprosthetic | **14.000** takipçi / 130 post | Instagram kamuya açık | Tip B | Ana hesap, EN ağırlıklı |
| IG @luxmedprotez (TR) | **1.521** takipçi | Instagram kamuya açık | Tip B | Bölünme rakamla kanıtlı |
| Facebook | 8.4K (baseline; bugün yeniden doğrulanamadı) | Facebook | Tip B | + Arapça /luxmedprotez.ar sayfası |
| Kanal sayısı (toplam tespit) | ≥9 varlık | Platform + KVKK metni | Tip B | 2 IG + ≥2 FB + YT + TikTok + LinkedIn + Telegram + Snapchat + WhatsApp |
| Tüzel yapı | A.Ş. | KVKK sayfası | Tip B | "Luxmed Protez Medikal Turizm Sanayi A.Ş." |
| Hasta uygulama (beyan) | "2.000+" / "yüzlerce" / "300+ biyonik el" | Site/LinkedIn copy | Tip B | Beyan — 3. taraf teyit yok; iç tutarsız |
| Uluslararası erişim (beyan) | "30+ ülke" | LinkedIn/Trustpilot copy | Tip B | Beyan — doğrulanmamış |
| Organik görünürlük | 1. sayfa (tespit edilen terimler) | Google SERP | Tip B | DA/trafik yok |
| Healthcare AI Overview kapsama | %88 (Aralık 2025; aralık: ~%60–%89) | BrightEdge | Tip A (dış benchmark) | Sektör verisi — Luxmed'e özgü değil |
| Organik Trafik | N/A | GSC erişimi yok | — | HTTP 403 |
| Domain Authority | N/A | Ahrefs/Moz yok | — | — |
| PageSpeed / CWV | N/A | Lighthouse yok | — | HTTP 403 |
| Dönüşüm Oranı (CVR) | N/A | Analytics yok | — | YMYL benchmark %2–4 |

> **Gerçek performans baseline'ı GSC + Analytics + Lighthouse bağlanınca kurulacak.** Önce teknik/AI-crawler engelini çöz, sonra ölç.

---

## v1 / 13-HAZ'A GÖRE DEĞİŞENLER & DERİNLEŞENLER (delta özeti)

| Tür | Bulgu |
|---|---|
| **AYNI** | HTTP 403 (Cloudflare) — bugün birinci elden yeniden teyit (WebFetch → 403). Google 4.7/190 geçerli. Çift IG bölünmesi (14K/1.521). 7 kategori niteliksel bant dağılımı geçerli. Sayısal genel skor verilmiyor (§0.1). |
| **YENİ — düzeltme/risk** | ⭐ "Garantili" dili **Luxmed'in KENDİ sayfasında** (`/protez-bacak-yapan-firmalar`). 13 Haz'da rakipte flag'lenmişti; bu turda Luxmed'de. Öncelik 2 risk. |
| **YENİ — stratejik** | ⭐ **B2B/franchise ortaklık modeli** (girişimciye klinik açma desteği + tıbbi turizm B2B). Önceki turlarda yoktu. Gerçek genişleme vektörü. |
| **YENİ — güven** | A.Ş. tüzel yapısı + KVKK sayfası teyit (baseline "güven sinyali görülemedi" → **düzeltildi: var**). Ücretsiz garanti/bakım modeli. |
| **YENİ — kanal** | Telegram + Snapchat (KVKK metninden) → kanal sayısı ≥9. Dağınıklık bulgusu güçlendi. |
| **YENİ — rekabet** | Proklinik = **resmi Ottobock Türkiye partneri** → Luxmed'in Ottobock farkı zayıfladı. Teknik Ortopedi Almanya'da da var → "uluslararası hasta hedeflemiyor" varsayımı düzeltildi. |
| **DERİNLEŞTİ** | AI Overview oranı artık **kaynaklı**: %88 (BrightEdge, Aralık 2025) — 13 Haz "sayı konulmadı" boşluğu dolduruldu; context belgesiyle de tutarlı. AI crawler bloğu (GPTBot/ClaudeBot) 13 Haz curl testiyle + bu tur SERP gözlemiyle teyitli. |
| **DERİNLEŞTİ** | İç beyan tutarsızlığı netleşti: "2.000+" vs "yüzlerce" vs "300+ biyonik el". |
| **AÇIK KALDI** | Bookimed €11.200 paketi kamuya açık profilde yok (Enes panelinden teyit etmeli). Şikayetvar şikayet hacmi doğrudan doğrulanamadı (fetch erişimi yok). |

---

## SONRAKİ ADIM

1. Bu rapor (v2) → **Denetmen 7 mercek** denetimi → Fox+Denetmen konsensüs → **Ayhan onayı** (Kademe 2).
2. Onay sonrası, **Strateji Ajanı** bu raporu teslim zincirinin temeli olarak alır (bloke edici sorular: Nesa exclusive durumu + SGK/serbest hasta oranı — context'ten).
3. **İçerik Ajanı** PDF + Excel üretir (aşağıdaki brief). PDF/Excel bu turda üretilmedi (Keşif üretmez — İçerik üretir, Keşif onaylar).
4. **Görüşmede teyit edilecekler:** (a) Bookimed €11.200 paket yayın durumu, (b) kanal çoğalması plan mı/organik mi, (c) bot koruması kimin yönetiminde (hosting/ajans?), (d) GSC + Analytics erişimi — sayısal baseline ön koşulu, (e) Şikayetvar profil durumu/şikayet var mı, (f) uzman kadrosu bio/sertifika sitede var mı.

---

## İÇERİK AJANI BRİEF

### PDF — Luxmed Marka Denetim Raporu v2 (pdf-motoru.py, ayhan-premium register — PPTX değil)
- **Marka:** Luxmed Protez | **Tarih:** 13 Haziran 2026 | **Format:** PDF (ayhan-premium: Didot/Avenir/altın — müşteriye profesyonel sunum)
- **Renk paleti:** Altın (#C9A84C) + koyu lacivert (#1A2744) + beyaz + klinik gri aksanlar (marka-kiti.md ile teyit)
- **Bölüm listesi:**
  1. Kapak — "Luxmed Protez — Marka Denetim Raporu | 13 Haziran 2026 | Marka Bulutu OS"
  2. Kanıt Kısıtı kutusu — "Site 403; performans ölçümü teknik/AI-crawler engeli kalkınca" (güven artıcı dürüstlük)
  3. Genel Olgunluk Profili — "Baseline: Karma (1 Kritik Açık · 2 Zayıf · 3 Orta · 1 İyi)" + Tip A/B açıklaması. **Sayısal genel skor YOK.**
  4. Olgunluk Isı Haritası — 7 kategori renk-kodlu bant (🔴🟠🟡🟢). **Radar/sayısal grafik YOK** (Tip A performans verisi yok). Tip A güven metrikleri ayrı kutu: Google 4.7/190 + Yandex 4.9/24.
  5. Güçlü Yanlar — 5 madde (güven metrikleri öne, ayrı kutu)
  6. Kritik Açıklar — 8 madde öncelik sıralı (özellikle "Garantili" dili + AI crawler bloğu öne)
  7. Risk & Fırsat kayıtları
  8. Baseline Metrikleri tablosu (Tip A/B işaretli)
  9. Stratejik Yol Haritası — 3 öncelik (0–7 gün / 1–4 hafta / 1–3 ay)
  10. Sonraki Adım — Strateji Ajanı'na geçiş, Marka Bulutu OS faz zinciri
- **Ton:** Klinik güveni teyit eden, boşlukları çözüm odaklı sunan; dürüstlük açıkça yazılır ("altyapı + 3. taraf değerlendirildi, performans ölçümü engel kalkınca").
- **⚠️ Görsel kalite:** pdf-motoru.py, ayhan-premium tema. Render-and-review zorunlu. AI yüz/karakter YASAK (medikal güven). Türkçe glyph kontrolü (İ, Ş, Ğ, ü, ö, ç).

### Excel — Luxmed SEO Teknik Kritik
- **Çıktı yolu:** `/raporlar/luxmed-seo-kritik.xlsx`
- **Sheet 1 (Teknik Sorunlar):** URL | HTTP | Sorun | Öncelik | Aksiyon | Etki | Durum
  - Ana sayfa: HTTP 403 | Cloudflare — AI crawler bloğu (GPTBot/ClaudeBot test edildi) | YÜK | Bot koruması yapılandırması; verified AI crawler izni; GSC kapsam | AI görünürlük kaybı + 3. taraf senkron | Açık
  - /en, /hakkimizda, /iletisim: HTTP 403 | Aynı | YÜK | Aynı | — | Açık
  - robots.txt / sitemap.xml: erişilemedi (403) | Crawl yönergesi doğrulanamıyor | ORTA | 403 çözülünce kontrol | — | Açık
  - Hreflang (TR/EN): Bilinmiyor | Dil çakışması riski | ORTA | GSC hreflang raporu | Uluslararası sıralama | Açık
- **Sheet 2 (İçerik/Uyum Sorunları):** Sayfa | Sorun | Öncelik | Aksiyon
  - /protez-bacak-yapan-firmalar | "Garantili" dili — Reklam Kurulu/RDTDK riski | YÜK | "garantili"→mevzuata uygun dil | Açık
  - /protez-kol-fiyatlari | Başlık 2025 Nisan'da bayat | ORTA | 2026'ya güncelle | Açık
  - Genel | İç tutarsız hasta sayısı (2.000+/yüzlerce/300+) | ORTA | Tek tutarlı, kaynaklı rakam | Açık
- **Sheet 3 (İçerik Boşlukları):** Anahtar Kelime | Mevcut | Hedef Sayfa | Öncelik
  - "prosthetics Istanbul" / Var (zayıf) → /en/about-us güçlendir / YÜK
  - "best prosthetic clinic Turkey 2026" / Yok → /en blog / YÜK
  - "protez İstanbul Rusça (Yandex)" / Zayıf → RU landing / YÜK
  - "Össur protez Türkiye" / Var → güncel tut / ORTA
  - "çocuk protez İstanbul" / Var → güçlendir / ORTA
- **Sheet 4 (3. Taraf Vitrin):** Platform | Durum | Aksiyon | Öncelik
  - Bookimed | 15 ay bayat, 5/190 yorum, profilsiz doktor | Tazele + verified + doktor bio | YÜK
  - Yandex | 4.9/24 — kaldıraçlanmamış | RU içerik + yorum artır | ORTA
  - Trustpilot | 7 yorum | Yorum kampanyası | DÜŞÜK
  - Şikayetvar | Durum teyitsiz | Profil sahipliği + yanıt durumu kontrol | ORTA
- **Renk:** Başlık (Altın #C9A84C + koyu lacivert #1A2744, beyaz metin) | Öncelik YÜK=kırmızı / ORTA=sarı / DÜŞÜK=yeşil | Durum açık=kırmızı / kapalı=yeşil

---

*Keşif & Denetim Ajanı — Tam tur (v2), 13 Haziran 2026.*
*Kanıt sınırı: Site HTTP 403 (Cloudflare) nedeniyle doğrudan taranamadı — birinci elden teyit edildi. Tüm Tip B gözlemler; SERP, kamuya açık sosyal profiller, Bookimed/Yandex/Trustpilot/Şikayetvar/LinkedIn 3. taraf kayıtları ve müşteri görüşme notlarına dayanır. Erişilemeyen alanlar açıkça işaretlendi. Tip A sayı yalnızca doğrulanmış platform puanlarından; genel sayısal skor §0.1 gereği verilmedi. Denetmen 7 merceğinden geçmeden müşteriye gitmez.*
