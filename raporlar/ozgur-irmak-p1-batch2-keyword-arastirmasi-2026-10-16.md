# Özgür Irmak — P1 Batch 2: Anahtar Kelime + AI Sorgu Araştırması (+ Statik Sayfa Duplicate Taraması)

*Growth Ajanı · 16 Ekim 2026 · Kademe 1 — ARAŞTIRMA/BRİEF, hiçbir yazı yazılmadı/taslak oluşturulmadı*

**Devralınan:** `ozgur-irmak-icerik-hacmi-plani-2026-10-16.md` (P1 dalgası — 37 net başlık, 5 küme, DÜŞÜK gate; bugün 6'sı yazıldı) · `ozgur-irmak-p1-batch1-keyword-arastirmasi-2026-10-16.md` (metodoloji + format şablonu + Denetmen'in bugün bulduğu açık: blog-blog duplicate taraması yapıldı, **blog-statik/kategori sayfası** taraması yapılmadı) · `ozgur-irmak-genel-checkup-2026-10-15.md` (58 statik sayfa teyidi) · `ozgur-irmak-rakip-gorunurluk-kiyaslama-2026-09-28.md` · `marka-bulutu-os-medikal-protez-bagi.md` §A.3/§C.

> ⚖️ **ETİK SINIR (değişmeden taşındı):** Proklinik/rakip sayfaları yalnızca konu haritası/ilham — hiçbir metin/cümle alınmadı veya parafraz edilmedi. Metin Yazarı sıfırdan yazacak.

---

## 0 · BU TURUN FARKI — statik/kategori sayfası duplicate taraması

