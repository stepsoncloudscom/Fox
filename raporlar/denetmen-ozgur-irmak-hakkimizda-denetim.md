# DENETMEN RAPORU (Orkestratör Sentezi) — Özgür Irmak Hakkımızda Sayfası (TR + EN)

*Tarih: 3 Ağustos 2026*
*Denetlenen: Metin Yazarı — `raporlar/ozgur-irmak-hakkimizda-v01.md` (v0.1)*
*Çağrılan alt roller: **Red Team + Verification + Devil's Advocate** — üç mercek de bu turda orkestratör tarafından inline uygulandı (dış temas metni + olgu iddiası + mimari karar bir arada; bulgu satırlarında mercek belirtilir).*
*Zemin: KKK (`ozgur-irmak-branding-kilitli.md`) · medikal paket §A/§C/§D · `ozgur-irmak-uyumlu-ticaret-plani.md` §0.B/§1/§2 · web şeması · blog v0.3 (onaylı lafız) · ürün metinleri uyum planı §3.4 (onaylı kapanış).*

---

## GENEL DURUM

Metin, kalite tabanının **üstünde**. Ham SEO yığınından okunur bir anlatı çıkarılmış; Türkçe glyph temiz; yasak kelime taraması (mevzuat + onur + AI-klişe) bağımsız tekrarımda da **temiz** — "en iyi/tek/lider/garantili/kesin çözüm/%X başarı/kampanya/hemen arayın" sıfır, ünlem sıfır, ilham pornosu sıfır, seçicilik sinyali sıfır. Kaynak disiplini ciddi: çelişkili ham veri (Proteor/Nabtesco, çoğul merkez, insoles unit, şehir) metne alınmamış, E'de sorulmuş. Beyan edilen kelime sayıları bağımsız sayımla doğrulandı (A 466 / B 114 / C 546 / C.1 109 — fark yalnız kapanış tagline'ının sayıma dahil edilip edilmemesi; sapma yok).

Bulgular bunun üstüne biniyor: **3 DUR · 10 DÜZELT · 6 NOT.** DUR'ların hiçbiri "metin kötü" demiyor; üçü de **metnin doğru, ama kapının yanlış yere çizilmiş olmasıyla** ilgili.

Ana teşhis tek cümlede: *Metin Yazarı doğru soruları sordu ama gate'i bir kademe aşağıya çizdi — cümleyi bayrakladı, sayfayı bayraklamadı; kelimeyi Branding'e gönderdi, mevzuata göndermedi; "uydurmadım"ı "doğru"ya eşitledi.*

---

## BULGULAR

### 🔴 DUR

---

**D1. [Red Team / Tutarlılık] EN sürümün TAMAMI sarı kuşakta — Metin Yazarı yalnızca C.2 bloğunu gate'ledi, oysa gate C bölümünün bütününü kapsıyor.**

**Kanıt:**
- `ozgur-irmak-uyumlu-ticaret-plani.md` §2 (SARI KUŞAK / madde 3): *"…o zamana dek **EN/AR/RU yayın yok**."* Bu, tek bir cümlenin değil, **yabancı dilli yayının tamamının** avukat kapısında olduğunu söylüyor.
- Aynı belge §0.B: 2025 tarihli Sağlık Hizmetlerinde Tanıtım Yönetmeliği M.8, yurt dışına yönelik tanıtımı **"AYRI internet sitesi veya sosyal medya hesabı"** koşuluna bağlıyor; belge bunun üzerine **"🚩 MİMARİ ETKİ — WEB ŞEMASI REVİZYON BAYRAĞI"** koymuş ve iki-katlı mimari önermiş (① TR kurumsal site ② ayrı uluslararası property).
- Metin Yazarı C bölümünün lokalizasyon notunda dayanağını açıkça beyan ediyor: *"EN okuru büyük ölçüde uluslararası hasta funnel'ının ilk temasıdır (web şeması §1)"* — yani metnin kendi beyanına göre bu sayfa **tam da M.8'in düzenlediği faaliyetin** ilk halkası.
- Dayanak alınan `ozgur-irmak-web-semasi.md` hâlâ **tek-site / 4-dil** mimarisini anlatıyor ve 4 Tem'de konan revizyon bayrağını **taşımıyor**. Metin Yazarı, üzerinde açık revizyon bayrağı olan bir belgeyi yürürlükteki şema sanarak inşa etmiş — kusur onun değil, belgenin güncellenmemiş olması.

**Neden DUR:** Sorun EN metninin içeriği değil (iddia seviyesi TR ile aynı, temiz). Sorun **kabı**: mimari kararı düşmeden EN'in nereye yazıldığı bilinmiyor. İki-katlı mimari benimsenirse EN Hakkımızda'nın evi değişir **ve rejimi de değişir** — M.8 tarafında hasta hikâyesi ve sponsorlu tanıtım serbest, yani EN metni TR'nin aynadaki görüntüsü olmak zorunda değil; muhtemelen **baştan farklı yazılması gerekir.** Şu hâliyle EN, yanlış kaba dökülmüş doğru bir metin olma riski taşıyor.

**Önerilen hamle:**
1. §C ve §C.1 **"onaya hazır" statüsünden çıkarılır**, `⏸️ MİMARİ KARARA BAĞLI TASLAK` olarak etiketlenir. Yayın değil, revizyon riski taşıdığı için Ayhan'a "bitti" diye sunulmaz.
2. TR (§A + §B) yolundan devam eder — avukat gate'ine **tek başına** girebilir. Bu bir durdurma değil, **ayrıştırma**: TR ilerler, EN mimariyi bekler.
3. `raporlar/ozgur-irmak-web-semasi.md`'ye 0.B revizyon bayrağı **bugün işlenir** (Fox). İşlenmezse sonraki her ajan aynı bayat mimariyi devralır — bu, `[[denetim-zinciri-acigi-yakalayamadi]]` dersinin birebir tekrarı olur: çıktıyı düzeltip merceği düzeltmemek.

