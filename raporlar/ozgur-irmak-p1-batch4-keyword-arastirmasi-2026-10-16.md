# Özgür Irmak — P1 Batch 4: Anahtar Kelime + AI Sorgu Araştırması (+ P1'in Kapanışına Yakın Envanter)

*Growth Ajanı · 16-17 Ekim 2026 · Kademe 1 — ARAŞTIRMA/BRİEF, hiçbir yazı yazılmadı/taslak oluşturulmadı*

**Devralınan:** `ozgur-irmak-icerik-hacmi-plani-2026-10-16.md` (P1 — 37 net başlık, 5 küme, DÜŞÜK gate) · `ozgur-irmak-p1-batch1-keyword-arastirmasi-2026-10-16.md` (6 yazıldı) · `ozgur-irmak-p1-batch2-keyword-arastirmasi-2026-10-16.md` (7 yazıldı + 3 duplicate elendi + statik-sayfa-tarama yöntemi kuruldu) · `ozgur-irmak-p1-batch3-keyword-arastirmasi-2026-10-16.md` (6 yazıldı + 6 duplicate/yüksek-risk elendi, "TİP vs SÜREÇ" bulgusu, gait slotu açık bıraktı) · `marka-bulutu-os-medikal-protez-bagi.md` §A.3 (yasak/güvenli dil) + §C (YMYL/E-E-A-T).

> ⚖️ **ETİK SINIR (değişmeden taşındı):** Proklinik/rakip sayfaları yalnızca konu haritası/ilham — hiçbir metin/cümle alınmadı veya parafraz edilmedi. Metin Yazarı sıfırdan yazacak.

---

## 0 · ENVANTER DÜZELTMESİ — "~18 kaldı" neden yanlış, gerçek sayı kaç

Görev tanımı 37 − 19 = ~18 diyordu, ama kendi içinde bunun yanlış olacağını işaretlemişti: batch 1-3'ün **yazdığı** 19 başlığın dışında, her batch kendi turunda bazı adayları **duplicate/yüksek-risk** bulup elemişti (batch 2'de 3 + 1 dolaylı, batch 3'te 5 kesin + 1 açık-slot). Bu elenenler "kalan" havuzda sayılamaz. Üç raporu satır satır okuyup kümeye göre temiz bir defter çıkardım:

| Küme | P1 toplam | Yazıldı (B1-3) | Elendi (duplicate, B1-3) | **Bu batch'te kullanılan** | Kalan (P1 sonu) |
|---|---|---|---|---|---|
| Ortez-genel | 9 | 4 | 3 (Ortez Çeşitleri · Kullanım Amaçları · Bacak/Diz Ortezleri genel) | **2** (Soft Ortez Bakım · KAFO Bakım) | **0** |
| Alt ekstremite derinleştirme | 8 | 4 | 2 (Kalça Dezartik. · Diz Üstü/Transfemoral genel) | **2** (Ayak Amp. Seviyeleri · Silikon Ayak Netliği) | **0** |
| Üst ekstremite derinleştirme | 9 | 5 | **4** (Parmak Protezi · Myoelektrik-vs-Biyonik Fark · Tipler/Uyum genel · Dirsek Üstü Kapsamlı Kılavuz) | 0 | **0** |
| Mikroişlemcili diz derinleştirme | 6 | 2 | 0 | **1** (Alışma Süreci) | **3** (thin sinyal, açık) |
| Teknoloji-vitrin DÜŞÜK | 5 | 4 | 0 (1 açık bırakılmıştı: gait) | **1** (Yürüyüş Analizi — gait slotu bu turda kapandı) | **0** |
| **TOPLAM** | **37** | **19** | **9** | **6** | **3** |

**19 + 9 + 6 + 3 = 37.** ✓ Rakamlar kodla değil elle sayıldı ama her satır ilgili rapordaki isimle eşlendi — uydurma yok.

