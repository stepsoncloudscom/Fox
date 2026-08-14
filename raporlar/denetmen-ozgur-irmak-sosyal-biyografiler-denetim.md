# DENETMEN RAPORU — Özgür Irmak Sosyal Medya Biyografileri v0.1

*Denetmen v2 (Faz 3 Orkestratör) · 14 Ağustos 2026*

**Denetlenen:** `raporlar/ozgur-irmak-sosyal-biyografiler-v01.md` — Metin Yazarı v1.2, 12 metin bloğu / 5 sosyal yüzey
**Çağrılan alt roller:** Verification · Red Team · Devil's Advocate (üçü birden — kalıcı kamu yüzeyi + mevzuat + doğrulanmamış olgu)
**Zemin:** KKK (`ozgur-irmak-branding-kilitli.md`) · v07 · `marka-bulutu-os-medikal-protez-bagi.md` · `ozgur-irmak-uyumlu-ticaret-plani.md` · `fox-metin-insan-sesi-korpusu.md` · IG lansman stratejisi

---

## NİHAİ HÜKÜM: 🔴 **DÜZELT — mevcut hâliyle yayına giremez**

Dört 🔴 bulgunun ikisi metin kalitesiyle ilgili değil: **kaynaksız olgu** ve **kanalın yanlış kuşakta sınıflandırılması.** Metin işçiliği gerçekten iyi — sorun yazımda değil, zeminde ve teslim kapsamında.

**Blokajı kaldıran üç hamle:** ① "Ataşehir" ve miyoelektrik/mikroişlemcili iddialarının belgelenmesi ya da çıkarılması ② her bio'nun cihazsız "Kat 1" varyantının üretilmesi ③ mevcut hesapların eski içerik denetimi.

---

## 0 · ÖNCE DOĞRULANANLAR (bunlar temiz — kovalanmasın)

Metin Yazarı'nın raporladığı sayıları **bağımsız koşturdum**, rapordaki sayılara güvenmedim.

| Kontrol | Beyan | Benim ölçümüm | Sonuç |
|---|---|---|---|
| IG isim alanı | 26 krkt | **26** | ✅ (limit 30) |
| IG bio Varyant A | 136 krkt | **136** (satır sonu dahil) | ✅ (limit 150) |
| IG bio Varyant B | 130 krkt | **130** | ✅ |
| FB kısa bio | 87 krkt | **87** | ✅ (limit 101) |
| FB orta metin | 268 krkt / 33 kelime | **268 / 33** | ✅ |
| FB uzun | 984 krkt / 131 kelime | **984 / 131** | ✅ |
| LinkedIn slogan | 46 krkt | **46** | ✅ (limit 120) |
| LinkedIn şirket Hakkında | 1.350 krkt / 177 kelime | **1.350 / 177** | ✅ |
| LinkedIn headline | 118 krkt | **118** | ✅ (limit 220) |
| LinkedIn kişisel Hakkında | 993 krkt / 130 kelime | **993 / 130** | ✅ |
| YouTube açıklaması | 965 krkt / 131 kelime | **965 / 131** | ✅ (limit 1.000) |

**Karakter sayılarının tamamı doğru. Hiçbiri platform limitini aşmıyor. Teslim hatası yok.**

`sozdizim_tarama.py` — dört metni tek tek koşturdum, **rapordaki değerlerin tamamı birebir tuttu** (FB uzun 0,443/3,9/7,8 · LinkedIn şirket 9,1 · LinkedIn kişisel 0,459/4,2/0,20 · YouTube exit 0 TEMİZ). **SERT bulgu gerçekten yok.** `slop_tarama.py` — 10 metin bloğunu ayrı ayrı taradım, **temiz** (tam dosyadaki iki "placeholder" eşleşmesi raporun kendi düzyazısından, metinlerden değil — artefakt).

**Ayrıca doğrulanan ve onaylanan kararlar:**
- Fiyat, kampanya, testimonial, hasta anlatısı, öncesi/sonrası, tedarikçi marka adı, internet satışı iması, sağlık turizmi iması: **hiçbir platformda yok.** Bunlar M.5 ve 15/1-a'nın en sert kalemleri; temiz geçilmiş.
- Kanonik kıdem disiplini **kusursuz**: yalnız "1998'den beri". "30 yıl", "20 yılı aşan", "28 yıl" hiçbir yerde yok.
- Ana tagline KKK §2 ile **birebir** ("1998'den beri ustalık, bugünün teknolojisiyle.") ve bilinçli olarak seyrek kullanılmış — ayırt edici varlık disiplini doğru anlaşılmış.
- **Ses kuralı 7 doğru yorumlanmış.** IG carve-out'unun ("Yenilendik. Yeni enerji.") bio'ya değil post'a ait olduğu tespiti — *"dönem dili akışta, kalıcı dil profilde"* — bu dosyanın en iyi tek kararı. Onaylanır.
- **"Güdük" terimi doğru işlendi:** kullanılmadı, sessizce atlanmadı, Branding+klinisyen eskalasyonuna verildi. Kaçınma değil, usulüne uygun askıya alma.
- Akademik unvanın headline'a konmaması: doğru refleks.

---

## BULGULAR

### 🔴 D1 · [Red Team + Verification] Kanal yeşil kuşakta değil — **sarı kuşakta**. Rapor kendi zemin belgesinin yanlış bölümünü referans göstermiş.