---

**D2. [Verification / Doğruluk] Kurumsal "1998" iddiası metinden temizlenmiş ama SEO katmanından sızıyor — üç yerde. Ayrıca 1998 değerinin kendisi hâlâ belge-teyitsiz.**

**Kanıt — sızıntı noktaları:**
| Yer | Lafız | Sorun |
|---|---|---|
| §B, 1. cümle | "Özgür Irmak Protez ve Ortez **Merkezi**, 1998'den beri … yapıyor." | Özne **kurum**. Ham kaynakta merkezin kuruluş yılı YOK. |
| §D.1 Title | "Hakkımızda \| Özgür Irmak Protez ve Ortez, **1998'den Beri**" | Kurum adı + tarih = kurumsal kıdem beyanı. Title tag arama sonucunda **metinden daha çok okunur**. |
| §D.2 Title alt. 2 | "About Us — Prosthetic and Orthotic **Center Since 1998**" | Aynı iddianın EN'i, hem de açık lafızla. |

Metin Yazarı §B sızıntısını kendi bayrağında (F.3/2) yakalamış — **ama iki title'ı yakalamamış** ve kendi F.2 taramasından "temiz" notuyla geçirmiş.

**Kanıt — değerin kendisi:** `ozgur-irmak-marka-kimligi-v01.md` §1.1: *"1998 — **Ayhan beyanı**… **Yayın öncesi müşteri belge teyidi şarttır** — ⚠️ eski araştırma notları **1999** diyordu… fark çıkarsa tüm türev belgeler yeniden taranır."* Yani 1998 **Tip B**'dir (beyan), Tip A (belge) değil. Metin Yazarı bunu Doğruluk 20/20 ile kapatmış.

**Neden DUR:** Bu, tek sayfalık bir hata değil — kıdem çapası **her kanalda tekrarlanacak** ve YMYL sayfasında yanlış kurumsal kıdem beyanı, 2025 yönetmeliği M.18/6 çerçevesinde "olmayan özelliği var gösterme" bandına yaklaşır. Bir de pratik risk var: eski site/ticaret sicili/Google profilinde farklı bir yıl duruyorsa çelişki dışarıdan görülür.

**Önerilen düzeltme lafzı:**
- §B ilk cümle → *"Özgür Irmak Protez ve Ortez Merkezi'nin kurucusu **Özgür Irmak, 1998'den beri** protez ve ortez uygulamaları yapıyor."* (özne kişiye döner, kıdem korunur)
- §D.1 Title → **"Hakkımızda | Özgür Irmak Protez ve Ortez Merkezi"** (48 kr). Tarih belge teyidine kadar title'dan çıkar.
- §D.2 Title alt. 2 → **silinir**; alt. 1 kalır.
- **Belge teyidine kadar gövde dilinde tercih "çeyrek asrı aşkın" olur.** Gerekçe: 1998 → 28 yıl, 1999 → 27 yıl; **ikisi de "çeyrek asrı aşkın"dır.** Yani bu türev, 1998/1999 belirsizliğine karşı dayanıklı; "1998'den beri" değil. Belge gelince tarih geri açılır.

**KKK'nın kendisi düzeltme gerektiriyor mu — evet, ama küçük.** KKK §1 tagline'ı ("1998'den beri ustalık…") dilbilgisel olarak **doğru**: özne "ustalık", yani kişiye ait. Düzeltilmesi gereken KKK'nın *sessizliği*. KKK'ya §1'e tek satır eklenir:

> **1998 = Özgür Bey'in mesleki başlangıcıdır (kişi çapası).** Merkezin kuruluş yılı ayrı ve şu an bilinmeyen bir veridir; kurumsal özneyle ("Merkez 1998'den beri…") **kullanılamaz**. Belge teyidine kadar tercih edilen türev: "çeyrek asrı aşkın".

---

**D3. [Red Team / Verification] Disclaimer birleşimi "yeni lafız" değil — onaylı koruyucu cümlenin DÜŞÜRÜLMESİ. Metin Yazarı'nın bayrağı doğru ama şiddeti eksik.**

**Kanıt — üç metnin karşılaştırması:**

| Kaynak | Lafız |
|---|---|
| Blog v0.3 (**avukat "aynen" onayladı**, 30 Tem) | "Bu içerik genel bilgilendirme amaçlıdır; kişiye özel tıbbi tavsiye ya da tanı yerine geçmez. **Kendi durumunuz için merkezinize ya da hekiminize danışın.**" |
| Ürün metinleri (onaylı kapanış, 29 Tem) | "Cihazın uygunluğu kişiye özel değerlendirme ile belirlenir; uygulama ve uyarlama merkezimizde teknik sorumlu tarafından yapılır." |
| **Hakkımızda birleşimi** | "Bu **sayfa** genel bilgilendirme amaçlıdır; kişiye özel tıbbi tavsiye ya da tanı yerine geçmez. Cihazın uygunluğu … teknik sorumlu tarafından yapılır." |

**Birleşimde kaybolan:** *"Kendi durumunuz için merkezinize ya da **hekiminize** danışın."* — Bu, disclaimer'ın **işlevsel** cümlesidir. İlk cümle sorumluluğu *reddeder*; kaybolan cümle okuru *doğru mercie yönlendirir*. Onun yerine gelen cümle okuru **merkeze** yönlendiriyor, hekime değil.

**Neden DUR:** YMYL sayfasında "tıbbi tavsiye değildir" demek ama hekime yönlendirmemek, koruyucu işlevi olmayan bir feragattir; üstelik yönlendirmenin hedefi hizmeti satan tarafa kaymış oluyor. Bu, avukatın onayladığı dengenin **içeriğinin** değişmesidir, sadece lafzının değil. "Onaylı sayılmaz" bayrağı doğru ama yetersiz — bu hâliyle avukata gitse bile, gitmeden önce zaten düzeltilmesi gereken bir gerileme.