Bugün Denetmen, batch 1'in duplicate taramasının **yalnız 10 canlı blog yazısına karşı** yapıldığını, Özgür Irmak'ın kendi **statik/kategori sayfalarına** (ürün hub'ları: `/ortezler`, `/kalça-protezleri`, `/kol-protezleri` vb.) karşı hiç bakılmadığını buldu — "Ortez Nedir/AFO-KAFO" yazısı yayınlandıktan SONRA, `/ortezler` statik sayfasının başlığının zaten **"Ortez Nedir?"** olduğu ve AFO/DAFO/KAFO/GRAFO/Soft Ortez/Yürüme Cihazları'nı aynı çerçevede kapsadığı ortaya çıktı. Bu turda bu açık kapatıldı — her kandidat **önce** canlı sitenin tam statik+kategori sayfası envanterine karşı test edildi, **sonra** araştırmaya geçildi.

**Yöntem (canlı veriden, uydurma yok):**
1. `curl https://www.ozgurprotez.com/sitemap.xml` → 8 alt-sitemap tespit edildi.
2. `pages-sitemap.xml` çekildi: **63 URL** (homepage + 3 Wix sistem sayfası [groups/portfolio/members/inquiry-services-page] hariç tutulunca **~59 içerik sayfası** — checkup raporundaki "58-59" rakamıyla örtüşüyor, fark yok).
3. `store-categories-sitemap.xml` çekildi: **18 kategori sayfası.**
4. `blog-posts-sitemap.xml` çekildi: **18 canlı yazı** — bugünkü 6 yeni + bilinen 8-9 eski yazı + **1 önceden hiç envantere girmemiş eski yazı** (aşağıda §7'de ayrıca işlendi).
5. Her aday başlık, bu üç listeye karşı önce **slug/anahtar-kelime eşleşmesi**, şüpheli çıkanlar için **WebFetch ile canlı sayfa içeriği okuma** (başlık + kapsam) yapılarak test edildi — "benzer isim" değil "gerçekten aynı konuyu mu kapsıyor" sorusu cevaplandı.

**Sonuç — 3 aday, DUPLICATE bulunduğu için bu turdan çıkarıldı (detay §1):**

| Aday başlık | Çakıştığı canlı sayfa | Kanıt (WebFetch, bugün okundu) |
|---|---|---|
| Ortez Çeşitleri / Vücut Bölgesine Göre Sınıflandırma | **`/ortezler`** (statik) | Sayfanın H1'i zaten **"Ortez Nedir?"**; AFO, DAFO, KAFO, GRAFO, Soft Ortezler, Yürüme Cihazları aynı çerçevede anlatılıyor. |
| Kalça Dezartikülasyonu Protezi Nedir | **`/kalça-protezleri`** (statik) | Sayfa kalça dezartikülasyonunu "pelvik soket, yük taşıma mekanizması, eklem stabilitesi" düzeyinde zaten derinlemesine işliyor + Modüler Mekanik/Hidrolik Kalça Protezleri ürünlerini listeliyor. |
| Parmak / Kısmi El Protezi Nedir | **`/özel-üretim-silikon-parmak-protezleri`** + **`/özel-üretim-el-protezleri`** (statik) | İki ayrı ürün sayfası zaten bu tam konuyu kapsıyor. |

**Bir 4. duplicate, dolaylı:** "Diz Üstü (Transfemoral) Protez — genel bakış" adayı da elendi; bkz. §7 — hem `/diz-üstü-protezleri` statik sayfası HEM de **daha önce envantere girmemiş, 7 Eylül'den beri canlı bir eski blog yazısı** ("Diz Üstü Protezlere Detaylı Bakış") bu konuyu zaten kapsıyor.

**Neden önemli:** Özgür Irmak'ın 63 statik sayfası çoğu zaman "ürün kategorisi + kısa eğitici tanım" karması (örn. `/bacak-protezleri` soket/pylon/ayak ünitesini kısaca tanımlıyor ama derinleştirmiyor — bu **tehlikeli değil**, çünkü hub kısa geçiyor, blog derinleştiriyor). Tehlikeli olan, `/ortezler` ve `/kalça-protezleri` gibi sayfaların **zaten TAM bir "X Nedir?" anlatısı** taşıdığı durumlar — blog aynı soruyu aynı derinlikte tekrar sorarsa, iki sayfa SEO açısından birbiriyle yarışır (keyword cannibalization) ve Google hangisini öncelemesi gerektiğini şaşırır. Aşağıdaki 7 seçim bu ayrımı net tutuyor.

---

## 1 · SEÇİM GEREKÇESİ — neden bu 7

Plan'ın 31 kalan P1 başlığı 5 kümeye yayılıyor: Ortez-genel kalanı(8) · Alt ekstremite derinleştirme kalanı(7) · Üst ekstremite derinleştirme kalanı(8) · Mikroişlemcili diz derinleştirme kalanı(5) · Teknoloji-vitrin DÜŞÜK kalanı(3: CPM+FES+ bir üçüncü, araştırma turunda net sinyal bulunamadı).

**Seçilen 7 (duplicate taramasından TEMİZ çıkanlar):**

| # | Küme | Konu |
|---|---|---|
| 1 | Ortez-genel | Ortez Malzemeleri Nelerdir (Termoplastik / Karbon Fiber / Çelik) |
| 2 | Ortez-genel | El ve Kol Ortezleri Ne İşe Yarar, Kimler İçin Uygundur |
| 3 | Alt ekstremite derinleştirme | Protez Bacağın Bileşenleri: Soket, Liner, Pylon, Ayak Ünitesi |
| 4 | Alt ekstremite derinleştirme | Protez Bacak/Ayak Seçerken Nelere Dikkat Edilir |
| 5 | Üst ekstremite derinleştirme | Omuz Dezartikülasyonu Protezi Nedir, Kimler İçin Uygulanır |
| 6 | Teknoloji-vitrin DÜŞÜK | CPM (Sürekli Pasif Hareket) Cihazı Nedir |
| 7 | Teknoloji-vitrin DÜŞÜK | FES (Fonksiyonel Elektriksel Stimülasyon) Nedir |

**Bilerek dışarıda bırakılanlar, gerekçeli:**
- **Ortez Çeşitleri, Kalça Dezartikülasyonu, Parmak Protezi** — §0'da kanıtlı duplicate. Yazılmaz; yazılacaksa önce ilgili statik sayfayla "hangisi ne yapar" net ayrımı (örn. statik sayfa = ürün/karar sayfası, blog = yalnızca X durumu çok daha derin ele alır) kurulmalı — bu turda o ayrım kurulamadığı için konu havuzda tutulmuyor.
- **Mikroişlemcili diz derinleştirme kümesi (5 kalan) — bu turda HİÇBİRİ seçilmedi.** Araştırma turunda bu kümenin kalan alt-başlıkları (mikroişlemcili diz özellikleri, pil/şarj yönetimi, elektronik kontrollü yürüme cihazı eklemleri) ya bugün zaten yayınlanan "Mikroişlemcili Diz ile Mekanik Diz Farkı" yazısıyla ya da eski "Mikroişlemcili Diz Nedir" yazısıyla çok yakın çakışıyor; gerçek boşluk thin (ince) çıktı. Batch 1'in CPM/FES için yaptığı dürüstlük hamlesiyle aynı mantık: zayıf sinyali zorla doldurmak yerine açık bırakıldı — 3. batch'te tek-tek, daha derin araştırmayla değerlendirilmeli.
- **Teknoloji-vitrin'in 3. DÜŞÜK başlığı** — net bir aday bu turda bulunamadı (plan'ın kendi kümesi "3D, analiz, SGK, CPM, FES" diyor; 3D ve SGK zaten yazıldı, CPM+FES bu turda alındı — kümenin 5. üyesi muhtemelen "statik/dinamik analiz" veya "yürüyüş eğitimi" gibi bir konu ama bunlar `/yürüyüş-analizi` statik sayfasıyla çakışma riski taşıyor, bu turda derinlemesine doğrulanamadı → boş bırakıldı, uydurulmadı).

---

## 2 · Ortez Malzemeleri Nelerdir (Termoplastik, Karbon Fiber, Çelik)

**Klasik arama kalıbı:**
- "ortez hangi malzemeden yapılır"
- "ortez protez malzemeleri"
- "karbon fiber ortez nedir"

**AI-konuşma kalıbı:**
- "Ortezler plastikten mi karbon fiberden mi yapılıyor, hangisi daha iyi?"
- "Bana önerilen ortez termoplastikmiş, bu ne demek, karbon fiberden farkı ne?"
- WebSearch cevabı üç malzeme sınıfını (termoplastik: PP/PE/PETG — ısıyla şekillenir; karbon fiber — hafif+enerji depolar; çelik — dayanıklı+ucuz) net bir liste halinde döndürdü; bu **tanım+karşılaştırma** kalıbı AI-özetin tercih ettiği yapı.

**Rakip başlık kalıbı (gözlemlenen, kopyalanmayacak):**
- İleri Ortopedi: *"Karbon ve Plastik Hammadde Arasındaki Farklar"*
- Kompozit.net: *"Ortez Protez Karbon Fiber Ürünleri"* (ürün/ticari sayfa, bilgilendirme değil)
- **Not:** Proklinik'in kendi listesinde bu tam konuda dedike bir sayfa bulunamadı (`ortez-protez-malzemeleri` slug'ı var ama malzeme karşılaştırması derinliğinde değil görünüyor) — gerçek bir boşluk.

