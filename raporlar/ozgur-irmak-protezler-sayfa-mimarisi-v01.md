# Özgür Irmak — "Protezler" Menü & Anlatı Sayfası Mimarisi (v0.1)

*Fox · 1 Eylül 2026 · Ayhan emri: menüye Protezler dalı, **anlatı sayfaları** olarak (kategori değil). Ürünlere dokunulmadı.*

> **Karar (Ayhan, 1 Eyl):** Bu kırılım **mağaza kategorisi değil**, bilgilendirme sayfası mimarisidir. Her kırılım = kendi URL'i, kendi metni, kendi SEO hedefi olan bir sayfa. `Protezler` mağaza kategorisindeki **51 ürüne dokunulmaz.**

---

## 0 · NEDEN BU İŞ ZATEN AÇIK BİR BORÇTU (kanıt)

Bu sayfalar yeni bir fikir değil — mevcut içerik mimarisi **onları varsayarak** kuruldu ve yazılmadıkları için bir boşluk oluştu:

- `ozgur-irmak-hakkimizda-v05.md:60` — *"Anahtar kelime devri: … **tamamı Çözümler kategori sayfalarına.** Bu sayfa artık bu kelimelerde yarışmıyor; **o sayfalar yazılmadan bu kelimelerde görünürlük beklenmez.**"*
- `hakkimizda-v01:155` / `v02:170` / `v03:99` — *"Uzun-kuyruk (**aktif vakum, pin sistemli**, dezartikülasyon, DAFO, kanal sayıları) **Çözümler sayfalarına aittir** — buraya yığılmaz."*

→ Ayhan'ın istediği kırılım, Hakkımızda'dan bilinçli olarak **çıkarılmış** kelimelerin kurulu adresidir. Şema ile çelişmiyor; şemanın eksik halkasını kapatıyor.

**Sonuç:** `aktif vakum`, `pin sistemli`, `diz altı protez`, `diz üstü protez` kelimelerinde site bugün **yarışmıyor.** Bu sayfalar o yarışı açar.

---

## 1 · SAYFA AĞACI (Ayhan şeması — birebir)

```
Protezler                                    [hub]
├── Bacak Protezleri                         [ara hub]
│   ├── Diz Altı Protezleri                  [ara hub]
│   │   ├── Aktif Vakum Sistemli Protezler   [uç sayfa]
│   │   ├── Pasif Vakum Sistemli Protezler   [uç sayfa]
│   │   ├── Silikonliner Pin Sistemli Prot.  [uç sayfa]
│   │   └── Modüler Klasik Protezler         [uç sayfa]
│   └── Diz Üstü Protezleri                  [uç sayfa — §3'e bak]
└── Kol Protezleri                           [uç sayfa]
```

**Toplam 9 sayfa.** 3 hub + 6 uç sayfa.

## 2 · URL ŞEMASI (ASCII — Türkçe karakter YOK)

| # | Sayfa | Slug | Menü etiketi |
|---|---|---|---|
| 1 | Protezler | `/protezler` | Protezler |
| 2 | Bacak Protezleri | `/bacak-protezleri` | Bacak Protezleri |
| 3 | Diz Altı Protezleri | `/diz-alti-protezleri` | Diz Altı Protezleri |
| 4 | Aktif Vakum Sistemli Protezler | `/aktif-vakum-sistemli-protezler` | Aktif Vakum Sistemli |
| 5 | Pasif Vakum Sistemli Protezler | `/pasif-vakum-sistemli-protezler` | Pasif Vakum Sistemli |
| 6 | Silikonliner Pin Sistemli Protezler | `/silikonliner-pin-sistemli-protezler` | Silikonliner Pin Sistemli |
| 7 | Modüler Klasik Protezler | `/moduler-klasik-protezler` | Modüler Klasik |
| 8 | Diz Üstü Protezleri | `/diz-ustu-protezleri` | Diz Üstü Protezleri |
| 9 | Kol Protezleri | `/kol-protezleri` | Kol Protezleri |

⚠️ **Slug'da Türkçe karakter kullanılmaz.** Gerekçe: SOC'de `/hakkımızda` (noktasız ı) kuruldu, `/hakkimizda` (Latin i) **404 verdi** → redirect kurmak zorunda kalındı ([[steps-on-clouds-wix-site]]). Medikal SEO sitesinde bu hata tekrarlanmaz. Sayfa **başlığı** Türkçe ve tam (`Diz Altı Protezleri`), yalnız **slug** ASCII.

## 3 · ⚠️ DİZ ÜSTÜ NEDEN ALT KIRILIMSIZ — ve bu DOĞRU

Ayhan'ın şemasında Diz Altı 4'e bölünürken Diz Üstü bölünmüyor. Bu bir eksik değil, **teknik olarak tutarlı** bir tercih:

- Diz Altı'nın 4 kırılımı (aktif vakum · pasif vakum · silikonliner pin · modüler klasik) hepsi **süspansiyon/bağlantı sistemi** ekseninde. Tek eksen, temiz kırılım.
- Diz Üstü'nün doğal kırılımı ise **diz eklemi tipi** (mikroişlemcili · hidrolik · pnömatik · mekanik) — **başka bir eksen.**

Bu ayrımı Denetmen zaten bir kez yakalamıştı: *"süspansiyon sistemleri (vakum/pin) ile diz tipleri (hidrolik/pnömatik/mikroişlemcili) tek seriye dizilmiş"* — TR metninde karışmıştı, EN'de doğru ayrılmıştı (`denetmen-ozgur-irmak-hakkimizda-denetim.md:233`, bulgu N3).

→ **Öneri:** Diz Üstü şimdilik tek sayfa kalsın; içinde diz eklemi tipleri **bölüm** olarak anlatılsın. İleride ayrı sayfalara bölünecekse ekseni "diz eklemi tipi" olarak adlandır — "vakum/pin" ile aynı seviyeye dizme. **Ayhan onayı gerekmez, mevcut şema zaten böyle; bilgi olarak not.**

## 4 · ⚠️ MENÜ DERİNLİĞİ — Editör oturumunda karar

Ağaç **4 seviye** derin (Protezler → Bacak → Diz Altı → Aktif Vakum). Header açılır menüsünde 4 seviye:

- Wix klasik editörde render **edilebilir ama doğrulanmadı** — Editör oturumunda kontrol edilecek.
- Render etse bile 4 seviyeli hover menüsü **WCAG AA'da düşer** (klavye navigasyonu + hedef boyutu). HAT 4 bu siteye WCAG AA tabanı şart koşuyor; bu marka *erişilebilirlik satıyor* — menüsü erişilemez olamaz.

**Fox önerisi — menü 2 seviye, sayfa 4 seviye:**

```
MENÜ (header):  Protezler ▾ → Bacak Protezleri · Diz Üstü Protezleri · Kol Protezleri
SAYFA içi:      Bacak Protezleri sayfası → Diz Altı / Diz Üstü kartları
                Diz Altı sayfası → 4 sistem tipi kartı (her biri tam sayfa)
```

9 sayfanın hepsi kurulur ve URL'i olur; yalnız **menüde 4 kat açılır liste olmaz.** Derinlik breadcrumb + sayfa içi kartlarla taşınır. Ayhan aksini isterse 4 seviye menü de kurulur — kararı Editör oturumunda ekrana bakarak veririz.

## 5 · SAYFA İSKELETİ (her uç sayfa aynı şablon)

Madde 15/2 yatağında — *"cihaz nedir, kime uygulanır, süreç nasıl işler"*:

1. **H1** — sayfa adı (birebir, kelime oyunu yok)
2. **Bu nedir** — sistemin tanımı, sade dil, 2-3 paragraf
3. **Kimler için uygundur** — aktivite düzeyi, güdük yapısı, günlük kullanım profili
4. **Nasıl çalışır** — mekanizma, sade anlatım
5. **Süreç** — ölçü → prova → teslim → takip (site geneliyle tutarlı)
6. **Sık sorulanlar** — 3-5 soru (AI-SEO yüzeyi)
7. **CTA** — danışma/randevu talebi (tek, net, sürtünmesiz)

**Hub sayfalar (Protezler · Bacak · Diz Altı):** kısa yönlendirici metin + alt sayfa kartları + breadcrumb. Uç sayfalarla **keyword kanibalizasyonu yapmaz** — hub geniş terimi, uç sayfa uzun-kuyruğu tutar.

## 6 · ANAHTAR KELİME DAĞITIMI (Hakkımızda'dan devredilen)

| Sayfa | Birincil | İkincil |
|---|---|---|
| Protezler | protez ve ortez merkezi | protez çeşitleri |
| Bacak Protezleri | bacak protezi · protez bacak | protez bacak fiyatları ⚠️ (§7) |
| Diz Altı Protezleri | diz altı protez | tibia protezi · şeffaf soket |
| Aktif Vakum Sistemli | aktif vakum protez | elektrikli vakum · vakum süspansiyon |
| Pasif Vakum Sistemli | pasif vakum protez | mekanik vakum süspansiyon |
| Silikonliner Pin Sistemli | pin sistemli protez | silikon liner · shuttle lock |
| Modüler Klasik | modüler protez | klasik protez · endoiskelet |
| Diz Üstü Protezleri | diz üstü protez | mikroişlemcili diz · femur protezi |
| Kol Protezleri | kol protezi · protez kol | miyoelektrik protez · biyonik kol |