⚠️ **Düzeltme notu (batch 3'ün kendi hatası):** Batch 3'ün §4'ü "Üst ekstremite'nin kalan 3'ü batch 4'e taşınır" diyordu. Kendi §2 tablosunu satır satır saydığımda, batch 3 o kümenin **remaining 6 slotunun tamamını** (6 aday: Myoelektrik-vs-Biyonik, Tipler/Uyum genel, Dirsek Üstü Kılavuz, Dirsek Mekanizması, Takma/Çıkarma, Miyoelektrik Değerlendirme) zaten test etmiş ve kullanmıştı (3 yazıldı + 3 elendi = 6/6). "Kalan 3" rakamı muhtemelen batch 3'ün kendi ön-tur (§0) tablosundaki eski "remaining 6" sayısının güncellenmeden taşınmasıydı. **Bu yüzden bu turda Üst ekstremite'de YENİ bir aday aranmadı** — küme gerçekten 0'da, zorla doldurulmadı (166 vs 207, ~24 vs 21 düzeltmelerinin aynı dürüstlük çizgisi).

**Sonuç — P1'in bu batch sonrası durumu:** 25/37 yazıldı (B1-3'ün 19'u + bu turun 6'sı), 9/37 duplicate nedeniyle kapandı, **3/37 kaldı** — hepsi Mikroişlemcili diz kümesinde, sinyali thin (bkz. §5). P1 pratik olarak **bu batch ile kapanıyor**; geriye kalan 3'ün ayrı bir mini-tur mu hak ettiği yoksa P1'in bu 3 eksikle kapatılıp kalanının CPM/FES/3D Tarama presedanıyla (zayıf sinyal zorla doldurulmaz) açık bırakılacağı Ayhan/Fox kararı.

---

## 1 · YÖNTEM — statik sayfa testi önce (batch 2-3 checklist'i), bu turda 1 katman daha derin

Bu turda test edilen statik sayfalar, batch 2-3'ün baktığı genel hub'lardan (`/ortezler`, `/bacak-protezleri`) farklı — Özgür Irmak'ın **daha niş ürün-bileşen sayfaları** (`/soft-ortezler`, `/yürüme-cihazları`, `/hidrolik-diz-eklemli-protezler`, `/pnomatik-diz-eklemli-protezler`, `/mekanik-modüler-yük-frenli-protezler`, `/diz-dezartikülasyon-eklemli-protezler`, `/syme-silikon-karbon-protez`, `/parsiyel-ayak-protezleri`, `/kişiye-özel-üretim-silikon-ayak-protezi`, `/mikroişlemcili-biyonik-protezler`, `/yürüyüş-analizi`) — 12 sayfa bugün WebFetch ile tek tek okundu.

