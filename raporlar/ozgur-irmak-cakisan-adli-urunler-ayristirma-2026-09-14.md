# Özgür Protez — Çakışan Adlı Ürünlerin Teknik Ayrıştırılması
**Tarih:** 14 Eylül 2026 · **Site:** ÖzgürProtez (Draft) · **Talimat:** Ayhan —
"isimleri birebir benzeyen ürünlerin özelliklerini üretici sitelerinden bularak
özelliklerine göre yazılarını güncelle."

> Bu iş, aynı gün yapılan marka temizliğinin (bkz. `ozgur-irmak-urun-aciklamalari-marka-temizligi-2026-09-14.md`)
> doğrudan devamıdır: marka adları çıkınca ayırt edicilik açığı ortaya çıktı.
> **Ayrıştırma markayla değil özellikle yapıldı** — model adları geri konmadı.

---

## 1 · Sonuç
| | |
|---|---|
| Çakışan ad grubu | 4 |
| Etkilenen ürün | 15 (14 birebir çakışan + 1 yakın çakışan) |
| Açıklaması yeniden yazılan | 15 |
| Adı düzeltilen | 1 (yanlış cihaz kategorisi) |
| Başarısız yazma | 0 |
| Marka sızıntısı doğrulaması | Ottobock · Össur · Genium · Stumble → **0 eşleşme** |

---

## 2 · Yöntem ve kural
1. Her ürünün **hangi cihaz olduğu** görsel dosya adından okundu (ör. `...-3b5-4-genium-x4-01.png`).
2. Teknik veri yalnız **üreticinin kendi sitesinden** (ottobock.com / ossur.com) alındı.
3. **Doğrulanamayan veri yazılmadı** — yumuşatılmadı, çıkarıldı (Anayasa: medikalde uydurma
   sıfır toleransı). Bulunamayanlar §5'te listeli.
4. Üretici kaynaklı her sayı "üreticinin verilerine göre" ibaresiyle hedgelendi.
5. Ayırt edici özellik **ilk iki cümlede** verildi — kullanıcı listede ayrımı görebilsin diye.

---

## 3 · Grup A — "Mikroişlemcili Diz Eklemi" (6 ürün, birebir aynı ad)

| slug | Cihaz | Yazıya giren ayırt edici özellik |
|---|---|---|
| `camo-backpack` | Genium X4 | IP68 tam su geçirmez (tatlı/klor/tuzlu) · **mobilite 2–4, 150 kg'a kadar** · sensör 100 Hz · 5 hareket modu · batarya 5 güne kadar · öngörülen ömür 6 yıl |
| `i-m-a-product-11` | Rheo Knee | **Manyetoreolojik (MR) sıvı** teknolojisi · **K2–K3, düşük–orta aktivite** · azami 136 kg |
| `canvas-backpack` | Navii | MR aktüatör · **IP68'in ötesinde: çamur ve kuma da dayanıklı** · **batarya 72 saat** · K2–K4 · mekanik kilit |
| `genium` | Genium (3B1-3) | **IP67 — hava koşullarına dayanıklı ama suya daldırılamaz** · IMU + zemin tepki kuvveti · 5 hareket modu · Bluetooth · karbon gövde |
| `kenevo` | Kenevo | **Rehabilitasyon odaklı, düşük–orta mobilite** · gelişmiş takılma algılama · **uyarlanabilir aktivite modları A/B/B+/C** · tekerlekli sandalye modu · **IP54 (daldırılamaz)** |
| `movido` | Movido (3R68) | **HİDROLİK — mikroişlemcili değil** · çocuk · 4 akslı · ~250 g · 145° fleksiyon · ~25 kg / ~45 kg iki versiyon |

**🔴 Ad düzeltmesi yapıldı — `movido`:** Adı "Mikroişlemcili Diz Eklemi" idi. Üretici sayfası
bunu **hidrolik salınım fazı kontrollü çocuk diz eklemi** olarak tanımlıyor; mikroişlemci yok.
Bu bir üslup tercihi değil, **yanlış cihaz kategorisi beyanıdır** — tıbbi cihaz sayfasında
yanlış cihaz beklentisi doğurur. Ad **"Çocuk Hidrolik Diz Eklemi"** olarak değiştirildi.
Ayhan isterse geri alınabilir (Wix revizyon geçmişi).

Kalan 5 üründe ad aynı bırakıldı — talimat "yazılarını güncelle" idi. Ad önerileri §6'da.

---

## 4 · Grup B, C, D

### Grup B — "Miyoelektrik Çok Eklemli El" (4 birebir + 1 yakın)
| slug | Cihaz | Ayırt edici özellik |
|---|---|---|
| `i-m-a-product-2` | i-Limb Access | **12 otomatik kavrama** · manuel başparmak · giriş seviyesi · hareket kontrolü YOK |
| `i-m-a-product` *(ad: "…(Titanyum)")* | i-Limb Access titanium | 12 kavrama · **titanyum güçlendirmeli parmak** · hareket kontrolü YOK |
| `i-limb-ultra-el` | i-Limb Ultra | **18 otomatik kavrama** · **elektrikli dönen başparmak** (manuel geçersiz kılmalı) · titanyum parmak → taşıma yükü +%50 · hareket kontrolü YOK |
| `i-limb-quantum-el` | i-Limb Quantum | **Hareket Kontrolü (gesture control) — bu modele özgü:** dört yönden birine hareketle 4 kavrama · titanyum parmak · +%50 yük / +%30 kuvvet / +%30 hız |
| `bebionic-hand` | bebionic (8E7) | **14 kavrama ve el konumu** · tripod 36 N / anahtar 26 N · açılma 75 mm · 433 g (S) / 616 g (M) · ömür 5 yıl · otomatik kayma algılama |

