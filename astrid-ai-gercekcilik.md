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

## DURAKLAMA — "HÂLÂ FAKE GELİYOR" (14 Ekim, Ayhan: Sahne A v2 teknik kutuları işaretledi ama genel izlenim ikna etmedi)

### 1. DENETİM — Modül 16'nın mevcut tavsiyeleri Sahne A v2'ye karşı
| Tavsiye | Uygulandı mı | Sonuç |
|---|---|---|
| Reality-anchoring dili (pores, film grain, subsurface scattering, no plastic skin) | Evet, promptta birebir vardı | **Kısmen işe yaramadı** — bkz. aşağıdaki somut teşhis #2, metin talimatı küçük ölçekte yüzeyi kurtaramadı |
| 11 katmanlı yapı | Evet, tüm katmanlar dolduruldu | Yapı tam, ama yapının kendisi "fake" hissinin çözümü değilmiş — eksik olan başka bir şeymiş (aşağı bkz.) |
| Pozitif kilitler / görsel referans stratejisi | Evet (9 gerçek referans) | Kıyafet/mekân/kürk/saç sadakati mükemmel ÇIKTI — bu tavsiye doğrulandı, sorun burada değil |
| Anti-sinyal ("no CGI smoothness, no digital artifacts") | Evet | Yetersiz — bkz. #2, #3 |
| **Hiç denenmemiş:** el/parmak anatomisi için özel dil | Hayır — hiçbir promptta "five fingers," "anatomically correct hand" gibi açık bir talimat yoktu | **Bu, en büyük boşluk oldu** — bkz. #1 |
| **Hiç denenmemiş:** çoklu-tur img2img rötuş iş akışı | Hayır — tek seferde "global" bir kare üretildi, sorunlu bölge (el) ayrıca düzeltilmedi | İkinci büyük boşluk — bkz. Yeni Bulgu #4 |
| **Hiç denenmemiş:** tane/gren dağılımının "eşit değil, gölgede yoğun" olması talimatı | Hayır — "film grain" yalnız genel olarak istendi, nerede yoğun olacağı belirtilmedi | Üçüncü boşluk — bkz. Yeni Bulgu #3 |

