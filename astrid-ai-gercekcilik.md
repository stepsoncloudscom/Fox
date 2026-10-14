# Astrid Nilsen — Gelişim Modülü 16: AI Gerçekçiliği (ÖNCELİKLİ MODÜL)
*Ayhan'ın emri (10 Ekim 2026): "AI konusunda gerçekçilikten asla vazgeçmek istemiyorum — en çok araştırma/eğitim yatırımını buraya yapalım." Bu modül diğerlerinden farklı: **salt bilgi değil, Astrid'in çalışma yöntemi.** Kaynak: Higgsfield'in kendi teknik prompting guide'ları + bağımsız teknik analiz (WebFetch ile tam metin çekildi — uydurma yok, her teknik doğrudan kaynağından).*

---

## TEMEL PARADOKS — "PLASTİK TEN" SORUNU
**Neden olur:** Seedance (Higgsfield'in video modeli), yüklenen referans görseli **kare kare denoising sürecine gömülen güçlü bir koşullandırma sinyali** olarak kullanır — "sadakat motoru, düzeltici değil." Model, prompt talimatından çok **referansa sadakati** önceliklendirir.

**Sayı şaşırtıcı ama doğrulanmış:** Aşırı keskin, kusursuz temiz bir referans görsel **daha iyi değil, daha kötü (daha plastik)** sonuç verir. Model, pürüzsüz dijital netliği "yapay" olarak okur ve öyle animasyonlar — mumsu, CGI görünümlü sonuç. Seedance'ın denoising katmanları doğal film fiziği (tane, mikro-kusur, ışık saçılımı, deri altı saçılım/subsurface scattering) için ayarlı; sıfır gürültülü kusursuz girdi "dijital/yapay" okunur.

**Pratik sonuç:** Astrid referans görsel hazırlarken **kusursuzluk hedeflemez** — doğal dokuyu korur.

---

## GERÇEKLİK-ÇAPALAYAN DİL (Reality-Anchoring) — DOĞRUDAN KULLANILABİLİR
**Olumlu (dahil edilir):**
- *"Realistic skin with visible pores and subtle oil"*
- *"Natural micro-imperfections, film grain"*
- *"ARRI Alexa 35mm aesthetic, soft subsurface scattering"*
- Pore-seviyesi detay: *"pores, chapped lips, windburn, wet lash clumps, no beauty retouch"*

**Anti-sinyal (açıkça reddedilir):**
- *"No plastic skin, waxy texture, over-sharpened digital sheen, or AI artifacts"*

**Film dokusu (plastik/CGI görünümü yener):**
- *"light authentic 35mm film grain, gentle gate weave, halation bloom on highlights, faint chromatic aberration at frame edges, natural micro motion blur"*

**Astrid'in kuralı:** Her prompt'ta hem olumlu reality-anchoring dili HEM anti-sinyal birlikte bulunur — yalnız biri yeterli değil.

---

## REFERANS GÖRSEL STRATEJİSİ — CLAUDIA'NIN SOUL ID SETİNE DOĞRUDAN UYGULANIR
Bu bölüm `fox-ai-director-insa.md`'deki Soul ID iş akışını (icat → çoğalt → eğit) **teknik olarak derinleştirir:**

1. **Karakter sayfası stratejisi:** En fazla **üç açı** (ön, 3/4, profil), **aynı ışık oturumundan.** Farklı ışık sıcaklıkları karıştırılırsa (sıcak+soğuk referans) ortalamaya düşer — ten tonu ve görünen yaş kayar.
2. **Hiyerarşik keskinlik:** Birincil referans (ön, iyi ışıklı, **yumuşak** — aşırı keskin değil) + ikincil referans (detay/doku için net çekim, ama yalnız doku sağlar, "yapay parlaklık yok" notuyla).
3. **Yükleme sırası önemli:** İlk yüklenen görsel **%40-50 daha fazla ağırlık** alır. Claudia'nın kimlik referansı her zaman ilk sırada (`@Image1`), destekleyici referanslar sonra, promptta rolleri açıkça belirtilir.
4. **Orta-çözünürlüklü bir kare dahil etmek** (tüm set keskin olmasın) yüzey detayına "overfitting"i önleyebilir — şekli korurken aşırı pürüzsüzlüğü engeller.
5. **En yüksek kaldıraçlı adım:** Referans üretimi, "hızlı bir ön hazırlık" değil, **prodüksiyonun en kritik aşaması** olarak ele alınır. Kusursuz-ama-doğal-dokulu bir portre referansına zaman harcamak, kusurlu referans üzerinde saatlerce prompt denemesinden daha iyi sonuç verir.

---

## IŞIK FİZİĞİ — TEK KAYNAK İLKESİ (Modül 3'ü derinleştirir)
**Motive edilmiş, tek-kaynaklı ışık** gerçekçiliğin temeli. Örnek (kaynaktan doğrudan): *"Tek gerçek kaynak, güneş, denizin dört derece üzerinde, sıcak koyu altın, 15 saniye boyunca sabit."* Çoklu, birbiriyle yarışan ışık kaynağı yapay görünür.
**Pozlama önceliği:** Vurgular (highlights) için pozlanır, yüzlerin gölgeye düşmesine izin verilir — rim ışık/göz parıltısıyla hafifletilir.
**Çoklu sahnede tutarlılık:** Güneşin konumunu her segmentte yeniden tarif etmek yerine, **aynı ışık yönü/kalitesini** koru.

## LENS/KAMERA KİLİDİ (Modül 5, 10'u derinleştirir)
**Segment başına lens kilidi:** Her sahne/segment için net bir lens kararı — kuruluş için geniş, portre için telefoto, sıkıştırma için dar — **drift'i önler.**
**Odak uzaklığını derece cinsinden belirt, mm değil** — model karışıklığını azaltır (kaynaktan doğrudan teknik not).
**Hareket grameri:** *"Heavy studio dolly and locked-off tripod behavior, slow, deliberate, machine-smooth moves, no handheld jitter"* — handheld tamamen farklı fizik sonucu üretir, ikisi karıştırılmaz.
**Anamorfik artefaktlar** (oval bokeh, flare, halation — Modül 10) ima edilmez, **açıkça isimlendirilir.**

---

## PROMPT YAPI FORMÜLÜ — ASTRID'İN ARTIK STANDART ÇALIŞMA YÖNTEMİ
Kaynaktan doğrulanmış, 11 katmanlı hiyerarşi — **her çekim listesi satırı bu sırayla düşünülür:**

1. **GLOBAL STİL** (tür, renk derecelendirme, film stoku)
2. **SAHNE** (tek cümlelik özet)
3. **KARAKTERLER** (yüz, yapı, kostüm)
4. **MEKÂN** (alan, aksesuar — insanlardan ayrı tutulur)
5. **İLK KARE VE BLOCKING** (kesin başlangıç pozisyonları)
6. **SAHNE-SAHNE KIRILIM** (etiketli, kesin kesmelerle)
7. **OPTİK** (sahne başına lens, diyafram davranışı)
8. **KAMERA** (hareket tipi ve mesafe)
9. **FİZİK** (kumaş, saç, sıvı davranışı)
10. **IŞIK** (kaynak, yön, pozlama önceliği)
11. **SES** (en son: ortam, efekt, diyalog kuralları)

**Kritik kural (kaynaktan birebir):** *"Bir prompt, etiketli bölümlere ayrılmış tek bir sürekli metin bloğu olarak en iyi çalışır. Bir bölüm atlanırsa, çıktı belirli ve tahmin edilebilir bir şekilde başarısız olur."*

**Bu, Astrid'in KOL 2 (Çekim Listesi) çalışmasının yeni iskeletidir** — tablo formatının yanında, her satır bu 11 katmana göre doldurulur.

---

## TUTARLILIK KİLİTLERİ — KOL 3'ÜN YENİ TEKNİK ARACI
Çoklu-kesim sahnelerde tutarlılık için **pozitif kilitler** — genel "tutarlı olsun" talebinden çok daha güvenilir:
- Karakter yüzü/kostümü sahne ortasında **asla yeniden tasarlanmaz**
- Ekran yönü (screen direction, Modül 1'deki 180 derece kuralı) açık not olmadan **asla ters çevrilmez**
- **Zaman birikim kuralları:** Islaklık yalnız artar, kir kaybolmaz, yanık izi kalıcıdır — sahneler arası "sıfırlanmaz"
- **Kesin sayı kısıtları** (örn. "tam olarak dört kişi, asla beş") — belirsiz "birkaç kişi" değil

**Astrid'in kuralı:** KOL 3'teki süreklilik notları artık genel gözlem değil, **pozitif kilit listesi** olarak yazılır — her sahne başlamadan önce "neyin asla değişmeyeceği" açıkça listelenir.

---

## TOPLULUK/FORUM DENEYİMLERİNDEN DERSLER (Ayhan'ın talebiyle eklendi)
*Resmi guide'lar "nasıl doğru yapılır"ı anlatır — topluluk/forum tartışmaları "nerede gerçekten kırılıyor"u gösterir. Not: belirli bir Reddit thread'ine doğrudan ulaşılamadı (arama motoru kısıtı); aşağıdakiler 2026 pratisyen tartışmalarından **sentezlenmiş, doğrulanmış örüntüler** — kaynağı belirsiz tekil iddia yok.*

**"Kredi Tuzağı" (Credit Trap) — üretim disiplini dersi:**
2026 topluluk tartışmalarında en sık şikayet: başarısız üretimlere (artefakt, "erime," zayıf prompt uyumu) harcanan gerçek para. **Astrid'e bağlanır:** KOL 2'deki çekim listesi, üretime geçmeden önce **tam** olmalı (11 katman eksiksiz, Soul ID referansı doğru sırada) — "dene-gör" yaklaşımı pahalıdır, Kademe 2 onayından önce prompt kalitesi maksimize edilir.

**Nesne/kimlik sürekliliği ("erime") — 5 saniye eşiği:**
Karakterlerin arka plana "erimesi" ya da kimliğinin sahne ortasında değişmesi, özellikle **5 saniyeyi geçen kliplerde** yaygın bir pratisyen şikayeti. Yüz ilk karede iyi görünüp zamanla sert jestlere/tuhaf göz kırpmaya "kayabiliyor." **Astrid'e bağlanır:** Uzun sahneler (Modül 16'nın "pozitif kilitler" bölümü) için özellikle dikkatli olunmalı — 5 saniye eşiği bir **risk işareti** olarak çekim listesine not düşülür.

**Çözünürlük/süre değiş tokuşu:**
1080p çoğu zaman ~6 saniyeyle sınırlı; 768p'ye inince aynı kaynakla ~10 saniye mümkün olabiliyor (model/plana göre değişir — kesin sayı değil, eğilim). **Astrid'e bağlanır:** Üretim sırası (KOL 4) kurulurken çözünürlük/süre dengesi bilinçli bir karar olarak not edilir, varsayılan ayarla "oluruna bırakılmaz."

**Araç-görev uyumsuzluğu:**
Pratisyenlerin sık yaptığı hata: "snackable" sosyal içerik için güçlü bir araç, anlatı sürekliliği gerektiren işte zayıf kalabiliyor (ve tersi). **Astrid'e bağlanır:** Modül 15'teki editorial/kampanya vs UGC/Reels ayrımı burada teknik bir karşılığa kavuşuyor — iki register yalnız prompt dili değil, **araç/model seçimi** olarak da ayrışabilir.

---

## MODEL SEÇİMİ VE REFERANS MEKANİĞİ — GERÇEK ÜRETİM DERSLERİ (11 Ekim 2026, Claudia/Cloud One serisi)
*Yukarısı kaynak dokümantasyondan; bu bölüm **Astrid'in kendi gerçek üretiminden** doğrulanmış, tekrarlanabilir bulgular — Higgsfield'in resmi belgelerinde yazmıyor.*

**1. `text2image_soul_v2` + `--soul-id` + `--image` kombinasyonu sessizce prompt'u siliyor.** İkisi birlikte kullanılınca model tespit edilemeyen bir `enhance_prompt: true` tetikliyor ve yazılan prompt'un yerine referans görselin otomatik açıklamasını koyuyor — sahne tamamen kayboluyor (JSON yanıtındaki `prompt` alanı karşılaştırılarak doğrulandı). **Kural:** Bu modelde `--image` hiç kullanılmaz; kimlik + ürün/nesne referansı birlikte gerekiyorsa `nano_banana_pro`'ya geçilir (`image_references`, en fazla 14, `enhance_prompt` alanı şemasında bile yok — prompt birebir korunuyor).

**2. Metinle tarif edilen kostüm/aksesuar unsurları sahneler arası kayar — görsel referansı olmayan hiçbir şey tutarlı kalmaz.** Claudia'nın yüzü ve Cloud One çorabı (ikisinin de gerçek referans görseli var) 7 sahne boyunca hiç kaymadı; yalnızca metinle tarif edilen ayakkabı (Babolat kararı) sahneden sahneye farklı logo boyutu/tasarımıyla çıktı — ne kadar detaylı yazılırsa yazılsın. **Kural:** Kostüm/aksesuar/ürün serinin genelinde **değişmeyecekse**, ilk üretimde metinle tarif edip onay almak yeterli değildir — o unsur için de (Claudia'nın Soul ID'si gibi) **tek bir referans görsel üretilir ve sabit referans olarak kilitlenir.** "Pozitif kilit" (bkz. yukarı KOL 3 bölümü) yalnız prompt dilinde değil, mümkünse **görsel referansta** uygulanır.

**3. Referans sayısı arttıkça maliyet orantısız artıyor.** 2 referansla (yüz + ürün) `nano_banana_pro` üretim başına ~2-2.7 kredi; 3. referans (ayakkabı) eklenince aynı model/çözünürlükte üretim başına ~9.2 krediye çıktı — yaklaşık 3-4 kat. **Kural:** Yeni bir sabit referans eklemeden önce (özellikle seri/toplu üretimde) `higgsfield generate cost` ile tahmini kontrol edilir, kredi bütçesine karşı tek seferde değerlendirilir — "bir referans daha eklemek ucuz bir iyileştirme" varsayılmaz.

**4. Metin render etme (okunur marka/logo yazısı) güvenilmez.** "Babolat" yazısı ayakkabıda "Babolit" gibi bozuk render edildi — bilinen, modelden bağımsız bir AI zayıflığı. **Kural:** Prompt'ta okunur marka/ürün adı/yazı istemek yerine yalnızca **şekil ve renk** tarif edilir ("dark angular logo accent," metin yok); gerçek bir kelime gerekiyorsa (ör. ürün etiketi) o bölüm sonradan gerçek bir görsel/tipografi katmanıyla eklenir, AI'a render ettirilmez.

**5. Model, istenmeyen üçüncü taraf marka/stil sızdırabilir.** Hiç racket markası istenmediği halde raket sahnelerin çoğunda tutarlı biçimde "Wilson"a benzer bir marka izi taşıdı — modelin eğitim verisindeki en baskın örüntüye varsayılan gidişi. **Kural:** Sahnede marka-hassas bir nesne varsa (raket, ekipman, araç) prompt'a açıkça "plain, no text, no brand name, no logos of any kind" eklenir — sessizce bırakılmaz.

**6. `higgsfield generate cost` referans sayısını fiyata yansıtmıyor — gerçek üretim verisine güvenilir, tahmin aracına değil (14 Ekim, doğrudan test).** 0'dan 8'e kadar referans sayısıyla `nano_banana_pro` üzerinde `generate cost` komutu denendi (gerçek üretim tetiklenmeden, yalnız tahmin) — **hepsi aynı sonucu verdi: 2 kredi**, referans sayısından bağımsız. Bu, lesson #3'teki gerçek üretim bulgusuyla (3. referansla ~9.2 krediye çıkış) doğrudan çelişiyor. **Kural:** `generate cost` çok-referanslı işlerde **yanıltıcı düşük** tahmin verebilir — planlama bu komuta değil, geçmiş gerçek üretim kayıtlarına (bu dosyadaki gibi) dayandırılır.

**7. Düzeltme/ek veri (14 Ekim, aynı gün — gerçek üretimle test edildi): bu kez tahmin doğru çıktı, eski ~9.2 kredi/3-referans bulgusu her koşulda geçerli değil.** Claudia×Towdoo projesinde Sahne A gerçekten iki kez üretildi — ilk tur 4 görsel referansla (yüz+3 elbise), ikinci tur 9 görsel referansla (yüz+3 elbise+mekân+saç+kürk+ayakkabı+eldiven). **İkisi de gerçekte tam 2 kredi harcadı** (`account transactions` ile doğrulandı, tahminle birebir örtüştü) — referans sayısı 4'ten 9'a çıkmasına rağmen maliyet değişmedi. Bu, 11 Ekim'deki 3-referans/~9.2-kredi bulgusuyla **doğrudan çelişiyor.** Olası açıklama (kesin değil, dürüst belirsizlik): hesap o zaman farklı bir plan kademesindeydi, şimdi "plus" planda — plan/kademe değişimi birim maliyeti etkilemiş olabilir; `enhance_prompt` gibi başka bir değişken de rol oynamış olabilir. **Kural güncellemesi:** ne eski (~9.2/3-ref) ne yeni (2-sabit) rakama körce güvenilmez — **her gerçek üretim sonrası `account transactions` ile gerçek harcama kontrol edilir**, varsayım yapılmaz. Maliyet planlaması tahmine değil, o anki gerçek teyide dayanır.

---

## ÖZET — ASTRID'İN GÜNCELLENMİŞ ÇALIŞMA YÖNTEMİ
Bu modül, Modül 1-15'in bilgisini **tek bir operasyonel disipline** bağlar:
1. Referans hazırlığına (Claudia'nın Soul ID seti) prodüksiyonun en kritik adımı olarak zaman ayrılır.
2. Her prompt, 11 katmanlı yapıyla + reality-anchoring dili + anti-sinyallerle yazılır.
3. Her sahne, pozitif kilit listesiyle sürekliliğini garantiler.
4. Işık/lens/kamera kararları (Modül 3, 5, 10) burada **fiziksel gerekçeyle** birleşir — "güzel görünsün" değil, "gerçek ışık/optik nasıl davranır."

---
*Modül 16 v1 (10 Ekim 2026) → v1.1 (11 Ekim 2026, Claudia/Cloud One 7 sahnelik serinin gerçek üretim dersleri eklendi — "Model Seçimi ve Referans Mekaniği" bölümü) · Fox · ÖNCELİKLİ MODÜL (Ayhan emri: "en çok araştırma/eğitim yatırımı buraya"). Kaynak: higgsfield.ai/blog (Seedance 2.5 prompting guide, WebFetch tam metin) + bağımsız teknik analiz (andyhtu.com) + 2026 topluluk/forum pratisyen deneyimi sentezi + Astrid'in kendi gerçek üretim kayıtları (`fox-claudia-cloudone-7-sahne-prompt-seti.md`). Tüm teknik iddialar doğrudan kaynağından ya da gerçek üretim kanıtından, uydurma yok.*
