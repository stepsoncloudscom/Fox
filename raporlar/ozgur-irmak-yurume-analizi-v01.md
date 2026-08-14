# Özgür Irmak — Yürüme Analizi ve Kişiye Özel Tabanlık (Çözümler alt sayfası) v0.1

*Metin Yazarı v1.2 · 13 Ağustos 2026 · Kaynak: `raporlar/ozgur-irmak-yurume-analizi-sartname-kaynak.md` · Ses referansı: Hakkımızda v0.7 · Rejim: yeşil kuşak bilgilendirme (TİTCK 15/2)*

---

## [H1]

Yürüme Analizi ve Kişiye Özel Tabanlık

## [GİRİŞ]

Ayakkabınızı çıkarıyorsunuz ve sensörlü bir bantta birkaç dakika yürüyorsunuz. O birkaç dakika boyunca ayağınızın altındaki basınç kaydediliyor: topuk yere hangi noktadan değiyor, ağırlık ön ayağa nasıl geçiyor, sağ adımınızla sol adımınız birbirini tutuyor mu.

Yürüyüş dışarıdan bakınca çoğu zaman düzgün görünür. Ölçüm daha ayrıntılı konuşur.

Merkeze geldiğinizde ölçüm 2 bölümde ilerliyor: önce bantta yürürken, sonra ayağınızın kalıbı çıkarılırken.

## [H2] Bantta ne ölçülüyor

Bandın yüzeyi basınç sensörleriyle kaplı, altında da bir kuvvet platformu var. ⟦⚠️ MARKA SLOTU — cihaz markası ve sensör sayısı (kaynak şartnamede 11.260 kapasitif sensör geçiyor) yalnızca Özgür Bey'in "merkezde bu cihaz var" teyidi + avukat onayı sonrası bu cümleye girer. Teyitsiz yazılmaz.⟧

İki şeye birden bakıyoruz. Biri ayağa gelen kuvvet ve basınç, diğeri vücudun hareketi: adımın hızı, ağırlık merkezinin duruşta nereye düştüğü, topukla ön ayağın koordinasyonu. Yürüyüş, ayağın yere bastığı ve havada olduğu iki faza ayrılarak inceleniyor.

Ortaya çıkan şey, ayağınızın altındaki basıncın haritası. Hangi bölgeye fazla yük biniyor, iki ayak arasında fark var mı, ağırlık merkeziniz ayakta dururken nereye düşüyor. Bunlar çıplak gözle görülen şeyler değil.

Veriler 3 boyutlu grafiğe dönüşüyor. Tüm yürüme parametrelerinin raporu yaklaşık 10 saniyede çıkıyor. Çıktısını isterseniz yanınızda götürebilirsiniz.

Ölçüm dosyası merkezde kalıyor. Bir sonraki ölçümde ikisini yan yana koyabilmemizin sebebi bu.

## [H2] Ayağın kalıbı nasıl çıkıyor

Ölçümün ikinci yarısı ayakta ya da oturarak yapılıyor. Platformun yüzeyindeki ince pimler yükselip ayağınızın tabanına oturuyor, kendi ağırlığınıza göre basınçları ayarlanıyor, ayağınızın 3 boyutlu kalıbı ekrana çıkıyor. Tarama en fazla 10 saniye sürüyor. Sonra pimler iniyor ve diğer ayağa geçiliyor.

Bu sırada ayak bileğini anatomik olarak nötr pozisyonda tutuyoruz. Arkadan gelen bir lazer çizgisi aşil tendonunu ortalıyor, böylece kalıp ağırlık merkezinin orta hattına göre alınıyor.

Pimli tarama kemikle yumuşak dokuyu farklı hassasiyette okuyor. Ayak boyu da aynı ölçümde çıkıyor.

Sizin yapmanız gereken tek şey, ayağınızı platforma koyup beklemek. 4 adımlık akış kumandayla yürütülüyor ve iki ayak arka arkaya taranıyor.

## [H2] Tasarımdan tezgâha

Ekrandaki 3 boyutlu model üzerinde tabanlığın ayarları yapılıyor: ark yüksekliği, topuk kavrayışı, iç ya da dış kama, metatarsal ped, kalınlık, açı.

Ayakta belirgin bir şekil bozukluğu varsa kalıp olduğu gibi kullanılmıyor. Model üzerinde düzeltme yapılarak nötr bir ayak kalıbı elde ediliyor ve tabanlık onun üzerine kuruluyor.

