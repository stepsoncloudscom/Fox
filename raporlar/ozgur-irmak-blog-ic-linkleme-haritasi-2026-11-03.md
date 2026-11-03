# Özgür Irmak — Blog İç Linkleme Haritası v1

*Fox · 3 Kasım 2026 · Kaynak: Wix Blog API (60 canlı yazı, salt-okuma) + canlı SSR metni. Durum: TASLAK — Denetmen ve Ayhan onayı bekliyor; siteye hiçbir şey yazılmadı.*

## Yöntem

- **Kelime değişmez.** Bağlam içi link yalnız yazıda zaten geçen ifadeye eklenir; cümle yeniden yazılmaz. Başlık, ilk paragraf, sorumluluk reddi ve zaten link taşıyan metin parçası atlanır.
- **Yazı başına en fazla 3 bağlam içi link**, öncelik aynı konu kümesi.
- **"İlgili Yazılar" bloğu:** her yazının sorumluluk reddi paragrafının hemen önüne başlık + 3 maddelik liste (aynı kümeden, bağlam içinde zaten linklenmemiş yazılar; metin = yazının canlı başlığı). Yeni içerik yok, yalnız gezinme.
- **Kırık link onarımı:** 404 dönen 2 mevcut link canlı karşılığına çevrilir.

## Kırık linkler (curl ile 404 doğrulandı)

| Kırık hedef | Bulunduğu yazı | Yeni hedef |
|---|---|---|
| /post/miyoelektrik-el-nasil-calisir | Kozmetik (Estetik) Kol ve El · Dirsek Altı Biyonik Kol (2×) | /post/miyoelektrik-biyonik-el-nasıl-çalışır |
| /post/protez-turleri | Diz Altı Protezi Nedir? | /post/protez-çeşitleri-bacak-ve-kol-protez-türlerine-genel-bakış |

## Konu kümeleri

- **Protez ayak** (9): `protez-ayak-çeşitleri-hangi-tip-hangi-ak`, `protez-ayak-seçiminde-k-aktivite-seviyes`, `karbon-fiber-protez-ayak-nedir-enerji-de`, `protez-ayak-malzemeleri-karbon-fiber-ve-`, `koşu-bıçağı-ile-günlük-protez-ayağı-aras`, `protez-ayaklarda-azami-kullanıcı-ağırlığ`, `protez-ayak-kılıfı-kozmetik-kapak-ne-i-ş`, `protez-ayaklar-suya-dayanıklı-mı`, `protez-ayakta-taban-zemin-uyumu-farklı-y`
- **Bacak protezi yapısı/seviye** (12): `protez-bacak-ve-protez-ayak-seçerken-han`, `diz-alti-protezi-nedir`, `diz-ustu-protezler`, `kalça-dezartikülasyonu-özel-bir-amputasy`, `protez-bacağın-bileşenleri-nelerdir-soke`, `protez-soket-türleri-vakum-mu-pin-kilit-`, `silikon-liner-nedir-ne-i̇şe-yarar`, `pasif-vakum-sistemli-protez-bacak-nedir`, `aktif-vakum-sistemli-protez-nedir`, `mikroişlemcili-diz-nedir-nasıl-çalışır`, `mikroişlemcili-diz-ile-mekanik-diz-arası`, `mikroişlemcili-dizin-pil-şarj-yönetimi-v`
- **Genel** (1): `protez-çeşitleri-bacak-ve-kol-protez-tür`
- **Kol/el protezi** (9): `miyoelektrik-biyonik-el-nasıl-çalışır`, `üst-ekstremite-protezlerinde-miyoelektri`, `dirsek-alti-biyonik-kol-protezi`, `protez-kolun-dirsek-eklemi-nasıl-çalışır`, `omuz-dezartikülasyonu-protezi-nedir-kiml`, `kozmetik-estetik-kol-ve-el-protezi-nedir`, `kısmi-el-ve-parmak-protezleri-fonksiyone`, `kozmetik-silikon-parmak-protezi-nedir`, `kol-protezi-günlük-yaşamda-nasıl-takılır`
- **Süreç & rehabilitasyon** (12): `kol-ampütasyonu-sonrası-protez-sürecine-`, `bacak-ampütasyonu-sonrası-protez-sürecin`, `ampütasyon-sonrası-rehabilitasyon-süreci`, `fizyoterapinin-protez-sürecindeki-rolü`, `i̇lk-protez-ne-beklemeli`, `protez-süreci-ne-kadar-sürer`, `protez-ve-psikolojik-uyum`, `fantom-hayalet-uzuv-hissi-nedir`, `güdükte-yara-varken-protez-kullanılır-mı`, `sgk-protez-ve-ortez-bedelini-karşılıyor-`, `protez-ve-ortez-üretiminde-3d-tarama-ve-`, `çocuk-protezleri-büyüme-ve-uyum`
- **Bakım** (4): `kalan-uzuv-bölgesi-bakımı-günlük-kontrol`, `protez-bacak-ve-kol-bakimi`, `mevsimsel-protez-bakımı-yaz-teri-ve-kış-`, `protez-kılavuzu-okuma-servis-ve-garanti`
- **Günlük yaşam** (7): `protez-ile-günlük-yaşam-i-ş-seyahat-sosy`, `protez-kullananlar-i-çin-seyahat-rehberi`, `protez-ile-spor-ve-fiziksel-aktivite`, `protez-ayaklarla-dans-ve-hareket`, `protezle-merdiven-rampa-ve-denge`, `diyabet-ve-ayak-sağlığı-protez-kullanand`, `uzuv-kaybı-farkındalık-ayı-toplumsal-far`
- **Ortez** (6): `afo-nasıl-kullanılır-günlük-giyim-bakım-`, `ortez-nedir-protezden-farkı-ne-afo-ve-ka`, `el-ve-kol-ortezleri-ne-i-şe-yarar-kimler`, `ortez-ve-protezler-hangi-malzemeden-yapı`, `cpm-sürekli-pasif-hareket-cihazı-nedir-n`, `fes-fonksiyonel-elektriksel-stimülasyon-`