Dosyanın açılış şerhi: *"Tüm metin yeşil kuşakta (bilgilendirme) tutuldu"* ve zemin olarak `ozgur-irmak-uyumlu-ticaret-plani.md` **§1 yeşil kuşak** gösteriliyor.

**Kanıt — §1 yeşil kuşakta sosyal medya YOK.** §1'in altı kalemi: kurumsal kimlik/rebrand · resmî web sitesi · B2B yönlendirici programı · bilimsel/eğitsel faaliyet · Google Business Profile · süreç/atölye hikâyesi. Yurt içi sosyal medya **§2 SARI KUŞAK'ın 1 numaralı kalemidir** ve başlığı birebir şudur: *"SARI KUŞAK — avukat onayı olmadan BAŞLAMAZ."*

Aynı maddenin talimatı da açık: *"Öneri: hesaplar kurumsal/eğitim rejiminde, **cihaz-merkezli ve hasta-merkezli içerik avukat çizgisine kadar yok.**"*

Burada bir kategori hatası var: **dilin register'ı** (bilgilendirici, satmayan — bu gerçekten yeşil) ile **kanalın kuşağı** (faaliyet olarak sarı) birbirine karıştırılmış. Metin yeşil yazılmış olabilir; kanal yine de sarı.

**Pratik sonuç — soru #1'in net cevabı budur:** Belirsizlik "her şey beklesin" demek değil, **katman ayrımı** demek. İki rejim üst üste biniyor ve ayrılabilirler:

