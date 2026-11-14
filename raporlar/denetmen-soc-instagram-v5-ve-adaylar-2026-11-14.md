# DENETMEN RAPORU (Orkestratör Sentezi) — 2. tur

**Tarih:** 14 Kasım 2026, Cumartesi
**Denetlenen:** Fox — SoC Instagram planı v5 (A) · madde 11 kaydırmalı taslağı, 6 kare (B) · Higgsfield adayları: 4 durağan + 3 UGC kare + 5 UGC video (C) · Metin Yazarı metinler v01 (D) · Astrid sahne seti (E)
**Mercekler:** Verification · Red Team · Devil's Advocate (tek elden yürütüldü, ayrı alt ajan çağrılmadı) + Tutarlılık / Değer Uyumu / Kalite Tabanı / Atlanmış Soru / İnsan Sesi / Erişilebilirlik (uygulanmaz: hiçbir şey yayınlanmadı)
**Kapsam:** Ayhan'ın 14 Kas kararları (Higgsfield, spor çizgisi, geniş açı lifestyle, UGC dilinde üretim, Belgesel Stills izni) verili alındı, tartışılmadı. Hiçbir dosya değiştirilmedi, hiçbir şey yayınlanmadı, kredi harcanmadı. `Yapay Zeka Görselleri` klasörü yalnız okundu; videolardan scratch dizinine küçük kare tabloları çıkarıldı, başka hiçbir araca girdi verilmedi.

## KARAR: DİKKAT — B ve C'nin UGC kısmı bu haliyle yayın için DUR

Uydurma tarih ya da rakam bulmadım; madde 11'deki olguların hepsi birincil kaynakla tutuyor. Sorun üç yerde: (1) YZ "UGC" adayları planın kendi dürüstlük kuralını ve "yüz yok" kuralını çiğniyor, (2) madde 11'de gerçek sporcular tanınabilir ve karelerde dört ayrı üçüncü taraf işareti var, (3) plan v5 ile bugün fiilen üretilenler birbirinden kopmuş.

---

## DOĞRULANANLAR (bulgu değil, kayıt)

| Olgu (kare) | Kaynak (bugün açıldı) | Sonuç |
|---|---|---|
| 13 Aralık 2006, BM Genel Kurulu kabul (2) | treaties.un.org IV-15: "New York, 13 December 2006", A/RES/61/106 | Tutuyor |
| 3 Mayıs 2008 yürürlük (2) | aynı sayfa: "3 May 2008, in accordance with article 45(1)" | Tutuyor |
| 194 taraf (3) | aynı sayfa: "Signatories : 164. Parties : 194" | Tutuyor (14 Kas okuması; taraflardan biri AB, "194 devlet" denmemeli — kare "taraf" diyor, doğru) |
| Türkiye 30 Mar 2007 imza, 28 Eyl 2009 onay (3) | aynı sayfa, Türkiye satırı | Tutuyor |
| "13 Aralık'ta 20 yaşında" (1) | kabul tarihinden 20 yıl | Doğru (yürürlükten değil kabulden sayılıyor; kare 2 bunu açıklıyor) |
| "Making Humanity Together", 2026 (6) | un.org/en/observances/human-rights-day: "2026 Theme – Making Humanity Together" | Tutuyor |
| Madde 30 başlığı ve 5. fıkra (4, 5) | aile.gov.tr resmî Türkçe metin (başlık: "Kültürel Yaşama, Dinlenme, Boş Zaman Aktiviteleri ve Spor Faaliyetlerine Katılım"); ohchr.org 403 verdi, İngilizce metin hafızadan karşılaştırıldı | Özet içerikçe sadık; iki nüans bulgu 6'da |
| Sözleşme'nin resmî Türkçe adı | aile.gov.tr + Resmî Gazete 14.07.2009/27288 (5825 sayılı Kanun) | **"Engellilerin Haklarına İlişkin Sözleşme"** — metinler v01'deki bayrak kapanabilir |
| Türkçe glyph | altı PNG gözle bakıldı | İ (İçinde, İnsan), ı (YIL, ARALIK, yazıyor), ş, ü, ğ, î (resmî) doğru. Marka fontları yüklü (Bebas Neue + Comfortaa) |
| 3 Aralık 2026 teması (metinler, madde 07 kare 6) | idpwd.gov.au (Avustralya hükümeti) "The CRPD at 20: Building on Progress, Advancing the Future" diyor; BM'nin kendi sayfasında **görmedim** | Hâlâ ikincil. Bayrak yerinde kalmalı |

