# Denetmen Raporu — Özgür Irmak 3 Amputasyon-Hazırlık/Yara Blog Taslağı Bağımsız Doğrulaması

*Denetmen (orkestratör, Verification mercekleriyle) · 2 Kasım 2026*

**Bağlam:** Üç başlık içerik takviminde (§2 #11-13) 🔴 YÜKSEK-YMYL olarak klinisyen+avukat-partili üretim gerektiriyordu. Ayhan standart akışı bu seferlik (oturumda 8-10. kez) onayladı; telafi olarak "mutlak sınır" disiplini (tanı/tedavi/protokol/süre rakamı yok) ve editör notlarının bağımsız doğrulaması yapıldı. Yöntem: her dosya satır satır okundu; grep ile yasak-kalıp taraması (tanı/tedavi/doz/süre rakamı, ilham-pornosu/acıma kalıpları, satış/garanti dili); kaynak gösterilen 5 yayınlanmış yazı (`ilk-protez`, `amputasyon-rehabilitasyon`, `gudukbakimi-derinlesme`, `diyabet-ayak-sagligi`, HUB `protez-bakimi-v04`) açılıp atıfların birebir doğruluğu kontrol edildi; `slop_tarama.py` ve `sozdizim_tarama.py` **bağımsız olarak yeniden çalıştırıldı** (self-report'a güvenilmedi).

---

## DOSYA 1 — Bacak Ampütasyonu Sonrası: Protez Sürecine Nasıl Hazırlanılır?

1. **Tanı/tedavi/protokol/süre rakamı:** Temiz — grep taraması sıfır sonuç (ameliyat tekniği, komplikasyon, gün/hafta rakamı yok).
2. **Kapsam düzeltmesi (#11):** Doğrulandı. Gövdede ameliyatın kendisi/tekniği/komplikasyon yönetimi hiç açılmıyor; metin açıkça "Ameliyatınızın nasıl geçtiği burada konuşulmuyor... O konu sizi ameliyat eden ekibe ait" diyor ve yalnız protez sürecinin ne zaman başladığına odaklanıyor.
3. **TİTCK M.5:** Temiz — fiyat/kampanya/testimonial/talep yaratma dili yok.
4. **Onur filtresi:** Temiz — ilham-pornosu/acıma/kahraman kalıpları grep'te sıfır sonuç.
5. **Kırık iç link:** Temiz — gövdede tek markdown link, HUB'a (`protez-bacak-ve-kol-bakimi`), önceden teyitli canlı sayfa. "İlk Protez" ve "Rehabilitasyon" düz metinle anıldı, link kurulmadı (talimata uygun — ikisi de taslak, 404/canlı değil).
6. **Uydurma rakam/olgu:** Temiz.
7. **Tarama self-report doğruluğu:** **DİKKAT.** Editör notu "iki UYARI sınırda (karşıtlık yoğunluğu, somut çapa)" diyor. Bağımsız yeniden çalıştırmada **üç** UYARI çıkıyor: karşıtlık (6.7>6.0), somut çapa (4.7<5.5), **aforizma oranı (0.154>0.15 — editör notunda hiç anılmadı)**. SERT yok, blokaj değil — ama self-report tam sayıyı yanlış veriyor.

**Sonuç:** TEMİZ (madde 1-6) — DİKKAT (madde 7, kozmetik: editör notu UYARI sayısını eksik bildiriyor).

---

## DOSYA 2 — Kol Ampütasyonu Sonrası: Protez Sürecine Nasıl Hazırlanılır?

1-6: Dosya 1 ile aynı sonuç — tanı/tedavi/protokol/süre rakamı yok, kapsam düzeltmesi (#12) doğrulandı ("İleri cerrahi teknikler... isim bile geçmedi" — grep doğrulandı, TMR/reinervasyon kelimeleri metinde yok), TİTCK M.5 temiz, onur filtresi temiz, tek link HUB'a, uydurma yok.
7. **Tarama self-report doğruluğu:** **DİKKAT.** Editör notu "birkaç UYARI sınırda (karşıtlık yoğunluğu, somut çapa, noktalı virgül)" diyor — üç isim verilmiş. Bağımsız çalıştırmada **beş** UYARI çıkıyor: karşıtlık (6.3>6.0), somut çapa (4.4<5.5), noktalı virgül (0.9>0.7), **aforizma oranı (0.154>0.15)**, **paragraf uzunluğu değişkenliği (0.429<0.44)** — son ikisi editör notunda hiç anılmadı. SERT yok, blokaj değil.

**Sonuç:** TEMİZ (madde 1-6) — DİKKAT (madde 7, kozmetik: aynı örüntü — editör notu gerçek UYARI sayısının altında rapor veriyor).

---

## DOSYA 3 — Güdükte Yara Varken Protez Kullanılır mı?

1. **Tanı/tedavi/protokol/süre rakamı:** Temiz.
2. **Evet/hayır cevabı verilmemiş mi:** Doğrulandı. Metin açıkça "Doğru cevap 'evet' ya da 'hayır'dan daha fazlasını gerektiriyor" diyor ve hiçbir yerde kesin cevap vermiyor; karar "teknik sorumlu ve gerektiğinde hekiminizle birlikte" çerçevesinde bırakılmış.
3. **Çakışma — "Kalan Uzuv Bölgesi Bakımı: Günlük Kontrolü Derinleştirmek" ile:** Gerçek çakışma yok. Bu yazı kendi "ne zaman beklemeden başvurmalı" listesini veriyor ("yara, açık cilt, kötü koku ya da iltihap belirtisi") — mevcut yazının listesiyle ("geçmeyen kızarıklık, açık yara, su toplaması, kötü koku, iltihap belirtisi ya da kalıcı ağrı") örtüşen ama birebir kopya olmayan, aynı güvenlik sinyaline işaret eden doğal bir paralellik. Mevcut yazıya düz metin atıf var, hyperlink kurulmamış (talimata uygun), içerik tekrarlanmamış — yalnız "orada anlattık, burada tekrar etmiyoruz" diyerek yönlendiriyor.
4. **TİTCK M.5:** Temiz.
5. **Onur filtresi:** Temiz.
6. **Kırık iç link:** Temiz — tek link HUB'a.
7. **Uydurma rakam/olgu:** Temiz. "Diyabet ve Ayak Sağlığı" yazısındaki his-azalması ilkesinin genelleştirilmiş kullanımı doğrulandı — diyabet bağlamı açılmamış, kaynağın kapsamı yanlış temsil edilmemiş.
8. **Tarama self-report doğruluğu:** **DİKKAT — en belirgin olanı.** Editör notu "tek UYARI sınırda (noktalı virgül yoğunluğu...)" diyor. Bağımsız çalıştırmada tarama aracı **"✅ Sözdizimi temiz — insan sesi eşiklerinin içinde"** sonucunu veriyor — **sıfır UYARI.** Self-report var olmayan bir bulguyu raporluyor. Yön risksiz (gerçekte olmayan bir sorunu fazla raporlamak, az raporlamaktan farklı) ama denetim zincirinin "self-report'a güvenme, kaynağa bak" ilkesinin tam karşılığı — bu dosyada self-report'un tarama bölümü dosyanın son haliyle örtüşmüyor.

**Sonuç:** TEMİZ (madde 1-7) — DİKKAT (madde 8, kozmetik: editör notu var olmayan bir UYARI'yı raporluyor).

---

## GENEL SONUÇ

Üç dosyanın hiçbirinde medikal/hukuki eksende (tanı/tedavi/protokol/rakam, TİTCK M.5, onur filtresi, uydurma olgu) SERT veya bloke edici bulgu yok. Kapsam düzeltmeleri (#11/#12) ve çakışma-önleme (#13) talimata birebir uygun uygulanmış. Tek tekrar eden örüntü: **üç dosyanın editör notundaki "Tarama sonucu" cümlesi, bağımsız yeniden çalıştırmada gerçek UYARI sayısını/varlığını tutarlı biçimde eksik veya hatalı bildiriyor** — hiçbiri SERT'e dönüşmüyor ama "denetim zinciri açığı" örüntüsüyle aynı aile: self-report'un kendi ölçüm aracının çıktısını birebir yansıtmaması. Bu üçü tek seferlik kozmetik not olarak Ayhan'a taşınır; tekrar ederse (4. kez) Metin Yazarı'nın tarama-rapor adımına bir kapı eklenmeli (örn. "self-report'a eklenecek UYARI sayısı tool çıkışından otomatik kopyalanır, elle özetlenmez").

## SORULMAMIŞ SORULAR
Yok.

## KARAR ÖNERİSİ
☑ Temiz — onaya gidebilir (3 dosya da, kozmetik DİKKAT notlarıyla birlikte)
