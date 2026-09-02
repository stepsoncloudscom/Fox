# Özgür Irmak — "Protezler" Sayfaları ARAŞTIRMA DOSYASI (v0.1)

*Fox · 2 Eylül 2026 · Ayhan talebi: 9 anlatı sayfasının metinleri yazılmadan önce Össur, Ottobock ve diğer kaynaklardan zemin araştırması + mevcut site dilinin (Hakkımızda · Hizmet & Süreç) incelenmesi.*

> **Bu dosya metin değildir.** Metin yazılırken önüne konacak **zemin**: terim haritası, kim ne diyor, hangi cümle kurulabilir, hangi veri teyit ister. Sayfa iskeletleri ve doldurma formu ayrı: `ozgur-irmak-protezler-doldurma-paketi.md` · Mimari: `ozgur-irmak-protezler-sayfa-mimarisi-v01.md`

---

## §0 · ÖNCE BİR DÜZELTME — canlı siteden dil okunamadı

Ayhan'ın isteği "Özgür Protez'de şu an Hakkımızda ve Hizmet & Süreç kısmındaki dilleri de inceleyerek ele al" idi. Ölçüldü (2 Eyl):

| Adres | Durum |
|---|---|
| `ozgurprotez.com` | **200** ama tek sayfa: "YENİLENİYORUZ" + adres/telefon + ortak logoları. Hakkımızda ya da Hizmet & Süreç bölümü **yok**. |
| `ozgurirmakprotez.wixsite.com/mysite` (taslak site) | **404** — site Draft, yayından çekilmiş durumda. |
| Wix REST API | Klasik editörde **statik sayfa metnine erişmiyor** (31 Tem'de ölçüldü, 1 Eyl'de 414 kaynak taramasıyla teyit edildi). |

