# Kanıt Üçgeni — Ölçüm Kapanış Döngüsü
*Marka Bulutu OS'un kanıt motoru. Baseline → Tahmin → Gerçek üçgenini kapatır. "Şu kadar büyüttük" iddiasının sayısal zemini — Kuzey Yıldızı: kanıtlanabilir etki → marka değeri → premium fiyat.*

---

## NEDEN VAR (kanıt)

Ölçüm kapanışı sistemin en çok ertelenen ipliğiydi: Strateji Ajanı Faz 3 "Ölçüm Kapanışı (Ekim 2026)", Keşif Faz 3 "Karşılaştırmalı Benchmarking", İçerik Faz 3 "Performans Döngüsü", Growth Faz 1 "Tracking Altyapısı", Branding Faz 3 "Kimlik Tutarlılık Ölçümü" — **hepsi aynı üçgeni beş ayrı yerden tarif ediyordu ama mekanizma yoktu.** Bu şablon o mekanizmadır.

Üçgen kapanmazsa OS bir hizmet olarak kalır, satılabilir kanıta dönüşmez. Kapanınca her müşteri bir **kanıt kartına** dönüşür (satış kapısı + lisans katmanı yakıtı).

---

## ÜÇ KÖŞE

```
                    T0 · BASELINE (Keşif & Denetim)
                    "Bugün marka nerede?"
                    Tip A ölçüm + Tip B gözlem bandı
                         /                    \
                        /                      \
       T0 · TAHMİN (Strateji)  ─────────  T+90 · GERÇEK (Growth/ölçüm)
       "90 gün sonra nereye?"              "90 gün sonra gerçekte nerede?"
       hedef + gerekçe + benchmark          baseline'a karşı delta
```

### Köşe 1 — T0 BASELINE (Keşif & Denetim kurar)
Keşif raporundaki ölçümler bu köşenin verisidir. Her metrik **Tip A / Tip B** etiketli (§0.1):
- **Tip A (gerçek ölçüm):** organik trafik, CVR, DA, sıralama, engagement oranı, hasta sorgusu hacmi — GA4/GSC/platform verisi. Sayısal kaydedilir.
- **Tip B (gözlem):** site yapısı, CTA var/yok, kanal tutarlılığı — niteliksel band (Güçlü/Orta/Zayıf/Kritik). Delta hesabına GİRMEZ, yön göstergesi olarak izlenir.
- **Tip A yoksa:** "baseline kuruldu, performans ölçümü tracking bağlanınca" — üçgen T+90'da gerçek Tip A ile kapanır. (Growth Faz 1: önce tracking açığını kapat.)

### Köşe 2 — T0 TAHMİN (Strateji kurar)
Strateji belgesindeki her ana hamle için 90 gün sonrası hedef. **Uydurma değil, gerekçeli:**
- Metrik + mevcut baseline + hedef + **dayanak** (benchmark `puanlama-rubrigi.md` Bölüm 8 / sektör gerçeği / muhafazakâr-orta-agresif aralık).
- Örn: "Organik trafik: baseline 1.200/ay → hedef 1.700/ay (+%40), dayanak: schema + GEO içeriği healthcare AI Overview %88 kapsama; muhafazakâr +%25 / agresif +%60."
- Tahmin **açıkça tahmindir** — `[tahmin]` etiketli, taahhüt değil (Anayasa §11.5).

### Köşe 3 — T+90 GERÇEK (Growth/ölçüm kapatır)
90 gün sonra aynı metrikler yeniden ölçülür (aynı araç, aynı tanım — elma-elma):
- Baseline'a karşı **gerçek delta**. Tip A zorunlu — Tip B gözlem delta sayılmaz.
- Tahmin tuttu mu? Sapma varsa **neden** (dış faktör / uygulama eksiği / yanlış hipotez).

---

## KAPANIŞ TABLOSU (üçgenin çıktısı)

| Metrik | Tip | T0 Baseline | T0 Tahmin `[tahmin]` | T+90 Gerçek | Delta | Tahmin tuttu mu? |
|---|---|---|---|---|---|---|
| Organik trafik/ay | A | 1.200 | 1.700 (+%40) | — | — | — |
| Dönüşüm (form/sorgu) | A | 18/ay | 28/ay | — | — | — |
| Marka sesi tutarlılığı | B | Zayıf | Orta | — | (band) | — |
| ... | | | | | | |

**Öğrenme notu (zorunlu):** Tahmin sistematik olarak yüksek/düşük mü çıkıyor? Hangi hamle tuttu, hangisi tutmadı? Bu, bir sonraki müşterinin tahminini kalibre eder — üçgen tek seferlik değil, **öğrenen bir döngü**.

---

## KANIT KARTI (üçgenin satılabilir çıktısı)

Üçgen kapanınca Fox tek sayfalık **Kanıt Kartı** üretir (`pdf-motoru.py`, soc-mavi):
- Müşteri + sektör + süre (90 gün)
- 3 en güçlü Tip A delta (baseline → gerçek, görsel bar)
- Bir cümle hikâye ("X ayında organik hasta sorgusunu %Y artırdık")
- **Dürüstlük kuralı:** yalnızca Tip A gerçek delta kartlaşır. Ölçülmemiş = kartta yok. Uydurma delta = Denetmen 8. mercek DUR + güven kaybı + Kuzey Yıldızı ihlali.

Kanıt Kartı hem yeni müşteriye değer kanıtı (satış kapısı) hem lisans/ürünleştirme katmanının referansı.

---

## SORUMLULUK & AKIŞ

| Aşama | Sahip | Ne zaman |
|---|---|---|
| T0 Baseline verisi | Keşif & Denetim | Proje başı (denetim raporuyla) |
| T0 Tahmin | Strateji | Strateji belgesiyle |
| Tracking kurulumu | Growth | Proje başı (yoksa önce bu) |
| T+90 Gerçek ölçüm | Growth (+ Keşif audit aracı) | Teslimden 90 gün sonra |
| Kapanış tablosu + Kanıt Kartı | Fox (sentez) + Denetmen (doğrula) | T+90 |

**Tetikleyici:** Proje teslimi anında Fox takvime "T+90 ölçüm" koyar (bekleyen görev). Orkestrasyon §6 Filo Senkronizasyonu'na bağlı — vaka dersleriyle aynı anda kapanır.

---

## DİSİPLİN
- **§0.1 kutsal:** Sadece Tip A delta üçgeni kapatır. Tip B yön gösterir, sayı olmaz.
- **Elma-elma:** T0 ve T+90 aynı araç + aynı metrik tanımı. Araç değişirse delta geçersiz.
- **Tahmin ≠ taahhüt:** T0 tahmin `[tahmin]` etiketli; müşteriye garanti olarak sunulmaz.
- **Kademe 1:** Ölçüm/kayıt geri alınabilir iç iş. Kanıt Kartı müşteriye giderse Kademe 2 (Ayhan onayı).

---
*Kanıt Üçgeni v1 · Marka Bulutu OS · 28 Temmuz 2026 · Fox · Beş ajanın Faz 3 ölçüm ipliğini tek mekanizmada birleştirir*