| Katman | İçerik | Yasal dayanak | Statü |
|---|---|---|---|
| **Kat 1 — kurumsal** | Kuruluş adı, adres/iletişim, 1998, çalışma alanları, süreç anlatımı, ekip yapısı, takip | Sağlık Hiz. Tanıtım **M.4-5 serbest alan** — "kuruluş adı/adres/iletişim · hizmet/uzmanlık alanları · arama motoru ve **sosyal medya kaydı**" (ücretli/sponsorlu olmamak şartıyla) | **Sağlam zemin** |
| **Kat 2 — cihaz** | Miyoelektrik el, mikroişlemcili diz, karbon yürüme cihazları, kifoz/skolyoz korseleri, CNC tabanlık, silikon parmak protezi | Tıbbi Cihaz **15/1-a** yasak; **15/2** istisnası yalnız *"resmî internet sitelerinde"* — sosyal medyaya uzandığı **teyitli değil** (avukat S11/#6/#11) | **Gate'li** |

Yani: **kurum künyesi bugün yayınlanabilir; cihaz envanteri avukat çizgisi çizilene kadar yayınlanamaz.** Bu, projenin kendi planının zaten verdiği talimattır — dosya onu uygulamamış.

Dosyanın savunması (*"cihaz övgüsü sıfır, kapasite tarifi düzeyinde"*) makul bir hafifletmedir ama yanlış soruya cevap verir: 15/1-a **övgüyü değil, tüketiciye yönelik reklamı** yasaklar ve "bilgilendirme/reklam" çizgisinin sosyal medyada nerede durduğu tam olarak açık olan sorudur. Kendi kendine "gri alan varsayımıyla yazdım" demek, gri alanda yayın yapma iznini üretmez.

**En yüksek maruziyet: YouTube.** Açıklama hem cihaz envanteri taşıyor hem de içerik vaadi #3 ile *"Teknoloji açıklamaları: miyoelektrik el ve mikroişlemcili diz sistemleri nasıl çalışır"* diyerek **tüketiciye yönelik cihaz-merkezli içerik üretmeyi kamuya taahhüt ediyor.** Bu, planın §2/1 talimatının tam tersi ve geri alması zor bir beyan.

**Önerilen hamle.** Her yüzey için **iki varyant** üretilsin:
- **Kat 1 (cihazsız) — lansmana hazır.** Cihaz adları çıkar; yerine süreç ve kapasite dili kalır ("ölçü alma, üretim, uygulama, takip"; "üretimin büyük bölümü kendi atölyemizde"). FB kısa bio, IG bio, LinkedIn headline zaten neredeyse buna uygun — asıl iş FB uzun, LinkedIn şirket, LinkedIn kişisel ve YouTube'da.
- **Kat 2 (cihazlı) — avukat onayına kilitli.** Mevcut metinler bu rafta bekler.
- YouTube içerik vaadi #3 Kat 1 sürümünden **çıkarılır**; kanal açıklamasında ilan edilmez.
- Avukat dosyasına giden soru netleştirilir: *"15/2'nin 'resmî internet sitesi' ifadesi kurumun kendi sosyal medya hesabını kapsar mı? Kapsamıyorsa, hesapta cihaz kategorisi adı anmak (marka adı değil, tür adı) 15/1-a kapsamında reklam sayılır mı?"* — mevcut #6/#11 bu ayrımı sormuyor.

---

### 🔴 D2 · [Verification] "Ataşehir" hiçbir zemin belgesinde yok — ama beş yüzeyde doğrulanmış olgu gibi kullanılmış ve künyesi yanlış beyan edilmiş.

Dosyanın "Uydurma sıfır" şerhi şunu iddia ediyor: *"Metinlerdeki her somut çapa (1998, Trakya Üniversitesi, **Ataşehir**, 3D CAD/CAM…) v07'de zaten doğrulanmış havuzdan geliyor."*

**Kanıt — bu beyan yanlış.** Bağımsız taramam:
- `ozgur-irmak-hakkimizda-v07.md` içinde "Ataşehir" **geçmiyor**; "İstanbul" bile geçmiyor.
- Tüm repoda "Ataşehir" **tek yerde** geçiyor: `luxmed-doktor-referral-listesi.md` — orada da *Memorial Ataşehir hastanesi* kastediliyor, Özgür Irmak'la ilgisi yok.
- `fox-metin-insan-sesi-korpusu.md` §5, şehir/semt bilgisini **eksik somut malzeme listesinde** sayıyor: *"şehir/adres yok (teyit gelmedi)"*.

**Dosya kendi kendisiyle çelişiyor:** Açık Kalem 4 *"Tam adres… hiçbir belgede doğrulanmadı"* diyor, Açık Kalem 7 *"Merkezin fiziksel tarifi ve tam adres"*i müşteriden istenecekler arasına koyuyor — ama semt, beş yüzeyin **hepsinde** teyit işareti olmadan metnin içinde duruyor. Öz-denetim kapısı 2'nin *"Teyitsiz hiçbir veri metne girmedi"* iddiası bu kalemde geçersiz.

**Neden 🔴:** Karar Kuralı 5 (rakam/taahhüt uydurulmaz) doğrudan ihlal ediliyor — ve semt, sağlık kuruluşunda ruhsata bağlı bir veridir. Yanlış semt beş kalıcı yüzeye + Google Business Profile NAP zincirine yayılırsa düzeltme maliyeti yüksek. Ayrıca metnin **en çok tekrarlanan üç ayırt edici sinyalinden biri** olarak seçilmiş (raporun kendi tutarlılık tablosu: 1998 · Ataşehir · kendi atölyemizde) — yani markanın kimlik çapalarından biri kaynaksız bir veriye oturtulmuş.

**Önerilen hamle.** Ayhan tek soruyla kapatır ("merkez hangi ilçede?"). Cevap gelene kadar iki seçenek: ① semt satırı "İstanbul"a indirilir (il düzeyi risksiz) ② `⟦⚠️ TEYİT: semt⟧` işaretiyle metinden **çıkarılır**. Ayrıca "Uydurma sıfır" şerhindeki künye beyanı düzeltilir — yanlış künye, bulgunun kendisinden daha tehlikelidir: sonraki denetimleri kör eder.

---

### 🔴 D3 · [Verification] "Miyoelektrik el ve mikroişlemcili diz sistemlerinin uygulaması ve uyarlaması" — kapasite iddiası, hiçbir belgede doğrulanmamış.

İki yüzeyde birinci ağızdan kapasite beyanı olarak geçiyor (LinkedIn şirket maddesi 5; LinkedIn kişisel: *"…uygulamasını ve uyarlamasını yapıyoruz"*) ve YouTube içerik vaadinde tekrarlanıyor.

**Kanıt.** v07'de **geçmiyor**. Repoda geçtiği yerler kapasite beyanı değil:
- `ozgur-irmak-marka-kimligi-v01.md` — KKK KULLAN listesinde **kelime** olarak (onaylı sözcük dağarcığı, yetkinlik belgesi değil).
- Blog yazıları (`blog-miyoelektrik-el-v02`, `blog-protez-turleri-v02`) — bu teknolojilerin **ne olduğunu genel olarak anlatan** eğitici içerik; "biz bunu uyguluyoruz" demiyor.

Onaylı sözcük listesinde bulunmak, o işi yaptığının kanıtı değildir. Bu ikisi kategorinin en yüksek değerli, en yüksek denetim ilgisi çeken cihazları — kapasite iddiası burada belgesiz duramaz. 18/6 "olmayan özelliği var gösterme" ve "ekip yeterliliği hakkında yanlış bilgi" kalemleriyle doğrudan temas ediyor.

**Önerilen hamle.** Özgür Bey'den tek cümlelik teyit: bu sistemlerin uygulaması/uyarlaması merkezde yapılıyor mu, hangi belgeyle? Teyit gelmezse iki satır da çıkarılır. **Not:** D1'in Kat 1/Kat 2 ayrımı uygulanırsa bu kalem zaten Kat 2'ye düşer ve lansmanı bloke etmez.

---

### 🔴 D4 · [Atlanmış Soru + Red Team] Bu bir yeniden yazım değil, bir **göç**. Mevcut hesaplardaki eski içerik hiç denetlenmemiş.

Dosya beş yüzeyi boş sayfa gibi ele alıyor. Ama hesaplar **mevcut ve canlı**: LinkedIn'de "Özgür IRMAK Protez ve Ortez" varlığı olduğu dosyanın kendisinde yazıyor; IG handle "zaten elde"; Facebook sayfası var. Dosyada eski içeriğe dair **tek satır yok** — ne gönderiler, ne sabitlenmiş içerik, ne eski "Hakkında" alanları, ne IG öne çıkanları, ne kapak görselleri, ne Facebook değerlendirmeleri.

**Neden 🔴 — mesele estetik tutarlılık değil, maruziyet artışı.** Müşterinin **yüksek idari ceza geçmişi** var ve medikal paket bunun *"büyük olasılıkla bu çerçeveden"* geldiğini not ediyor (reklam/tanıtım hattı). Eğer eski gönderilerde fiyat, kampanya, memnuniyet paylaşımı ya da öncesi/sonrası varsa, bunlar **şu anda canlı** ve M.5 kapsamında. Cilalı yeni bir bio, hesaba trafik ve dikkat çeker — **denetlenmemiş bir arşivin üstüne görünürlük eklemek riski azaltmaz, artırır.**

İki somut alt kalem, ikisi de kimsenin sormadığı:
- **Facebook "Öneriler/Değerlendirmeler" özelliği.** Açıksa, kullanıcı memnuniyet yorumları = M.5'in açıkça yasakladığı testimonial ve marka bunu barındırıyor. Bu bir metin kararı değil, **hesap ayarı kararı** — lansmandan önce verilmeli. Dosyanın kapalı listesi testimonial'ı *üretmemeyi* garanti ediyor; *barındırmamayı* değil.
- **Facebook'ta canlı "20 yılı aşan tecrübe" tipi ifade.** Rakam olarak yanlış değil (28 > 20) ama **off-canon**: KKK tek onaylı türev olarak "çeyrek asrı aşkın"ı tanıyor. Yeni bio "1998'den beri" derken sayfanın başka bir yerinde daha belirsiz ve daha küçük bir kıdem imasının durması, çapayı zayıflatır.

**Önerilen hamle.** Lansmandan önce zorunlu ön adım: **eski içerik denetimi.** ① dört hesabın tüm gönderileri M.5/15-1a merceğinden taranır (fiyat/kampanya/testimonial/öncesi-sonrası/tanınabilir hasta görseli) ② uyumsuzlar arşivlenir veya gizlenir — **kalıcı silme Kademe 3, Ayhan yapar** ③ FB Öneriler kapatılır ④ eski "Hakkında"/kapak/öne çıkanlar yeni kanona hizalanır. Bu iş Metin Yazarı'nın değil, Growth/İçerik'in; ama **bio yayınından önce** bitmeli. Sırayı ters kurmak bu dosyanın en pahalı hatası olur.

**İkincil not (IG carve-out'un ömrü):** Lansman postu *"Yenilendik. Yeni enerji."* — dosya bunu bio'dan doğru şekilde ayırdı. Ama aynı mantığın devamı yazılmamış: **bu post sabitlenirse (pin) kalıcı yüzeye dönüşür** ve carve-out'un dayandığı "an" gerekçesi çöker. Kural tamamlanmalı: *dönem dili akışta kalır, sabitlenmez* — ya da sabitlenirse süresi baştan belirlenir.

---

### 🟡 D5 · [Verification] Facebook'ta B.2 ve B.3'ün yazıldığı alanların **var olduğu doğrulanmadı**.

Dosya Facebook için üç ayrı alan varsayıyor: Kısa Bio (101) · "Genel Bakış / Hakkında" (268 krkt) · "Uzun Şirket Bilgisi" (984 krkt). Bunlardan yalnız ilkinin limiti belgelenmiş.

Facebook'un Yeni Sayfa Deneyimi'ne (New Pages Experience) geçişinde klasik uzun serbest metin alanlarının (Company Overview / Mission / General Information / Description) **büyük bölümü kaldırıldı**; kalan yapı ağırlıklı olarak 101 karakterlik Bio + yapılandırılmış "Hakkında" alanlarıdır. Bunu bu oturumda canlı doğrulayamadım — ama doğrulanmadan 1.250 karakterlik metin üretilmiş olması başlı başına bulgudur: **var olduğu bilinmeyen bir alan için copy yazılmış.**

**Önerilen hamle.** Ayhan/Growth sayfa yöneticisinde alanları tek tek açıp hangi alanın mevcut ve kaç karakter olduğunu **ekran görüntüsüyle** tespit etsin; metinler ona göre bölünsün. Alan yoksa B.3'ün gerçek evi Facebook değil, **web sitesi Hakkımızda** ya da LinkedIn'dir — emek boşa gitmez, adresi değişir. Aynı kontrol IG'nin bio'yu "…devamı" ile kırpma davranışı için de yapılmalı: 136 karakter limite sığar ama ilk görünen satırlar kritiktir.

---

### 🟡 D6 · [Kalite Tabanı + Tutarlılık] Hukuki lafız, üslup taramasını memnun etmek için zayıflatılmış. Süreç ters çevrilmiş.

YouTube disclaimer'ı: *"…tıbbi tavsiye ya da tanı **içermez**."* Dosya bunu açıkça itiraf ediyor: standart kalıp *"…yerine geçmez"*di, `sozdizim_tarama.py` bunu karşıtlık kalıbı saydığı için **"içermez"e çevrildi.**

Üç sorun:
1. **Anlam zayıflıyor.** "Yerine geçmez" bir sorumluluk sınırlamasıdır. "İçermez" bir olgu iddiasıdır — ve bakım/kullanım anlatan bir kanalda **tartışmalı** bir iddiadır; tavsiyeye yakın içerik üreten kanal "tavsiye içermiyorum" dediğinde koruma değil, çelişki üretir.
2. **v07 ile çelişiyor.** Onaylı v07 sayfa altı: *"…tıbbi tavsiye ya da tanı **yerine geçmez**."* Aynı marka iki yüzeyde iki farklı hukuki lafız taşıyor.
3. **Kendi ilkesini çiğniyor.** Dosya "Ölçü taban, hedef değil — v06 Goodhart dersi" diye yazıp, ölçüyü tam da hedefe çevirmiş — üstelik risk maliyeti stilistik değil hukuki olan tek yerde.

Dosya şerh düşmüş ("avukatın lafzı üstündür") — bu dürüst, ama **taslakta duran metin zayıf olan.** Avukat adımı sıkışırsa canlıya giden o olur.

**Önerilen hamle.** Şimdi "yerine geçmez"e dönülür, tarama UYARI'sı gerekçeli bırakılır. Kural yazılır: **hukuki/uyum lafzı sözdizim taramasının kapsamı dışındadır**; ölçü metni değiştirmez. Bu kural `metin-yazari.md` İnsan Sesi Kapısı'na eklenmeli — yoksa aynı hata tekrar eder.

---

### 🟡 D7 · [Tutarlılık] Disclaimer neden yalnız YouTube'da?

Tutarlılık tablosu bunu açıkça gösteriyor: Disclaimer sadece YouTube'da ✅. Ama Facebook uzun metni ve iki LinkedIn metni de klinik süreç anlatıyor (3D yürüme analizi, rehabilitasyon, biyomekanik ayarlar, hazırlık dönemi/bandajlama/kompresyon). YMYL eşiği bu içerikler için de geçerli ve v07 web sayfası kendi disclaimer'ını taşıyor. Asimetri için gerekçe verilmemiş.

**Önerilen hamle.** FB uzun ve LinkedIn şirket metinlerinin sonuna tek satır uyum kaydı ("Bu içerik genel bilgilendirme amaçlıdır; kişiye özel tıbbi tavsiye yerine geçmez.") — ya da neden gerekmediği yazılı gerekçeyle kapatılsın. Karakter bütçesi buna müsait (LinkedIn 1.350/2.000).

---

### 🟡 D8 · [Atlanmış Soru] "Yüksek Teknoloji … Uygulama Merkezi" tescilli ticari unvan mı, yoksa kalite iddiası mı? Kimse sormamış.

Bu descriptor iki **en tüketiciye dönük** yüzeyde birinci satırda duruyor (IG bio satır 1, FB kısa bio). Dosya onu dokunulmaz kabul ediyor: *"kilitli bir dizgi; ondan kelime düşürmek kilidi bozmak olur."* Doğru — KKK açısından. Ama mevzuat açısından hiç sorgulanmamış.

Çatal net:
- **Tescilli/ruhsattaki unvansa** → bir addır, iddia değildir, sorun yok. En güvenli zemin.
- **Branding'in ürettiği tanımlayıcıysa** → "Yüksek Teknoloji", sağlık hizmeti yüzeyinde **belgelenmemiş bir nitelik sıfatıdır** ve M.5'in üstünlük/karşılaştırma ile 18/6'nın "olmayan özelliği var gösterme" kalemlerine değer. Dosya "tek bir üstünlük sıfatı yok" diyor — markanın kendi tanımlayıcısındaki sıfatı saymadan.

Bu, KKK ile mevzuatın kesiştiği ve kimsenin bakmadığı nokta. KKK bir kalemi kilitlemiş olması onu uyum denetiminden muaf tutmaz.

**Önerilen hamle.** Ticaret sicil/ruhsat unvanı belgeyle teyit edilsin. Tescilliyse dosyaya not düşülür ve konu kapanır (ayrıca en güçlü savunmadır). Değilse avukat sorusuna eklenir — ve gerekirse KKK ana belgesi güncellenir, sosyal metin tek taraflı değiştirilmez.

---

### 🟡 D9 · [Tutarlılık] KKK kısa hâli "&" ile kilitli; metinlerde "ve" olarak geçiyor. Öz-denetimin "birebir" iddiası bu kalemde yanlış.

KKK §2: kısa hâl **"Özgür Irmak Protez & Ortez"**. Bağımsız taramam: dosyada "&" 4 kez, **"ve" 2 kez** (satır 122 LinkedIn şirket Hakkında açılışı, satır 197 YouTube açıklaması).

Düzyazı içinde "ve" doğal bir tercih olabilir — itiraz ettiğim bu değil. İtirazım: dosya aynı anda ① Açık Kalem 6 ile hesap adlarının "&" hâline **standardize edilmesini** öneriyor ② öz-denetim kapısı 1'de *"kısa hâl… birebir"* diyor ③ gövde metninde kuralsızca "ve" kullanıyor. Kural yazılmadan üç farklı davranış.

**Önerilen hamle.** KKK'ya tek satır: *"'&' hesap adı/wordmark dizgisinde; düzyazı içinde 've' serbest."* Kural yazılınca tutarsızlık tutarlılığa dönüşür. Yazılmazsa her yüzeyde yeniden tartışılır.

---

### 🟡 D10 · [Bilgi Kalitesi] Tarama kapsamı metnin tamamını ölçmüyor; rapor bunu belirtmiyor.

`sozdizim_tarama.py` liste satırlarını (`- ` ile başlayanlar) ölçüm dışı bırakıyor. Sonuç:
- LinkedIn şirket: metin **177 kelime**, ölçülen **110** → 5 maddelik cihaz listesi (67 kelime, metnin %38'i) hiç taranmamış.
- YouTube: metin **131 kelime**, ölçülen **84** → "Videolarda ne var" listesi taranmamış. **"✅ TEMİZ"** hükmü metnin %36'sını kapsamıyor.

Rapor kelime sayılarını tabloda dürüstçe vermiş (84, 110) ama farkın **ölçülmemiş içerik** olduğunu söylememiş; okur "TEMİZ" ibaresini tüm metne ait sanır.

Ayrıca kapsam beyanı da gevşek: slop taramasında *"iki LinkedIn bloğu"* denmiş, oysa dört LinkedIn bloğu var (slogan, şirket Hakkında, headline, kişisel Hakkında). **Ben on bloğun hepsini taradım — hepsi temiz**, yani içerik olarak sorun yok; sorun kapsam iddiasının doğruluğunda.

**Önerilen hamle.** Tarama tablosuna "ölçülen/toplam kelime" sütunu eklensin. Liste ağırlıklı metinlerde hüküm "prosa katmanı temiz" diye yazılsın, "metin temiz" diye değil.

---

### 🟡 D11 · [Devil's Advocate] 88/100 savunulamaz — hem yöntem hem tek kalem olarak.

**Yöntem itirazı.** Alt puanlar (26/30, 23/25, 20/20, 14/15, 5/10) ölçüm gibi görünüyor ama arkalarında ölçüm yok; hepsi yargı. Bu, OS'un kendi yasakladığı örüntü: *veri olmadan sayısal puan verme — gözlemi performans gibi sunma* (Tip A/B testi). Gerçek Tip A ölçümler bu dosyada var ve iyi (karakter sayıları, sözdizim skorları) — ama onların yanına aynı ondalık hassasiyetle yargı puanları dizilince ikisi ayırt edilemez hâle geliyor. Ayrıca ajanın kendi çıktısına not vermesi ve *"skor 92-93 bandına oturur"* diye kendi gelecek notunu öngörmesi, maker-checker ayrımının puan üstünden delinmesidir.

**Tek kalem itirazı: Doğruluk 20/20 ayakta duramaz.** D2 ve D3 kaynaksız iki olgu gösteriyor; dahası "Uydurma sıfır" şerhi **yanlış künye beyanı** içeriyor (Ataşehir'i v07 havuzuna atfediyor). Doğruluk kaleminin tam puan aldığı yer, dosyanın en zayıf olduğu yer.

**Önerilen hamle.** Sayısal öz-puan kaldırılsın; yerine kapı listesi (geçti/geçmedi/gerekçe) kalsın — zaten var ve daha kullanışlı. Puan tutulacaksa Tip B olarak işaretlensin ve **Denetmen verir, Metin Yazarı değil.**

---

### 🟡 D12 · [Değer Uyumu + Devil's Advocate] Beş yüzeyde tekrarlanan ayırt edici varlık yanlış seçilmiş: markanın onur duruşu hiçbir yerde yok.

Raporun kendi tutarlılık okuması: tekrarlanan üç sinyal **1998 · Ataşehir · kendi atölyemizde üretim.**

**İtiraz.** "Kendi atölyemizde üretim" bir **kapasite**dir; sermayeyle satın alınabilir ve rakip bir CNC aldığı gün aynı cümleyi kurabilir. Ayırt edici varlık (Sharp/Ehrenberg-Bass) taklit edilmesi zor olandır.

Markanın gerçekten taklit edilemez duruşu v07'de yazılı ve **onaylı**: *"Kimseye hedef koymuyoruz. Kimin nereye yürümek istediğine kendisi karar verir."* Bu, KKK'nın özerklik/onur çekirdeğidir, Steps On Clouds misyonuyla birebir örtüşür ve rakiplerin çoğunun söyleyemeyeceği tek cümledir.

Bu duruşun izi **beş yüzeyin hiçbirinde yok.** Buna karşılık cihaz/tezgâh envanteri hepsinde var — üstelik D1 uyarınca envanter hukuken en kırılgan katman. Yani dosya, **hukuken en riskli malzemeyi her yerde tekrarlamış, etik olarak en güçlü ve en güvenli malzemeyi hiç kullanmamış.**

Onur merceğinde teknik ihlal yok (acıma yok, ilham pornosu yok, "vaka" dili yok, özne nesneleşmiyor — bunlar temiz). Ama KKK ses kuralı 2'nin testi *"okuyan neyi öğrenmiş oldu?"* — bu metinlerde cevap "atölyede hangi makineler var". Ses kuralı 3'ün "birlikte dili / ortak fiiller" gereği de kapanış cümlesi dışında karşılıksız. Metinler **merkezi** anlatıyor, **süreci birlikte yürüyen kişiyi** değil. Metin Yazarı'nın kendi verdiği −1 ("onur çerçevesi örtük") bunu doğru sezmiş, ama "bio türünün sınırı" diye kapatmış. Sınır değil bu; tercih.

**Önerilen hamle.** Kat 1 (cihazsız) varyantları yazılırken boşalan yere envanter değil **özerklik cümlesinin bir türevi** konsun. Bu tek hamle üç şeyi birden çözer: uyum riskini düşürür (D1), somut çapa kaybını marka anlamıyla telafi eder, ve markayı taklit edilebilir bir kapasite iddiasından ayırır.

---

### 🟡 D13 · [Bilgi Kalitesi] "İnsan işareti" açığının kapanacağı iddiası fazla iyimser.

Rapor: *"Özgür Bey'in alıntısı geldiğinde LinkedIn kişisel profil bu eşiği kendiliğinden geçer."* Doğru — **ama yalnız o metin için.** Eşik altı üç metin var: FB uzun (7,8), LinkedIn şirket (9,1), LinkedIn kişisel (—). Tek alıntı bir metni kurtarır; diğer ikisi eşik altında kalır ve rapor bunu kapanmış gibi sunuyor.

**Önerilen hamle.** Ya iki metin için de birer insan işareti planlansın (kurumsal ağızdan gerçek bir soru ya da ikinci bir alıntı), ya da açıkça yazılsın: *"FB uzun ve LinkedIn şirket metinlerinde insan işareti eşik altında kalacaktır; tür gereği kabul edilen kalıcı sapmadır."* İkisi de savunulabilir; belirsiz bırakmak savunulamaz.

---

### 🟡 D14 · [Red Team] "Merkez ziyareti için bize yazabilirsiniz" — M.5'in ilk yasağı "talep yaratma/yönlendirme".

LinkedIn şirket kapanışı: *"Meslektaş görüşmesi ve merkez ziyareti için bize yazabilirsiniz."* Rapor bunu "davet, satış değil" diye savunuyor ve meslek mensubu muhataba dayanıyor (17-19 serbest kanal).

Savunma büyük ölçüde geçerli — ama **LinkedIn şirket sayfası herkese açıktır**; 19/4 "profesyonel bilgiye erişim meslek mensuplarıyla sınırlı tutulur" derken erişim kontrolü ima ediyor, açık sayfa bunu sağlamıyor. "Meslektaş görüşmesi" ibaresi muhatabı daraltıyor, "merkez ziyareti" ise daraltmıyor.

Düşük-orta risk, ama bedava kapatılabilir.

**Önerilen hamle.** Daraltıcı ibare eklensin: *"Meslektaş görüşmesi ve merkez ziyareti için sağlık meslek mensupları bize yazabilir."* Avukat listesine ayrıca sorulsun: açık B2B sayfasında 17-19 rejimi geçerli mi, yoksa erişim kontrolü mü gerekiyor?

---

### 🟢 D15 · [Not — bulgu değil] v07 kanon dışı bir kıdem ifadesi taşıyor; biyografiler ondan temiz.

Ters yönde bir tutarsızlık: onaylı v07'nin giriş cümlesi *"…Protez ve Ortez'de **yirmi sekiz yıldır** seri üretim yok…"* diyor. KKK'nın tanıdığı tek türev "çeyrek asrı aşkın"; "yirmi sekiz yıl" kanon dışı. Biyografiler bu tuzağa düşmemiş.

Yani **kanon uyumu bakımından yeni metinler onaylı metinden daha temiz.** v07 Wix'e yüklendiği için bu canlı bir sapma.

**Önerilen hamle.** v07'nin o ifadesi "1998'den beri"ye çevrilsin ya da KKK'ya üçüncü onaylı türev olarak "yirmi sekiz yıldır" eklensin. Karar Branding'in; ama iki yüzey aynı anda iki farklı kıdem dili konuşmamalı.

---

## ÇELİŞKİ (alt roller arası)

**Devil's Advocate ↔ Red Team — cihaz envanteri.**
- *Devil's Advocate:* Envanteri çıkarmak metnin somut çapasını daha da düşürür (zaten FB 3,9 / LinkedIn kişisel 4,2 ile eşik altında). Cihaz adları metnin en somut malzemesi; atılırsa geriye soyut süreç dili kalır — yani **"AI yazmış" redine geri dönüş riski.** Kök neden kuralı da bunu söylüyor: soyutluk brif açığıdır.
- *Red Team:* Envanter hukuken en kırılgan katman ve projenin kendi planı onu gate'lemiş.

**Denetmen sentezi:** Çelişki gerçek ama çözülebilir — ve çözümü D12'dir. Boşalan yer **süreç somutluğu ve özerklik anlatısıyla** doldurulur (ölçü alma, koşu bandı ölçümü, teslim sonrası takip, kişinin kendi kararı), cihaz *adlarıyla* değil. Süreç somutluğu 15/1-a kapsamında değil; sayılabilir çapa da üretir. Yani "somutluk mu uyum mu" ikilemi yanlış ikilem. **Ayhan'a taşınan gerçek karar bu değil; Açık Kalem 7'deki eksik olgu listesinin ne zaman kapanacağı** — çünkü D12'nin önerdiği dolgu da, sözdizim eşikleri de asıl orada çözülüyor.

---

## SORULMAMIŞ SORULAR

1. **Bu hesaplar neden şimdi açılıyor?** Dosya beş yüzeyi eşzamanlı dolduruyor. Ama plan §2 sosyal medyayı avukat kapısına bağlamış ve Growth kapasitesi teyit edilmemiş. **Beş yüzeyi birden açmak, beşini birden beslemek demek.** YouTube'da dört format taahhüt edildi; üretilmezse kanal ölü görünür ve E-E-A-T açısından yoklukan kötüdür. Faz sırası sorulmamış: hangi iki yüzey önce?
2. **Kim yönetecek?** M.5 yorum/DM yükümlülükleri (hasta görselinde yorum açık bırakma yasağı, testimonial barındırma) günlük moderasyon gerektiriyor. IG stratejisinde 4 senaryoluk yanıt protokolü var — **ama yalnız IG için.** FB, LinkedIn ve YouTube yorumları için protokol yok. Kanal sayısı dörde çıkarken protokol birde kaldı.
3. **Hesap adı/handle değişikliğinin maliyeti ölçülmedi.** Açık Kalem 6 dört yüzeyde ad değişikliği öneriyor. LinkedIn özel URL ve Facebook kullanıcı adı değişiklikleri **sayı sınırlıdır** ve mevcut geri bağlantıları kırar. Kaç takipçi/geri bağlantı riske giriyor — bilinmiyor, ölçülmemiş.
4. **Özgür Bey'in tek cümlesi ne zaman gelecek?** v07'de (8 Ağu) açıktı, bu dosyada (14 Ağu) hâlâ açık. Aynı slot iki teslimi birden bekletiyor. Bu artık bir metin sorunu değil, **bir tahsilat sorunu** — Ayhan'ın tek telefonuyla kapanacak iş, iki hafta iki dosyayı asılı tutuyor.
5. **Öğretim görevliliği belgesi** aynı durumda: v07'de ⟦BELGE BEKLİYOR⟧, burada Açık Kalem 7. Dosyanın kendi ifadesiyle *"E-E-A-T açısından en yüksek getirili tek belge"* — ve iki teslimdir bekliyor. Belge talebi mesajı (`ozgur-irmak-belge-talebi-mesaj.md`) gönderildi mi, yanıt geldi mi? Dosyada iz yok.

---

## KARAR ÖNERİSİ

☑ **DÜZELT — Metin Yazarı + Growth/İçerik + Ayhan**

**Yayın öncesi bloke edenler (🔴):**
| # | Kim | Ne |
|---|---|---|
| D2 | Ayhan → Özgür Bey | Semt teyidi. Gelene kadar "İstanbul"a indir veya çıkar. "Uydurma sıfır" künye beyanını düzelt. |
| D3 | Ayhan → Özgür Bey | Miyoelektrik/mikroişlemcili kapasite teyidi + belge. Teyitsizse çıkar. |
| D1 | Metin Yazarı | Her yüzey için **Kat 1 (cihazsız)** varyant. YouTube içerik vaadi #3 Kat 1'den çıkar. Avukat sorusu #11 keskinleştirilir. |
| D4 | Growth/İçerik → Ayhan | Eski içerik denetimi + FB Öneriler kapatma + eski "Hakkında" hizalama. **Bio yayınından önce.** Silme Kademe 3 = Ayhan. |

**Yayın öncesi düzeltilecekler (🟡):** D5 (FB alan doğrulaması) · D6 (disclaimer "yerine geçmez"e dön) · D7 (disclaimer asimetrisi) · D8 (descriptor tescil teyidi) · D14 (B2B daraltıcı ibare)

**v0.2'ye taşınabilecekler (🟡):** D9 (& / ve kuralı → KKK) · D10 (tarama kapsam sütunu) · D11 (öz-puan kaldır) · D12 (özerklik cümlesi — Kat 1 yazımıyla birlikte) · D13 (insan işareti kararı) · D15 (v07 kanon düzeltmesi)

**Ayhan'a eskalasyon (karar gerektirenler):** ① faz sırası — beş yüzey birden mi, kademeli mi (Sorulmamış Soru 1) ② Özgür Bey'den bekleyen iki kalem (cümle + belge) için termin ③ 🕊 emoji ve "güdük" kalemleri Branding'de zaten açık — bu turda kapanmıyor.

---

## FOX'A KONSENSÜS NOTU

**Anlaşmazlık yok — kapsam genişletmesi var.**

Metin Yazarı'nın işçiliğine itirazım yok ve bunu ölçerek söylüyorum: karakter sayılarının tamamı doğru, tarama sonuçlarının tamamı birebir tuttu, SERT bulgu gerçekten yok, slop temiz, kanonik kıdem disiplini kusursuz, IG carve-out ayrımı bu dosyanın en iyi kararı. **Beyan edilen sayılara güvenilebilir** — bu, bir önceki turlardan sonra kayda değer bir güven sinyali ve tutanağa geçirilmeli.

Bulguların ağırlık merkezi metinde değil, **metnin etrafında**: kanalın hangi kuşakta olduğu (D1), iki olgunun nereden geldiği (D2/D3), hesapların zaten dolu olduğu (D4). Bunların hiçbiri "kötü yazılmış" demek değil; hepsi "iş, yazı işinden büyükmüş" demek. Metin Yazarı'nın kapsamı metindi ve o kapsamda iyi iş çıkardı — **eksik olan orkestrasyon: bio yazımı bir migrasyon projesinin son adımıdır, ilk adımı değil.** Sıralamayı Fox kurar, Metin Yazarı değil.

İki sistemik ders, ikisi de tek vakadan büyük:
1. **Zemin belgesine atıf yaparken bölüm numarası doğrulanmalı.** D1'in tamamı, §2'de yazan bir kuralın §1'e atfedilmesinden doğdu. Tek satırlık bir yanlış atıf, tüm uyum değerlendirmesini yanlış yatağa oturttu.
2. **Ölçüm aracı hukuki lafza dokunamaz.** D6 bunun canlı örneği. `metin-yazari.md` İnsan Sesi Kapısı'na muafiyet kuralı yazılmalı — yoksa Goodhart dersi her turda yeniden öğrenilir.

Ayrıca bir denetim zinciri açığı: **"Uydurma sıfır" tipi künye beyanları bugüne kadar doğrulanmadan kabul ediliyordu.** D2 bunun ilk yakalanışı. Bundan sonra her "kaynağı şudur" beyanı örneklemle sınanmalı — beyanın kendisi delil değildir. Bu kuralı Denetmen tarafında Verification'ın standart adımına ekliyorum.

---

*Denetmen v2 · Faz 3 Orkestratör · 14 Ağustos 2026 · Alt roller: Devil's Advocate · Red Team · Verification · Sonraki denetim: v0.2 (Kat 1 varyantları + D2/D3 teyitleri geldiğinde)*
