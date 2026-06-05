# Marka Bulutu OS — Puanlama Rubriği
*Tüm ajanların ortak ölçüm dili. Müşteriye giden her skorun arkasındaki somut gerekçe. Tekrarlanabilir, savunulabilir, kaynak-bilgili.*

**Sürüm:** v1 · **Yürürlük:** 5 Haziran 2026 · **Sonraki revizyon:** 5 Eylül 2026 (3 ay)
**Statü:** Yaşayan belge — ajanlar arttıkça + kalite algımız yükseldikçe güncellenir.

---

## NEDEN BU BELGE VAR

Denetmen, SOC denetim raporunda iki kritik açık tespit etti:
1. **"Neden konumlandırma 28?"** — Müşteri sorduğunda yanıt yoktu. Puan, ajanın sezgisine bırakılmıştı; tekrarlanabilir değildi.
2. **Skor metodolojisi tanımsız** — Eksik veri nasıl işlenir? Ham skor mu, ayarlı skor mu? İki müşterinin "28" ve "35"i kıyaslanabilir mi?

Bu belge ikisini de çözer. Her puan bandı **somut, gözlemlenebilir kritere** bağlıdır. Her skor savunulabilir: "28 çünkü şu üç gözlem var."

### DÜRÜSTLÜK NOTU (Anayasa §11.5)
Araştırma net: **endüstri genelinde tek bir standart ağırlık tablosu yoktur.** "İçerik %25, Dönüşüm %20" gibi ağırlıklar firmaların kendi metodolojileridir, evrensel norm değil. Bizim ağırlıklarımız da öyle: **kaynak-bilgili ama özgün.** Müşteriye "endüstri standardı ağırlık" diye sunulmaz; "Marka Bulutu OS metodolojisi, otoriteli benchmarklara dayalı" diye sunulur.

Eşik değerleri (SEO skoru, dönüşüm oranı, engagement vb.) ise gerçek endüstri benchmarklarıdır ve **Bölüm 8'de kaynağıyla** listelenir.

---

# BÖLÜM 0 — KULLANIM İLKELERİ (tüm ajanlar)

### 0.1 Eksik Veri Kuralı + İki Katman Kanıt (v1.1 — 5 Haz 2026, Ayhan düzeltmesi)

**Çözülen açık (5 Haz):** §0.1 v1 yalnızca "hiç gözlemlenemeyen" kategoriyi N/A yapıyordu. Ama "gözlemlenen ama performansı ölçülemeyen" kategorileri (örn. Dönüşüm: site açıldı, CTA görüldü — ama gerçek CVR/trafik verisi yok) yine de sayısal puanladık (Towdoo Dönüşüm 42, Marka&Güven 58). Sonuç: **altyapı gözlemi, performans ölçümü gibi okundu — sahte kesinlik.** Düzeltme: her puan, hangi kanıt tipine dayandığını beyan eder.

**Tip A — Ölçülmüş / Doğrulanmış veri → sayısal puan VERİLEBİLİR**
Gerçek metrik veya doğrulanmış dış kaynak: CVR (Analytics), organik trafik (GSC), DA (Ahrefs/Moz), PageSpeed (Lighthouse), Core Web Vitals, doğrulanmış platform puanı (örn. Trendyol 4.3/5 — 619 yorum). Sayı, gerçek bir ölçümü temsil eder.

**Tip B — Gözlem / Altyapı değerlendirmesi → sayısal puan VERİLMEZ**
Site yapısı, varlık/yokluk, kalite gözlemi (CTA var mı, sosyal kanıt taşınmış mı, hero değer önerisi içeriyor mu, blog kaç ay önce). Bunlar gerçek **gözlem** ama performans değil — **hazırlık/altyapı.** Niteliksel raporlanır: **Güçlü / Orta / Zayıf / Kritik açık** + "performans ölçümü bekliyor (kaynak: GSC/Analytics/…)".

