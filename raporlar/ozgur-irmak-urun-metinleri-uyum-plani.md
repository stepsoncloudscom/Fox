# Özgür Protez — Wix Ürün Metinleri: Uyum & Onur Yeniden Yazım Planı
*Fox · 29 Temmuz 2026 · Kaynak zemin: marka-bulutu-os-medikal-protez-bagi.md (§A yasak/güvenli dil), ozgur-irmak-marka-kimligi-v01.md (§2.3 ses, §2.4 kelime listesi), ozgur-irmak-marka-context.md (onur eki)*

> ⚖️ **GATE (pazarlık dışı):** Site medikal/protez. Hiçbir metin **avukat onayı** olmadan YAYINLANMAZ. Site şu an **Draft (yayınlanmamış)** — bu belgedeki tüm çalışma "hazırlık"tır (Kademe 1/2), yayın Ayhan+avukat kapısına bağlı. Fox avukat değildir; uyumlu-by-design taslak üretir, işaretler.

---

## 0 · DURUM (ne buldum)

- **Site:** ÖzgürProtez (Wix, id `6e57503f-4b11-4ac2-8912-9a46e160abf8`), **Draft/Free**, dil `en` ama **içerik Türkçe**, para birimi TRY.
- **Yapı:** **Wix Stores V3** (mağaza/katalog) — **73 ürün**. Her ürün: isim + açıklama + 2 "info section" + fiyat alanı + iade politikası + stok.
- **İçerik dili:** Türkçe (Ayhan'ın ve müşterinin iletişim dili). → Yeniden yazım **Türkçe** kalır.
- **Metinlerin kaynağı:** Büyük çoğunluğu **üreticinin (Össur/Ottobock) pazarlama metninin çevirisi.** Wix'in kendi uyarısı ürün alanında hâlâ duruyor: *"Write your own description instead of using manufacturers' copy."*

**Açıklama metni durumu (ilk 30 üründe örüntü — kalan 43 aynı desende):**
- **Gerçek Türkçe teknik metin (~%75):** teknik bilgi taşıyor ama pazarlama diliyle → uyum düzeltmesi + onur tonu gerekiyor, **teknik bilgi korunacak.**
- **Hâlâ Wix placeholder ("I'm a product description…") (~%25):** ör. Rheo Knee, Karbon Soket, I-Limb Access Titanium, TECHNICAL PACK, Evanto Ayak, Taleo Ayak, Navii Knee → sıfırdan **bilgilendirme** metni gerekiyor (uydurma yok — üretici verisi gelene kadar iskele + bayrak).
- **Info section'lar:** eski ürünlerde 2 bölüm de placeholder ("PRODUCT INFO" + **"Return and Refund policy"**); yeni ürünlerde boş.

---

## 1 · UYUM & ONUR TEŞHİSİ (metinlerdeki ihlaller)

Marka kimliği §2.4 kırmızı kuşak + medikal A.3'e göre mevcut metinlerdeki tekrar eden ihlaller:

| İhlal türü | Örnek (mevcut metinden) | Ürün |
|---|---|---|
| **Abartı / AI-klişe** | "devrim niteliğindeki tasarım", "kusursuz bir akış", "gerçek potansiyelinizi ortaya çıkarın", "zihninizi özgürleştirin" | Genium X4 |
| **Üstünlük iddiası** | "yeni bir standart belirliyor", "birinci sınıf", "sıra dışı" | Genium X4, I-Limb Quantum |
| **Talep yaratma / doğrudan satış hitabı** | "…mi arıyorsunuz?", "okumaya devam edin", "güvenebilirsiniz" | Taleo Adjust/Vertical Shock, Trias |
| **Ünlem / imperatif CTA** | "kendinize güvenin ve cesaret edin!" | Trias |
| **Pazarlama sloganı** | "Bu sadece bir protez ayak değil. Bu, bir temel." | Taleo Adjust/Adapt |

**Korunacak (bunlar yeşil kuşak — bilgilendirme, silme):** malzeme (karbon, titanyum, silikon), mekanizma (mikroişlemcili, miyoelektrik, hidrolik, torsiyon), teknik veri (yük kapasitesi 90+ kg, döngü ömrü 300.000, su geçirmezlik), üretici adı, uygulama/uyum notları. Bunlar cihaz yön. **Madde 15/2 bilgilendirme istisnası** kapsamındadır (resmî sitede cihaz bilgilendirmesi = reklam yasağı DIŞINDA).

---

## 2 · 🔴🔴 YAPISAL DUR BAYRAĞI (metnin ötesinde — Ayhan+avukat kararı)

Metinleri düzeltmek tek başına yetmez; **kabın kendisi risk taşıyor:**

- Medikal paket A.2: **"Bu merkezlerin cihazlarının tüketiciye internet üzerinden satışı YASAK → siteye e-ticaret/sepet/'satın al' ASLA konmaz; site = bilgilendirme + danışma talebi."**
- Mevcut site **mağaza (Wix Stores)** olarak kurulu: fiyat alanları, **"Return and Refund policy" (iade politikası)**, stok, sepet mantığı. Bu yapı, cihaz **satışı** izlenimi verir → **yasak bölge.**
- **Öneri:** Yapı "satış" değil **"bilgilendirme + danışma"** hattına çekilmeli: fiyat gizli/0 (şu an 0), sepet/satın-al kapalı, iade politikası bölümü kaldırılmalı, her ürün sayfasında "satın al" yerine **"danışma/değerlendirme talebi"** (Wix Forms, KVKK aydınlatmalı) durmalı.
- Bu, metin turundan **ayrı ve daha büyük bir karar** — avukat sorusu #1 ve #2'ye bağlı. **Bu belge onu çözmez; işaretler.**

*Ek küçük bayrak (Dikkat):* Görsel dosya adlarında rakip isimleri gömülü ("...ossur-ottobock-**luxmed-nesa-proklinik-teknik-ortopedi**..."). SEO amaçlı olabilir; rakip adını kendi varlık adında taşımak sarı bir nottur — ayrı ele alınır.

---

## 3 · YENİDEN YAZIM STANDARDI (uygulanacak kural)

Her ürün metni şu kalıba çekilir:
1. **Ne olduğu** (kategori + üretici): "X, [üretici] tarafından … için geliştirilmiş bir [kategori]."
2. **Nasıl çalıştığı / neyden yapıldığı** (teknik veri — korunur, üreticinin verisiyle sınırlı).
3. **Kime uygun** (aktivite düzeyi — "seçicilik" değil, teknik uygunluk dili).
4. **Standart kapanış satırı (tüm ürünlerde aynı — uyum + onur çapası):**
   > *"Cihazın uygunluğu kişiye özel değerlendirme ile belirlenir; uygulama ve uyarlama merkezimizde uzman tarafından yapılır."*
   Bu satır sayfayı "satın al"dan "değerlendir + uygula"ya çevirir (bilgilendirme yatağı) ve onur çerçevesini taşır.

**Yasak (çıkar):** ünlem, "siz…mi arıyorsunuz" hitabı, imperatif CTA, slogan, "en iyi/birinci sınıf/yeni standart/devrim/kusursuz/benzersiz", "potansiyelini ortaya çıkar" tipi AI-klişe, acıma/"engeline rağmen"/seçicilik.
**Ton:** sade, kanıtlı, dingin; özne = birey/kullanıcı, "vaka" değil.

---

## 4 · UYUMLU ÖRNEKLER (3 vaka — tone-lock için)

### Örnek A — Genium X4 (en ağır ihlal)
**MEVCUT:** "Zihninizi özgürleştirin ve gerçek potansiyelinizi ortaya çıkarın: Genium X4 ile tanışın. Ottobock'un yeni nesil mikroişlemcili dizi (MPK), performans, dayanıklılık ve kişiselleştirme alanlarında yeni bir standart belirliyor. Bu sıra dışı diz proteziyle … her hareket kusursuz bir akışla gerçekleşir. … Bu devrim niteliğindeki tasarımı … keşfetmek için okumaya devam edin."

**YENİDEN (uyumlu + onur):**
> Genium X4, Ottobock'un mikroişlemcili diz eklemi (MPK) ailesinde yer alır. Yürüyüş verilerini gerçek zamanlı okuyan mikroişlemci kontrolüyle çalışır; farklı yürüme hızlarına, eğim ve zemin değişimlerine, merdiven ve rampa gibi günlük hareketlere uyum sağlayacak biçimde tasarlanmıştır. Kişiye özel ayarlanabilen parametreleri ve dijital uygulama desteğiyle günlük kullanım için yapılandırılır.
>
> Cihazın uygunluğu kişiye özel değerlendirme ile belirlenir; uygulama ve uyarlama merkezimizde uzman tarafından yapılır.

*Korundu:* Ottobock, mikroişlemcili diz/MPK, uyum-yeteneği, kişiselleştirme, dijital destek. *Çıkarıldı:* tüm abartı/AI-klişe/üstünlük/CTA.

### Örnek B — Trias (ünlem + imperatif + güven-vaadi)
**MEVCUT:** "…orta derecede aktif kullanıcılar için geliştirilmiştir. Karbon ayağın hafif ağırlığı ve iyi yaylanma özellikleri, enerjiyi … tasarruf etmeye yardımcı olur. Uyumlu ve güvenilir fonksiyonelliği ile Trias protez ayağa güvenebilirsiniz. … Trias size emniyet hissi verir; kendinize güvenin ve cesaret edin!"

**YENİDEN:**
> Trias, iç mekânlarda ve bilinen dış mekânlarda hareket eden, yürüyüş sırasında dengeli bir stabiliteye önem veren orta derecede aktif kullanıcılar için Ottobock tarafından geliştirilmiş bir karbon protez ayaktır. Hafif yapısı ve yaylanma özelliği, adım sırasında açığa çıkan enerjinin bir bölümünü geri kazandırarak hareket için gereken eforu azaltmaya yardımcı olur. Düz zeminde ve gündelik dış mekân kullanımında dengeli bir yürüyüş sağlayacak biçimde tasarlanmıştır.
>
> Cihazın uygunluğu kişiye özel değerlendirme ile belirlenir; uygulama ve uyarlama merkezimizde uzman tarafından yapılır.

### Örnek C — Rheo Knee (placeholder → sıfırdan; uydurma yasağı)
**MEVCUT:** "I'm a product description…" (Wix placeholder)

**YENİDEN (iskele — üretici verisi bekliyor):**
> Rheo Knee, Össur'un mikroişlemcili diz eklemidir. Yürüyüş sırasındaki hareketi algılayarak direncini gerçek zamanlı ayarlayan mikroişlemci kontrolüyle çalışır ve farklı yürüme hızları ile zemin koşullarına uyum sağlayacak biçimde tasarlanmıştır. *[Ayrıntılı teknik özellikler üreticinin güncel verisiyle tamamlanacak — uydurma yapılmadı, §11.5.]*
>
> Cihazın uygunluğu kişiye özel değerlendirme ile belirlenir; uygulama ve uyarlama merkezimizde uzman tarafından yapılır.

---

## 5 · UYGULAMA PLANI (Faz B — onay sonrası)

1. **Tone-lock:** Ayhan yukarıdaki 3 örneği + standart kapanış satırını + info-section kararını onaylar (veya düzeltir).
2. **Tam census:** kalan 43 ürün çekilir; placeholder vs gerçek listesi kesinleşir.
3. **Toplu yeniden yazım:** 73 açıklama standarda çekilir (placeholder olanlar üretici verisi bulunana dek iskele+bayrak).
4. **Info section kararı:** "Return and Refund policy" bölümü **kaldırılır** (satış yok → iade yok); "PRODUCT INFO" bölümü ya kaldırılır ya teknik-özellik tablosuna çevrilir.
5. **Yazma mekaniği:** Wix Stores V3 `Update Product` (rich-content `description`, `revision` ile optimistic concurrency) — teknik doğrulama Faz B ilk adımı.
6. **Denetmen medikal merceği:** yasak-kalıp taraması + glyph + seçicilik + kapanış-satırı tutarlılığı.
7. **Avukat gate → Ayhan → yayın.** Site Draft kaldığı sürece 1-4 hazırlıktır; publish yalnız gate sonrası.

---

## 6 · SONUÇ — UYGULANDI (29 Tem 2026, Ayhan onayı: B)

**Yapılan (Draft'ta, yayınlanmadı):**
- **48 ürün açıklaması** TİTCK yeşil-kuşak + onur standardına çekildi (46 gerçek metin uyumlaştırıldı + placeholder'lar temiz Türkçe stub'la değişti: Rheo Knee, i-Limb Access Titanium, Karbon Soket, Navii Knee). Her açıklamaya standart kapanış satırı eklendi.
- **İki placeholder info-section varlığı silindi** (`41e8be53…` "PRODUCT INFO" + `e7578195…` "Return and Refund policy") → **tüm ürünlerden** otomatik kalktı. İade-politikası/satış izlenimi veren bölüm sitede hiçbir üründe yok.
- Doğrulandı: Genium X4 / Rheo Knee / MCPDriver → yeni açıklama + info-section [] + Türkçe glyph temiz.
- Mekanik: Wix Stores V3 Bulk Update Products (`returnEntity:false`), 2 batch + tekil düzeltmeler. Tüm çağrılar success.

**YAPILMADI — bilinçli (uydurma yasağı §11.5):**
- **24 ürün tamamen BOŞ** (hiç açıklama yok → kaybedilecek bilgi yok). Kaynak (üretici) verisi olmadan yazılmadı. Liste — Branding/İçerik'in kaynak-veri turunda doldurulacak:
  *Evanto - Prosthetic Foot · Sprinter Junior · Maverick Vertical Shock · Maverick junior · Freestyle Swim · Kintrol · Restore · Bebionic Hand · Bebionic Hand EQD · Michelangelo Hand Transcarpal · AxonHook · AxonSkin Visual · AxonRotation · Electric wrist rotator · Myo Plus TR · Transhumeral Soft Harness · Genium X3 · Movido · Modular Knee Joint with Rotary Hydraulic · Knee joint with friction brake (monocentric, lock) · Polycentric Modular Knee Joint · ProFlex Plus Sleeve · C-Brace · E-Mag Active.*
- **3 gizli (visible:false) yinelenen ürün** — info-section'ları temizlendi ama İngilizce placeholder açıklama duruyor (gizli, görüntülenmiyor): *TECHNICAL PACK · Evanto Ayak · Taleo Ayak.* Ayhan kararı: bunlar silinmeli mi (yinelenen) yoksa stub mu?

**AÇIK — Ayhan/avukat kapısı:**
1. **🔴 YAPISAL:** Site hâlâ Wix Stores (mağaza) altyapısında. Fiyat alanları (0) + sepet/satın-al mantığı duruyor. TİTCK internet-satışı yasağı için bunların da kapatılması/"danışma talebi"ne çevrilmesi gerekir — ayrı iş, avukat sorusu #1-2.
2. **Yayın:** Hiçbir şey publish edilmedi; site Draft. Yayın öncesi Denetmen medikal merceği + avukat onayı şart.
3. Görsel dosya adlarındaki rakip isimleri (luxmed/nesa/proklinik) — SEO/itibar notu, ayrı ele alınacak.

---
*v2 · 29 Tem 2026 · Fox · Metin turu UYGULANDI (Draft); yapısal satış-yapısı + yayın Ayhan+avukat kapısında.*