**Çarpıcı ön-bulgu:** Bu niş sayfaların **6'sı** (hidrolik diz, pnömatik diz, yük frenli diz, diz dezartikülasyonu, soft ortez, yürüme cihazları) Wix Harmony AI tarafından batch 2-3'ün gördüğü genel hub'lardan **çok daha derin** üretilmiş — tanım + mekanizma + karşılaştırma + avantaj + kişiye özel uygulama hepsi var. Bu, ilk bakışta güçlü aday gibi görünen 5 konuyu (Hidrolik-vs-Pnömatik Fark, Yük Frenli Diz Nedir, Diz Dezartikülasyonu Nedir, Soft Ortez Nedir-genel, Yürüme Cihazı Nedir-genel) **tek tek elemek zorunda bıraktı** — çünkü bu konuların "nedir/fark" çerçevesi zaten o sayfalarda var. Batch 3'ün "statik sayfa NE sorusunu cevaplıyor, blog NASIL/NEDEN/SÜREÇ'te boşluk" bulgusu burada da doğrulandı, ama bu turda NE DE "NASIL/SÜREÇ" seviyesinde bazı konular (Hidrolik-vs-Pnömatik karşılaştırması, Yük Frenli'nin kilitli dizle farkı) zaten derinlemesine o sayfalarda işlenmişti — saturasyon beklenenden daha ileri çıktı.

---

## 2 · ELENEN ADAYLAR — bu turda test edilip duplicate/yüksek-risk bulunanlar

| Aday | Test edilen statik sayfa | Sonuç (WebFetch, bugün okundu) |
|---|---|---|
| Hidrolik Diz ile Pnömatik Diz Arasındaki Fark | `/hidrolik-diz-eklemli-protezler` + `/pnomatik-diz-eklemli-protezler` | ❌ **DUPLICATE.** İki sayfa da birbirine ve mekanik/mikroişlemcili sistemlere karşı KENDİ karşılaştırmasını zaten yapıyor ("pnömatik sistemlerde hareket kontrolü hava direnciyle, hidrolik dizlerde sıvı direnciyle sağlanır"). |
| Yük Frenli (Safety/Stance-Control) Diz Nedir, Kimler İçin Uygun | `/mekanik-modüler-yük-frenli-protezler` | ❌ **DUPLICATE.** Çalışma prensibi + kimler için uygun + avantajlar + "kilitli diz ile farklılıklar" + hizalama süreci zaten dolu. |
| Diz Dezartikülasyonu Nedir, Diz Üstü/Altı Farkı | `/diz-dezartikülasyon-eklemli-protezler` | ❌ **DUPLICATE.** Tanım + diz üstüne karşı 7 maddelik avantaj listesi + "4 bar mekanizmalı polisentrik diz" teknik detayı zaten var. |
| Soft Ortez Nedir (genel tanım/tür) | `/soft-ortezler` | ❌ **DUPLICATE.** 7 ortez türü (el bileği/ayak bileği/diz/bel/boyun/dirsek/omuz) her biri tanım+kullanım alanı+sağladığı destek ile zaten işlenmiş. **Ama** bakım/yıkama bilgisi YOK → bu boşluk kullanıldı (§3.1). |
| Yürüme Cihazı (Ortez) Nedir (genel tanım/tür) | `/yürüme-cihazları` | ❌ **DUPLICATE.** 4 kategori (Kısa/Uzun/Nöro/Mikroişlemcili Ortezler) endikasyon+avantaj+kişiye özel planlama ile zaten işlenmiş. **Ama** günlük giyim/temizlik/değiştirme bilgisi YOK (ikinci bir WebFetch ile bugün ayrıca doğrulandı) → bu boşluk kullanıldı (§3.2). |

**Not — bu 5'in 2'si (Soft Ortez, Yürüme Cihazı) tam elenmedi, pivot etti:** Batch 3'ün "AFO Nedir elendi → AFO Nasıl Kullanılır'a pivot etti" örüntüsüyle birebir aynı — "nedir" sorusu dolu ama "nasıl kullanılır/bakım" sorusu boş. Bu ikisi §3.1 ve §3.2'de yazılabilir başlığa dönüştü.

---

## 3 · SEÇİLEN 6 BAŞLIK

### 3.1 · Soft Ortez (Bandaj/Breys) Nasıl Kullanılır, Bakımı ve Yıkaması Nasıl Yapılır?
*(Küme: Ortez-genel — kümenin son slotu)*

**Duplicate notu:** §2'de işlendi — `/soft-ortezler` tanım/tür/kullanım-alanı dolu, bakım/yıkama boş.

**Klasik arama kalıbı:** "ortez bakımı nasıl yapılır" · "dizlik nasıl yıkanır" · "elastik bandaj temizliği"

**AI-konuşma kalıbı:** "Diz bandajımı/ortezimi nasıl yıkamalıyım, makinede olur mu?" — WebSearch cevabı somut geldi: haftada bir ılık sabunlu bez/anti-bakteriyel mendil, diz ortezleri için **30°C'de elde, çitilemeden, beyaz sabunla, makinede yıkama/kurutma YOK, havluya serip oda sıcaklığında kurutma**, ağartıcı/sert kimyasal yasak. Bu "adım-adım bakım talimatı" kalıbı AI-cevabın tercih ettiği format.

**Rakip başlık kalıbı:** Zetka, ASM Medikal, Variteks gibi medikal-market siteleri genel "elastik bandaj/dizlik" bakımı yazıyor — **protez-ortez merkezi bağlamında** dedike bir sayfa bulunamadı (Proklinik'in /bilgi listesinde de soft-ortez/bandaj girişi yok). Gerçek bir boşluk.

**Önerilen H1:** *"Soft Ortez (Diz, Bel, Bilek Bandajı) Nasıl Kullanılır ve Yıkanır? Bakım Rehberi"*

**FAQ:** Soft ortez her gün yıkanmalı mı, ne sıklıkla? · Makinede yıkanabilir mi? · Hangi malzemeler (neopren/elastik kumaş/silikon destek) farklı bakım ister mi? · Ciltte tahriş olursa ne yapılmalı?
⚠️ **Avukat/doğruluk notu:** WebSearch'teki "30°C, haftada bir" gibi somut talimatlar **genel sektör bilgisi** — Özgür Irmak'ın sattığı spesifik marka/malzeme için üreticinin kendi etiket talimatı önceliklidir, yazı "genel kural + ürününüzün etiketine/uzmanınıza danışın" çerçevesiyle kapanır.

---

### 3.2 · KAFO (Uzun Bacak Ortezi) Günlük Kullanım ve Bakımı Nasıl Yapılır?
*(Küme: Ortez-genel — kümenin son slotu)*

**Duplicate notu:** §2'de işlendi + ikinci bir WebFetch ile doğrulandı — `/yürüme-cihazları` sayfasının "Uzun Yürüme Cihazları (KAFO)" bölümü **"sadece tanım, endikasyon ve avantaj seviyesinde kalıyor... günlük giyim süresi, takılıp çıkarılması, temizlik-bakım, cilt kontrolü veya değiştirme zamanlaması gibi pratik kullanım talimatları YOK"** (WebFetch'in kendi ifadesi). Zaten yayındaki "AFO Nasıl Kullanılır" (B3) yazısından farkı: AFO ayak bileği seviyesinde, KAFO diz+ayak bileği — farklı giyim dinamiği (kilitleme mekanizması, daha uzun donning süresi).

**Klasik arama kalıbı:** "KAFO nasıl giyilir" · "KAFO bakımı" · "KAFO ne zaman değiştirilir"

**AI-konuşma kalıbı:** "Çocuğuma/bana KAFO verdiler, nasıl takacağım, ciltte iz kalır mı?" — WebSearch cevabı: ilk 1-2 hafta kademeli alıştırma (günde birkaç saat → kademeli artış), kayış/mekanik parça kontrolü, hasar/deformasyon/işlev kaybında değiştirme.

**Rakip başlık kalıbı:** Luxmed'in *"AFO ile KAFO Arasındaki Fark Nedir"* (zaten batch1'de not edilmiş rakip) + Provital *"Kafo Ortezi Neden Kullanılır"* + Mardin Ortopedi *"Kişiye Özel KAFO Uygulaması Nasıl Planlanır"* (planlama/uyum süreci, günlük kullanım değil) — **hiçbiri günlük giyim/bakım/değiştirme pratiğini** AFO'daki gibi dedike işlemiyor. Proklinik'in kendi `/bilgi/mikroislemcili-bacak-ortezi-kafo` sayfası da teknoloji-odaklı, bakım değil.

