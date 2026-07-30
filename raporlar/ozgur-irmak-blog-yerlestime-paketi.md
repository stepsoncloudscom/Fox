# Özgür Irmak — Blog Yerleştirme Paketi (Protez Bakımı v0.2)
*İçerik Ajanı · Marka Bulutu OS · 30 Temmuz 2026 · Model A ilk canlı test: metin Metin Yazarı'ndan, yerleştirme + görsel yön + schema İçerik'ten.*

> ⚖️ **GATE AÇIK — TASLAK YAYINLANMADI.** Wix'te statü `UNPUBLISHED`. Yayın öncesi zorunlu sıra: Denetmen medikal re-check → klinisyen (nöropati lafzı) → avukat (disclaimer + genel) → Ayhan onayı. Bu paket yerleştirme + görsel/schema hazırlığıdır; hiçbir kelime uydurulmadı, hiçbir gate atlanmadı.

---

## 1 · NE YAPILDI — Wix Taslak Durumu

| Alan | Değer |
|---|---|
| Wix Blog app | ✅ **KURULU** (ID `14bcded7-0066-7c35-14d7-466cb3f09103`) — app kurma gerekmedi |
| Site | ÖzgürProtez · ID `6e57503f-4b11-4ac2-8912-9a46e160abf8` · statü **Draft/Free** · dil `en`, ülke TR |
| Taslak post ID | **`b75a0b66-a6d3-4be9-ab54-7d5ecb5cb340`** |
| Statü | **`UNPUBLISHED`** (taslak — `publish` parametresi ASLA set edilmedi) |
| Başlık (H1 = post-title) | Protez Bacak ve Kol Bakımı: Her Gün İçin Pratik Notlar |
| Dil | `tr` |
| Yazar (memberId) | **Steps On Clouds** (`bd311e7a…`) — teknik "taslağı hazırlayan" alanı. Gerçek E-E-A-T künyesi ⟦bekliyor⟧; müşteri adı doğrulanmamış yazar olarak ATANMADI (Denetmen §7-4). |
| Erişim | Wix Dashboard → Blog → Drafts (taslak olduğu için public URL yok; `slugs:[]`) |
| Okuma süresi | ~4 dk (Wix otomatik) |

**Gövde:** §3 birebir taşındı. H1 = post-title (çiftlenmedi, §37 yapısal notuna uyuldu); 6 bölüm başlığı **H2**; FAQ 5 Q&A (soru = bold paragraf); belirti listesi = bulleted list; "Adım adım, birlikte." bold kilitli kapanış korundu; "teknik sorumlu" terimi korundu (KKK, "uzman" değil).

**En başta BLOCKQUOTE editör-notu** eklendi ("BU TASLAK YAYINLANMAZ" + gate sırası + 3 yer tutucu uyarısı + künye/görsel eksik) → yayınlayan yanlışlıkla canlıya almasın. Bu blok yayından önce silinir.

**3 ⟦…⟧ yer tutucu görünür + italik** bırakıldı (doldurulmadı):
1. "Cilt ve Güdük Bakımı" altında → ⟦Branding + klinisyen: "güdük" vs onur-öncelikli terim⟧
2. Diyabet FAQ cevabından sonra → ⟦Klinisyen: nöropati/diyabet kesin tıbbi lafız⟧
3. Özet içinde → ⟦Avukat: disclaimer lafzı⟧

### Bayraklanan 2 teknik pürüz (dürüstlük)
- **`hashtags:[]` döndü** — "bilgilendirme" etiketi persist OLMADI; "Bilgilendirme" **kategorisi de yok** (kategori listesi boş). Kategori/etiket, editörde ya da ayrı Categories/Tags API çağrısıyla kurulmalı. Site taksonomisi kararı (kaç bilgilendirme kategorisi olacak) Branding/Ayhan alanı → **bayrak, tek taraflı kategori yaratmadım.**
- **Editör-notu blockquote'u** iki paragrafı tek paragraf + satır sonuna normalize etti (Wix davranışı). Kozmetik; okunur, uyarı işlevi bozulmadı.