→ **Sonuç:** Canlıdaki metin şu an hiçbir kanaldan okunamıyor. Bu dosyadaki ses analizi (§1), **onaylı taslak metinlerden** çıkarıldı: `Hakkımızda v0.7` (Ayhan'ın kabul ettiği sürüm) ve `Yürüme Analizi v0.2` (Denetmen turundan geçmiş süreç sayfası). İkisi zaten sitenin yayınlanacak dilidir.

⚠️ **Ayhan'dan istenen:** Kastettiğin "Hizmet & Süreç" bölümü Wix editöründeki taslak ana sayfada duruyorsa, o metni yapıştır ya da editör ekran görüntüsünü gönder — ses kalibrasyonunu ona göre günceller, farkı işaretlerim. Şu an elimdeki iki metin yeterli ama tam değil.

---

## §1 · MEVCUT DİL — ne yaptığımızın anatomisi

Onaylı iki metinden çıkarılan **12 kural.** Yeni 9 sayfa bu kurallarla yazılırsa site tek ağızdan konuşur; yazılmazsa yamalı görünür.

**Kişi ve mesafe**
1. **Okur "siz"dir, hasta değil.** "Merkeze geldiğinizde", "sizin yapmanız gereken tek şey". Üçüncü tekil klinik dili ("hasta soket içine yerleştirilir") kullanılmıyor.
2. **Merkez "biz"dir ama öne çıkmaz.** "Bakıyoruz", "yürütüyoruz" — özne çoğu cümlede iş, kurum değil.
3. **Kimseye hedef koyulmaz.** Hakkımızda'nın kendi cümlesi: *"Kimin nereye yürümek istediğine kendisi karar verir."* Motivasyon dili yok, "hayatınızı geri kazanın" yok.

**Cümle ve ritim**
4. **Somut sahneyle açılır, tanımla değil.** Yürüme Analizi: *"Sensörlü bir bantta yürüyorsunuz."* Hakkımızda: *"Bir soket, tezgâhta tek bir kişinin ölçüsüne göre frezelenir."*
5. **Şimdiki zaman, -iyor.** "Ölçüleniyor, frezeleniyor, çıkıyor." Edilgen kurumsal dil ("gerçekleştirilmektedir") yok.
6. **Uzunluk serbest, ritim değişken.** Kısa cümle vurgu içindir, kural değil (v0.6 telgraf diye reddedildi — [[ai-sesi-sozdizimindedir]]).
7. **Terim geçtiği yerde açıklanır.** "Soket", "liner", "süspansiyon" ilk geçişte yan cümleyle çözülür.

**İçerik ahlakı**
8. **Sonuç vaat edilmez, amaç bildirilir.** *"Amacı basıncı dağıtmak... Sonuç kişiye göre değişir."*
9. **Sayı varsa kaynaklıdır, yoksa cümle çıkar.** Teyitsiz kalem yumuşatılmaz — silinir.
10. **Takip, işin kendisi olarak anlatılır.** *"Takip teslimattan sonra yapılan bir nezaket değil, işin kendisi."* Bu markanın çekirdek vaadi; her sayfada karşılığı olmalı.

**Sayfa mimarisi**
11. **Kapanış sabit:** yumuşak davet cümlesi ("Sürecin sizin için nasıl ilerleyeceğini merkezimizde birlikte konuşabiliriz.") + kalın **"Adım adım, birlikte."**
12. **Sayfa altı sabit:** genel bilgilendirme uyarısı + kişiye özel değerlendirme cümlesi + güncelleme tarihi/içerik sorumlusu. Sonra SEO bloğu.

---

## §2 · LİDERLER NASIL KONUŞUYOR — ve biz neyi alabiliriz

### 2.1 Össur
- Marka ekseni **"Life Without Limitations"**; misyon "We Improve People's Mobility". Kullanıcıyı "engelli/atlet" diye etiketlemez, **bağımsızlık arayan insan** olarak konumlar. Kurucusu Össur Kristinsson kendisi ampüte bir protezist — Iceross silikon liner'ı o icat etti.
- Ürün dili **kısa, teknik, iddiasız**: "sleeveless vacuum system", "three seal options depending on user needs". Övgü değil, seçim kriteri anlatır.

### 2.2 Ottobock
- Logo bir **"empowerment signature"**; imza rengi "life long blue" #004595. **"Dear AI"** kampanyasında protez kullanıcıları kendi hikâyelerini kendileri anlatır — başkası onlar adına konuşmaz.
- Hasta anlatımı **fayda merkezli ve sade**: aktif vakumda dört başlık — *cilt koruması · hacim yönetimi · propriosepsiyon · dolaşım.* Her biri tek cümleyle açıklanır.
- Süreç anlatımı **adım adım ve beklenti kuran**: kalıp → test soketi → dinamik dizilim → teslim → yürüme eğitimi → takip. Takip bölümünde *"güdüğünüzün boyut ve şekil değiştirmesi tamamen normaldir"* diyerek endişeyi önden karşılıyor.

### 2.3 Bizim için üç ders + üç sınır

| ✅ Alınacak | ❌ Alınmayacak (TİTCK) |
|---|---|
| Fayda başlıklarını **tek cümlede** açıklamak (Ottobock kalıbı) | "En gelişmiş / dünyanın en iyisi" tipi üstünlük dili (Össur ve Ottobock serbestçe kullanıyor, **biz kullanamayız** — 18/6-b) |
| Seçim kriterini anlatmak: "şu koşulda şu tercih edilir" | Sistemler arası **üstünlük** kurmak ("aktif vakum pin sisteminden iyidir") |
| Beklenti kuran süreç anlatımı (değişim normaldir dili) | Kullanıcı hikâyesi/testimonial — Ottobock'un en güçlü aracı, **bize yasak** (M.5) |

> **Not:** Liderlerin dilini birebir çevirmek en kolay tuzak. Onlar üretici, biz uygulama merkeziyiz; onlar ABD/AB reklam rejiminde, biz TİTCK 15/2 yatağındayız. Kalıbı al, iddiayı alma.

---

## §3 · TEKNİK ZEMİN — sayfa sayfa ham bilgi

> Aşağıdaki her kalem kaynaklıdır (§7). **Merkezin fiilen ne uyguladığı ayrı bir sorudur** — §6'daki teyit listesi kapanmadan hiçbiri "biz bunu yapıyoruz" diye yazılamaz.

### 3.0 Çerçeve cümlesi — Diz Altı hub'ının omurgası
Diz altındaki dört kırılımın ortak ekseni tek şey: **protezin güdüğe nasıl tutunduğu** (süspansiyon). Soket, ayak, dizilim aynı kalabilir; değişen bağlantı yöntemidir. Bu cümle net kurulmazsa dört sayfa birbirine karışır.

Bilinen dört yöntem ailesi: ① kılıf/kemer gibi **dış askı**, ② **liner + pin/kilit** (mekanik kilitlenme), ③ **emme (suction)** — tek yönlü valf, ④ **yükseltilmiş vakum (elevated vacuum)** — pompayla aktif hava tahliyesi.

### 3.1 Aktif vakum
**Ne:** Soketle liner arasındaki havanın bir **pompa** ile aktif olarak dışarı atılması. Ottobock'un tanımı: yürüyüş sırasında hava soketten aktif olarak pompalanır; pompa ve tahliye valfi basıncı sürekli düzenler.
**Pompa tipi ikiye ayrılır:** *mekanik* (yürüyüşün kendi enerjisiyle çalışır — ör. Ottobock Harmony P-serisi, Össur Unity ayaktan güç alır, diz kılıfı gerektirmez) ve *elektronik* (pilli/sensörlü — ör. Harmony E2/E3, WillowWood LimbLogic; LimbLogic'te vakum düzeyi protezist tarafından belirlenen aralıkta ayarlanabilir).
**Ne sağlıyor (üretici anlatımı, dört başlık):** soket içi hareketin azalması → cilt sürtünmesi/yara riskinin azalması · gün içindeki **hacim değişiminin yönetimi** · **propriosepsiyon** (protezi hissetme) · dolaşım desteği.
**Literatür ne diyor (dürüst tablo):**
- Board ve ark. 2001: aktif vakumla güdük hacim değişimi ve pistonlama, emme sistemine göre azaldı; adım uzunluğu ve duruş süresi daha simetrik.
- Unity ile yapılan yürüyüş çalışmaları: düz ve engebeli zeminde bazı parametrelerde fark çıktı ama farklar **küçük ve klinik olarak anlamlı sayılmadı**. Kullanıcı geri bildiriminde konfor ve propriosepsiyon iyi bulundu.
- Mekanik test: kopma öncesi taşınan yük — aktif vakum 812±221 N · vakum kapalı 727±213 N · emme yok 401±184 N.
→ **Yazım kuralı:** "daha iyi yürütür" denmez. "Soket içi hareketi kontrol etmek için tasarlanmıştır; ölçümlerde hacim değişimi ve pistonlama azalıyor" denir.
**Kimler için:** gün içinde hacmi belirgin değişen, aktif kullanan, soket içinde kayma/pistonlama yaşayan kişiler. Kesin liste yok — kişiye özel değerlendirme.
**Bakım gerçeği (SSS malzemesi):** pompa ve valf bakım ister; elektronik sistemde şarj/pil vardır. Bu, sayfanın en çok sorulan yeri olur.

### 3.2 Pasif vakum — ⚠️ TERİM ÇATALLANMASI (bu sayfanın en büyük riski)
Türkiye pazarındaki yaygın kullanım ile uluslararası literatür **aynı şeyi kastetmiyor**:

| | Türkiye'deki yaygın kullanım | Uluslararası literatür |
|---|---|---|
| **Pasif vakum** | Yumuşak liner + **tek yönlü valf** + diz kılıfı. Pompa yok; vakum adım attıkça doğal olarak oluşur. (= suction) | "Suction suspension" denir; "vacuum" başlığına genelde girmez |
| **Aktif vakum** | Pompalı sistem (mekanik ya da elektronik fark etmez) | "Elevated vacuum"; kendi içinde *mechanical pump* / *electronic pump* diye ikiye ayrılır |

→ **Karar gerekiyor (Özgür Bey):** Merkezin "pasif vakum" dediği şey **tek yönlü valfli emme sistemi** mi, yoksa **mekanik pompalı** bir sistem mi? İkisi farklı sayfa, farklı anlatım, farklı SSS. Yanlış eşleşme = sayfanın tamamı yanlış.
**Doğru kurgulanırsa bu sayfanın en güçlü bölümü:** aktif vakumdan **farkı**. Kural: "üstündür" değil, "şu koşulda şu tercih edilir." (Örn. daha az bileşen, pil/şarj yok, bakım daha basit; buna karşılık hacim dalgalanmasını yönetme kapasitesi farklıdır.)

### 3.3 Silikon liner + pin (shuttle lock) sistemli
**Ne:** Güdüğe giydirilen silikon liner'ın ucundaki **pim**, soketin dibindeki kilide (shuttle lock) oturur ve mekanik olarak kilitlenir. Çıkarmak için düğmeye basılır.
**Nasıl çalışır:** kilitlenme sesle geri bildirim verir — görme kaybı olan kullanıcılarda ayrıca değerli.
**Güçlü yanları (literatür):** oturarak takıp çıkarma kolaylığı · hacim dalgalanmasına emme sistemlerinden daha toleranslı · memnuniyet anketlerinde diz altı kullanıcılarında emme sistemine göre daha yüksek memnuniyet ve daha kolay takıp çıkarma.
**Bilinen sınırı — açıkça yazılmalı:** pimin uçtan çekmesi, güdüğün uç dokusunda gerilme ("milking") ve pistonlama ile ilişkilendirilir; uzun vadede doku uzaması, tibia kenarında ve kesi ucunda ağrı bildirilmiştir. Yeni nesil liner'larda uç bölgeye konan takviye matrisi bu çekme kuvvetini azaltmak için tasarlanmıştır.
→ Bu sınırı yazmak **risk değil, güven kaynağıdır** ve 15/2 yatağına birebir uyar: bilgilendirme, satış değil.
**Liner malzemesi (SSS malzemesi):** silikon dayanıklı ve elastik, ama yastıklaması sınırlı; TPE/jel liner yastıklama önceliğinde, kemik çıkıntılı ya da nedbeli güdükte tercih edilir, viskoelastik tipleri basıncı yüksek bölgeden düşüğe kaydırır.
**Bakım:** liner **her gün** yıkanır (yumuşak sabun + ılık su, iyi durulama, açık havada kurutma). Yıkanmayan liner ciltte tahrişe yol açar. Bu, sayfanın en somut ve en çok aranan bilgisidir.
**Not:** `ozgur-irmak-blog-silikon-liner-v02.md` elde hazır — **kopyalanmaz, linklenir** (kanibalizasyon).

### 3.4 Modüler klasik protezler — ⚠️ "klasik" tuzağı
**İki ayrı kavram tek başlıkta:**
- **Modüler (endoiskelet):** soket + bağlantı adaptörleri + diz/ayak, hepsi **sökülüp takılabilir** parçalar. Güdük zamanla değiştiğinde protez baştan yapılmaz, ayarlanır/parça değişir. Bugünkü standart yapı budur.
- **Klasik (eksoiskelet/konvansiyonel):** dış kabuğu taşıyıcı, tek parça laminasyonla üretilen yapı. Sonradan ayar ve modifikasyon imkânı sınırlıdır.
**Yazım riski:** "Modüler Klasik Protezler" başlığı okuru "eski model" diye düşündürebilir. Sayfanın görevi tersini yapmak: **bu yapının hâlâ neden tercih edildiğini** anlatmak — sadelik, dayanıklılık, bakım kolaylığı, ayarlanabilirlik, pil/pompa gerektirmemesi. Kendi ürününü kötüleyen sayfa yazılmaz.
**Soket/askı tarafında geçen klasik terimler:** PTB ve KBM soket tipleri; güdükle sert soket arasına giren yumuşak iç soket. Bunlar merkez fiilen uyguluyorsa yazılır, uygulamıyorsa girmez.

### 3.5 Diz üstü protezleri — iki eksen, karıştırma
Bu sayfanın kırılımı **süspansiyon değil, diz eklemi tipidir.** (Denetmen bu karışmayı Hakkımızda metninde bir kez yakaladı — bulgu N3.)

**A) Diz eklemi tipleri**
| Tip | Nasıl çalışır | Tipik kullanıcı profili |
|---|---|---|
| **Kilitli (manuel kilit)** | Tek eksenli, yürürken kilitli; oturmak için kullanıcı kilidi açar | En yüksek stabilite ihtiyacı, düşük hareket düzeyi |
| **Tek eksenli / ağırlıkla frenlenen** | Tek menteşe; duruş fazında ağırlık binince fren devreye girer | Stabilite önceliği, sabit hızda yürüyüş |
| **Polisentrik (çok eksenli)** | Dört-bar bağlantı; dönme merkezi hareket eder, duruşta stabilite yüksek, salınımda diz kolay bükülür | Dezartikülasyon/uzun güdük dahil geniş kullanım |
| **Pnömatik** | Silindir içinde hava; salınım fazını yumuşatır | Değişken yürüyüş hızı, orta düzey aktivite |
| **Hidrolik** | Silindir içinde sıvı; salınım ve/veya duruş fazını kontrol eder | Değişken hız, engebeli zemin, daha aktif kullanım |
| **Mikroişlemcili (MPK)** | Sensörler dizin açısını/yükünü sürekli okur, direnç anlık ayarlanır | Değişken zemin, rampa/merdiven, yüksek stabilite ihtiyacı |

**B) Soket ve askı (bölüm olarak, ayrı sayfa değil)**
Soket tasarımında iki ana hat: **kuadrilateral** ve **iskial içerimli (ischial containment)**; iskial içerimlide yük ağırlığı tek noktada değil güdük yüzeyine dağıtılır. Bunların türevleri (MAS, subiskial) da vardır. Askı: emme valfi · liner-kilit · vakum · Silezyen/TES kemeri.

