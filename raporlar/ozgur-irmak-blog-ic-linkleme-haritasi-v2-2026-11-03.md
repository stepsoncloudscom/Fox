# Özgür Irmak — Blog İç Linkleme Haritası v2

*Fox · 3 Kasım 2026 · v1 Denetmen'den DÜZELTMEYLE ONAY aldı; bu sürüm o düzeltmeleri işler. Siteye hiçbir şey yazılmadı. Uygulama Kademe 2: Ayhan onayı.*

## v1'den farklar

- 25 bağlam içi link silindi (13 anlam uyumsuz, 8 çift link, 3 gereksiz tekrar, 1 üretici adı geçen cümle). 1 link düzeltildi ("Mevsimsel Protez Bakımı").
- "İlgili Yazılar" artık gövdeye metin bloğu olarak yazılmıyor. Wix'in sayfada zaten görünen bileşeni `relatedPostIds` doluysa o yazıları gösteriyor (canlıda tarayıcıda doğrulandı: protez ayak çeşitleri sayfası kendi 2 ilgili yazısını gösteriyor; alan boşsa en yeni 3 yazıyı gösteriyor, 55 yazıdaki "Koşu bıçağı…" tekrarının sebebi bu). Her yazıya anlama göre elle seçilmiş 3 yazı.
- Mevcut hatalar eklendi: 404 veren 3 link onarımı, "Protez Süreci" linkinin bakım yazısına gittiği 4 yazıda hedef düzeltmesi, 1 düz metin yolun linke çevrilmesi.

## Uygulama güvenlik kuralları (Denetmen şartları)

