# Özgür Protez — Ürün Görseli Envanteri & İndirme Standardı
*Fox · 16 Ağustos 2026 · Konum: Ayhan'ın masaüstü (Fox reposunda değil — 200MB+ ikili dosya)*

> **Neden bu dosya var:** Össur/Ottobock/Fior Gentz görselleri Temmuz–Ağustos'ta indirildi ama **standardı hiçbir yerde yazılı değildi.** 16 Ağu'da Proteor eklenirken standart klasörlerden geriye mühendislikle çıkarıldı. Bir dahaki markada tahmin edilmesin diye buraya yazıldı.

---

## 1 · STANDART (mevcut klasörlerden çıkarıldı, Proteor'da uygulandı)

**Klasör adı:** `<Marka>-Protez-Gorselleri` · `<Marka>-Yurume-Cihazi-Gorselleri`
· Sonuna **` Temiz`** eklenmişse: indirme sonrası **ayıklama turu yapılmış** demektir (tekrar kareler + bozuk/aşırı yakın kırpımlar çıkarılmış). Kalanların numarası korunur, boşluk normaldir (`-01 -03 -05 …`).

**Ürün alt klasörü:** `<Kategori>_<ürün kodu> - <ad>`
· Kategoriler: **Ayak · Diz · El · Kisa** (kısa yürüme cihazı/AFO) · **Uzun** (KAFO) · *(Proteor'da eklendi:* **Sistem** *— diz+bilek+ayak bütünleşik)*
· Ürün kodu varsa öne (`Ayak_1C30-1 - Trias`), yoksa yalnız ad (`Ayak_Pro-Flex-Terra`).

**Dosya adı (sabit SEO öneki + ürün slug + 2 haneli sıra):**
```
Ozgur-protez-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak-<slug>-NN.<uzantı>
```
· Ortez/yürüme cihazı klasörlerinde önek `Ozgur-protez-**ortez**-ossur-…` olur.
· Önek **markadan bağımsız sabittir** — El/Diz ürünlerinde bile `bacak-ayak` geçer. Proteor'da aynen korundu (bkz. §4 açık karar).

---

## 2 · ENVANTER (16 Ağu 2026)

| Klasör | Ürün | Görsel | Ayıklandı mı |
|---|---:|---:|---|
| Ossur-Protez-Gorselleri Temiz | 20 | 64 | ✅ |
| Ossur-Yurume-Cihazi-Gorselleri Temiz | 4 | 7 | ✅ |
| Ottobock-Protez-Gorselleri Temiz | 35 | 156 | ✅ |
| Ottobock-Yurume-Cihazi-Gorselleri | 10 | 36 | ❌ ham |
| Fior-Gentz-Yurume-Cihazi-Gorselleri | 37 | 138 | ❌ ham |
| **Proteor-Protez-Gorselleri** | **35** | **338** | ❌ ham (16 Ağu) |

> ⚠️ **16 Ağu tespiti:** Össur ve Ottobock'un 4 klasörü o gün masaüstünde **görünmez oldu** (Çöp Kutusu boş, aynı anda masaüstüne yeni dosyalar geldi → iCloud Masaüstü senkronu ya da başka cihazdaki taşıma). Yukarıdaki sayılar aynı gün ölçülen son gerçek değerlerdir. **Ayhan iCloud Drive → Masaüstü'nden teyit etmeli.**

### Proteor detayı (16 Ağu, yeni)
- **315** ürün görseli · **18** yaşam karesi (`_Yasam-Kareleri/`) · **5** ikon/piktogram (`_Ikon-Piktogram/`) · 222 MB
- **34/35 üründe** ürün çekimi var · 800px altı **sıfır** · 1000px+ **101** görsel
- Kaynak: `proteor.com/components/` + `us.proteor.com` (modern `/feet/ /knees/ /ankles/` + eski `/composants/`), içerik hash'iyle tekilleştirildi.
- Üretim betiği: `sablonlar/araclar/proteor_gorsel_indir.py`

---

### Zebris — yürüme analizi cihazı (17 Ağu, yeni klasör tipi)
`~/Desktop/Zebris-Yurume-Analizi-Gorselleri/` · **10 görsel** · 4,8 MB · kaynak `zebris.de/en/medical/*` · betik `sablonlar/araclar/zebris_gorsel_indir.py`

**Neden standarttan sapıyor (bilinçli):** Bu klasör *ürün* değil *hizmet sayfası* besliyor. Üç sapma:
1. Klasör adı `Zebris-Yurume-**Analizi**-Gorselleri` — mevcut `…-Yurume-Cihazi-…` ortez/AFO demek, çakışmasın diye.
2. Alt klasör yok (10 dosya, tek düzey).
3. Dosya adı öneki `ozgur-protez-yurume-analizi-` — rakip klinik adları (`luxmed-nesa-proklinik…`) **gömülmedi**; küçük harf. Ayhan sabit öneki isterse toplu adlandırma 1 dakika.

| Dosya (önek `ozgur-protez-yurume-analizi-`) | Ne | Çözünürlük |
|---|---|---|
| `zebris-fdm-t-klinik-yurume-bandi.jpg` | h/p/cosmos tabanlı klinik band, ürün çekimi | 4000×3091 |
| `zebris-fdm-t-yurume-bandi-tutamakli.jpg` | Tutamaklı + oturaklı klinik varyant | 4000×3091 |
| `zebris-ayak-tabani-basinc-haritasi-3d.png` | Band üzerinde 3B basınç tepeleri | 2103×897 |
| `zebris-yurume-analizi-yazilimi-kamera-gorunumu.jpg` | Yazılım: 3B basınç + senkron video | 1200×719 |
| `zebris-ayak-yuvarlanma-basinc-dagilimi-ekrani.jpg` | Yazılım: sağ/sol yuvarlanma haritası | 1200×719 |
| `zebris-statik-durus-analizi-ciplak-ayak.jpg` | Yazılım: statik duruş + yük dağılımı %'leri | 1200×719 |
| `zebris-yurume-analizi-raporu.jpg` | Çıktı raporu sayfaları | 1200×675 |
| `zebris-yurume-yolu-basinc-olcum-platformu.jpg` | Uzun yürüme yolu basınç platformu | 1200×798 |
| `zebris-pdm-c-basinc-olcum-platformu.jpg` | Platform + ekran, kullanım karesi (insanlı) | 1999×2622 |
| `zebris-ayak-basinc-dagilimi-3d-model.jpg` | Tek ayak 3B basınç modeli | 852×416 |

**Render-and-review iki hata yakaladı — ikisi de dosya adına güvenmekten:**
- `Laufbaender/TLR4_h.jpg` (4167px, en yüksek çözünürlüklü kare) **Reebok tüketici koşu bandı.** Medikal sayfada klinik cihaz gibi durur → elendi.
- `Trittschaum_Aufsicht_260520.jpg` — "Aufsicht" üstten görünüm; içerik **boş teal plaka**, basınç haritası değil → `Trittschaum_Druckgebirge` ile değiştirildi.
- Teknik not: zebris.de TYPO3; sayfada görseller 576px `_processed_` türev. Orijinal yalnız lightbox `href`inde ya da `srcset`in son adımında. Türevi indiren bir betik 10 karenin 10'unu da 576px alırdı.

## 3 · BULGULAR (Proteor turu)

1. **🔴 ALLUX 2 — görsel yok.** Proteor'un kendi 3 sayfasında da tek görsel var, o da **404 ölü bağlantı** (`Visuel-paysage-prothese.jpg`). Üreticinin sitesindeki kırık bağlantı; bayi sitesinden çekilmedi (üçüncü taraf telifi + düşük kaynak güvenilirliği). **Görsel doğrudan Proteor'dan istenmeli.**
2. **⚠️ Proteor'un varlık kalitesi Össur/Ottobock'un altında.** Össur/Ottobock 1400–1600px kare veriyor; Proteor'un eski Freedom hattında (Sierra, Agilix, Plie 3, RUSH ailesi, Pacifica) **orijinaller 279×349px**. Kırpılmış değil — kaynağın kendisi o. ABD sitesi birleştirilerek 800px altı sıfıra indirildi ama bazı ürünlerde tavan 952px'te kalıyor.
3. **⚠️ Yürüme cihazı tarafı Proteor'da ürün granülünde yok.** `proteor.com/equipment/` sayfaları ürün değil **kategori** sayfası (ankle-foot-orthoses, leg-orthoses…). Ottobock/Fior Gentz'deki gibi `Kisa_/Uzun_` ürün klasörü kurulamaz. Bu yüzden **yalnız `Proteor-Protez-Gorselleri` kuruldu.**
4. **✅ Doğrulandı, hata değil:** Ottobock klasöründeki F23/F24 Maverick, VS4 Kintrol, VS5 Restore, LP2-W2 Freestyle Swim **doğru yerde.** 2020 Freedom Innovations devrinde Ottobock Maverick ailesini ve Kintrol'ü **elinde tuttu**; Proteor'a Plie3, Kinnex, Kinterra, Agilix, DynAdapt, Sierra, Highlander, Pacifica geçti.

---

## 4 · AÇIK KARARLAR (Ayhan)

| # | Karar | Fox'un varsayımı (uygulandı) |
|---|---|---|
| 1 | Dosya adı önekine `proteor` eklensin mi? | **Eklenmedi** — önek site geneli sabit dize. Toplu yeniden adlandırma 1 dakikalık iş, geri alınabilir. |
| 2 | Proteor klasörü "Temiz" turundan geçsin mi? | Ham bırakıldı; ayıklama Ayhan'ın gözüyle yapılır. |
| 3 | ALLUX 2 görselleri Proteor'dan istenecek mi? | Beklemede. |

---

## 5 · 🔴 TELİF BAYRAĞI (dört marka için de geçerli — kapanmadı)

Bu görsellerin tamamı **üreticinin telifli materyalidir.** Yazılı kullanım izni / bayilik belgesi olmadan sitede yayınlanması:
- telif ihlali riski,
- **belgesiz "yetkili bayi" iması** (medikal bağlamda ayrıca ağır),
- Wix'in kendi ürün alanı uyarısıyla da çelişir (*"Write your own description instead of using manufacturers' copy"*).

Aynı bayrak Özgür Irmak marka kimliği denetiminde **"Össur telifli görseller"** maddesi olarak zaten açılmıştı — kapanmadı, Proteor'la birlikte kapsamı büyüdü. **Zebris'te bayrak bir kat daha ağır (17 Ağu):** görsel yalnız telif değil **cihaz sahipliği iması** taşıyor. Merkezde birebir bu cihazın bulunduğu teyit edilmeden Zebris marka görseli sitede kullanılırsa, sayfa sahip olunmayan bir cihazı gösterir — bu telif değil **yanıltıcı tanıtım**dır (TİTCK alanı). Yürüme Analizi sayfasının 11 kalemlik teknik teyidi (Denetmen D1) bu görsellerin de kapısıdır.
**Fox avukat değildir; işaretler.** Yayın öncesi: ya üreticiden yazılı görsel kullanım izni, ya kendi çekimlerimiz.

*Yan not (sarı):* Dosya adlarında rakip klinik adları gömülü (`luxmed-nesa-proklinik-teknik-ortopedi`). SEO kazancı ile marka hijyeni arasında Ayhan kararı — ayrı ele alınacak.

---
*Bağlı belgeler: `raporlar/ozgur-irmak-urun-metinleri-uyum-plani.md` (73 Wix ürünü, metin tarafı) · `marka-bulutu-os-medikal-protez-bagi.md` (TİTCK/uyum zemini)*