Sonra veri freze tezgâhına gidiyor. Sıkıştırılmış EVA malzemeden bir takoz makineye yerleştiriliyor ve tabanlık ayak başına 6-10 dakikada frezeleniyor. Son olarak kullanacağınız ayakkabıya göre ölçüleniyor, üstü kaplanıyor.

Üretim, Avrupa 37 ile 50 numara arasında yapılıyor. Dar kalıp 37-40 aralığında ayrıca mevcut.

Tabanlıklar, 1998'den beri çalışan Özgür Irmak Protez ve Ortez atölyesinde üretiliyor. Ölçüm de üretim de aynı çatı altında yapılıyor.

## [H2] Sertliği ne belirliyor

Tabanlığın sertliği ve yoğunluğu kişiye göre planlanıyor. Atölyede 5 farklı yoğunlukta malzeme var. Hangisinin kullanılacağına ölçüm sonrasındaki değerlendirme karar veriyor.

Sertlik, üzerinde konuşulabilen ölçülü bir değer. Kullandığımız takozlar Shore A 21 ile 60 arasında, en yumuşağından en rijidine kadar.

Bu kararı etkileyen şeyler arasında kilo, gün içindeki hareket miktarı, yapılan spor ve ayak tabanının durumu var. Aynı kişinin iki ayağı için iki ayrı sertlik seçilebiliyor.

Ayağında his kaybı olan kişilerde değerlendirmeyi ayrıca dikkatli yürütüyoruz. ⟦⚠️ KLİNİSYEN LAFZI BEKLİYOR — nöropati/diyabetik ayak gibi durumlarda kişi basıncı hissetmediği için "ağrı varsa gelin" tipi bir uyarı işe yaramaz. His-bağımsız bir kontrol cümlesi (ör. günlük gözle kontrol + düşük eşikle başvuru) gerekiyorsa lafzını hekim/teknik sorumlu yazar. Fox bu cümleyi kendisi kuramaz.⟧

## [H2] Ne kadar dayanır, sonra ne oluyor

Peki bir tabanlık ne kadar dayanıyor?

⟦⚠️ ALINTI SLOTU — burada gerçek bir hasta sorusu tırnak içinde çok daha güçlü durur (İnsan Sesi Kapısı kural 4). Özgür Bey'den "hastaların en çok sorduğu 3 şey" alınırsa bu satır onunla değişir. Uydurulmaz.⟧

EVA malzeme ortalama 3-6 ay sonra şok emme özelliğini yitiriyor ve tabanlığın yenilenmesi öneriliyor. Bu süre kiloya, kullanım sıklığına ve yapılan spora göre değişiyor.

Yenilemede ölçümü baştan yapıyoruz. Yeni ölçüm eskisinin yanına konuyor ve arada ne değiştiği görülüyor. Aynı karşılaştırmayı bir operasyon öncesiyle sonrası için de kullanabiliyoruz.

Bir kişide birden fazla çift olabiliyor. Koşu ayakkabısı için ayrı, günlük ayakkabı için ayrı tasarlanabiliyor.

## [H2] Kimler ölçülebilir

Yürüyüşünü değerlendirmek isteyen herkes ölçülebilir. Tabanlığın uygun olup olmadığına, uygunsa hangi yoğunlukta üretileceğine değerlendirme sonrasında birlikte karar veriyoruz.

Ölçüm için merkezimize gelmeniz yeterli.

## [KAPANIŞ — kalın]

Adım adım, birlikte.

---

## SAYFA ALTI — KÜÇÜK PUNTO

Bu içerik genel bilgilendirme amaçlıdır; kişiye özel tıbbi tavsiye ya da tanı yerine geçmez. Kendi durumunuz için merkezimize ya da hekiminize danışın.

Tabanlığın uygunluğu kişiye özel değerlendirme ile belirlenir. Ölçüm, tasarım ve uyarlama merkezimizde teknik sorumlu tarafından yapılır.

Bu sayfa [TARİH] tarihinde güncellenmiştir. İçerik sorumlusu: ⟦⚠️ E-E-A-T KÜNYESİ — sağlık içeriğinde gerçek uzman adı + yetki künyesi gerekir. Özgür Irmak'ın unvan/belge teyidi geldiğinde buraya girer.⟧ · [E-POSTA GİRİLECEK]

---

## SEO