Plan sayımları: kaynak dengesi (6+1 / 8 / 2 / 3 = 20), format (6 / 6 / 6 / 1 / 1), çekirdek 14 + isteğe bağlı 6 — üçü de tablodan yeniden sayıldı, tutuyor. Beş özel gün karşılanıyor (04, 07+08, 11, 13 şartlı, 18).

---

## BULGULAR

### Bloklayan

**1. (C) YZ "UGC" kareleri ve videoları gerçek kullanıcı izlenimi veriyor; plan kendi kuralıyla çelişiyor.** *Red Team + Değer Uyumu*
Kanıt: (a) `tur-4-prompt-ugc-*.txt` ilk satırı: "It is a real, casual photo taken on a current iPhone by a friend or by the person themself and posted to Instagram as is." Amaç metni gerçek kullanıcı paylaşımını taklit etmek. (b) Plan §2 karar 4: "Oyuncuya kullanıcı gibi davrandırmak plan dışı"; §2.1: "UGC dilindeki kareler gerçek kullanıcı içeriği gibi sunulmaz." Var olmayan bir insana kullanıcı gibi davrandırmak aynı şeyin YZ hali. (c) `ugc-ayna-soyunma-odasi.png`: ayna selfie'si, üç mercekli telefon, yüzün yarısı görünür — kareyi gören "bu kadın çorabı aldı ve paylaştı" okur. (d) K8 (YZ etiketi) hâlâ açık karar; etiket caption'ın altında kalır, kare ekran görüntüsüyle dolaşır.
İşaret (hüküm değil, avukata): Türkiye'de reklam mevzuatında tanıklık içeren reklam ve örtülü reklam hükümleri (6502 sayılı Kanun md. 61, Ticari Reklam ve Haksız Ticari Uygulamalar Yönetmeliği) ve Reklam Kurulu'nun sosyal medya kılavuzu bu tür içeriğe dokunabilir. Meta gerçekçi YZ video için etiket istiyor.
Düzeltme: ayna selfie'si elenir (en yüksek aldatma riski). Kalan geniş açı kareler "UGC" adıyla değil "marka çekimi, YZ ile üretildi" diye adlandırılır; plan ve dosya adlarından "UGC" çıkar. K8 "öneri" olmaktan çıkıp ön koşul olur: etiket + caption'da bir satır. Prompt'tan "posted to Instagram as is by the person" cümlesi çıkar. Madde 17 (gerçek davetli içerik) ile aynı ay içinde yan yana durmaları ayrıca sorun: gerçek kullanıcı içeriği geldiğinde kimse inanmaz.

**2. (C/A) Plan "yüz yok" diyor; yedi adayın beşinde okunur yüz var.** *Tutarlılık + Red Team*
Kanıt: Plan §2.1: "Yüz yok. Üretilen karelerde yalnız diz altı, el, eşya." K1: "yüzsüz bir figür (diz altı, eller)". Adaylar: `ugc-tribun-kosu-sonrasi.png` kameraya dönük olmasa da tam yüz, kahkaha; `ugc-korttan-cikis.png` tam profil; `ugc-video-kort-servis-hazirligi.mp4` 6 saniye boyunca yüz; `ugc-video-pist-esneme.mp4` ikinci yarıda yüz. Astrid'in kendi kuralı (§Yön 13: "Kameraya bakan, gülümseyen figür yok") da tribün karesinde çiğnenmiş. Fotogerçekçi YZ yüzün gerçek bir kişiye benzeme riski ölçülmedi, ölçülemez; benzeyen biri çıkarsa "yüzüm reklamda" şikâyeti markaya gelir.
Düzeltme: ya plan dürüstçe güncellenir ("tam boy figürde yüz arkadan/profilden, küçük; kahkaha ve okunur yüz yok") ve tribün + servis videosu buna göre elenir/yeniden kadrajlanır, ya da Ayhan okunur YZ yüzü bilerek kabul eder. Bu bir Ayhan kararı ve K listesinde yok.

