# Fox — İnsan Sesi Korpusu (Türkçe Prosa Tabanı)
*Metin Yazarı'nın "AI yazmış" hissini aşma eğitimi. Ölçülmüş korpustan çıkarılmış örüntüler + kalibre eşikler.*

**Kuruluş:** 8 Ağustos 2026 · **Tetikleyici:** Özgür Irmak Protez müşteri geri bildirimi — *"yapay zekâya mı yazdırdın"* · **Ayhan emri:** "metin yazarını eğitelim… Türkiye'de bulunan önemli gazetecilerin makalelerini incelettirelim."

---

## 0 · NEDEN BU BELGE VAR

Özgür Protez için üretilen Hakkımızda metni (v0.5, 4 Ağu) tüm iç kapılardan geçmişti: Denetmen onayı, YMYL filtresi, KKK uyumu, `slop_tarama.py` **temiz**. Müşteri yine de "AI yazmış" dedi.

**Teşhis:** Kaçak kelimede değildi, **cümle mimarisindeydi.** `slop_tarama.py` kelime tarar ("elevate", "yeni nesil", "kusursuz deneyim") — bu metinde onlardan biri bile yoktu. Tell sözdizimindeydi ve hiçbir aracımız sözdizimine bakmıyordu.

> **Kural:** Bundan sonra "AI hissi" bir zevk tartışması değil, **ölçülen bir büyüklüktür.** Ölçen araç: `sablonlar/araclar/sozdizim_tarama.py`.

---

## 1 · YÖNTEM (ve sınırları — dürüstçe)

**Korpus:** 18 köşe yazısı · 12.568 kelime · 3 yazar
| Yazar | Kaynak | Yazı | Kelime |
|---|---|---|---|
| Zülal Kalkandelen | Cumhuriyet | 6 | 4.171 |
| Fatih Altaylı | fatihaltayli.com.tr | 6 | 5.803 |
| Yılmaz Özdil | Sözcü (istanbulgercegi arşivi) | 6 | 2.594 |