### 2. SAHNE A v2'NİN SOMUT TEŞHİSİ (genel "daha gerçekçi yap" değil, eleman eleman)
*Görsel üzerinde gerçek crop/zoom ile doğrulandı (`sahneA-v2.png`, Astrid'in kendi incelemesi, varsayım değil).*

1. **EL/PARMAK ANATOMİSİ — en büyük tek suçlu.** Ateşe uzanan eldivenli elde parmaklar yanlış — dört parmak net ayrışmıyor, başparmak konumu doğal değil, parmaklar arasında olmaması gereken bir "kaynaşma" var. Bu, diffusion modellerinin **evrensel, iyi belgelenmiş** zayıf noktası (bkz. aşağıdaki araştırma) — tesadüfi bir hata değil, beklenmesi gereken bir risk. Muhtemelen tek başına "fake" hissinin en büyük kaynağı, çünkü göz bilinçsizce önce ele gider ve anatomik hata anında "bu sahte" sinyali verir — ışık/kompozisyon ne kadar doğru olursa olsun.
2. **CİLT DOKUSU/ÇİLLER KÜÇÜK ÖLÇEKTE KAYBOLDU.** Prompt'ta "visible pores... faint natural freckles" açıkça istendi ve yüz referansında çiller gerçekten var — ama Sahne A geniş/çevre-baskın bir kare olduğğu için yüz karede küçük bir alan kaplıyor; model bu küçük alanda pürüzsüz/düz bir cilt üretti, çiller hiç çıkmadı. **Teşhis: bu bir kelime seçimi sorunu değil, ölçek sorunu** — küçük bir yüze "gözenekli doku" talimatı vermenin modelin ifade edebileceği piksel bütçesi yok.
3. **IŞIK/TANE "FAZLA TEMİZ."** Sıcak-sol/soğuk-sağ ayrımı neredeyse kusursuz bir ikili bölünme gibi duruyor — gerçek bir odada lamba+mum+TV+şömine birbirine karışır, bu kadar temiz bölünmez. Benzer şekilde istenen film taneciği genele yayılmış görünüyor, gölge/düz yüzeylerde yoğunlaşmıyor.
4. **ZEMİNDE GRAFİK/TEMAS GÖLGESİ ZAYIF.** Hem istenen "uzun grafik gölge" hem ayakların zeminle temas gölgesi neredeyse yok — figür zemine "yapıştırılmış" değil, hafif "üzerine yerleştirilmiş" hissi var.
5. **Göreceli olarak İYİ olan (yanlış teşhis koymamak için not):** kıyafet/kürk/mekân sadakati, kompozisyon, bakış yönü, kumaş fiziği — bunlar gerçekten çalıştı, "fake" hissinin kaynağı bunlar değil.

### 3. YENİ ARAŞTIRMA (14 Ekim, WebSearch + WebFetch — doğrulanmış kaynaklardan)

**Yeni Bulgu #1 — El/parmak hatası modelin yapısal sınırı, prompt kelimesiyle garanti çözülmez ama azaltılabilir.** Diffusion modelleri elleri zor render eder çünkü eller sabit bir forma sahip değil, simetri yok, küçük bir hareket tüm şekli değiştirir — model "kaç parmak istendiğini" yerel piksel sürecinden çıkaramaz (doğrulanmış: arXiv "HandCraft" makalesi + Medium analizi). **Somut düzeltme:** parmak sayısını ve pozu **açıkça** yaz — *"both hands visible, five fingers each, natural relaxed hand position, anatomically correct fingers, no fused fingers, no extra digits."* Genel "realistic hands" yeterli değil, sayı ve poz açıkça belirtilmeli.

**Yeni Bulgu #2 — Çoklu-tur/img2img rötuş iş akışı, tek-seferlik "global" üretimin yerini almalı.** Bağımsız kaynak (apiyi.com, Nano Banana Pro'ya özel): önerilen disiplin "önce global, sonra lokal" — önce geniş kareyi üret, en iyi adayı seç, sonra **yalnız sorunlu bölgeyi** (el, yüz dokusu) img2img ile ayrı bir turda düzelt, geri kalanı (kıyafet/mekân/kompozisyon) kilitli tutarak. Aynı kaynak: *"Nano Banana Pro şu an farklı üretimler arasında %100 yüz/el tutarlılığı sağlayamıyor — referans görsel + yinelemeli rötuş şart, yalnız prompt optimizasyonu yetmiyor."* **Astrid'e bağlanır:** KOL 2'ye yeni bir adım eklenir — "global üretim" tek başına son adım sayılmaz, el/yüz gibi riskli bölgeler için **ikinci, hedefli bir rötuş turu** standart akışın parçası olur (üretime Ayhan onayı gerektiren Kademe 2 kuralı bu ikinci tur için de aynen geçerli).

**Yeni Bulgu #3 — "Gerçekçilik çapası" kelimeleri DAĞILIM belirtmeden eksik kalıyor.** Bağımsız kaynak (imagera.ai, 2026 "sahte görsel" tellleri): gerçek fotoğrafta tane/gren **gölgelerde ve düz yüzeylerde yoğunlaşır**, eşit dağılmaz; gerçek ışık **tek baskın yönlü kaynaktan gelir ve tutarlı renk sıcaklığıyla söner**, "çok temiz" bir ikili bölünme de en az "çok karışık" bir sahne kadar yapay okunur. **Somut düzeltme:** "film grain" yerine *"film grain concentrated in shadow areas and flat midtones, nearly invisible in bright highlights"*; ışık için *"light sources naturally overlap and mix in color temperature at their boundary, not a clean binary split."*

**Yeni Bulgu #4 — Göz/diş simetrisi de bir tell (bu sahnede test edilemedi, gelecek için not).** Aynı kaynak: iki gözde birebir aynı ışık yansıması (catchlight) ya da mükemmel simetrik/eşit aralıklı dişler sahte okunuyor — gerçek gözlerde yansımalar asimetriktir, dişler genişlik/parlaklık/gölgede farklılık gösterir. Doğrudan kameraya bakan/gülen bir kare geldiğinde bu kontrol listesine eklenecek.

**Yeni Bulgu #5 — Kenar/arkaplan geçişi kontrolü (bu sahnede göreceli iyiydi, yine de kalıcı kontrol maddesi).** Aynı kaynak: "kesilip yapıştırılmış gibi keskin özne + düzgün bulanık arkaplan" sahte bir tell; gerçek lensler kademeli derinlik geçişi, kromatik sapma, köşe vinyeti üretir. Sahne A v2'de bu tell görece zayıftı (kenar geçişleri makul yumuşaktı) — ama her yeni sahnede ayrıca kontrol edilecek bir madde olarak listeye girdi.

### 4. SONUÇ — Astrid'in çalışma yöntemine eklenen somut kurallar
1. **El varsa, el için ayrı dil zorunlu:** "five fingers, anatomically correct, no fused/extra digits, natural relaxed position" her sahnede elin göründüğü her yerde yazılır — atlanmaz.
2. **Yüz küçük kalacaksa (çevre-baskın kompozisyon), doku beklentisi düşürülür ya da ayrı bir yakın-plan/rötuş turu planlanır** — küçük bir yüze "gözenek" yazmak tek başına yetmez.
3. **Gren/ışık dağılım dili eklenir** — "nerede yoğun/nerede yok" belirtilmeden "film grain" ve "warm/cool light" yetersiz kalıyor.
4. **KOL 2'ye ikinci bir standart adım eklendi: hedefli rötuş turu.** Global üretim onaylandıktan sonra, sorunlu bölge varsa (el/yüz) bunun için ayrı, küçük bir img2img turu önerilir — otomatik değil, Ayhan'ın "üret" onayı burada da geçerli.
5. **Render-and-review checklist'e 2 yeni madde:** (a) eller var mı, varsa parmak sayısı/anatomisi doğru mu — zum yapıp bak; (b) gölge/ışık geçişi "çok temiz" mi, gerçek oda karmaşıklığından yoksun mu.

---

## ÖZET — ASTRID'İN GÜNCELLENMİŞ ÇALIŞMA YÖNTEMİ
Bu modül, Modül 1-15'in bilgisini **tek bir operasyonel disipline** bağlar:
1. Referans hazırlığına (Claudia'nın Soul ID seti) prodüksiyonun en kritik adımı olarak zaman ayrılır.
2. Her prompt, 11 katmanlı yapıyla + reality-anchoring dili + anti-sinyallerle yazılır.
3. Her sahne, pozitif kilit listesiyle sürekliliğini garantiler.
4. Işık/lens/kamera kararları (Modül 3, 5, 10) burada **fiziksel gerekçeyle** birleşir — "güzel görünsün" değil, "gerçek ışık/optik nasıl davranır."
5. **(14 Ekim eklendi) Tek-seferlik "global" üretim son adım değildir.** El/yüz gibi riskli bölgeler için hedefli ikinci bir rötuş turu standart akışın parçası; gren/ışık dili "nerede yoğun/nerede yok" diye dağılım belirtir, genel "ekle" yetmez; her çıktı el varsa parmak anatomisi için ayrıca zumlanıp kontrol edilir.

---
*Modül 16 v1 (10 Ekim 2026) → v1.1 (11 Ekim 2026, Claudia/Cloud One 7 sahnelik serinin gerçek üretim dersleri eklendi — "Model Seçimi ve Referans Mekaniği" bölümü) → v1.2 (14 Ekim 2026, "hâlâ fake geliyor" duraklaması: Sahne A v2'nin somut eleman-eleman teşhisi — el/parmak anatomisi en büyük suçlu, küçük ölçekte cilt dokusu kaybı, aşırı temiz ışık/gren dağılımı, zayıf temas gölgesi — + yeni araştırma: el-anatomisi için açık dil, çoklu-tur img2img rötuş disiplini, gren/ışık dağılım dili, göz/diş simetrisi ve kenar-geçişi kontrol maddeleri) · Fox/Astrid · ÖNCELİKLİ MODÜL (Ayhan emri: "en çok araştırma/eğitim yatırımı buraya"). Kaynak: higgsfield.ai/blog (Seedance 2.5 prompting guide, WebFetch tam metin) + bağımsız teknik analiz (andyhtu.com, arXiv "HandCraft", imagera.ai, apiyi.com, Medium) + 2026 topluluk/forum pratisyen deneyimi sentezi + Astrid'in kendi gerçek üretim kayıtları (`fox-claudia-cloudone-7-sahne-prompt-seti.md`, `fox-claudia-towdoo-proje-calisma-notu.md`). Tüm teknik iddialar doğrudan kaynağından, gerçek üretim kanıtından ya da Astrid'in kendi crop/zoom incelemesinden — uydurma yok.*