---

## 2 · GÖRSEL YÖN BRIEFİ (üretim değil, yön — KKK §6 zemininde)

> Register = **Özgür Irmak kendi kimliği** (SOC değil). Palet: Irmak Gecesi `#0C2B2E` · Canlı Kor `#D4602B` (aksan ≤%10, metin/ana yüzey değil) · Ten `#E9D9C4` · Sıcak kırık beyaz `#F6F3EC`. Saf beyaz/siyah yok; kategori-mavisi (Ottobock bölgesi) yok.
> **KESİN YASAK (KKK §6 + standart §8):** stok görsel · **medikalde AI yüz** · acıma/ilham pornosu kadrajı · floresan-klinik/steril katalog ışığı · protezi saklama VEYA fetişleştirme.

**Ortak dil (her kare):** gerçek atölye + gerçek eller/malzeme; sıcak, atmosferik, yönlü ışık; doku görünür (silikon, karbon fiber, ahşap, deri); cömert negatif alan, off-center, tek odak, film-still hissi. Özne = günlük hayatını yöneten birey; göz hizası/güç açısı, acıyan bakış YOK. Onur testi: *figür özne mi, nesne mi?* Nesne ise red.

| # | Yerleşim | Kadraj yönü | Not |
|---|---|---|---|
| Kapak | Post hero | Bir bireyin gündelik anı — protezle hareket/duruş; yüz görünüyorsa **gerçek kişi + yazılı KVKK izni** (KKK §7), aksi halde eller/gövde/atölye ortamı, dingin güç. Off-center, sıcak yönlü ışık, negatif alan. | Kapak "bakım" değil "kendi akışında yaşam" hissi versin (tagline: Hayat, kendi akışında). |
| Gövde-1 | "Silikon Liner… Temizliği" bölümü | Ters çevrilmiş silikon liner'ın iç yüzeyinin ılık su + yumuşak bezle temizlenişi; gerçek eller, atölye tezgâhı. Silikon dokusu okunur. | Ürün-katalog ışığı değil; sıcak, yakın plan, editorial. |
| Gövde-2 | "Cilt ve Güdük Bakımı" bölümü | Günlük cilt kontrolü anı — ayna yardımıyla; dokunuş nazik, birey öznedir. **Yara/lezyon/tıbbi close-up YOK** (mevzuat + onur). | ⚠️ Terim kararı (güdük) çözülene dek alt-text de nötr kalır. |
| Gövde-3 | "Soket, Mekanik…" bölümü | Mikroişlemcili diz / miyoelektrik el gibi bir bileşenin bağlantı-yüzeyinin kuru bezle silinişi; karbon fiber + elektronik doku, teknoloji + insan eli birlikte (ton dengesi 50/50). | Teknoloji "soğuk" değil, elle temas eden sıcak kare. |
| Gövde-4 | "Nasıl Saklanır" bölümü | Liner'ın standında, tozdan uzak, düzenli saklanışı; sade natürmort, sıcak ışık, negatif alan. | En "still-life" kare; süssüz (KKK §3-4 dürüstlük = süssüzlük). |

**Prodüksiyon notu:** Bu blog "1 kampanya çekimi" (D1 lansman) kapsamında planlanan atölye/kullanım çekiminden beslenebilir — ayrı stok satın alma gereksiz. Görsel üretilmeden önce görsel üretim standardı §7 render-and-review + onur eki (C) uygulanır. AI yüz üretimi bu müşteride devre dışı.

---

## 3 · ALT-TEXT YÖNÜ (SEO + a11y + onur — SEO §4.8)

