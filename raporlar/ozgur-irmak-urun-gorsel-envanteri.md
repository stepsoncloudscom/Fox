# Özgür Protez — Ürün Görseli Envanteri & İndirme Standardı
*Fox · 16 Ağustos 2026 · Konum: Ayhan'ın masaüstü (Fox reposunda değil — 200MB+ ikili dosya)*

> **Neden bu dosya var:** Össur/Ottobock/Fior Gentz görselleri Temmuz–Ağustos'ta indirildi ama **standardı hiçbir yerde yazılı değildi.** 16 Ağu'da Proteor eklenirken standart klasörlerden geriye mühendislikle çıkarıldı. Bir dahaki markada tahmin edilmesin diye buraya yazıldı.

---

## 1 · STANDART (mevcut klasörlerden çıkarıldı, Proteor'da uygulandı)

**Klasör adı:** `<Marka>-Protez-Gorselleri` · `<Marka>-Yurume-Cihazi-Gorselleri`
· Sonuna **` Temiz`** eklenmişse: indirme sonrası **ayıklama turu yapılmış** demektir (tekrar kareler + bozuk/aşırı yakın kırpımlar çıkarılmış). Kalanların numarası korunur, boşluk normaldir (`-01 -03 -05 …`).

**Ürün alt klasörü:** `<Kategori>_<ürün kodu> - <ad>`
· Kategoriler: **Ayak · Diz · El · Kisa** (kısa yürüme cihazı/AFO) · **Uzun** (KAFO) · *(Proteor'da eklendi:* **Sistem** *— diz+bilek+ayak bütünleşik)* · *(Össur liner turunda eklendi:* **Liner · Liner-Corap · Liner-Aksesuar · Liner-Arac** *— Össur'un kendi alt kategorisinden türetildi)* · *(Levitate turunda eklendi:* **Blade · Blade-Kit · Ayak-Kilifi · Taban · Adaptor** *)*
· Ürün kodu varsa öne (`Ayak_1C30-1 - Trias`), yoksa yalnız ad (`Ayak_Pro-Flex-Terra`).

**Dosya adı (sabit SEO öneki + ürün slug + 2 haneli sıra):**
```
Ozgur-protez-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak-<slug>-NN.<uzantı>
```
· Ortez/yürüme cihazı klasörlerinde önek `Ozgur-protez-**ortez**-ossur-…` olur.
· Önek **markadan bağımsız sabittir** — El/Diz ürünlerinde bile `bacak-ayak` geçer. Proteor'da aynen korundu (bkz. §4 açık karar).

---

## 2 · ENVANTER (16 Ağu 2026)

| Klasör | Ürün | Görsel | Ayıklandı mı |
|---|---:|---:|---|
| Ossur-Protez-Gorselleri Temiz | 20 | 64 | ✅ |
| Ossur-Yurume-Cihazi-Gorselleri Temiz | 4 | 7 | ✅ |
| Ottobock-Protez-Gorselleri Temiz | 35 | 156 | ✅ |
| Ottobock-Yurume-Cihazi-Gorselleri | 10 | 36 | ❌ ham |
| Fior-Gentz-Yurume-Cihazi-Gorselleri | 37 | 138 | ❌ ham |
| **Proteor-Protez-Gorselleri** | **35** | **338** | ❌ ham (16 Ağu) |
| **Ossur-Liner-Gorselleri** | **40** | **49** *(+41 ikon)* | ❌ ham (17 Ağu) |
| **Levitate-Protez-Gorselleri** | **27** | **199** | ❌ ham (17 Ağu) |

> ⚠️ **16 Ağu tespiti:** Össur ve Ottobock'un 4 klasörü o gün masaüstünde **görünmez oldu** (Çöp Kutusu boş, aynı anda masaüstüne yeni dosyalar geldi → iCloud Masaüstü senkronu ya da başka cihazdaki taşıma). Yukarıdaki sayılar aynı gün ölçülen son gerçek değerlerdir. **Ayhan iCloud Drive → Masaüstü'nden teyit etmeli.**

