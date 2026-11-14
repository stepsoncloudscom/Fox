# Fox — TESLİM KÜTÜĞÜ
*Açılış: 14 Ağustos 2026. CLAUDE.md §5'in ("ölçü, kabul edilen teslim başına token") ve fox-generallik-doktrini "Generalin Sınavı"nın veri tabanı.*

## Neden var
§5 Haziran'dan beri yazılı, **tek satır veri yoktu.** Ölçülmeyen şey yönetilmiyor: hangi işin kaç turda kapandığı, redlerin neden geldiği, hangi ajanın ilk turda tutturduğu — hepsi hafızada kalıyordu, hafıza da oturumla birlikte gidiyordu.

**Bugün dürüstçe ölçebildiğim şey token değil, yeniden-iş.** Geçmiş oturumların token'ı geri alınamaz; tur sayısı ve red sebebi dosyalardan doğrulanabilir. Asıl maliyet sürücüsü de zaten bu: bir işi dört kez yazmak, bir kez yazıp bir kez denetlemekten pahalıdır. Token sütunu **bu tarihten sonraki** işlerde doldurulur.

## Doldurma kuralı
- Bir satır = **dışarı çıkan bir teslim** (müşteriye/yayına giden). İç not, araştırma, taslak ara sürümü satır açmaz — tur sayısına yazılır.
- Satır, iş **kapandığında** yazılır (kabul / red / bloklu).
- **Red sebebi boş bırakılamaz.** Red kaydı olmayan bir öğrenme döngüsü yoktur.
- Ayın son oturumunda alt tabloya rollup: toplam teslim · ilk-turda-kabul oranı · ortalama tur · en sık red sebebi.

## Kütük

