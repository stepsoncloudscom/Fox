# Tasarım — Instagram Haftalık Döngü (@stepsoncloudscom)
*14 Kasım 2026 · Fox · v2 (Ayhan'ın cevapları + kurucu okuması işlendi) · Durum: TASARIM, Ayhan onayı bekliyor · Sistem geliştirme programının ilk parçası ("tüm sistemi geliştireceğiz, sen de dahil" — Ayhan, 14 Kas)*

---

## 1 · Niyet ve neden

**Ayhan'ın başarı tanımı (14 Kas):** "Instagram'ın düzenli çalışması."

Bağlam: Satış odağı 3 Kas'tan beri CloudOne + Steps On Clouds markası (karar günlüğü). Marka hesabı 295 takipçi, son kendi gönderisi 24 Eylül — 51 gün sessiz. v5 Instagram planı (`raporlar/soc-instagram-plani-2026-11-17_12-31.md`) hazır ama tek seferlik bir kampanya: başlamadan 13 karar (K0–K12), her maddeye ayrı onay, her gönderiye ayrı yayın adımı. Nakit Motoru'nun Temmuz'da takıldığı yerle aynı yapı: üretim var, onay ve gönderim Ayhan'da birikiyor (39 taslak Gmail'de kaldı).

**Bu tasarımın işi:** kampanyayı **kendi kendine dönen bir haftalık düzene** çevirmek. Hazırlık Ayhan'ın hatırlamasına bağlı olmadan yapılır; Ayhan haftada bir kısa oturumda onaylar ve zamanlar.

## 2 · Ayhan'ın kararları (bu konuşmada, olduğu gibi)

| Karar | Ayhan'ın seçimi |
|---|---|
| Satış hattı | CloudOne (Marka Bulutu OS park kalır — 3 Kas kararı geçerli) |
| Başarı ölçütü | "Instagram'ın düzenli çalışması" |
| Sıklık | **"Haftada 3 ideal"** |
| Ayhan'ın payı | **Haftalık oturum** — pazartesi: önüne hazır paketler gelir, onaylar, Meta Business Suite'te zamanlar |
| Makine | **Otomatik hazırlık** — zamanlanmış görev paketleri hazırlar, pazartesi onay |
| Deneme kareleri | **"Evet, maksimum 3 deneme karesi uygun"** — görev, Higgsfield maddesi başına en çok 3 deneme karesini Ayhan'a sormadan üretebilir |
| Video çözünürlüğü | **"1080p uygun"** — Reels yayın sürümü 1080p |
| Video sıklığı | **"Haftada 1 video paylaşımı yetecektir"** — haftada en çok 1 Reels; diğer gönderiler tek fotoğraf / kaydırmalı |
| Yer | **"Mac'te kalsın"** — görev, paketler, pazartesi oturumu ve yükleme bu Mac'te |

Fox'un önerip Ayhan'ın itiraz etmediği çerçeve: kuyrukta 2 haftalık onaylı tampon · 14 Kas görsel kuralları sabit (v5 §2.1).

## 3 · Hedefler, hedef olmayanlar, anti-hedefler

**Hedefler**
- Haftada 3 gönderi (en çok 1'i video), 19 Kasım'dan itibaren hiç boş hafta yok. Taban 2: bir slot boşalırsa hafta en az 2 ile kapanır, sıfıra düşmez.
- Ayhan'ın Instagram'a haftalık payı ~30 dk (onay + zamanlama). Ayın ilk pazartesi +10 dk (havuz onayı + Insights). Gerçek süre ilk dört pazartesi ölçülür.
- Kuyrukta her an ≥ 7 gün onaylı içerik; hedef 14 gün.
- Her paket ölçülür: tur, Denetmen kararı, Ayhan kararı, red sebebi, token, kredi → `raporlar/teslim-kutugu.md`.
- Düzen 31 Aralık'ta bitmez: v5 maddeleri tükenince aylık havuzla devam eder.

**Hedef olmayanlar (bu tasarım yapmaz)**
- Fox yayınlamaz, zamanlamaz. Yayın tuşu Ayhan'da (Kademe 2). Meta API ile otomatik yayın kapsam dışı.
- Yorum/DM yönetimi, günlük Story akışı, reklam.
- Wix mağaza düzeltmeleri (Growth Sprint S1–S5) — yalnız K0 önkoşul olarak bağlanır (§6).
- Yeni ajan. Mevcutlar: Metin Yazarı, İçerik Ajanı, Astrid, Denetmen.
- Fox'un diğer bakım açıkları (aylık budama, ilişki hafızası, rubrik v2) — programın sonraki parçaları.

**Anti-hedefler (teknik olarak çalışsa bile başarısızlık sayılır)**
- Ayhan'ın yeniden görsel yön turlarına çekilmesi (14 Kas: 6 tur). Kurallar sabit; yeni yön turu yalnız Ayhan isterse.
- Onaysız paketlerin birikmesi, görevin boşa koşması (Nakit Motoru zombisi).
- "Fake" görünen YZ karesinin yayına çıkması.
- Acıma/ilham dili, Red Lions'ta bireysel hikâye, "protez uyumlu" iddiası, uydurma rakam.
- Kredinin dönem ortasında tükenip düzenin durması.

## 4 · Kısıtlar

- **Kademe:** üretim/denetim Kademe 1 · onay ve zamanlama Kademe 2 (Ayhan) · Fox hiçbir hesaba giriş/şifre girmez.
- **Kredi kuralı** (memory `kredi-harcayan-uretim-ayhan-yapar`): varsayılan Fox başlatmaz. Bu tasarımda iş bazında iki açık izin var: (a) madde başına en çok 3 deneme karesi, onaysız (Ayhan, 14 Kas); (b) tam üretim yalnız kartta maliyeti yazılmış yön onayından sonra. Bu, 14 Kas kapısı (a) ve Astrid'in "kredi harcayan her adım Kademe 2" kuralının **yalnız bu akış için** istisnasıdır; başka işte geçmez.
- **Görsel kurallar:** v5 §2.1 aynen (spor çizgisi, geniş açı tam boy, üretilmiş yüz görünebilir — Ayhan 14 Kas "Evet, görünsün"; şartlar: kameraya bakan portre yok, YZ etiketi, gerçek kullanıcı gibi sunulmaz — engellilik temalı içerikte YZ insan yok, logo yakın planda gerçek fotoğraftan, gerçek ürün referansı, YZ etiketi K8'e göre).
- **Kaynak dengesi** (memory `soc-orijinal-yz-dengesi`, `redlions-arsiv-yalniz-soc-gorunen`): orijinaller `Görseller/` altından; `Yapay Zeka Görselleri` tekrar girdi olmaz; Red Lions'tan yalnız SoC görünen kare.
- **Dil:** Türkçe glyph kontrolü (İ/ı/ğ/ş), `sozdizim_tarama.py` + `slop_tarama.py` her metinde.
- **Denetmen:** her paket Denetmen'den geçer. DUR alan paket karta çıkmaz.
- **Kredi:** bakiye ~623 (durum dosyası, 14 Kas sonu). Maliyet: görsel 2, 720p klip 35, **1080p klip 80**. Bir Reels 1–3 klip → 80–240 kredi.

## 5 · Yaklaşımlar

| | Ne | Kazanç | Bedel |
|---|---|---|---|
| **1 · Otomatik hazırlık + pazartesi onayı** ✅ seçildi | Perşembe zamanlanmış görev, iki hafta sonrasının paketlerini hazırlar; pazartesi Ayhan onaylar | Düzen Ayhan'ın hatırlamasına bağlı değil; onay oturumu kısa | Zombi riski → üç sigorta (§7.5) |
| 2 · Elle tetikleme | Pazartesi Ayhan "Instagram haftası" der, hazırlık o oturumda | Basit, boşa koşma yok | 30 dk → 1–2 saat; tampon Ayhan'ın oturum açmasına bağlı |
| 3 · Aylık blok + haftalık onay | Ayda bir toplu üretim | Kredi verimli | "Fake" sorunu çözülmeden toplu üretim kredi yakar; içerik bayatlar |

Neden 1: "düzenli" hedefi, düzenin Ayhan'ın hafızasına bağlı olmamasını gerektiriyor; sigortalar Temmuz hatasını kapatıyor.

## 6 · Başlangıç — 16–19 Kasım

İlk perşembe görevi 19 Kas'ta koşar ve 30 Kas haftasını hazırlar. 19–29 Kas (v5 Hafta 1–2) elle hazırlanır.

1. **Pazartesi 16 Kas, ilk oturum:**
   - **4 başlangıç kararı** (v5 §3): **K0** mağaza sayfası ("550 TL" SEO açıklaması + 15/7 gün iade çelişkisi; ilk ürün gönderisinden önce kapanmalı) · **K4** Steps On Mela hakları (Hafta 1 arşiv maddeleri buna bağlı) · **K8** YZ etiketi · **K10** bio. Diğer K'ler akışta, ilgili paket kartta göründüğünde sorulur.
   - **v5 listesinin havuz onayı** (§7.6'daki aylık havuz onayının ilk örneği): 20 maddeye evet/hayır. Haftada 3 hedefiyle isteğe bağlı (İ) maddeler de normal akışa girer; Denetmen'in 12 madde önerisi ve madde 09 kararı burada kapanır. **Yalnız havuzda onaylı madde üretilir ya da kredi harcar.**
   - **T0 Insights** ekranları (v5 §6).
   - **Hafta 1–2 kartı:** Hafta 1 = 01, 02, 03 (arşiv, kredisiz) · Hafta 2 = 04 (Higgsfield tek kare, Öğretmenler Günü, 14 Kas taslakları) · 05 (Reels; onaylı 720p kliplerin yön onayı — 1080p yayın sürümü 19 Kas'ta üretilir, ~240 kredi) · 06 (aday kare hazır). Onaylananlar zamanlanır.
2. **19 Kas perşembe:** ilk otomatik koşu — 05'in 1080p sürümü + 30 Kas haftasının hazırlığı.
3. **23 Kas pazartesi:** 05 yayın onayı (26 Kas).

K4 olumsuz çıkarsa Hafta 1 arşiv maddeleri tipografik/Belgesel Stills yedeklerle değişir (§7.4).

**Slot kuralı:** haftada 3 gönderi hedef, 2 taban; **haftada en çok 1 video** (Reels). İlk kuyruk v5'in tarihli takvimidir; özel gün maddeleri kendi tarihinde kalır (3, 10, 31 Aralık perşembe olsa da). v5'te gönderi olmayan günler (27 Kas indirim günü) boş kalır.

**v5 takviminin "haftada 1 video"ya uyarlanması** *[Fox önerisi — 16 Kas havuz onayında kesinleşir]*:

| Hafta | Video | Değişiklik |
|---|---|---|
| 1 · 19–22 Kas | — | yok (01, 02, 03) |
| 2 · 23–29 Kas | 05 | yok (04, 05, 06) |
| 3 · 30 Kas–6 Ara | 08 (konuşma) | yok (07, 08, 09) |
| 4 · 7–13 Ara | 12 (paket) | **10 bu haftadan çıkar** — iki Reels vardı. 12 kalır: hediye sezonunun satış gönderisi, son sipariş tarihini taşır. Hafta 11 + 12 (+ kredisiz yedek) |
| 5 · 14–20 Ara | **10** (19 Ara) | **10 buraya taşınır, 15 düşer** (İ idi, aynı "pist/kort lifestyle" dili). 13 yalnız tek kare olur (Reels seçeneği kapanır) |
| 6 · 21–27 Ara | 16 (yılbaşı) | 17 yalnız fotoğraf olarak bu haftaya girer; video gelirse 7. haftaya kayar |
| 7 · 28 Ara–3 Oca | — ya da 17 | 19, 20 (+ 17 video gelirse) |

## 7 · Tasarım

### 7.1 · Haftalık takvim

| Gün | Ne olur | Kim |
|---|---|---|
| **Perşembe** (saat: §9) | Zamanlanmış görev `instagram-haftalik-hazirlik`: kuyruğu okur, 2 hafta sonrasının 3 slotunu hazırlar, Higgsfield maddeleri için deneme karelerini üretir, yön onayı almış maddelerin tam üretimini yapar, revize notlarını işler, kuyruğu günceller, kütüğe yazar, commit+push | Fox + ajanlar |
| **Pazartesi sabah** | Sabah brifingi: "Instagram: kartta N paket · tampon X gün · dönem kredisi Y" satırı | morning-brief |
| **Pazartesi oturum** (~30 dk) | Ayhan Fox'a "Instagram" der → Fox önce perşembe heartbeat'ini kontrol eder (§11), onay kartını açar → her paket için Onay / Revize (+not) / Çıkar → Ayhan onaylananları Meta Business Suite'te zamanlar ve "zamanlandı" der → Fox kuyruğu günceller | Ayhan + Fox |

### 7.2 · Kuyruk — `raporlar/instagram-kuyruk.md`

Tek doğruluk kaynağı. Tablo, satır = bir gönderi slotu:

`slot tarihi · saat · madde no · başlık · hat (ürün/marka/özel gün) · üretim yolu (arşiv/tipografik/Higgsfield/gerçek çekim) · durum · tur · kredi · dosya yolu · not`

**Durumlar:** `havuzda` → `deneme karelerinde` (yalnız Higgsfield: 3 deneme karesi + 5 satırlık yön kartı + tam üretim maliyeti birlikte kartta) → `üretimde` → `denetimde` → `onay bekliyor` → `onaylandı` → `zamanlandı` → `yayında` · yan yollar: `revize` · `park` · `çıkarıldı`.

Üstte üç sayaç: **tampon (gün)** = bugünden sonraki `zamanlandı`+`onaylandı` slotların kapsadığı gün · **dönem kredisi: harcanan / bütçe / bakiye** · **görev durumu** (`AKTİF` / `DURAKLADI` + sebep). Altta **heartbeat** satırları: her koşunun tarihi ve tek satır özeti.

### 7.3 · Paket

Her paket bir klasör: görsel(ler) ya da video (yayın çözünürlüğünde), `metin.md` (caption TR — madde 18 EN, hashtag, alt metin, YZ etiketi evet/hayır, önerilen saat), Denetmen notu. Klasör: `Desktop/Steps On Clouds/Design /Instagram/Paketler/<slot-tarihi>_<madde>/`. YZ ham çıktıları `Görseller/Yapay Zeka Görselleri/…` altında kalır (memory `soc-yz-gorsel-kayit-yeri`); pakete yalnız seçilen kopya girer.

**Üretim zinciri (perşembe):** Metin Yazarı metni yazar → İçerik Ajanı görseli hazırlar (arşiv/tipografik) ya da Astrid sahne+prompt kurar (Higgsfield) → render edilip gözle denetlenir (öz-denetim ⑧) → Denetmen → kart.

### 7.4 · Üretim yoluna göre akış

- **Arşiv / tipografik (kredisiz):** tek döngü. Perşembe hazırlanır → pazartesi onay → zamanlanır.
- **Higgsfield:** iki döngü. 1. perşembe: en çok 3 deneme karesi (≤ 6 kredi) + 5 satırlık yön kartı + tam üretimin kredi maliyeti → pazartesi **yön onayı** (onay o maliyeti kapsar) → 2. perşembe: tam üretim → pazartesi **yayın onayı**. 2 haftalık tampon bu yüzden var.
- **Video:** yayın sürümü **1080p**. Onaylı 720p adaylar (bank, file kenarı, kort kapısı, servis hazırlığı, esneme) yön onayı yerine geçer; 1080p sürümleri tam üretimde yapılır. **Risk:** 1080p yeniden üretim, onaylı klibin hareketini birebir tekrar etmeyebilir — üretici modeli yeniden çalıştırır. Kurucu önce Higgsfield'da var olan klibi yükseltme (upscale) yolu olup olmadığına bakar; yoksa 1080p klip yeni bir aday sayılır ve yayın onayında Ayhan 720p ile yan yana görür.
- **Gerçek çekim (08 konuşma, 12 paket):** görev çekim listesini karta koyar; Ayhan çeker, dosyayı klasöre bırakır; sonraki perşembe kurgu.
- **Revize:** not bir sonraki perşembe işlenir. **En çok 2 revize**; üçüncüde madde `park`, slot yedekten dolar.
- **Yedek havuzu:** kuyrukta her zaman **2 kredisiz yedek paket** (arşiv/tipografik, Denetmen'den geçmiş) hazır durur. Revize, ret ya da üretim hatası slotu boşaltırsa yedek girer — düzen kırılmaz.

### 7.5 · Sigortalar (Nakit Motoru dersi)

1. **Kredi bütçesi — bakiye okunarak.** Görev her koşunun başında Higgsfield bakiyesini CLI'den okur ve kuyruktaki sayaca yazar. Kayıt (`fox-claudia-towdoo-proje-calisma-notu.md`): plus plan, 1000 kredi, 14 Ekim'de yenilendi → dönem büyük olasılıkla her ayın 14'ü; görev yenilenmeyi bakiyeden görür, varsayıma dayanmaz. Bir maddenin tam üretim maliyeti bakiyeyi ya da Instagram payını aşıyorsa üretim yapılmaz, karta bayrak düşer, slot yedekten dolar. Reels maliyeti haftalara bölünmez; yön onayı tek seferde kapsar.
   - **Tahmini harcama, 14 Aralık'a kadar:** 05 (3 klip) ~240 + deneme kareleri ve tek kareler ~40 → **~280 / ~623.** 10 (19 Ara'ya taşındı, 160–240) ve 16 (80–160) 14 Aralık'tan sonra; yenilenme bakiyeden görülür. Haftada 1 video kuralıyla bir dönemin Higgsfield yükü en çok ~4 Reels × 80–240.
2. **Kendini durdurma.** Perşembe koşusu, kartta **iki pazartesi üst üste hiçbir karar verilmediğini** görürse yeni üretim yapmaz ve kredi harcamaz, kuyruğa `DURAKLADI — 2 hafta kararsız kart` yazar, yalnız heartbeat ve kütük satırını işleyip çıkar. Ayhan karttan tek karar verdiğinde sonraki perşembe kendiliğinden `AKTİF`'e döner. Her koşu, iş çıkmasa bile heartbeat yazar ve commit+push eder; push başarısızsa brifingde bayrak.
3. **Tampon göstergesi.** morning-brief her sabah kuyruğu okur: Komuta Kartı'nda "Instagram tampon X gün" satırı. **< 7 gün → DİKKAT, < 3 gün → DUR** (yedek havuzundan acil doldurma önerisiyle).

### 7.6 · 31 Aralık sonrası — aylık havuz

v5'in 20 maddesi ilk havuzdur. Her ayın son perşembe koşusu, gelecek ay için **12–13 maddelik** havuz önerisi hazırlar (haftada 3, bunun en çok 1'i video → ayda ~4 Reels + ~8–9 tek fotoğraf/kaydırmalı; üç hat dengesi, özel günler, önceki ayın Insights'ından okunanlar, dönem kredisine göre Higgsfield/arşiv/tipografik karışımı). Ayın ilk pazartesi Ayhan havuzu onaylar (+10 dk). Havuz onayı yoksa görev yedek havuzla döner, yeni madde açmaz.

### 7.7 · Ölçüm

- **İçerik:** ayın ilk pazartesi Ayhan Insights'tan v5 §6'daki ekranları verir (T0: 16 Kas). Ham sayı raporlanır, yüzde değil.
- **Satış:** Instagram'dan okunmaz — UTM'li link + Wix Stores sipariş verisi (Growth Sprint S1'e bağlı; yoksa "ölçülmedi").
- **Maliyet (§5):** her kapanan paket kütüğe bir satır — tur, Denetmen kararı, Ayhan kararı, **red sebebi (boş bırakılamaz)**, token, kredi. Token kesin okunamazsa "~tahmin" etiketiyle yazılır; "ölçülmedi" bu akışta yasak. Ölçü: **kabul edilen paket başına kredi ve token**.
- **Ayhan'ın süresi:** ilk dört pazartesi oturumun gerçek süresi kuyruğa yazılır; 30 dk'yı sürekli aşarsa kart sadeleştirilir.

## 8 · Fox kalemleri (bu programın içinde, Kademe 1)

1. **Nakit Motoru'nu duraklat.** `nakit-motoru-gunluk-kosu` görevi `enabled: false`. Gerekçe: Marka Bulutu OS/moda outreach'i 3 Kas'ta park edildi, görev hâlâ hafta içi her gün koşuyor; defteri 19 Tem'den beri boş. Geri alınabilir — görev dosyası silinmez.
2. **Durum dosyasının kesilmesini düzelt.** `fox-durum.md` 41 satır ama 12,9 KB; SessionStart çıktısı 11,8 KB'ta kesiliyor ve yeni oturum yalnız ilk ~2 KB'ı görüyor. (a) Dosya ≤ 40 satır **ve ≤ 6 KB**'a indirilir; ayrıntı `raporlar/oturum-gunlugu.md`'ye. (b) Kapı: SessionStart hook komutu, dosya 6 KB'ı aşarsa çıktının **başına** "⚠️ fox-durum.md X KB — tavan 6 KB, kesiliyor" satırı basar. (Red → ölçü kuralı: paragraf değil kapı.)
3. **Instagram cephesi durum dosyasına tek satır** — "kuyruk: `raporlar/instagram-kuyruk.md`"; ayrıntı kuyrukta yaşar.

## 9 · Varsayılan değerler (Ayhan değiştirebilir)

| Değer | Varsayılan |
|---|---|
| Instagram'ın kredi payı | Claudia/AI Director işi duraklatılmış olduğu sürece bakiyenin tamamı; o iş yeniden başlarsa Ayhan pay belirler |
| Perşembe koşu saati | 10:00 |
| Pazartesi oturum saati | Ayhan'ın takvimine göre; brifing 07:40'ta hatırlatır |
| Gönderi günleri/saatleri | v5'in tarihli slotları; v5 sonrası T0 Insights "en aktif zamanlar"dan. O gelene kadar Salı, Perşembe, Cumartesi 19:00 (varsayım, ilk ölçümle düzelir) |

## 10 · Kurucuya bırakılanlar

- Zamanlanmış görevin SKILL.md metni, ajan çağrı sırası ve brief formatları (mevcut ajan dosyalarının ÖN KOŞUL'larına uyarak).
- Onay kartının biçimi: pazartesi oturumunda Fox'un açtığı tek sayfa (özel claude.ai Artifact) — her paket için görsel/video önizleme, metin, Denetmen notu, kredi, Onay/Revize/Çıkar. Sayfa oturum içinde yayınlanır; zamanlanmış görev yalnız kuyruğu ve paket klasörlerini hazırlar.
- Zamanlanmış görev ortamında Agent aracı ve Higgsfield CLI'nin (bakiye okuma dahil) çalıştığının **kuru koşuyla doğrulanması** (19 Kas'tan önce). Çalışmıyorsa: görev yalnız kredisiz paketleri hazırlar, Higgsfield adımları pazartesi oturumunda yapılır — bu sapma Ayhan'a bildirilir.
- Higgsfield'da 720p→1080p yükseltme yolu olup olmadığının kontrolü (§7.4).
- morning-brief SKILL.md'ye Instagram satırının eklenme yeri ve biçimi (Komuta Kartı içinde).
- Kuyruk tablosunun tam sütun biçimi.

## 11 · Kurucu okumasından çıkan Fox kararları (Ayhan düzeltebilir)

- **Kaçan koşu:** perşembe koşusu kaçarsa (Mac kapalı), pazartesi oturumu önce kuyruktaki heartbeat'e bakar; perşembe satırı yoksa hazırlığı oturum içinde Fox yapar.
- **Kredi bütçesi:** haftalık sabit tavan yerine bakiye okuması + madde bazlı maliyet onayı (§7.5). Kredi yenilenme tarihi ve devir kuralı varsayılmaz, bakiyeden okunur.
- **Havuz onayı ve slot kuralı:** §6.

---
*Fox · 14 Kas 2026 · Kaynaklar: v5 planı, Growth Sprint v2 (§6), karar günlüğü 3 Kas, Nakit Motoru defteri ve 12 Eyl sistemik bulgu (oturum günlüğü), teslim kütüğü 14 Kas kapıları, Claudia/Towdoo çalışma notu (kredi planı).*
