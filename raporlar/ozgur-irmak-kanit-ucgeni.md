# Kanıt Üçgeni — Özgür Irmak Protez ve Ortez
*T0 Baseline kurulumu · 14 Ağustos 2026 · Fox*
*Şablon: `sablonlar/kanit-ucgeni-olcum-sablonu.md` · OS'un ilk canlı kanıt üçgeni (bugüne kadar 0 müşteride koşmuştu)*

---

## 🔴 ÖNCE BUNU OKU — ölçüm sırasında çıkan bulgu

**Site yayında değil. Altı haftalık içerik üretimi kamuya görünmüyor.**

| Ne | Ölçüm | Kaynak (14 Ağu 2026) |
|---|---|---|
| Wix sitesi durumu | **Draft — hiç yayınlanmamış** · Plan: **Free** | Wix API `GetSiteContext` |
| `ozgurirmakprotez.wixsite.com/mysite` | **HTTP 404** | doğrudan istek |
| `ozgurprotez.com` (asıl alan adı) | Hâlâ eski **"YENİLENİYORUZ"** bakım sayfası | doğrudan istek |
| Site dili | **yalnız `tr`** — TR/EN/AR/RU hedefi uygulanmamış | Wix API |

**Ne anlama geliyor:** 30 Temmuz'daki "blog YAYINLANDI" kaydı **Wix'in blog koleksiyonu içinde** doğruydu — post `PUBLISHED` statüsünde. Ama **sitenin kendisi hiç yayınlanmadı**, dolayısıyla yazı kamuya erişilebilir değil. İki ayrı yayın kavramı (post publish ≠ site publish) birbirine karıştı ve altı hafta boyunca kimse fark etmedi. Fox da fark etmedi — çıktıyı doğruladı, **erişilebilirliği** doğrulamadı.

**Muhtemel kilit:** Wix **Free** planı özel alan adı bağlamaya izin vermez. `ozgurprotez.com` → Wix bağlantısı için önce ücretli plan gerekir. Yani web hattı teknik bir eksikte değil, **bir ticari kararda** duruyor. Kimin ödeyeceği (müşteri mi, SoC mu) sözleşmede tanımlı mı — kayıtlarda yok.

**Ayhan'a talep:** ① Wix planı kimin adına/hangi bütçeyle yükseltilecek? ② Site yayına alınmadan önce hangi kapılar kapanmalı (avukat onayı — bkz. marka context §Hukuki Çerçeve)? Bu ikisi cevaplanmadan içerik üretmeye devam etmek **stok biriktirmek**, teslim etmek değil.

**İkincil bulgu — mükerrer yazı:** Blogda "Protez Bacak ve Kol Bakımı" başlığı **iki kayıt** olarak duruyor: yayınlanmış olan (7 Ağu, 4 dk) ve 8 Ağustos'ta İnsan Sesi Kapısı düzeltmesiyle **yeni draft olarak açılmış** ikinci kopya (3 dk, `UNPUBLISHED`). Yani düzeltilmiş metin yayında değil; yayındaki metin düzeltme öncesi sürüm. Site yayına alınırsa aynı başlık iki URL üretir (kanonik/SEO çakışması). Düzeltme mevcut yazının **üzerine** yazılmalı, yeni kayıt açılmamalıydı.

---

## KÖŞE 1 — T0 BASELINE (14 Ağustos 2026)

**Elma-elma kuralı:** T+90 ölçümü aynı araçlarla yapılacak — Wix API (yapısal), doğrudan HTTP (erişilebilirlik), GSC/GA4 (trafik — **henüz bağlı değil**).