**Ölçülemeyenler — bayrak:**
- **Gazete Oksijen:** 10 yazar çekildi ama sitenin ücretli duvarı gövdeyi ~130 kelimede kesiyor; temizlik sonrası ölçüm eşiğinin (60 kelime) altında kaldı. **Korpusa girmedi.** Oksijen'in editoryal register'ı bizim hedefimize (Ayhan'ın estetiği) muhtemelen en yakın olanı — abonelikle ya da baskı PDF'iyle ikinci turda eklenmeli.
- **Cüneyt Özdemir:** düzenli köşe yazısı yerine video/yayın ağırlıklı çalışıyor; yazılı korpus toplanamadı.

**Tür farkı uyarısı (kritik):** Korpus **gazete köşe yazısıdır.** Bizim ürettiğimiz marka/kurum metni ayrı bir türdür — daha sessiz, daha az birinci şahıs, daha az polemik. Bu yüzden korpus **taklit edilecek bir üslup değil, "insan Türkçesi tabanı"dır.** Eşikler bu payla çekildi (bkz. §4).

**Kanıt statüsü (İki Katman Kanıt — Tip A/B):** Aşağıdaki sayılar **Tip A**'dır (gerçek metin, gerçek ölçüm, tekrarlanabilir komut). Eşikler **iç çalışma eşiğidir**, sektör benchmark'ı değil — rapora öyle yazılır.

**Tekrarlanabilirlik:**
```bash
python3 sablonlar/araclar/sozdizim_tarama.py raporlar/hedef-metin.md
```

---

## 2 · BULGU TABLOSU — insan yazarlar vs. bizim metinlerimiz

| Ölçü | Kalkandelen | Altaylı | Özdil | **İnsan medyanı** | Özgür Hakkımızda | Özgür blog |
|---|---|---|---|---|---|---|
| Karşıtlık ("X değil Y") /1000 kelime | 2,2 | 3,4 | 1,0 | **2,3** (maks 7,1) | **21,6** ❌ | 2,5 |
| Karşıtlık taşıyan cümle oranı | 0,035 | 0,046 | 0,021 | **0,042** (maks 0,10) | **0,318** ❌ | 0,03 |
| Somut çapa /100 kelime (sayı, özel ad, ölçü) | 13,1 | 8,8 | 8,4 | **11,2** | 24,8 | **2,2** ❌ |
| Cümle uzunluğu değişkenliği (CV) | 0,58 | 0,60 | 1,38 | **0,63** | 0,52 | 0,49 |
| En kısa – en uzun cümle (kelime) | 3–52 | 2–42 | 2–127 | **geniş** | 4–30 | 5–25 |
| Kısa cümle oranı (≤6 kelime) | 0,061 | 0,215 | 0,367 | **0,16** | 0,091 | 0,073 |
| Tek cümlelik paragraf oranı | 0,67 | 0,64 | 0,50 | **0,64** | 0,56 | **0,06** ❌ |
| İnsan işareti /1000 (1. şahıs + soru + alıntı) | 22 | 34 | 31 | **31** (min 16,9) | **6,2** ❌ | **8,7** ❌ |
| Noktalı virgül /100 kelime | 0,3 | 0,0 | 0,3 | **0,2** (maks 0,7) | **2,8** ❌ | **1,7** ❌ |
| Aforizmayla kapanan paragraf oranı | 0,065 | 0,082 | 0,000 | **0,033** | **0,214** ❌ | 0,10 |

**Üç numaralı bulgu (en sert):** Hakkımızda metninde karşıtlık yoğunluğu, korpustaki **en karşıtlık-yüklü insan yazısının 3 katı.** 324 kelimede 7 karşıtlık ekseni. Hiçbir insan yazar bu bölgeye girmiyor.

**Dört numaralı bulgu (en sinsi):** İki metinde de **konuşan bir özne yok.** Birinci şahıs sıfır, soru sıfır, alıntı sıfır. Üç gazetecinin hiçbirinde bu oran 16,9'un altına inmiyor. Metin kimsenin ağzından çıkmıyor — bu, okurun "makine yazmış" demesinin en doğrudan sebebi.

---

## 3 · İNSAN PROSASININ 9 ÖRÜNTÜSÜ (korpustan çıkarıldı — uygulanabilir)

*Örnekler bizim alanımızdan uydurulmuştur; gazetecilerin cümleleri alıntılanmaz (telif).*

**1. Somut açılış — tez değil sahne.**
Korpustaki 18 yazının hepsi adı konmuş bir aktör, olay, tarih ya da rakamla açılıyor. Hiçbiri soyut bir tezle başlamıyor.
- ✗ *"Protez, teslim edilen bir cihaz değil kişiye özel bir süreçtir."* (tez + karşıtlık)
- ✓ *"Geçen hafta bir hasta, protezini üç kere geri getirdi. Sorun soketin kendisinde değildi."*

**2. Karşıtlık bütçesi: 1000 kelimede en fazla 2.**
"X değil Y" güçlü bir figür — **bir kere** kullanıldığında. Üst üste kullanılınca metin bir düşünce değil bir tik üretir. İnsan medyanı 2,3/1000. **Bütçe: metin başına 1, uzun metinde 2.** Fazlası siliniyor, karşıtlık düz cümleye çevriliyor.

**3. Dinamik cümle aralığı — vuruş + taşıma.**
İnsan yazarlar 2 kelimelik cümleden 127 kelimeliğe kadar geziniyor. Bizim metinlerimiz 4–30 arasında sıkışık. Bir metin monotonsa fikir doğru olsa da makine gibi okunur.
**Kural:** her 150 kelimede en az bir **≤6 kelimelik** cümle. Kısa cümle oranı %5'in altına inmez.

**4. Konuşan özne — metnin bir ağzı olmalı.**
Birinci şahıs (biz/ben), gerçek bir soru, ya da alıntılanmış bir cümle. Marka metni polemik yazısı değil, ama **sıfır** olamaz.
- ✓ *"Bize en çok sorulan şey şu: 'Ne zaman yürüyebilirim?'"* — bir soru + bir alıntı + bir "biz", tek cümlede.

**5. Somut çapa yoğunluğu — 100 kelimede en az 5–6.**
Sayı, tarih, marka adı, ölçü, yer, kişi. Özgür blogunda 800 kelimede **sıfır rakam** vardı — bir bakım rehberinde. Soyutluk AI hissinin yakıtıdır.
**Kural:** somutluk kotası dolmuyorsa metni cilalama — **eksik olan bilgidir, üslup değil.** Müşteriden veri iste (§5).

**6. Aforizma kotası: metin başına 1.**
Paragrafı bilgece bir genellemeyle kapatmak iyi bir hamledir; her paragrafı öyle kapatmak imzadır. İnsan oranı %3,3; bizim Hakkımızda %21,4.

**7. Noktalı virgül neredeyse yok.**
Türkçe köşe yazısında ";" yoğunluğu 100 kelimede 0,2 (Altaylı'da tam sıfır). Bizde 2,8. Yoğun ";" kullanımı **İngilizceden çevrilmiş** izlenimi verir — ve LLM Türkçesinin en görünür parmak izlerinden biridir. Noktalı virgülü nokta yap, cümleyi böl.

**8. Tek cümlelik paragraf normaldir.**
İnsan yazarların paragraflarının ~%64'ü tek cümle. Özgür blogunda bu oran %6 — hepsi 3-4 cümlelik tek tip bloklar. Simetrik paragraflar sayfaya makine deseni verir.

**9. Kapanış düşer, özetlemez.**
İnsan yazarlar kısa, sert, çoğu zaman konuşma diline yakın bir satırla biter. Bizim metinlerimiz özetleyip bağlıyor ("Bu adımlar … daha rahat kılar"). Özet zaten metnin içindeydi; kapanışta tekrarı okuyucuya "otomatik üretim" hissi verir.

---

## 4 · KALİBRE EŞİKLER (`sozdizim_tarama.py`)

- **UYARI eşiği** = korpusun p90'ı (alt-yönlü ölçüde p10) — *insan aralığının kenarı.*
- **SERT eşiği** = korpusta **hiçbir yazarda görülmemiş** bölge (maksimum/minimum ötesi).

**Doğrulama:** eşikler 18 insan yazısına geri uygulandı → **16/18 SERT-temiz.** (Tek istisna: 358 kelimelik kısa bir Özdil yazısı, küçük örneklem gürültüsü.) Yani eşikler insan prosasını yanlışlıkla suçlamıyor.

`insan_isareti_bin` eşiği bilinçli olarak korpusun altına çekildi (uyarı 12,0 — korpus min 16,9): marka metni türü doğal olarak daha sessizdir.

**Kullanım kademesi:**
- **SERT bulgu → metin dışarı çıkmaz.** Yeniden yazılır.
- **UYARI bulgu → gerekçelendirilir.** Bilinçli tercihse Denetmen'e Hazırlık Notu'na yazılır.
- Tarama **Denetmen'in ve insan kulağının yerine geçmez** — ilk süzgeçtir. Sesli okuma testi kalkmadı.

---

## 5 · KÖK NEDEN: SOYUTLUK BİR ÜSLUP HATASI DEĞİL, BİR BRİF AÇIĞIDIR

Özgür Hakkımızda metninin somut çapası, bilinçli kararlarla **boşaltılmıştı**: şehir/adres yok (teyit gelmedi), kadro sayısı ve personel yok (Ayhan kilidi), ürün/marka adı yok (Çözümler sayfasına), üniversite beyanı yok, CAD/CAM teyit edilmedi. Geriye yalnızca 1998 kaldı.

Metin Yazarı bu boşluğu **üslupla doldurdu** — soyut tezler, karşıtlıklar, aforizmalar. AI hissinin asıl kaynağı budur.

> **YENİ KURAL (bağlayıcı):** Somutluk kotası (100 kelimede ≥5 çapa) dolmuyorsa metin **cilalanarak kapatılmaz.** Metin Yazarı durur ve **eksik olguların listesini** Fox'a bayrakla verir. Fox bunu Ayhan'a "müşteriden şu 5 bilgi lazım" olarak taşır. Boş bilgiyi güzel cümleyle örtmek, tam olarak müşterinin yakaladığı şeydir.

**Özgür Protez için şu an eksik olan somut malzeme (Ayhan → Özgür Bey):**
1. Merkezde yılda kaç kişiye uygulama yapılıyor (kaba aralık yeter)
2. Bir hastanın ilk görüşmeden ilk adıma kadar geçen tipik süre
3. Özgür Bey'in kendi ağzından bir cümle — neden bu işi yapıyor (alıntılanabilir)
4. Yayımlanabilir tek bir vaka: ne geldi, ne yapıldı, ne değişti (isimsiz olabilir)
5. Şehir/semt ve merkezin fiziksel tarifi (yayın kararı Ayhan'da)

---

## 6 · KALİBRASYON PROTOKOLÜ (yaşayan belge)

- Korpus büyüdükçe eşikler yeniden hesaplanır; **eşik değişimi bu belgeye tarih ve gerekçeyle yazılır.**
- Ayhan bir metni "AI gibi" diye reddederse: metin taranır, hangi ölçünün kaçırdığı bulunur, **ölçü seti genişletilir.** (Denetim zinciri açığı yakalayamadıysa mercek de güncellenir — yerleşik kural.)
- Ayhan bir metni onaylarsa: metin ölçülür, değerleri **hedef bandı** olarak buraya işlenir (onaylı iç korpus).
- **İkinci tur korpus hedefleri:** Gazete Oksijen (ücretli duvar aşılırsa — register olarak en yakın kaynak), edebi/deneme Türkçesi (dergi denemesi), ve marka türünde gerçek insan yazımı kurumsal metinler.
- Korpus ham metinleri **repoya girmez** (telif); yalnız ölçüm ve örüntü saklanır.

---

*v1 · 8 Ağustos 2026 · Fox · Kaynak vaka: Özgür Irmak Protez "AI mı yazdı" geri bildirimi. Bağlı: `sablonlar/araclar/sozdizim_tarama.py` (ölçüm), `.claude/agents/metin-yazari.md` §İnsan Sesi Kapısı (uygulama), `fox-ses-parmak-izi.md` §Negatif Parmak İzi 8 (Ayhan markası), `.claude/agents/denetmen.md` (denetim merceği).*