**Önerilen düzeltme — birleştirme, YAN YANA KOYMA:**
> *Bu içerik genel bilgilendirme amaçlıdır; kişiye özel tıbbi tavsiye ya da tanı yerine geçmez. Kendi durumunuz için merkezinize ya da hekiminize danışın.*
>
> *Cihazın uygunluğu kişiye özel değerlendirme ile belirlenir; uygulama ve uyarlama merkezimizde teknik sorumlu tarafından yapılır.*

Her iki cümle **birebir onaylı hâlleriyle** durur ("sayfa" değişikliği dahil hiçbir kelime oynatılmaz — "içerik" bir sayfayı da kapsar). Avukata giden soru "yeni lafzı onaylar mısınız?" değil, çok daha ucuz olan **"iki onaylı lafzın aynı sayfada yan yana durmasında sakınca var mı?"** olur.

**EN disclaimer ayrıca bayraklı:** EN'de bugüne kadar **hiçbir** lafız avukat onayı almadı. §C'deki EN disclaimer, birleştirilmiş TR'nin çevirisi — yani iki kat onaysız. D1 gereği zaten beklemede; oraya not düşülür.

---

### 🟠 DÜZELT

---

**Z1. [Red Team / Atlanmış Soru] "protetist" bir mevzuat unvanı değil — bu kelime Branding'e değil, avukat/mevzuat kapısına gider. Eskalasyon yanlış adrese yapılmış.**

**Kanıt:** Ismarlama Protez ve Ortez Merkezleri Yönetmeliği'nin personel terminolojisi **"ortez ve protez teknikeri / teknisyeni"** (sağlık meslek yüksekokulu / meslek yüksekokulu mezunu sağlık teknikeri) ve **"sorumlu müdür"**. "Protetist" bu metinlerde geçen bir unvan değil, İngilizce *prosthetist*'in doğrudan aktarımı. Ürün metinlerinde **tam olarak bu sebeple** "uzman → teknik sorumlu" düzeltmesi yapılmıştı (Ayhan, 29 Tem: *"'uzman' hukuken yanıltıcı çağrışım riskli"*). Aynı gerekçe "protetist" için de geçerli, hatta daha güçlü: "uzman" en azından genel bir sıfat; "protetist" **unvan gibi** okunur.

Metin Yazarı bunu E.1'de "kelime kararı" diye Branding'e eskale etmiş. Yanlış routing: bu bir zevk/ton kararı değil, **unvan beyanı** kararıdır — 18/6 "ekip yeterliliği hakkında yanlış bilgi" bandına dokunur.

**Önerilen düzeltme lafzı** (her iki geçiş için):
- "Merkezimizde **protetistler** ve fizyoterapistler…" → *"Merkezimizde **teknik kadromuz** ve fizyoterapistler…"*
- "…**deneyimli protetistler** tarafından yapılır" → *"…**merkezimizin teknik kadrosu** tarafından yapılır"* (Z2'yi de aynı hamlede kapatır)
- EN: "experienced prosthetists" → *"our technical team"*
- Nihai terim seçimi (teknik kadro / ortez-protez teknikeri / teknik sorumlu) **avukat sorusuna** eklenir — Branding'e değil.

---

**Z2. [Verification / KKK Ses Kuralı 1] "deneyimli protetistler" kanıtsız yetkinlik sıfatıdır — ve "ham kaynaktan geliyor" savunması bu dosyada geçersiz.**

**Kanıt:** KKK §2 Ses kuralı 1: **"Kanıt konuşur — sıfat yerine belge."** Metin Yazarı bu sıfatı F.1/1'de *"tek nitelemedir ve ham kaynaktan gelir"* diyerek geçirmiş. Ama ham kaynak, müşterinin **kendi eski pazarlama metnidir** — yani temizlenmekte olan şeyin ta kendisi. `ozgur-irmak-urun-metinleri-uyum-plani.md` §0 aynı kaynağın karakterini zaten tespit etmiş: metinlerin çoğu üreticinin pazarlama metninin çevirisi, %25'i Wix placeholder. Bir sıfatın gerekçesi olarak "ham kaynakta vardı" demek, döngüsel: kaynak zaten uyum turunun **konusu**, dayanağı değil.

Ek olarak: kadro sayısı ve nitelikleri **teyit edilmemiş** (E-5 açık). Kaç kişi, hangi belge — bilinmiyor. Bilinmeyen bir kadroya "deneyimli" demek, tanımı gereği kanıtsız.

**Önerilen hamle:** Z1'deki düzeltmeyle birlikte sıfat düşer. Kadro belgeleri (çalışma belgesi/diploma) geldiğinde sıfat yerine **veri** gelir: *"Merkezimizde ortez-protez teknik kadrosu ve fizyoterapistler birlikte çalışır."* + künyede gerçek isim/unvan (bkz. Z5).

---

**Z3. [Verification / Red Team] Marka listesinde üç ayrı hata var — ve liste zaten bu sayfaya ait değil.**

**Kanıt (bağımsız doğrulama, 3 Ağu):**
1. **"Touch Bionic" yanlış yazım** — şirketin adı **Touch Bionics**'tir (2016'da **Össur** tarafından satın alındı). Yani liste hem markayı yanlış yazıyor hem de sahibini **iki kez** sayıyor (Össur + Touch Bionics).
2. **"Bebionic"** — Ottobock'un markası (2017'de Steeper'dan satın alındı) ve üretici kendi yazımında **küçük harfle "bebionic"** kullanıyor. Burada da aynı yineleme: Ottobock + bebionic.
3. **"X5 Liner" doğrulanamadı.** Ottobock / Össur / ALPS ürün hatlarında bu adla bir liner bulunamadı (Tip B — yokluğu kanıtlanmış değil, ama üç büyük üreticinin katalog aramasında karşılığı çıkmıyor). Ham kaynakta transkripsiyon hatası olması kuvvetle muhtemel (ör. Genium X3/X4 ile karışma).