### Proteor detayı (16 Ağu, yeni)
- **315** ürün görseli · **18** yaşam karesi (`_Yasam-Kareleri/`) · **5** ikon/piktogram (`_Ikon-Piktogram/`) · 222 MB
- **34/35 üründe** ürün çekimi var · 800px altı **sıfır** · 1000px+ **101** görsel
- Kaynak: `proteor.com/components/` + `us.proteor.com` (modern `/feet/ /knees/ /ankles/` + eski `/composants/`), içerik hash'iyle tekilleştirildi.
- Üretim betiği: `sablonlar/araclar/proteor_gorsel_indir.py`

### Össur Linerler detayı (17 Ağu, yeni)
`~/Desktop/Ossur-Liner-Gorselleri/` · **40 ürün klasörü · 49 ürün görseli · 41 ikon · 435 MB** · betik `sablonlar/araclar/ossur_liner_gorsel_indir.py`

- **Kaynak Össur Türkiye (`ossur.com/tr-tr`), ürün adları ve kategori Türkçe geldi** — `commercialName` alanı doğrudan sitenin TR kaydı. Uydurma çeviri yok.
- **Kategori dağılımı:** 32 `Liner_` · 4 `Liner-Corap_` · 2 `Liner-Aksesuar_` · 2 `Liner-Arac_`. Össur bu dördünü tek "Linerler" menüsüne koyuyor; klasör adında ayrıldı ki çorap/aksesuar ürün gibi sayfalanmasın.
- **Çözünürlük: medyan 6000px, maksimum 7680px, 1000px altı sıfır.** Dört markanın en iyi kaynağı.
- **Ürün kodu = Össur'un kendi `PN` numarası** (`Liner_PN20011 - Iceross Dermo Locking`). Ottobock'taki `1C30-1` mantığının Össur karşılığı.

**Teknik yöntem (bir dahaki Össur turunda tekrar keşfedilmesin):**
1. `ossur.com/tr-tr` sayfaları **client-side render**; HTML'de ürün görseli **yok**, `__NEXT_DATA__` içindeki `content` boş gelir. Sayfayı curl'lemek işe yaramaz — Proteor'daki HTML-kazıma yöntemi burada çalışmaz.
2. Veri, sayfanın tarayıcıda çağırdığı ürün API'sinden gelir (bifrost, betiğin başında yazılı): `?limit=0&loadLevel=full&locale=tr-tr` → **tek istekte 234 ürünlük tüm TR kataloğu** (ayak, diz, kol, kilit, adaptör dahil). Liner turu bunun `/linerler/` dilimi.
3. Görseller Cloudinary'de. Sitenin verdiği URL bir **dönüşüm** taşır (`f_auto,q_auto,w_1400,h_1400,c_pad`) → 1400px. Bu blok URL'den **silinince orijinal iner** (3000–7680px). Betik bunu yapar.

**Bulgular:**
1. **✅ Sitenin gösterdiği 1400px tavan değil.** Eski `Ossur-Protez-Gorselleri` klasöründeki 1400–1600px kareler bu yüzden öyle; orijinaller 4–5 kat büyük. **Ayak/Diz/Kol tarafı aynı betikle yeniden çekilirse çözünürlük sıçrar** — `YOL` sabitini değiştirmek yetiyor.
2. **⚠️ Ürün başına tek stüdyo karesi.** Össur TR ürün sayfasında galeri yok, tek hero görseli var; 6 üründe API ek kare veriyor (en fazla 4). Proteor'daki 9 kare/ürün yoğunluğu burada yok — sayfa tasarımı buna göre kurulmalı.
3. **⚠️ Kaynakta paylaşılan kare:** PN20041 Iceross Stabilo Junior Locking ile PN20042 Iceross Dermo Junior Locking **aynı fotoğrafı** kullanıyor (bayt bayt aynı). İki ürün sayfası aynı görselle çıkacaksa bu bilinçli bir karar olmalı. *Betik dersi: tekilleştirme ürün içinde yapılır, ürünler arasında yapılmaz — global hash ikinci ürünün klasörünü boş bırakıyordu.*
4. **ℹ️ 41 ikon/piktogram** (`_Ikon-Piktogram/`) ürüne değil **özelliğe** ait: aktivite seviyesi, güdük şekli, yumuşak doku durumu, el becerisi, süspansiyon yöntemi. Marka genelinde ortak kullanıldığı için ürün klasörlerine kopyalanmadı, kökte tek kopya duruyor. Ürün karşılaştırma tablosu ya da "hangi liner sana uygun" akışı kurulacaksa hazır görsel dil.


