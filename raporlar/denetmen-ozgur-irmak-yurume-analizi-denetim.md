# DENETMEN RAPORU (Orkestratör Sentezi) — Özgür Irmak / Yürüme Analizi sayfası v0.1

*13 Ağustos 2026 · Denetlenen: Metin Yazarı v1.2 — `raporlar/ozgur-irmak-yurume-analizi-v01.md`*
*Çağrılan alt roller: **Verification** (rakam/olgu) · **Red Team** (mevzuat + dış okuma) · orkestratör mercekleri (Tutarlılık / Değer Uyumu / Kalite Tabanı / Atlanmış Soru / İnsan Sesi)*
*Kaynaklar: `ozgur-irmak-yurume-analizi-sartname-kaynak.md` · `ozgur-irmak-uyumlu-ticaret-plani.md` §0-§3, §6 · `marka-bulutu-os-medikal-protez-bagi.md` A.2-A.3, C · ses referansı `ozgur-irmak-hakkimizda-v07.md`*

**KARAR: GERİ** — metin düzeltmeye. Sonrasında koşullu onay + avukat kapısı.

---

## DUR — yayın engelleyici (7)

### D1 · Bayrak çok dar çizilmiş: sayfanın tamamı teyitsiz şartname verisi üzerine kurulu
`⟦MARKA SLOTU⟧` yalnız **marka adını ve sensör sayısını** koruma altına alıyor. Oysa kaynak belgenin doğrulama bayrağı daha geniş: *"merkezde birebir bu cihazların bulunduğu teyitli değil."* Sayfa ise merkezin bugünkü pratiğini anlatan şimdiki zamanla yazılmış:

> "Bandın yüzeyi basınç sensörleriyle kaplı, altında da bir kuvvet platformu var."
> "Atölyede 5 farklı yoğunlukta malzeme var."
> "Kullandığımız takozlar Shore A 21 ile 60 arasında…"
> "Tarama en fazla 10 saniye sürüyor." · "4 adımlık akış kumandayla yürütülüyor."

**Kanıt:** Hakkımızda v0.7 yalnız *genel yeteneği* doğruluyor ("yürüyüş sensörlü koşu bandında ölçülüyor, tabanlıklar farklı yoğunluklarda CNC ile üretiliyor"). Şartnamedeki **spesifikasyonların** merkeze ait olduğu hiçbir yerde teyitli değil — belge bir tedarikçi ihale metni (içinde Kazakistan Sağlık Bakanlığı kurulumu geçiyor). Cihaz farklıysa lazer aşil hattı, 4 adımlık akış, Shore A aralığı, 10 sn tarama, 5 dansite, 37-50 kalıp aralığı — hepsi yanlış olur.
**Risk:** Yanlışlık değil, **yanıltıcılık** kategorisi: 18/6 "olmayan özelliği var gösterme". Bilgilendirme rejiminin (15/2) koruması, bilginin doğru olması şartına bağlı.
**Önerilen hamle:** Bayrağı sayfa başına taşı: *"Bu sayfadaki tüm süreç ve teknik detaylar merkezin kendi cihaz envanteriyle satır satır teyit edilmeden yayına girmez."* Metin Yazarı'na değil, önce Özgür Bey'e gider (Soru 1 zaten yazılmış — kapsamı genişletilmeli: marka adı değil, **her spesifikasyon**).

### D2 · "Kimler ölçülebilir" bölümü — üç adımlık talep yaratma dizisi
Cümleler tek tek masum; **dizi** olarak okunduğunda funnel:

> ① "Yürüyüş dışarıdan bakınca çoğu zaman düzgün görünür." → ② "Yürüyüşünü değerlendirmek isteyen herkes ölçülebilir." → ③ "Ölçüm için merkezimize gelmeniz yeterli."

