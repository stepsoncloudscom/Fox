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

> **v2'de yeniden sıralandı (3 Kas, satış odağı).** Bu bölüm görünürlük sırasıyla korunuyor. Geçerli sıra §6'da. Kısaca: A1 → S1'e katıldı · A2 → Editör günü listesine (güven) · A3 → ikincil, S5'i besler · A4 → park (satışa uzak) · B5 → Editör günü 9 Kas'a sabitlendi, ticari kol satırı park.

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

**① Wix Editör oturum günü** *(açık: ~70+ gün)* — *v2: KAPANDI, Pazartesi 9 Kas (saat açık).*
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

**③ Ticari kol kimliği + fiyat** — *v2: PARK (3 Kas, MBOS/Moda Edisyonu outreach'i park edildi). Editör günü bu satırı açmaz.*
- **Talep:** Menüdeki adı ("Ajans" mı, "Marka Bulutu OS" mu) ve sayfada fiyat görünüp görünmeyeceği.
- **Bağlam:** Kuzey Yıldızı #1'in kamuya açık tek yüzü bu. Ürün tanımı v0.1 hazır, fiyatlar [AYHAN]. Moda pivotu (20 Haz) ticari kolun öncelikli segmentini değiştirmiş olabilir.
- **Seçenekler:** (a) "Marka Bulutu OS" adı, fiyatsız, tek CTA keşif görüşmesi. (b) "Ajans" adı, alt bölümler: sosyal sorumluluk projeleri / marka büyüme sistemi. (c) Bu sprintte açma, Editör günü yalnız hataları kapatsın.
- **Öneri:** **(a).** Fiyat kararını sayfa açılışından ayırır. Görüşme kapısı fiyatsız da çalışır.
- **Termin:** Editör gününden önce. Kapanmazsa (c) otomatik uygulanır, B5 kısalır.

**④ Mağaza mekanizması** *(açık: 10 Haz'dan beri)* — *v2: önceliği yükseldi, §6 Soru 2.*
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

---

## § v2 — Satış Odağı (3 Kas)
*Growth Ajanı · 3 Kas 2026 · Tetik: Ayhan kararı "CloudOne ve markanın geneline odaklanalım" (karar günlüğü, 3 Kas). MBOS / Moda Edisyonu outreach'i park, bu bölüm ona dokunmaz. Pencere: 4 Kas – 4 Ara. Hiçbir şey yayınlanmadı, değiştirilmedi, gönderilmedi.*

> **Temel sınır:** Satış adedi, gelir ve stok **ÖLÇÜLMEDİ**. Wix Stores siparişleri bu turda okunamadı. Aşağıdaki hiçbir hamle "şu kadar satar" demez; her ölçü T0'ı Ayhan'ın vereceği sipariş verisine bağlar (Soru 1).

### 6.1 · Canlıdan okunanlar (3 Kas, ham HTML: `/product-page/cloudone-çorap`, `/en/...`, `/terms-and-conditions`)

| Alan | Canlıda ne var | Kanıt | Satışa etkisi |
|---|---|---|---|
| Fiyat | ₺700,00, indirim yok | Tip A | Teyitli (Ayhan) |
| **Ürün SEO açıklaması** | `"… sosyal etki için tasarlandı. 550 TL."` TR **ve** EN sayfada | Tip A | 🔴 Google/AI sonucunda eski fiyat görünür. Sitede 700, aramada 550 |
| **Ala hang tag** | Tasarımda **600 TL** (`ala-materyaller/_review/1_hang_tag_p1.png`) | Tip A (dosya, Denetmen PNG'ye baktı) · basılıp basılmadığı ÖLÇÜLMEDİ · 600, 6 Haz brief'inde konmuş (`ala-skateboards-fiziksel-materyal-brief.md:14`; site o gün 550) — kimin kararı olduğu kayıtsız | 🔴 Dolaşımda üç fiyat olabilir: 550 / 600 / 700 |
| Ürün açıklaması | 3 cümle. Misyon bağı: "Steps On Clouds misyonunun somut parçası: hareket kültürü, görünürlük, sosyal etki." Mekanizma yok | Tip A | Karar #4'ü bekliyor |
| Ürün detayı | One size 38-44 · Pamuk %80, Poliamid %18, Elastan %2 | Tip A | ✅ var |
| Kargo | "2-3 iş günü içinde kargoya" + takip e-postası. **Kargo ücreti ürün sayfasında yok.** Yurt dışı gönderim bilgisi yok | Tip A · ödeme adımı test edilmedi, ücret ÖLÇÜLMEDİ | 🟡 Sepette sürpriz maliyet riski |
| İade | Ürün sayfası: **15 gün**, kullanılmamış/ambalajı açılmamış. Şartlar sayfası: **"yedi gün içerisinde … cayma hakkı"** ve "genel iade süresi 7 gündür" | Tip A | 🔴 İki sayfa birbirini tutmuyor. Yasal süreye uygunluğu Fox değerlendirmez, avukata/Ayhan'a gider. `[Denetmen, 3 Kas ham HTML]` Şartlar sayfası doldurulmamış şablon: "Kargo Ücreti : … -TL", "Toplam Satış Bedeli : …. -TL", sipariş tarihi "../../….", satıcı adı "……………" boş |
| Stok | `isTrackingInventory: false`, `quantity: 0`, durum "in_stock" | Tip A | 🟡 Stok takip kapalı: site eldeki adedi bilmiyor, yılbaşında fazla satış riski |
| Görseller | **2** görsel (ürün `media` dizisi, TR+EN), ikisinde de `altText: null`; sayfa yedek olarak ürün adını ("CloudOne Çorap") alt diye basıyor. Ürün dosyasında 10 çekim var (`soc-urun-cloudone.md`) | Tip A | 🟡 8 kare kullanılmıyor, görsel arama için tanımlayıcı alt metin yok |
| Sosyal kanıt | Sayfada yorum/puan bölümü görünmüyor | Tip A (görünür metin) | 🟡 Tek güven sinyali iade/kargo metni |
| EN sayfa | Title ve meta Türkçe, açıklama farklı ve eski copy ("summer and winter"), fiyat yalnız ₺ | Tip A | 🟡 Global kapı açık ama yarım |
| Breadcrumb | TR sayfada "All Products" | Tip A | ⚪ küçük |
| Ödeme yöntemleri | — | ÖLÇÜLMEDİ (ödeme adımı açılmadı, sipariş verilmedi) | Editör gününde Ayhan'la bakılır |

### 6.2 · 5 SATIŞ HAMLESİ (4 Kas – 4 Ara)

Sıra mantığı: önce ölç, sonra fiyatı tekleştir, sonra dışarı çık. Fiyat üç yerde farklıyken B2B'ye gitmek ya da sezona girmek kendi kendini yalanlamak olur. **Yürütme sırası: S1 → S2 → S3 → S4 → S5** (numara = sıra; aşağıda B2C/B2B başlığına göre gruplu).

**B2C — mağaza dönüşümü**

**S1 · Sipariş + stok T0'ı al, stok takibini aç** — *AARRR: tümü (ölçüm zemini) · eski A1'i kapsar*
- **Ne:** Ayhan Wix Stores'tan sipariş listesini (tarih, adet, tutar; kişisel veri olmadan) dışa aktarır ve eldeki çift sayısını söyler. Stok takibi o sayıyla açılır. GA4 bağlantısı (A1) aynı oturumda.
- **Sahip:** Ayhan veri verir · Fox T0 tablosunu `sablonlar/kanit-ucgeni-olcum-sablonu.md`'ye işler.
- **Ölçü (Tip A):** Haziran'dan bugüne aylık sipariş adedi + tutar = T0. Stok sayısı canlıda takipli. 4 Ara'da aynı dışa aktarım tekrarlanır.
- **Kademe:** Veri paylaşımı ve stok açma Ayhan (2). Analiz 1.
- **Ayhan dakikası (tahmin):** ~15 dk.

**S2 · Ürün sayfası güven paketi: tek fiyat, tutarlı iade, görünür kargo** — *AARRR: Aktivasyon (dönüşüm) · Editör günü 9 Kas*
- **Mevcut ↔ önerilen** (onaysız dokunulmaz; çoğu Wix Stores panelinden, Editör kanvası gerekmez):

| Mevcut (canlı) | Önerilen | Bağlı |
|---|---|---|
| SEO açıklaması "… 550 TL." (TR+EN) | Fiyatsız açıklama (fiyat değişince yine eskimesin). Metni Metin Yazarı yazar | — |
| İade 15 gün (ürün) / 7 gün (şartlar) | Tek süre, iki sayfada aynı. Hangisi olacağı Ayhan + avukat | Soru 5 |
| Kargo ücreti sayfada yok | Ücret (ya da "ücretsiz") ve yurt dışı gönderim var/yok tek satır | Soru 5 |
| 2 görsel, alt metin alanı boş | 10 çekimden ürün dosyasının önerdiği #1, #2, #3, #5 + alt metin | — |
| Misyon cümlesi mekanizmasız | Karar #4'e göre tek cümle. "Finanse eder" seçilirse oran/tutar beyanı şart (§11.5) | Soru 2 |
| EN title/meta Türkçe, eski açıklama | EN açıklama TR'nin çevirisi, EN title/meta | — |
| "All Products" | "Tüm Ürünler" | — |

- **Sahip:** Fox paneli sürer (Ayhan girişli) · Metin Yazarı yeni satırlar · Denetmen.
- **Ölçü (Tip A):** Ertesi gün ham HTML'de "550" yok, iki sayfada aynı iade süresi, kargo satırı var, alt metin dolu görsel sayısı. Dönüşüm etkisi: S1 T0'ına karşı 4 Ara siparişleri (az veriyle yön okunur, oran iddia edilmez).
- **Kademe:** 2.
- **Ayhan dakikası (tahmin):** ~30 dk (Editör gününün içinde).

**S5 · Hediye sezonu: indirimsiz, gerçek tarihli** — *AARRR: Edinim + Gelir · 16 Kas'tan itibaren, S2 bittikten sonra*
- **Değer tartısı:** Kasım sonu indirim dönemi (Efsane Cuma vb.) **önerilmiyor.** Fiyat 25 Ağu ile 3 Kas arasında 550'den 700'e çıktı (değişiklik tarihi kayıtsız), indirim bunu geri alır ve "asıl fiyat bu değil" der; moda paketi de indirim kültürünü kalıcı hasar sayıyor. Kıtlık dili de yok: stok takibi bugün kapalı, "son X çift" iddiası doğrulanamaz.
- **Ne (önerilen):** Tek gerçek bilgi: "Yılbaşına yetişmesi için son sipariş: [tarih]". Tarihi Ayhan kargo süresine göre koyar (sitedeki "2-3 iş günü" + bölge farkı). Ürün sayfasında tek satır + Instagram'da (@stepsoncloudscom) 2-3 paylaşım, ürün linki UTM'li. Redlions sponsorluk yazısı (eski A3) yayımlanırsa ürüne düz link verir, mekanizma iddiası kurmaz.
- **Onur kapısı:** Hediye anlatısı ürün ve hareket üzerinden. "Bir ampute için al", "anlamlı hediye ver, hayat değiştir" tipi acıma/kurtarıcı dili yok.
- **Sahip:** Metin Yazarı paylaşım metinleri · İçerik görsel (mevcut 10 çekimden) · Denetmen · Ayhan yayınlar.
- **Ölçü (Tip A):** 16 Kas – son sipariş tarihi arası sipariş adedi (S1'deki T0'a karşı) + UTM'li linkten gelen oturum (GA4 bağlıysa; değilse ÖLÇÜLMEDİ).
- **Kademe:** 2 (yayın).
- **Ayhan dakikası (tahmin):** ~20 dk (tarih + onay + yayın).

**B2B — satış noktaları**

**S3 · Ala / House of Superstep: durumu öğren, fiyatı tekleştir** — *AARRR: Gelir + Tavsiye/Topluluk*
- **Bilinen:** 4 Haz modeli: ödeme/komisyon yok, Tuncay bedelsiz alan veriyor, karşılık ortak içerik (amputasyon × kaykay). 4 materyal 6 Haz'da baskıya hazırlandı (brief'te baskı tarihi 9 Haz). Baskı, raf ve satış **kayıtsız**, mailde iz yok. Etiketteki fiyat 600 TL.
- **Ne:** Ayhan Tuncay'a tek mesaj atar (taslak aşağıda): rafta ne var, alan/soran oldu mu, etiket basıldıysa fiyat. Cevaba göre: basıldıysa etiket fiyatı canlıya çekilir (yeniden üretim `sablonlar/ala-print-materyaller.py` ile tekrar edilebilir, baskı maliyeti Ayhan kararı); basılmadıysa 700 ile basılır.
- **Sahip:** Ayhan gönderir · Fox cevabı kayda işler (`fox-iliski-hafizasi.md`, Notion panosu Ayhan onayıyla).
- **Ölçü (Tip A):** Raf durumu var/yok, alandaki çift sayısı, alandan satış adedi (Tuncay'ın beyanı, kaynağı yazılarak). Etiket fiyatı = site fiyatı.
- **Kademe:** 2 (mesaj).
- **Ayhan dakikası (tahmin):** ~10 dk.

**S4 · Wunder: tek nazik takip, sonra kapat** — *AARRR: Gelir (B2B edinim)*
- **Bilinen:** 24 Haz soğuk mail (info@wunder.com.tr), tek mesaj, cevap yok (~19 hafta). Wunder indirim-yoğun çalışıyor (ilişki hafızası bayrağı).
- **Ne:** Tek takip maili (taslak aşağıda). 10 iş günü içinde cevap yoksa kanal kapanır, üçüncü mail yok (§11.10, başarısız kanalı tekrar etme). Cevap gelirse ilk görüşmeden önce toptan fiyat ve koşul Ayhan'dan gelmiş olmalı (Soru 4). Mağaza tarafının indirim beklentisinde 700 konumu korunur.
- **Sahip:** Ayhan gönderir · Fox takip tarihini tutar.
- **Ölçü (Tip A):** Cevap var/yok (Gmail), görüşme var/yok, ilk sipariş adedi.
- **Kademe:** 2.
- **Ayhan dakikası (tahmin):** ~5 dk gönderim (+ cevap gelirse ayrı).

**Yeni satış noktası adayları — bu turda doğrulanmış aday yok.**
- Arama (US lokasyonlu araç) Time Out İstanbul'da **Outrunner**'ı (Beşiktaş, Çırağan Cad.) koşu odaklı uzman mağaza olarak listeliyor ve Ortaköy Run Club'ın her perşembe orada başladığını söylüyor. Mağazanın kendi sitesi (outrunner.com.tr) JS ile yükleniyor, ham HTML'den **çorap kategorisi okunamadı**. Time Out sayfasının tarihi bilinmiyor. **Statü: doğrulanmamış aday**, segment teyidi olmadan temas önerilmez.
- Önerilen eleme ölçütü (Wunder emsali): çok markalı, çorap/aksesuar kategorisi sitede görünür, koşu/kaykay/outdoor topluluğu olan, indirim kampanyası ana iletişimi olmayan mağaza. Ayhan'ın bildiği bir isim varsa önce o (Soru 6).
- Bilerek önerilmeyen: kurumsal hediye satışı. Redlions sponsor ağı veya Rotary gibi kanallar altın kural ve çıkar çatışması bayrağı (Ayhan takımın sporcusu) kapanmadan satış kanalı olarak kullanılmaz.

### 6.3 · Editör Günü — Pazartesi 9 Kas (satışı etkileyen kalemler önde)

| Sıra | Kalem | Yer | Bağlı |
|---|---|---|---|
| 1 | Stok sayısı gir, takibi aç (S1) | Stores paneli | Soru 1 |
| 2 | Ürün SEO açıklamasından "550 TL"yi çıkar (S2) | Stores → ürün SEO | — |
| 3 | İade süresini iki sayfada tekleştir (S2) | Ürün info bölümü + Şartlar sayfası | Soru 5 |
| 4 | Kargo ücreti / yurt dışı satırı (S2) | Ürün info bölümü | Soru 5 |
| 5 | Mekanizma cümlesi (S2) | Ürün açıklaması | Soru 2 |
| 6 | Görsel + alt metin, EN title/meta/açıklama, "Tüm Ürünler" (S2) | Stores paneli + çeviri | — |
| 7 | Ödeme adımını Ayhan'la birlikte gör (ödeme yöntemi, kargo ücreti), sipariş verilmez | Canlı site | — |
| 8 | Eski B5 listesi: hero, `Ekİbİmİz`, `ınto`, şablon metni, AR "1850 TL", EN/AR form başlığı, ana sayfa meta, etkinlik tarihleri (A2) | Editör + Events paneli | Karar ② |
| — | ~~Ticari kol menü/sayfa~~ | — | **park** |

**Ayhan dakikası (tahmin):** satış kalemleri (1-7) ~45 dk · eski B5 kalemleri ~60 dk · toplam ~1 sa 45 dk. Zaman yetmezse 1-7 önce.

### 6.4 · TASLAK mesajlar — Ayhan gönderir

**TASLAK — Ayhan gönderir · Wunder (info@wunder.com.tr), mevcut thread'e yanıt olarak**
> Konu: (thread'in mevcut konusu, "Re:" ile)
>
> Merhaba,
>
> 24 Haziran'da Steps On Clouds'un CloudOne çorabı için yazmıştım. Ulaşmadıysa ya da o dönem gündeminizde değildiyse, kısaca tekrar hatırlatmak istedim.
>
> CloudOne beyaz, uzun konçlu bir atletik çorap. Pamuk %80, poliamid %18, elastan %2. Tek beden, 38-44. Sitede ₺700'den satılıyor.
>
> Uygunsa mağazaya örnek bir çift bırakabilirim, ekibiniz elde görsün. Uygun değilse de bir satırlık cevap yeterli, tekrar yazmam.
>
> Ayhan Erden
> Steps On Clouds
> stepsonclouds.com

*Not: "örnek çift bırakırım" bir taahhüt. Ayhan istemezse o cümle çıkar. Fiyat yalnız perakende (canlıdaki) fiyat; toptan rakam yok. `[Denetmen]` Göndermeden önce 24 Haz mailinde fiyat yazıp yazmadığına bakılır: yazdıysa (550) takipteki 700 açıklamasız bir zam gibi okunur.* `[Fox, 3 Kas — Gmail'den okundu]` 24 Haz mailinde fiyat YOK (ürün tanımı + numune teklifi var). Koşul kapandı; takipteki ₺700 zam gibi okunmaz.

**TASLAK — Ayhan gönderir · Tuncay Kocal (WhatsApp/mesaj)**
> Tuncay merhaba, nasılsın?
>
> Haziran'da çorap için hang tag, raf kartı, poster ve QR kart tasarlamıştık. Alanda şu an durum ne? Çorap rafa çıktı mı, soran ya da alan oldu mu?
>
> Bir de etiketler basılıp rafa kondu mu? Fiyatı güncellemem gerekebilir, ona göre ben bakarım.
>
> Kaykay videosunu da konuşalım, müsait olduğun bir gün söylersin.
>
> Ayhan

*Sözdizimi taraması (`sozdizim_tarama.py`, 3 Kas):* iki taslak da aracın ölçüm alt sınırının (60 kelime / 5 cümle, 8+ kelimelik paragraf) altında kaldı, araç **ölçmedi** (çıkış 0, bulgu yok). "Temiz" sayılmaz; kulak kontrolü Denetmen'de.

*`[Denetmen, 3 Kas]` Kulak kontrolü yapıldı: karşıtlık kalıbı, aforizma, övgü, uydurma rakam yok. Değişenler: Wunder'de "uygun" üç kez tekrarlanıyordu (biri "gündeminizde" oldu), "bir örnek çifti" düzeltildi, thread içi yanıtta yeni konu satırı çıkarıldı. Tuncay'da fiyat cümlesi Soru 3 kapanmadan 700'ü ilan ediyor ve düzeltmeyi bedelsiz alan veren Tuncay'la paylaştırıyordu ("birlikte düzeltelim"); yalnız soruya indirildi, iş Ayhan'da kaldı. "takvimine bakarsın" emir kipi gibi okunuyordu.*

### 6.5 · AYHAN'A SORULAR (Karar Formülü, tek liste, satışı en çok açan en üstte)

**1 · Sipariş ve stok verisi**
- **Talep:** Haziran'dan bugüne CloudOne sipariş listesi (tarih, adet, tutar) ve eldeki çift sayısı.
- **Bağlam:** Bu olmadan hiçbir satış hamlesinin etkisi ölçülemez. Site stok takibi kapalı, adedi bilmiyor.
- **Seçenekler:** (a) Wix Stores dışa aktarımı + stok sayısı. (b) Yalnız toplam adet + stok, yaklaşık. (c) Editör gününde birlikte panelden okuruz.
- **Öneri:** (a). Kişisel veri sütunları olmadan.
- **Termin:** 9 Kas'tan önce. Stok takibi o gün açılacak.

**2 · Mağaza mekanizması: "destekler" mi, "finanse eder" mi** *(10 Haz'dan beri açık)*
- **Talep:** Ürün sayfasındaki misyon cümlesinin fiili.
- **Bağlam:** Satış copy'sinin tek açık satırı; hediye sezonu metni de buna bağlı.
- **Seçenekler:** (a) "Destekler", nitel. (b) "Finanse eder" + açık oran/tutar ve takibi. (c) Bugünkü cümle kalır.
- **Öneri:** (a). Bugün ölçülen bir finansman akışı yok; (b) bir rakam vaadine dönüşür.
- **Termin:** 9 Kas.

**3 · Tek fiyat**
- **Talep:** ₺700 her kanalda tek fiyat mı? Ala etiketleri (600 TL) basıldı mı?
- **Bağlam:** Arama sonucunda 550, etikette 600, sitede 700 görünebiliyor.
- **Seçenekler:** (a) 700 her yerde, etiket yeniden basılır. (b) Mağaza içi farklı fiyat bilinçli bir karar (gerekçesi yazılır). (c) Etiketten fiyat kaldırılır, rafta ayrı fiyat kartı.
- **Öneri:** (a), etiket basılmadıysa maliyeti yok. Basıldıysa (c) daha ucuz olabilir; maliyet Ayhan'da.
- **Termin:** Tuncay'ın cevabıyla birlikte.

**4 · B2B koşulları** *(Wunder cevap verirse gerekli)*
- **Talep:** Toptan fiyat ya da konsinye/komisyon tercihi, asgari adet.
- **Bağlam:** Fox rakam koymaz (§11.5). Cevap gelince masaya boş gidilmesin.
- **Seçenekler:** (a) Toptan satış (sabit birim fiyat). (b) Konsinye (satılan kadar). (c) Önce yalnız örnek, koşul görüşmede.
- **Öneri:** Karar Ayhan'ın; Fox yalnız şunu işaretler: indirim-yoğun bir mağazada perakende 700'ün korunması koşula yazılmalı.
- **Termin:** Wunder takibi gönderilmeden önce.

**5 · İade süresi ve kargo**
- **Talep:** İade süresi (ürün sayfası 15 gün, şartlar 7 gün) ve kargo ücreti / yurt dışı gönderim.
- **Bağlam:** İki sayfa çelişiyor. Yasal sürelere uygunluk avukat konusu, Fox değerlendirmez. `[Denetmen]` Avukata gidecek olgu: Şartlar'daki "yedi gün" ve "385 sayılı VUK genel tebliği" atfı eski (2014 öncesi) şablon diline benziyor; güncel Mesafeli Sözleşmeler Yönetmeliği cayma süresini 14 gün sayıyor (teyit avukatta). Şartlar'da kargo ücreti, satıcı adı ve tarih alanları boş.
- **Seçenekler:** (a) Avukata tek soru, sonra iki sayfa birlikte düzelir. (b) Ayhan şimdilik daha uzun olan süreyi iki sayfaya yazar, avukat sonra bakar. (c) Bekler.
- **Öneri:** (b) + (a). Uzun süre müşteri lehine, çelişki 9 Kas'ta kapanır.
- **Termin:** 9 Kas.

**6 · Gönderim onayları ve aday**
- **Talep:** Wunder takibi ve Tuncay mesajı gönderilsin mi (taslaklar §6.4)? Aklında yeni bir satış noktası var mı?
- **Bağlam:** Doğrulanmış yeni aday yok; Outrunner yalnız ikincil kaynaktan.
- **Seçenekler:** (a) İkisi de bu hafta. (b) Önce Tuncay, Wunder fiyat kararı (Soru 3-4) sonrası. (c) Bekler.
- **Öneri:** (b). Fiyat tekleşmeden Wunder'a fiyat yazmak riskli.
- **Termin:** Tuncay 6 Kas'a kadar; Wunder Soru 3-4 kapanınca.

### 6.6 · Emin olamadıklarım
- Sipariş sayısı, stok, gelir: hiçbiri bilinmiyor. "Satış az" ya da "çok" demiyorum.
- Ala materyalleri basıldı mı, çorap alanda mı, satış oldu mu: kayıt yok.
- Kargo ücreti ve ödeme yöntemleri: ödeme adımı açılmadı.
- SEO açıklamasındaki "550 TL"nin Google sonucunda bugün nasıl göründüğü: SERP'e bakmadım (araç US lokasyonlu).
- İade süresinin yasal uygunluğu: avukat konusu.
- Outrunner'ın çorap satıp satmadığı ve Time Out bilgisinin güncelliği.
- Redlions'ta takımın CloudOne giyip giymediği: kayıtta yok, içerikte kullanılmadı.

### 6.7 · TZP — Growth katmanı güncellemesi
- **Üretilen:** S1-S5 (AARRR etiketli), Editör günü satış listesi, 2 taslak mesaj.
- **Açık kararlar:** Soru 1-6.
- **T+90 ölçümü (Growth):** S1 T0'ına karşı sipariş adedi + tutar (Tip A, Wix Stores); alan satışları (Tuncay beyanı, kaynaklı); Wunder sonucu (var/yok).
- **Taşınan uyarılar:** Redlions altın kuralı + çıkar çatışması bayrağı (satış kanalı olarak kullanılmaz) · indirim/kıtlık dili yok · "protez uyumlu" ifadesi yasak (10 Haz) · MBOS park.

### Denetmen'e Hazırlık Notu (v2)
Doğrulanacaklar: (1) ürün sayfası ve EN sayfada SEO açıklamasındaki "550 TL", (2) iade 15 gün / şartlar 7 gün, (3) `isTrackingInventory: false`, (4) hang tag PNG'sindeki 600 TL. Özellikle bakılacak: S5'in değer tartısı (indirim/kıtlık reddi yeterli mi), Wunder taslağındaki "örnek çift" taahhüdü, Tuncay mesajının ilişki tonuna uygunluğu. Dakikaların hepsi tahmin.