**3. (B) Madde 11'deki sporcular "yüz yok" olsa da tanınabilir; marka hesabı kullanımı için rıza teyidi yazılı değil.** *Red Team + Değer Uyumu*
Kanıt: kare 1 — bacakta dövme + bıçak protezde mavi pençe çıkartması; kare 3 — iki sporcu arkadan, biri çift taraflı koşu protezi kullanıyor, kulak ve saç okunur; kare 4 — tişört kolunda kulüp arması, yüzün bir kısmı. Türkiye'de protezli atletizm küçük bir çevre; bu üç kare o çevrede isimle okunur. Ayhan'ın "belgesel stills'i kullanabilirsin" izni filmin sahibi olarak kendi hakkını kapatır; sporcuların filme verdiği rızanın **çorap satan bir marka hesabını** kapsayıp kapsamadığı ayrı soru. Hafıza notu da "reşit olmayan kapısı yine uygulanır" diyor; karelerdeki kişilerin yaşı dosyada yazmıyor.
Ayhan'a tek cümle: *"Bu dört karedeki sporcular, görüntülerinin belgeselin dışında Steps On Clouds'un Instagram hesabında kullanılmasına da evet dedi mi, aralarında 18 yaşından küçük var mı?"* Cevap gelene kadar kare 1–4 yayınlanmaz.

**4. (B) Karelerde dört üçüncü taraf işareti var; biri rakip kategori.** *Red Team*
Kanıt: kare 1 sol üst — şortta üç bant + yazı (Adidas görünümlü); kare 2 — ayakkabı dilinde okunur "NIKE", yanında desenli **başka bir çorap markasının** logolu çorabı kareyi dolduruyor, protez bıçağında üretici yazısı ("FRE…"); kare 4 — ayakkabıda belirgin swoosh + aynı desenli çorap; kare 3 — bıçak tabanında sarı marka deseni (düşük).
Risk düzeyi: hukuki taraf **orta-düşük** (gerçek belgesel karesi, ürün satmıyor; ama marka hesabı ticari hesap — işaret avukata). Ticari/itibar tarafı **orta-yüksek**: çorap satan bir markanın hak günü gönderisinin ikinci karesinde başka bir çorap markası başrolde; ve bu markalar kendi hesaplarından "hak gününde logomuzla ne yapıyorsunuz" diyebilir. Plan madde 11 kapısı yalnız "ayakkabıdaki marka işareti" diyor; şort, çorap ve protez üreticisi yazılmamış.
Düzeltme: kare 2 değişir (çorap + NIKE aynı karede, kırpmayla kurtulmaz). Kare 4 ayak bölgesi kadraj dışına alınır ya da kare değişir. Kare 1'de sol üst köşe kırpılır. Logoyu silmek/boyamak önermiyorum: belgesel karesinde rötuş "gerçek kare" iddiasını zayıflatır; doğrusu başka kare seçmek.

**5. (E) Astrid sahne seti YZ çıktısını yeniden girdi yapıyor; Ayhan'ın açık yasağı.** *Tutarlılık*
Kanıt: Astrid §4, 05-2 / 05-3 / 05-4 / 10-1 / 10-2 / 10-3 referans sırası: "4) `tur-3-soyunma-odasi.jpg` (mekân ve kişi kilidi)", "`tur-3-kort-esigi.jpg`", "`tur-3-pist.jpg`"; §3: "ilk onaylanan geniş kare… kilit olur". Bunlar `Yapay Zeka Görselleri/Adaylar` içindeki dosyaların repo kopyası. Ayhan: "Sakın… Yapay Zeka Görselleri klasörünü tekrar tekrar işleme"; hafıza: "referans/girdi olarak tekrar üretime sokulmaz. Higgsfield referansı yalnız orijinal fotoğraftan verilir." Bugünkü beş video da YZ kareden hareketlendirildi ("exactly as in the first frame"): yasak görselden-videoya üretimi kapsıyor mu, sorulmamış.
Düzeltme: üretimden önce Ayhan'a tek soru: "YZ karesini (a) videoya çevirmek, (b) sonraki kareye kişi/mekân kilidi olarak vermek yasağın içinde mi?" Cevap gelene kadar set yalnız üç orijinal referansla (`3H2A9014/8997/8554`) çalışır; 4. referans satırları çıkar.

