# Marka Denetim Raporu v2 — DELTA — Syla Atelier

> **🔒 İÇ RAPOR — müşteriyle paylaşılmaz.** Bu belge iç-satış değerlendirmesi ve teklif taktiği içerir (§3, §6). Sıla Uslu'ya sunulacak versiyon ayrıca üretilmelidir.

**Marka:** Syla Atelier (sylaatelier.com)
**Kurucu:** Sıla Uslu
**Kategori:** Contemporary luxury / ipek odaklı tasarımcı kadın giyim *(siteden yeniden doğrulandı: meta description "contemporary luxury womenswear crafted from exceptional silk and couture fabrics"; "The Essence of Silk" sayfası "quiet luxury" dilini kullanıyor)*
**Denetim tarihi:** 15 Temmuz 2026 · **Baseline:** 21 Haziran 2026 (v1 raporu, Denetmen onaylı)
**Denetim tipi:** DELTA — tam tekrar değil; v1 bulguları bugünkü canlı durumla karşılaştırıldı
**Metodoloji:** Marka Bulutu OS Puanlama Rubriği v1.1 · §0.1 İki Katman Kanıt · Moda/Perakende bağlamı (§2.2-B)

> **Sayısal skor yok (§0.1):** GA4/GSC/satış verisine erişim hâlâ yok. Tüm kategoriler niteliksel band ile raporlanır; sayısal değerler yalnızca doğrulanabilir sayılabilir gerçeklere (ürün adedi, fiyat, SSL tarihi) eşlik eder. Kanıt tipi her satırda işaretlidir: **Tip A** = ölçülmüş/doğrulanmış gerçek · **Tip B** = gözlem/altyapı.

---

## 1 · YÖNETİCİ ÖZETİ

**v1 baseline'ı geçerliliğini koruyor — hatta ana teşhisi keskinleşti.** v1'in temel tanısı "güçlü estetik/yaratıcı temel, geride kalan ticari-teknik altyapı" idi; 24 günde marka yaratıcı tarafta büyük bir hamle yaptı (10 Temmuz 2026'da 60 ürünlük yeni **Hasbahçe / RESORT'26** koleksiyonu yayınlandı, katalog 109 ürüne çıktı, editorial içerik gövdesi — Our Makers, The Essence of Silk, 5 makalelik Journal — sitede canlı) ama **v1'in beş Hızlı Kazanımı'nın hiçbiri uygulanmadı:** sylaofficial.com'un dolmuş SSL'li ölü mağazası hâlâ canlı (bugün yeniden doğrulandı), ana sayfada hâlâ H1 yok, title hâlâ tek kelime, görsellerin %71'i hâlâ alt metinsiz, değer önerisi hâlâ ilk ekranda taşınmıyor. Yaratıcı kas ile teknik hijyen arasındaki makas **açılıyor** — bu, Marka Bulutu OS teklifinin tam da doldurduğu boşluk ve outreach'teki somut kanca (ölü domain) tazeliğini koruyor. Yeni risk sinyali: Hasbahçe'yle gelen üst fiyat katmanı (100.000 TL üzerinde 13 ürünlük sistematik kademe, tepe 182.300 TL; katalog medyanı 52.600 TL), stratejinin "accessible luxury" tek-bant netliği için yeni bir kalibrasyon sorusu doğuruyor.

---

## 2 · DELTA TABLOSU (v1 bulgusu → 15 Tem 2026 durumu)