- **Sayfa başlığı:** Yürüme Analizi ve Kişiye Özel Tabanlık | Özgür Irmak Protez ve Ortez
- **Meta açıklama:** Sensörlü bantta yürürken ayağınıza binen basınç ölçülüyor, ayağınızın 3 boyutlu kalıbı çıkarılıyor ve tabanlık bu ölçüme göre üretiliyor. Süreç nasıl işliyor, burada anlattık.
- **Slug:** cozumler/yurume-analizi-ve-kisiye-ozel-tabanlik
- **H1:** Yürüme Analizi ve Kişiye Özel Tabanlık
- **Schema:** `MedicalWebPage` + `FAQPage` (SSS bloğu) · `about: MedicalDevice` değil — cihaz sayfası değil süreç bilgilendirmesi olarak işaretlenir (15/2 yatağı). İç link: Hakkımızda + Çözümler ana sayfası.
- **Anahtar kelime yönü (organik, doldurma yok):** yürüme analizi · kişiye özel tabanlık · ortopedik tabanlık nasıl yapılır · ayak basınç ölçümü. ⟦⚠️ ARAMA HACMİ TEYİDİ — Growth'un kelime taramasıyla doğrulanmadan bu liste kesinleşmez.⟧

---

## SSS (sayfa altına, FAQPage schema ile)

**Yürüme analizi ne kadar sürüyor?**
Bantta yürüme kısmı birkaç dakika. Ayağın 3 boyutlu taraması ayak başına en fazla 10 saniye, raporun çıkması yaklaşık 10 saniye. Randevunun toplam süresi kişiye göre değişiyor. ⟦⚠️ TOPLAM RANDEVU SÜRESİ — kaynakta yok. Özgür Bey'den tipik randevu süresi alınırsa buraya somut aralık girer.⟧

**Tabanlığım ne zaman hazır olur?**
Frezeleme ayak başına 6-10 dakika sürüyor. Ölçümden teslime kadar geçen toplam süre randevu yoğunluğuna göre değişiyor. ⟦⚠️ TESLİM SÜRESİ — merkezden teyit gerekiyor; teyitsiz süre yazılmaz.⟧

**Tabanlığı ne zaman yenilemem gerekir?**
EVA malzeme ortalama 3-6 ayda şok emme özelliğini yitiriyor. Yenilemede ölçüm baştan yapılıyor ve önceki ölçümle karşılaştırılıyor.

**Aynı tabanlığı her ayakkabıda kullanabilir miyim?**
Tabanlık, kullanacağınız ayakkabıya göre ölçülendiriliyor. Spor ayakkabısı ile günlük ayakkabı için ayrı çiftler tasarlanabiliyor.

**Ölçüm için doktor raporu gerekiyor mu?**
⟦⚠️ CEVAP BEKLİYOR — merkezin çalışma pratiği ve sevk/rapor gerekliliği kaynakta yok. Özgür Bey cevaplayacak. Cevap gelmeden bu soru yayına girmez.⟧

---

## YAZARIN NOTU — hangi karar neden

**1. Teknik tarafı geri çektim, hastanın sorusunu öne aldım.**
Şartname bir B2B ihale metni: sensör sayısı, Shore A durometre aralığı, 3 eksenli bıçak, toz haznesi. Bunların hiçbiri hastanın kafasındaki soruya cevap vermiyor. Sayfa şu dört soruya göre kuruldu: *ne ölçülüyor · nasıl geçiyor · neden bana özel · sonra ne oluyor.* Süreler (10 sn tarama, 10 sn rapor, 6-10 dk üretim, 3-6 ay ömür) kaldı, çünkü bunlar hastanın gerçek sorusunun cevabı. "Hızlı" övgüsüne çevrilmedi, "ne kadar sürer" cevabı olarak bırakıldı.

**2. Kondisyon→ürün tablosu yazılmadı (bilinçli).**
Kaynak §5'te pes planus→no:2, epin kalkanei→no:4 tarzı bir eşleştirme var. Web'e konsaydı iki risk birden doğardı: okuyucu kendine tanı koyar, metin de endikasyon iddiasına dönerdi. Yerine "sertliğe değerlendirme karar verir" çerçevesi kuruldu. Bu aynı zamanda KKK ses kuralı 3'ün (birlikte dili) karşılığı.

**3. Marka adı yazılmadı.**
Zebris/Contemplas/Amfit geçmiyor. Kaynak belge bir tedarikçi şartnamesi ve merkezde birebir bu cihazların bulunduğu teyitli değil. Ayrıca cihaz markası kullanımı avukat sorusu #1'e bağlı. ⟦⚠️ MARKA SLOTU⟧ tek yerde açık bırakıldı.