### Düzeltilmeli

**6. (B) Madde 30 özeti: iki nüans ve bir görsel-yazı kopukluğu.** *Verification*
- Kare 5: "engelli çocuklar… diğer çocuklarla eşit erişir." Sözleşme bir yükümlülük koyar (devletler eşit erişimi **sağlamak için tedbir alır**); kare bunu olmuş bir durum gibi yazıyor. Türkiye'de okulda spora erişemeyen bir çocuğun velisi bu cümleyi yanlış bulur. Öneri: "Devletler, engelli çocukların… eşit erişimini sağlamakla yükümlü."
- Kare 4: "teşvik eder, … sağlar" yükümlülüğü abartmıyor, ama "uygun tedbirleri alır" çerçevesi ve "genel (herkese açık) spor etkinlikleri / mümkün olan en geniş ölçüde" kaydı düşmüş. Kabul edilebilir kısaltma; "Taraf devletler" yazılırsa daha doğru.
- Kare 5 görseli bir apartman boşluğu ve bisikletler; başlık "OKULDA DA". Görsel okul değil. Hafıza notundaki "görsel yazı sinerjisi" isteğiyle çelişiyor.
- Kare 6 uyarı satırı ("Madde özetleri bize ait, resmî çeviri değildir") 21 px; 1080 px karede telefonda yaklaşık 7 punto, okunmaz. Uyarı okunmuyorsa yok sayılır. En az 34 px ya da caption'a da yazılmalı.
- "194 taraf… bugün": sayı 14 Kasım okuması; 10 Aralık sabahı yeniden okunmalı (yayın günü kapısı).
- Adlandırma: kare 1 "BM Engelli Hakları Sözleşmesi" (yaygın kısa ad), metinler v01 caption'ı "Engellilerin Haklarına İlişkin Sözleşme" (resmî ad, bugün teyit edildi). Yanlış değil ama iki ad aynı gönderide. Caption'da resmî ad bir kez, karede kısa ad kalabilir. "Sözleşmesi / sözleşmeyi / Sözleşmeye" büyük-küçük harf tutarsız.

**7. (B) Onur: kapakta protez kanca kare olarak çalışıyor; kare 4 yorgunluk okutuyor.** *Değer Uyumu*
Kare 1: kişi kesilmiş, kadrajın öznesi bıçak protez, üstünde 377 punto "20 YIL." İnsan değil cihaz kapakta. Acıma ya da ilham çerçevesi yok, süper-insan dili yok; ama hak temalı bir gönderide dikkat çekici nesne olarak protez seçilmiş — planın kendi sabiti ("protez… görselle de kurulmaz", "kanca kare" kaygısı) ile aynı aileden. Kare 3 (iki sporcu yan yana yürüyor, biri kolunu diğerinin omzuna atmış; fail, gündelik, eşit) bu setin en onurlu karesi ve kapak adayı.
Kare 4: sporcu başını engele yaslamış, yüz kollarda; üstünde "Devletler… teşvik eder". Antrenman arası dinlenme, ama hak cümlesiyle yan yana "zorlanıyor, devlet yardım etmeli" diye okunabilir. Kurban çerçevesine en yakın kare bu. Hareket hâlinde bir kareyle değişmeli.
Öneri: sıra 3 → kapak; kare 1 içeriye; kare 4 değişir.

**8. (C) Çorap logosu ve ürün temsili: aday aday.** *Verification — gerçek referans `3H2A9014.jpg` ile karşılaştırıldı (bulut konturu + sağ üstte küçük figür, koncun dış yanında, yaklaşık konç genişliğinin yarısı)*

