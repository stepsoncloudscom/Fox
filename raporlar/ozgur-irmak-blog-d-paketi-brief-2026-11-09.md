# Özgür Protez — Blog D Paketi Brifi (9 Kas 2026)
*Fox → Metin Yazarı · Ayhan talimatı: "D blog ile alakalı kısımları hallet, soket çözümleri seri olacak, yazıları SEO açısından zenginleştir — 'aktif vakum protez seçenekleri' gibi kelime gruplarını kullan; Google'da protez/ortez aramalarında site öne çıkmalı."*

## Ortak kurallar (hepsi zorunlu)
- **Şablon/precedent:** `raporlar/ozgur-irmak-blog-k-aktivite-seviyesi-v01.md` (yapı, künye satırı, disclaimer birebir, kapanış "Adım adım, birlikte.", YAYIN META, EDİTÖR NOTU) · eski soket yazısı `raporlar/ozgur-irmak-blog-soket-turleri-v01.md`.
- **Zemin:** `sablonlar/ozgur-irmak-marka-context.md` + `sablonlar/ozgur-irmak-branding-kilitli.md` varsa KKK · `marka-bulutu-os-medikal-protez-bagi.md` (TİTCK reklam yasağı dil listesi, YMYL) · `fox-metin-insan-sesi-korpusu.md`.
- **Tıbbi ihtiyat:** tanı/tedavi vaadi yok, rakam (yüzde, süre, fiyat, ağırlık) yok, üstünlük/"en iyi"/garanti yok. Karar "teknik sorumlu ve hekiminizle birlikte". Uydurma teknik detay YOK — emin olunmayan her teknik iddia `[ÖZGÜR BEY TEYİT]` ile işaretlenir.
- **Marka-nötr:** üretici adı (Ottobock, Össur vb.) metne girmez (14 Eyl kararı). Ticari adı olan sistemler jenerik adıyla yazılır; EDİTÖR NOTU'na "marka adı eklenebilir mi — Ayhan/Özgür Bey kararı" yazılır.
- **Fiyat sorgusu:** "fiyat" kelime grubu yüksek hacimli; rakam vermeden "fiyatı neye göre değişir" (bileşen, seviye, aktivite, SGK) H2'si kullanılabilir, SGK yazısına link.
- **SEO zenginleştirme (Ayhan'ın asıl talebi):**
  - H1 + SEO başlık birincil anahtar kelimeyi içerir; slug ASCII-dışı Türkçe karakterli olabilir (sitedeki mevcut stil) ama kısa.
  - Her yazıda 1 birincil + 4-8 ikincil/uzun kuyruk kelime grubu, doğal geçişle H2'lere dağıtılır ("aktif vakum protez seçenekleri", "diz altı protez çeşitleri" gibi). Anahtar kelime doldurma yok — okunurluk önce.
  - SSS bölümü: Google "insanlar bunu da soruyor" tarzı 3-5 soru (FAQ şeması için).
  - **İç link:** 3-5 bağlam içi link, yalnız aşağıdaki canlı URL listesinden (birebir), + seri içi linkler (henüz yayında değil → düz metin, "[SERİ-LİNK: başlık]" etiketiyle).
  - Meta açıklama ≤155, SEO başlık ≤60.
  - Uzunluk: 600-1000 kelime (eski yazılardan uzun — SEO için derinlik; dolgu yok).
- **Tarama:** `python3 sablonlar/araclar/slop_tarama.py` + `sozdizim_tarama.py` her yazıda, sonuç EDİTÖR NOTU'na.
- **Çıktı:** her yazı ayrı dosya `raporlar/ozgur-irmak-blog-<slug-ascii>-v01.md`.

## Google TR öneri verisi (ham: `raporlar/ozgur-irmak-d-paketi-google-oneri-ham-2026-11-09.txt`)
Güçlü sinyaller: diz üstü protez çeşitleri · diz altı protez çeşitleri · protez soket çeşitleri · **diz üstü protez soket çeşitleri** · protez bacak soketi · protez soket yapımı · soft soket protez · kilitli soket · hidrolik diz üstü protez · hidrolik diz eklemi · pnömatik diz eklemi · rgo ortezi nedir · silikon liner diz altı protez · silikon liner pin sistemli protez · silikon liner kilit sistemli modüler diz altı protezi · protez silikon liner · aktif vakum diz altı protezi · karbon fiber protez bacak · uzun yürüme cihazı · protez bacak fiyatları (rakamsız ele al).
Sıfır öneri (niş): rotasyon adaptörü, 3D cover, kaydırma adaptörü, laminasyon/çift aşamalı/ayarlanabilir soket → bu yazılar geniş kümeye bağlanır ("diz üstü protez parçaları", "protez bacak parçaları", "protez soket çeşitleri").

## Yazı listesi
**Grup 1 — Dizüstü aparatları + liner**
1. Rotasyon adaptörü (protez bacakta rotasyon adaptörü nedir; bağdaş kurma/araba/ayakkabı giyme gibi günlük kullanım)
2. 3D cover (protez bacak kaplaması / kozmetik kılıf — mevcut "Protez Ayak Kılıfı" yazısıyla çakışmasın: o ayak, bu bacak/diz-baldır hacmi)
3. Kaydırma adaptörü (hizalama/ofset ayarı)
4. Silikon liner çeşitleri ve kullanım tercihleri (pin/kilitli, vakum/emme, yastık liner; diz altı/diz üstü) — mevcut "Silikon Liner Nedir?" ile çakışmasın: o tanım, bu seçim/karşılaştırma

**Grup 2 — Dizler + RGO**
5. Hidrolik diz (hidrolik diz üstü protez / hidrolik diz eklemi) — "Mikroişlemcili vs Mekanik Diz" yazısından ayrış: bu yalnız hidrolik kontrol mantığı
6. Pnömatik diz eklemi — hidrolik ile farkı tek paragraf, gerisi pnömatik
7. RGO ortezi nedir (reciprocating gait orthosis — kimin için değerlendirilir, nasıl kullanılır; yürüme cihazı kümesi)

**Grup 3 — Kişiye Özel Soket Çözümleri serisi (hub + 8)**
0. HUB: Kişiye Özel Protez Soket Çözümleri — "protez soket çeşitleri / diz üstü protez soket çeşitleri / protez bacak soketi / soket yapımı" birincil; 8 yazıya kısa giriş + link; mevcut "Protez Soket Türleri: Vakum mu, Pin-Kilit mi?" (bağlantı sistemi odaklı) ile ayrış: hub = soketin yapımı/malzemesi/tasarımı
1. 3D soket (3D tarama/baskı ile soket)
2. Hibrit TF kilit sistemi (transfemoral, hibrit kilitleme)
3. Direct socket (doğrudan uzuv üzerinde üretilen soket)
4. Lanyard / ip-kayış bağlantılı soket sistemi (Ayhan'ın notunda "Ottobock KISS" — marka-nötr yaz, bayrak koy)
5. Laminasyon soket
6. Karbon soket
7. Çift aşamalı soket (test soketi → kalıcı soket)
8. Ayarlanabilir soket

## Canlı blog URL'leri (iç link için birebir)
Bkz. `raporlar/ozgur-irmak-canli-blog-url-listesi-2026-11-09.txt`