**C) Hareket düzeyi (K / MOBIS) — kullanıcıya anlatım dili**
Uluslararası pratikte cihaz seçimi hareket düzeyine göre konuşulur:
- **K1** — ev içi ve kontrollü ortamda, sabit hızda kısa mesafe.
- **K2** — ev dışına çıkabilen, kaldırım/eşik gibi küçük engelleri aşabilen, sınırlı mesafe.
- **K3** — toplum içinde değişken hızda yürüyen, farklı zeminlerde hareket eden, yürürken yük taşıyabilen.
- **K4** — yüksek etkili aktivite, koşu ve spor dahil.
→ **Kullanım kuralı:** Bu ölçek sayfada **etiket** olarak değil, *"gününüz nasıl geçiyor"* sorusunun cevabı olarak anlatılır. Site geneli zaten bu çizgide. Kimseye seviye atanmaz.

### 3.6 Kol protezleri
**Üç aile (uluslararası sınıflandırma):**
1. **Pasif / kozmetik (silikon):** hareketi yoktur; görünüm, denge ve karşı-tutuş (bir nesneyi iki elle sabitlerken destek) işlevi görür. Parmak, parsiyel el ve el düzeyinde silikon protezler bu ailededir — **merkezin kendi silikon ünitesinde döktüğü ürün hattı budur** (Hakkımızda v0.7'de doğrulanmış olgu).
2. **Bedenle çalışan (body-powered):** omuz/gövde hareketini kablo-koşum sistemiyle ele aktarır. Mekanik bağlantı sayesinde kullanıcıya **kuvvet geri bildirimi** verir — bu yüzden ileri teknolojiye rağmen hâlâ tercih edilir.
3. **Miyoelektrik / biyonik:** güdükteki kas kasılmalarının yüzeyden okunan elektriksel sinyali motorları sürer.
   - *Tek kavramalı (standart) el:* tek tip kavrama yapar (ör. Ottobock Myohand VariPlus Speed tipi).
   - *Çok kavramalı (çok eklemli) el:* beş parmağı ayrı hareket eder, farklı kavrama kalıpları seçilebilir (bebionic · i-Limb · Michelangelo hattı). Parmak düzeyinde i-Digits benzeri çözümler vardır.
**Seviye:** parmak · parsiyel el · el bileği (transkarpal) · dirsek altı · dirsek üstü · omuz. Seçim seviyeye, kalan kas kontrolüne ve günlük kullanım profiline bağlıdır.
**Dürüstlük notu:** "biyonik" pazarlama kelimesidir, teknik bir sınıf değil. Sayfa "miyoelektrik" der, "biyonik" kelimesini yalnız aranan terim olduğu için ve tanımlayarak kullanır.
**Not:** `ozgur-irmak-blog-miyoelektrik-el-v02.md` hazır — linklenir, kopyalanmaz.

### 3.7 Ayak ve ayak bileği (hem diz altı hem diz üstü sayfalarında geçer)
| Aile | Kısa tanım |
|---|---|
| SACH | Sabit ayak bileği, yumuşak topuk takozu; hafif ve dayanıklı, düşük hareket düzeyinde |
| Esnek omurgalı | SACH benzeri, omurgası biraz esner; engebeye biraz daha uyumlu |
| Tek eksenli | Mekanik bileği önde-arkada hareket eder; ilk temasta stabilite |
| Çok eksenli | İçe-dışa ve önde-arkada hareket; eğimli ve düzensiz zeminde denge |
| Dinamik yanıtlı (karbon) | Yüklenirken enerji depolar, itiş fazında geri verir; aktif kullanım |
| Hidrolik bilek | Sıvı damperle bilek açısı zemine ve hıza göre uyum sağlar |
→ Seçim: amputasyon seviyesi, kilo, ayak numarası, günlük hareket miktarı, meslek ve hedef.

### 3.8 Süreç — sitedeki 4 adımın karşılığı
Ottobock'un hasta yol haritası altı adım sayıyor: **kalıp/ölçü → test soketi (şeffaf prova soketi) → dinamik dizilim → teslim → yürüme eğitimi → takip.** Bizim site dili dört adımı kullanıyor: **ölçü → prova → teslim → takip.** Eşleme:

| Site adımı | İçine giren |
|---|---|
| **Ölçü** | Ölçüm + alçı/dijital kalıp, güdük değerlendirmesi |
| **Prova** | Şeffaf test soketi, gerektiği kadar tekrar; dinamik dizilim |
| **Teslim** | Son dizilim ve ince ayar |
| **Takip** | Yürüme/rehabilitasyon çalışması, kontrol randevuları, güdük değiştikçe ayar |

Ottobock'un kullanıcıyı rahatlatan cümlesi bizde de karşılığını bulmalı: **güdüğün boyut ve şekil değiştirmesi normaldir; ayar bu yüzden vardır.** Bu cümle Hakkımızda'daki "takip işin kendisi" vaadinin sayfa içindeki kanıtıdır.
⚠️ Merkezin gerçek akışı (kaç prova, ne kadar sürede kontrol, geçici protez veriliyor mu) **teyit ister** — Yürüme Analizi sayfasında aynı boşluk F6 olarak açık duruyor.

---

## §4 · SSS HAVUZU — gerçekten sorulan sorular

Sayfa başına 3-5 tanesi seçilir. Pazarlama sorusu uydurulmaz; aşağıdakiler arama davranışının ve klinik pratiğin bilinen soruları:

**Ortak**
- Protez ne kadar sürede hazır oluyor? · Kaç prova yapılıyor? · Güdüğüm zamanla değişirse ne oluyor? · Protezle duş alınır mı? · Ne sıklıkla kontrole gelmem gerekiyor? · Protez ne kadar dayanır?

**Vakumlu sistemler**
- Pompa bozulursa ne olur? · Elektronik sistemde pil ne kadar gidiyor / nasıl şarj oluyor? · Vakum sesi duyulur mu? · Sıcakta terleme artınca ne oluyor?

**Pin/kilit**
- Pim kilide oturmazsa ne yapmalıyım? · Liner'ı nasıl temizlerim, ne sıklıkla? · Uçta çekilme hissi normal mi? *(Bu sorunun cevabı klinisyen lafzı ister — Fox yazmaz.)*

**Modüler**
- Parça değişimi mümkün mü? · Ayakkabı yüksekliği değişirse ayar gerekir mi?

**Diz üstü**
- Merdiven ve rampada ne değişir? · Mikroişlemcili dizde şarj ne kadar gidiyor? · Oturup kalkarken diz nasıl davranır?

**Kol**
- Miyoelektrik el nasıl kumanda ediliyor? · Ne kadar ağırlık kaldırır? · Silikon parmak protezi günlük işlerde ne yapar, ne yapmaz? · Islanır mı?

⚠️ Hiçbir cevapta **süre/fiyat/garanti** taahhüdü verilmez; merkezin fiilen uyguladığı akış teyitlenmeden somut sayı yazılmaz.

---

## §5 · KIRMIZI HAT — kaynakta olan, bizde olamayan cümleler

Araştırma sırasında toplanan ve **doğrudan kullanılamayacak** kalıplar, güvenli karşılıklarıyla:

| Kaynakta geçen | Neden alınmaz | Güvenli karşılık |
|---|---|---|
| "world's most advanced knees" (Össur) | Üstünlük iddiası (18/6-b) | "Diz eklemi tipleri şu şekilde ayrılır: …" |
| "unprecedented socket fit" (Ottobock) | Ölçülemez iddia | "Soket içi hareketi azaltmak için tasarlanmıştır" |
| "promotes blood circulation" | Tedavi/etki iddiası; klinik onay ister | Kaynak atfıyla ve ölçülü: "üretici, dolaşım üzerine yapılmış çalışmalara atıf yapıyor" — ya da **hiç girme** |
| Kullanıcı hikâyeleri / "Dear AI" formatı | M.5 testimonial yasağı | Hikâye yok; süreç anlatımı var |
| "X sistem Y'den daha iyidir" | Karşılaştırma yasağı | "Şu koşulda şu tercih edilir" |
| Fiyat/paket/kampanya | M.5 ücret bilgisi yasak | Fiyattan hiç söz edilmez |
| "Hemen randevu al, kontenjan sınırlı" | Aciliyet/talep yaratma | "Danışma talebi oluşturabilirsiniz" |

**Marka adı kullanımı ayrı bir kapı:** Össur/Ottobock/Levitate ürün adlarını sayfada anmak (Harmony, Unity, Iceross, bebionic) hem **üretici görsel/marka izni** hem **TİTCK-marka hukuku** açısından açık soru — `fox-durum.md` risk bayrağı. Bu dosyadaki ürün adları **araştırma notudur**, sayfa metnine izin teyidi olmadan girmez. Sayfa jenerik anlatımla (aktif vakum, mekanik pompa, pin kilit) eksiksiz yazılabilir; marka adı gerekmiyor.

---

## §6 · TEYİT LİSTESİ — Özgür Bey'e gidecek sorular

Mevcut teyit talebine (Yürüme Analizi 11 kalem + Levitate 4 kalem + ÜTS/TİTCK kaydı) **eklenecek** sorular. Tek mesajda gitsin.

**Sistem eşlemesi (bloklayıcı)**
1. Merkezin "**pasif vakum**" dediği sistem: tek yönlü valfli emme mi, mekanik pompalı mı? (§3.2)
2. "**Aktif vakum**" olarak uygulanan sistem mekanik pompalı mı, elektronik/pilli mi? İkisi de varsa hangisi hangi durumda?
3. **Pin/kilit** tarafında hangi liner tipleri kullanılıyor (silikon / TPE-jel / uç takviyeli)?
4. "**Modüler klasik**" başlığı altında kastedilen: modüler endoiskelet mi, konvansiyonel eksoiskelet mi, ikisi birden mi?

**Diz üstü**
5. Merkezde fiilen uygulanan diz eklemi tipleri hangileri (kilitli · tek eksenli/ağırlıkla frenlenen · polisentrik · pnömatik · hidrolik · mikroişlemcili)?
6. Soket tarafında hangi tasarım uygulanıyor (kuadrilateral · iskial içerimli · diğer)?

**Kol**
7. Uygulanan hatlar: pasif/kozmetik silikon · bedenle çalışan · tek kavramalı miyoelektrik · çok kavramalı. Hangileri fiilen yapılıyor?
8. Silikon ünitesinde üretilen düzeyler: parmak · parsiyel el · el · üstü?

**Süreç (tüm sayfalar için ortak)**
9. Tipik akış: kaç prova soketi, şeffaf test soketi kullanılıyor mu, geçici protez veriliyor mu?
10. Teslimden sonra ilk kontrol ne zaman, sonra hangi aralıkla çağrılıyor?
11. Yürüme/rehabilitasyon çalışması merkez içinde mi yürütülüyor (Hakkımızda "fizyoterapistlerimiz eşliğinde" diyor — sayfada aynı şekilde yazılabilir mi)?

**Görsel/izin**
12. Sayfalarda üretici stüdyo görseli kullanılacaksa distribütör izni var mı? Yoksa merkezde çekilmiş atölye/cihaz kareleri kullanılır (en temiz yol).

---

## §7 · KAYNAKLAR

**Üretici / kurumsal**
- [Ottobock — Active Vacuum](https://www.ottobock.com/en-gb/prosthetics/sockets/active-vacuum) · [Harmony Academy genel bakış](https://academy.ottobock.com/product/harmony/en/index.html) · [Ottobock US — Harmony below-knee vacuum](https://www.ottobockus.com/prosthetics/lower-limb-prosthetics/solution-overview/harmony-below-knee-vacuum-system/)
- [Ottobock Care — Amputee Mobility Levels (K1-K4)](https://www.ottobockcare.us/en-us/blog/amputee-mobility-levels) · [Ottobock Care — Roadmap to Recovery (süreç adımları)](https://www.ottobockcare.us/en-us/resources/new-amputee/roadmap-to-recovery)
- [Össur — Unity Sleeveless Vacuum System](https://www.ossur.com/en-us/prosthetics/unity) · [Össur — Iceross Seal-In X Locking](https://www.ossur.com/en-us/prosthetics/liners/iceross-seal-in-x-locking)

**Klinik / akademik**
- [Mechanical Evaluation of Unity Elevated Vacuum Suspension System (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10443497/) — yük dayanımı sayıları
- [Effects of the Unity vacuum suspension system on transtibial gait, simulated non-level surfaces (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6002056/) — farklar küçük/klinik anlamlı değil
- [The evidence-base for elevated vacuum in lower limb prosthetics (ScienceDirect)](https://www.sciencedirect.com/science/article/abs/pii/S0268003316300948)
- [The Effects of Suction and Pin/Lock Suspension Systems on Transtibial Amputees' Gait Performance (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC4021017/) — memnuniyet/takıp çıkarma
- [The Pin Lock Reference Manual for Prosthetists (AAOP)](https://assets.noviams.com/novi-file-uploads/aaop/pdfs-and-documents/Locks.pdf) — milking / uç doku uzaması
- [Physiopedia — Lower Limb Prosthetic Sockets and Suspension Systems](https://www.physio-pedia.com/Lower_Limb_Prosthetic_Sockets_and_Suspension_Systems) · [Physiopedia — Prosthetic Knees](https://www.physio-pedia.com/Prosthetic_Knees)
- [Prosthetic Foot Selection for Individuals with Lower-Limb Amputation (JPO / Hanger klinik kılavuzu)](https://hangerclinic.com/wp-content/uploads/clinical-practice-guidelines-prosthetic-foot.pdf) · [Amputee Coalition — Prosthetic Feet](https://amputee-coalition.org/resources/prosthetic-feet/)
- [The Hybrid Subischial Socket for Persons With Transfemoral Amputation (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10443468/) — TF soket tasarımları
- [Economic evaluation of upper limb prostheses / multi-grip vs standard myoelectric (PMC)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10721225/) — üst ekstremite sınıflandırması

**Türkçe terim kullanımı (pazar dili — teknik kaynak değil, terim haritası için)**
- [Çapa Protez — Pasif vakumlu diz altı protez](https://www.capaprotez.com/pasif-vakumlu-diz-alti-protez/) · [Ayak Analiz Merkezi — Aktif vakum sistem](https://ayakanalizmerkezi.com/protez/alt-ekstremite/aktif-vakum-sistem/) · [Alsan Ortopedi — Harmony aktif vakum](https://alsanortopedi.com/harmony-aktif-vakum-diz-alti-protez-sistemi/)
- [MEB MEGEP — Diz Altı Protezi Ölçüsü (PDF)](https://megep.meb.gov.tr/mte_program_modul/moduller_pdf/Diz%20Alt%C4%B1%20Protezi%20%C3%96l%C3%A7%C3%BCs%C3%BC.pdf) — modüler/klasik ayrımı, PTB/KBM

**İç kaynaklar**
`ozgur-irmak-hakkimizda-v07.md` (ses) · `ozgur-irmak-yurume-analizi-v02.md` (süreç sayfası sesi + blok formatı) · `ozgur-irmak-referans-ossur-ottobock.md` (marka dersleri) · `ozgur-irmak-protezler-sayfa-mimarisi-v01.md` · `ozgur-irmak-protezler-doldurma-paketi.md` · `marka-bulutu-os-medikal-protez-bagi.md` · `fox-metin-insan-sesi-korpusu.md`

---

*Statü: araştırma tamam, metin yazılmadı. Sıradaki adım Ayhan'ın vereceği sayfa linkleri — başlıklar geldiğinde bu zeminden doldurulur. §6 teyit listesi kapanmadan teknik iddia içeren bölümler yazılamaz.*
