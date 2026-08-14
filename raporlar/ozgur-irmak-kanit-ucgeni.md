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
*T0 Baseline · 14 Ağu 2026 · Fox · Ölçüm araçları: Wix API (GetSiteContext, Blog v3, Stores v3), doğrudan HTTP. GSC/GA4 bağlı değil.*