**Neden önemli:** Bu, güven inşa etmek için konmuş bir listenin **güveni bozması** demek. Sayfayı okuyan bir meslek mensubu ya da bilgili hasta yakını "Touch Bionic" ve "X5 Liner"i görünce metnin denetlenmediğini anlar. E-E-A-T açısından ters etki.

**Ortaklık iması sorusuna cevap:** Metin Yazarı'nın formülasyonu ("Kullanılan protez sistem ve materyalleri arasında … ürünleri bulunur") **ortaklık ima etmiyor** — "ile beraber çalışılmaktadır" kalıbından kaçınması doğru karar, F.3/5'teki tereddüdü yersiz. **Asıl mesele lafız değil, yer.**

**Önerilen hamle — yeniden yazma değil, TAŞIMA:**
- Marka listesi cümlesi **Hakkımızda'dan çıkarılır**. Web şeması §1'de bu içeriğin adresi zaten var: **"Teknoloji & Çözüm Ortakları"** sayfası. Hakkımızda'da tutmanın SEO getirisi ~sıfır (marka adları bu sayfa için düşük niyetli), hukuki maruziyeti ise avukat #1 + #8'in tamamı.
- Liste o sayfaya taşınırken **her ad üreticinin kendi güncel yazımından tek tek doğrulanır** ve ana marka/alt marka yinelemeleri temizlenir.
- ⚠️ Ayrıca not: hedef sayfanın **adı** ("Çözüm **Ortakları**") ortaklık imasını başlıkta taşıyor. Metin bundan kaçınırken sayfa başlığı iması kuruyor. Bu, ayrı bir DÜZELT kalemi olarak İçerik/Growth'a düşer (öneri: "Kullandığımız Teknolojiler").

---

**Z4. [Kalite Tabanı / Sahte Kesinlik — Tip A/B] "Doğruluk 20/20" ve "TOPLAM 95/100 — A" savunulamaz.**

**Kanıt:** Aynı belgenin E bölümünde **10 açık olgu sorusu** ve E.1/E.2'de **5 çözülmemiş karar** duruyor: kuruluş yılı bilinmiyor, üniversite eğitimi teyitsiz, kadro sayısı teyitsiz, CAD/CAM aktif mi bilinmiyor, marka listesi teyitsiz (ve Z3'e göre hatalı), şehir bilinmiyor. Bu tabloda "Doğruluk 20/20" verilmesi, **"uydurmadım" ile "doğru"yu** eşitlemektir. Bunlar farklı iddialardır: birincisi süreç, ikincisi olgu.

Bu, `[[veri-olmadan-sayisal-puan-verme]]` ile **birebir aynı** hata deseni ve rubrik §0.1 (Tip A/B) tam bu durum için var: doğrulanmış kaynak yoksa **skor değil, bant** verilir.

**Önerilen düzeltme:**
- Doğruluk satırı: `20/20` → **"Süreç: temiz (uydurma yok) · Olgu: DOĞRULANMAMIŞ (10 açık kalem) — Tip B, skorlanmaz."**
- TOPLAM: `95/100 — A` → **"Bant: yayına hazır değil / avukat + teyit öncesi taslak."** Sayısal toplam, açık kalemler kapanınca verilir.
- Gerekçe pratik: Ayhan'ın masasına "95/100 A" olarak giden bir metin **bitmiş** okunur. Bu metin bitmemiş; kaynağı bitmemiş.

---

**Z5. [Atlanmış Soru / Red Team] Mevzuatın sitede açıkça istediği üç öğe sayfada yok — ve Hakkımızda tam da onların evi.**

**Kanıt:**
1. **Son güncelleme tarihi + editör/içerik sorumlusu iletişimi** — 2025 Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Yönetmeliği M.5 detay yükümlülüğü (`uyumlu-ticaret-plani` §0.B: *"son güncelleme tarihi + editör iletişimi sitede açık"*). Sayfada ikisi de yok.
2. **Yetki belgesi / sorumlu müdür görünürlüğü** — medikal paket §C güven sinyal seti + `uyumlu-ticaret-plani` §1/2: *"yetki belgesi + sorumlu müdür belgesi görünürlüğü (zaten merkezde asılı olmak zorunda — dijital yansıması güven mimarisiyle örtüşür)."* Sayfada yok.
3. **Künye** — E.2/4'te "belge teyidi bekliyor" diye bırakılmış. Doğru bekletme, ama YMYL/E-E-A-T'nin çekirdek sinyali ve mevzuatın istediği "editör" ile aynı kişiyi işaret ediyor; iki ayrı iş gibi ele alınmış.

**Neden aynı bulguda:** Üçü de aynı boşluğun parçaları — sayfa **kim olduğunu** söylemiyor. Metin Yazarı'nın E-listesi baştan sona *"bunu söyleyebilir miyiz?"* diye soruyor; hiçbir maddesi *"neyi kanıtlayabiliyoruz?"* diye sormuyor. Oysa tek bir belge talebi (ruhsat + sorumlu müdür belgesi + diploma + varsa üretici yetki yazıları) E'deki 10 maddenin **altısını birden** kapatır.