| v1 Bulgusu (21 Haz) | Bugünkü Durum (15 Tem) | Delta | Kanıt |
|---|---|---|---|
| sylaofficial.com canlı, SSL 15 Kas 2025'te dolmuş (`CN=*.myshopify.com`) | **Aynen duruyor.** OpenSSL bugün yeniden teyit etti: `notAfter=Nov 15 00:22:23 2025 GMT`, `subject=CN=*.myshopify.com`; DNS Shopify IP'sine (23.227.38.65) çözümleniyor; tarayıcı isteği sertifika hatası veriyor | **AYNI (8 aydır dolmuş — risk yaşlanıyor)** | Tip A — openssl + curl, 15 Tem |
| Ana sayfada H1 yok | H1 sayısı: **0** (hâlâ) | **AYNI** | Tip A — HTML kaynağı |
| Title "Syla Atelier" (tek kelime, 12 kr) | Ana sayfa title hâlâ yalnızca "Syla Atelier" | **AYNI** | Tip A — HTML kaynağı |
| 14 görselden 10'u alt metinsiz (%71) | 14 görselden 10'u alt metinsiz — sayfa içeriği değişmiş (hero artık Hasbahçe) ama oran aynı | **AYNI** | Tip A — img/alt sayımı |
| `lang="en"` tek dil, hreflang yok | Aynı: `lang="en"`, hreflang 0 | **AYNI** | Tip A — HTML kaynağı |
| Para birimi yalnız TL (İngilizce site + TL çelişkisi) | Shopify aktif para birimi **TRY**; localization/market-switcher app snippet'i sitede mevcut AMA yapılandırılmış tek pazar TR/TRY/EN — kullanıcıya görünen gerçek değişmedi | **AYNI** (altyapıda kıpırtı var, aktif değil) | Tip A — `Shopify.currency={"active":"TRY"}` + sgcr_localization config |
| Ürün gamı: 49 elbise, 7 set, Silk Edit 40, Bridal Edit 15 | **Toplam 109 ürün** (products.json). Menü: Dresses 60 · Skirts 9 · Sets 7 · Tops 6 · Scarves 6 · Jackets 5 · Pants 4 · Corsets 2 (+şort, gömlek, pelerin, fular tipleri). "The Silk Edit" koleksiyon URL'si artık **404** — navigasyon kategori-temelliye dönüştü; The Bridal Edit URL'si yaşıyor (200) | **DEĞİŞTİ — katalog ~2×, yapı yeniden kurgulandı** | Tip A — products.json (109) + URL testleri |
| Fiyat bandı (elbise) 36.700–75.300 TL | **Elbise: 32.600–182.300 TL** (Artemisia → Humâr). Tüm katalog: 5.175 TL (Râz Foulard) – 182.300 TL. Üst uç v1 maksimumunun ~2,4 katı. *(Not: alt uç — Artemisia 32.600 TL — Mayıs 2025'ten beri katalogda; v1 bandının dar olması örneklem eksiğiydi, delta değil)* | **DEĞİŞTİ — üst uç açıldı** (alt uç: v1 örneklem düzeltmesi) | Tip A — products.json varyant fiyatları + published_at |
| İndirim yok (indirimsiz disiplin) | 109 üründe **0 indirimli varyant** (compare_at_price boş) | **AYNI — disiplin korunuyor (olumlu)** | Tip A — products.json |
| Öne çıkan ürün (Eden) Sold Out; tükenmişlik oranı bilinmiyor | Eden Dress stokta (4/4 varyant available); **109/109 üründe en az bir beden stokta** | **DEĞİŞTİ — tükenmiş ürün bugün gözlemlenmedi** | Tip A — products.json availability |
| Eden Dress ana kumaş %17 ipek / %80 viskoz; "ipek mesajı kalibre edilmeli" | Aynen: "Fabric: 80% Viscose, 17% Silk, 3% Lycra" — ürün düzeyinde silk-blend kalibrasyonu yapılmamış; ANCAK "The Essence of Silk" sayfası ipek anlatısını marka düzeyinde derinleştiriyor | **AYNI (ürün düzeyi) / kısmi ilerleme (marka düzeyi)** | Tip A — ürün sayfası metni |
| Sosyal kanıt 0 (yorum yok) | İncelenen yeni üründe (Lâlezar Gown) ve ana sayfada yorum/yıldız/inceleme uygulaması izi yok (judge.me/yotpo/loox taraması boş) | **AYNI — hâlâ 0** | Tip B — gözlem |
| Ana sayfa hero kampanya-öncelikli, değer önerisi gömülü | Hero şimdi "RESORT'26 — ENTER THE GARDEN OF HASBAHÇE"; yapı aynı: kampanya var, markanın ne olduğu ilk ekranda yok | **AYNI (içerik değişti, yapı değişmedi)** | Tip B — sayfa metni |
| Schema: Organization + WebSite (ana sayfa) | Ana sayfa aynı (+SearchAction); ürün sayfasında **Product schema + H1 mevcut** *(v1'de ürün sayfası schema kaydı yoktu — delta değil, kayıt genişletmesi)* | **AYNI / kayıt genişledi** | Tip A — JSON-LD tarama |
| Sitemap "5 URL — çok düşük" | **v1 düzeltmesi:** o 5 satır sitemap *index*'inin 5 alt-sitemap girişiymiş. Ürün alt-sitemap'i bugün **110 URL** içeriyor; indeksleme kapsamı sorunu görünmüyor (gerçek indeks durumu yine GSC ister) | **v1 BULGUSU DÜZELTİLDİ (hata kaydı)** | Tip A — sitemap_products_1.xml sayımı |
| Instagram 6.992 takipçi, verified | **Doğrulanamadı** — IG bot engeli, profil verisi çekilemedi. Takipçi/aktivite hakkında bugün hiçbir iddia yok | **DOĞRULANAMADI** | — |
| Toptan W&B + retail Milagron | Bu denetimde yeniden doğrulanmadı (site footer'ında görünmüyor; IG bio erişilemedi) | **DOĞRULANAMADI (bugün)** | — |

---

## 3 · v1 HIZLI KAZANIMLARI — UYGULAMA DURUMU

| # | v1 Hızlı Kazanımı | Uygulandı mı? |
|---|---|---|
| 1 | sylaofficial.com'u kapat / 301 yönlendir | ❌ **HAYIR** — sertifika hâlâ dolmuş, site hâlâ çözümleniyor (Tip A, bugün teyit) |
| 2 | Ana sayfaya anlamlı H1 | ❌ HAYIR — H1 sayısı 0 |
| 3 | Title'ları zenginleştir (50-60 kr) | ❌ HAYIR — ana sayfa hâlâ "Syla Atelier" |
| 4 | Kritik görsellere alt metin | ❌ HAYIR — 10/14 hâlâ alt'sız |
| 5 | "Our Story" özünü ana sayfaya taşı | ❌ HAYIR — hero yalnızca Hasbahçe kampanyası |

**Sonuç: 5/5 açık.** Marka bu pencerede enerjisini koleksiyon lansmanına ve editorial içeriğe vermiş (aşağıda); teknik hijyen listesine hiç girilmemiş. Bu, dışarıdan bir ajans müdahalesi olmadığının da dolaylı işareti — ve teklifimizin değer alanının boş durduğunu gösteriyor.

*(Stratejik önerilerden de: dil/para birimi mimarisi ❌ aktif değil; sosyal kanıt sistemi ❌ yok; segment keskinleştirme sitede görünür değil ❌.)*

---

## 4 · YENİ BULGULAR (v1'de olmayan)

1. **Hasbahçe / RESORT'26 lansmanı (10 Tem 2026):** Tek günde **60 yeni ürün** yayınlanmış (Tip A — products.json `published_at`). Adlandırma dili değişti: L'Eclipse / Canto Del Sole (Fransız/İtalyan) → **Lâlezar, Seher, Peyda, Letâfet, Humâr, Derûn** (Osmanlıca/Türkçe). Kimlik açısından çift okuma: kültürel köken sahiplenmesi (güçlü, farklılaştırıcı) ya da adlandırma sistemi tutarsızlığı. **Branding raporuyla hizası kontrol edilmeli** — koleksiyon-başına-dil bilinçli bir mimariyse sorun değil, savrulmaysa erken yakalanmalı.
2. **Kategori genişlemesi:** Elbise-ağırlıklı gamdan tam gardıroba (ceket, korse, pantolon, etek, gömlek, şort, pelerin, fular/eşarp) geçilmiş. "Bir malzeme etrafında derinlik" konumlandırma tezi (Strateji 1.2) hâlâ savunulabilir ama genişleme hızı izlenmeli.
3. **Fiyat mimarisinin üst ucu açıldı:** Katalog 5.175 TL fular'dan 182.300 TL elbiseye uzanıyor (~35×); alt uç Mayıs 2025'ten beri vardı (v1 örneklem eksiği), **gerçek delta Hasbahçe'nin getirdiği üst katman.** Bu katman tekil outlier değil: **100.000 TL üzerinde 13 ürünlük sistematik bir kademe** var (katalog medyanı 52.600 TL). Giriş-fiyatlı aksesuar katmanı klasik lüks "kapı ürünü" taktiği olarak olumlu okunabilir; ama sistematik 100K+ kademesi "accessible luxury" segment tanımını yeniden sorduruyor. Strateji halkasına geri besleme gerekli. *(Kur çevrimi bilinçli verilmedi — §11.5, güncel kur teyidi yok.)*
4. **Editorial içerik gövdesi canlı:** "OUR WORLD" menüsü — Our Story + **Our Makers** (dolu içerik: "ethically crafted in Turkey", Türk ipek dokuma atölyeleri, sınırlı adet, elde dikiş) + **The Essence of Silk** (quiet luxury anlatısı) + **JOURNAL** (5 makale: L'Eclipse in Venice/Padova, Canto Del Sole Milano/Villa Monastero, Silk essence). *(Dürüstlük notu: bu sayfaların v1 tarihinde var olup olmadığı v1'de kayıtlı değil ve arşiv anlık görüntüsü yok — "yeni eklendi" iddiası doğrulanamadı; ancak v1 uzun-vade önerisi #12 ile birebir örtüşen varlıklar bugün canlı. Makale yayın tarihleri sayfadan okunamadı — doğrulanamadı.)*
5. **Meta description mevcut ve konum-yüklü:** "contemporary luxury womenswear crafted from exceptional silk and couture fabrics…" — v1'de meta description durumu kayıtlı değildi; bugün var ve strateji raporunun diliyle ("contemporary/accessible luxury") uyumlu. Delta kesinleştirilemez.
6. **Market-switcher altyapısı sitede ama boş:** `sgcr-localization` app snippet'i kurulu, fakat yapılandırılmış tek ülke TR (TRY/EN). Çok para birimine geçişin teknik zemini hazır görünüyor — aktivasyon yapılmamış.
7. **Ücretsiz kargo çubuğu gözlendi:** sepet çekmecesinde "qualifies for free shipping / …away from free shipping" mekaniği; boş sepette "200TL away" gösteriyor — eşik değeri bu görüntüden güvenilir okunamıyor (şablon/placeholder olabilir), **doğrulanamadı**, müşteriyle teyit edilmeli.
8. **Ürün sayfası hijyeni ana sayfadan iyi:** İncelenen ürün sayfalarında H1 var, Product schema var, title "Ürün – Syla" formatında. Teknik açık ağırlıkla **ana sayfada** yoğunlaşıyor.

---

## 5 · NİTELİKSEL BAND GÜNCELLEMESİ (sayısal skor yok — §0.1)

Moda/Perakende ağırlıkları (§2.2-B). GA4/GSC hâlâ bağlı değil; tüm bandlar Tip B gözlem + Tip A sayılabilir gerçeklerle gerekçeli.

| Kategori | Ağırlık | v1 Band | v2 Band (15 Tem) | Gerekçe |
|---|---|---|---|---|
| Marka & Güven | %25 | Güçlü–Orta | **Güçlü–Orta (aynı)** | Editorial derinlik arttı (Our Makers/Essence/Journal); AMA ölü domain 8. ayında hâlâ canlı, sosyal kanıt hâlâ 0 — güven tarafı yerinde sayıyor |
| İçerik & Mesaj | %20 | Güçlü (hikâye) / Orta (taşınma) | **Güçlü / Orta (aynı etiket, içerik gövdesi kalınlaştı)** | Journal + zanaat anlatısı hikâyeyi büyütüyor; değer önerisi ana sayfada hâlâ gömülü, H1 hâlâ boş |
| Dönüşüm | %20 | Orta | **Orta (aynı)** | Sosyal kanıt 0, CTA hiyerarşisi değişmedi; artı: tükenmiş ürün görünmüyor (satış kaybı riski azalmış), indirimsizlik sürüyor |
| Konumlandırma | %15 | Orta–Güçlü | **Orta (hafif geri)** | Segment sitede hâlâ sabitlenmemiş; yeni belirsizlikler eklendi: fiyat bandı ~35× açıldı, adlandırma dili koleksiyonlar arası değişti, kategori genişledi. Yaratıcı yön güçlü ama konum tanımı bulanıklaşma riskinde |
| Görünürlük (SEO) | %10 | Zayıf | **Zayıf (aynı; içerik tarafı kıpırdıyor)** | H1/title/alt/hreflang aynen açık; artılar: Journal içerik varlığı, ürün sayfası H1+Product schema, sitemap bulgusu düzeltildi (110 ürün URL'si mevcut) |
| Büyüme & Strateji | %10 | Orta | **Orta (aynı, olumlu sinyalle)** | Koleksiyon ritmi işliyor (~13,5 ayda 3 koleksiyon — products.json yayın tarihlerine göre), katalog 2×; kanal/dil mimarisi kararı hâlâ verilmemiş, sadakat katmanı hâlâ yok |

> Onur & Temsil v1'deki gibi aktif değil (insan-merkezli marka değil); ağırlığı Marka & Güven'de.

**Genel profil (v2):** "Güçlü ve *büyüyen* yaratıcı-editorial temel · yerinde sayan ticari-teknik altyapı." Baseline tanısı geçerli; makas açıldı.

---

## 6 · SIRADAKİ ADIM (teslim zinciri + outreach bağı)

1. **Outreach hâlâ gönderilebilir durumda — kanca tazelendi.** Taslaktaki somut değer kancası (sylaofficial.com SSL, 15 Kas 2025) bugün yeniden doğrulandı ve artık "8 aydır dolmuş" olarak daha da güçlü. İkinci kanca eklenebilir: "Yeni Hasbahçe lansmanınız güçlü — ama onu taşıyacak teknik/keşif altyapısı (H1, çok para birimi, sosyal kanıt) hâlâ kapalı." Gönderim durumu belirsiz → Ayhan'dan teyit; gönderilmediyse bu delta ile güncellenip gitmeli (Kademe 2).
2. **Strateji halkasına geri besleme (küçük revizyon):** üst fiyat katmanı (100K+ 13 ürünlük kademe) + Türkçe adlandırma + kategori genişlemesi "accessible luxury" tanımıyla hizalanmalı; Hasbahçe, konumlandırma anlatısına dahil edilmeli.
2b. **Branding halkasına da geri besleme:** brand book §3.1 Romance-dil adlandırmayı (L'Eclipse, Canto Del Sole) "korunacak DNA" ilan etmişti; Hasbahçe'nin Osmanlıca/Türkçe adlandırması bu ilkeyi kırdı. Koleksiyon-başına-dil bilinçli mimariyse brand book güncellenmeli; savrulmaysa kurucuyla konuşulacak ilk kimlik sorusu bu.
3. **Kalan halkalar: İçerik + Growth.** Müşteri kazanılırsa ilk 30 gün önceliği v1'in hâlâ açık 5 hızlı kazanımı (özellikle ölü domain + H1/title + değer önerisi) — düşük efor, gösterilebilir etki; ardından Growth halkasıyla çok para birimi aktivasyonu (altyapı snippet'i zaten kurulu) + sosyal kanıt sistemi.
4. **Ölçüm ön koşulu değişmedi:** GA4 + GSC erişimi olmadan hiçbir before/after sayısallaşmaz; onboarding'de ilk istek bu.

---

## VERİ EKSİKLERİ / DOĞRULANAMAYANLAR (15 Tem)

- GA4 / GSC / satış / AOV / iade — erişim yok (v1 ile aynı).
- Instagram takipçi/etkileşim — bot engeli, **doğrulanamadı** (v1'deki 6.992 güncellenemedi).
- TikTok metrikleri — bakılmadı/erişilemedi.
- Wolf & Badger + Milagron kanallarının güncel durumu — bugün yeniden doğrulanamadı.
- Journal makalelerinin ve Our World sayfalarının yayın tarihleri — sayfadan okunamadı; arşiv anlık görüntüsü yok (Wayback boş döndü).
- Ücretsiz kargo eşiği — görünen "200TL" değeri şablon olabilir, teyit gerekir.
- Kur çevrimleri (TL→EUR) bu raporda bilinçli olarak verilmedi — güncel kur teyidi olmadan rakam yazılmaz (§11.5).

---

*Marka Denetim Raporu v2 (DELTA) · Syla Atelier · 15 Temmuz 2026 · Marka Bulutu OS Keşif & Denetim Halkası · Baseline: 21 Haz 2026 v1 (ezilmedi, ayrı dosya) · Metodoloji: Rubrik v1.1 §0.1 + §2.2-B Moda · Bu rapor müşteriye gitmeden Denetmen 7 merceği + Ayhan onayından geçer (Kademe 2).*