1. 60 yazının richContent / seoData / memberId / firstPublishedDate / slug / relatedPostIds JSON yedeği alınır.
2. Yayındaki sürüm ile draft arasında fark olan yazı atlanır ve raporlanır.
3. Gövdede `memberId` ve `firstPublishedDate` gönderilmez; mevcut BOLD/ITALIC/LINK süslemeleri korunur, zaten link taşıyan metne ikinci link eklenmez. Slug'lar API'den kopyalanır (3 slug'da birleşik nokta karakteri var).
4. Önce 1 yazıda pilot; canlı sayfada link sayısı, hedeflerin 200 dönmesi, yazar/tarih/SEO/slug'ın değişmediği doğrulanır. Sonra toplu.
5. Toplu işlemden sonra canlıda yeniden ölçülür (kanıt: URL + durum kodu).

## Bağlam içi linkler (61)

| Kaynak | İfade | Hedef |
|---|---|---|
| diyabet-ve-ayak-sağlığı-protez-kullananda-dikkat-edilec | Liner | silikon-liner-nedir-ne-i̇şe-yarar |
| el-ve-kol-ortezleri-ne-i-şe-yarar-kimler-i-çin-uygundur | Ortez Nedir | ortez-nedir-protezden-farkı-ne-afo-ve-kafo-açıklaması |
| protez-bacağın-bileşenleri-nelerdir-soket-liner-pylon-v | liner | silikon-liner-nedir-ne-i̇şe-yarar |
| protezle-merdiven-rampa-ve-denge | rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci |
| protezle-merdiven-rampa-ve-denge | fizyoterapi | fizyoterapinin-protez-sürecindeki-rolü |
| protez-çeşitleri-bacak-ve-kol-protez-türlerine-genel-ba | Kozmetik protez | kozmetik-estetik-kol-ve-el-protezi-nedir-kimler-i-çin-u |
| mikroişlemcili-diz-ile-mekanik-diz-arasındaki-fark-hang | merdivende | protezle-merdiven-rampa-ve-denge |
| protez-bacak-ve-protez-ayak-seçerken-hangi-faktörler-di | mikroişlemcili diz | mikroişlemcili-diz-nedir-nasıl-çalışır |
| protez-bacak-ve-protez-ayak-seçerken-hangi-faktörler-di | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü |
| omuz-dezartikülasyonu-protezi-nedir-kimler-i-çin-uygula | Dirsek altı | dirsek-alti-biyonik-kol-protezi |
| omuz-dezartikülasyonu-protezi-nedir-kimler-i-çin-uygula | Kozmetik Kol | kozmetik-estetik-kol-ve-el-protezi-nedir-kimler-i-çin-u |
| protez-ayaklarda-azami-kullanıcı-ağırlığı-sınırı-neden- | K Aktivite Seviyesi | protez-ayak-seçiminde-k-aktivite-seviyesi-nedir |
| protez-ayak-çeşitleri-hangi-tip-hangi-aktivite-seviyesi | Enerji depolayan | karbon-fiber-protez-ayak-nedir-enerji-depolayan-ayaklar |
| ortez-ve-protezler-hangi-malzemeden-yapılır-termoplasti | AFO | afo-nasıl-kullanılır-günlük-giyim-bakım-ve-değiştirme-z |
| aktif-vakum-sistemli-protez-nedir | liner | silikon-liner-nedir-ne-i̇şe-yarar |
| kalça-dezartikülasyonu-özel-bir-amputasyon-seviyesinde- | Omuz Dezartikülasyonu | omuz-dezartikülasyonu-protezi-nedir-kimler-i-çin-uygula |
| kalça-dezartikülasyonu-özel-bir-amputasyon-seviyesinde- | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü |
| miyoelektrik-biyonik-el-nasıl-çalışır | kol ampütasyonunda | kol-ampütasyonu-sonrası-protez-sürecine-nasıl-hazırlanı |
| miyoelektrik-biyonik-el-nasıl-çalışır | fizyoterapiyle | fizyoterapinin-protez-sürecindeki-rolü |
| protez-ayakta-taban-zemin-uyumu-farklı-yüzeylerde-kulla | koşu bıçağı | koşu-bıçağı-ile-günlük-protez-ayağı-arasındaki-fark |
| protez-ayakta-taban-zemin-uyumu-farklı-yüzeylerde-kulla | Rampa | protezle-merdiven-rampa-ve-denge |
| diz-ustu-protezler | liner | silikon-liner-nedir-ne-i̇şe-yarar |
| diz-ustu-protezler | mikroişlemcili diz | mikroişlemcili-diz-nedir-nasıl-çalışır |
| diz-ustu-protezler | aktivite seviyesi | protez-ayak-seçiminde-k-aktivite-seviyesi-nedir |
| bacak-ampütasyonu-sonrası-protez-sürecine-nasıl-hazırla | Günlük yaşamınızda | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-hayat |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çözümler | miyoelektrik | miyoelektrik-biyonik-el-nasıl-çalışır |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çözümler | Kozmetik protezlerin | kozmetik-estetik-kol-ve-el-protezi-nedir-kimler-i-çin-u |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çözümler | Kozmetik parmak | kozmetik-silikon-parmak-protezi-nedir |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-günlük-bakımı | Mikroişlemcili dizlerin | mikroişlemcili-diz-nedir-nasıl-çalışır |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-günlük-bakımı | mekanik diz | mikroişlemcili-diz-ile-mekanik-diz-arasındaki-fark-hang |
| kol-ampütasyonu-sonrası-protez-sürecine-nasıl-hazırlanı | Günlük yaşamınızda | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-hayat |
| diz-alti-protezi-nedir | soket tipi | protez-soket-türleri-vakum-mu-pin-kilit-mi |
| protez-ayaklar-suya-dayanıklı-mı | kompozit | protez-ayak-malzemeleri-karbon-fiber-ve-kompozit-karşıl |
| protez-ayaklar-suya-dayanıklı-mı | koşu bıçağı | koşu-bıçağı-ile-günlük-protez-ayağı-arasındaki-fark |
| protez-ayaklar-suya-dayanıklı-mı | Mevsimsel Protez Bakımı | mevsimsel-protez-bakımı-yaz-teri-ve-kış-şartları |
| protez-ile-spor-ve-fiziksel-aktivite | liner | silikon-liner-nedir-ne-i̇şe-yarar |
| protez-ile-spor-ve-fiziksel-aktivite | fizyoterapistiniz | fizyoterapinin-protez-sürecindeki-rolü |
| protez-ile-spor-ve-fiziksel-aktivite | kalan uzuv | kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-derinleştirme |
| üst-ekstremite-protezlerinde-miyoelektrik-değerlendirme | Miyoelektrik | miyoelektrik-biyonik-el-nasıl-çalışır |
| üst-ekstremite-protezlerinde-miyoelektrik-değerlendirme | kozmetik protez | kozmetik-estetik-kol-ve-el-protezi-nedir-kimler-i-çin-u |
| üst-ekstremite-protezlerinde-miyoelektrik-değerlendirme | Fizyoterapiyle | fizyoterapinin-protez-sürecindeki-rolü |
| protez-soket-türleri-vakum-mu-pin-kilit-mi | Liner | silikon-liner-nedir-ne-i̇şe-yarar |
| koşu-bıçağı-ile-günlük-protez-ayağı-arasındaki-fark | Protez Ayak Çeşitleri | protez-ayak-çeşitleri-hangi-tip-hangi-aktivite-seviyesi |
| mevsimsel-protez-bakımı-yaz-teri-ve-kış-şartları | liner | silikon-liner-nedir-ne-i̇şe-yarar |
| güdükte-yara-varken-protez-kullanılır-mı | Kalan uzuv | kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-derinleştirme |
| protez-ayak-malzemeleri-karbon-fiber-ve-kompozit-karşıl | K Aktivite Seviyesi | protez-ayak-seçiminde-k-aktivite-seviyesi-nedir |
| protez-bacak-ve-kol-bakimi | suya dayanıklılık | protez-ayaklar-suya-dayanıklı-mı |
| protez-bacak-ve-kol-bakimi | silikon liner | silikon-liner-nedir-ne-i̇şe-yarar |
| protez-bacak-ve-kol-bakimi | diyabet | diyabet-ve-ayak-sağlığı-protez-kullananda-dikkat-edilec |
| protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-hayat | seyahatin | protez-kullananlar-i-çin-seyahat-rehberi |
| protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-hayat | liner | silikon-liner-nedir-ne-i̇şe-yarar |
| protez-ayaklarla-dans-ve-hareket | fiziksel aktivite | protez-ile-spor-ve-fiziksel-aktivite |
| mikroişlemcili-diz-nedir-nasıl-çalışır | Mekanik diz | mikroişlemcili-diz-ile-mekanik-diz-arasındaki-fark-hang |
| dirsek-alti-biyonik-kol-protezi | Liner | silikon-liner-nedir-ne-i̇şe-yarar |
| ampütasyon-sonrası-rehabilitasyon-süreci | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü |
| protez-ayak-seçiminde-k-aktivite-seviyesi-nedir | Protez Ayak Çeşitleri | protez-ayak-çeşitleri-hangi-tip-hangi-aktivite-seviyesi |
| protez-ayak-seçiminde-k-aktivite-seviyesi-nedir | Rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci |
| ortez-nedir-protezden-farkı-ne-afo-ve-kafo-açıklaması | AFO | afo-nasıl-kullanılır-günlük-giyim-bakım-ve-değiştirme-z |
| protez-süreci-ne-kadar-sürer | Rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci |
| protez-kullananlar-i-çin-seyahat-rehberi | Günlük Yaşam | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-hayat |
| protez-kullananlar-i-çin-seyahat-rehberi | liner | silikon-liner-nedir-ne-i̇şe-yarar |

## Onarımlar (8)

| Kaynak | Mevcut | Yeni hedef | Not |
|---|---|---|---|
| kozmetik-estetik-kol-ve-el-protezi-nedir-kimler-i-çin-u | /post/miyoelektrik-el-nasil-calisir | miyoelektrik-biyonik-el-nasıl-çalışır | 404 onarım |
| dirsek-alti-biyonik-kol-protezi | /post/miyoelektrik-el-nasil-calisir | miyoelektrik-biyonik-el-nasıl-çalışır | 404 onarım |
| diz-alti-protezi-nedir | /post/protez-turleri | protez-çeşitleri-bacak-ve-kol-protez-türlerine-genel-ba | 404 onarım |
| aktif-vakum-sistemli-protez-nedir | anchor:Protez Süreci | protez-süreci-ne-kadar-sürer | yanlış hedef (bakım yazısına gidiyordu) |
| pasif-vakum-sistemli-protez-bacak-nedir | anchor:Protez Süreci | protez-süreci-ne-kadar-sürer | yanlış hedef (bakım yazısına gidiyordu) |
| diz-alti-protezi-nedir | anchor:Protez Süreci | protez-süreci-ne-kadar-sürer | yanlış hedef (bakım yazısına gidiyordu) |
| dirsek-alti-biyonik-kol-protezi | anchor:Protez Süreci | protez-süreci-ne-kadar-sürer | yanlış hedef (bakım yazısına gidiyordu) |
| protez-bacağın-bileşenleri-nelerdir-soket-liner-pylon-v | /bacak-protezleri | PAGE:/bacak-protezleri | düz metin yol linke çevrilir |

## İlgili Yazılar (`relatedPostIds`, 60 × 3)

| Yazı | 1 | 2 | 3 |
|---|---|---|---|
| protez-ayakta-taban-zemin-uyumu-farklı-yüzeylerde-kulla | protez-ayak-seçiminde-k-aktivite-seviyes | protez-ayak-çeşitleri-hangi-tip-hangi-ak | protezle-merdiven-rampa-ve-denge |
| protez-ayak-malzemeleri-karbon-fiber-ve-kompozit-karşıl | karbon-fiber-protez-ayak-nedir-enerji-de | protez-ayaklarda-azami-kullanıcı-ağırlığ | protez-ayak-çeşitleri-hangi-tip-hangi-ak |
| koşu-bıçağı-ile-günlük-protez-ayağı-arasındaki-fark | protez-ile-spor-ve-fiziksel-aktivite | karbon-fiber-protez-ayak-nedir-enerji-de | protez-ayak-çeşitleri-hangi-tip-hangi-ak |
| protez-ayaklarda-azami-kullanıcı-ağırlığı-sınırı-neden- | protez-ayak-malzemeleri-karbon-fiber-ve- | protez-ayak-seçiminde-k-aktivite-seviyes | protez-bacak-ve-protez-ayak-seçerken-han |
| protez-ayak-kılıfı-kozmetik-kapak-ne-i-şe-yarar | protez-ayaklar-suya-dayanıklı-mı | protez-bacak-ve-kol-bakimi | protez-ayak-çeşitleri-hangi-tip-hangi-ak |
| protez-ayak-seçiminde-k-aktivite-seviyesi-nedir | protez-ayak-çeşitleri-hangi-tip-hangi-ak | protez-bacak-ve-protez-ayak-seçerken-han | mikroişlemcili-diz-ile-mekanik-diz-arası |
| protez-ayaklar-suya-dayanıklı-mı | protez-ayak-kılıfı-kozmetik-kapak-ne-i-ş | protez-kullananlar-i-çin-seyahat-rehberi | mevsimsel-protez-bakımı-yaz-teri-ve-kış- |
| protez-ayak-çeşitleri-hangi-tip-hangi-aktivite-seviyesi | karbon-fiber-protez-ayak-nedir-enerji-de | protez-bacak-ve-protez-ayak-seçerken-han | protez-ayak-seçiminde-k-aktivite-seviyes |
| karbon-fiber-protez-ayak-nedir-enerji-depolayan-ayaklar | protez-ayak-malzemeleri-karbon-fiber-ve- | koşu-bıçağı-ile-günlük-protez-ayağı-aras | protez-ayak-çeşitleri-hangi-tip-hangi-ak |
| protez-bacak-ve-protez-ayak-seçerken-hangi-faktörler-di | protez-ayak-seçiminde-k-aktivite-seviyes | protez-ayak-çeşitleri-hangi-tip-hangi-ak | protez-bacağın-bileşenleri-nelerdir-soke |
| diz-alti-protezi-nedir | diz-ustu-protezler | protez-soket-türleri-vakum-mu-pin-kilit- | bacak-ampütasyonu-sonrası-protez-sürecin |
| diz-ustu-protezler | mikroişlemcili-diz-nedir-nasıl-çalışır | kalça-dezartikülasyonu-özel-bir-amputasy | diz-alti-protezi-nedir |
| kalça-dezartikülasyonu-özel-bir-amputasyon-seviyesinde- | diz-ustu-protezler | omuz-dezartikülasyonu-protezi-nedir-kiml | ampütasyon-sonrası-rehabilitasyon-süreci |
| protez-bacağın-bileşenleri-nelerdir-soket-liner-pylon-v | protez-soket-türleri-vakum-mu-pin-kilit- | silikon-liner-nedir-ne-i̇şe-yarar | protez-ayak-çeşitleri-hangi-tip-hangi-ak |
| protez-soket-türleri-vakum-mu-pin-kilit-mi | silikon-liner-nedir-ne-i̇şe-yarar | aktif-vakum-sistemli-protez-nedir | pasif-vakum-sistemli-protez-bacak-nedir |
| silikon-liner-nedir-ne-i̇şe-yarar | protez-soket-türleri-vakum-mu-pin-kilit- | kalan-uzuv-bölgesi-bakımı-günlük-kontrol | mevsimsel-protez-bakımı-yaz-teri-ve-kış- |
| pasif-vakum-sistemli-protez-bacak-nedir | aktif-vakum-sistemli-protez-nedir | protez-soket-türleri-vakum-mu-pin-kilit- | silikon-liner-nedir-ne-i̇şe-yarar |
| aktif-vakum-sistemli-protez-nedir | pasif-vakum-sistemli-protez-bacak-nedir | protez-soket-türleri-vakum-mu-pin-kilit- | silikon-liner-nedir-ne-i̇şe-yarar |
| mikroişlemcili-diz-nedir-nasıl-çalışır | mikroişlemcili-diz-ile-mekanik-diz-arası | mikroişlemcili-dizin-pil-şarj-yönetimi-v | diz-ustu-protezler |
| mikroişlemcili-diz-ile-mekanik-diz-arasındaki-fark-hang | mikroişlemcili-diz-nedir-nasıl-çalışır | mikroişlemcili-dizin-pil-şarj-yönetimi-v | protez-ayak-seçiminde-k-aktivite-seviyes |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-günlük-bakımı | mikroişlemcili-diz-ile-mekanik-diz-arası | mikroişlemcili-diz-nedir-nasıl-çalışır | protez-kılavuzu-okuma-servis-ve-garanti |
| protez-çeşitleri-bacak-ve-kol-protez-türlerine-genel-ba | diz-alti-protezi-nedir | miyoelektrik-biyonik-el-nasıl-çalışır | ortez-nedir-protezden-farkı-ne-afo-ve-ka |
| miyoelektrik-biyonik-el-nasıl-çalışır | üst-ekstremite-protezlerinde-miyoelektri | dirsek-alti-biyonik-kol-protezi | kozmetik-estetik-kol-ve-el-protezi-nedir |
| üst-ekstremite-protezlerinde-miyoelektrik-değerlendirme | miyoelektrik-biyonik-el-nasıl-çalışır | dirsek-alti-biyonik-kol-protezi | kol-ampütasyonu-sonrası-protez-sürecine- |
| dirsek-alti-biyonik-kol-protezi | miyoelektrik-biyonik-el-nasıl-çalışır | protez-kolun-dirsek-eklemi-nasıl-çalışır | kol-protezi-günlük-yaşamda-nasıl-takılır |
| protez-kolun-dirsek-eklemi-nasıl-çalışır-mekanik-ve-ele | dirsek-alti-biyonik-kol-protezi | omuz-dezartikülasyonu-protezi-nedir-kiml | üst-ekstremite-protezlerinde-miyoelektri |
| omuz-dezartikülasyonu-protezi-nedir-kimler-i-çin-uygula | protez-kolun-dirsek-eklemi-nasıl-çalışır | kalça-dezartikülasyonu-özel-bir-amputasy | kozmetik-estetik-kol-ve-el-protezi-nedir |
| kozmetik-estetik-kol-ve-el-protezi-nedir-kimler-i-çin-u | miyoelektrik-biyonik-el-nasıl-çalışır | kısmi-el-ve-parmak-protezleri-fonksiyone | kozmetik-silikon-parmak-protezi-nedir |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çözümler | kozmetik-silikon-parmak-protezi-nedir | kozmetik-estetik-kol-ve-el-protezi-nedir | miyoelektrik-biyonik-el-nasıl-çalışır |
| kozmetik-silikon-parmak-protezi-nedir | kısmi-el-ve-parmak-protezleri-fonksiyone | kozmetik-estetik-kol-ve-el-protezi-nedir | protez-bacak-ve-kol-bakimi |
| kol-protezi-günlük-yaşamda-nasıl-takılır-çıkarılır | kozmetik-estetik-kol-ve-el-protezi-nedir | dirsek-alti-biyonik-kol-protezi | kol-ampütasyonu-sonrası-protez-sürecine- |
| kol-ampütasyonu-sonrası-protez-sürecine-nasıl-hazırlanı | üst-ekstremite-protezlerinde-miyoelektri | ampütasyon-sonrası-rehabilitasyon-süreci | protez-ve-psikolojik-uyum |
| bacak-ampütasyonu-sonrası-protez-sürecine-nasıl-hazırla | ampütasyon-sonrası-rehabilitasyon-süreci | i̇lk-protez-ne-beklemeli | güdükte-yara-varken-protez-kullanılır-mı |
| ampütasyon-sonrası-rehabilitasyon-süreci | fizyoterapinin-protez-sürecindeki-rolü | bacak-ampütasyonu-sonrası-protez-sürecin | i̇lk-protez-ne-beklemeli |
| fizyoterapinin-protez-sürecindeki-rolü | ampütasyon-sonrası-rehabilitasyon-süreci | protezle-merdiven-rampa-ve-denge | protez-ile-spor-ve-fiziksel-aktivite |
| i̇lk-protez-ne-beklemeli | protez-süreci-ne-kadar-sürer | protez-ve-psikolojik-uyum | protez-bacak-ve-kol-bakimi |
| protez-süreci-ne-kadar-sürer | i̇lk-protez-ne-beklemeli | sgk-protez-ve-ortez-bedelini-karşılıyor- | protez-ve-ortez-üretiminde-3d-tarama-ve- |
| protez-ve-psikolojik-uyum | fantom-hayalet-uzuv-hissi-nedir | i̇lk-protez-ne-beklemeli | uzuv-kaybı-farkındalık-ayı-toplumsal-far |
| fantom-hayalet-uzuv-hissi-nedir | protez-ve-psikolojik-uyum | ampütasyon-sonrası-rehabilitasyon-süreci | kalan-uzuv-bölgesi-bakımı-günlük-kontrol |
| güdükte-yara-varken-protez-kullanılır-mı | kalan-uzuv-bölgesi-bakımı-günlük-kontrol | silikon-liner-nedir-ne-i̇şe-yarar | diyabet-ve-ayak-sağlığı-protez-kullanand |
| kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-derinleştirme | güdükte-yara-varken-protez-kullanılır-mı | diyabet-ve-ayak-sağlığı-protez-kullanand | mevsimsel-protez-bakımı-yaz-teri-ve-kış- |
| sgk-protez-ve-ortez-bedelini-karşılıyor-mu-başvuru-şart | protez-süreci-ne-kadar-sürer | protez-çeşitleri-bacak-ve-kol-protez-tür | protez-kılavuzu-okuma-servis-ve-garanti |
| protez-ve-ortez-üretiminde-3d-tarama-ve-dijital-teknolo | protez-bacağın-bileşenleri-nelerdir-soke | protez-süreci-ne-kadar-sürer | ortez-ve-protezler-hangi-malzemeden-yapı |
| çocuk-protezleri-büyüme-ve-uyum | i̇lk-protez-ne-beklemeli | protez-ve-psikolojik-uyum | afo-nasıl-kullanılır-günlük-giyim-bakım- |
| protez-bacak-ve-kol-bakimi | mevsimsel-protez-bakımı-yaz-teri-ve-kış- | protez-kılavuzu-okuma-servis-ve-garanti | kalan-uzuv-bölgesi-bakımı-günlük-kontrol |
| mevsimsel-protez-bakımı-yaz-teri-ve-kış-şartları | protez-bacak-ve-kol-bakimi | protez-ayaklar-suya-dayanıklı-mı | silikon-liner-nedir-ne-i̇şe-yarar |
| protez-kılavuzu-okuma-servis-ve-garanti | protez-bacak-ve-kol-bakimi | mikroişlemcili-dizin-pil-şarj-yönetimi-v | sgk-protez-ve-ortez-bedelini-karşılıyor- |
| protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-hayat | protez-kullananlar-i-çin-seyahat-rehberi | protez-ile-spor-ve-fiziksel-aktivite | protez-ve-psikolojik-uyum |
| protez-kullananlar-i-çin-seyahat-rehberi | protez-ile-günlük-yaşam-i-ş-seyahat-sosy | protez-ayaklar-suya-dayanıklı-mı | mikroişlemcili-dizin-pil-şarj-yönetimi-v |
| protez-ile-spor-ve-fiziksel-aktivite | koşu-bıçağı-ile-günlük-protez-ayağı-aras | protez-ayaklarla-dans-ve-hareket | fizyoterapinin-protez-sürecindeki-rolü |
| protez-ayaklarla-dans-ve-hareket | protez-ile-spor-ve-fiziksel-aktivite | protezle-merdiven-rampa-ve-denge | protez-ayak-seçiminde-k-aktivite-seviyes |
| protezle-merdiven-rampa-ve-denge | protez-ayaklarla-dans-ve-hareket | protez-ayakta-taban-zemin-uyumu-farklı-y | fizyoterapinin-protez-sürecindeki-rolü |
| diyabet-ve-ayak-sağlığı-protez-kullananda-dikkat-edilec | kalan-uzuv-bölgesi-bakımı-günlük-kontrol | güdükte-yara-varken-protez-kullanılır-mı | protez-bacak-ve-kol-bakimi |
| uzuv-kaybı-farkındalık-ayı-toplumsal-farkındalık-neden- | protez-ve-psikolojik-uyum | protez-ile-günlük-yaşam-i-ş-seyahat-sosy | çocuk-protezleri-büyüme-ve-uyum |
| afo-nasıl-kullanılır-günlük-giyim-bakım-ve-değiştirme-z | ortez-nedir-protezden-farkı-ne-afo-ve-ka | ortez-ve-protezler-hangi-malzemeden-yapı | fes-fonksiyonel-elektriksel-stimülasyon- |
| ortez-nedir-protezden-farkı-ne-afo-ve-kafo-açıklaması | afo-nasıl-kullanılır-günlük-giyim-bakım- | el-ve-kol-ortezleri-ne-i-şe-yarar-kimler | ortez-ve-protezler-hangi-malzemeden-yapı |
| el-ve-kol-ortezleri-ne-i-şe-yarar-kimler-i-çin-uygundur | ortez-nedir-protezden-farkı-ne-afo-ve-ka | cpm-sürekli-pasif-hareket-cihazı-nedir-n | fes-fonksiyonel-elektriksel-stimülasyon- |
| ortez-ve-protezler-hangi-malzemeden-yapılır-termoplasti | protez-ve-ortez-üretiminde-3d-tarama-ve- | ortez-nedir-protezden-farkı-ne-afo-ve-ka | protez-ayak-malzemeleri-karbon-fiber-ve- |
| cpm-sürekli-pasif-hareket-cihazı-nedir-ne-zaman-kullanı | fes-fonksiyonel-elektriksel-stimülasyon- | el-ve-kol-ortezleri-ne-i-şe-yarar-kimler | ortez-nedir-protezden-farkı-ne-afo-ve-ka |
| fes-fonksiyonel-elektriksel-stimülasyon-nedir-protez-or | cpm-sürekli-pasif-hareket-cihazı-nedir-n | afo-nasıl-kullanılır-günlük-giyim-bakım- | el-ve-kol-ortezleri-ne-i-şe-yarar-kimler |

## Kapsam dışı (bilgi)

- `diz-ustu-protezler` yazısında sorumluluk reddi paragrafı yok (59/60'ta var). Standart ret metninin eklenmesi metin değişikliği olduğu için ayrı onaya bırakıldı.