### Tip A — gerçek ölçüm
| Metrik | T0 değeri | Araç |
|---|---|---|
| Site kamuya erişilebilir mi | **Hayır** (404 / Draft) | HTTP + Wix API |
| Yayınlanmış blog yazısı (kamuya açık) | **0** | site yayında değil |
| Yayınlanmış blog yazısı (Wix içi statü) | **1** | Wix Blog API |
| Yayınlanmamış blog yazısı (hazır, bekleyen) | **5** (1'i mükerrer) | Wix Blog API |
| Site dili sayısı | **1** (tr) · hedef 4 | Wix API |
| Organik trafik / ay | **ölçülemiyor — GSC/GA4 bağlı değil** | — |
| Dönüşüm (form/sorgu/telefon) | **ölçülemiyor — tracking yok** | — |
| Anahtar kelime sıralaması | **ölçülemiyor** (site indekslenemez, yayında değil) | — |

> §0.1 gereği boş bırakıldı. **Uydurma baseline yok.** Trafik/dönüşüm/sıralama T+90'da anlamlı olabilmesi için önce (a) site yayını, (b) GSC + GA4 bağlantısı gerekir. Bu ikisi yapılmazsa üçgen T+90'da **kapanamaz** — ve o zaman "şu kadar büyüttük" denemez.

### Tip B — gözlem bandı (delta hesabına girmez)
| Boyut | T0 bandı | Not |
|---|---|---|
| İçerik envanteri (hazır ama yayınlanmamış) | **Güçlü** | 5 blog + Hakkımızda v0.7 + ~70 ürün metni + Yürüme Analizi v0.2 + KVKK politikası |
| Kimlik zemini | **Güçlü** | KKK kurulmuş (renk/tipografi/değer seti/tagline kilitli), logo park |
| Uyum (compliance) zemini | **Orta** | TİTCK yeşil kuşak mimarisi kurulu; avukat kapısı hâlâ açık |
| Kamuya görünür dijital varlık | **Kritik** | Site 404 · asıl alan adı bakım sayfası · 29 Haz'dan bu yana değişmedi |
| Ölçüm altyapısı | **Kritik** | GSC/GA4 yok — Growth Faz 1 hedefi, henüz açılmadı |
| Çok dillilik (TR/EN/AR/RU) | **Kritik** | 1 dil; döviz/yurtdışı hasta hedefinin (Kuzey Yıldızı #3) taşıyıcısı yok |

---

## KÖŞE 2 — T0 TAHMİN (Strateji) — `[AÇILMADI]`

Tahmin köşesi **bilerek boş.** Tahmin, baseline'ın üstüne kurulur; kamuya görünür baseline sıfırken "%X artış" tahmini anlamsızdır — sıfırdan her şey sonsuz artıştır, bu kanıt değil gösteridir.

**Açılma koşulu:** site yayına girer + GSC/GA4 bağlanır → ilk 30 günün gerçek verisi T0 olur → Strateji o zaman 90 günlük gerekçeli tahmini yazar (`[tahmin]` etiketli, taahhüt değil).

---

## KÖŞE 3 — T+90 GERÇEK — `[BEKLİYOR]`

**Tetikleyici tarih:** site yayın tarihi + 90 gün. Site yayınlanmadığı için sayaç **başlamadı**.
Bugünden takvime konan tek şey: **her ayın ilk oturumunda "site yayında mı?" kontrolü** — sayaç ancak "evet" ile başlar.

---

## KAPANIŞ TABLOSU (henüz kapanmadı)

| Metrik | Tip | T0 Baseline | T0 Tahmin | T+90 Gerçek | Delta |
|---|---|---|---|---|---|
| Site erişilebilirliği | A | Hayır (404) | — | — | — |
| Kamuya açık içerik sayısı | A | 0 | — | — | — |
| Organik trafik/ay | A | *(ölçülemedi)* | — | — | — |
| Dönüşüm/ay | A | *(ölçülemedi)* | — | — | — |
| İçerik envanteri | B | Güçlü | — | — | (band) |
| Kamuya görünür varlık | B | Kritik | — | — | (band) |

**Kanıt Kartı durumu:** üretilemez. Tip A delta yok. *(Dürüstlük kuralı: ölçülmemiş = kartta yok.)*

---

## ÖĞRENME NOTU (OS'a geri besleme)

Bu üçgenin ilk çalıştırması **tahmin kalibrasyonu değil, bir kör nokta** ortaya çıkardı:

> **Teslim ≠ üretim.** OS'un beş halkası da (Keşif→Strateji→Metin→İçerik→Growth) "çıktı üretildi mi?" sorusunu soruyordu. Hiçbiri **"çıktı hedef kitleye ulaştı mı?"** diye sormuyordu. Denetmen 9 mercekten bakıyor — hiçbiri erişilebilirlik değil.

**Kapı önerisi (Denetmen'e 10. mercek):** *Erişilebilirlik.* Dışarı çıktığı iddia edilen her teslim için tek soru: **"Bunu bugün, hesabı olmayan bir yabancı görebiliyor mu? Kanıt?"** Cevap URL + statü kodu olmalı; "yükledim" cevap değildir. Bu mercek olsaydı bulgu 30 Temmuz'da çıkardı, 14 Ağustos'ta değil.

---

## GÜNCELLEME — 15 Ekim 2026 (Growth Ajanı — gelişim paketi sırasında)

**Durum değişti: site artık yayında (Published, 21 Tem'den beri, custom domain) ve GSC `VALID`+`READY`.** 14 Ağustos'taki "404/Draft" tablosu artık geçerli değil — o satırlar silinmedi (tarihsel kayıt), bu güncelleme üstüne eklenir.

### Tip A — bugün ilk kez çekilen gerçek arama performansı (GSC Site Readiness API, `search-analytics`)
**Pencere: 15 Eylül – 12 Ekim 2026 (28 gün, Google'ın "son günler eksik olabilir" uyarısıyla).**

| Metrik | Değer |
|---|---|
| Toplam tıklama | **69** |
| Toplam gösterim | **2.078** |
| CTR | **%3,3** |
| Ortalama pozisyon | **5,28** |

**Sorgu kırılımı (ilk 20, tıklamaya göre):** İlk 4 sorgu — *"özgür protez"* (19 tık, poz 1,3) · *"özgür ırmak protez"* (12 tık, poz 1,3) · *"özgür ırmak"* (7 tık, poz 2,5) · *"özgür ırmak protez ve ortez merkezi"* (5 tık, poz 1,3) — **toplam 43 tıklama, hepsi marka-adı sorgusu.** Jenerik/bilgi-niyetli sorgularda tek olumlu sinyal: *"ortez protez merkezi"* (1 tık, 8 gösterim, poz 4,75) — marka-dışı bir sorguda ilk sayfadayız. Buna karşılık *"ayak protez fiyatları"* (poz 45,6) · *"ayak protezi"* (poz 22,3) · *"ayak protez"* (poz 14,5) gibi jenerik sorgularda görünürlük yok denecek kadar zayıf, 0 tıklama. İlk 20 sorgunun toplamı 46 tıklama — kalan ~23 tıklama 20'den uzun kuyrukta, bu oturumda tek tek görülmedi.

**Okuma:** Site şu an **marka-bilinirliği olan kişiler tarafından bulunuyor, yeni talep tarafından değil.** Rakip kıyaslamasının (28 Eylül) "4 blog yazısı vs Proklinik ~230 sayfa" bulgusu burada sayısal karşılığını buluyor — jenerik/bilgilendirici sorgularda pratikte yokuz. Bu, aşağıdaki Growth paketindeki içerik-hacmi önceliğinin kanıtı (bkz. `raporlar/ozgur-irmak-growth-gelistirme-2026-10-15.md`).

### Neden hâlâ "T0 Baseline KAPANDI" diyemeyiz
- **GA4 bağlı değil** (bugün `GetSiteContext` Apps listesinde "Google Analytics" yok) → dönüşüm/form-WhatsApp-telefon teması hâlâ ölçülemiyor.
- **STATIC_PAGE SEO verisi 14 Ekim'de geri dönmüş** (checkup 15 Eki) → title/description/schema katmanı kararsız; bu pencerenin SONUNA denk gelen 1-2 gün bu dalgalanmayı taşıyor olabilir, tam temiz bir pencere değil.
- Bu yüzden: **arama performansı (Tip A) artık var ve gerçek** — ama "T0 Baseline KAPANDI" ilanı GA4 bağlanıp + STATIC_PAGE kararlılığı teyit edilince yapılır. O zamana kadar bu sayılar **"ilk gerçek ölçüm, taşınan referans"** statüsünde — T+90 sayacı hâlâ başlamadı.

---
*T0 Baseline · 14 Ağu 2026 (orijinal) + 15 Eki 2026 güncellemesi · Fox/Growth Ajanı · Ölçüm araçları: Wix API (GetSiteContext, GSC Site Readiness/search-analytics). GA4 hâlâ bağlı değil.*