**Önerilen hamle:**
- Sayfa altına (disclaimer'ın altına) standart blok eklenir — lafız avukat gate'ine gider:
  > *Bu sayfa [GG.AA.YYYY] tarihinde güncellenmiştir. İçerik sorumlusu: [Ad Soyad, unvan] · [e-posta].*
- Ayhan → Özgür Bey'e **tek bir belge talebi** gider (E-listesinin yanına, ondan önce): merkez ruhsatı/yetki belgesi · sorumlu müdür belgesi · Özgür Bey'in diploması · varsa üniversite görevlendirme yazısı · varsa üretici yetki/bayilik yazıları. Bu talep, E'deki 1-2-3-5-8-9 maddelerinin çoğunu tek hamlede çözer.

---

**Z6. [Kalite Tabanı / Ton 50/50] "Merkezimizdeki Üniteler ve Teknoloji" bölümü ton kuralını bölüm düzeyinde ihlal ediyor — ve öz-denetim tam o bölümü atlamış.**

**Kanıt:** KKK §1 kilitli yapı kararı 2, testi net veriyor: *"bir sayfa/karede yalnız duygu ya da yalnız teknik veri varsa denge bozuktur."* Söz konusu bölüm iki paragraf, ~135 kelime ve **tek bir insan cümlesi içermiyor** — baştan sona envanter.

Metin Yazarı F.1/6'da 7/7 ✔ vermiş ve gerekçe olarak **"Süreç Nasıl İlerler"** ile **"Birlikte"** bölümlerini göstermiş. Yani öz-denetim, geçen iki bölümü örneklemiş, kalan tek başarısız bölümü **denetim dışında bırakmış.** Bu, bulgunun kendisinden daha önemli: seçici öz-denetim, sonraki turlarda da aynı kör noktayı üretir.

**Önerilen düzeltme lafzı** — bölümün sonuna tek cümle, dengeyi kurar ve zaten sayfanın tezi olan şeyi tekrar eder:
> *Hangi sistemin kullanılacağını cihazın özelliği değil, kişinin gününün nasıl geçtiği belirler.*

---

**Z7. [Verification] Mezuniyet beyanındaki kurum/program adı büyük olasılıkla yanlış — diploma teyidi olmadan yayınlanmamalı.**

**Kanıt (bağımsız doğrulama):** Trakya Üniversitesi'nde bu alandaki program, **Sağlık Hizmetleri Meslek Yüksekokulu** bünyesinde ve resmî adı **"Ortopedik Protez ve Ortez"** (ön lisans). Metindeki *"Trakya Üniversitesi **Protez ve Ortez Bölümü**"* / EN *"the **Prosthetics and Orthotics Department** of Trakya University"* bu adla örtüşmüyor; EN'deki "Department" ayrıca **fakülte/lisans** çağrışımı taşıyor. (Tip B — programın 1998'de hangi adla ve hangi yapıda olduğunu doğrulayamadım; kesin veri **diplomadadır**.)

**Neden önemli:** YMYL sayfasında eğitim beyanı, E-E-A-T'nin en yakından bakılan alanıdır ve 2025 yönetmeliği M.5'in "mesleki-akademik unvanlar" serbestliği **doğru beyan** koşuluna bağlıdır. Yanlış program/kurum adı, en ucuz ve en gereksiz güven kaybı türü.

**Önerilen hamle:** Program adı **diplomadan birebir alınır** (Z5'teki belge talebine dahil). Teyide kadar nötr form kullanılabilir: *"Özgür Irmak, 1998 yılında Trakya Üniversitesi'nin protez ve ortez programından mezun oldu."*

---

**Z8. [Devil's Advocate / Verification] Üniversite eğitim iddiası belirsiz bırakılarak "güvenli"leştirilmiş — oysa belirsizlik burada iki dünyanın da en kötüsünü veriyor.**

**Kanıt:** Metin: *"çeşitli üniversitelerin ortopedi, protez ve ortez bölümlerinde eğitim ve öğretim çalışmalarına devam ediyor."* Metin Yazarı bunu bilinçli olarak **üniversite adı ve unvan olmadan** yazmış, gerekçe: "unvan şişirme hukuki/itibari risk" (E-2).

Karşı argüman: adsız ve unvansız bir akademik faaliyet beyanı **doğrulanamaz**. Doğrulanamayan kimlik beyanı, YMYL değerlendirmesinde olumlu değil **olumsuz** sinyaldir; mevzuat tarafında da 18/6'nın "ekip yeterliliği hakkında yanlış bilgi" bandına, isimlendirilmiş bir beyandan **daha yakın** durur — çünkü ispat yükünü karşılayacak hiçbir tutamak bırakmıyor. Yani belirsizlik burada riski azaltmıyor, faydayı siliyor.

**Önerilen hamle — ikili seçenek, ortası yok:**
- **(a)** Görevlendirme/davet yazısı varsa üniversite(ler) **adıyla ve doğru sıfatla** yazılır (en güçlü E-E-A-T kazancı bu cümlededir).
- **(b)** Belge yoksa cümle **v1'den tamamen çıkarılır**, belge geldiğinde eklenir.
- Aynı mantık **CAD/CAM tezgâhı** cümlesi için de geçerli (E-9): Metin Yazarı "teyit gelmezse silinir" demiş — asimetri yanlış yönde kurulmuş. Olmayan ekipmanı ilan etmenin maliyeti, bir cümlenin yokluğundan **kat kat** yüksek. **Varsayılan: çıkar; teyit gelirse ekle.**

---

**Z9. [Tutarlılık / KKK §1.4] "Bir Ustanın Yolu" H2'si + ona verilen Lora ayrıcalığı, kilitli hibrit mimariyle çelişiyor.**

**Kanıt:** KKK §1 Kilitli yapı kararı 1: *"Marka mimarisi: **HİBRİT** — kurum markası önde; ustanın çeyrek asrı aşkın kişisel güven mirası **kanıt katmanı olarak içeride.** Kimlik ustanın portresi üzerine kurulmaz."*

Metinde ise: sayfanın **ilk H2'si** ustaya ayrılmış; §G'de bu bölüme sayfanın **tek editorial tipografi ayrıcalığı** (Lora) tahsis edilmiş. İkisi birlikte, ustayı "içeride kanıt katmanı" olmaktan çıkarıp sayfanın **görsel ve yapısal zirvesine** taşıyor. Metin Yazarı bunu F tablosunda −1 ile geçmiş ("hafifçe edebi") — bulgu doğru teşhis edilmiş ama ağırlığı düşük tutulmuş; mesele üslup değil, **kilitli mimari kararı**.

Ek tutarsızlık: TR H2 "Bir Ustanın Yolu: 1998'den Bugüne" iken EN H2 **"Mastery Since 1998, With Today's Technology"** — yani EN'de KKK'nın **ana kurumsal tagline'ı** bir gövde başlığına indirilmiş. Tagline hero/lockup öğesidir; gövde H2'sine inince (a) hero'da tekrar kullanıldığında aynı sayfada iki kez görünür, (b) TR/EN başlık yapısı paralelliğini kaybeder.

**Önerilen düzeltme:**
- TR H2 → **"1998'den Bugüne"** (Metin Yazarı'nın kendi alternatifi; doğru olan bu) veya **"Ustalığın Zemini"**.
- EN H2 → **"From 1998 to Today"** — tagline gövdeden çekilir, hero'ya bırakılır.
- Lora ayrıcalığı korunabilir (KKK §4 "Hakkında hikâye açılış bloğu" izni gerçek), ama **H1 altındaki giriş paragrafına** verilir; usta bölümüne değil. Böylece editorial an kuruma ait olur.

---

**Z10. [Kalite Tabanı] EN metinde imla sistemi karışık — uluslararası okurun ilk temasında düzeltilmemiş metin izlenimi verir.**

**Kanıt:** Aynı belgede İngiliz imlası (*practised*, *orthopaedics*) ile Amerikan imlası (*center*, tüm başlık ve descriptor'larda) yan yana. "Center" KKK §2'de **kilitli** descriptor olduğu için ("Prosthetics & Orthotics Center") sistem **Amerikan** imlasına sabitlenmelidir.

**Önerilen düzeltme:** *practised* → **practiced** · *orthopaedics* → **orthopedics**. (EN sürüm D1 gereği beklemede olsa da düzeltme şimdi işlenir, sonra unutulur.)

---

### ⚪ NOT

**N1. [Verification] Proteor / Nabtesco kararı doğrudur — onaylanır.** Çelişkili kaynakta (Proteor yalnız EN Parça 1'de, düzeltilmiş sürümde yerine Endolite) metne almama refleksi tam olarak beklenen davranış.

**N2. [Değer Uyumu / Branding] "residual limb" kararı doğrudur — Branding'e boş soru değil, **önerili karar** gitmelidir.** Gerekçe: TR'de "güdük" seçilme **ilkesi**, kullanıcının kendi kullandığı dile sadakattir (Özgür Bey "uygun" dedi). Aynı ilke EN'de uygulandığında sonuç "residual limb"tir — çünkü EN klinik ve hasta-topluluğu konvansiyonu o yöne kaymıştır. Yani iki karar **kelimede farklı, ilkede aynı**; tutarsızlık yok. Öneri: "residual limb" KKK §2 kelime listesine **EN kilidi** olarak işlenir. SEO tarafında "stump" hacmi gerekiyorsa yeri Hakkımızda değil, Çözümler/SSS'deki terim açıklamasıdır.

**N3. [Kalite Tabanı] TR'de teknik kategori karışması var; düzeltmesi zaten EN'de yazılı.** TR: *"vakumlu ve pin sistemli, hidrolik, pnömatik ve mikroişlemcili diz eklemli sistemler"* — süspansiyon sistemleri (vakum/pin) ile diz tipleri (hidrolik/pnömatik/mikroişlemcili) tek seriye dizilmiş. EN aynı cümleyi doğru ayırmış: *"vacuum and pin-lock **suspension systems**, hydraulic and pneumatic **knee joints**, and microprocessor-controlled knees"*. EN'deki ayrım TR'ye geri taşınır.

**N4. [Onur] "bireyin doğru pozisyonlanması" — özne/nesne kayması.** Cümle: *"Uzuv amputasyonunun ardından bireyin doğru pozisyonlanması, güdük bakımı…"* Burada birey, konumlandırılan **nesne**. KKK §6/3'ün görsel testi ("figür özne mi nesne mi?") dile de uygulanır. Öneri: *"Amputasyondan sonraki dönemde doğru pozisyonlama, güdük bakımı, bandajlama ve kompresyon uygulamaları ilk halkadır."* (Ayrıca "uzuv amputasyonu" ikilemesi de düşer.) Gövdedeki tek onur pürüzü budur; sayfanın geri kalanı bu mercekte temiz.

**N5. [Değer Uyumu] İlan edilen dört çekirdek değer (GÜVEN · CESARET · ADALET · EMPATİ) sayfada hiç geçmiyor.** KKK §1 bunları "dışa dönük her yerde bu dört" diye kilitlemiş. Sayfa hiçbir yerde değer beyan etmediği için teknik olarak **ihlal değil** — ama Hibrit mimaride kurumun kendini anlattığı tek sayfa burasıdır ve markanın ilan edilmiş değerleri burada yoksa başka nerede olacağı belirsiz kalır. Karar Ayhan/Branding'in: değerler Hakkımızda'ya bir blok olarak girecek mi, yoksa brand book'ta mı kalacak? Cevap "girecek"se bu, v2'nin en doğal eksik bölümü.

**N6. [Verification] Beyan edilen kelime sayıları doğru.** Bağımsız sayım: A 466 · B 114 · C 546 · C.1 109 (beyan: 461/111/538/104). Fark yalnız kapanış tagline'ının sayıma dahil edilmesinden; sapma yok, hedef bandı korunuyor. Bu kalem **temiz**.

---

## SORULMAMIŞ SORULAR

*(Bulgu değil — bu çıktıyı üreten sürecin hiç sormadığı, ama cevabı gelmezse aynı işi ikinci kez yaptıracak sorular.)*

**1. Bu sayfa hangi kaba girecek — tek site mi, iki katlı mimari mi?** D1'in kökü. Cevap gelmeden EN'in yalnız *zamanı* değil, **rejimi ve içeriği** de belirsiz. Bu soru 4 Tem'de soruldu (uyumlu-ticaret §0.B), bir ay geçti, kimse cevaplamadı, ama üzerine üretim yapılmaya devam edildi.

**2. Ham 5 parçanın kaynağı kim?** Özgür Bey'in kendi kalemi mi, önceki ajansın metni mi, üretici pazarlama metninin çevirisi mi? Ürün metinlerinde bu sorunun cevabı **"büyük çoğunluğu üreticinin pazarlama metninin çevirisi"** çıkmıştı. Aynı köken buradaysa: (a) "ham kaynaktan geliyor" gerekçesi tüm bulgu savunmalarında düşer (Z2), (b) üçüncü taraf telif sorusu doğar. Bu soru hiç sorulmadı.

**3. Neyi KANITLAYABİLİYORUZ?** E-listesinin 10 maddesinin tamamı *"bunu söyleyebilir miyiz?"* biçiminde. Hiçbiri *"elimizde hangi belge var?"* diye sormuyor. Tek bir belge talebi 6 maddeyi birden kapatır (Z5). Üç turdur eksiltiyoruz; bir kez de **toplamayı** deneyelim.

**4. 2025 yönetmeliğinin istediği "editör / içerik sorumlusu" KİM?** Bu bir metin kararı değil, **bir kişi ataması**. Sitede adı ve iletişimi açık duracak. Kimse bu kişiyi belirlemedi.

**5. Önceki cezanın madde dayanağı hâlâ alınmadı mı?** `uyumlu-ticaret-plani` §4/3 bunu keşif ödevi olarak koymuştu ("hangi fiil, hangi kanal?"). Hangi davranışın cezalandırıldığını bilmeden Hakkımızda yayınlamak, kör yayındır — üstelik metnin bugün hangi cümlesinin riskli olduğunu **tam olarak** o dosya söyler.

---

## ÇELİŞKİ (Ayhan'a iki görüş birden gider)

**Devil's Advocate der ki:** Bu proje kapı üstüne kapı biriktiriyor. Site Draft, ürün metinleri Draft, blog künyesiz, IG serisi beklemede, şimdi de EN mimariye bağlandı. Müşteri bir aydır **hiçbir şeyin yayınlandığını görmedi**. Kendi kurumunu tanıtan, hiçbir iddia içermeyen, hiçbir cihaz övmeyen bir EN sayfası, M.4-5'in serbest alanındadır (kuruluş adı, hizmet alanları, koruyucu bilgi) — sponsorlu değil, talep yaratmıyor, hasta hikâyesi yok. Bunu da bekletmek, uyumu değil **atalet**i korumak olur; ve bir noktada müşteri "bu ajans bir şey yayınlamıyor" der.

**Red Team der ki:** EN sayfası tam olarak M.8'in düzenlediği faaliyetin ilk halkasıdır — bunu Metin Yazarı'nın kendi lokalizasyon notu yazıyor. Mimari kararı düşmeden yayınlanan bir EN sayfası, iki katlı yapıya geçilince **yanlış domainde kalmış bir uluslararası vitrin** olur; taşımak, 301'lemek, yeniden yazmak gerekir. Ve bu müşterinin dosyasında **zaten idari ceza geçmişi var** — riski test edecek son müşteri o.

**Sentezim (orkestratör):** İkisi de haklı ve çatışma göründüğü kadar keskin değil, çünkü **TR ile EN'i ayırmak ikisini de karşılıyor.** TR sayfası bugün avukat gate'ine girer — o, projenin görünür ilerlemesidir ve Devil's Advocate'in itirazını karşılar. EN, mimari kararına bağlı taslak olarak bekler — Red Team'in itirazını karşılar. Gerçek darboğaz EN metni değil, **bir aydır cevaplanmamış mimari sorusu**; asıl hamle avukat görüşmesini takvime almaktır, EN'i zorlamak değil.

---

## KARAR ÖNERİSİ

**☑ DÜZELT — sonra Ayhan → sonra avukat gate.**

**Metin Yazarı'na geri döner (v0.2 için, avukat öncesi):**
D2 (kurumsal 1998 sızıntısı — §B + 2 title) · D3 (disclaimer yan yana koyma) · Z1 + Z2 (protetist/deneyimli → teknik kadro) · Z3 (marka listesini sayfadan çıkar) · Z4 (skor → bant) · Z6 (denge cümlesi) · Z7 (program adı nötrlenir) · Z8 (üniversite + CAD/CAM: belge yoksa çıkar) · Z9 (H2'ler) · Z10 (EN imla) · N3 · N4.

**Fox'a döner (belge/sistem işi):**
D1 (§C statüsü `⏸️ MİMARİ KARARA BAĞLI TASLAK`) · `ozgur-irmak-web-semasi.md`'ye 0.B revizyon bayrağının işlenmesi · KKK §1'e "1998 = kişi çapası" satırının eklenmesi · Z5 belge talebi listesinin Ayhan'a hazırlanması · "Çözüm Ortakları" sayfa adı notunun İçerik/Growth'a düşülmesi.

**Statü:** v0.2 bu düzeltmelerle **TR tarafında avukat gate'ine hazır** olur. EN mimari kararını bekler. Hiçbir sürüm yayına gitmez.

---

## AYHAN'A GİDEN KARAR MADDELERİ

| # | Karar | Kim çözer | Aciliyet |
|---|---|---|---|
| **1** | **Belge talebi Özgür Bey'e gider mi?** (ruhsat/yetki belgesi · sorumlu müdür belgesi · diploma · üniversite görevlendirme yazısı · üretici yetki yazıları) — E-listesinin 6 maddesini tek hamlede kapatır. | Ayhan → Özgür Bey | **Yüksek** — diğer her şey buna bağlı |
| **2** | **Web mimarisi: tek site mi, iki katlı mı?** (uyumlu-ticaret §0.B, 4 Tem'den beri açık) — EN'in evi, rejimi ve içeriği buna bağlı. | Ayhan + ⚖️ **avukat** | **Yüksek** — EN üretimi bunu bekliyor |
| **3** | **"1998" çapası: kurumsal özneyle kullanım yasağı KKK'ya yazılsın mı?** Ve belge teyidine kadar gövde dilinde "çeyrek asrı aşkın" tercih edilsin mi? | Ayhan (Branding uygular) | Orta |
| **4** | **Değerler (GÜVEN·CESARET·ADALET·EMPATİ) Hakkımızda'ya blok olarak girsin mi?** (N5) | Ayhan + Branding | Orta |
| **5** | **Sitenin "içerik sorumlusu / editörü" kim?** — mevzuat gereği adı ve iletişimi sitede açık duracak. Kişi ataması. | Ayhan + Özgür Bey | Orta |
| **6** | **Künye kararı:** blog künyesiz gitti; Hakkımızda kurumsal sayfa — künye açılsın mı? (belge teyidine bağlı) | Ayhan | Orta |

### ⚖️ AVUKAT KAPISINA GİDENLER (işaretli)

1. **Disclaimer:** iki onaylı lafzın aynı sayfada **yan yana** durması sakıncalı mı? *(Birleştirilmiş yeni lafız değil — D3'teki düzeltmeden sonra soru bu hâle gelir; çok daha ucuz bir onay.)*
2. **"protetist" / "teknik kadro" / "ortez-protez teknikeri":** merkezin web sitesinde hangi personel adlandırması mevzuata uygun? *(Z1 — "uzman → teknik sorumlu" düzeltmesinin devamı.)*
3. **Marka adları** (Ottobock, Össur, Endolite, ALPS, Freedom, bebionic, Touch Bionics) sitede hangi çerçevede geçebilir — ad ile logo ayrı rejim mi? *(Mevcut avukat sorusu #1 + #8; Z3'ten sonra soru "Teknoloji sayfası" bağlamına taşınır.)*
4. **EN/AR/RU yayını + iki katlı mimari:** M.8 "ayrı site" koşulu bizim için nasıl uygulanır; sponsorsuz EN kurumsal sayfa ana domainde durabilir mi? *(D1 + avukat #4/#5/S14.)*
5. **Üniversite eğitim beyanı:** isimlendirilmiş akademik faaliyet beyanı hangi belgeyle güvenli hâle gelir? *(Z8.)*
6. **Mevzuatın istediği sayfa öğeleri:** son güncelleme tarihi + editör iletişimi lafzı; yetki belgesi/sorumlu müdür görünürlüğünün dijital biçimi. *(Z5.)*

---

## EK — METİN YAZARI'NIN 5 SORUSUNA DOĞRUDAN CEVAP (F.3)

1. **CAD/CAM cümlesi tutulmalı mı?** → **Hayır, çıkarılmalı.** Asimetri yanlış kurulmuş: olmayan ekipmanı ilan etmenin maliyeti, bir cümlenin yokluğundan çok yüksek. Varsayılan "teyide kadar çıkar", "teyit gelmezse sil" değil. *(Z8)*
2. **"1998"in kişiye bağlanması KKK ile çelişiyor mu?** → **Hayır — KKK tagline'ının öznesi "ustalık"tır, yani kişidir; metin doğru yapmış.** Çelişen şey §B ve iki title. KKK düzeltilmez, **açıklık kazandırılır** (tek satır ekleme). *(D2)*
3. **Disclaimer bayrağı doğru mu?** → **Doğru ama eksik.** Bu bir "yeni lafız" değil, onaylı koruyucu cümlenin düşürülmesi. Birleştirme yerine yan yana koyma. *(D3)*
4. **"residual limb" tutarsızlık mı?** → **Değil.** İki karar kelimede farklı, ilkede aynı (kullanıcının kendi dili). Branding'e **önerili** gider, boş soru olarak değil; KKK'ya EN kilidi işlenir. *(N2)*
5. **Marka listesi bayilik ima ediyor mu?** → **Lafız ima etmiyor, formülasyonun doğru.** Sorun lafızda değil **yerde**: liste Hakkımızda'ya değil Teknoloji sayfasına ait, ve üç doğrulama hatası taşıyor. *(Z3)*

**Sorulmayan altıncı soru — sayfa işini görüyor mu?** Kısmen. Gövdenin ~%40'ı süreç + envanter, yani Çözümler ve Süreç sayfalarının işi; gerçek Hakkımızda maddesi (merkez neden var, nerede, kimler, hangi belge, hangi değerler) **kaynakta olmadığı için** yazılamamış. Yani kelime bütçesi, sayfanın ihtiyacı olan malzemeye değil, **eldeki malzemeye** harcanmış. Bu metnin kusuru değil, kaynağın eksikliği — ve çözümü daha iyi yazmak değil, **Karar Maddesi 1'i çalıştırmak.**

---

*Denetmen v2 · Faz 3 Orkestratör · 3 Ağustos 2026 · Sonraki halka: Metin Yazarı v0.2 → Fox konsensüs → Ayhan → ⚖️ avukat gate → yayın.*