**Kurallar:**
1. Bir kategori yalnızca **Tip B** kanıta dayanıyorsa → **sayısal puan verilmez.** Niteliksel değerlendirme + eksik performans verisi açıkça listelenir.
2. **Genel skor yalnızca Tip A verisi olan kategorilerden** hesaplanır (normalizasyon: kalan ağırlıklar 1.0'a ölçeklenir). **Hiç Tip A yoksa → genel sayısal skor verilmez;** "Baseline kuruldu — performans skoru [GSC/Analytics/…] bağlanınca hesaplanacak" yazılır.
3. **Hiç gözlemlenemeyen** kategori (bot koruması, erişim yok) → eskisi gibi "N/A — Ölçülemedi", skora hiç girmez.
4. Eksik veri ASLA varsayım puanı eklemez/çıkarmaz (SOC 39.75→48 hatası tekrarlanmaz).
5. Bir kategori hem Tip A hem Tip B içerebilir → Tip A kısmı sayısal, Tip B kısmı niteliksel; ayrı gösterilir, karıştırılmaz.

**Neden kritik (Kuzey Yıldızı bağı):** Hedefimiz "markalarda gerçek etki göster." Tip B'yi sayısallaştırırsak before/after **sahte** olur (42→65 deriz ama ikisi de gözlem, gerçek metrik değil). Tip A/B ayrımı, "iyileştirdik" dediğimizde sözün gerçek bir ölçüme dayanmasını garanti eder — ürünün temel vaadi budur.

### 0.2 Her Skor Kanıta Bağlanır
Hiçbir puan gerekçesiz verilmez. Her kategori skorunun yanında **en az bir somut gözlem** bulunur: "Hero başlığı değer önerisi içermiyor" / "3 sayfada CTA yok" / "blog son güncelleme 8 ay önce". Tahminse "tahmin" denir.

### 0.3 5 Seviyeli Master Skala (Bölüm 1) Her Yerde Geçerli
Tüm ajanlar, tüm kategoriler aynı 5 bandı kullanır. Bu, müşterinin "Keşif'te 55 aldık, Strateji'de 70" gibi karşılaştırma yapabilmesini sağlar.

### 0.4 Müşteriye Gösterim
Her ajan çıktısının sonunda **kendi rubriğine göre bir Kalite/Olgunluk Skoru** bulunur. Müşteri bu skoru görür. Skor, satış aracı (öncesi) + etki kanıtı (sonrası) işlevi görür.

---

# BÖLÜM 1 — MASTER SKOR SKALASI (ortak)

| Skor | Not | Etiket | Anlam |
|---|---|---|---|
| **85–100** | A | Mükemmel | Sınıfının en iyisi. Rakip karşısında belirgin üstünlük. Korunması gereken güç. |
| **70–84** | B | İyi | Sağlam temel, net fırsat alanları. Optimizasyonla A'ya çıkar. |
| **55–69** | C | Orta | Temel var ama zayıf. Ciddi boşluklar. Yapısal çalışma gerekiyor. |
| **40–54** | D | Yetersiz | Büyük revizyon gerekli. Mevcut hâli marka değerine zarar veriyor. |
| **0–39** | F | Kritik | Yok sayılabilir veya aktif zarar veriyor. Sıfırdan inşa. |

**Bileşik skor** = Σ (kategori skoru × ağırlık), eksik veri + iki katman kuralıyla (§0.1) normalize. **Yalnızca Tip A (ölçülmüş/doğrulanmış) verisi olan kategoriler bileşik skora girer.** Tip B (gözlem/altyapı) kategoriler niteliksel raporlanır, sayıya çevrilmez. Hiç Tip A yoksa bileşik sayısal skor verilmez. Yorumda harf notu + tek cümle.

---

# BÖLÜM 2 — KEŞİF & DENETİM AJANI RUBRİĞİ

## 2.1 Genel Çerçeve — 7 Kategori, Her Biri 5 Seviye

### Ağırlıklar (varsayılan — bağlama göre Bölüm 2.2'de değişir)
| Kategori | Ağırlık | Ölçtüğü |
|---|---|---|
| İçerik & Mesaj | %25 | Değer önerisi, ikna, hikâye, marka sesi |
| Dönüşüm | %20 | CTA, form, güven sinyali, sürtünme |
| Görünürlük (SEO) | %15 | Teknik + içerik SEO, görünürlük |
| Konumlandırma | %15 | Farklılaşma, kategori, rakip farkındalığı |
| Marka & Güven | %10 | Tutarlılık, görsel kimlik, sosyal kanıt |
| Onur & Temsil | %10 | (İnsan-merkezli/sosyal etki) güç vs. acıma |
| Büyüme & Strateji | %5 | Fiyat, kanal, sadakat, genişleme |

> Onur & Temsil yalnızca insan-merkezli/sosyal etki markalarında aktiftir. Değilse ağırlığı Marka & Güven'e eklenir (%20).

---

### KATEGORİ 1 — İÇERİK & MESAJ

| Skor | Gözlemlenebilir Kriter |
|---|---|
| **85–100** | Değer önerisi ilk 5 saniyede net. Müşteri dili (verbatim) kullanılıyor. Her sayfa tek net fikir taşıyor. Hikâye + somut fayda dengeli. Fayda>özellik. |
| **70–84** | Değer önerisi net ama bazı sayfalar zayıf/jenerik. Müşteri dili kısmen var. Akış çoğunlukla iyi. |
| **55–69** | Değer önerisi var ama bulanık — "ne yapıyorsunuz?" sorusu birkaç saniye sürüyor. Şirket-merkezli dil ağır basıyor. |
| **40–54** | Değer önerisi belirsiz. Jenerik/buzzword dil. Mesaj dağınık, sayfa başına fikir karışık. |
| **0–39** | Ne yaptığı anlaşılmıyor. Değer önerisi yok. Boş/placeholder içerik veya alakasız mesaj. |

**Kanıt toplama:** Hero başlığını oku, 5-saniye testi uygula. İlk 3 sayfada değer önerisi tutarlı mı? Müşteri context'indeki verbatim cümleler sitede geçiyor mu?

---

### KATEGORİ 2 — DÖNÜŞÜM

| Skor | Gözlemlenebilir Kriter |
|---|---|
| **85–100** | Her sayfada net, tek birincil CTA (eylem fiili + kazanç). Form ≤5 alan. Güçlü sosyal kanıt (5+ referans/video). Sürtünme minimum. |
| **70–84** | CTA net ama bazı sayfalarda zayıf/çoklu. Form makul. Sosyal kanıt var ama sınırlı (1-4 referans). |
| **55–69** | CTA var ama belirsiz fiil ("Tıkla", "Daha fazla"). Form uzun (6+ alan) veya sosyal kanıt zayıf. |
| **40–54** | CTA yanlış hedefe götürüyor veya yok. Sosyal kanıt yok. Form sürtünmeli. |
| **0–39** | Dönüşüm mekanizması yok. CTA yok veya tamamen yanlış kitleye hitap ediyor. İletişim yolu belirsiz. |

**Benchmark bağı (Bölüm 8):** Dönüşüm oranı verisi varsa sektör ortalamasıyla kıyasla (sağlık %2-4, B2B %2-4, moda %1-2). CTA tek kelime değişimi %10-30 fark yaratır (Invespcro).

---

### KATEGORİ 3 — GÖRÜNÜRLÜK (SEO)

| Skor | Gözlemlenebilir Kriter |
|---|---|
| **85–100** | Teknik sağlık 80+. Core Web Vitals "iyi" (LCP<2.5s). Kırık sayfa yok. Düzenli, search-intent uyumlu içerik. Meta yapısı tam. |
| **70–84** | Teknik sağlık 60-80. Birkaç optimizasyon açığı. İçerik var ama düzensiz. Çoğu meta tam. |
| **55–69** | Teknik sağlık 50-60. Bazı kırık sayfalar/hız sorunu. İçerik seyrek. Meta eksikleri. |
| **40–54** | Teknik sağlık <50. Çok sayıda kırık sayfa. İçerik neredeyse yok (≤2 yazı). Meta dağınık. |
| **0–39** | Site indekslenmiyor/erişilemiyor. Yapısal SEO yok. İçerik yok. |

**Benchmark bağı (Bölüm 8):** Teknik sağlık skoru (Semrush/TrackSEO), PageSpeed (Lighthouse), Core Web Vitals (Google eşikleri), DA (Moz — *karşılaştırmalı, rakiple ölç*). Not: keyword density sıralama faktörü DEĞİL (Google/Mueller) — search intent uyumuna bak.

---

### KATEGORİ 4 — KONUMLANDIRMA

| Skor | Gözlemlenebilir Kriter (April Dunford 5 bileşen temelli) |
|---|---|
| **85–100** | Rekabet alternatifi net, benzersiz özellikler+değer kanıtı açık, hedef müşteri tanımlı, kategori bağlamı keskin. Müşteri kendi diliyle markayı tanımlayabilir. Me-too değil. |
| **70–84** | Konumlandırma çoğunlukla net, 1-2 bileşen zayıf. Farklılaşma var ama her yerde tutarlı vurgulanmıyor. |
| **55–69** | Konumlandırma var ama genel. Farklılaştırıcılar yüzeysel veya rakiple benzer ("biz de yaparız"). Kategori belirsiz. |
| **40–54** | Konumlandırma zayıf/çelişkili. Birden çok kimlik çakışıyor. Farklılaşma yok. |
| **0–39** | Konumlandırma yok. Marka ne olduğu/kime olduğu anlaşılmıyor. Kategori tanımsız. |

**Zayıf konumlandırma sinyalleri (Dunford):** yeni adaylar ne sattığını anlamıyor, uzun satış döngüsü, fiyat baskısı, me-too dil. *(SOC örneği: iki kimlik çakışması = 28 = D bandı.)*

---

### KATEGORİ 5 — MARKA & GÜVEN

| Skor | Gözlemlenebilir Kriter |
|---|---|
| **85–100** | Görsel kimlik tutarlı+premium. Güçlü sosyal kanıt (logo, referans, basın, ödül). Şeffaflık. E-E-A-T sinyalleri güçlü. |
| **70–84** | Görsel kimlik tutarlı. Bazı güven sinyalleri var ama eksik (örn. logo var referans yok). |
| **55–69** | Görsel kimlik dağınık veya güven sinyalleri zayıf. Sosyal kanıt minimal. |
| **40–54** | Görsel tutarsızlık belirgin. Güven sinyali neredeyse yok. |
| **0–39** | Marka kimliği yok/tutarsız. Hiçbir güven sinyali yok. Güvenilmez izlenim. |

**Benchmark bağı (Bölüm 8):** Sosyal kanıt %34'e kadar dönüşüm artışı; 5+ yorum %270 etki; ideal puan 4.2-4.5 (5.0 değil — özgünlük). E-E-A-T'de Trustworthiness en kritik bileşen (Google).

---

### KATEGORİ 6 — ONUR & TEMSİL *(yalnızca insan-merkezli/sosyal etki)*

0-4 ham skala (Nielsen 2024 temelli), 0-100'e ölçeklenir (×25):

| Ham | Skor | Gözlemlenebilir Kriter |
|---|---|---|
| **4** | 100 | Co-creation (topluluğun sesi içerikte), intersectionality, erişilebilirlik (WCAG). Birey özne. |
| **3** | 75 | Özgün temsil, topluluğun sesi dahil. Güç/fail çerçevesi. Acıma yok. |
| **2** | 50 | Görünürlük var ama pasif/yüzeysel. Birey nesne konumunda ama zararlı değil. |
| **1** | 25 | Nötr — engeli/farkı görmezden geliyor. Temsil eksik. |
| **0** | 0 | Inspiration porn / acıma anlatısı / klişe / araçsallaştırma. |

**Kırmızı bayraklar:** "ilham verici" çerçevesi (engelsiz bireyin iyi hissetmesi için), "hobi olarak", "ihtiyaç sahibi" dili, kurban/süper-insan ikiliği. *(SOC: 62 — acıma yok ama kurucu hikâyesi/güç çerçevesi eksik.)*

---

### KATEGORİ 7 — BÜYÜME & STRATEJİ

| Skor | Gözlemlenebilir Kriter |
|---|---|
| **85–100** | Net kanal stratejisi. Fiyat/değer iletişimi düşünülmüş. Email/sadakat sistemi aktif. Genişleme yolu görünür. |
| **70–84** | Strateji çoğunlukla var, 1-2 boşluk (örn. email listesi yok ama kanal net). |
| **55–69** | Temel var ama dağınık. Kanal önceliği belirsiz veya sadakat mekanizması yok. |
| **40–54** | Strateji görünmüyor. Fiyat gizli, kanal karışık, sadakat yok. |
| **0–39** | Hiçbir büyüme altyapısı yok. |

---

## 2.2 BAĞLAM ADAPTASYONLARI (5 sektör)

Her keşif bağlamında ağırlıklar ve ek kriterler değişir. Genel rubrik temel; bağlam üstüne biner.

### A) KLİNİK / SAĞLIK (Darya Dental, Luxmed, Nesa)
**YMYL alanı — güven çıtası yüksek (Google).**

| Kategori | Ağırlık (değişim) |
|---|---|
| Marka & Güven | **%25** (↑ — E-E-A-T kritik, hekim profili, sertifika, hasta yorumu) |
| Dönüşüm | **%25** (↑ — randevu/iletişim, sağlık CVR ort. %2-4) |
| İçerik & Mesaj | %20 |
| Görünürlük (SEO) | %15 (lokal SEO + "yakınımdaki" aramaları) |
| Konumlandırma | %10 |
| Büyüme & Strateji | %5 |
| ~~Onur & Temsil~~ | Marka & Güven'e dahil |

**Ek kriterler:** Hekim/uzman kimliği görünür mü (E-E-A-T Expertise)? Hasta yorumları + öncesi/sonrası (etik sınırda)? Sertifika/akreditasyon? Gizlilik/KVKK güveni?

### B) MODA / PERAKENDE (Towdoo, Ala)
**Görsel-öncelikli + e-ticaret dönüşümü.**

| Kategori | Ağırlık (değişim) |
|---|---|
| Marka & Güven (görsel kimlik) | **%25** (↑ — görsel kalite kritik) |
| İçerik & Mesaj | %20 |
| Dönüşüm | **%20** (moda CVR ort. %1-2) |
| Konumlandırma | %15 |
| Görünürlük (SEO) | %10 |
| Büyüme & Strateji | %10 (↑ — sezonluk, koleksiyon, sadakat) |

**Ek kriterler:** Editorial görsel kalitesi (estetik müfredatı zemini)? Ürün fotoğrafı tutarlılığı? Sezonluk hikâye? Sürdürülebilirlik anlatısı doğru mu (Towdoo: cupro)?

### C) SOSYAL ETKİ / İNSAN-MERKEZLİ (SOC misyon kolu, ampüte içerik)
**Onur temsili en kritik kategori.**

| Kategori | Ağırlık (değişim) |
|---|---|
| Onur & Temsil | **%25** (↑↑ — en kritik) |
| İçerik & Mesaj | %25 |
| Marka & Güven | %15 (şeffaflık, etki ölçümü) |
| Dönüşüm | %15 (bağış/katılım/farkındalık) |
| Konumlandırma | %10 |
| Görünürlük (SEO) | %10 |

**Ek kriterler:** Co-creation var mı? Topluluğun sesi mi yoksa dışarıdan anlatı mı? Etki ölçümü şeffaf mı? Erişilebilirlik (WCAG)? Inspiration porn riski?

### D) KOBİ / HİZMET / DANIŞMANLIK (SOC ticari kolu, B2B)
**Konumlandırma + lokal/niş SEO + referans.**

| Kategori | Ağırlık (değişim) |
|---|---|
| Konumlandırma | **%25** (↑ — farklılaşma B2B'de kritik) |
| İçerik & Mesaj | %20 |
| Dönüşüm | **%20** (B2B lead CVR ort. %2-4) |
| Marka & Güven | %15 (vaka çalışması, referans) |
| Görünürlük (SEO) | %15 |
| Büyüme & Strateji | %5 |

**Ek kriterler:** Vaka çalışması var mı (B2B'de en güçlü kanıt)? Niş otorite içeriği? LinkedIn varlığı (B2B kanalı)? Lead capture sistemi?

### E) E-TİCARET (saf online satış)
**Dönüşüm + ürün sayfası + sepet.**

| Kategori | Ağırlık (değişim) |
|---|---|
| Dönüşüm | **%30** (↑↑ — sepet, ürün sayfası, ödeme akışı) |
| Görünürlük (SEO) | **%20** (ürün/kategori SEO) |
| İçerik & Mesaj | %15 |
| Marka & Güven | %15 (yorum, iade politikası, güvenli ödeme) |
| Konumlandırma | %10 |
| Büyüme & Strateji | %10 (sadakat, e-posta, retargeting) |

**Ek kriterler:** Ürün sayfası kalitesi? Sepet terki azaltma? Yorumlar (5+ = %270 etki)? Ödeme güveni? Mobil dönüşüm?

---

# BÖLÜM 3 — STRATEJİ AJANI RUBRİĞİ

Strateji çıktısının (konumlandırma + mesaj mimarisi + AARRR) kendi kalite skoru. Müşteriye "Strateji Olgunluk Skoru" olarak gösterilir.

| Kategori | Ağırlık | 85-100 (A) | 40-54 (D) |
|---|---|---|---|
| **Konumlandırma Netliği** (Dunford 5 bileşen) | %25 | 5 bileşen de net + keskin kategori | Çelişkili/me-too |
| **ICP & JTBD Tanımı** | %20 | Persona + dört kuvvet + verbatim dil tam | Genel "herkes" tanımı |
| **Rekabet Haritası** | %15 | Direkt+ikincil+dolaylı, her birinin açığı net | Rakip farkındalığı yok |
| **Mesaj Mimarisi** | %20 | Hiyerarşik, kanal-bağımsız tutarlı, kanıtlı | Dağınık, kanıtsız iddia |
| **AARRR Funnel Bütünlüğü** | %15 | 5 aşama da kapsanmış, metrik+aksiyon bağlı | Aşamalar eksik/kopuk |
| **Uygulanabilirlik** | %5 | Somut, önceliklendirilmiş, kaynak-gerçekçi | Soyut, uygulanamaz |

**Kanıt kuralı:** Strateji "rakam uydurmaz" (§11.5). Pazar iddiası → kaynak veya "varsayım" etiketi. AARRR benchmarkları Bölüm 8'den çekilir.

---

# BÖLÜM 4 — GROWTH AJANI RUBRİĞİ

Growth çıktısının (görünürlük/AI-SEO/dönüşüm/topluluk/elde tutma) kalite skoru. "Büyüme Hazırlık Skoru."

| Kategori | Ağırlık | 85-100 (A) | 40-54 (D) |
|---|---|---|---|
| **SEO Uygulama Kalitesi** | %25 | Teknik+içerik+intent uyumu, benchmark-bağlı hedef | Genel tavsiye, eşiksiz |
| **Dönüşüm Optimizasyonu** | %25 | CTA/form/sürtünme somut, A/B planlı, CVR hedefi sektör-bağlı | Belirsiz "iyileştir" |
| **Email & Lead Sistemi** | %20 | Lead magnet + sekans + open rate hedefi (%35+) | Liste/sistem yok |
| **Kanal Stratejisi** | %15 | Müşteri-bağlamına uygun kanal + engagement hedefi | Jenerik "her yerde ol" |
| **Ölçüm & Tracking** | %15 | Baseline + KPI + tracking kurulumu net | Ölçüm yok (kör uçuş) |

**Benchmark zorunluluğu:** Her hedef Bölüm 8'e bağlı (email open %35+ iyi, LinkedIn ER %2.5-4 iyi, Instagram ER %0.6-1.5 iyi). "İyi olsun" değil, "X benchmark'a göre Y hedef".

---

# BÖLÜM 5 — BRANDING AJANI RUBRİĞİ

Branding çıktısının (sözel+görsel kimlik, brand book) kalite skoru. "Marka Kimliği Olgunluk Skoru."

| Kategori | Ağırlık | 85-100 (A) | 40-54 (D) |
|---|---|---|---|
| **Sözel Kimlik** (isim, slogan, ses, ton) | %25 | Ses parmak izine sadık, tutarlı, akılda kalıcı | Jenerik, taklit, tutarsız |
| **Görsel Kimlik** (logo, renk, tipografi) | %25 | Marka kiti tutarlı, premium, ayırt edici | Dağınık, klişe |
| **Brand Book Tamlığı** | %20 | Kullanım kuralları+yanlış kullanım+örnek tam | Eksik, uygulanamaz |
| **Kanal-Arası Tutarlılık** | %20 | Web+sosyal+basılı aynı kimlik | Her kanal farklı |
| **Onur & Temsil (görsel)** | %10 | Güç çerçevesi, gerçek prodüksiyon (AI yüz yok) | Acıma/klişe görsel |

**SOC özel kuralı:** İki register ayrımı (Ayhan Erden iş / Steps On Clouds misyon) korunuyor mu? Marka kiti (marka-kiti.md) ile çelişki var mı?

---

# BÖLÜM 6 — İÇERİK AJANI RUBRİĞİ

İçerik çıktısının (metin+görsel yön) kalite skoru. "İçerik Kalite Skoru." HubSpot Accuracy/Clarity/Completeness + E-E-A-T temelli.

| Kategori | Ağırlık | 85-100 (A) | 40-54 (D) |
|---|---|---|---|
| **Kopya Kalitesi** (netlik/fayda/spesifik) | %25 | Netlik>zekâ, fayda>özellik, spesifik, tek fikir | Buzzword, muğlak, özellik-listesi |
| **Ses Uyumu** | %20 | Müşteri/Ayhan sesine birebir sadık | Jenerik AI sesi |
| **Doğruluk** (E-E-A-T/Accuracy) | %20 | Tüm iddialar kaynaklı, uydurma yok | Uydurma rakam/iddia |
| **Görsel Yön Kalitesi** | %15 | Parmak izine uygun brief, estetik bilinçli | Düz, yönsüz |
| **Onur & Temsil** | %10 | Güç/fail/gündelik gerçeklik | Acıma/ilham pornosu |
| **Teknik** (Türkçe doğruluk, SEO meta) | %10 | Türkçe kusursuz, meta tam | Türkçe karakter hatası |

**Üretim çıktıları (PPTX/Excel) için ek:** Brief'e sadakat, marka kimliği (renk/tipografi), müşteriye sunulabilirlik. *(Bkz. İçerik Ajanı Kol 3.)*

---

# BÖLÜM 7 — MÜŞTERİ RAPORLARINDA GÖSTERİM

Her ajan, çıktısının sonunda kendi skorunu **standart blokla** sunar:

```
─────────────────────────────────
[AJAN ADI] KALİTE SKORU: XX/100 — [Not]
─────────────────────────────────
Kategori 1: XX/100 — [tek cümle gerekçe + kanıt]
Kategori 2: XX/100 — [tek cümle gerekçe + kanıt]
...
Ölçülemeyen: [kategori] — [sebep]
─────────────────────────────────
Bu skor [tarih] baseline'ıdır. [Sonraki ölçüm: ...]
```

**Disiplin:** Skor = satış kapısı (öncesi düşük → değer göster) + etki kanıtı (sonrası yüksek → "şu kadar büyüttük"). Kuzey Yıldızı: kanıtlanabilir etki → marka değeri → premium fiyat.

---

# BÖLÜM 8 — BENCHMARK REFERANS TABLOSU (kaynaklı)

Eşik değerleri gerçek endüstri benchmarklarıdır. Ağırlıklar bizim metodolojimiz (Bölüm 0 dürüstlük notu).

| Metrik | Düşük | Orta | İyi | Mükemmel | Kaynak |
|---|---|---|---|---|---|
| Teknik SEO skoru | <50 | 50-60 | 60-80 | 80+ | Semrush/TrackSEO |
| PageSpeed (mobil) | <50 | 50-69 | 70-89 | 90+ | Google Lighthouse |
| LCP (yükleme) | >4s | 2.5-4s | <2.5s | <1.5s | Google Core Web Vitals |
| INP (etkileşim) | >500ms | 200-500ms | <200ms | <100ms | Google (FID yerine) |
| CLS (stabilite) | >0.25 | 0.1-0.25 | <0.1 | <0.05 | Google |
| Domain Authority | <20 | 20-30 | 30-50 | 50+ | Moz (*rakiple kıyasla*) |
| Sağlık CVR | <%1 | %1-2 | %2-4 | %4+ | Invespcro |
| Moda/perakende CVR | <%0.5 | %0.5-1 | %1-2 | %2.5+ | Invespcro/DynamicYield |
| B2B lead CVR | <%1 | %1-2 | %2-4 | %4+ | Ruler Analytics |
| Form alanı (optimal) | 6+ | 5 | 3-4 | 3 | Forrester 2024 |
| Email open rate | <%25 | %25-35 | %35-45 | %45+ | MailerLite 2024-25 |
| Email click rate | <%1 | %1-2 | %2-3 | %3+ | MailerLite 2024-25 |
| LinkedIn ER | <%1 | %1-2.5 | %2.5-4 | %4+ | Hootsuite 2024-25 |
| Instagram ER | <%0.3 | %0.3-0.6 | %0.6-1.5 | %1.5+ | Buffer/Hootsuite 2025 |
| Sosyal kanıt | Yok | 1-4 yorum | 5-20 yorum | 20+ +video | SmashBalloon |
| İdeal yıldız puanı | 5.0 (şüpheli) | <4.0 | 4.2-4.5 | 4.2-4.5 | WiserReview |

**Çerçeveler:** April Dunford (Obviously Awesome — konumlandırma) · Google E-E-A-T (içerik kalitesi, Trustworthiness en kritik) · HubSpot Accuracy/Clarity/Completeness (içerik) · Nielsen 2024 Disability-Inclusive Marketing (onur temsili) · AARRR (Pirate Metrics — büyüme).

**Uyarılar:**
- DA/Authority **karşılaştırmalı** — mutlak değil, sektör rakibiyle ölç.
- Instagram ER 2024→2025 %26 düştü; pasif etkileşim (kaydet/DM) kamuya açık metriğe girmiyor — düşük görünüm yanıltıcı olabilir.
- Keyword density sıralama faktörü **değil** (Google/Mueller) — search intent uyumu esas.
- Disability temsilinde GLAAD eşdeğeri tek otorite belge **henüz yok**; Nielsen 2024 en yakın referans.

---

# BÖLÜM 9 — GÜNCELLEME TAKVİMİ

| Sürüm | Tarih | Tetikleyici | Kapsam |
|---|---|---|---|
| **v1** | 5 Haz 2026 | İlk kuruluş | 5 ajan rubriği + 5 bağlam + benchmark |
| **v1.1** | 5 Haz 2026 | Ayhan düzeltmesi — Towdoo dönüşüm puanı | §0.1 İki Katman Kanıt: Tip A (ölçülmüş→sayısal) / Tip B (gözlem→niteliksel). Gözlemi performans gibi sayısallaştırma açığı kapatıldı. |
| **v2** | 5 Eyl 2026 | 3 ay sonra (planlı) | Ajan artışı + kalite algısı yükselişi + saha verisi |

**v2'de gözden geçirilecekler:**
- Yeni ajanlar (İş Katmanı: Satış/Finans/Hukuk) için rubrik eklenir mi?
- Gerçek müşteri verisiyle eşikler kalibre edilir (SOC + Darya + Towdoo baseline'ları).
- Ağırlıklar saha sonuçlarına göre ayarlanır.
- Kalite çıtası yükseldikçe "85-100 A" tanımı sıkılaşır (bugünün A'sı yarının B'si olabilir).
- Bağlam sayısı artar mı (yeni sektörler)?

**Disiplin:** Bu belge yaşayan. Her ajan kendi rubriğini kullanırken boşluk/tutarsızlık görürse Fox'a bildirir; ara güncelleme yapılabilir. Planlı revizyon 3 ayda bir.

---

*Marka Bulutu OS — Puanlama Rubriği v1.1 · 5 Haziran 2026 · Fox*
*Kaynak araştırması: Semrush, Moz, Google, Invespcro, Ruler Analytics, MailerLite, Hootsuite, April Dunford, HubSpot, Nielsen. Ağırlıklar SOC metodolojisi (kaynak-bilgili, endüstri standardı değil — §11.5).*