⚠️ İkincil kelimeler **hipotez** — gerçek arama hacmi taraması yapılmadı. Keyword araştırması HAT 3'te açık boşluk olarak duruyor. Yayın öncesi doğrulanmalı; **bu tablo şu haliyle "ölçülmüş" diye sunulamaz.**

## 7 · ⚖️ UYUM KAPISI (her sayfaya, istisnasız)

**Yasal yatak:** Madde 15/2 — *"…satış merkezlerinin resmî internet sitelerinde yapmış oldukları **cihaz bilgilendirmeleri**, birinci fıkra hükümleri kapsamı dışındadır."* Resmî site, cihaz bilgilendirmesi için **açık alandır.** Sınır: bilgilendirme ≠ reklam.

**Sıfır tolerans — yasak dil:**
- ❌ "en iyi / kesin çözüm / garantili sonuç" (18/6-b)
- ❌ **fiyat · indirim · kampanya · promosyon** → §6'daki "protez bacak fiyatları" kelimesi **hedeflenmez**; M.5 ücret bilgisini yasaklıyor
- ❌ aciliyet dili · "sepete ekle / satın al" (internet satışı yasak) · çekiliş
- ❌ karşılaştırma/üstünlük iddiası · hasta görseli · öncesi-sonrası · **testimonial**

**Denetmen 15/2 testi (her sayfaya 3 soru):** ① Bilgilendirme mi reklam mı — satın almaya iten dil var mı? ② 18/6 yanıltıcılık kalıplarına değiyor mu? ③ Hedef tüketici mi meslek mensubu mu?

**Yaptırım:** ihlal → uyarı → 3 iş günü içinde düzeltilmezse **15 gün satış durdurma** (15/5). Kriz protokolü: uyumlu ticaret planı §4.

## 8 · AÇIK BAĞIMLILIKLAR (bu sayfalar bunlarsız yayınlanmaz)

| # | Bağımlılık | Kimde | Bloklar mı |
|---|---|---|---|
| 1 | **Editör oturumu** — klasik editörde sayfa/menü kurmanın REST API'si YOK. Fox şifre girmez (Kademe 3). | Ayhan | 🔴 Kurulumu bloklar |
| 2 | **Teknik veri teyidi** — 4 sistem tipinin merkezde fiilen uygulanan hangi ürünlerle karşılandığı. Uydurulamaz (medikal, sıfır tolerans). | Özgür Bey | 🔴 Metni bloklar |
| 3 | **Avukat onayı** — dil rejimi örnek sayfayla onaylanacak (uyumlu ticaret planı, Soru 1 yeniden çerçevelendi). | Ayhan → avukat | 🔴 Yayını bloklar |
| 4 | **Metin üretimi** — prosa Metin Yazarı'nın kulvarı (CLAUDE.md §6: Fox içerik üretmez, koordine eder). | Ayhan onayı | ⚠️ Fox tek başına başlatmaz |
| 5 | Keyword araştırması (§6 ikincil kelimeler hipotez) | Fox/Growth | ⚠️ Yayını bloklamaz, kaliteyi düşürür |

⚠️ **Site zaten Draft ve 404.** Bu sayfalar kurulsa bile mevcut yayın blokajı (Free plan · dil yalnız `tr` · avukat kapısı) açılmadan kimse göremez. `fox-durum.md` risk bayrağı — bu iş o blokajı **çözmez**, stoka bir kalem daha ekler. Yayın kası açılmadan 9 sayfa daha üretmek ölçülmemiş iştir ([[yayin-kasi-cikti-canlida-kapanir]]).

---

## 9 · SIRADAKİ ADIM (Fox önerisi)

1. **Ayhan:** Editör oturumu günü belirle → 9 sayfa iskeleti + menü kurulur (Fox tarayıcıyı sürer, Ayhan giriş yapar). Menü derinliği kararı orada ekrana bakarak verilir.
2. **Ayhan → Özgür Bey:** 4 sistem tipi için teknik teyit talebi (Yürüme Analizi 11 kalem + Levitate 4 kalem taleplerine eklenir — tek mesajda gider, ayrı ayrı rahatsız etmeye gerek yok).
3. **Teyit gelince:** Metin Yazarı 9 sayfayı üretir → Denetmen (15/2 testi + İnsan Sesi kapısı) → avukat → yayın.

*Kaynaklar: `ozgur-irmak-web-semasi.md` · `ozgur-irmak-uyumlu-ticaret-plani.md` §1-2, §6 · `denetmen-ozgur-irmak-hakkimizda-denetim.md` N3 · `ozgur-irmak-hakkimizda-v05.md` §anahtar kelime devri · `ozgur-irmak-kalan-hatlar.md` HAT 4*
