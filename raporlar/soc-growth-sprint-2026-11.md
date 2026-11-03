# Steps On Clouds — Growth Sprint (4 Kas – 4 Ara 2026)
*3 Kasım 2026 · Growth Ajanı · Öz-pilot · Durum: TASLAK · Denetmen 3 Kas: DİKKAT (6 küçük düzeltme dosyada uygulandı, `[Denetmen]` işaretli)*

> **Yöntem:** Canlı site bugün iki yoldan okundu: ham HTML (`curl`, string kontrolü) ve render edilmiş sayfa (WebFetch). **Tip A** = bugün ölçüldü ya da ham HTML'de doğrulandı. **Tip B** = gözlem. **ÖLÇÜLMEDİ** = bu turda erişilemedi, tahmin yazılmadı. Sayısal skor yok (§0.1). Hiçbir şey değiştirilmedi, yayınlanmadı, kimseye mesaj gitmedi.

---

## 1 · DELTA: 25 Ağu → 3 Kas (canlı)

| Alan | 25 Ağu | 3 Kas (bugün) | Delta | Kanıt |
|---|---|---|---|---|
| **Etkinlikler (Blok 0.1)** | 5 Tem + 2 Ağu "Yaklaşan", kayıt açık | İkisi hâlâ **"Yaklaşan Etkinlikler"** başlığı altında, ana sayfada da öyle. "Geçmiş" bölümü yok. Detay sayfalarında **"Biletler satışta değil"** yazıyor, Kayıt Ol butonu yok. | 🟡 **Yarım kapandı.** Kayıt artık alınmıyor (büyük ihtimalle "Son kayıt: 30 Haziran" tarihi otomatik geçtiği için, elle kapatıldığı için değil; nedenini teyit etmedim). Etkinlikler ise **hâlâ "yaklaşan" diye** duruyor. | Tip A |
| **Yoğurtçu etkinliğinde tarih çelişkisi** | Kayıtta yok | Aynı sayfada üç ayrı tarih var: program **2 Ağu**, sayfa başlığı **26 Tem**, açıklama **"25 Temmuz'da"**. | 🔴 **Yeni bulgu** (önceden de olabilir, Ağustos'ta kayda geçmemiş) | Tip A (ham HTML) |
| **Hero (Blok 0.2)** | `farklılıkları güce çevİr`, reddedilmiş slogan | Aynısı. Ham HTML'de `çevİr` var. | ⚪ **Değişmedi** | Tip A |
| **Glyph hatası, ikinci yer** | Kayıtta yok | Hakkımızda başlığı: **`Ekİbİmİz`** | 🔴 **Yeni bulgu.** Hata aynı (Bebas büyük-İ), ikinci sayfada | Tip A (ham HTML) |
| **Glyph hatası, üçüncü yer** `[Denetmen]` | Kayıtta yok | TR header satırı (ana sayfa, Hakkımızda, Projeler — tüm TR sayfalar): **`take a step ınto the sky`** (noktasız ı). EN sürümü doğru (`into`) | 🔴 **Yeni bulgu.** Ters yönlü hata: İngilizce kelimede Türkçe ı | Tip A (ham HTML, 3 Kas Denetmen ölçümü) |
| **Blog** | 1 yazı (31 Eki 2025) | Hâlâ 1 yazı, aynı yazı | ⚪ **Değişmedi**, blog 12+ aydır sessiz | Tip A |
| **Projeler** | 2 Össur başlığı, açıklama yok | Aynı | ⚪ Değişmedi | Tip A |
| **Hakkımızda** | 4 kişilik ekip, sayısal iddia yok | Aynı. Render edilmiş sayfa ekip bölümünde **İngilizce şablon metni** gösteriyor | ⚪ + yeni gözlem | Tip A · `[Denetmen]` şablon metni ham HTML'de de var ("…your Team section. It's a great place to introduce your team…"); görünürlüğü Editör'de teyit edilecek |
| **Menü / ticari kol** | Ticari kol yok | Projeler · Mağaza · Etkinlikler · Hakkımızda · Blog. Ajans ya da MBOS **yok** | ⚪ Değişmedi | Tip A |
| **Mağaza** | 1 ürün, CloudOne Çorap **₺550** | 1 ürün, CloudOne Çorap **₺700,00** (indirimli fiyat yok, `comparePrice: 0`) | 🟢 **Fiyat değişmiş — Ayhan teyit etti (3 Kas): değişikliği kendisi yaptı.** Mekanizma metni hâlâ belirsiz ("Ticaret misyonu taşır. Misyon ticarete anlam verir.") | Tip A |
| **Ölçüm (Blok 3)** | Teyitsiz | Ana sayfada **`google-site-verification` meta etiketi var**. Yani bir GSC mülkü en azından doğrulama aşamasından geçmiş. GA4/GTM ölçüm kimliği ham HTML'de **bulunamadı**. | 🟡 GSC: kanıt var, veriye erişim yok. GA4: büyük ihtimalle bağlı değil (fox-durum "GA4 bağlantısı Ayhan'da" diyor) | Tip A (etiket) / ÖLÇÜLMEDİ (GSC verisi) |
| **Çok dilli sürümler** | Kayıtta yok | `/en` ve `/ar` aktif, hreflang tanımlı. **AR ana sayfada "HAREKET HİKAYESİ" yerine `1850 ليرة تركية` / `ميزانية` ("1850 TL" / "bütçe") yazıyor**, yani makine çevirisi bozuk. AR'da "Yaklaşan Etkinlikler" başlığı Türkçe kalmış (EN'de doğru: "Upcoming Events" `[Denetmen]`). Sayfa başlıkları (title) üç dilde de Türkçe. | 🔴 **Yeni bulgu.** Global kapı (Kuzey Yıldızı #3) açık ama kırık | Tip A (ham HTML) |
| **Ana sayfa SEO meta** | Kayıtta yok | Title: `Steps On Clouds \| Sen de Adım At protez ampute` · Description: `hareket aracılığıyla ampute bireyleri topluma kazandır. Doğru Protez seni hayata bağlar.` | 🟡 Yeni gözlem. Description protez tedarikçisi gibi konuşuyor, konumlandırmayla (sosyal etki markası) uyuşmuyor | Tip A (metin) · değerlendirme Tip B |
| **Sosyal hesaplar** | ÖLÇÜLMEDİ | ÖLÇÜLMEDİ | — | — |

**Özet:** Ağustos'tan bu yana sitede kasıtlı bir düzeltme görmedim. Kayıt formu dışarıdan bakınca kapanmış görünüyor, ama nedeni büyük ihtimalle Wix'in son kayıt tarihinin geçmesi. Kök neden değişmedi: üretim var, yayın yok. Bu turda dört yeni hata bulundu: tarih çelişkisi, `Ekİbİmİz`, bozuk AR çevirisi ve protez dilindeki meta açıklaması. Denetmen turunda beşincisi eklendi: TR header'da `ınto`.

---

## 2 · GÖRÜNÜRLÜK KONTROLÜ (Tip B, manuel, skor yok)

**Sınır:** Arama aracı ABD lokasyonlu (TR Google SERP'i değil). AI-cevap motorlarının (ChatGPT/Perplexity/AI Overview) cevabını doğrudan sorgulayamadım, bu kısım **ÖLÇÜLMEDİ**. Aşağıdakiler bir web arama motorunun sonuçlarından gözlem.

| Sorgu | SoC göründü mü | Kim görünüyor | Okuma |
|---|---|---|---|
| "Steps On Clouds ampute" | ❌ | Alakasız sonuçlar ("Clouds" şarkıları, dans) | Marka adı tek başına arama motoruna bağlam vermiyor; varlık (entity) sinyali zayıf |
| "\"Steps On Clouds\" Ayhan Erden" | ❌ | Alakasız kişiler | Kurucu ile marka arasında indekslenmiş bir bağ yok |
| "ampute koşu İstanbul etkinlik" | ❌ | Spor İstanbul / İstanbul'u Koşuyorum, Aile Bak. maraton haberi, ampute futbol | Empati Koşusu bu sorguda hiç yok |
| "Empati Koşusu Kadıköy ampute" | ❌ | Kadıköy Bel. "Empati Sahnesi" (eski haberler) | Etkinliğin kendi adıyla bile iz yok. Sitedeki etkinlik sayfaları dahil |
| "engelli bireyler aktif yaşam etkinlik İstanbul sosyal etki markası" | ❌ | Neredeyse tamamı aile.gov.tr il müdürlüğü haberleri + Peugeot "Engelsiz Yaşam" KSS projesi | **Boşluk:** bu kümede STK/marka sesi yok, cevap kamu kurumu bültenlerinden geliyor |
| "amputee socks brand Turkey CloudOne" | ❌ | IOMI (UK), Acquire.com satılık bir ABD markası | CloudOne İngilizce aramada yok |
| "Redlions engelli yelken Marmaris" | — | Medyascope (22 Eki 2026) şampiyona haberi, Fanatik Hüseyin Akbulut etiketi | Redlions basında görünür. Haberde SoC adı geçiyor mu bakamadım (403), **ÖLÇÜLMEDİ** |

**Okuma:** Gözlenen hiçbir sorguda SoC yok. Sorun, **indekslenecek içeriğin olmaması**: 1 blog yazısı, açıklamasız 2 proje, yanlış tarihli 2 etkinlik. Gözlenen tek açık alan "engelli bireyler aktif yaşam" bilgi kümesi; orada cevabı kamu bültenleri veriyor. Redlions ise basında **zaten görünür**, yani SoC'nin elinde bugün olan en güçlü dış kanıt orada.

---

## 3 · 30 GÜNLÜK SPRINT — 5 HAMLE

**Kapı kuralı:** Yayın kapısı açık olmayan hamleye üretim konmaz.

**Kapı envanteri (bugünkü bilgiyle):**
- **Wix Blog:** API ile yayın, Özgür Irmak'ta 60 yazıda kanıtlandı. SoC sitesinde blog API erişimi bu turda **test edilmedi**. Yazmaya başlamadan önce ilk iş bu teyit.
- **Wix Events:** etkinlik durumu Dashboard'dan yönetilir, Editör kanvası gerekmez. Ayhan'ın giriş yapmış tarayıcısı gerekir.
- **Statik sayfa metni / menü / çeviri:** yalnız Editör'den yapılır, yani 4 numaralı karara bağlı.

### GRUP A — Ayhan'ın 4 açık kararına bağlı değil

**A1 · Ölçüm kapısını aç (GSC verisi + GA4)** — *AARRR: tümü (ölçüm zemini)*
- **Ne:** Sitede GSC doğrulama etiketi var. Ayhan GSC'yi kendi hesabıyla açar, mülkü teyit eder, son 3 ayın sorgu/sayfa dışa aktarımını Fox'a verir. GA4'ü Wix panelinden bağlar (Özgür Irmak'taki bekleyen işle aynı adım, birlikte yapılabilir).
- **Sahip:** Ayhan bağlar, Fox/Keşif baseline'ı yazar.
- **Ölçü:** GSC'den T0 baseline tablosu (gösterim/tıklama/sorgu, Tip A) `sablonlar/kanit-ucgeni-olcum-sablonu.md`'ye işlenir. GA4'te ilk 7 günün verisi akar.
- **Kademe:** Hesap bağlama ve erişim Ayhan'ın işi (Kademe 3: erişim paylaşma). Analiz Kademe 1.
- **Ayhan dakikası (tahmin):** ~15 dk.
- **Neden ilk:** Bu olmadan sprint sonunda "ne değişti" sorusu yine Tip B kalır. Ayrıca T+90 kanıtı ancak bugün T0 alınırsa mümkün.

**A2 · Etkinlik yanlışını Dashboard'dan kapat** — *AARRR: Aktivasyon (güven)*
- **Ne:** Wix Events'te iki koşuyu "geçmiş" durumuna çek ya da yaklaşan listesinden kaldır. Yoğurtçu'daki üç tarihi tek tarihe indir. Hangisinin doğru olduğunu Ayhan söyler, Fox seçmez.
- **Mevcut ↔ önerilen:**

| Mevcut (canlı) | Önerilen |
|---|---|
| Ana sayfa + /etkinlikler: "Yaklaşan Etkinlikler" altında 5 Tem + 2 Ağu | Yaklaşan listede geçmiş etkinlik yok. Yaklaşan etkinlik yoksa bölüm boş kalır ya da gizlenir |
| Yoğurtçu: 2 Ağu / 26 Tem / "25 Temmuz" | Tek tarih (Ayhan teyidi) |
| Açıklama metinleri | **Dokunulmaz**, yalnız tarih alanı düzelir |

- **Sahip:** Ayhan giriş yapar, Fox Dashboard'u sürer.
- **Ölçü:** Ana sayfada ve /etkinlikler'de bugünden eski tarihli "yaklaşan" etkinlik sayısı 0. Yoğurtçu sayfasında 1 tarih. Canlıda tekrar ölçülür.
- **Kademe:** 2 (canlı değişiklik, Ayhan onayı).
- **Ayhan dakikası (tahmin):** ~10 dk (giriş + tarih teyidi + onay).
- **Not:** Wix Events'te ayrıca kayıt verisi duruyor (+40 / +6 konuk, kontenjan 75). Blok 1.1'deki "kanıtı kurtar" taraması bu oturumda yapılabilir. Etkinlik sayfasındaki "konuk" rakamı katılımcı sayısı demek değildir, gerçek sayı olarak yazılmaz.

**A3 · Redlions co-marketing: sponsorluğu SoC kanalında görünür kıl** — *AARRR: Edinim + Tavsiye/Topluluk*
- **Ne:** SoC blogunda tek bir yazı: SoC'nin Redlions'a sponsor olması (bugün çorap, gelecek dönem forma) ve takımın **2026 TYF Türkiye Yat Şampiyonası'nda kategori birinciliği**. `[Denetmen]` Kaynak: Ayhan'ın 22 Eki teyidi + çok sayıda basın haberi. Resmi TYF sonuç listesi görülmedi; Medyascope 22 Eki haberi yarış bitmeden (19-23 Eki) yayımlanmış, sonucu tek başına doğrulayamaz. Yazıya girmeden önce resmi sonuç linki eklenmeli. Karşılığında Redlions kanallarında SoC sponsor olarak etiketlenir. Değer/pay mantığı (§11.2): SoC görünürlük ve kanıt alır, takım sponsor görünürlüğü ve içerik alır. Para akışı yok, bedava iş yok, iki taraf da kazanır.
- **Altın kural ve onur kapıları (yazıdan önce, Denetmen'e karşı):**
  - Sporcular **yalnız başarı ve görevleriyle** anılır. "Nasıl oldu", tıbbi geçmiş ve engel türüne dayalı anlatı yok (S16).
  - Keşif görüşmesindeki iki anekdot **yasak** (yayın onayı yok).
  - Ayhan'ın sporcu kimliği yalnız iskele olarak yer alır: "Balon Trim" görevi ve takımın sporcusu olması. Kişisel cümleyi ve ruhu Ayhan yazar, ya da hiç girmez. Bu kararı Ayhan verir.
  - Acıma, ilham, "engellere rağmen" dili yok. Yelken dili, yarış dili var.
  - Onay mercii: Hüseyin Akbulut. S19 (başka paydaş var mı) **hâlâ açık**, yayından önce kapanmalı. `[Denetmen]` Basın haberlerinde takımı destekleyen **Acarkent Rotary Kulübü** adı geçiyor: S19 için somut aday, Hüseyin'e sorulmalı.
- **Sahip:** Metin Yazarı yazar → Denetmen (onur merceği + altın kural) → Ayhan + Hüseyin onayı → Fox Blog API ile yayınlar.
- **Ölçü:** Yazı canlı (URL). Redlions IG'de SoC etiketi (var/yok, Tip A). GSC bağlıysa yazının 30 günlük gösterimi (Tip A). Bağlı değilse ÖLÇÜLMEDİ yazılır.
- **Kademe:** 2 (yayın + üçüncü taraf adına içerik).
- **Ayhan dakikası (tahmin):** ~20 dk (Hüseyin'e sorma + taslak okuma + onay).
- **Bağımlılık notu:** Yazı mağazaya link verirse "satış takımı finanse eder" gibi bir mekanizma iddiası **kurmaz**, çünkü o 1 numaralı karar. Link yalnız ürünü gösterir.

**A4 · GEO bilgi yazısı: "İstanbul'da ampute ve engelli bireyler için aktif yaşam: branşlar ve kulüpler"** — *AARRR: Edinim (AEO/GEO)*
- **Ne:** 2. bölümde gözlenen boşluğa (cevabı kamu bültenlerinin verdiği küme) tek bir soru-cevap yapılı rehber yazı. Kaynaklı listeler: federasyonlar, ampute futbol, paralimpik yelken (Redlions'a doğal bağ), koşu etkinlikleri. Article + FAQPage şeması. Her kulüp ve federasyon adı kendi resmi kaynağından doğrulanır, uydurma yok.
- **Kısıt:** SoC medikal sağlayıcı değil. Tanı, tedavi ve protez önerisi **yok** (YMYL). Yazı yalnız katılım ve erişim rehberi olur.
- **Sahip:** Growth anahtar kelime ve soru havuzunu çıkarır → Metin Yazarı yazar → Denetmen (Verification: her isim/URL) → Ayhan onayı → Blog API ile yayın.
- **Ölçü:** Yazı canlı. 30. günde aynı 5 sorgu tekrar gözlenir (Tip B). GSC varsa sorgu gösterimi (Tip A).
- **Kademe:** 2.
- **Ayhan dakikası (tahmin):** ~10 dk (okuma + onay).

### GRUP B — Ayhan'ın kararlarına bağlı

**B5 · Editör Günü paketi: canlı hataları kapat + ticari kolu aç** — *AARRR: Aktivasyon + Edinim (B2B)*
- **Bağlı kararlar:** **#4 (gün)** her şeyi açar. **#2 (hero)** hero satırını açar. **#3 (ticari kol)** menü ve sayfa satırını açar. **#1 (mağaza)** mağaza metni satırını açar.
- **Kapsam (her satır mevcut ↔ önerilen ile Ayhan'a gösterilir, onaysız dokunulmaz):**

| Mevcut (canlı) | Önerilen | Karar |
|---|---|---|
| Hero `farklılıkları güce çevİr` | Ayhan'ın seçtiği slogan, büyük-İ glyph'i düzgün | #2 + #4 |
| Hakkımızda `Ekİbİmİz` | `EKİBİMİZ` ya da `Ekibimiz` (glyph testinden sonra) | yalnız #4 |
| TR header `take a step ınto the sky` `[Denetmen]` | `take a step into the sky` | yalnız #4 |
| Hakkımızda ekip alanında İngilizce şablon metni (Tip A, ham HTML) | Önce Editör'de varlığı teyit edilir, sonra kaldırılır ya da gerçek metin konur | yalnız #4 |
| AR ana sayfa "1850 TL / bütçe" | Doğru çeviri ya da AR sürümü geçici olarak kapatılır (karar Ayhan'ın) | yalnız #4 |
| EN/AR'da Türkçe başlıklar ve title | Dil başına doğru başlık | yalnız #4 |
| Meta description "Doğru Protez seni hayata bağlar." | Konumlandırmayla uyumlu bir açıklama (Metin Yazarı önerir) | yalnız #4 |
| Menüde ticari kol yok | Tek sayfa, tek CTA (keşif görüşmesi). Stoktaki Faz 4 Ajans copy'si **o günkü konumlandırmaya karşı yeniden denetlenerek** | #3 + #4 |
| Mağaza mekanizma metni | 1 numaralı karara göre kesinleşen cümle | #1 + #4 |

- **Sahip:** Ayhan giriş yapar ve karar verir. Fox Editör'ü sürer. Metin Yazarı yeni satırları yazar, Denetmen denetler.
- **Ölçü:** Ertesi gün canlı yeniden ölçülür. Reddedilmiş varlık sayısı 0, glyph hatası 0, AR "1850 TL" yok, menüde ticari kol var/yok (Tip A).
- **Kademe:** 2.
- **Ayhan dakikası (tahmin):** ~90-120 dk tek oturum. Karar #3 kapanmamışsa ticari kol satırı düşer ve süre ~60 dk'ya iner.

**Sprint'e bilerek alınmayanlar:** e-posta listesi ve lead magnet (ticari kol yokken boş vitrin olur), reklam (ölçüm yok, bütçe Kademe 3), influencer (moda pivotu SoC'nin kendi kanalı değil), Empati Koşusu vaka sayfası (malzeme kurtarılmadan yazılmaz, A2 notuna bakın).

**Toplam Ayhan zamanı (tahmin):** Grup A ~55 dk + Grup B ~90-120 dk.

---

## 4 · AYHAN'IN 4 KARARI (Karar Formülü, sprint'i en çok açan en üstte)

**① Wix Editör oturum günü** *(açık: ~70+ gün)*
- **Talep:** Fox'un Editör'ü süreceği 2 saatlik oturum için bir gün.
- **Bağlam:** Statik sayfa, menü ve çeviri yalnız Editör'den değişiyor. Bu gün olmadan canlıdaki 6 hata ve ticari kol stokta kalır.
- **Seçenekler:** (a) Tek 2 saatlik oturum, sabit gün. (b) 2 × 45 dk: önce hatalar, sonra ticari kol. (c) Ayhan kendisi yapar, Fox adım listesi hazırlar.
- **Öneri:** **(a)**, A2 Dashboard işiyle aynı oturumda. Kararları (#2, #3) oturumdan önce kapatırsak tek seferde biter.
- **Termin:** 14 Kas'a kadar. Neden: sprint ortası. Sonraya kalırsa B5'in ölçümü 4 Ara'dan önce yapılamaz.

**② Hero slogan**
- **Talep:** Reddedilen "farklılıkları güce çevir" yerine canlıya çıkacak cümle.
- **Bağlam:** 10 Haz'dan beri reddedilmiş slogan glyph hatasıyla canlıda. 10 Haz'da hazırlanan alternatifleri dosyalarda bulamadım. Elimdeki tek iskele Branding Faz 3 §2.4: "Farklılığı güce çeviren sosyal etki markası. Her adım bir temsil, her temsil bir kimlik."
- **Seçenekler:** (a) 10 Haz alternatiflerinden biri (Ayhan'da varsa). (b) Metin Yazarı 3 aday üretir, Ayhan seçer. (c) Geçici olarak slogansız hero: yalnız marka tanımı cümlesi ("ampute ve engelli bireylerin aktif yaşamını görünür kılan bir sosyal etki markası"), bu cümle zaten canlıda ve tutarlı.
- **Öneri:** **(c) şimdi, (b) paralel.** Reddedilmiş varlık hemen iner, slogan acele seçilmez.
- **Termin:** Editör gününden 2 gün önce.

**③ Ticari kol kimliği + fiyat**
- **Talep:** Menüdeki adı ("Ajans" mı, "Marka Bulutu OS" mu) ve sayfada fiyat görünüp görünmeyeceği.
- **Bağlam:** Kuzey Yıldızı #1'in kamuya açık tek yüzü bu. Ürün tanımı v0.1 hazır, fiyatlar [AYHAN]. Moda pivotu (20 Haz) ticari kolun öncelikli segmentini değiştirmiş olabilir.
- **Seçenekler:** (a) "Marka Bulutu OS" adı, fiyatsız, tek CTA keşif görüşmesi. (b) "Ajans" adı, alt bölümler: sosyal sorumluluk projeleri / marka büyüme sistemi. (c) Bu sprintte açma, Editör günü yalnız hataları kapatsın.
- **Öneri:** **(a).** Fiyat kararını sayfa açılışından ayırır. Görüşme kapısı fiyatsız da çalışır.
- **Termin:** Editör gününden önce. Kapanmazsa (c) otomatik uygulanır, B5 kısalır.

**④ Mağaza mekanizması** *(açık: 10 Haz'dan beri)*
- **Talep:** CloudOne satışı misyonu "destekler" mi, "finanse eder" mi? (₺550 → ₺700 değişikliği Ayhan'ın kendisi — 3 Kas teyit edildi, bayrak kapandı.)
- **Bağlam:** Canlı metin ikisini de söylemiyor, bu yüzden yanlış da değil. Sprint'te bu kararı bekleyen tek satır mağaza metni. Fiyatın değiştiğini bugün ölçtüm, kimin kararı olduğu bilinmiyor.
- **Seçenekler:** (a) "Destekler": nitel, ölçü yükü yok. (b) "Finanse eder": oran/tutar beyanı ve takibi gerekir (§11.5, uydurma rakam yok). (c) Mevcut cümle kalır, karar ertelenir.
- **Öneri:** **(a).** Bugün ölçülebilir bir finansman akışı yok, "finanse eder" bir rakam vaadine dönüşür.
- **Termin:** Editör günü. En az acil olan karar bu, sprint'in geri kalanını bloklamıyor.

**Sıra önerisi:** ① → ② → ③ → ④. Gerekçe: ① maliyetsiz bir takvim kararı ve tüm statik yayın kapısını açıyor. ② canlıdaki en görünür hata. ③ en büyük stratejik değer ama ertelenirse sprint yine ilerler. ④ hiçbir hamleyi tek başına bloklamıyor.

---

## 5 · GROWTH KATMANI (TZP) — Açık Kararlar / Ölçüm

- **T+90 ölçüm sahibi:** Growth. Metrikler: GSC gösterim/tıklama (A1'den sonra), canlı hata sayısı (B5), Redlions çapraz etiket (A3), 5 sorgu gözlemi (Tip B, tekrar).
- **Taşınan uyarılar:** Redlions altın kuralı ve S16 · S19 onay mercii açık · YMYL (SoC medikal değil) · mevcut içerik varsayılan korunur.
- **Brand-içi çelişki (bilgi için, değişiklik önerilmiyor):** Branding Faz 3 "yalnız değilsin" dilini kara listeye almış. 14 Haz'da Ayhan kararıyla kilitlenen form başlığı "Bize Ulaş, Yalnız Değilsin" idi. `[Denetmen, 3 Kas ham HTML]` Canlı durum farklı: **TR başlık bugün "İlk Adımı Birlikte Atalım"**; "Yalnız değilsin." TR'de yalnız gönderim-sonrası teşekkür mesajında. **EN ("Contact Us, You Are Not Alone") ve AR ("اتصل بنا، أنت لست وحدك") başlıkları hâlâ eski kilitli cümle.** **3 Kas — Ayhan teyit etti: TR başlığı kendisi değiştirdi.** Yeni kilit = "İlk Adımı Birlikte Atalım"; çelişki kapandı (Branding kara listesiyle artık uyumlu). Kalan iş: EN/AR başlıkları yeni cümleye çekilir → B5 Editör günü kapsamına eklendi. Teşekkür mesajındaki "Yalnız değilsin." ayrıca Ayhan'a gösterilecek (mevcut korunur, karar onun).

## Büyüme Hazırlık Durumu (Tip B, niteliksel, skor yok)
SEO Uygulama: **Kritik açık** · Dönüşüm: **Zayıf** (yanlış tarihli etkinlik, ticari CTA yok) · Email & Lead: **Yok** · Kanal: **Zayıf** (blog ölü; Redlions dış kanıt kullanılmıyor) · Ölçüm: **Kritik açık → kısmi** (GSC etiketi var, veri erişimi yok). Ölçüm bekliyor.

## Denetmen'e Hazırlık Notu
Doğrulanması gerekenler: (1) Yoğurtçu tarih çelişkisi ham HTML'de, (2) AR "1850 TL" string'i, (3) ₺700 fiyatı, (4) Medyascope'taki kategori birinciliği ifadesi (403 aldım, arama özetinden geliyor). A3'te altın kural ve onur merceği öncelikli. Dakika rakamlarının hepsi tahmin.

---
*Growth Ajanı · 3 Kas 2026 · Kaynak: canlı site (ham HTML + render), WebSearch (US lokasyonlu), repo dosyaları. Ölçülemeyenler işaretli.*
