# Özgür Protez — Wix Sitesi Yasal Risk Analizi
*Fox · 12 Eylül 2026 · Kaynak: canlı Wix verisi (site ID `6e57503f-4b11-4ac2-8912-9a46e160abf8`)*

> ⚖️ **Fox avukat değildir.** Bu belge risk **işaretler**, hukuki görüş vermez. Her madde
> `marka-bulutu-os-medikal-protez-bagi.md` §A zeminine dayanır; kesinleşmesi avukat teyidine bağlıdır.

> ✅ **Zamanlama avantajı:** Site şu an **Draft** (plan: Free, dil: yalnız `tr`). Aşağıdaki hiçbir
> bulgu henüz kamuya açık değil. Yayın öncesi kapatılırsa maruziyet sıfır; yayından sonra
> kapatılırsa her biri fiilî ihlal.

## Denetlenen yüzey (12 Eyl, API ile doğrulandı)
115 ürün · 3 yayında blog yazısı · 3 form şeması · 10 kurulu uygulama.
Denetlenemeyen: sayfa yerleşimi, çerez bandı, footer politika linkleri (klasik editörde REST API yok — Editör oturumunda gözle).

---

## 🔴 DUR — yayın öncesi kapanmazsa ihlal

### 1. Site bir e-ticaret mağazası olarak kurulu
**Bulgu:** Wix Stores (Catalog V3) kurulu, 115 ürün `visible:true`, para birimi TRY; yanında
Wix Forms & Payments ve Wix Invoices de kurulu.
**Zemin:** Tıbbi Cihaz Satış, Reklam ve Tanıtım Yönetmeliği — ısmarlama protez-ortez merkezlerinin
cihazlarının tüketiciye **internet üzerinden satışı yasak**.
**Neden fiyat ₺0,00 kurtarmıyor:** Yasak satış *fiyatına* değil satış *mecrasına* bakar. Sepet/ödeme
akışı duruyorsa görünen şey mağazadır.
**Yaptırım mekaniği:** uyarı → 3 iş günü içinde düzeltilmezse **15 gün satış faaliyeti durdurma**.
**Aksiyon:** Katalog "mağaza"dan "bilgilendirme mimarisi"ne taşınmalı; sepet/checkout kapatılmalı;
Forms & Payments + Invoices kaldırılmalı. Uygulama kuşakları: `ozgur-irmak-uyumlu-ticaret-plani.md`.

### 2. Görsel dosya adlarında rakip klinik isimleri
**Bulgu:** En az **61 görselin** dosya adı `...-ossur-ottobock-luxmed-nesa-proklinik-...` kalıbında.
Örnek: `Ozgur-protez-liner-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak-comfort-scs-01.png`
**Zemin:** Luxmed / Nesa / Proklinik **rakip firmalar**. Rakibin ticaret unvanını kendi sitesinin
metadata'sına gömmek → haksız rekabet (TTK m.54-55) + marka hakkına tecavüz iddiası (SMK).
Arama trafiğini rakip adı üzerinden çekmek bu alanın klasik dava konusu.
**Bu listenin en somut dava riski budur** — TİTCK'den farklı olarak burada davacı rakibin kendisidir.
**Aksiyon:** 61+ görsel yeniden adlandırılıp yeniden yüklenmeli, eski medya silinmeli.