## Bağlam içi linkler (86)

| Kaynak yazı | Link ifadesi | Hedef | Cümle |
|---|---|---|---|
| diyabet-ve-ayak-sağlığı-protez-kullananda-dik | farkındalık | uzuv-kaybı-farkındalık-ayı-toplumsal-farkında | …ktiğini en iyi hekiminiz bilir. Bu yazı genel bir **farkındalık** çerçevesi veriyor; kişisel planınızı hekiminizle … |
| diyabet-ve-ayak-sağlığı-protez-kullananda-dik | Liner | silikon-liner-nedir-ne-i̇şe-yarar | …tığınız günlük rutine eklenen bir dikkat katmanı. **Liner**'ı temizlerken, cildi gözden geçirirken, aynı anda… |
| diyabet-ve-ayak-sağlığı-protez-kullananda-dik | günlük bakımın | protez-bacak-ve-kol-bakimi | …Ağrı beklemeden kontrol etmek demek, **günlük bakımın** sırasını değiştirmek demek. Önce bakılır, sonra "… |
| el-ve-kol-ortezleri-ne-i-şe-yarar-kimler-i-çi | Ortez Nedir | ortez-nedir-protezden-farkı-ne-afo-ve-kafo-aç | …Protez, eksik bir uzvun yerini alıyor. Bu ayrımı "**Ortez Nedir**, Protezden Farkı Ne?" başlıklı yazımızda daha ayr… |
| protez-bacağın-bileşenleri-nelerdir-soket-lin | liner | silikon-liner-nedir-ne-i̇şe-yarar | …4 parça birlikte çalışıyordu: soket, **liner**, pylon, ayak ünitesi. Genel yapıyı /bacak-protezl… |
| protez-bacağın-bileşenleri-nelerdir-soket-lin | enerji depolayan | karbon-fiber-protez-ayak-nedir-enerji-depolay | …. Sabit modelleri var, Össur ve Ottobock kaynaklı **enerji depolayan** modelleri var.… |
| protezle-merdiven-rampa-ve-denge | rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci | …Merdiven inip çıkma, **rehabilitasyon** programının kendi başlığı olan bir parçasıdır. Ge… |
| protezle-merdiven-rampa-ve-denge | fizyoterapi | fizyoterapinin-protez-sürecindeki-rolü | …Protez kullanan biri için bu, Özgür Irmak'ta **fizyoterapi** programının genellikle ilk 2-3 hedefinden biri ol… |
| protezle-merdiven-rampa-ve-denge | Günlük bakım | protez-bacak-ve-kol-bakimi | …**Günlük bakım** rutininin denge ve yürüyüşle ilişkisini Protez Ba… |
| kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-der | Takma ve çıkarma | kol-protezi-günlük-yaşamda-nasıl-takılır-çıka | …**Takma ve çıkarma** anları bölgeye en çok yük bindiği zamanlar. Harek… |
| protez-çeşitleri-bacak-ve-kol-protez-türlerin | Kozmetik protez | kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | …yön var: 1) kozmetik, 2) mekanik, 3) myoelektrik. **Kozmetik protez** görünümü tamamlar. Mekanik protez kablo ve kayış … |
| mikroişlemcili-diz-ile-mekanik-diz-arasındaki | Mikroişlemcili diz | mikroişlemcili-diz-nedir-nasıl-çalışır | …**Mikroişlemcili diz**, içindeki sensörlerle adımın 3 evresinden hangisi… |
| mikroişlemcili-diz-ile-mekanik-diz-arasındaki | merdivende | protezle-merdiven-rampa-ve-denge | …a pnömatik bir mekanizma her adımda, düz yolda da **merdivende** de, aşağı yukarı benzer bir tepki verir. Zemin de… |
| protez-bacak-ve-protez-ayak-seçerken-hangi-fa | mikroişlemcili diz | mikroişlemcili-diz-nedir-nasıl-çalışır | …cilerin ürettiği enerji depolayan ayak üniteleri, **mikroişlemcili diz** gibi bileşenler gündeme gelebiliyor. Meslek de bi… |
| protez-bacak-ve-protez-ayak-seçerken-hangi-fa | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü | …Ortopedi hekimi, **fizyoterapist** ve protez-ortez teknik sorumlusu birlikte değerle… |
| omuz-dezartikülasyonu-protezi-nedir-kimler-i- | Dirsek altı | dirsek-alti-biyonik-kol-protezi | …**Dirsek altı** ya da dirsek üstü amputasyonda kolun bir kısmı, b… |
| omuz-dezartikülasyonu-protezi-nedir-kimler-i- | Kozmetik Kol | kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | …ketsiz protezler de tercih ediliyor; bu seçeneği "**Kozmetik Kol** ve El Protezi Nedir?" başlıklı yazımızda ele aldı… |
| protez-ayaklarda-azami-kullanıcı-ağırlığı-sın | K Aktivite Seviyesi | protez-ayak-seçiminde-k-aktivite-seviyesi-ned | …iyesine göre model seçimini Protez Ayak Seçiminde **K Aktivite Seviyesi** Nedir? yazımızda, genel bakım ilkelerini Protez B… |
| protez-ayak-çeşitleri-hangi-tip-hangi-aktivit | Enerji depolayan | karbon-fiber-protez-ayak-nedir-enerji-depolay | …ik ayaklar farklı yürüme hızlarına uyum sağlıyor. **Enerji depolayan** karbon fiber ayaklar ise adım sırasında biriken g… |
| cpm-sürekli-pasif-hareket-cihazı-nedir-ne-zam | rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci | …ket ettirerek bu riski azaltmaya yardımcı oluyor, **rehabilitasyon** programının bir parçası olarak.… |
| cpm-sürekli-pasif-hareket-cihazı-nedir-ne-zam | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü | …erde cihaza bağlanıyor, süreç boyunca hekim ya da **fizyoterapist** takibi sürüyor ve hangi ameliyatta ne süreyle kul… |
| fantom-hayalet-uzuv-hissi-nedir | Günlük bakım | protez-bacak-ve-kol-bakimi | …**Günlük bakım** rutininin ayrıntılarını Protez Bacak ve Kol Bakım… |
| ortez-ve-protezler-hangi-malzemeden-yapılır-t | AFO | afo-nasıl-kullanılır-günlük-giyim-bakım-ve-de | …r malzeme. Soğuduğunda sertleşiyor. Sebebi basit: **AFO** ve KAFO'ların büyük bölümü tam da bu yüzden, yani… |
| aktif-vakum-sistemli-protez-nedir | liner | silikon-liner-nedir-ne-i̇şe-yarar | …Soketle **liner** arasındaki havayı boşaltıp negatif basınç oluştur… |
| aktif-vakum-sistemli-protez-nedir | Pasif Vakum | pasif-vakum-sistemli-protez-bacak-nedir | …etleşir. Pasif sistemle farkını merak ediyorsanız **Pasif Vakum** Sistemli Protez Bacak yazımıza, genel süreci mera… |
| kozmetik-silikon-parmak-protezi-nedir | parmak protezi | kısmi-el-ve-parmak-protezleri-fonksiyonel-çöz | …Kozmetik/silikon **parmak protezi** tam bunu konuşur.… |
| çocuk-protezleri-büyüme-ve-uyum | merdivenin | protezle-merdiven-rampa-ve-denge | …rklı bir doğallıkla kabul eder, oyunun, koşmanın, **merdivenin** bir parçası olarak — teknik ekip de ayarları tam … |
| kalça-dezartikülasyonu-özel-bir-amputasyon-se | soket tipini | protez-soket-türleri-vakum-mu-pin-kilit-mi | …vise oturmak zorundadır. Bu fark, size önerilecek **soket tipini** baştan belirler.… |
| kalça-dezartikülasyonu-özel-bir-amputasyon-se | Omuz Dezartikülasyonu | omuz-dezartikülasyonu-protezi-nedir-kimler-i- | …Üst ekstremitedeki benzer niş seviyeyi **Omuz Dezartikülasyonu** Protezi yazımızda, genel bakım ilkelerini Protez … |
| kalça-dezartikülasyonu-özel-bir-amputasyon-se | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü | … üçü birlikte, teknik sorumlu, hekim ve gerekirse **fizyoterapist** tarafından değerlendirilir.… |
| miyoelektrik-biyonik-el-nasıl-çalışır | kol ampütasyonunda | kol-ampütasyonu-sonrası-protez-sürecine-nasıl | …Myoelektrik el her **kol ampütasyonunda** otomatik seçim olmaz. Kalan kas dokusunun durumun… |
| miyoelektrik-biyonik-el-nasıl-çalışır | fizyoterapiyle | fizyoterapinin-protez-sürecindeki-rolü | …üçlüyse kontrol çabuk oturur. Sinyal zayıfsa önce **fizyoterapiyle** o kas güçlendirilir. Bazı kullanıcı 2-3 hafta içi… |
| protez-ayakta-taban-zemin-uyumu-farklı-yüzeyl | koşu bıçağı | koşu-bıçağı-ile-günlük-protez-ayağı-arasındak | … standart taban yeterli tutuşu vermeyebilir. Bazı **koşu bıçağı** sistemlerinde burada devreye giren çözüm değiştir… |
| protez-ayakta-taban-zemin-uyumu-farklı-yüzeyl | Rampa | protezle-merdiven-rampa-ve-denge | …**Rampa**, yokuş ya da hafif eğimli yüzeyde adım mekaniği d… |
| sgk-protez-ve-ortez-bedelini-karşılıyor-mu-ba | rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci | …lık kurulundan çıkıyor. Ortopedi, fizik tedavi ve **rehabilitasyon** gibi birden fazla uzman hastayı birlikte değerlen… |
| diz-ustu-protezler | liner | silikon-liner-nedir-ne-i̇şe-yarar | …Soket ve **liner**: Protezin bacağa uyumunu ve vücut ile güvenli bağ… |
| diz-ustu-protezler | mikroişlemcili diz | mikroişlemcili-diz-nedir-nasıl-çalışır | …Gelişmiş **mikroişlemcili diz** sistemleri, sensör ve elektronik kontrol teknoloj… |
| diz-ustu-protezler | aktivite seviyesi | protez-ayak-seçiminde-k-aktivite-seviyesi-ned | …Diz eklemi seçimi yapılırken kullanıcının **aktivite seviyesi**, yürüme alışkanlıkları, günlük yaşam koşulları ve… |
| bacak-ampütasyonu-sonrası-protez-sürecine-nas | Günlük yaşamınızda | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | …zaman konuşabileceğinizi hastane ekibinize sorun. **Günlük yaşamınızda** neyin değişebileceğini düşünmeye başlayın.… |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çöz | miyoelektrik | miyoelektrik-biyonik-el-nasıl-çalışır | …hareketinden gelen güçle parmağı hareket ettirir, **miyoelektrik** seçeneklerde kas sinyali parmağı tetikler.… |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çöz | Kozmetik protezlerin | kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | …Hareketli parçalar düzenli kontrol ister. **Kozmetik protezlerin** bakımı daha basittir, ama zamanla rengi ya da dok… |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çöz | Kozmetik parmak | kozmetik-silikon-parmak-protezi-nedir | …**Kozmetik parmak** protezi görünümü ve psikolojik rahatlığı önceler,… |
| protez-kılavuzu-okuma-servis-ve-garanti | günlük bakım | protez-bacak-ve-kol-bakimi | …l olarak dikkat edilmesi iyi olan 4 başlık şöyle: **günlük bakım** ve temizlik talimatları, kullanım sınırları (örne… |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-gün | Mikroişlemcili dizlerin | mikroişlemcili-diz-nedir-nasıl-çalışır | …**Mikroişlemcili dizlerin** çoğu gece boyunca şarja takılacak şekilde tasarla… |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-gün | mekanik diz | mikroişlemcili-diz-ile-mekanik-diz-arasındaki | …ik protezler sayfamızda ve mikroişlemcili diz ile **mekanik diz** farkı yazımızda bulabilirsiniz.… |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-gün | Suya dayanıklılık | protez-ayaklar-suya-dayanıklı-mı | …**Suya dayanıklılık** modelden modele büyük fark gösteriyor. Garanti yo… |
| kol-ampütasyonu-sonrası-protez-sürecine-nasıl | Günlük yaşamınızda | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | …İlk görüşme bir reçete anı değil. **Günlük yaşamınızda** kolunuzu nasıl kullandığınızı, beklentilerinizi, … |
| diz-alti-protezi-nedir | soket tipi | protez-soket-türleri-vakum-mu-pin-kilit-mi | …Tek doğru kurulum yok. Hangi **soket tipi**, hangi ayak bileşeni uygun — bunu teknik sorumlu,… |
| diz-alti-protezi-nedir | Protez Türleri | protez-çeşitleri-bacak-ve-kol-protez-türlerin | …bu görevi üstleniyor — bu sistemlere Bacak ve Kol **Protez Türleri** yazımızda değindik.… |
| protez-ayaklar-suya-dayanıklı-mı | kompozit | protez-ayak-malzemeleri-karbon-fiber-ve-kompo | …Cam elyaf **kompozit** gibi malzemeler suyla doğrudan temasta bozulmaz. … |
| protez-ayaklar-suya-dayanıklı-mı | koşu bıçağı | koşu-bıçağı-ile-günlük-protez-ayağı-arasındak | …Kısa cevap: bazı protez ayak ve **koşu bıçağı** sistemleri suya dayanıklı tasarlanır. Uzun cevabı… |
| protez-ayaklar-suya-dayanıklı-mı | Protez Bakımı | protez-bacak-ve-kol-bakimi | …ı yazımızda, mevsimsel bakım farklarını Mevsimsel **Protez Bakımı** yazımızda bulabilirsiniz.… |
| protez-ile-spor-ve-fiziksel-aktivite | liner | silikon-liner-nedir-ne-i̇şe-yarar | …nı şekilde yük taşımaz. Ayak tipi, soket uyumu ve **liner** seçimi, hangi aktivitenin ne kadar rahat yapılabi… |
| protez-ile-spor-ve-fiziksel-aktivite | fizyoterapistiniz | fizyoterapinin-protez-sürecindeki-rolü | …uğunu teknik sorumlunuz, hekiminiz ve gerekiyorsa **fizyoterapistiniz** birlikte değerlendirir. Karar, kalan uzuv bölgeni… |
| protez-ile-spor-ve-fiziksel-aktivite | kalan uzuv | kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-der | …in farklı bir aktivite daha uygun olabilir. Yanıt **kalan uzuv** bölgesinin durumuna, protez bileşenine ve genel s… |
| kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | Miyoelektrik | miyoelektrik-biyonik-el-nasıl-çalışır | …**Miyoelektrik** (biyonik) protez, kas sinyalleriyle hareket eden … |
| kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | Günlük yaşam | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | …**Günlük yaşam** biçimi, beklenti ve hedefler merkezimizde birlikt… |
| üst-ekstremite-protezlerinde-miyoelektrik-değ | Miyoelektrik | miyoelektrik-biyonik-el-nasıl-çalışır | …**Miyoelektrik** protez için değerlendirme tek bir ölçüeye indiril… |
| üst-ekstremite-protezlerinde-miyoelektrik-değ | kozmetik protez | kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | …gun sinyali göstermiyorsa süreç orada kapanmıyor, **kozmetik protez** ya da body-powered seçenekler gündeme geliyor ve … |
| üst-ekstremite-protezlerinde-miyoelektrik-değ | Fizyoterapiyle | fizyoterapinin-protez-sürecindeki-rolü | … performansı düşürebiliyor. Süreç orada bitmiyor. **Fizyoterapiyle** sinyal kontrolü eğitimi devreye giriyor.… |
| protez-soket-türleri-vakum-mu-pin-kilit-mi | Liner | silikon-liner-nedir-ne-i̇şe-yarar | …Mantık basit: **Liner**'ın ucunda bir pin vardır, soketin tabanında da bu… |
| koşu-bıçağı-ile-günlük-protez-ayağı-arasındak | Protez Ayak Çeşitleri | protez-ayak-çeşitleri-hangi-tip-hangi-aktivit | …Genel ayak tiplerini **Protez Ayak Çeşitleri** yazımızda, sporla ilgili geniş kapsamlı öneriler … |
| mevsimsel-protez-bakımı-yaz-teri-ve-kış-şartl | Günlük bakım | protez-bacak-ve-kol-bakimi | …**Günlük bakım** rutininin tüm ayrıntılarını Protez Bacak ve Kol B… |
| mevsimsel-protez-bakımı-yaz-teri-ve-kış-şartl | liner | silikon-liner-nedir-ne-i̇şe-yarar | …Sıcak havada **liner** ile cilt arasındaki nem artar. Bu basit değişim b… |
| güdükte-yara-varken-protez-kullanılır-mı | Kalan uzuv | kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-der | …**Kalan uzuv** bölgesinin günlük kontrolü hakkında "Kalan Uzuv B… |
| protez-ayak-malzemeleri-karbon-fiber-ve-kompo | K Aktivite Seviyesi | protez-ayak-seçiminde-k-aktivite-seviyesi-ned | … seviyesi sınıflandırmasını Protez Ayak Seçiminde **K Aktivite Seviyesi** Nedir? yazımızda, genel bakım ilkelerini Protez B… |
| protez-bacak-ve-kol-bakimi | suya dayanıklılık | protez-ayaklar-suya-dayanıklı-mı | …rçaları suya karşı korumak önemlidir; cihazınızın **suya dayanıklılık** düzeyi modeline göre değişir ve yalnızca üreticin… |
| protez-bacak-ve-kol-bakimi | silikon liner | silikon-liner-nedir-ne-i̇şe-yarar | …ın bir parçası. Onu taşıyan cildiniz, cilde değen **silikon liner** ve hareketi sağlayan mekanik parçalar da aynı öze… |
| protez-bacak-ve-kol-bakimi | diyabet | diyabet-ve-ayak-sağlığı-protez-kullananda-dik | …His azalması ya da **diyabet** gibi durumlarda nelere dikkat edilmeli?… |
| protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | seyahatin | protez-kullananlar-i-çin-seyahat-rehberi | …Valize ne koyulacağını düşünmek **seyahatin** sıradan bir parçası. Protez kullanıcısının listes… |
| protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | liner | silikon-liner-nedir-ne-i̇şe-yarar | …, sonra birden ayakta bir sunum yapmak — soket ve **liner** için iki farklı yük demek. Yeni bir iş rutinine g… |
| protez-ayaklarla-dans-ve-hareket | fiziksel aktivite | protez-ile-spor-ve-fiziksel-aktivite | …Genel spor ve **fiziksel aktivite** sorularını Protez ile Spor ve Fiziksel Aktivite y… |
| mikroişlemcili-diz-nedir-nasıl-çalışır | Mekanik diz | mikroişlemcili-diz-ile-mekanik-diz-arasındaki | …**Mekanik diz** eklemleri sabit bir direnç mantığıyla çalışır: he… |
| dirsek-alti-biyonik-kol-protezi | Miyoelektrik | miyoelektrik-biyonik-el-nasıl-çalışır | …**Miyoelektrik** bir el, kas sinyaliyle çalışıyor — bunu önceki ya… |
| dirsek-alti-biyonik-kol-protezi | dirsek ekleminin | protez-kolun-dirsek-eklemi-nasıl-çalışır-meka | … — tıpta transradial olarak da geçiyor — önkolda, **dirsek ekleminin** altındaki bir seviyede uzuv kaybını tarif ediyor.… |
| dirsek-alti-biyonik-kol-protezi | Liner | silikon-liner-nedir-ne-i̇şe-yarar | …**Liner** burada özel bir rol oynuyor: cildi korurken elekt… |
| pasif-vakum-sistemli-protez-bacak-nedir | Aktif Vakum | aktif-vakum-sistemli-protez-nedir | …**Aktif Vakum** Sistemli Protez yazımızda anlattığımız gibi, akti… |
| ampütasyon-sonrası-rehabilitasyon-süreci | fizyoterapist | fizyoterapinin-protez-sürecindeki-rolü | …Hekim, **fizyoterapist**, merkezinizdeki teknik sorumlu — herkes farklı bi… |
| protez-ayak-seçiminde-k-aktivite-seviyesi-ned | Protez Ayak Çeşitleri | protez-ayak-çeşitleri-hangi-tip-hangi-aktivit | …e seviyesine göre hangi ayak tipinin önerildiğini **Protez Ayak Çeşitleri** yazımızda, genel bakım ilkelerini Protez Bacak ve… |
| protez-ayak-seçiminde-k-aktivite-seviyesi-ned | Rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci | …K seviyesi zamanla değişebilir. **Rehabilitasyon** ilerlediğinde ya da sağlık durumu değiştiğinde ye… |
| protez-ayak-seçiminde-k-aktivite-seviyesi-ned | geri ödeme | sgk-protez-ve-ortez-bedelini-karşılıyor-mu-ba | … adıyla da geçer, Amerika Birleşik Devletleri'nin **geri ödeme** sisteminden çıkıp dünyaya yayılmış bir ölçektir.… |
| ortez-nedir-protezden-farkı-ne-afo-ve-kafo-aç | AFO | afo-nasıl-kullanılır-günlük-giyim-bakım-ve-de | …**AFO**, ayak bileğini ve ayağı kapsayan bir ortez türü. … |
| ortez-nedir-protezden-farkı-ne-afo-ve-kafo-aç | günlük yaşamın | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | …i olabiliyor. Kalıcı bir nörolojik durumda ortez, **günlük yaşamın** sürekli bir parçası olabiliyor.… |
| protez-süreci-ne-kadar-sürer | Rehabilitasyon | ampütasyon-sonrası-rehabilitasyon-süreci | …**Rehabilitasyon**, protez teslim edildikten sonra başlayan alışma v… |
| protez-kullananlar-i-çin-seyahat-rehberi | Günlük Yaşam | protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | …Gündelik yaşamın geri kalanını Protez ile **Günlük Yaşam** yazımızda, cilt ve bakım rutininin tamamını Prote… |
| protez-kullananlar-i-çin-seyahat-rehberi | liner | silikon-liner-nedir-ne-i̇şe-yarar | … aksesuar sorunu günü bozabilir — bir bağcık, bir **liner**, bir yedek vida. Kabin bagajına küçük bir bakım k… |

## İlgili Yazılar blokları (175 link)

| Kaynak yazı | 1 | 2 | 3 |
|---|---|---|---|
| diyabet-ve-ayak-sağlığı-protez-kullananda-dik | protez-ile-günlük-yaşam-i-ş-seyahat-sosy | protez-kullananlar-i-çin-seyahat-rehberi | protez-ile-spor-ve-fiziksel-aktivite |
| el-ve-kol-ortezleri-ne-i-şe-yarar-kimler-i-çi | ortez-ve-protezler-hangi-malzemeden-yapı | cpm-sürekli-pasif-hareket-cihazı-nedir-n | fes-fonksiyonel-elektriksel-stimülasyon- |
| protez-bacağın-bileşenleri-nelerdir-soket-lin | protez-soket-türleri-vakum-mu-pin-kilit- | pasif-vakum-sistemli-protez-bacak-nedir | aktif-vakum-sistemli-protez-nedir |
| protezle-merdiven-rampa-ve-denge | diyabet-ve-ayak-sağlığı-protez-kullanand | uzuv-kaybı-farkındalık-ayı-toplumsal-far | protez-ile-günlük-yaşam-i-ş-seyahat-sosy |
| kalan-uzuv-bölgesi-bakımı-günlük-kontrolü-der | protez-bacak-ve-kol-bakimi | mevsimsel-protez-bakımı-yaz-teri-ve-kış- | protez-kılavuzu-okuma-servis-ve-garanti |
| protez-çeşitleri-bacak-ve-kol-protez-türlerin |  |
| mikroişlemcili-diz-ile-mekanik-diz-arasındaki | mikroişlemcili-dizin-pil-şarj-yönetimi-v | protez-bacak-ve-protez-ayak-seçerken-han | diz-alti-protezi-nedir |
| uzuv-kaybı-farkındalık-ayı-toplumsal-farkında | protez-ile-günlük-yaşam-i-ş-seyahat-sosy | protez-kullananlar-i-çin-seyahat-rehberi | protez-ile-spor-ve-fiziksel-aktivite |
| protez-bacak-ve-protez-ayak-seçerken-hangi-fa | diz-alti-protezi-nedir | diz-ustu-protezler | kalça-dezartikülasyonu-özel-bir-amputasy |
| omuz-dezartikülasyonu-protezi-nedir-kimler-i- | kısmi-el-ve-parmak-protezleri-fonksiyone | kozmetik-silikon-parmak-protezi-nedir | kol-protezi-günlük-yaşamda-nasıl-takılır |
| kol-protezi-günlük-yaşamda-nasıl-takılır-çıka | miyoelektrik-biyonik-el-nasıl-çalışır | üst-ekstremite-protezlerinde-miyoelektri | dirsek-alti-biyonik-kol-protezi |
| protez-ayaklarda-azami-kullanıcı-ağırlığı-sın | protez-ayak-kılıfı-kozmetik-kapak-ne-i-ş | protez-ayaklar-suya-dayanıklı-mı | protez-ayakta-taban-zemin-uyumu-farklı-y |
| protez-ayak-çeşitleri-hangi-tip-hangi-aktivit | protez-ayak-seçiminde-k-aktivite-seviyes | protez-ayak-malzemeleri-karbon-fiber-ve- | koşu-bıçağı-ile-günlük-protez-ayağı-aras |
| cpm-sürekli-pasif-hareket-cihazı-nedir-ne-zam | fes-fonksiyonel-elektriksel-stimülasyon- | afo-nasıl-kullanılır-günlük-giyim-bakım- | ortez-nedir-protezden-farkı-ne-afo-ve-ka |
| fantom-hayalet-uzuv-hissi-nedir | güdükte-yara-varken-protez-kullanılır-mı | sgk-protez-ve-ortez-bedelini-karşılıyor- | protez-ve-ortez-üretiminde-3d-tarama-ve- |
| afo-nasıl-kullanılır-günlük-giyim-bakım-ve-de | ortez-nedir-protezden-farkı-ne-afo-ve-ka | el-ve-kol-ortezleri-ne-i-şe-yarar-kimler | ortez-ve-protezler-hangi-malzemeden-yapı |
| ortez-ve-protezler-hangi-malzemeden-yapılır-t | cpm-sürekli-pasif-hareket-cihazı-nedir-n | fes-fonksiyonel-elektriksel-stimülasyon- | ortez-nedir-protezden-farkı-ne-afo-ve-ka |
| aktif-vakum-sistemli-protez-nedir | mikroişlemcili-diz-nedir-nasıl-çalışır | mikroişlemcili-diz-ile-mekanik-diz-arası | mikroişlemcili-dizin-pil-şarj-yönetimi-v |
| kozmetik-silikon-parmak-protezi-nedir | kol-protezi-günlük-yaşamda-nasıl-takılır | miyoelektrik-biyonik-el-nasıl-çalışır | üst-ekstremite-protezlerinde-miyoelektri |
| çocuk-protezleri-büyüme-ve-uyum | kol-ampütasyonu-sonrası-protez-sürecine- | bacak-ampütasyonu-sonrası-protez-sürecin | ampütasyon-sonrası-rehabilitasyon-süreci |
| kalça-dezartikülasyonu-özel-bir-amputasyon-se | protez-bacağın-bileşenleri-nelerdir-soke | silikon-liner-nedir-ne-i̇şe-yarar | pasif-vakum-sistemli-protez-bacak-nedir |
| miyoelektrik-biyonik-el-nasıl-çalışır | üst-ekstremite-protezlerinde-miyoelektri | dirsek-alti-biyonik-kol-protezi | protez-kolun-dirsek-eklemi-nasıl-çalışır |
| protez-ayakta-taban-zemin-uyumu-farklı-yüzeyl | protez-ayak-çeşitleri-hangi-tip-hangi-ak | protez-ayak-seçiminde-k-aktivite-seviyes | karbon-fiber-protez-ayak-nedir-enerji-de |
| sgk-protez-ve-ortez-bedelini-karşılıyor-mu-ba | protez-ve-ortez-üretiminde-3d-tarama-ve- | çocuk-protezleri-büyüme-ve-uyum | kol-ampütasyonu-sonrası-protez-sürecine- |
| i̇lk-protez-ne-beklemeli | protez-süreci-ne-kadar-sürer | protez-ve-psikolojik-uyum | fantom-hayalet-uzuv-hissi-nedir |
| diz-ustu-protezler | kalça-dezartikülasyonu-özel-bir-amputasy | protez-bacağın-bileşenleri-nelerdir-soke | protez-soket-türleri-vakum-mu-pin-kilit- |
| bacak-ampütasyonu-sonrası-protez-sürecine-nas | ampütasyon-sonrası-rehabilitasyon-süreci | fizyoterapinin-protez-sürecindeki-rolü | i̇lk-protez-ne-beklemeli |
| kısmi-el-ve-parmak-protezleri-fonksiyonel-çöz | kol-protezi-günlük-yaşamda-nasıl-takılır | üst-ekstremite-protezlerinde-miyoelektri | dirsek-alti-biyonik-kol-protezi |
| protez-kılavuzu-okuma-servis-ve-garanti | kalan-uzuv-bölgesi-bakımı-günlük-kontrol | mevsimsel-protez-bakımı-yaz-teri-ve-kış- |
| karbon-fiber-protez-ayak-nedir-enerji-depolay | protez-ayak-malzemeleri-karbon-fiber-ve- | koşu-bıçağı-ile-günlük-protez-ayağı-aras | protez-ayaklarda-azami-kullanıcı-ağırlığ |
| mikroişlemcili-dizin-pil-şarj-yönetimi-ve-gün | protez-bacak-ve-protez-ayak-seçerken-han | diz-alti-protezi-nedir | diz-ustu-protezler |
| kol-ampütasyonu-sonrası-protez-sürecine-nasıl | bacak-ampütasyonu-sonrası-protez-sürecin | ampütasyon-sonrası-rehabilitasyon-süreci | fizyoterapinin-protez-sürecindeki-rolü |
| diz-alti-protezi-nedir | diz-ustu-protezler | kalça-dezartikülasyonu-özel-bir-amputasy | protez-bacağın-bileşenleri-nelerdir-soke |
| protez-ayaklar-suya-dayanıklı-mı | protez-ayakta-taban-zemin-uyumu-farklı-y | protez-ayak-çeşitleri-hangi-tip-hangi-ak | protez-ayak-seçiminde-k-aktivite-seviyes |
| protez-ayak-kılıfı-kozmetik-kapak-ne-i-şe-yar | protez-ayaklar-suya-dayanıklı-mı | protez-ayakta-taban-zemin-uyumu-farklı-y | protez-ayak-çeşitleri-hangi-tip-hangi-ak |
| protez-ile-spor-ve-fiziksel-aktivite | protez-ayaklarla-dans-ve-hareket | protezle-merdiven-rampa-ve-denge | diyabet-ve-ayak-sağlığı-protez-kullanand |
| kozmetik-estetik-kol-ve-el-protezi-nedir-kiml | kısmi-el-ve-parmak-protezleri-fonksiyone | kozmetik-silikon-parmak-protezi-nedir | kol-protezi-günlük-yaşamda-nasıl-takılır |
| fizyoterapinin-protez-sürecindeki-rolü | i̇lk-protez-ne-beklemeli | protez-süreci-ne-kadar-sürer | protez-ve-psikolojik-uyum |
| üst-ekstremite-protezlerinde-miyoelektrik-değ | dirsek-alti-biyonik-kol-protezi | protez-kolun-dirsek-eklemi-nasıl-çalışır | omuz-dezartikülasyonu-protezi-nedir-kiml |
| protez-soket-türleri-vakum-mu-pin-kilit-mi | pasif-vakum-sistemli-protez-bacak-nedir | aktif-vakum-sistemli-protez-nedir | mikroişlemcili-diz-nedir-nasıl-çalışır |
| protez-ve-ortez-üretiminde-3d-tarama-ve-dijit | çocuk-protezleri-büyüme-ve-uyum | kol-ampütasyonu-sonrası-protez-sürecine- | bacak-ampütasyonu-sonrası-protez-sürecin |
| koşu-bıçağı-ile-günlük-protez-ayağı-arasındak | protez-ayaklarda-azami-kullanıcı-ağırlığ | protez-ayak-kılıfı-kozmetik-kapak-ne-i-ş | protez-ayaklar-suya-dayanıklı-mı |
| mevsimsel-protez-bakımı-yaz-teri-ve-kış-şartl | protez-kılavuzu-okuma-servis-ve-garanti | kalan-uzuv-bölgesi-bakımı-günlük-kontrol |
| protez-kolun-dirsek-eklemi-nasıl-çalışır-meka | omuz-dezartikülasyonu-protezi-nedir-kiml | kozmetik-estetik-kol-ve-el-protezi-nedir | kısmi-el-ve-parmak-protezleri-fonksiyone |
| fes-fonksiyonel-elektriksel-stimülasyon-nedir | afo-nasıl-kullanılır-günlük-giyim-bakım- | ortez-nedir-protezden-farkı-ne-afo-ve-ka | el-ve-kol-ortezleri-ne-i-şe-yarar-kimler |
| güdükte-yara-varken-protez-kullanılır-mı | sgk-protez-ve-ortez-bedelini-karşılıyor- | protez-ve-ortez-üretiminde-3d-tarama-ve- | çocuk-protezleri-büyüme-ve-uyum |
| protez-ayak-malzemeleri-karbon-fiber-ve-kompo | koşu-bıçağı-ile-günlük-protez-ayağı-aras | protez-ayaklarda-azami-kullanıcı-ağırlığ | protez-ayak-kılıfı-kozmetik-kapak-ne-i-ş |
| protez-bacak-ve-kol-bakimi | mevsimsel-protez-bakımı-yaz-teri-ve-kış- | protez-kılavuzu-okuma-servis-ve-garanti | kalan-uzuv-bölgesi-bakımı-günlük-kontrol |
| protez-ile-günlük-yaşam-i-ş-seyahat-sosyal-ha | protez-ile-spor-ve-fiziksel-aktivite | protez-ayaklarla-dans-ve-hareket | protezle-merdiven-rampa-ve-denge |
| silikon-liner-nedir-ne-i̇şe-yarar | pasif-vakum-sistemli-protez-bacak-nedir | aktif-vakum-sistemli-protez-nedir | mikroişlemcili-diz-nedir-nasıl-çalışır |
| protez-ayaklarla-dans-ve-hareket | protezle-merdiven-rampa-ve-denge | diyabet-ve-ayak-sağlığı-protez-kullanand | uzuv-kaybı-farkındalık-ayı-toplumsal-far |
| mikroişlemcili-diz-nedir-nasıl-çalışır | mikroişlemcili-dizin-pil-şarj-yönetimi-v | protez-bacak-ve-protez-ayak-seçerken-han | diz-alti-protezi-nedir |
| protez-ve-psikolojik-uyum | fantom-hayalet-uzuv-hissi-nedir | güdükte-yara-varken-protez-kullanılır-mı | sgk-protez-ve-ortez-bedelini-karşılıyor- |
| dirsek-alti-biyonik-kol-protezi | omuz-dezartikülasyonu-protezi-nedir-kiml | kozmetik-estetik-kol-ve-el-protezi-nedir | kısmi-el-ve-parmak-protezleri-fonksiyone |
| pasif-vakum-sistemli-protez-bacak-nedir | mikroişlemcili-diz-nedir-nasıl-çalışır | mikroişlemcili-diz-ile-mekanik-diz-arası | mikroişlemcili-dizin-pil-şarj-yönetimi-v |
| ampütasyon-sonrası-rehabilitasyon-süreci | i̇lk-protez-ne-beklemeli | protez-süreci-ne-kadar-sürer | protez-ve-psikolojik-uyum |
| protez-ayak-seçiminde-k-aktivite-seviyesi-ned | karbon-fiber-protez-ayak-nedir-enerji-de | protez-ayak-malzemeleri-karbon-fiber-ve- | koşu-bıçağı-ile-günlük-protez-ayağı-aras |
| ortez-nedir-protezden-farkı-ne-afo-ve-kafo-aç | el-ve-kol-ortezleri-ne-i-şe-yarar-kimler | ortez-ve-protezler-hangi-malzemeden-yapı | cpm-sürekli-pasif-hareket-cihazı-nedir-n |
| protez-süreci-ne-kadar-sürer | protez-ve-psikolojik-uyum | fantom-hayalet-uzuv-hissi-nedir | güdükte-yara-varken-protez-kullanılır-mı |
| protez-kullananlar-i-çin-seyahat-rehberi | protez-ile-spor-ve-fiziksel-aktivite | protez-ayaklarla-dans-ve-hareket | protezle-merdiven-rampa-ve-denge |
