# KAYNAK — Yürüme Analizi & Kişiye Özel Tabanlık Sistemi Teknik Şartnamesi
*Ayhan tarafından 13 Ağustos 2026'da verildi. Ham teknik şartname (tedarikçi firma dili, B2B/ihale metni). Son kullanıcı metninin OLGU KAYNAĞI — buradaki hiçbir cümle olduğu gibi web'e geçmez.*

> ⚠️ **DOĞRULAMA BAYRAĞI:** Bu belge bir tedarikçi ihale şartnamesi (metinde "Kazakistan Sağlık Bakanlığı" kurulumu geçiyor). Merkezde **birebir bu cihazların** (Zebris/Contemplas + Amfit) bulunduğu Ayhan/Özgür Bey teyidi olmadan marka adı yazılmaz. Marka adı kullanımı ayrıca **avukat sorusu #1**'e bağlı (bkz. `marka-bulutu-os-medikal-protez-bagi.md` A.4).

---

## 1. Kişiye özel tabanlık — tanım
- Yürüme analizi + statik ve dinamik ölçüm sonrası, ayağın anatomik yapısına göre üretilen tabanlık.
- Amaç: ayağa binen basıncı azaltmak, eklem stabilitesini artırmak, deformasyonun ilerlemesini yavaşlatmak.
- **Sertlik derecesi kişiye göre planlanır.** Belirleyiciler: diyabet varlığı, ayak altında basınç yarası, kilo, spor aktivitesi.

## 2. Dinamik ölçüm — yürüme analizi (Zebris / Contemplas)
- Kişi sensörlü yürüme bandında yürütülür; yürüyüşün **kinetik** (kuvvet, basınç, moment) ve **kinematik** (yer değiştirme, hız, ivme, açısal büyüklükler) incelemesi yapılır.
- Banda entegre kuvvet platformu (force plate) + **11.260 kapasitif sensör**.
- Ölçülenler: statik kütle merkezi (duruş), sağ/sol topuk–ön ayak koordinasyonu, stance ve swing fazlarının ayrıştırılması, ayak tabanında hangi noktaya ne kadar basınç geldiği.
- Sonuçlar 3 boyutlu grafiğe dönüşür; **tüm yürüme parametreleri ~10 saniyede raporlanır**, çıktı alınabilir, Excel'e aktarılıp arşivlenebilir.
- **Karşılaştırma özelliği:** aynı kişinin farklı zamanlardaki ölçümleri yan yana konur (ör. operasyon öncesi–sonrası, botoks öncesi–sonrası, normal yürüyüş).
- Sistem içeriği: sensörlü koşu bandı platformu + Contemplas yazılım + bilgisayar + yazıcı.

## 3. Statik ölçüm — 3D pimli sayısallaştırıcı (Amfit digitizer)
- Hasta platformda ayakta veya oturur haldeyken, ayak tabanındaki **algılayıcı pimler** ayağın kalıbını 3 boyutlu olarak ekrana çıkarır. Ayak boyu da ölçülür.
- Ayak bileği **nötral (uygun anatomik) pozisyonda** ölçülür; arka taraftan çıkan **lazer aşil tendonunu ortalar** (ağırlık merkezi orta hattı).
- 4 adımlı akış (kumandayla): pimler yükselir → kişinin ağırlığına göre pim basıncı ayarlanır ve ölçüm sabitlenir → 3D görüntü ekrana aktarılır → pimler iner, diğer ayağa geçilir.
- **Tarama süresi maksimum 10 saniye.**
- Kemik ve yumuşak dokuya karşı farklı hassasiyet (2 boyutlu tarayıcılardan farkı budur).
- Ölçüm aralığı: **Avrupa 37–50 numara** (bay/bayan).

## 4. Tasarım (dijital modifikasyon)
Ekrandaki 3D model üzerinde yapılabilenler: ark yükseltme, metatarsal ped, kısalık ekleme, iç/dış kama, supinasyon–pronasyon ayarı, topuk kavrayıcı. Ayrıca taban yüksekliği, açı, kalınlık, topuk yüksekliği, ayak boyu/genişliği, malzeme kalınlığı modifiye edilebilir. Aşırı deformasyonda düzeltme yapılarak **nötral ayak kalıbı** elde edilir.

## 5. Malzeme — evazote takoz
- Sıkıştırılmış EVA. Sertlik/yoğunluk: **Shore A 21–60 durometre.**
- **5 farklı dansite:**
  1. Düşük (soft)
  2. Orta (şok absorbe)
  3. Yüksek (sert/rijit)
  4. At nalı (epinli)
  5. Yarı sert–yarı orta (topuk no:3, ön ayak no:2)
- Şartnamedeki örnek eşleştirmeler (⚠️ **web'e kondisyon→ürün tablosu olarak KONMAZ** — öz-tanı daveti + endikasyon riski): diyabetik ayak/metatarsalji/nasır → no:1 · pes planus, pes cavus, plantar fasiit → no:2 · pes plano valgus → no:3 · epin kalkanei → no:4 · metatarsalji ve sporcular → no:5.
- Kalıp aralığı: bay geniş 37–50, bayan dar 37–40.

## 6. Üretim — CAD/CAM freze (Amfit Mill)
- Digitizer + analiz verileri ağ/taşıyıcı ile freze makinesine aktarılır; son dakika değişikliği yapılabilir.
- Uygun dansite ve boydaki evazote takoz makineye yerleştirilir; **ayak başına ~6–9 dk** (şartnamenin B bölümünde ayak başına 7–10 dk, çift başına 14–20 dk).
- 3 eksenli hassas taşıyıcı bıçak. Entegre toz toplama haznesi.
- Üretim sonrası tabanlık ayakkabıya göre frezelenir; üzeri plastazote vb. ile kaplanabilir.
- Bitmiş ürün boy aralığı: ABD 3–17 / Avrupa 37–50.

## 7. Kullanım ömrü ve yenileme
- Evazote tabanlığın ortalama kullanım süresi **3–6 ay**; sonrasında malzeme şok absorbsiyon özelliğini yitirdiğinden yenilenmesi önerilir.
- Yenilemede tekrar analiz yapılır, önceki tabanlıkla elde edilen değişim karşılaştırılır.
- Ömrü etkileyen faktörler: spor aktivitesi (kros, basketbol, voleybol vb.), kilo, kullanım sıklığı, kişide birden fazla çift bulunup bulunmadığı (spor ayakkabı ile klasik/günlük kullanım için ayrı tabanlık tasarlanabilir).

## 8. Metne GİRMEYECEK bölümler (B2B/tedarik alanı)
Garanti koşulları, montaj-kurulum-eğitim hizmeti, voltaj/güç değerleri, cihaz ağırlıkları, bilgisayar model adları (Dell Optiplex 745, 26" monitör, HP yazıcı, Windows XP), USB bağlantısı, "1000 çift takoz makineyle verilecek", "sadece bizim takoz materyallerimiz kullanılabilir" maddesi. Bunlar satın alan kuruma aittir, hastaya değil.