**Önerilen H1/title:**
> **"Ortez ve Protezler Hangi Malzemeden Yapılır? Termoplastik, Karbon Fiber, Çelik Karşılaştırması"**

**FAQ alt-başlıkları:**
- Termoplastik ortez ile karbon fiber ortez arasındaki fark nedir?
- Karbon fiber neden daha hafif ve enerji depolayan bir malzeme kabul edilir?
- Malzeme seçimini hangi faktörler belirler (kullanım yoğunluğu, yaş, bütçe)?
- ⚠️ Malzeme karşılaştırmasında "en iyisi" / "en dayanıklısı" gibi üstünlük iddiası kurulmaz — nötr, teknik bilgilendirme.

---

## 3 · El ve Kol Ortezleri Ne İşe Yarar, Kimler İçin Uygundur

**Duplicate kontrolü (§0 yöntemiyle):** `/ortezler` statik sayfası AFO/DAFO/KAFO/GRAFO/Soft Ortez/Yürüme Cihazları'nı kapsıyor — **hepsi alt ekstremite (bacak-ayak) ortezi.** El/kol/dirsek/omuz ortezleri (üst ekstremite) o sayfada hiç geçmiyor → **temiz, gerçek boşluk.**

**Klasik arama kalıbı:**
- "el ortezi ne işe yarar"
- "kol ortezi nedir"
- "dirsek ortezi ne zaman kullanılır"

