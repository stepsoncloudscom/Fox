# Denetmen Raporu — Özgür Irmak 5 Yüksek-YMYL Blog Taslağı Bağımsız Doğrulaması

*Denetmen (orkestratör, Verification mercekleriyle) · 28 Ekim 2026*

**Bağlam:** Beş başlık normalde klinisyen-partili üretim gerektiriyordu (içerik takviminde 🔴/🔴🔴 YÜKSEK-YMYL). Ayhan bu şartı bu seferlik atlamayı onayladı; telafi olarak metin yazarının kendi editör notunda işaretlediği "mutlak sınır" disiplinine (tanı/tedavi/evre/rakam yok) bağımsız doğrulama yapıldı.

**Yöntem:** Her dosya satır satır okundu; 6 kontrol maddesi için metin gövdesi (YAYIN META/EDİTÖR NOTU dışı) tarandı; `grep` ile yasak-kalıp taraması; HUB kaynak dosyasıyla birebir karşılaştırma; `slop_tarama.py` ve `sozdizim_tarama.py` **bağımsız olarak yeniden çalıştırıldı** (self-report'a güvenilmedi — Verification ilkesi: "Fox'un vardığı sonuca değil, kaynağa bak").

---

## DOSYA 1 — Kalan Uzuv (Güdük) Bakımı: Derinleşme

1. **Tanı/tedavi/evre/rakam:** Temiz. Evre, enfeksiyon sınıflandırması, ürün ismi, süre rakamı yok.
2. **TİTCK M.5/15.2:** Temiz. Satış/reklam dili yok; bilgilendirme çerçevesinde (M.15/2 istisnası — kendi sitesinde cihaz/bakım bilgilendirmesi).
3. **HUB birebir alıntı:** N/A (bu dosyada HUB'dan birebir alıntı yok, çapraz atıf var — doğru, iddia edildiği gibi).
4. **Onur filtresi:** N/A (bu dosya onur-kritik kategori değil) — temiz.
5. **Kırık iç link:** Temiz. Tek markdown link → `/protez-bacak-ve-kol-bakimi` (HUB, canlı). "Protez Süreci" hiç anılmamış — doğru.
6. **Uydurma rakam/olgu:** Temiz.

**Sonuç:** TEMİZ (madde 1-6).

---

## DOSYA 2 — Fantom (Hayalet Uzuv) Hissi: Nedir?

1-6: Temiz. Nörolojik mekanizma, tedavi yöntemi, prevalans rakamı, aciliyet derecelendirmesi — hiçbiri yok; metin kasıtlı olarak dar. HUB alıntısı yok (iddia edilmiyor da). İç link yalnız HUB'a — ama **markdown link olarak HUB'a da atıf yok**, sadece dosyanın YAYIN META'sında "İç link: HUB — tek link" deniyor, gövdede hiçbir `[...](...)` yok (grep doğrulandı — 0 sonuç). Küçük tutarsızlık: meta "tek link" diyor ama gövdede fiilen hiç link yok. Risk değil (daha az bağlantı, daha fazla değil) ama meta kendi iddiasını doğrulamıyor.

**Sonuç:** TEMİZ (madde 1-6) — DİKKAT (meta/gövde tutarsızlığı, kozmetik, yayın öncesi düzeltilsin: ya HUB'a gerçek bir link eklensin ya da meta "iç link yok" olarak güncellensin).

---

## DOSYA 3 — Ampütasyon Sonrası Rehabilitasyon Süreci

1-4, 6: Temiz.
5. **Kırık iç link:** Gövdede **hiçbir markdown link yok** (grep doğrulandı). YAYIN META şöyle diyor: *"İç link: HUB (protez-bacak-ve-kol-bakimi) — tek link, canlı olduğu teyitli."* — **bu iddia yanlış.** Gövdede HUB'a (ya da başka hiçbir sayfaya) hiçbir hyperlink yok; yalnızca isimsiz düz-metin atıf var ("Protez sürecinin adımlarını önceki bir yazımızda anlatmıştık"). "Protez Süreci" ve "İlk Protez" de düz metinle (isim verilmeden) anıldı — bu doğru ve istenen (404/taslak sayfaya link verilmemiş). Ama meta'nın "HUB'a tek link var" cümlesi fiiliyatla örtüşmüyor.

**Sonuç:** TEMİZ (gerçek broken-link riski yok — çünkü hiç link yok) — **DİKKAT: YAYIN META kendi iddiasıyla çelişiyor, düzeltilmeli** (meta satırı "iç link yok, düz metin atıf var" olarak yazılmalı; bu küçük ama denetim güvenilirliğini zayıflatan bir hata — editör notlarının doğruluğuna körü körüne güvenilmemeli).

---

## DOSYA 4 — Protez ve Psikolojik Uyum

1, 2, 3 (N/A), 5, 6: Temiz.
4. **Onur filtresi (satır satır):** Bağımsız tarandı — "ilham verici/kahraman/engeline rağmen/acıma/zor-kolay vaka/normal hayata dönüş" kalıplarının hiçbiri metinde yok (grep doğrulandı). "Güçlü olmalısın" cümlesi kasıtlı olarak eleştirel bağlamda kullanılmış — doğru okunmuş. Klinik evre modeli (inkâr/kabul vb.) kurulmamış — doğru.

**Sonuç:** TEMİZ (madde 1-6).

---

## DOSYA 5 — Diyabet ve Ayak Sağlığı: Protez Kullananda Dikkat Edilecekler

1. **Tanı/tedavi/evre/rakam:** Temiz — tip ayrımı, kan şekeri değeri, ilaç, Wagner skalası yok.
2. **TİTCK:** Temiz.
3. **HUB birebir alıntı — BAĞIMSIZ DOĞRULANDI:** `ozgur-irmak-blog-protez-bakimi-v04.md` satır 76-77'deki FAQ cevabı ile bu dosyadaki alıntı **karakter karakter karşılaştırıldı — birebir aynı, tek kelime farkı yok.** İddia doğru.
4. N/A.
5. **Kırık link:** Temiz. Tek markdown link → `/protez-bacak-ve-kol-bakimi` (gerçek, HUB'ın kendi slug'ıyla eşleşiyor).
6. **Uydurma rakam/olgu:** Temiz.

**Sonuç:** TEMİZ (madde 1-6) — bu dosya beş yazının en sıkı kaynak disiplinine sahip olanı, iddialar tam doğrulandı.

---

## BAĞIMSIZ BULGU — sozdizim_tarama.py self-report tutarsızlığı (5 dosyanın hepsi)

Her dosyanın EDİTÖR NOTU'nda şu iddia var: *"sozdizim_tarama.py → ⚠️ UYARI (SERT yok)"*. Bu iddia Fox'un kendi beyanı; Verification ilkesi gereği bağımsız tekrar çalıştırıldı (araç gövde-dışı satırları — başlık/alıntı/liste/tablo — otomatik atlıyor, dolayısıyla hem tam dosya hem salt gövde üzerinde test edildi).

**Sonuç: 5 dosyanın 5'i de gövde metninde en az bir SERT (sert eşik aşımı) üretti** — self-report'un iddia ettiği "SERT yok" durumuyla ÖRTÜŞMÜYOR:

| Dosya | SERT bulgular (gövde-only, bağımsız çalıştırma) |
|---|---|
| Güdük Bakımı | Somut çapa yoğunluğu: 1.0 < 3.0 |
| Fantom His | Cümle uzunluğu değişkenliği: 0.397<0.42 · Somut çapa: 0.0<3.0 |
| Rehabilitasyon | Somut çapa: 0.0<3.0 |
| Psikolojik Uyum | Somut çapa: 0.0<3.0 · Paragraf uzunluğu değişkenliği: 0.25<0.3 |
| Diyabet | Cümle uzunluğu değişkenliği: 0.312<0.42 · Somut çapa: 1.2<3.0 |

CLAUDE.md'nin kendi yazılı kuralı: **"SERT bulgu = otomatik geri gönderme."** Bu kural mekanik uygulanırsa, 5 dosyanın 5'i de şu anki haliyle geri gönderilmesi gerekir — self-report'un "temiz/UYARI" sonucuna güvenilerek onaya gönderilemez.

**Ama — Sokratik ön-süzgeç uygulanmalı (İnsan Sesi merceği, "bu metnin somut malzemesi var mıydı?"):** Düşük "somut çapa" skorunun kök nedeni bu beş dosyada **kasıtlı bilgi eksikliği değil, kasıtlı bilgi YOKLUĞU'dur** — editör notları bunu açıkça belgeliyor (rakam/isim/evre bilerek yazılmadı, çünkü klinisyen filtresi yok). Normal durumda "somut çapa düşük = brif açığı, müşteriden olgu iste" kuralı işler; burada tersi geçerli — **somut çapa'yı yükseltecek malzeme (rakam/isim/evre) güvenlik gereği kasıtlı olarak eklenmiyor.** Yani SERT bulgusu gerçek bir "kötü yazılmış" veya "eksik brif" sinyali değil, **aracın eşiğinin bu tür bilerek-az-bilgili YMYL metniyle kalibre edilmemiş olmasının** sinyali.

**Bu, aracı görmezden gelme gerekçesi değildir — bir kalibrasyon/istisna kararı gerektirir.** İki seçenek Ayhan'a/Denetmen'e kalır: ① bu 5 dosya için "YMYL-kısıtlı metin" istisna profili tanımlanır (somut çapa eşiği bu profilde düşürülür, gerekçe kayda geçer) ② ya da mevcut haliyle SERT kuralı mekanik uygulanır ve 5 dosya da "düzelt" kararıyla geri döner. **Fox'un kendi self-report'u ("SERT yok") her durumda yanlıştı ve bu rakamlara güvenilerek yayına onay VERİLEMEZ** — bu denetimin asıl bulgusu budur.

**slop_tarama.py self-report doğrulandı:** 5/5 dosyada bağımsız çalıştırma "✅ Temiz" sonucunu teyit etti — bu araçta tutarsızlık yok.

---

## ÇELİŞKİ

Yok (alt rol çağrılmadı — bu denetim doğrudan Verification merceğiyle yapıldı, routing tablosu kuralına göre rakam/kaynak doğrulaması gerektiren çıktı).

## SORULMAMIŞ SORULAR

1. **sozdizim_tarama.py'nin "somut çapa" eşiği YMYL-kısıtlı/bilgi-az içerik için hiç kalibre edildi mi?** Mevcut eşikler (3.0 sert / muhtemelen ~5.5 uyarı) muhtemelen normal pazarlama/anlatı metninden kalibre edilmiş; bu beş dosyanın temsil ettiği "bilerek az bilgili klinik metin" kategorisi farklı bir kalibrasyon gerektirebilir. Bu soru Fox'a/Ayhan'a sorulmadı.
2. Metin Yazarı'nın editör notlarındaki "Tarama sonucu" rakamları hangi dosya sürümünde/hangi kapsamda (tam dosya mı, gövde mi) çalıştırıldı? Rakamlar şu anki dosya içeriğiyle eşleşmiyor — bu bir süreç sorusu (hangi adımda neyin tarandığı kayıt altına alınmalı).
3. HUB (`protez-bacak-ve-kol-bakimi`) şu an gerçekten canlıda mı (HTTP 200)? Beş dosyanın hepsi bunu "teyitli" diye iddia ediyor ama bu denetim kapsamında tarayıcıyla bağımsız doğrulanmadı — önceki oturumlarda teyit edilmiş olabilir, ama bu denetim o teyidi tekrar üretmedi.

## KARAR ÖNERİSİ

☑ **Düzelt** — tıbbi/hukuki eksen (madde 1-6) **TEMİZ**, bu eksende yayına engel yok. Ama iki ayrı düzeltme şart, biri kozmetik biri yöntemsel:
- **Kozmetik (Dosya 2 ve 3):** YAYIN META'daki "İç link: HUB — tek link" iddiası gövdeyle uyuşmuyor; meta satırları düzeltilsin.
- **Yöntemsel (5 dosyanın hepsi):** sozdizim_tarama.py SERT bulguları Fox/Ayhan'a taşınmadan yayına geçilmemeli. Ayhan ya eşik-istisnası kararı verir (gerekçeli, kayda geçer) ya da Metin Yazarı'ndan somut çapayı güvenlik ihlali etmeden yükseltecek bir revizyon ister (ör. süreç adımlarını daha isim/sayı-temelli anlatmak — "teknik sorumlu" yerine "merkezinizdeki teknik sorumlu [X adım]" gibi somutlaştırma, tıbbi ayrıntı eklemeden).

□ Temiz — onaya gidebilir *(tıbbi/hukuki eksende evet, ama sozdizim bulgusu çözülmeden tam "temiz" denemez)*
□ Ayhan'a eskalasyon