Betimleyici, anahtar-dostu ama zorlamasız; nötr/onurlu, acıma yok. Öneri iskeletler (görsel netleşince kesinleşir):
- Kapak: "Protez bacak ile gündelik hayatını sürdüren bir birey" *(yüz/izin durumuna göre uyarlanır)*
- Gövde-1: "Silikon liner iç yüzeyinin ılık su ve yumuşak bezle temizlenmesi"
- Gövde-2: "Protez kullanan bir kişinin günlük cilt kontrolünü ayna yardımıyla yapması"
- Gövde-3: "Miyoelektrik el bileşeninin temas yüzeyinin kuru bezle silinmesi"
- Gövde-4: "Silikon liner'ın standında, tozdan uzak saklanması"

Kural: alt-text'te "engelli/mağdur/kahraman" dili YOK; eylem + nesne + bağlam. WCAG: kontrast + başlık hiyerarşisi çıktı kapısında (SEO §5.6).

---

## 4 · SCHEMA NOTU (Growth + geliştirmeye — SEO §3.1/§3.2/§4.7)

Yapı hazır; **uygulama Growth/dev** (Wix custom code / SEO ayarı). Yayın öncesi gate'e tabi — placeholder'lı alan schema'ya GİRMEZ.

### 4.1 FAQPage (en yüksek getirili)
Gövdedeki 5 Q&A'dan türetilir (`mainEntity` → her biri `Question` + `acceptedAnswer`):
1. Silikon liner nasıl temizlenir? → cevap hazır ✅
2. Cilt ve güdük bakımı nasıl yapılır? → cevap hazır ✅ *(terim kararı §4.4 beklerse "güdük" ifadesi Branding/klinisyen onayına göre kalır/değişir)*
3. Protez ve liner nasıl saklanır? → cevap hazır ✅
4. Güdükte kızarıklık/yara olursa ne zaman başvurmalı? → cevap hazır ✅
5. His azalması/diyabet varsa nelere dikkat? → **⚠️ cevap lafzı ⟦klinisyen bekliyor⟧** — bu Q&A schema'ya klinisyen onaylı lafız gelmeden EKLENMEZ (YMYL).

### 4.2 MedicalClinic / MedicalBusiness (organizasyon)
Alanlar: `name` = "Özgür Irmak Yüksek Teknoloji Protez ve Ortez Uygulama Merkezi" · `address` **[NAP bekliyor]** · `telephone` **[bekliyor]** · `areaServed` (yurtiçi + uluslararası hasta) · `url`. NAP künye/schema/GMB'de birebir aynı olmalı (GEO güveni, SEO §3.4).

### 4.3 MedicalWebPage + E-E-A-T künye
`author` = **gerçek uzman adı + belge** ⟦bekliyor — Denetmen §7-4, belge teyidi⟧ · `reviewedBy` = klinisyen ⟦bekliyor⟧ · `dateModified`. Anonim YMYL içerik görünürlük almaz → künye yayın ön-koşulu.

### 4.4 İç link (yalnız bilgilendirme — satış/sepet ASLA)
"silikon liner" → varsa/planlanıyorsa "Silikon liner nedir" bilgilendirme sayfası; "soket/mekanik" → "Protez süreci" bilgilendirme sayfası. Wix Stores/sepet linki YASAK (internet-satışı yasağı).

---

## 5 · ÜRETİM/YAPI NOTLARI (bilinçli kararlar — şeffaflık)
- **Dev-yönlü meta notlar gövdeye TAŞINMADI:** kaynak §3'teki "(Yapısal not — İçerik/geliştirici…)" (satır 37) ve "(FAQPage schema zemini — Growth…)" (satır 82) reader-copy değil, bana/dev'e talimat → placeholder sızıntısı olmasın diye okuyucu gövdesine girmedi (standart §5). İkisi de eyleme döküldü (H1 çiftlenmedi; schema notu §4). Bu paraphrase DEĞİL — üretim iskelesi ayıklaması.
- **SEO meta (§2) — Growth uygular:** SEO başlık `Protez Bacak ve Kol Bakımı: Günlük Kullanım Rehberi` (51 krkt) · meta açıklama = excerpt'e yazıldı (133 krkt) · önerilen slug `protez-bacak-ve-kol-bakimi`. Formal `seoData.tags` + slug kilidi schema ile tek geçişte Growth tarafından set edilir (gated draft'ta yarım SEO bırakmamak için).