**AI-konuşma kalıbı:**
- "Elimde güç kaybı var, hangi ortez bana yardımcı olabilir?"
- "Doktorum bilek ortezi önerdi, bu ne işe yarıyor, sürekli mi takılıyor?"
- WebSearch cevabı üst ekstremite ortezlerini alt-tipe göre ayırdı (el/bilek/dirsek) ve her biri için somut kullanım senaryosu (parmak kırığı, karpal tünel, dirsek çıkığı/post-cerrahi) verdi — **tip + senaryo** eşleşmesi AI-cevabın standart kalıbı.

**Rakip başlık kalıbı:**
- Memorial: *"Ortez Nedir? Ortez Neden Kullanılır?"* — genel, üst/alt ekstremite ayrımı yapmıyor.
- Dinamik Ortopedi: *"Eklemli Dirsek Kol Ortezi / El ve K Ortezi"* — ürün sayfası, eğitici değil.
- **Gözlem:** TR pazarında "üst ekstremite ortezleri" başlığı altında toplu, eğitici bir sayfa net değil — çoğu ürün sayfası veya genel "ortez nedir" tekrarı.

**Önerilen H1/title:**
> **"El ve Kol Ortezleri Ne İşe Yarar? Kimler İçin Uygundur?"**

**FAQ alt-başlıkları:**
- El/kol ortezi ile protez arasındaki fark nedir? (zaten yayındaki "Ortez Nedir" yazısına iç link)
- Hangi durumlarda el ortezi, hangi durumlarda dirsek/kol ortezi önerilir?
- Ortez kalıcı mı, yoksa geçici bir destek mi?
- ⚠️ İnme/felç/nörolojik tanı **detaylandırılmaz** — plan'ın kendi gate ayrımı (Ortez-nörolojik 🔴 YÜKSEK, ayrı küme/P4) burada da korunur; bu yazı tanım/referans düzeyinde kalır.

---

## 4 · Protez Bacağın Bileşenleri: Soket, Liner, Pylon, Ayak Ünitesi

**Duplicate kontrolü:** `/bacak-protezleri` statik sayfası bileşenleri (soket, liner, diz eklemi, ayak ünitesi) **kısaca** tanımlıyor ama "nasıl birlikte çalıştığı"nı derinleştirmiyor (WebFetch doğrulaması: "bileşenlerin birlikte nasıl çalıştığına dair detaylı teknik açıklama bulunmamaktadır"). Bu, batch 1'deki tehlikeli örüntüden (hub = TAM anlatı) farklı: burada hub kısa geçiyor, blog derinleştiriyor → **güvenli derinleştirme ilişkisi, duplicate değil** — ama yazı hub'a link vermeli, onun yerine geçmemeli.

**Klasik arama kalıbı:**
- "protez bacak bileşenleri"
- "protez soket nedir"
- "protez pylon ne işe yarar"

**AI-konuşma kalıbı:**
- "Protez bacak nelerden oluşuyor, soket ile pylon farkı ne?"
- "Protezimin liner'ı yıpranırsa ne olur, soketle ilgisi ne?"
- WebSearch cevabı 4 bileşeni (soket/liner/pylon/ayak) net bir sıralamayla, her birinin fonksiyonuyla birlikte verdi — bu **parça-fonksiyon eşleştirmesi**, yapılandırılmış AI-cevap formatı.

**Rakip başlık kalıbı:**
- Proklinik: *"Protez Bacak Hakkında Bilgilendirme ve Uygulama"* — doğrudan rakip, bilgi sayfası.
- Alsan Ortopedi: *"Protez Bacak Soket Sistemleri ve Çeşitleri"*
- **Not:** Proklinik'in kendi "Kalça Dezartikülasyon Protezi Temel Bilgiler" sayfası da bu aramada çıktı — bu bizim §0'da elediğimiz konunun Proklinik tarafında gerçekten var olduğunu (ve bizim duplicate kararımızın doğru yönde olduğunu) teyit ediyor.

**Önerilen H1/title:**
> **"Protez Bacağın Bileşenleri Nelerdir? Soket, Liner, Pylon ve Ayak Ünitesi Nasıl Çalışır"**