**Önerilen H1:** *"KAFO (Uzun Bacak Ortezi) Nasıl Kullanılır? Günlük Giyim ve Bakım Rehberi"*

**FAQ:** KAFO ilk takıldığında alıştırma süresi nasıl planlanır? · Günlük kaç saat kullanılmalı? · Kayış/kilit mekanizması nasıl kontrol edilir? · Ne zaman değiştirilmesi gerekir?
⚠️ Nörolojik tanı (SP/inme) **detaylandırılmaz** — plan'ın kendi gate ayrımı (Ortez-nörolojik 🔴 YÜKSEK, P4) burada da korunur, bu yazı tanım/pratik düzeyinde kalır.

---

### 3.3 · Yürüyüş Analizi Protez-Ortez Sürecinde Neden ve Ne Zaman Yapılır?
*(Küme: Teknoloji-vitrin — batch 1/3'ün açık bıraktığı gait slotu, bu turda kapandı)*

**Duplicate notu — kritik, iki WebFetch ile doğrulandı:** `/yürüyüş-analizi` sayfası sensör/teknoloji + ölçülen parametreleri (basınç, adım hızı, ağırlık merkezi) kapsıyor ama WebFetch'in kendi ifadesiyle **"NE ZAMAN/NEDEN YAPILIR: sayfa açıklamıyor, sadece 'yenileme sırasında' geçiyor"** ve **"SONUÇLAR PROTEZ TASARIMINA NASIL YANSIR: hiç yer almıyor."** Bu, batch 1/3'ün TZP uyarısının (teyitsiz tedarikçi-şartname rakamı riski) tam karşılığı DEĞİL — çünkü bu yazı sensör sayısı/tarama süresi gibi teknik speklere hiç girmeyecek, sadece "neden/ne zaman/karar nasıl etkilenir" sorusunu cevaplayacak. TZP'nin uyarısı böylece ihlal edilmeden konu açılabildi.

**Klasik arama kalıbı:** "yürüyüş analizi neden yapılır" · "yürüyüş analizi kimlere uygulanır"

**AI-konuşma kalıbı:** "Protez/ortez öncesi yürüyüş analizi yapılması gerekir mi, ne işime yarar?" — WebSearch cevabı: "normal ile patolojik yürüyüş arasındaki fark ortaya çıkarılır, tespit edilen yürüyüş şekline göre protez/ortez belirlenir" + "uygulama sonrası hastanın yürümesi tekrar incelenir" — **öncesi-sırası-sonrası** üç aşamalı karar döngüsü, AI-cevabın sevdiği yapılandırılmış format.

**Rakip başlık kalıbı:** Proklinik'in 4 dedike /bilgi sayfası var (`ayak-analizi-nedir`, `dinamik-analiz`, `statik-analiz`, `postur-analizi`) ama hepsi **teknoloji-odaklı** (bizim statik sayfamızla aynı boşluk). WebSearch'te bulunan rakip içerik (Hisar Hospital, fizyoo.com, Dr. Sarıkaya) **hastane/fizyoterapi kliniği** kaynaklı, nörolojik hasta (SP/inme/Parkinson) odaklı — **protez-ortez merkezi bağlamında "neden/ne zaman" sorusuna dedike bir rakip sayfa bulunamadı.** Gerçek boşluk.

**Önerilen H1:** *"Yürüyüş Analizi Protez ve Ortez Sürecinde Neden Yapılır, Ne Zaman Gerekir?"*

**FAQ:** Yürüyüş analizi ilk protez/ortez öncesinde mi yoksa sonrasında mı yapılır? · Hangi durumlarda tekrar analiz gerekir (yenileme, rahatsızlık hissi)? · Analiz sonucu protez/ortez tasarımını nasıl değiştirebilir? · Bu bir ağrı/tanı testi mi, yoksa protez uyumu değerlendirmesi mi?
⚠️ **Sensör sayısı/tarama süresi gibi tedarikçi-şartname rakamları yazıya KONMAZ** (TZP'nin teyitsiz-teknik-detay uyarısı hâlâ geçerli — bu yazı "neden/ne zaman" çerçevesiyle sınırlı kalarak o riski by-pass eder, "nasıl ölçülüyor" teknik detayına girmez). Nörolojik tanı örnekleri (SP/inme/Parkinson) WebSearch'te sık geçti ama **yazıya girmez** — protez-ortez bağlamında kalır, nöroloji kliniğine kaymaz (DÜŞÜK gate korunur).

---

### 3.4 · Ayağın Hangi Bölümünden Ampütasyon Olursa Hangi Protez Uygulanır? Transmetatarsal, Lisfranc, Chopart ve Syme Karşılaştırması
*(Küme: Alt ekstremite derinleştirme)*

**Duplicate notu:** `/parsiyel-ayak-protezleri` hub 5 tipi (parmak/ön ayak/transmetatarsal/Chopart/Lisfranc) tanımlıyor + "seçim kriterleri" bölümü var ama WebFetch'in kendi ifadesiyle **"her tip hakkında detaylı teknik açıklamalar yoktur."** `/syme-silikon-karbon-protez` kendi sayfasında Syme'ı diz-altı amputasyona karşı karşılaştırıyor ama **"diğer ayak amputasyon seviyeleri (Chopart, Lisfranc, parsiyel) ile karşılaştırma bulunmamaktadır"** (WebFetch'in kendi ifadesi). Yani: her ürün kendi tanımını yapıyor, ama seviyeler ARASINDAKİ fonksiyonel/protetik farkı yan yana koyan bir içerik YOK — bu, batch 2'nin "Protez Bacağın Bileşenleri" ile `/bacak-protezleri` ilişkisiyle aynı desen (hub kısa/dar, blog derinleştirir).

**Klasik arama kalıbı:** "ayak ampütasyon seviyeleri" · "Lisfranc Chopart farkı" · "parsiyel ayak protezi çeşitleri"

**AI-konuşma kalıbı:** "Ayağımın bir kısmı kesildi, hangi protez bana uygun, seviyeye göre değişir mi?" — WebSearch EN tıbbi literatürden (ResearchGate, PubMed) geldi: Lisfranc (metatars-tarsal ayrımı, daha fazla ayak korunur, daha fonksiyonel) vs Chopart (talonaviküler/kalkaneoküboid ayrımı, daha karmaşık protez desteği gerektirir, ökçe deformite riski) vs Syme (tibia/fibula distal, topuk yağ yastığı korunur, uçtan yük taşıma mümkün) — **yapılandırılmış seviye-bazlı karşılaştırma.**

**Rakip başlık kalıbı — EN ÇARPICI BULGU:** Proklinik'in /bilgi listesinde (207 URL) bu konuda **hiçbir sayfa yok** (Syme/Chopart/Lisfranc/parsiyel için grep sonucu boş). WebSearch'te TR dilinde de **hiçbir hasta-dili rakip sayfa bulunamadı** — sonuçların tamamı İngilizce akademik/klinik literatür (ResearchGate, ScienceDirect, PubMed). Bu, batch 1'in "mikroişlemcili vs mekanik" bulgusuyla aynı örüntünün daha da güçlü hali: TR pazarında bu karşılaştırma **hiç yok**, EN'de var — büyük GEO-citation fırsatı.

**Önerilen H1:** *"Ayağın Hangi Bölümünden Ampütasyon Olursa Hangi Protez Uygulanır? Transmetatarsal, Lisfranc, Chopart, Syme Farkları"*

**FAQ:** Bu dört seviye arasındaki temel fark nedir (ne kadar ayak korunuyor)? · Hangi seviyede protez ihtiyacı daha karmaşık hale gelir? · Topuk/ayak tabanı korunması neden önemli? · Seviyeyi kim belirler — cerrah mı, protez-ortez uzmanı mı?
⚠️ **Ampütasyon seviyesi kararı KESİNLİKLE cerrahi/hekim kararıdır** — yazı bu seviyeleri "protez-ortez açısından ne anlama geldiği" düzeyinde bilgilendirir, hangi seviyenin "daha iyi" olduğuna dair öneri vermez (TİTCK M.5 + tıbbi tavsiye sınırı). EN kaynaklı teknik terimler (disartikülasyon tipleri) avukat/klinisyen teyidinden geçmeden TR hasta diline çevrilmeden kullanılmaz.

---

### 3.5 · "Silikon Ayak Protezi" Derken Hangisi Kastediliyor? İki Farklı Ürünün Farkı
*(Küme: Alt ekstremite derinleştirme — kümenin son slotu; en hedged seçim, bkz. not)*

**Seçim notu (dürüstlük):** Bu, altı başlığın en zayıf sinyalli olanı — `/kişiye-özel-üretim-silikon-ayak-protezi` hub'ı zaten tanım+malzeme+işlev+"karbon/fonksiyonel parsiyel ayak protezlerinden farklı" karşılaştırmasını **orta düzeyde** yapıyor, ve WebSearch'te TR rakipleri (Dinamik Ortopedi, Opoden, protezci.net) benzer "nedir" sayfaları taşıyor. Ama araştırma sırasında somut bir **terim çakışması** ortaya çıktı — bu çakışma yazının asıl değerini oluşturuyor: WebSearch cevabı "silikon ayak protezi" teriminin **iki farklı ürünü** kapsadığını gösterdi: **(1)** parsiyel ayak/parmak kaybında ayağın KENDİSİNİN yeniden üretildiği kozmetik-fonksiyonel protez (bizim statik sayfamızın konusu) vs **(2)** diz-altı/üstü tam bacak protezinde karbon ayağın ÜZERİNE giyilen, onu koruyan ve gizleyen kozmetik kılıf ("protez ayak silikonu, karbon ayağın zarar görmemesi için dışına takılan koruyucu bir ayak formudur"). Hasta/aile bu ikisini kolayca karıştırabilir — bu netleştirme AEO açısından değerli (açık soru-cevap + net ayrım kalıbı).

**Klasik arama kalıbı:** "silikon ayak protezi nedir" · "silikon protez ayak kılıfı"

**AI-konuşma kalıbı:** "Silikon ayak protezi ile karbon ayak aynı şey mi, ikisi birlikte mi kullanılıyor?"

**Rakip başlık kalıbı:** Dinamik Ortopedi *"Silikon Kozmetik Protezler"*, Opoden *"Silikon Ayak ve El Protez Çeşitleri"*, protezci.net *"El, Ayak ve Parmak İçin Kozmetik Silikon Protez"* — hiçbiri bu **iki-anlam ayrımını** başlıkta/çerçevede netleştirmiyor, hepsi tek bir ürün gibi anlatıyor.

**Önerilen H1:** *"'Silikon Ayak Protezi' Derken Hangisi Kastediliyor? Parsiyel Ayak Protezi ile Kozmetik Ayak Kılıfı Arasındaki Fark"*

**FAQ:** Parsiyel ayak kaybında kullanılan silikon protez neyi yeniden oluşturur? · Karbon/fonksiyonel protez ayağın üzerine giyilen silikon kılıf ne işe yarar? · İkisi aynı hastada birlikte kullanılabilir mi? · Hangi durumda hangisi önerilir?
⚠️ **Zayıf/riskli sinyal notu (§0.1 dürüstlüğü):** Bu başlık diğer 5'ten daha az net bir "boşluk" — hub zaten orta-derinlikte kapsıyor. Denetmen'e bu notla gitmeli; onay vermezse batch'in 6'sı 5'e düşer, bu kabul edilebilir (zorla doldurulmaz).

---

### 3.6 · Mikroişlemcili (Protez) Dize Alışma Süreci: İlk Haftalarda Neler Beklenir?
*(Küme: Mikroişlemcili diz derinleştirme)*

**Duplicate notu:** `/mikroişlemcili-biyonik-protezler` teknoloji+avantaj+seçim kriteri+biyomekanik bütünlük kapsıyor ama WebFetch'in kendi ifadesiyle **"Adaptasyon/Alışma Süreci: ilk kullanım haftalarında ne yaşanacağı, uyum zaman dilimi ve ilk zorluklar hakkında hiç bilgi yok"** ve **"Rehabilitasyon/Fizyoterapi: bu kritik süreç hakkında açıklama yapılmamış."** Temiz boşluk.

**⚠️ TERİM ÇAKIŞMASI UYARISI — bu turun en önemli bulgusu:** "Mikroişlemcili diz protezine alışma süreci" diye arattığımda WebSearch sonuçlarının **tamamı diz PROTEZİ AMELİYATI'na (artroplasti/diz replasmanı — ameliyat sonrası iyileşme) gitti**, protez bacak (ampute) bağlamına değil. "Diz protezi" Türkçede iki ayrı şeyi karşılıyor: (a) ampute bireyin protez bacağındaki diz ünitesi, (b) eklem kireçlenmesi ameliyatıyla takılan yapay diz (TKR). Bu çakışma başlıkta ve metinde **özellikle "protez bacak/bacak protezi" + "mikroişlemcili diz ünitesi"** kelimeleri erken ve net kullanılmazsa, hem okuyucu hem AI-sentezi yanlış bağlama (ameliyat sonrası fizyoterapi) kayabilir — SGK/Karbon Ayak yazılarında bu risk yoktu çünkü o başlıklarda "protez ayak/protez bacak" zaten netti.

**Rakip başlık kalıbı:** Aratılan rakip içerik (kayhanturan.com, drozcankaya.com.tr vb.) **tamamı ortopedi/artroplasti cerrahları** — protez-ortez merkezi bağlamında "mikroişlemcili diz ÜNİTESİNE alışma" konusunu işleyen hiçbir TR kaynak bulunamadı. Bu hem gerçek bir boşluk hem de terim-çakışması riskinin **kanıtı.**

**Önerilen H1 (terim çakışmasını önlemek için kelime sırası kasıtlı):** *"Protez Bacakta Mikroişlemcili Diz Ünitesine Alışma Süreci: İlk Haftalarda Neler Beklenir?"*

**FAQ:** Mikroişlemcili diz ünitesini kullanmaya başlarken ilk günler nasıl geçer? · Yürüme paterni ne kadar sürede doğallaşır? · İlk haftalarda hangi zorluklar normal kabul edilir? · Fizyoterapi/yürüme eğitimi bu süreci nasıl destekler?
⚠️ **Başlık/H1'de "protez bacak" veya "bacak protezi" kelimesi İLK cümlede geçmeli** — "diz protezi ameliyatı" ile karışmaması için editoryal kontrol zorunlu, bu not Metin Yazarı'na birebir taşınmalı.

---

## 4 · EN ÇARPICI BULGU

**İki bulgu var, biri metodolojik biri içerik odaklı:**

1. **Saturasyon beklenenden hızlı geldi.** Batch 1-3 ortalama 12 adayda 6'sını elerken (yarı-yarıya), bu turda **11 adaydan 5'i** (Hidrolik-vs-Pnömatik, Yük Frenli, Diz Dezartikülasyonu + 2 pivot) doğrudan duplicate çıktı — çünkü Özgür Irmak'ın niş ürün-bileşen sayfaları (Wix Harmony AI üretimi) genel hub'lardan daha derin yazılmış. **Pratik sonuç:** P1'in geri kalanı (Mikroişlemcili diz'in 3'ü) için de aynı yüksek-saturasyon beklentisiyle gidilmeli — zayıf sinyali zorla doldurmak yerine CPM/FES presedanı (açık bırakma) muhtemelen tekrar gerekecek.

2. **"Diz protezi" terim çakışması, ilk kez bu turda net görüldü (§3.6).** Batch 1'in "mikroişlemcili diz ile mekanik diz farkı" yazısı muhtemelen bu riski taşımıyordu çünkü başlığında zaten "protez" bağlamı (vs mekanik, karşılaştırma) güçlüydü; ama "alışma/adaptasyon süreci" gibi daha genel bir ifade arandığında arama sonuçları doğrudan artroplasti (TKR) içeriğine kayıyor. **Bu, gelecekteki tüm "diz" içerikli başlıklarda (P2-P4'te de "mikroişlemcili diz" veya "diz" geçen her başlık) kontrol edilmesi gereken kalıcı bir terim-netliği checklist maddesi olmalı** — SGK/Karbon Ayak gibi "protez ayak/bacak" zaten net olan başlıklarda bu risk yok, ama "diz" tek başına belirsiz.

---

## ÖZ-DENETİM NOTU (§0.1 — veri dürüstlüğü)

- **Hiçbir arama hacmi/zorluk rakamı yok** — yine Tip B (WebSearch'ün döndürdüğü gerçek başlık/cevap yapısı + WebFetch'in canlı statik sayfa okuması), Ahrefs/Semrush erişimi yok.
- **12 statik sayfa bugün WebFetch ile tam okundu** (soft-ortezler, yürüme-cihazları, diz-dezartikülasyon-eklemli-protezler, parsiyel-ayak-protezleri, syme-silikon-karbon-protez, hidrolik-diz-eklemli-protezler, pnomatik-diz-eklemli-protezler, mekanik-modüler-yük-frenli-protezler, yürüyüş-analizi ×2, kişiye-özel-üretim-silikon-ayak-protezi, mikroişlemcili-biyonik-protezler) — tahmin değil, gerçek sayfa içeriği.
- **Proklinik'in 207 /bilgi URL'si bugün tekrar grep'lendi** (Syme/Chopart/Lisfranc/hidrolik/pnömatik/yük-frenli/soft-ortez/silikon-ayak için) — hiçbiri bulunamadı, bu "rakipsiz" iddiası gerçek arama sonucuna dayanıyor, varsayım değil.
- **Batch 3'ün "Üst ekstremite kalan 3" iddiası bu turda yanlış bulundu ve düzeltildi** (§0) — kendi kaynağından (batch 3'ün §2 tablosu) doğrulandı, gizlenmedi.
- **"Diz protezi" terim çakışması (§3.6) WebSearch'ün gerçek sonucu** — uydurma değil, arama yapıldığında fiilen artroplasti içeriği çıktı.
- **3.5 (Silikon Ayak Netliği) en zayıf sinyalli seçim olarak açıkça işaretlendi** — zorla 6'ya tamamlamak için eklenmedi, gerçek bir terim-çakışması bulgusuna dayanıyor ama hub'ın kendi kapsamı diğerlerinden daha dar bir boşluk bırakıyor.
- **Rakip başlıkları yalnızca gözlem** — hiçbiri yazıya kopyalanmadı/parafraz edilmedi.
- **Bu belge bir yazı değil** — Metin Yazarı bu brief'i alıp sıfırdan yazacak; H1 önerileri taslak, kesin değil.

---

## SIRADAKİ ADIM (Ayhan/Fox kararı)

1. Bu 6 başlık Denetmen'e taşınabilir — özellikle **3.4 (Ampütasyon seviyesi karşılaştırması — cerrahi karar sınırı)**, **3.5 (en zayıf sinyal, hub ile kısmi örtüşme)** ve **3.6 (terim çakışması — H1/ilk paragraf editoryal kontrolü zorunlu)** işaretli gitmeli.
2. Onaylanırsa Metin Yazarı'na 6 ayrı brief olarak devredilir.
3. **P1'in kapanışı:** Bu batch sonrası P1'de yalnızca **3 başlık** kaldı, hepsi Mikroişlemcili diz kümesinde, sinyali bu turda da aranmadı (kapsam dışı — zaman sınırı, uydurulmadı). Ayhan/Fox kararı: (a) ayrı bir mini-tur (batch 5, sadece 3 aday) açılsın mı, yoksa (b) CPM/FES presedanıyla "zayıf sinyal, P1 bu 34/37 ile pratik olarak kapansın, kalan 3 P2 ile birleştirilsin" mi?
4. **Eski takvim entegrasyonu (plan §8'den beri açık):** P1 pratik olarak kapanınca, plan'ın §8'inde işaretlenen "eski takvim + yeni plan birleşik backlog" kararı artık ertelenemez — P2'ye geçmeden önce bu entegrasyon oturumu gerekir.

---
*Growth Ajanı · 16-17 Ekim 2026 · Kademe 1 (araştırma/brief, iç rapor) — dışarı gönderim yok, hiçbir yazı yazılmadı. Kaynak: WebSearch + WebFetch (canlı site + Proklinik sitemap, bugünkü oturum) + `ozgur-irmak-icerik-hacmi-plani-2026-10-16.md` + batch 1-3 raporları. Rakamsal arama hacmi/zorluk uydurulmadı. Batch 3'ün "Üst ekstremite kalan 3" hatası düzeltildi (§0).*