---

## 6 · İÇERİK KALİTE SKORU (v3 rubriği — görsel/belge ağırlıklı)

**Toplam: 90 / 100 — A** *(bu bir yerleştirme + yön işi; görsel PIKSEL üretilmedi — "Görsel Yön" = yön kalitesi ölçülür, render edilmiş imge değil.)*

| Kategori | Ağırlık | Puan | Gerekçe |
|---|---|---|---|
| Görsel Yön & Kalite | %30 | 26/30 | Brief KKK §6 zeminli, spesifik, slop-önler; kapak+4 gövde + prodüksiyon notu. Eksi: imge üretilmedi (rol gereği yön); pikselde render-and-review yapılamadı. |
| Brief'e Sadakat | %20 | 19/20 | §3 birebir; yapı/H2/FAQ/kapanış korundu; 3 placeholder görünür; editör-notu eklendi. Metin Yazarı sözü paraphrase edilmedi. |
| Marka Kimliği (KKK) | %20 | 18/20 | Doğru register (Özgür Irmak, SOC değil); palet+görsel dil KKK'dan; "teknik sorumlu" korundu. Eksi: blog gövde tipografisi (IBM Plex/Lora) site-tema config'i — bu API kapsamı dışı, bayrak. |
| Onur & Temsil | %15 | 14/15 | Gate korundu; alt-text nötr/onurlu; acıma yok; yara close-up yasağı brief'te. |
| Teknik (glyph/Türkçe/render) | %15 | 13/15 | Türkçe glyph kusursuz (İ/ş/ç/ğ/ö/ü); ₺ kullanılmadı; metin render-and-review (API echo) temiz. Eksi: hashtag persist olmadı, SEO seoData henüz set değil (Growth'a devredildi), blockquote normalize. |

Doğruluk: uydurma rakam/iddia YOK → D bandı tetiklenmedi. Medikal kesin lafız uydurulmadı (klinisyen/avukat bayraklı).

---

## 7 · GATE DURUMU & DEVİR

**Yayın öncesi eksikler (tümü açık):**
- ⟦Klinisyen⟧: nöropati/diyabet FAQ lafzı (schema Q5 dahil)
- ⟦Avukat⟧: disclaimer lafzı + genel medikal onay
- ⟦Branding + klinisyen⟧: "güdük" vs onur-öncelikli terim kararı (gövde + FAQ + alt-text'e yansır)
- E-E-A-T künye: gerçek uzman adı + belge teyidi (Denetmen §7-4)
- Görsel: gerçek atölye çekimi (stok/AI yüz yasak)
- Kategori/etiket "bilgilendirme": editörde/API'de set edilecek (persist olmadı)
- NAP (adres/telefon) → MedicalClinic schema için

**Devir:**
- **Growth/dev'e:** §4 schema yapısı + §5 SEO meta değerleri + iç link haritası + kategori/etiket kurulumu.
- **Branding + klinisyen'e:** güdük terim kararı.
- **Klinisyen + avukat'a:** 3 placeholder lafzı.
- **Ayhan'a:** yayın sırası son onay + "Bilgilendirme kategorisi taksonomisi" kararı.

**Yayın sırası (bozulmaz):** Denetmen medikal re-check → klinisyen → avukat → Ayhan → yayın (draft `publish`).

---
*İçerik Ajanı · 30 Tem 2026 · Kaynak: Metin Yazarı v0.2 + Growth SEO uyarlama §4/§5 + KKK §3/§6/§7 + görsel üretim standardı §6/§7/§8 + marka-context. Model A ilk canlı test — metin birebir taşındı, prosa üretilmedi.*