*Senin yürüyüşün de sorunlu olabilir → herkes gelebilir → tek yapman gereken gelmek.*
**Kanıt:** Sağlık Hizmetlerinde Tanıtım ve Bilgilendirme Yönetmeliği M.5 — **talep yaratma/yönlendirme yasak.** "…gelmeniz yeterli" bir sürtünme kaldırma cümlesi (dönüşüm copy'si kalıbı), bilgilendirme değil. "Herkes ölçülebilir" ayrıca **kaynakta yok** — kapsam iddiası, uydurma.
**Karşılaştır (onaylı ses):** v0.7 aynı işi şöyle yapıyor: *"Sürecin sizin için nasıl ilerleyeceğini merkezimizde birlikte konuşabiliriz."* — koşullu, davetsiz.
**Önerilen hamle:** ②+③ silinsin. Yerine: *"Ölçümün kimin için uygun olduğu, kişiye özel değerlendirmede belirlenir. Süreci merkezimizde birlikte konuşabiliriz."* ①'in kaderi F1'de.

### D3 · Gövde, SSS'nin "cevap bekliyor" dediği soruyu zaten cevaplıyor
> SSS: **"Ölçüm için doktor raporu gerekiyor mu?"** → `⟦CEVAP BEKLİYOR — … Cevap gelmeden bu soru yayına girmez.⟧`
> Gövde: **"Ölçüm için merkezimize gelmeniz yeterli."**

Gövde "hayır, gerekmiyor" diyor; SSS "bilmiyoruz" diyor. İç çelişki **ve** yazarın kendi teyitsiz saydığı operasyonel bilgiyi gövdede olgu gibi yayınlıyor.
**Önerilen hamle:** D2 düzeltmesi bunu da kapatır. Kapatmazsa gövde cümlesi çıkar.

### D4 · Açılış cümlesinde iki kaynaksız olgu
> "**Ayakkabınızı çıkarıyorsunuz** ve sensörlü bir bantta **birkaç dakika** yürüyorsunuz."

**Kanıt:** Kaynak §2'de ne ayakkabı ne süre geçiyor — yalnız "kişi sensörlü yürüme bandında yürütülür". İkisi de merkezin protokolüne dair iddia. Yürüme analizi çıplak ayakla da ayakkabıyla da yapılabilir; protokol yanlışsa hasta yanlış hazırlıkla gelir.
**Ağırlaştırıcı:** "birkaç dakika" SSS'de süre cevabı olarak **tekrarlanıyor** ("Bantta yürüme kısmı birkaç dakika") — aynı SSS'nin toplam süreyi "kaynakta yok" diye bayrakladığı yerde. Bilinmeyen bir sürecin bir parçasına süre biçilmiş.
**Önerilen hamle:** İkisi de çıkar ya da Özgür Bey teyidiyle girer. Açılış sahnesi olgusuz da kurulabilir: *"Sensörlü bir bantta yürüyorsunuz. O sırada ayağınızın altındaki basınç kaydediliyor…"*

### D5 · Künye + tarih + e-posta boş — bu bir yasal yükümlülük, eksik bilgi değil
`⟦E-E-A-T KÜNYESİ⟧` · `[TARİH]` · `[E-POSTA GİRİLECEK]`
**Kanıt:** M.5 detay yükümlülüğü: **son güncelleme tarihi + editör iletişimi sitede açık** olacak. YMYL/E-E-A-T (medikal paket C) ayrıca gerçek uzman künyesi istiyor. Yazarın bayrağı doğru — statüsü teyit edildi: **bloklayıcı.**
**Ek bulgu (v0.7'ye taşar):** v0.7'nin sayfa altında içerik sorumlusu **"Ayhan Erden"** yazıyor. Sağlık sayfasının içerik sorumlusu ajans sahibi olamaz — merkezin teknik sorumlusu olmalı. Yeni taslak doğru yaklaşımı alıyor; **v0.7 footer'ı da düzeltilmeli.**

### D6 · His kaybı uyarısının klinisyen lafzı — güvenlik kapısı
`⟦KLİNİSYEN LAFZI BEKLİYOR⟧` (nöropati/diyabetik ayak). Yazarın kararı doğru: mevcut cümle ("değerlendirmeyi ayrıca dikkatli yürütüyoruz") tek başına güvenli, ama **basıncı hissetmeyen okuyucuya kontrol talimatı vermiyor.** YMYL sayfasında yüksek riskli alt grup uyarısız kalmaz. Ucuz düzeltme: hekime tek mesaj.
**Statü:** bloklayıcı, doğru bayraklanmış.

### D7 · Bayrak envanteri üç farklı sayı veriyor
Fox'un denetim talebi **6** açık bayrak diyor · metnin kendi skor tablosu **"4 doğrulanmamış alan"** diyor · dosyada gerçekte **8** yayınlanabilir bayrak var (satır 21, 61, 67, 93, 104, 111, 114, 123).
**Neden DUR:** Bu sayfada bir numaralı operasyonel risk, çözülmemiş bir bayrağın yayına sızması. Sayının kendisi tutmuyorsa kontrol mekanizması yok demektir.
**Önerilen hamle:** Metnin sonuna tek bir bayrak tablosu (satır · konu · bloklayıcı mı · sahibi · statü). Yayın öncesi `grep -c "⟦⚠️"` sıfır dönmeden Wix'e geçilmez.

---

## DÜZELT (7)

### F1 · İki cümlelik "sende de olabilir" ikilisi
> "Ölçüm daha ayrıntılı konuşur." + "Bunlar çıplak gözle görülen şeyler değil."

Tek tek savunulabilir (ölçüm gerçekten gözün görmediğini gösterir). Birlikte, sayfanın iki ayrı yerinde, aynı işi yapıyorlar: **gözle anlaşılmayan bir eksiklik hissi.** 18/6'nın "kullanmazsan refahın azalır" kalemine yaklaşan retorik. Aforizma formu ("…konuşur") olguyu ikna hamlesine çeviriyor.
**Hamle:** Aforizmayı nesnelleştir — *"Ölçüm, gözün göremediğini sayıya çeviriyor."* İkincisi kalabilir. (Not: bu cümle taramada metnin tek aforizması; düşürmek İnsan Sesi ölçüsünü bozmaz, kural "metin başına 1" — 0 da geçerli.)

### F2 · "Tabanlığım ne zaman hazır olur?" cevabı yanlış rakamla açılıyor
> "Frezeleme ayak başına 6-10 dakika sürüyor. Ölçümden teslime kadar geçen toplam süre randevu yoğunluğuna göre değişiyor."

Makine çevrim süresi, teslim süresi değil. Soruya cevap makine süresiyle başlayınca okuyucuda **aynı gün** beklentisi doğar; ikinci cümle onu geri alamaz.
**Hamle:** Sırayı ters çevir — önce "toplam süre randevu yoğunluğuna göre değişiyor", frezeleme süresi ikinci cümlede bağlamıyla ("makinede geçen süre kısa; toplam süreyi belirleyen randevu akışı").

### F3 · 6-10 dk birleştirmesi savunulabilir ama hiçbir kaynakta geçmiyor
Kaynak §6: ayak başına **~6-9 dk**; şartnamenin B bölümünde **7-10 dk**. Metin **6-10** yazıyor = iki aralığın birleşimi. Abartma yok (hız iddiası doğurmuyor), ama iki kaynağın da desteklediği bölge **7-9**.
**Hamle:** ya "7-9 dakika" (kesişim, iki kaynak da destekliyor) ya rakamsız ("ayak başına on dakikayı bulmuyor"). Hangisi seçilirse Yazarın Notu'na kaynak çelişkisi şerhi düşülsün.

### F4 · Küçük sayılar rakamla yazılmış — onaylı ses yazıyla yazıyor, üstelik ölçüyü şişiriyor
> "2 bölümde ilerliyor" · "3 boyutlu" · "4 adımlık akış" · "5 farklı yoğunlukta"

v0.7 aynı durumda **yazıyla** yazıyor: *"yirmi sekiz yıldır"*. Rakam yoğunluğu ölçüldü: v0.7 = 337 kelimede 3 rakam · bu metin = 543 kelimede 19 rakam (~4 kat).
**Ölçülen etki:** Bu dört ifadeyi yazıya çevirdiğimde somut çapa **5,0 → 3,8**'e düşüyor (SERT eşiği 3,0). Yani raporlanan 5,0'ın ~1,2 puanı yeni olgudan değil, **yazım biçiminden** geliyor.
**Hamle:** Süreç sayfası 10 saniye / 37-50 / 3-6 ay gibi ölçüleri rakamla yazsın (doğru), ama sayım sayıları yazıya dönsün. UYARI 1 gerekçesi buna göre güncellensin (bkz. N1).

### F5 · Brief "teknik tarafı geride bırak" diyordu; sayfadaki en şartname-benzeri satır duruyor
> "…ark yüksekliği, topuk kavrayışı, iç ya da dış kama, metatarsal ped, kalınlık, açı."

Altı terimden dördü hastanın bilmediği jargon. Yazarın kendi ilkesiyle (Yazarın Notu #1) çelişiyor.
**Hamle:** İki örneğe indir + karşılığını ver: *"Ark yüksekliği, topuğun nasıl kavranacağı, kalınlık — hepsi ekrandaki model üzerinde ayarlanıyor."*

### F6 · Sayfa teslimde bitiyor; markanın çekirdek vaadi teslimden sonra başlıyor
v0.7: *"Takip bu yüzden teslimattan sonra yapılan bir nezaket değil, işin kendisi."* Bu sayfada tabanlık frezeleniyor, kaplanıyor, bitiyor. **Deneme, ayak uydurma, ilk hafta, ayar kontrolü yok.** Marka sesinin en güçlü cümlesi bu sayfada karşılıksız kalıyor — hem tutarlılık hem içerik boşluğu.
**Hamle:** "Ne kadar dayanır" bölümünden önce kısa bir paragraf: tabanlığın verildikten sonraki ilk uyum dönemi ve kontrol. **Olgu Özgür Bey'den gelir** — uydurulmaz (soru listesine ekle).

### F7 · Kendi skorundaki Doğruluk 17/20 şu anda savunulamaz
"Her olgu kaynak belgeden. Uydurma rakam yok." — D1 (teyitsiz spesifikasyon zemini), D2 ("herkes ölçülebilir") ve D4 (ayakkabı + birkaç dakika) bunu yanlışlıyor. Skor Tip B bir yargı, ölçüm değil; cihaz teyidi gelene kadar bu kalem düşük yazılmalı.

---

## NOT (9)

**N1 · UYARI 1 gerekçesi kabul — ama eksik.** "Somut çapa açığı üslup sorunu değil brif açığı" tespiti **doğru** ve korpus §5 kök neden kuralının doğru uygulaması. Eksik olan şerh: 2,9 → 5,0 yükselişinin bir bölümü (a) **teyitsiz şartname rakamlarıyla** (Shore A, 37-50, 5 dansite — D1) ve (b) **rakam yazım biçimiyle** (F4) sağlandı. Cihaz teyidi olumsuz gelirse hem olgular hem ölçü çöker. Gerekçe bu şerhle yeniden yazılsın. → **Ölçüyü gevşetmek için gerekçe üretilmemiş** (v06 Goodhart'ının tersi değil), ama gerekçe elindekinin sağlamlığını olduğundan güvenli gösteriyor.

**N2 · UYARI 2 gerekçesi kabul, kovalanmasın.** Paragraf CV 0,377 — süreç sayfası türünün doğal sonucu; yapay bölme v06 hatasının tekrarı olurdu. Doğru karar. Alıntı ve eksik olgular gelince ölçü kendiliğinden yükselir.

**N3 · Araç kalibrasyon bayrağı (İnsan Sesi Korpusu'na).** Aynı araçla ölçtüm: **Ayhan onaylı v0.7 gövdesi somut çapa 2,8 = SERT** veriyor (+ cümle CV 0,448 UYARI). Yani eşik, onaylı sesin hakemi değil — düz anlatı/kurumsal prosa türünde eşik yanlış kalibre. Denetimin kendi merceği yanlış işaret veriyorsa mercek de güncellenir (yerleşik kural). `fox-metin-insan-sesi-korpusu.md`'ye tür bazlı eşik notu düşülmeli. **Bu, mevcut denetimin sonucunu değiştirmiyor** — bu metinde tarama zaten SERT vermedi.

**N4 · Bloklamayan 4 bayrak serbest bırakılabilir** (yayın 8 bayrağı birden beklemesin):
- `ARAMA HACMİ TEYİDİ` — kelime seti yayın sonrası ayarlanır, sayfayı bekletmez.
- `TOPLAM RANDEVU SÜRESİ` — SSS cevabı zaten dürüst ("kişiye göre değişiyor"); rakamsız yayınlanabilir.
- `TESLİM SÜRESİ` — aynı; F2 düzeltmesiyle birlikte sorun kalmaz.
- `ALINTI SLOTU` — sayfa onsuz ayakta; ayrıca N5'teki riski taşıyor.
**Bloklayan 4:** cihaz teyidi (genişletilmiş D1) · künye/tarih/e-posta (D5) · his kaybı lafzı (D6) · doktor raporu (D3 ile birlikte çözülür).

**N5 · Alıntı slotunun kendi riski var.** Yurt içi sitede **hasta görüşü/memnuniyet ifadesi M.5'te yasak.** Hasta *sorusu* memnuniyet ifadesi değil — ama sınıra yakın ve alıntı formatı testimonial gibi okunabilir. Avukat sorusuna eklensin: *"Hasta memnuniyeti içermeyen, yalnız soru aktaran alıntı yurt içi sitede kullanılabilir mi?"*

**N6 · Atlanmış sorular** (hastanın soracağı, sayfada olmayan):
1. **"Bu bana ne sağlar?"** — Kaynak §1'deki amaç cümlesi (basıncı azaltmak, eklem stabilitesi, deformasyonun ilerlemesini yavaşlatmak) bilinçli çıkarılmış. Yazarın gerekçesi savunulabilir ama sonuç şu: **sayfa nasıl yapıldığını anlatıyor, neden yapıldığını hiç söylemiyor.** Cihazın amacını söylemek, "kesin başarı beklentisi" (18/6) değildir. Bu **sessiz bir karar olarak kalmasın** — somut cümleyle avukata gitsin: *"Kişiye özel tabanlığın amacı ayağa binen basıncı dağıtmak ve eklem stabilitesini desteklemektir; sonuç kişiye göre değişir."*
2. **"Ayakkabımı getirmeli miyim?"** — Metin tabanlığın "kullanacağınız ayakkabıya göre" ölçülendiğini söylüyor ama getirilmesi gerekip gerekmediğini söylemiyor. Ucuz, gerçek, çapa değeri yüksek.
3. **"Acıyor mu / rahatsız mı?"** — pimli platform ve bant, ilk kez duyan için endişe kaynağı.
4. **"Çocuk ölçülebilir mi / 37 numaradan küçük ayak?"** — metin 37-50 diyor; v0.7 çocuklar için üretim yapıldığını söylüyor. Okuyucuda çelişki.
5. **"SGK karşılıyor mu?"** — en çok sorulan soru; ücret/kampanya bilgisi M.5'te yasak, ama SGK kapsamı ayrı bir kalem. Sessizlik **bilinçli** olmalı, kazara değil → avukat sorusu.

**N7 · KVKK.** "Ölçüm dosyası merkezde kalıyor." — sağlık verisi = özel nitelikli kişisel veri. Cümle doğru ve şeffaf; sayfanın aydınlatma metniyle/KVKK politikasıyla eşleşmesi kontrol edilsin (`Ozgur-Protez-KVKK-Politikasi-v01.docx`).

**N8 · "operasyon öncesiyle sonrası" ifadesi.** M.5'in yasakladığı "öncesi-sonrası", reklam amaçlı **hasta görseli**. Buradaki kullanım metinsel ve ölçüm karşılaştırması — düşük risk, ama düzenlemenin yasaklı terimine değiyor. Avukat listesine bir satır; metin değişmesin.

**N9 · v0.7'de yazım hatası** (kapsam dışı, kayda geçsin): sayfa altı *"Kendi durumunuz için **merkezinize** ya da hekiminize danışın"* → **merkezimize**. Yeni taslakta doğru yazılmış.

---

## SORULMAMIŞ SORULAR

1. **Bu sayfa hangi rejimde yayınlanıyor?** Uyumlu Ticaret Planı §0.B'nin iki katlı mimari bayrağı (TR bilgilendirme / uluslararası M.8) hâlâ açık ve avukat teyidi bekliyor. Sayfa TR tarafına yazıldı — doğru varsayım, ama **yazılı karar yok.**
2. **Avukat kapısı ne zaman?** Plan §1/2 diyor ki yeşil kuşak web dili avukata "onaylar mısınız?" diye gider. Bu sayfa yeşil kuşağın **ilk gerçek örneği**. Onaylanan bir şablon çıkarsa sonraki Çözümler sayfaları tek tek denetlenmez. Bu sayfayı örnek dosya yapmak, ölçek kararıdır — Ayhan'a ait.
3. **Diğer Çözümler sayfaları aynı kaynak sorunuyla mı gelecek?** D1 bu sayfaya özel değil: elimizde tedarikçi şartnamesi var, merkez envanteri yok. Envanter teyidi **bir kere** alınırsa tüm Çözümler zinciri açılır; alınmazsa her sayfa aynı yerde takılır.

---

## KARAR ÖNERİSİ

☑ **GERİ — Metin Yazarı'na.** D2, D3, D4, F1-F6 metin düzeltmesi (yeniden yazım değil, cerrahi). D7 bayrak tablosu eklenir.
Sonra: **KOŞULLU ONAY** → Özgür Bey teyit seti (D1 genişletilmiş cihaz envanteri + D6 klinisyen lafzı + F6 takip olgusu + N6/2 ayakkabı) → **avukat kapısı** (N5, N6/1, N6/5, N8) → Ayhan onayı → yayın.
Serbest bırakılan 4 bayrak (N4) yayını bekletmez.

---
*Denetmen v2 · Faz 3 Orkestratör · Bulgular: 7 DUR · 7 DÜZELT · 9 NOT*