**FAQ alt-başlıkları:**
- Soket neden kişiye özel üretilir?
- Liner ile soket arasındaki fark nedir, ikisi birlikte nasıl çalışır?
- Pylon hangi malzemeden yapılır (titanyum/karbon fiber), neden önemli?
- Bu bileşenlerden biri değiştiğinde protezin geneli nasıl etkilenir?
- ⚠️ Yazı `/bacak-protezleri` sayfasına açıkça iç link verir ("daha fazla protez türü için") — rekabet değil tamamlama ilişkisi kurulur.

---

## 5 · Protez Bacak/Ayak Seçerken Nelere Dikkat Edilir

**Duplicate kontrolü:** `/protezler` hub sayfası WebFetch ile doğrulandı — **"sadece ürün ve kategori listesi"**, "hangi protez bana uygun" tipi bir karar rehberi/karşılaştırma **yok**. Temiz boşluk.

**Klasik arama kalıbı:**
- "protez bacak seçerken nelere dikkat edilmeli"
- "hangi protez bana uygun"
- "protez ayak çeşitleri karşılaştırma"

**AI-konuşma kalıbı:**
- "Bacağımı diz üstünden kaybettim, hangi protezi seçmeliyim, karara kim karar veriyor?"
- "Protez seçimi yaşam tarzına göre mi yapılır, yoksa doktor tek başına mı belirliyor?"
- WebSearch cevabı dört karar eksenini (amputasyon seviyesi, güdük/sağlık durumu, yaşam tarzı/aktivite, profesyonel danışmanlık) ayrı başlıklar altında verdi — **çok-faktörlü karar rehberi** formatı, AI'ın "hangisi bana uygun" sorularında tercih ettiği yapı.

**Rakip başlık kalıbı (⚠️ özel dikkat):**
- **Luxmed: *"5 Uzmandan Protez Bacak ve Protez Ayak Rehberi: Her Şey Dahil"*** — plan'ın §6'sında zaten "Protez Merkezi Seçerken Sorulacak 12 Soru" örneğiyle işaretlenmiş aynı rakip, aynı tüketici-karar-rehberi tonu. Bu konu, plan'ın orijinal "özel avukat taraması" 3'lüsünden biri — batch 1 bilerek bu turu bekletmişti.
- Alsan Ortopedi: *"İlk Protez Uygulamasında Dikkat Edilmesi Gerekenler"*
- Proklinik: *"PROTEZ BACAK: Kapsamlı Rehber"*

**Önerilen H1/title:**
> **"Protez Bacak ve Protez Ayak Seçerken Hangi Faktörler Dikkate Alınır?"**

**FAQ alt-başlıkları:**
- Protez seçimini en çok hangi faktör belirler (amputasyon seviyesi)?
- Diz altı ve diz üstü protez seçimi neden farklı değerlendirilir?
- Yaşam tarzı/aktivite düzeyi protez seçimini nasıl etkiler?
- Bu kararı kim verir — hasta mı, hekim mi, protez-ortez uzmanı mı?
- ⚠️ **ÖZEL AVUKAT TARAMASI ZORUNLU (plan §6'dan taşındı):** Luxmed'in "her şey dahil rehber" tonuna yakınlık riski yüksek — çerçeve sıkı tutulmalı: "bizi seçin/en iyi biziz" hiçbir cümleye sızmaz, karar her zaman "hekim + protez-ortez uzmanı ekibi"ne bağlanır, Özgür Irmak kendi hizmetini öne çıkarmaz. TİTCK M.5 (talep yaratma) sınırına en yakın başlık bu — Denetmen'e özellikle işaretli gitmeli.

---

## 6 · Omuz Dezartikülasyonu Protezi Nedir, Kimler İçin Uygulanır

**Duplicate kontrolü:** `/kol-protezleri` statik sayfası WebFetch ile doğrulandı — Kozmetik Silikon/Myoelektrik/Biyonik 3 tür var, **omuz dezartikülasyonu için özel bir bölüm yok**, sadece genel "amputasyon seviyesine göre protez belirlenir" cümlesi geçiyor. Temiz boşluk — plan §0'da ("bilerek dışarıda bırakılanlar") zaten işaretlenmiş, bu turda alındı.

**Klasik arama kalıbı:**
- "omuz dezartikülasyonu protezi"
- "omuzdan kol protezi"
- "omuz ampütasyonu protez"

**AI-konuşma kalıbı:**
- "Omuzdan ampute olan biri için protez var mı, nasıl kontrol ediliyor?"
- "Doğuştan kolu olmayan birine omuz seviyesinde protez takılabilir mi?"
- WebSearch cevabı bu protezin diğer kol protezlerinden (dirsek altı/üstü) **daha ileri/özel bir uygulama** olduğunu ve genellikle kablo-kontrollü (body-powered) sistemle dirsek/el hareketini manuel kumanda ettiğini açıkladı — bu nüans batch 1'in diğer kol protezi yazılarında (Kozmetik Kol, Dirsek Altı Biyonik) hiç geçmedi, gerçek bir derinleştirme.

**Rakip başlık kalıbı:**
- **Proklinik: *"Omuz Dezartikülasyon Protez Kol"*** — doğrudan rakip, Proklinik'in kendi `/bilgi` kümesinden (bu konunun plan'daki Üst Ekstremite kümesinden geldiğini teyit ediyor).
- Medikal.com: *"Fonksiyonel Omuz Dezartikülasyon Protezi"* — ürün sayfası.