### Grup C — "Miyoelektrik Parmak Protezi" (2 ürün)
| slug | Cihaz | Ayırt edici özellik |
|---|---|---|
| `i-m-a-product-3` | i-Digits Access | **12'ye kadar kavrama** · uyumlu (compliant) kavrama · hareket kontrolü YOK |
| `i-m-a-product-4` | i-Digits Quantum | **32'ye kadar otomatik kavrama** · **hareket kontrolü var** (dört yön) |

### Grup D — "Çocuk Koşu Ayağı" (2 ürün)
| slug | Cihaz | Ayırt edici özellik |
|---|---|---|
| `i-m-a-product-6` | Flex-Run Junior | Dikey uyum + verimli enerji dönüşü · **karbon katman esnemesi ağırlık ve darbe düzeyine göre** · seviye/ağırlık değerlendirmeyle belirlenir |
| `1e97-sprinter-junior` | Sprinter Junior (1E97) | **Transtibial (diz altı)** · **15–45 kg** · Paralimpik yetişkin spor protezi temelli · sprint/koşu |

---

## 5 · Doğrulanamadığı için YAZILMAYAN veriler
Aşağıdakiler üretici sitesinde bulunamadı; **tahmin yürütülmedi, metne konmadı**:
- **Genium (3B1-3)** azami kullanıcı ağırlığı ve mobilite derecesi
- **Navii** azami kullanıcı ağırlığı
- **Flex-Run Junior** ağırlık aralığı ve ampütasyon seviyesi
- **i-Limb Access titanium** taşıma yükü artış oranı (%50 değeri yalnız Ultra için doğrulandı)

**Kaldırılan teyitsiz iddia:** `i-m-a-product-6` (Flex-Run Junior) metninde "hem transfemoral
hem transtibial kullanıcılara yöneliktir" yazıyordu. Bu ibare üretici sitesinde doğrulanamadı
(yalnız üçüncü taraf bayi sayfalarında geçiyor) → **çıkarıldı**, yerine değerlendirmeye
bırakan cümle kondu.

---

## 6 · Ayhan'da duran kararlar

**① 🔴 İkinci yanlış cihaz kategorisi — `1c51-taleo-vertical-shock`**
Ürün adı: "Mikroişlemcili  Karbon Protez Ayak" *(çift boşluk da var)*.
Üretici sayfası bunu **aktif kullanıcılar için pasif karbon ayak** olarak tanımlıyor;
elastomer halka ile torsiyon ve dikey şok emer, **mikroişlemci yoktur**. Movido ile aynı
hatanın ikinci örneği. **Kapsam dışıydı, dokunulmadı.** Önerilen ad:
"Şok Emici Torsiyonlu Karbon Protez Ayak". Onay verirsen düzeltilir.
*(Yan veri: üretici sitesinde 22–30 cm beden, azami 150 kg, hava koşullarına dayanıklı.)*

**② Kalan 5 "Mikroişlemcili Diz Eklemi" adı aynı duruyor.** Açıklamalar artık ayrışıyor ama
ürün listesinde/başlıkta hâlâ aynı görünüyorlar. Önerilen adlar:
| slug | Öneri |
|---|---|
| `camo-backpack` | Mikroişlemcili Diz Eklemi (Su Geçirmez, Yüksek Aktivite) |
| `i-m-a-product-11` | Mikroişlemcili Diz Eklemi (Manyetoreolojik, K2–K3) |
| `canvas-backpack` | Mikroişlemcili Diz Eklemi (Su ve Kum Dayanımlı) |
| `genium` | Mikroişlemcili Diz Eklemi (Hava Koşullarına Dayanıklı) |
| `kenevo` | Mikroişlemcili Diz Eklemi (Rehabilitasyon ve Düşük Mobilite) |

Benzer şekilde el protezlerinde: "(12 Kavrama)", "(18 Kavrama)", "(Hareket Kontrollü)",
"(14 Kavrama)" gibi ekler ayrımı başlıkta görünür kılar. **Tek bir "evet" yeter.**

**③ Değişmeyenler:** görsel dosya adları, slug'lar ve SKU alanı hâlâ üretici/rakip adı taşıyor
(önceki raporun §4'ü). Bu iş onlara dokunmadı.

---

## 7 · Kaynaklar
- Genium X4 · Kenevo · Genium · Movido · Taleo Vertical Shock · Sprinter Junior — ottobock.com
- Rheo Knee · Navii · i-Limb Access/Ultra/Quantum · i-Digits Access/Quantum · Flex-Run Junior — ossur.com
- bebionic teknik föyü — ottobock.com

Site **Draft**; hiçbir değişiklik kamuya açık değil, tümü Wix revizyon geçmişinden geri alınabilir.
Bu belge **avukat ya da klinik onayın yerine geçmez**; teknik verilerin envanterle eşleştiği
Özgür Bey tarafından teyit edilmelidir.