**4. Uyum çizgisi.**
Üstünlük iddiası yok, karşılaştırma yok, fiyat/kampanya/aciliyet yok, "hemen arayın" yok. Tabanlığın etkisi sonuç vaadi olarak değil amaç olarak yazılmadı bile — metin ne yapıldığını anlatıyor, ne kazanacağınızı vaat etmiyor. "2 boyutlu tarayıcıdan farkı budur" cümlesi taslakta vardı, çıkarıldı: teknoloji kategorileri arası üstünlük kıyası bile bu mevzuatta gereksiz risk.

**5. His kaybı kapısı.**
Medikal how-to güvenlik alt-kapısı gereği yüksek riskli alt grubu (nöropati/diyabetik ayak) sessizce geçmedim. Ama uyarının tıbbi lafzını yazmadım — o cümle hekimin. Slot açık ve bayraklı.

**6. Ses.**
Hakkımızda v0.7'nin devamı gibi okunması için: akan cümleler, somut sahne açılışı (ayakkabıyı çıkarıp banda çıkmak), hedef/motivasyon dayatması yok, kapanış marka kilidindeki cümle. Telgraf üslubuna dönmemek için cümle uzunluğu serbest bırakıldı — v06 dersi.

### Tarama sonuçları (zorunlu kapı)