**Önerilen H1/title:**
> **"Omuz Dezartikülasyonu Protezi Nedir, Kimler İçin Uygulanır?"**

**FAQ alt-başlıkları:**
- Omuz dezartikülasyonu diğer kol amputasyon seviyelerinden (dirsek altı/üstü) nasıl farklı?
- Bu seviyede protez nasıl kontrol edilir?
- Doğuştan omuz/kol eksikliğinde bu protez ne zaman önerilir?
- Günlük yaşamda fonksiyonel beklenti ne düzeyde olmalı?
- ⚠️ "Fonksiyonel beklenti" bölümü gerçekçi/ölçülü kalır — "tam normal kol gibi kullanılır" tipi abartı kurulmaz (TİTCK A.3).

---

## 7 · CPM (Sürekli Pasif Hareket) Cihazı Nedir

**Duplicate kontrolü:** `/takip-ve-rehabilitasyon` statik sayfası WebFetch ile doğrulandı — "Takip/Rehabilitasyon/Bakım" genel süreç anlatıyor, **CPM veya FES gibi spesifik cihazlardan hiç bahsetmiyor.** Temiz boşluk.

**Klasik arama kalıbı:**
- "CPM cihazı nedir"
- "diz ameliyatı sonrası CPM cihazı"

**AI-konuşma kalıbı:**
- "Diz ameliyatından sonra CPM cihazı gerekli mi, evde nasıl kullanılır?"
- WebSearch cevabı cihazı "önceden ayarlanmış hareket aralığında eklemi pasif hareket ettiren motorlu cihaz" olarak tanımladı, faydalarını (hareket kısıtlılığını önler, ağrı/şişliği azaltır, eklem kıkırdağı beslenmesine yardımcı olur) listeledi.

**Rakip başlık kalıbı:**
- Ticari kiralama firmaları (cpmcihaz.com.tr, cpmkira.com, ankaracpmcihazi.com) — **hiçbiri protez-ortez merkezi değil**, medikal cihaz kiralama şirketleri.
- Proklinik'in kendi `/bilgi/diz-ve-kalca-cpm-cihazi` sayfası var — protez-ortez merkezi bağlamında bu konuyu işleyen gerçek bir örnek.

**Önerilen H1/title:**
> **"CPM (Sürekli Pasif Hareket) Cihazı Nedir, Ne Zaman Kullanılır?"**

**FAQ alt-başlıkları:**
- CPM cihazı hangi ameliyatlardan sonra önerilir?
- Cihaz evde mi kullanılır, nasıl bir süreç izlenir?
- CPM kullanımının iyileşmeye somut faydası ne?
- ⚠️ **Kapsam notu:** CPM, protez-ortez üretiminin değil post-operatif rehabilitasyonun bir parçası. Özgür Irmak'ın bu cihazı fiilen sağlayıp sağlamadığı bu oturumda teyit edilmedi — Özgür Bey'den teyit gelmeden "biz de sağlıyoruz" dili kurulmaz, yazı yalnız bilgilendirme çerçevesinde kalır.

---

## 8 · FES (Fonksiyonel Elektriksel Stimülasyon) Nedir