| # | Tarih | Teslim | Cephe | Ajan(lar) | Tur | Denetmen | Ayhan | Red/blok sebebi | Token |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 30 Tem 2026 | Blog: protez bakımı & günlük kullanım | Özgür Protez | Metin Yazarı → Denetmen → Growth → İçerik | v01→v04 | GERİ (5 düzelt) | ✅ Yayınlandı | Nöropati vigilance açığı · disclaimer eksik · YMYL künye · SERP niyeti yanlış (diş protezi) | — |
| 2 | 8 Ağu 2026 | Hakkımızda sayfası | Özgür Protez | Metin Yazarı | v01→v07 | onaylı | ⏳ Belge kapısında | **Ayhan redi (2 kez): "üslup kesik, akmıyor" · "Özgür Bey ölü, hikâye yok"** → İnsan Sesi Kapısı + sozdizim_tarama.py bu redden doğdu | — |
| 3 | 8 Ağu 2026 | Blog 4 yazı (liner/türler/miyoelektrik/süreç) | Özgür Protez | Metin Yazarı | v01→v02 | — | ⏳ Wix draft | İnsan Sesi Kapısı geçişi (AI sözdizimi) | — |
| 4 | 13 Ağu 2026 | Yürüme Analizi çözüm sayfası | Özgür Protez | Metin Yazarı → Denetmen | v01→v02 | **GERİ** (7 DUR · 7 DÜZELT · 9 NOT) | 🔴 Bloklu | Sayfanın tamamı **teyitsiz tedarikçi şartnamesi** verisine dayanıyordu; ayrıca 3 adımlık talep-yaratma dizisi (TİTCK M.5) | — |
| 5 | 14 Ağu 2026 | Süreklilik onarımı (durum bölme + hook'lar + bu kütük) | Fox içi | Fox | v01 | — | ✅ Onaylı (A/B/C) | — | — |
| 6 | 15 Ağu 2026 | Kanıt hattı: Özgür Protez TZP (geriye dönük) + Kanıt Üçgeni T0 | Fox içi / Özgür Protez | Fox | v01 | — | — | Ölçüm sırasında **🔴 site yayında değil** bulgusu çıktı (404 · Draft · Free plan) — 6 haftalık üretim kamuya görünmüyor. Kök neden: 9 merceğin hiçbiri **erişim** sormuyordu → Denetmen 10. mercek eklendi | — |

| 7 | 15 Ağu 2026 | Ürün tanımı iskeleti (K0-K3) + Pipeline Ajanı taslağı | Fox içi | Fox | v01 | — | ⏳ 5 açık karar Ayhan'da | Fiyat/kapsam Fox'un kararı değil — slotlar `[AYHAN]` bırakıldı (§11.5) | — |
| 8 | 16 Ağu 2026 | Sosyal biyografiler (IG/FB/LinkedIn ×2/YouTube — 12 blok) | Özgür Protez | Metin Yazarı → Denetmen → Fox doğrulama | v01→v02 | **GERİ** (4 🔴 · 11 🟡) | ⏳ Ayhan'da (slot verisi + 2 karar) | ① **Kanal kuşağı yanlış okundu** — sosyal medya §2 SARI kuşak, v01 §1'e atıfla "yeşil" demişti (tek yanlış bölüm atfı 4 bulgu doğurdu) ② **"Ataşehir" hiçbir belgede yok**, 5 yüzeyde olgu gibi kullanılmış ③ miyoelektrik/mikroişlemcili **kapasite iddiası belgesiz** ④ bio yazımı migrasyonun son adımı sayılmadı (canlı arşiv denetlenmemiş) ⑤ öz-puan 88/100 ölçümsüz (Doğruluk 20/20 — teyitsiz olgu barındıran metinde) | — |
| 9 | 3 Kas 2026 | Ecem Yaşar — YouTube taraması (Fox) + dijital kurumsal duruş denetimi (Keşif) | Ecem Yaşar (Lead) | Fox + Keşif → Denetmen (Verification) | v01→v02 | **DİKKAT** (DUR yok) | ⏳ temas noktası/kapsam/fiyat Ayhan'da | ① **Gözlem yereli kaydedilmedi** — Fox, İngilizce arayüzde görülen Shorts başlıklarını "dil karmaşası" 🔴 saydı; hl=tr'de başlıklar Türkçe → madde geri çekildi. **Kapı:** Keşif çıktısına + Verification yöntemine `hl/gl + giriş` alanı (3 Kas) ② "büyük kısmı" iddiası ölçümsüz (gerçek ~%25) ③ kişisel veri kalıntısı (telefon ilk hanesi, e-posta öneki) ④ unvan sorularında sorgu/ima tonu | Keşif ~202k + Denetmen ~172k + Fox |

## Aylık rollup

| Ay | Teslim | İlk turda kabul | Ort. tur | En sık red sebebi |
|---|---|---|---|---|
| Ağu 2026 | *(ay sonunda)* | | | |

## Şimdiden görünen örüntü (5 satır, temkinli okuma)
Redlerin **hiçbiri** biçim/format hatası değil — üçü de **kaynak yokluğu** ile ilgili: teyitsiz veriyle yazmak (4), yaşanmışlık olmadan hikâye kurmaya çalışmak (2), ölçülmemiş SERP niyetine yazmak (1). Kök neden kuralı bunu zaten söylüyordu: *somutluk kotası dolmazsa üslupla kapatma, müşteriden olgu iste.* Kural yazılıydı; **işin başında değil, redden sonra uygulanıyordu.**

**Bundan çıkan kapı (14 Ağu):** üretim başlamadan önce Metin Yazarı "elimdeki teyitli olgu sayısı" satırını yazar; kota dolmuyorsa metin yazılmaz, **önce soru seti müşteriye gider.**
| 2026-09-14 | Özgür Protez — ürün açıklamalarında marka/model temizliği (115 tarandı, 35 düzeltildi) | 1 tur | Denetmen: çağrılmadı (Kademe 1, Draft site, geri alınabilir) | Ayhan: doğrudan talimat | Red sebebi: yok — red olmadı | ~155k token (okuma ağırlıklı: katalog 7 sayfa tam okuma) |
| 2026-09-14 | Özgür Protez — çakışan adlı 15 ürünün üretici verisiyle ayrıştırılması + Movido ad düzeltmesi | 1 tur | Denetmen: çağrılmadı (Kademe 1, Draft site, geri alınabilir) | Ayhan: doğrudan talimat | Red sebebi: yok — red olmadı | ~75k token (web araştırma + 16 yazma) |
| 2026-11-03 | Özgür Protez — blog iç linkleme (60 yazı canlı: 61 bağlam içi link + 8 onarım + 60×3 ilgili yazı `relatedPostIds`; harita `-blog-ic-linkleme-haritasi-v2-2026-11-03.md`) | v1→v2 + pilot + 3 parti | Denetmen: DÜZELTMEYLE ONAY (25 link sildirdi, 4 yanlış hedefli mevcut link + gövde-blok yerine relatedPostIds önerisi) | Ayhan: ✅ "yalnız iç linkleme" | Red sebebi: v1 otomatik eşleştirme — anlam uyumsuz 13, çift link 8 (SSR düz metinden "zaten linkli" kontrolü yapılamaz → kapı: kontrol richContent LINK süslemesinden) · Uygulamada yan etki: Wix yeniden yayında U+0307'li 3 slug'ı "i-" biçimine normalleştirdi; kamu URL'si zaten bu biçimdeydi, eski adres 200+canonical → kırık yok | ~1,1M token (2 Denetmen turu ~410k dahil) |
| 2026-11-03 | Özgür Protez — şablon artığı 8 URL 301 (/group×2 + /groups → /blog; /portfolio + 3 alt sayfa + /members → /); plan `-sablon-artigi-temizlik-plani-2026-11-03.md` | 1 test + 1 parti | Denetmen: çağrılmadı (geri alınabilir yönlendirme, Ayhan doğrudan talimat; plan büyüme turu denetiminden geçmişti) | Ayhan: ✅ "test et" → "hepsini" | Red sebebi: yok — red olmadı. Açık: Groups/Hotels kaldırma + Portfolio silme + /members noindex Editör'de (Ayhan, Kademe 3); sitemap girişleri o zamana kadar kalır | ~40k token |
| 2026-11-09 | Özgür Protez D Paketi — 16 SEO blog yazısı | 2 (v01→Denetmen→yayın sürümü) | DİKKAT ×7, TEMİZ/DİKKAT ×8, DUR ×1 (çift aşamalı → Test Soketi) | Onay — teyitsiz yayın | — | ölçülmedi |
| 2026-11-11 | Özgür Protez — Güdük bandajlama blog yazısı | 1 | DİKKAT (düzeltildi) | Onay — yayın | — | ölçülmedi |
| 2026-11-11 | Özgür Protez — Aktif vakum protez çeşitleri yazısı | 1 | DİKKAT (düzeltildi) | Onay — yayın | — | ölçülmedi |
| 2026-11-13 | Özgür Protez — site fontu IBM Plex Sans (tüm site) | 1 | Denetmen: çağrılmadı (tasarım ayarı, geri alınabilir) | Onay — "Fontu yayınla" | — | ölçülmedi |
| 2026-11-13 | Özgür Protez — Kişiye Özel Soket Çözümleri statik sayfa | 1 | DİKKAT (düzeltildi) | Onay — "hepsini olduğu gibi yayınla"; görsel alanlarında AFO fotoğrafları duruyor | — | ölçülmedi |
| 2026-11-13 | Özgür Protez — Silikon Linerlar menüsü + 6 statik sayfa | 1 | DİKKAT ×4, TEMİZ ×1, DUR ×1 (Özel Linerlar: hizmet teyitsiz) | Onay — "hepsini olduğu gibi yayınla" (DUR ve diyabet klinisyen okuması açık iken, Ayhan kararı) | — | ölçülmedi |
| 2026-11-13 | Özgür Protez — Kişiye Özel Soket altında 8 statik sayfa | 1 | DİKKAT (düzeltildi) | Onay — "Şimdi yayınla"; görsel alanlarında liner fotoğrafları | — | ölçülmedi |
| 2026-11-14 | SoC — Instagram planı + Higgsfield/grafik adayları (AÇIK, yayın yok) | Plan v1→v5; görsel 6 tur (kirli/lo-fi → loafer → spor çizgisi → UGC → video → geniş açı) | Denetmen: DİKKAT ×2 (18 + 11 bulgu); 2. turda madde 11 taslağı ve YZ "UGC" adayları için DUR | Ayhan: yön onayları ("Evet, bu his", "son iki daha iyi"); madde onayı henüz yok | Red sebebi: (1) "en doğal/gerçekçi"yi kirli-belgesel diye yorumladım, (2) marka sızmasın diye klasik loafer styling, (3) görseli banda sıkıştıran grafik düzen, sayfa no/marka adı. Üçü de yön hatası, piksel değil | Higgsfield 241 kredi (1000→759), ~¾'ü video; ajan tokenı ~2,1M (Growth 227k, İçerik 267k, Astrid 139k+245k+270k, Denetmen 205k+271k, Metin 189k) |

**Bundan çıkan kapılar (14 Kas, red → kapı):** (a) **Yön kartı:** görsel üretimden önce beş satır (çizgi / styling / kadraj / referans markalar / ne DEĞİL) Ayhan'a gider; "evet" gelmeden kredi harcanmaz. (b) **Tur tavanı:** yön onaylanana kadar tur başına en çok 3 kare. (c) **Logo kapısı:** kare, gerçek ürün referansıyla yan yana bakılmadan videoya çevrilmez. (d) **Video yalnız onaylı kareden,** tek tek. (e) Ölçü: kabul edilen aday başına kredi.