### Levitate detayı (17 Ağu, yeni — 5. marka)
`~/Desktop/Levitate-Protez-Gorselleri/` · **27 ürün klasörü · 199 görsel · 280 MB** · kaynak `letslevitate.com` · betik `sablonlar/araclar/levitate_gorsel_indir.py`

**Levitate kim:** protez ayak/blade üreticisi — Forever ayak ailesi (S / LP / 6" / 7" / 9"), 8" ve 10" koşu blade'leri, footshell, taban, adaptör hattı. Dört markanın yanına 5. olarak eklendi.

| Kategori | Ürün | Görsel |
|---|---:|---:|
| `Ayak_` (Forever ailesi) | 5 | 65 |
| `Adaptor_` | 14 | 85 |
| `Blade_` + `Blade-Kit_` | 4 | 28 |
| `Ayak-Kilifi_` (footshell) | 2 | 13 |
| `Taban_` (sole) | 2 | 8 |

**Teknik yöntem:** mağaza **Shopify**. Shopify her mağazada açık bir katalog ucu bırakır: `/products.json?limit=250` → tüm ürünler + görsel listesi, verilen `src` zaten master dosya. Kazıma yok, tek istek. *(Üç ayrı çıkarma yöntemi biriktirdik: HTML kazıma = Proteor/Zebris · gizli ürün API'si = Össur · açık Shopify ucu = Levitate. Yeni markada önce platform tespit edilir, yöntem ondan sonra seçilir.)*

**Bulgular:**
1. **⚠️ Görsellerin tamamı CGI render, fotoğraf değil.** Beyaz zeminde 3B ürün görselleri; tek bir yaşam karesi, kullanıcı ya da ortam karesi yok. Sonuç: `_Yasam-Kareleri/` klasörü kurulmadı — **çünkü kaynakta yok.** Bir ürün sayfasında Össur/Ottobock'un stüdyo **fotoğrafları** ile Levitate'in render'ları yan yana gelirse görsel dil kırılır; ya hepsi ayrı bloklarda durur ya da tek dil seçilir.
2. **⚠️ Çözünürlük Össur'un altında:** medyan 1920px, maksimum 3085px (Össur medyan 6000px). 800px altı yok; tek kare 657px (`Adapter - Male`, kaynakta öyle). Baskı işi için yeterli değil, web için fazlasıyla yeterli.
3. **ℹ️ Ürün kodu yok.** Össur `PN20011`, Ottobock `1C30-1` verirken Levitate katalogda kod taşımıyor (kodlar yalnız varyant SKU'sunda). Klasör bu yüzden `<Kategori>_<ad>` — standardın "kod yoksa yalnız ad" dalı.
4. **ℹ️ Kaynakta paylaşılan kareler:** Forever 6"/7"/9" ortak kareler kullanıyor; `Blade 10" Kit`in 8 karesi `Blade 10"` ile birebir aynı. Össur'daki gibi her ürün klasörüne kondu — kit ile ürünü aynı görselle sayfalamak bilinçli karar olmalı.
5. **✅ Render-and-review yapıldı** (5 Haz dersi): örneklem gözle açıldı, hepsi doğru ürünü gösteriyor; logo/ölçü tablosu/placeholder karışmamış.

---

### Zebris — yürüme analizi cihazı (17 Ağu, yeni klasör tipi)
`~/Desktop/Zebris-Yurume-Analizi-Gorselleri/` · **10 görsel** · 4,8 MB · kaynak `zebris.de/en/medical/*` · betik `sablonlar/araclar/zebris_gorsel_indir.py`

**Neden standarttan sapıyor (bilinçli):** Bu klasör *ürün* değil *hizmet sayfası* besliyor. Üç sapma:
1. Klasör adı `Zebris-Yurume-**Analizi**-Gorselleri` — mevcut `…-Yurume-Cihazi-…` ortez/AFO demek, çakışmasın diye.
2. Alt klasör yok (10 dosya, tek düzey).
3. Dosya adı öneki `ozgur-protez-yurume-analizi-` — rakip klinik adları (`luxmed-nesa-proklinik…`) **gömülmedi**; küçük harf. Ayhan sabit öneki isterse toplu adlandırma 1 dakika.

| Dosya (önek `ozgur-protez-yurume-analizi-`) | Ne | Çözünürlük |
|---|---|---|
| `zebris-fdm-t-klinik-yurume-bandi.jpg` | h/p/cosmos tabanlı klinik band, ürün çekimi | 4000×3091 |
| `zebris-fdm-t-yurume-bandi-tutamakli.jpg` | Tutamaklı + oturaklı klinik varyant | 4000×3091 |
| `zebris-ayak-tabani-basinc-haritasi-3d.png` | Band üzerinde 3B basınç tepeleri | 2103×897 |
| `zebris-yurume-analizi-yazilimi-kamera-gorunumu.jpg` | Yazılım: 3B basınç + senkron video | 1200×719 |
| `zebris-ayak-yuvarlanma-basinc-dagilimi-ekrani.jpg` | Yazılım: sağ/sol yuvarlanma haritası | 1200×719 |
| `zebris-statik-durus-analizi-ciplak-ayak.jpg` | Yazılım: statik duruş + yük dağılımı %'leri | 1200×719 |
| `zebris-yurume-analizi-raporu.jpg` | Çıktı raporu sayfaları | 1200×675 |
| `zebris-yurume-yolu-basinc-olcum-platformu.jpg` | Uzun yürüme yolu basınç platformu | 1200×798 |
| `zebris-pdm-c-basinc-olcum-platformu.jpg` | Platform + ekran, kullanım karesi (insanlı) | 1999×2622 |
| `zebris-ayak-basinc-dagilimi-3d-model.jpg` | Tek ayak 3B basınç modeli | 852×416 |

**Render-and-review iki hata yakaladı — ikisi de dosya adına güvenmekten:**
- `Laufbaender/TLR4_h.jpg` (4167px, en yüksek çözünürlüklü kare) **Reebok tüketici koşu bandı.** Medikal sayfada klinik cihaz gibi durur → elendi.
- `Trittschaum_Aufsicht_260520.jpg` — "Aufsicht" üstten görünüm; içerik **boş teal plaka**, basınç haritası değil → `Trittschaum_Druckgebirge` ile değiştirildi.
- Teknik not: zebris.de TYPO3; sayfada görseller 576px `_processed_` türev. Orijinal yalnız lightbox `href`inde ya da `srcset`in son adımında. Türevi indiren bir betik 10 karenin 10'unu da 576px alırdı.

### Contemplas + Amfit — donanım zincirinin diğer iki ayağı (17 Ağu)
Sayfa tek cihaz değil bir **zincir** anlatıyor: Zebris ölçer → Contemplas videoyla eşler → Amfit kalıbı çıkarıp tabanlığı freze eder. Her ayak kendi klasöründe, kendi öneki ile.

`~/Desktop/Contemplas-Yurume-Analizi-Gorselleri/` · 3 görsel · 6,0 MB · kaynak `contemplas.com` (WordPress, `wp-content/uploads` = orijinal)

| Dosya (önek `ozgur-protez-yurume-analizi-`) | Ne | Çözünürlük |
|---|---|---|
| `contemplas-yazilim-olcum-modulleri.png` | Yazılımın 5 ölçüm katmanı etiketli (markersız takip / kuvvet / EMG / basınç / zamansal-uzamsal) | 7680×4320 |
| `contemplas-cok-kamerali-video-analizi.jpg` | 5 kameralı kurulum, kameralar numaralı | 5184×3456 |
| `contemplas-templo-yazilimi-ekrani.png` | TEMPLO yazılımı açılış ekranı | 1024×630 |

`~/Desktop/Amfit-Tabanlik-Uretim-Gorselleri/` · 3 görsel · 365 KB · kaynak `amfit.com` · format **webp** (web'e hazır; Wix kabul eder, düzenleme gerekirse dönüştürülür)

| Dosya (önek `ozgur-protez-kisiye-ozel-tabanlik-`) | Ne | Çözünürlük |
|---|---|---|
| `amfit-pimli-dijitizer-ve-cad-cam-freze.webp` | Freze + renkli pimli sayısallaştırıcı platformu, tek karede | 1600×1229 |
| `amfit-freze-tabanlik-uretimi.webp` | Freze detayı, takoz kesilirken | 1400×1400 |
| `amfit-cam-yazilimi-tabanlik-yerlesimi.webp` | CAM yazılımı: takoz üzerine tabanlık yerleşimi | 1600×1292 |

**Seçimde elenenler ve sebepleri:**
- **Amfit iMPRESS (köpük kalıp tarayıcı) kareleri alınmadı.** Şartname "ayak tabanındaki **algılayıcı pimler**" diyor — iMPRESS köpük kalıp tarar, farklı ölçüm yöntemi. Görsel doğru cihazı göstermezse metinle çelişir.
- **Contemplas'ın klinik/spor kulübü mekân kareleri alınmadı** (`spital_speising`, `hessingpark`, forma-sponsor duvarlı salon). Üçüncü tarafın tesisi; Özgür Protez sayfasında **"bizim merkezimiz" gibi okunur.**
- ⚠️ Aynı risk kalan `contemplas-cok-kamerali-video-analizi.jpg` için de geçerli — başka bir laboratuvar. Yöntem anlatan bir şema gibi, altyazıyla ("çok kameralı analiz prensibi") kullanılabilir; mekân iddiası taşıyan bir yere konmaz.
- ℹ️ TEMPLO ekranı "Version 2024" yazıyor — sayfa bir süre sonra tarihlenir.

## 3 · BULGULAR (Proteor turu)

1. **🔴 ALLUX 2 — görsel yok.** Proteor'un kendi 3 sayfasında da tek görsel var, o da **404 ölü bağlantı** (`Visuel-paysage-prothese.jpg`). Üreticinin sitesindeki kırık bağlantı; bayi sitesinden çekilmedi (üçüncü taraf telifi + düşük kaynak güvenilirliği). **Görsel doğrudan Proteor'dan istenmeli.**
2. **⚠️ Proteor'un varlık kalitesi Össur/Ottobock'un altında.** *(17 Ağu düzeltmesi: "Össur 1400–1600px verir" ölçümü **sitenin gösterdiği türev**e aitti; Össur'un orijinalleri 6000px+ — bkz. §2 Össur Linerler bulgu 1. Aradaki fark bu yüzden yazılandan büyük.)* Össur/Ottobock 1400–1600px kare veriyor; Proteor'un eski Freedom hattında (Sierra, Agilix, Plie 3, RUSH ailesi, Pacifica) **orijinaller 279×349px**. Kırpılmış değil — kaynağın kendisi o. ABD sitesi birleştirilerek 800px altı sıfıra indirildi ama bazı ürünlerde tavan 952px'te kalıyor.
3. **⚠️ Yürüme cihazı tarafı Proteor'da ürün granülünde yok.** `proteor.com/equipment/` sayfaları ürün değil **kategori** sayfası (ankle-foot-orthoses, leg-orthoses…). Ottobock/Fior Gentz'deki gibi `Kisa_/Uzun_` ürün klasörü kurulamaz. Bu yüzden **yalnız `Proteor-Protez-Gorselleri` kuruldu.**
4. **✅ Doğrulandı, hata değil:** Ottobock klasöründeki F23/F24 Maverick, VS4 Kintrol, VS5 Restore, LP2-W2 Freestyle Swim **doğru yerde.** 2020 Freedom Innovations devrinde Ottobock Maverick ailesini ve Kintrol'ü **elinde tuttu**; Proteor'a Plie3, Kinnex, Kinterra, Agilix, DynAdapt, Sierra, Highlander, Pacifica geçti.

---

## 4 · AÇIK KARARLAR (Ayhan)

| # | Karar | Fox'un varsayımı (uygulandı) |
|---|---|---|
| 1 | Dosya adı önekine `proteor` eklensin mi? | **Eklenmedi** — önek site geneli sabit dize. Toplu yeniden adlandırma 1 dakikalık iş, geri alınabilir. |
| 2 | Proteor klasörü "Temiz" turundan geçsin mi? | Ham bırakıldı; ayıklama Ayhan'ın gözüyle yapılır. |
| 3 | ALLUX 2 görselleri Proteor'dan istenecek mi? | Beklemede. |
| 4 | Liner dosya adı önekine `liner` eklensin mi? | **Eklendi** (`Ozgur-protez-**liner**-ossur-…`) — ortez klasörlerindeki `-ortez-` varyantı örnek alındı. Sebep: liner ürün adlarının hiçbirinde ("iceross-dermo-locking") kategori kelimesi geçmiyor, sabit önek de "bacak-ayak" diyor; dosya "silikon liner" görsel aramasına hiçbir yerden bağlanmıyordu. İstenmezse toplu adlandırma 1 dakika. |
| 5 | Össur Ayak/Diz/Kol klasörleri yeni betikle **yeniden mi çekilsin**? | Çekilmedi — talep linerdi. Ama §2'de ölçüldü: mevcut kareler 1400–1600px, orijinaller 6000px+. Karar Ayhan'da. |
| 6 | PN20041 ↔ PN20042 aynı fotoğrafı paylaşıyor (kaynakta öyle). İki ürün sayfası aynı görselle mi çıksın? | Her iki klasöre de kondu; ayrım isteniyorsa kendi çekimimiz gerekir. |
| 7 | **Levitate bu hattın parçası mı?** Dosya adı öneki diğer dört markayla aynı (Özgür Protez SEO dizesi) verildi. | **Varsayıldı** — talep "öncekiler gibi" geldi, marka da protez ayak/blade üreticisi. Levitate başka bir iş içinse önek yanlış; toplu adlandırma 1 dakika. |
| 8 | Levitate render'ları Össur/Ottobock fotoğraflarıyla aynı sayfada mı kullanılacak? | Karar Ayhan'da — görsel dil çakışması §2'de yazılı. |

---

## 5 · 🔴 TELİF BAYRAĞI (dört marka için de geçerli — kapanmadı)

Bu görsellerin tamamı **üreticinin telifli materyalidir.** Yazılı kullanım izni / bayilik belgesi olmadan sitede yayınlanması:
- telif ihlali riski,
- **belgesiz "yetkili bayi" iması** (medikal bağlamda ayrıca ağır),
- Wix'in kendi ürün alanı uyarısıyla da çelişir (*"Write your own description instead of using manufacturers' copy"*).

Aynı bayrak Özgür Irmak marka kimliği denetiminde **"Össur telifli görseller"** maddesi olarak zaten açılmıştı — kapanmadı, Proteor'la birlikte kapsamı büyüdü. **Zebris'te bayrak bir kat daha ağır (17 Ağu):** görsel yalnız telif değil **cihaz sahipliği iması** taşıyor. Merkezde birebir bu cihazın bulunduğu teyit edilmeden Zebris marka görseli sitede kullanılırsa, sayfa sahip olunmayan bir cihazı gösterir — bu telif değil **yanıltıcı tanıtım**dır (TİTCK alanı). Yürüme Analizi sayfasının 11 kalemlik teknik teyidi (Denetmen D1) bu görsellerin de kapısıdır. **Contemplas ve Amfit'te aynı kapı üç kat daha dar:** Amfit freze (CAD/CAM üretim ünitesi) merkezde fiilen var mı, yoksa tabanlık dışarıda mı frezeliyor? Görsel "bizde bu makine var" der; teyit yoksa yerine süreç anlatan bir şema konur, makine fotoğrafı konmaz.
**Fox avukat değildir; işaretler.** Yayın öncesi: ya üreticiden yazılı görsel kullanım izni, ya kendi çekimlerimiz.

*Yan not (sarı):* Dosya adlarında rakip klinik adları gömülü (`luxmed-nesa-proklinik-teknik-ortopedi`). SEO kazancı ile marka hijyeni arasında Ayhan kararı — ayrı ele alınacak.

---
*Bağlı belgeler: `raporlar/ozgur-irmak-urun-metinleri-uyum-plani.md` (73 Wix ürünü, metin tarafı) · `marka-bulutu-os-medikal-protez-bagi.md` (TİTCK/uyum zemini)*