| Aday | Logo | Diğer | Öneri |
|---|---|---|---|
| `aday-ipte` | Dört amblem de referansa yakın; konumu konç ağzına fazla yakın | Yok | Kullanılabilir (en temiz aday) |
| `aday-kort-esigi` | Ön çorap yakın; arka çorapta amblem dönmüş, figür altta | Ayakkabı referanstaki üçüncü taraf modelin neredeyse kopyası (yan panelde gri bant) | Arka amblem düzelmeden çıkmaz; ayakkabı K4'e bağlı |
| `aday-pist` | Amblem çorabın **arkasında**, sol çorapta iki amblem, sağda yarım üçüncü | — | Ele |
| `aday-soyunma-odasi` | Amblem gerçeğinin yaklaşık iki katı, figür yeri kaymış | Kadrajda şort/giysi görünmüyor, figür çıplak okunuyor (Astrid de not etmiş) | Ele ya da yeniden kadraj |
| `ugc-ayna-soyunma-odasi` | Sol çorapta amblem dikey bir işarete dönmüş | Üç mercekli telefon (logo yok ama tasarım tanınır); yüz | Ele (bulgu 1) |
| `ugc-korttan-cikis` | Küçük, kabul edilebilir | Raket çantasında marka grafiğine benzer kırmızı-yeşil işaretler; sol ayakkabıda topuk yanında koyu kavisli iz (%100'de bakılmalı); tam profil yüz | Çanta ve ayakkabı %100'de teyit edilmeden çıkmaz |
| `ugc-tribun-kosu-sonrasi` | Çok küçük | **Şortun paçasında yuvarlak ikinci bir amblem** (SoC'nin şortu yok: uydurma ürün ya da üçüncü taraf izlenimi); yanak ve omuzda patlamış parlak lekeler; tam yüz, kahkaha | Ele |
| video `bagcik` | İlk karelerde amblem yok, klibin ortasında beliriyor ve "JS" benzeri bir işarete dönüyor | — | Ele. Plan madde 10 bunu "aday video hazır" sayıyor |
| video `top-alma` | Klip boyunca tutarlı, referansa yakın | Top üçüncü kareden sonra kadrajdan çıkıyor (hata değil) | Yakın planlar içinde en kullanılabilir |
| video `pist-yuruyus` | Arkadan, amblem okunmuyor | Marka sızıntısı görmedim | Fizik temiz; ürün görünmüyor, "ürün" hattına yazılamaz |
| video `kort-servis-hazirligi` | Leke düzeyinde | Yüz baştan sona okunur | Bulgu 2'ye bağlı |
| video `pist-esneme` | Amblem kaval kemiğinin önünde ve büyük (gerçekte dış yanda) | **Bileklik ilk üç karede var, sonra yok** (süreklilik hatası); yüz | Düzeltilmeden çıkmaz |

Ölçemediğim: videoların sesi (dinleyemedim; YZ ses izi var, prompt "no voice" diyor ama teyitsiz), kareler %100 büyütmede, YZ yüzlerin gerçek bir kişiye benzerliği.
Reklam işareti: müşteri sitede gördüğü çorabı eline almalı (planın kendi cümlesi). Amblemi yeri/boyu farklı çorap gösteren reklam "ürünü yanlış temsil" şikâyetine açık. Kural öneriyorum: **amblemin okunduğu her kare referansla yan yana konup geçmeden yayın adayı sayılmaz.**

**9. (A) Plan v5 bugün olanların gerisinde kalmış; yedi iç tutarsızlık.** *Tutarlılık*
- Satır 4: "Hiçbir içerik üretilmedi." Üretildi: 12 YZ aday + 6 karelik taslak.
- §2.1: "Hesapta 1.000 kredi var"; bugün 763. "Önce üç karelik deneme… kredi yanmaz": altı tur yapıldı, 237 kredi harcandı.
- §2.1 "Yüz yok… yalnız diz altı" ile aynı bölümdeki "Geniş açı, tam boy" yan yana (bulgu 2). K1 metni eski; K1'in bağlı madde listesinde 04 ve 15 yok.
- §2 karar 4 ve okuma anahtarı hâlâ "Lo-fi" tanımlıyor (08, 12, §6 "Lo-fi ile editorial farkı", §9). 08 ve 12 gerçek telefon çekimi, reddedilen YZ lo-fi görünümü değil; ama terim iki anlamda kullanılıyor. 08/12 için "telefon çekimi" denmeli. "Loafer / lacivert pantolon" kalıntısı yok (yalnız "reddedildi" diye geçiyor).
- §5: madde 11 "tipografik hali yalnız tema teyidine bağlı". Madde 11 artık gerçek kareli; kapıları rıza, üçüncü taraf işaret ve metin.
- K3: "tipografik kareler (02, 07, 11)" logoya bağlı. Ayhan "her kareye marka adı/logo yok" dedi; 11 için K3 düşer.
- §8.0: "Bu sürüm (v3) Denetmen'den henüz geçmedi." Başlık v5.
- §7.5 klasör yolu (`Steps On Clouds/Instagram 2026-11_12/`) gerçek yollarla (`Design /Instagram…`, `Görseller/Yapay Zeka Görselleri/…`) tutmuyor.

**10. (A) Orijinal–YZ dengesi sayıda dengeli, görünürlükte YZ ağır.** *Devil's Advocate*
Sayım doğru: orijinal 6 (+19 şartlı), YZ 8. Ama: (a) çekirdek 14 içinde YZ 6, orijinal 4; (b) ürün hattındaki dört Reels'in dördü de YZ (05, 10, 15, 16), gerçek Reels yalnız 08 ve 12; (c) 24 Kas – 8 Ara arasında art arda dört YZ gönderi (04, 05, 06, 10), aralarında orijinal olarak yalnız 07/08/09. İlk izlenim haftalarında hesabın hareketli yüzü tamamen YZ olur. "Dengeli" Ayhan'ın sözü; sayı tutuyor, sıra tutmuyor.
Öneri: 14 (orijinal, `Steps On Mela` yakın planlar) 5 Aralık öncesine çekilir ya da 06 ile yer değiştirir; 10'un yakın planı gerçek arşiv videosundan gelir (varsa).

**11. (D) Metinler v01.** *İnsan Sesi + Değer Uyumu*
- **Madde 11 metni taslakla uyuşmuyor.** Metin 5 kare ve üç tarih anlatıyor; taslak 6 kare ve Madde 30. C1 "Yorum eklemedik" diyor, karelerde bizim özetimiz var. C1 "Üç tarihi kaydet" diyor. Yeniden yazılmalı; karelerdeki metin de Metin Yazarı'ndan geçmedi (Model A).
- **Madde 07 kare 5:** "'Rağmen'i çıkar. Cümle yine doğru." Çıkarınca "Buna çok iyisin" kalır; cümle doğru olmuyor. "'Buna rağmen'i çıkar" olmalı. Ayrıca emir kipi; aynı gönderinin caption'ı "kimseye ders olsun diye yazılmadı" diyor.
- **Kare 2:** "Kimsenin tebrik edilecek bir durumu yok." "Durum" kelimesi engelliliği eksiklik gibi okutabilir; dört karşı cümlenin en riskli olanı. Öneri yönü (yazmak Metin Yazarı'nın): cümle günü anlatsın, kişiyi değil.
- **Kare 4:** "Merdiveni sevgi kaldırmaz. Rampa yapılır." İki cümleye bölünmüş karşıtlık kalıbı; yazarın "karşıtlık sıfır" sayımı bunu görmüyor. Tek başına kalabilir, ama dört karenin dördü de aforizma ritminde: kalıp–cevap–kalıp–cevap. Vaaz tonu buradan geliyor. Bir ya da iki karede cevap yerine olgu (kaynaklı bir veri, bir tarih) konursa ton düşer.
- **07 C1:** "Biz de yıllarca duyduk." Marka adına yaşanmışlık beyanı; Ayhan'ın kendi cümlesi değilse uydurma yaşanmışlık. Ayhan onayı açıkça işaretlenmeli. **07 C2:** "Bir markanın sosyal medyasını yöneten birini tanıyor musun? Bu gönderiyi ona yolla." Planın "kimseyi hedef almaz" satırıyla doğrudan çelişir; çıkmalı.
- **Madde 04 "İLK ADIMI ÖĞRETENE":** bağ zorlama. İlk adımı öğretmen değil aile öğretir; C1'deki "İlk adımı onlardan öğrendik" cümlesi bu yüzden aksıyor. Marka ekseni ("adım") günün öznesinin önüne geçmiş. Üstüne görsel YZ: var olmayan bir koçla gerçek öğretmenlere teşekkür. "TEŞEKKÜRLER HOCAM" (seçenek 2) daha dürüst; ya da plan kendi cümlesini uygular ve gün atlanır.
- **Madde 16:** "CloudOne'da sormana gerek yok… numara sormadan alınır." 38–44 dışındaki ayak için yanlış; başlık 2 ("NUMARA SORMA") aynı sorun. "38–44 arasıysa sormana gerek yok."
- Kara liste, indirim/kıtlık dili, "protez uyumlu", övgü cümlesi: yok. `sozdizim_tarama.py` dosyanın tamamında çalıştırıldı, çıktı vermedi (araç kısa caption'ı ölçmüyor; yazarın notu doğru). 48 saat kuralı: aracın kısa metinde kör olduğu ikinci kez kayda geçti, kapıya dönüşmedi.

### Not

**12.** Kare 3'te beyaz gövde metni yaprak ve duvar üstünde; "194 taraf var." satırı açık zeminde zayıf. Gölge katmanı kare 3 için koyulaştırılmalı. · Planın punto ölçeği "377/233/144/34/21" diyor, üretici ve hafıza "377/233/144/89/55/34/21"; 89 ve 55 kullanılmamış, sorun değil. · Astrid §8.7'deki öneri (markasız tek ayakkabı referansı) ayakkabı sızıntısının kalıcı çözümü; ama o da YZ çıktısını girdi yapar (bulgu 5'e bağlı). · Astrid §8.5: madde 16'daki hediye kutusu uydurma; gerçek ambalaj gösterilmiyorsa "hediye paketi" ürünün ambalajı gibi okunmamalı.

---

## KIRMIZI TAKIM — olduğu gibi yayınlanırsa en kötü üç senaryo

1. **"Sahte kullanıcılarla reklam."** Bir takipçi ya da rakip ayna selfie'sinin YZ olduğunu gösterir (bileklik kayboluyor, logo değişiyor, şortta olmayan amblem). Marka aynı hafta başkalarına "kurmayacağımız cümleler" diye dil kuralı koymuş ve bio'sunda dürüstlük taşıyor. Sonuç: ikiyüzlülük okuması, Reklam Kurulu şikâyeti olasılığı, gerçek kullanıcı içeriğinin (madde 17) inandırıcılığının bitmesi. 295 takipçide yayılma küçük, ama ekran görüntüsü kalıcı ve Ayhan'ın adına yapışır.
2. **"Protezimi çorap reklamına kapak yaptılar."** Kare 1 ya da 3'teki sporculardan biri ya da kulübü, rızası olmadığını yazar. Gönderi hak günü gönderisi olduğu için çelişki en sert haliyle okunur: hakları anlatan gönderi, öznesinin hakkını sormamış. Kareler aynı hafta hediye sezonu satış gönderilerinin (8 ve 12 Aralık) arasında.
3. **"Hak gününü vitrine çevirdi."** 2–10 Aralık arası dört hak içeriği (07, 08, 11 + 13 Aralık Story), iki yanında YZ ürün Reels'leri ve yılbaşı son sipariş Story'si. 07'nin karşı cümleleri vaaz tonunda kalırsa ilk yorum "sen kimsin" olur; kare 2 ve 4'teki Nike/Adidas/rakip çorap işaretleri de "başkasının markasıyla hak içeriği" diye ayrıca dolaşır.

---

## MALİYET — 237 krediden çıkan kapı ve ölçü (CLAUDE.md §10: red → 48 saatte ölçü ya da kapı)

Gözlem: reddedilen turların sebebi piksel değil **yön**dü (kirli/lo-fi; loafer; diz altı ağırlık). Yön hatası üretmeden, bir cümleyle yakalanabilirdi. Commit kaydına göre iki video 70 kredi; beş video yaklaşık 175 kredi eder (harcamanın yaklaşık dörtte üçü; tam döküm dosyada yok). Ayhan'ın tercih etmediği üç yakın plan video, "videolarda da geniş açı istiyorum" sözünden **önce** mi sonra mı üretildi, kayıtta okunmuyor. `raporlar/teslim-kutugu.md`'de bugünün kredi satırı yok.

Önerilen kapılar (Fox uygular, Ayhan onaylar):
1. **Yön kartı kapısı (0 kredi).** Her yeni görsel yönden önce Ayhan'a beş satır: styling · mekân · kadraj (diz altı / tam boy) · figür ve yüz · bir referans kare (orijinal). "Evet" gelmeden üretim yok. Bugünkü üç reddin üçü bu kartta yakalanırdı.
2. **Tur tavanı.** Onaysız yönde tur başına en çok 3 kare (6 kredi). Video yalnız Ayhan'ın **o kareyi** onaylamasından sonra, tek tek; bir oturumda onaysız en çok 1 video.
3. **Logo kapısı (0 kredi).** Videoya gidecek karede amblem referansla yan yana konur; sapma varsa video üretilmez (video sapmayı miras alır: bağcık ve esneme klipleri).
4. **Maliyet satırı.** Her turdan önce "bu tur X kredi, kalan Y" yazılır; tur bitince teslim kütüğüne tur · kredi · kabul/ret · **ret sebebi** girer.
Ölçü: **kabul edilen aday başına kredi.** Bugünün değeri Ayhan hangi adayları tuttuğunu söyleyince hesaplanır; benim sayımımla kullanılabilir durumda olan en çok 4 aday var (`aday-ipte`, `top-alma`, `pist-yuruyus`, şartlı `korttan-cikis`), yani aday başına yaklaşık 60 kredi.

---

## ÇELİŞKİ

Alt roller arası çelişki yok (tek denetçi). Fox ile ayrışma beklediğim nokta: bulgu 1. Fox "UGC dili Ayhan'ın kararı" diyebilir; ben kararı tartışmıyorum, kararın içindeki riski yazıyorum: Ayhan "UGC'leri de buna göre çalış" dedi, "gerçek kullanıcı paylaşımı gibi görünsün" demedi. İkisi Ayhan'a birlikte gitmeli.

## SORULMAMIŞ SORULAR

1. Belgesel sporcularının rızası marka hesabını kapsıyor mu, reşit olmayan var mı? (bulgu 3)
2. YZ karesini videoya çevirmek ve sonraki kareye referans vermek "tekrar işleme" yasağının içinde mi? (bulgu 5)
3. Okunur YZ yüzü Ayhan bilerek kabul ediyor mu? (bulgu 2)
4. YZ ile üretilmiş gönderi @ayhanerden_ ile ortak paylaşılmayacak (K9); peki takipçi "bu kim?" diye sorarsa hesabın cevabı ne olacak? Cevap metni hazır değil.
5. Videoların sesi kim tarafından dinlendi? YZ ses izi yayınlanacak mı, kesilecek mi?
6. Madde 04 için 24 Kasım'a on gün var, sahne (04b) henüz üretilmedi ve iki figürlü geniş açı hiç denenmedi. Gün atlanırsa yerine ne çıkar?

## KARAR ÖNERİSİ

☐ Temiz
☑ **Düzelt — Fox:** bulgu 9 (plan güncelleme), 8 (aday eleme tablosu), 6 ve 4 (madde 11 kare değişimi ve metin) · **Metin Yazarı:** bulgu 11 ve madde 11 kare metinleri · **Astrid:** bulgu 5, 2
☑ **Ayhan'a eskalasyon:** bulgu 1 (YZ "UGC"nin nasıl sunulacağı + K8), bulgu 2 (yüz), bulgu 3 (sporcu rızası), bulgu 5 (yasağın kapsamı). Dördü de Ayhan'ın tek cümlelik cevabıyla kapanır; hiçbiri onun verdiği kararı geri almıyor.

## Kaynaklar

- treaties.un.org, IV-15 (CRPD durum sayfası): https://treaties.un.org/Pages/ViewDetails.aspx?src=TREATY&mtdsg_no=IV-15&chapter=4&clang=_en
- un.org, Human Rights Day: https://www.un.org/en/observances/human-rights-day
- Aile ve Sosyal Hizmetler Bakanlığı, Sözleşme tam metni: https://www.aile.gov.tr/eyhgm/engellilerin-haklarina-iliskin-sozlesme/sozlesme-surumleri-ve-ek-protokol/normal-surum/tam-metin/
- TBMM, Resmî Gazete 27288: https://www.tbmm.gov.tr/Files/Komisyonlar/insanHaklari/docs/ulusal_belgeler/Rg27288.pdf
- idpwd.gov.au, UN IDPwD theme (ikincil): https://www.idpwd.gov.au/about-international-day-people-disability/united-nations-idpwd-theme
- ohchr.org CRPD metni: 403, açılamadı.