### 3. Üretici marka adları URL/slug içinde
**Bulgu:** `genium`, `genium-x3`, `axonhook`, `axonskin-visual-axonskin-black`, `1c59-taleo-adapt`,
`1c56-taleo-adjust`, `1c51-taleo-vertical-shock`, `1a1-2-empower`, `1c30-1-trias`,
`1c70-evanto-prosthetic-foot`, `i-limb-ultra-el`, `i-limb-quantum-el`, `livingskin-el`,
`1e97-sprinter-junior`, `pro-flex-xc-torsion-ayak` — Ottobock/Össur tescilli adları.
**Zemin:** Distribütörlük/görsel-marka kullanım izni belgesi yoksa çift risk: marka hukuku +
TİTCK tanıtım kapsamı. (Avukat sorusu #8; durum dosyasındaki IP bayrağının aynısı.)
**Aksiyon:** Özgür Bey'den yazılı kullanım izni/distribütörlük teyidi; gelmezse slug'lar jenerikleştirilir.

### 4. KVKK: üç formun hiçbirinde aydınlatma metni ve açık rıza yok
**Bulgu:**
| Form | Toplanan | Durum |
|---|---|---|
| `Contact` (TR, güncellendi 26 Tem) | Ad, soyad, e-posta *(zorunlu)*, konu, **serbest metin "Mesaj"** | Aydınlatma yok, rıza kutusu yok |
| `Inquiry Services Form` (1 Eyl) | Ad, soyad, **telefon (zorunlu)** | Aydınlatma yok, rıza kutusu yok |
| `Subscriptions` | E-posta + abonelik onayı | Aydınlatma yok |
**Zemin:** Serbest metin alanına hasta kaçınılmaz olarak sağlık bilgisi yazar → **özel nitelikli
kişisel veri**, ayrı açık rıza şart. Veri Wix altyapısına akıyor → **yurt dışına aktarım** rejimi.
**Aksiyon:** KVKK v01 metni hazır ama sitede değil. Politika + form aydınlatması + rıza kutusu
birlikte devreye alınmalı; sağlık detayı formdan çıkarılıp görüşmeye bırakılmalı (§A.3 form tasarımı).

---

## 🟡 DİKKAT — yayın kalitesi ve ikincil yaptırım

### 5. Newsletter formu — İYS / ETK riski
`JOIN OUR MAILING LIST` / `SUBSCRIBE NOW` ile ticari elektronik ileti izni toplanıyor.
6563 sayılı ETK: İleti Yönetim Sistemi (İYS) kaydı ve usulüne uygun onay metni gerekir; idari para
cezası bağlı. Ayrıca onay kutusu `required: true` — **onay vermeden form gönderilemiyor**;
zorunlu onay KVKK'nın "özgür irade" şartını da zedeler. Form İngilizce.

### 6. 7 Eylül'de yayınlanan blog yazısında tıbbi sorumluluk reddi yok
Diğer iki yazının sonunda "Bu içerik genel bilgilendirme amaçlıdır…" ibaresi var; **"Diz Üstü
Protezlere Detaylı Bakış"ta yok.** Aynı yazı *"merkezimizde kullanılan biyomekanik analiz ve
ayarlama sistemi"* diyor — bu, Yürüme Analizi sayfasında **envanter teyitsiz** olduğu için
bloke ettiğimiz iddianın ta kendisi. Teyitsizse yanıltıcı beyan (TKHK / Reklam Kurulu).
Yazı Ayhan talimatıyla denetimden geçmeden yayınlandı; kapı burada kaçtı.

### 7. Şablon artığı İngilizce form canlı şemada
`Inquiry Services Form` (1 Eyl'de oluşmuş) "Service Inquiry" başlıklı ve seçenekleri:
**Menu Design · Online Menu Setup · Brand Identity.** Protez merkezinde menü tasarımı seçeneği.
Yasal ihlal değil ama tıbbi ciddiyeti ve güveni doğrudan zedeler.

### 8. Kullanılmayan uygulamalar veri yüzeyi açıyor
Kurulu ama işe yaramayan: **Wix Members Area · Wix Groups · Wix Hotels · Wix Invoices · Wix Chat.**
Members Area = üyelik verisi; Chat = anlık mesajla sağlık verisi akar, aydınlatma yok.
KVKK m.4 veri minimizasyonu gereği kullanılmayanlar kaldırılmalı.

### 9. Katalog hijyeni — yanlış cihaz eşleşme riski
"Mikroişlemcili Diz Eklemi" adı **üç ayrı üründe** aynı; "Çocuk Koşu Ayağı" ve "Miyoelektrik Çok
Eklemli El" de tekrarlı. Slug'lar şablon artığı: `camo-backpack`, `canvas-backpack`,
`i-m-a-product-11`. Tıbbi cihaz bilgilendirmesinde hangi cihazın anlatıldığının belirsiz olması
sıradan bir özensizlik değil — yanlış cihaz beklentisi doğurur.

### 10. "Stokta var" beyanı ısmarlama üretimle çelişiyor
Ürünlerin ezici çoğunluğu `IN_STOCK`. Ismarlama protez-ortez stoktan satılmaz; bu beyan hem
gerçeğe aykırı hem de 1. maddedeki "mağaza" görüntüsünü pekiştiriyor.

---

## ✅ TEMİZ — denetlendi, sorun çıkmadı
- **Blog dili uyumlu.** 3 yazının hiçbirinde fiyat, kampanya, indirim, testimonial, "en iyi/tek/
  garantili/%X başarı" ifadesi yok. Koşullu dil doğru kullanılmış ("yardımcı olabilir",
  "desteklenmesi hedeflenir"). İki yazıda tıbbi disclaimer mevcut (istisna: madde 6).
- **Promosyon rozeti yok** — 115 üründe tek "New" etiketi dışında kampanya işareti bulunmadı.
- **Site Draft.** Maruziyet şu an sıfır.

---

## Avukata eklenecek 3 yeni soru
*(mevcut 10 soru: `marka-bulutu-os-medikal-protez-bagi.md` §A.4)*
11. Rakip firma adlarının (Luxmed, Nesa, Proklinik) görsel dosya adı/metadata'sında bulunması
    haksız rekabet veya marka tecavüzü sayılır mı; geçmişe dönük sorumluluk doğar mı?
12. Ticari elektronik ileti (newsletter) için İYS kaydı bu merkez açısından zorunlu mu; sağlık
    kuruluşu istisnası var mı?
13. Sitede sepet/ödeme akışı kapalı olsa bile **ürün kataloğu formatının kendisi** "satışın
    yapıldığı internet ortamı" sayılır mı — yoksa M.15/2 bilgilendirme istisnası bu formatı da korur mu?

---

## Önerilen sıra (bağımlılığa göre)
1. **Görsel yeniden adlandırma** (madde 2) — avukat beklemez, tek somut dava riski, bugün başlar.
2. **Formlar + KVKK** (madde 4, 5) — metin hazır, yayın kapısında zaten duruyor.
3. **Mağaza → bilgilendirme dönüşümü** (madde 1) — en büyük iş, Editör oturumu gerekir.
4. **Blog disclaimer + biyomekanik iddia teyidi** (madde 6) — Özgür Bey'in teknik teyit mesajına eklenir.
5. **Uygulama temizliği + katalog hijyeni** (madde 8, 9, 10) — Editör oturumunda birlikte.