Ölçüm yalnız **gövde** üzerinde yapıldı (H1'den kapanışa; ⟦⚠️⟧ bayrak blokları yayınlanmayacağı için çıkarıldı). 523 kelime · 53 cümle · 25 paragraf · ortalama cümle 9,9 kelime.

```
python3 sablonlar/araclar/slop_tarama.py    → ✅ TEMİZ (çıkış kodu 0)
python3 sablonlar/araclar/sozdizim_tarama.py → SERT bulgu YOK, 2 UYARI (çıkış kodu 2)
```

| Ölçü | Bu metin | Eşik (uyarı / sert) | Durum |
|---|---|---|---|
| Karşıtlık /1000 kelime | 1,9 | 6,0 / 8,0 | temiz |
| Karşıtlık taşıyan cümle oranı | 0,019 | 0,09 / 0,13 | temiz |
| Cümle uzunluğu CV | 0,50 | 0,47 / 0,42 | temiz |
| Kısa cümle oranı (≤6 kelime) | 0,283 | 0,05 / 0,02 | temiz |
| İnsan işareti /1000 | 15,3 | 12,0 / 5,0 | temiz |
| Noktalı virgül /100 kelime | 0,0 | 0,7 / 1,2 | temiz |
| Aforizma oranı | 0,04 | 0,15 / 0,25 | temiz |
| Simetri kalıbı /1000 | 0,0 | 3,0 / 5,0 | temiz |
| Formüler bağlaç oranı | 0,0 | 0,05 / 0,08 | temiz |
| **Somut çapa /100 kelime** | **5,0** | 5,5 / 3,0 | ⚠️ UYARI |
| **Paragraf CV** | **0,377** | 0,44 / 0,30 | ⚠️ UYARI |

**UYARI 1 — somut çapa 5,0 (araç eşiği 5,5). Bu bir üslup sorunu değil, brif açığı.**
İlk taramada ölçü **2,9 ile SERT bölgedeydi** ve metin dışarı çıkamazdı. Kaynaktan hastaya anlamlı gelen gerçek olguları (2 bölümlü ölçüm akışı, 4 adımlık tarama, 37-50 ve 37-40 numara aralıkları, Shore A 21-60, 1998, atölye) geri koyarak 5,0'a çıktı — İnsan Sesi Korpusu'nun kural 5 kotası (100 kelimede ≥5 çapa) artık **doluyor**, aracın kendi uyarı eşiği (5,5) hâlâ biraz üstte. Kalan açığı üslupla kapatmadım — çünkü eksik olan **bilgi**: toplam randevu süresi, teslim süresi, yılda kaç kişiye uygulama yapıldığı, sevk gerekip gerekmediği. Dördü de aşağıdaki soru listesinde. Bu cevaplar gelirse ölçü kendiliğinden 6'nın üstüne çıkar (İnsan Sesi Korpusu §5 kök neden kuralı).

**UYARI 2 — paragraf uzunluğu değişkenliği 0,377 (eşik 0,44).**
Bu bir hizmet süreci sayfası: bölümler adım adım ilerliyor, her adım benzer ağırlıkta, paragraflar da benzer uzunlukta çıkıyor. Web'de taranabilirlik zaten bunu istiyor. Değişkenliği yapay olarak artırmak için paragraf bölmek ya da şişirmek, v06'da düşülen tuzağın aynısı olurdu — ölçüyü hedefe çevirmek. Sesli okumada metin takılmıyor. Bilinçli bırakıldı.

**Taramada görünen ama kasıtlı olan iki şey:** metindeki tek karşıtlık ("çıplak gözle görülen şeyler değil") ve tek aforizma ("Ölçüm daha ayrıntılı konuşur") bütçe dahilinde — kural metin başına 1'er. İnsan işareti 15,3 (eşik 12,0): birinci çoğul fiiller ("bakıyoruz", "tutuyoruz", "karar veriyoruz") ve bir soru taşıyor. Tırnaklı gerçek hasta sorusu gelirse bu ölçü de yükselir.

---

## METİN KALİTE SKORU — 84/100 (B+)

*Rubrik: `marka-bulutu-os-puanlama-rubrigi.md` Bölüm 6, Metin Yazarı ağırlıkları.*

| Kategori | Ağırlık | Puan | Gerekçe |
|---|---|---|---|
| Kopya Kalitesi | %30 | 26/30 | Hastanın 4 gerçek sorusuna cevap veriyor, akıyor, telgraf değil. Eksi: "Sertliği ne belirliyor" bölümü bir cevabı (hangi malzeme kime) mevzuat gereği açık bırakmak zorunda — okuyucu için hafif tatminsiz. |
| Ses Uyumu | %25 | 22/25 | KKK ses kuralları 1-7 uygulandı (kanıt konuşuyor, birlikte dili, ünlem/aciliyet yok, geçmişe atıf yok). v0.7 ile aynı ağızdan okunuyor. Eksi: 50/50 ton dengesinde metin teknik tarafa biraz ağır — Ayhan'ın direktifi gereği bilinçli, ama görsel katman insan tarafını taşımazsa denge bozulur. |
| Doğruluk | %20 | 17/20 | Her olgu kaynak belgeden. Uydurma rakam yok. Eksi: 4 doğrulanmamış alan var, hepsi ⟦⚠️⟧ bayraklı ve cevaplanmadan yayına girmiyor. |
| Onur & Temsil | %15 | 14/15 | Acıma yok, ilham pornosu yok, hedef dayatması yok, öz-tanı daveti yok. Okuyucu özne. |
| Teknik (Türkçe/SEO) | %10 | 5/10 | Türkçe temiz, schema ve slug hazır. Eksi: anahtar kelime seti Growth taramasıyla doğrulanmadı, künye (E-E-A-T) boş, iç link haritası Çözümler yayınına bağlı. |

**Neden A değil:** metin hazır, sayfa değil. 4 olgu eksiği + künye + avukat onayı kapanmadan bu sayfa yayına giremez. Skoru yükseltecek şey yeniden yazım değil, cevaplar.

**İnsan Sesi durumu:** SERT bulgu yok, 2 UYARI gerekçelendirildi (yukarıda). B bandı tavanı uygulanmadı.

---

## AYHAN / ÖZGÜR BEY'E SORULAR (metin bunlarsız da yayına yakın, ama bu 5 cevap sayfayı tamamlar)

1. **Cihaz teyidi:** Merkezde yürüme analizi ve tabanlık üretimi hangi cihazlarla yapılıyor? Şartnamedeki sistemle birebir aynı mı? (Marka adı yazılacaksa ayrıca avukat onayı gerekiyor.)
2. **Toplam randevu süresi:** Bir kişi ölçüm için geldiğinde merkezde tipik olarak ne kadar kalıyor?
3. **Teslim süresi:** Ölçümden tabanlığın teslimine kadar tipik olarak kaç gün geçiyor?
4. **Doktor raporu:** Ölçüm için sevk/rapor gerekiyor mu, yoksa doğrudan gelinebiliyor mu?
5. **His kaybı uyarısı:** Diyabetik ayak/nöropati durumunda merkezin standart bilgilendirmesi ne? Bu cümlenin lafzını hekim/teknik sorumlu yazmalı.
6. **Hasta sorusu (alıntı için):** Tabanlık için gelenlerin en çok sorduğu 3 şey ne? Bir tanesini tırnak içinde metne koymak, sayfayı gözle görülür şekilde insanlaştırır — ve uydurulamaz.

*Bonus (zorunlu değil, ölçüyü yükseltir): merkezde yılda kaç kişiye tabanlık uygulanıyor — kaba aralık yeter.*