**Duplicate kontrolü:** Aynı `/takip-ve-rehabilitasyon` sayfası — FES de geçmiyor. Temiz boşluk teknik olarak, **ama aşağıdaki gate notuna bakın.**

**Klasik arama kalıbı:**
- "FES cihazı nedir"
- "fonksiyonel elektriksel stimülasyon"

**AI-konuşma kalıbı:**
- "Felç sonrası ayağım düşüyor, FES cihazı bu soruna çözüm olur mu?"
- WebSearch cevabı FES'i "sinir sistemi/kas fonksiyon kaybında kas kasılmasını tetikleyen elektroterapi" olarak tanımladı; kullanım alanlarını **doğrudan nörolojik tanılarla** verdi: inme, omurilik yaralanması, MS, Parkinson, serebral palsi.

**Rakip başlık kalıbı:**
- Türkiye Klinikleri, Apollo Hospitals, Vikipedi — akademik/hastane kaynaklı, protez-ortez merkezi değil.
- Proklinik'in kendi `/bilgi/fonksiyonel-elektriksel-stimulasyon-fes` sayfası var.

**Önerilen H1/title:**
> **"FES (Fonksiyonel Elektriksel Stimülasyon) Nedir, Hangi Durumlarda Kullanılır?"**

**FAQ alt-başlıkları:**
- FES hangi durumlarda (ayak düşmesi, kavrama güçlüğü) kullanılır?
- FES bir ortez değil — AFO ile birlikte mi kullanılıyor, yoksa ayrı bir yöntem mi?
- ⚠️ **GATE UYUMSUZLUĞU — Denetmen'e özellikle taşınmalı:** Plan bu konuyu DÜŞÜK gate'e koymuş (Teknoloji-vitrin kümesi), ama araştırma gösteriyor ki FES içeriği **doğrudan nörolojik tanılarla** (inme, MS, SP, omurilik yaralanması) iç içe — plan'ın kendi çerçevesinde bu tanılar **Ortez-nörolojik kümesinde 🔴 YÜKSEK gate.** Bu bir sınır vakası: yazı yalnızca "cihaz nedir, genel mekanizma" düzeyinde kalır, hiçbir tanıya "FES size yardımcı olur" şeklinde doğrudan bağlanmaz — aksi halde DÜŞÜK sınıflandırma yanlış olur ve yazı fiilen YÜKSEK-gate içerik gibi okunur.

---

## 9 · EN ÇARPICI BULGU

**Özgür Irmak'ın kendi statik sayfa mimarisi, içerik hacmi planının en büyük gizli riski.** 63 statik + 18 kategori sayfası, çoğunlukla "ürün kategorisi + kısa-orta uzunlukta eğitici tanım" karması olarak kurulmuş (Wix Harmony AI'nin otomatik ürettiği içerik mimarisi, 3 Temmuz şema belgesinde planlanan "her kategori sayfası: tanım · kimler için · teknoloji · süreç · SSS" şablonunun birebir uygulanmış hali). Bu, iki türlü sonuç veriyor:

1. **Güvenli derinleştirme (çoğunluk):** Hub kısa geçer (`/bacak-protezleri`'nin soket/pylon/ayak ünitesi tanımı 1-2 cümle), blog derinleştirir (bu turda §4). Duplicate değil, tamamlama.
2. **Tehlikeli çakışma (istisna ama gerçek):** Bazı hub'lar (`/ortezler`, `/kalça-protezleri`) zaten **TAM bir "X Nedir?" anlatısı** taşıyor — blog aynı derinlikte aynı soruyu tekrar sorarsa iki sayfa keyword cannibalization'a girer. Batch 1'in "Ortez Nedir" yazısı tam bu 2. kategoriye düştü, Denetmen bunu yakaladı.

**Pratik sonuç:** İçerik hacmi planının geri kalan turlarında (batch 3, P2-P4), her yeni başlık yazılmadan önce **ilgili statik/kategori sayfası WebFetch ile okunmalı** (slug eşleşmesi yetmez — `/kalça-protezleri` örneği gösterdi ki görünüşte "genel" bir hub sayfası aslında spesifik bir alt-konuyu [kalça dezartikülasyonu] zaten derinlemesine kapsıyor olabilir). Bu, batch 1'in blog-blog taramasından farklı, **ayrı bir kalıcı checklist adımı** olmalı — tek seferlik değil, her gelecek batch için.

**İkincil bulgu:** "Diz Üstü Protezlere Detaylı Bakış" adlı, 7 Eylül'den beri canlı olan ama plan/batch1'in hiçbir envanterinde (ne §2 canlı-çakışan tablosu ne 28 Eylül rakip kıyaslaması) görünmeyen bir blog yazısı bulundu. Bu, plan'ın §0.1'inde "9. canlı yazı hangisi, netleştirilemedi" diye açık bırakılan boşluğun **muhtemel cevabı** olabilir (yayın tarihi ve eski-stil URL formatı [`diz-ustu-protezler`, Türkçe karakter yok] bu hipotezi destekliyor) — ama kesin teyit bu oturumun kapsamında değil, iddia olarak değil ihtimal olarak not ediliyor.

---

## ÖZ-DENETİM NOTU (§0.1 — veri dürüstlüğü)

- **Hiçbir arama hacmi/zorluk rakamı yok** — yine Tip B (WebSearch'ün döndürdüğü gerçek başlık/cevap yapısı), Ahrefs/Semrush erişimi yok.
- **Statik/kategori sayfası sayıları (63/18/18-canlı-blog) `curl` ile bugün doğrudan sitemap.xml'den okundu** — tahmin değil, gerçek HTTP yanıtı. Checkup raporunun "58 statik sayfa" rakamıyla ~59-63 arası küçük fark, Wix sistem sayfalarının (groups/portfolio/members) dahil/hariç tutulmasından kaynaklanıyor — bu fark burada açık tutuldu, gizlenmedi.
- **"Diz Üstü Protezlere Detaylı Bakış" yazısının plan'ın "9. canlı yazı" boşluğuna karşılık geldiği iddiası DOĞRULANMADI** — yalnızca tarih+format uyumuna dayalı bir hipotez, kesin teyit değil.
- **Rakip başlıkları yalnızca gözlem** — hiçbiri yazıya kopyalanmadı/parafraz edilmedi.
- **Bu belge bir yazı değil** — Metin Yazarı bu brief'i alıp sıfırdan yazacak; H1 önerileri taslak, kesin değil.
- **3 konu (Ortez Çeşitleri, Kalça Dezartikülasyonu, Parmak Protezi) bilerek dışarıda bırakıldı** — zorla 8. ve 9. konu olarak eklenebilirdi ama duplicate kanıtı netken bunu yapmak dürüstlük ilkesine (§0.1) aykırı olurdu.

---

## SIRADAKİ ADIM (Ayhan/Fox kararı)

1. Bu 7 başlık Denetmen'e taşınabilir — özellikle **#5 (seçim kriterleri — Luxmed yakınlığı)** ve **#8 (FES — gate uyumsuzluğu)** işaretli gitmeli, ikisi de bu turun en hassas noktaları.
2. Onaylanırsa Metin Yazarı'na 7 ayrı brief olarak devredilir.
3. **Kalıcı checklist önerisi (orkestrasyon/TZP'ye eklenebilir):** Her yeni blog başlığı onaydan geçmeden önce "ilgili statik/kategori sayfası WebFetch ile okundu mu" adımı — bu turda elle yapıldı, ileride otomatikleştirilebilir (örn. `sablonlar/araclar/`'a bir duplicate-tarama scripti).
4. P1'in geri kalanı: Mikroişlemcili diz kümesinin 5 başlığı + Teknoloji-vitrin'in belirsiz 3. üyesi + bugün elenen 3 duplicate-riskli konunun "statik sayfayla net ayrım kurulursa yazılabilir" revize versiyonları, batch 3'e taşınır.

---
*Growth Ajanı · 16 Ekim 2026 · Kademe 1 (araştırma/brief, iç rapor) — dışarı gönderim yok, hiçbir yazı yazılmadı. Kaynak: WebSearch + WebFetch (16 Ekim, bugünkü oturum, canlı site verisi) + `ozgur-irmak-icerik-hacmi-plani-2026-10-16.md` + `ozgur-irmak-p1-batch1-keyword-arastirmasi-2026-10-16.md` + canlı `sitemap.xml` taraması. Rakamsal arama hacmi/zorluk uydurulmadı.*
