# Nakit Motoru — İŞLENENLER (Kalıcı Dedup Defteri + Koşu Günlüğü)
*Motorun HAFIZASI. Günlük koşu BURAYI önce okur ve içindeki hedefleri aday havuzundan ÇIKARIR. Bu dosya inmezse (yazılmaz/commit edilmezse) motor ertesi gün aynı isimleri tekrar eder — tekrar-bug'ın kök sebebi buydu. Bu yüzden her koşu SONUNDA buraya yazılır + commit + push, **0 iş çıksa bile.***
*Oluşturuldu: 17 Haziran 2026 — tekrar-bug düzeltmesi. Düzeltme öncesi koşular (12–17 Haz) Gmail'e 0 taslak + git'e 0 commit bıraktı; gerçekte hiçbir hedefe temas edilmedi → defter boş-temiz başlıyor (ilk koşu havuzun tepesinden başlar, bu doğru — tekrar 2. koşudan itibaren durur).*

---

## 1 · DEDUP KURALI (motor için — mutlak)
1. Aşağıdaki **DURUM TABLOSU**'nda adı geçen hiçbir hedef yeniden ADAY yapılmaz. O hedef artık tablodaki kendi kadansından (takip/arşiv) yürür — yeni temas akışına geri DÖNMEZ.
2. **COOLDOWN:** `DOĞRULANAMADI` / `KANAL-YOK` durumundakiler **14 gün** yeniden denenmez (son deneme tarihi + 14). Süre dolunca yeniden aday olabilir. Bu, "her sabah aynı tıkanan hedefi tekrar deneme" döngüsünü kırar.
3. **ROTASYON:** Yeni aday seçerken havuzu HER ZAMAN baştan tarama. §3 ROTASYON İŞARETİ'nden devam et, listeyi dönüşümlü tüket.
4. Pazartesi besleme (yeni isim ekleme) yapılırken: eklemeden ÖNCE bu deftere karşı kontrol et — zaten temas edilmiş ismi havuza geri ekleme.

## 2 · DURUM TABLOSU (temas edilen/işlenen her hedef — append + update)
*Durum değerleri: İŞLENDİ (doğrulandı+gözlemlendi, taslak hazır) · GÖNDERİLDİ · TAKİP-1 · TAKİP-2 · YANIT · GÖRÜŞME · ARŞİV(sebep) · DOĞRULANAMADI(cooldown) · KANAL-YOK(cooldown)*

| Hedef | Şerit | İlk işlenme | Son durum | Son temas | Kanal | Varyant | Sonuç / Not |
|---|---|---|---|---|---|---|---|
| LUOKK | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@luokk.co | V1 | Who's Next ihracatçı, büyük beden nişi, stüdyo→editorial boşluk |
| IT'S BASIC | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@itsbasic.com | V2 | 72K IG, 3 dil site (TR/EN/RU), denim/casual |
| BASAKLA | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@basakla.com | V1 | London/Istanbul kimliği, deri+denim nişi, 3.8K IG |
| MERI CREATIVE | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@mericreative.com | V1 | 2015, butik kreatif, 300+ proje, in-house foto/video yok |
| MODA KREATİF | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | hello@modakreatif.com | V2 | ICP zayıf (moda müşterisi yok, isim aldatıcı), genel dijital ajans |
| VDR VIADELLEROSE | C2 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@viadellerose.com | V1 | 147K IG @vdrofficial, Macaristan mağazası (ihracatçı), IFCO 2026 katılımcısı |
| ddip digital/design | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@ddip.co | V1 | İstanbul+Paris, Golden Rose/Pastel güzellik müşterileri, uluslararası brief |
| MARGITTES | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | 14 gün cooldown. Doğrudan site/Instagram bulunamadı. Tekrar: 2026-07-08 |
| FONEM | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | 14 gün cooldown. Doğrudan site/iletişim bulunamadı. Tekrar: 2026-07-08 |
| DOLCEZZA | C1 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | 14 gün cooldown. dczfashion.com 503 hatası, kanal doğrulanamadı. Tekrar: 2026-07-08 |
| BİZE FASHION | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@bizefashion.com | V2 | 39K IG, @bizelondon + Wholesale/Franchising = ihracatçı sinyali; Who's Next katılımcısı |
| VUQU | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@vuqu.com.tr | V1 | Deri çanta, 33K IG @vuquofficial, Bebek/Nişantaşı/Emaar mağazaları |
| CRABS MEDIA | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@crabsmedia.com | V2 | Şişli+Galata, Google Partners, 2014 kuruluş |
| ISTCODE | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@istcode.com | V1 | Ford Otosan/Turk Telekom müşterileri; e-ticaret servisleri var, moda müşterisi yok |
| BossyDigital | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@bossydigital.com | V2 | Sevore/Sassy GO moda+e-ticaret müşterileri ⭐ — en güçlü Şerit B ICP |
| NOX İstanbul | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | hello@noxistanbul.com | V1 | Bağımsız kreatif ajans, Titanic Hotels lüks müşteri |
| MA MULIER | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@mamulier.com | V2 | ⭐⭐ Paris+Londra+Milan gösterileri = en güçlü ihracatçı; Osmanbey showroom; bespoke atölye |
| KÜRE AJANS | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@kureajans.com | V1 | 360° medya; kendi foto/video hizmeti de var — ICP zayıf (in-house çakışma şüphesi) |
| AHTAPOT | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@ahtapotsm.com | V2 | Şişli, 45 kişi — ICP üst sınırı; moda müşterisi bilinmiyor |
| CREATIVE DİJİTAL İSTANBUL | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@creativedijital.istanbul | V1 | İstanbul+Aydın; moda müşterisi yok (Citroën/kafe/diş) — ICP zayıf |
| ZILBERMAN | C1 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@zilbermanwardrobe.com | V1 | Who's Next katılımcısı; @zilbermanwardrobe; linen/cotton/viscose koleksiyonlar |
| UKUŞ | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@ukusajans.com | V2 | "Hayallerden Hikayelere" — marka hikayeciliği odaklı; müşteri portföyü bilinmiyor |
| DijiCrea | B | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | hello@dijicrea.com.tr | V1 | Bakırköy, e-ticaret/web ağırlıklı; moda müşterisi bilinmiyor |
| NAGRADA | C2 | 2026-06-24 | İŞLENDİ (taslak Gmail) | 2026-06-24 | info@nagrada.com.tr | V2 | IFCO katılımcısı, Şişli, B2B iş ortaklıkları, düzenli koleksiyon |
| SOFISA | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | sofisagroup.com SSL süresi dolmuş. Cooldown: 2026-07-08 |
| NILMARK | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | nilmark.com 403 hatası. Cooldown: 2026-07-08 |
| YXL COLLECTION | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | Site/sosyal medya bulunamadı. Cooldown: 2026-07-08 |
| L'ATELIER DE GAIA | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | Türkiye versiyonu net değil; bulunan IG hesapları Türk markası değil. Cooldown: 2026-07-08 |
| MON REVE | C1 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | @monrevebijoux 188K IG; e-posta yok, WhatsApp/form. Gmail taslağı yok. Cooldown: 2026-07-08 |
| MILOU JEWELRY | C1 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | Site var (milou jewelry.com.tr); form only, e-posta yok. Cooldown: 2026-07-08 |
| BIRELIN | C1 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | Cloudflare email protection; form + WhatsApp +905453488151. Gmail taslağı yok. Cooldown: 2026-07-08 |
| CLANDE | C2 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | clande.com.tr; form only, e-posta yok. Modest giyim segmenti. Cooldown: 2026-07-08 |
| LAMANTE | C2 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | lamantemos.com; form + @lamantekahramanmaras; Kahramanmaraş merkezli. Cooldown: 2026-07-08 |
| PUNKQUEEN | C2 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | @punkqueenofficial; WhatsApp only; e-posta yok. Cooldown: 2026-07-08 |
| HİSSET | C2 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | IFCO'dan gelen isim; doğrudan site/sosyal bulunamadı. Cooldown: 2026-07-08 |
| TERZİ DÜKKANI | C2 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | terzidukkani.com; telefon var (0212 602 20 24); e-posta bulunamadı. Cooldown: 2026-07-08 |
| LOKAL ETKİ | B | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | Dijitalajanslar.com listesinden; doğrudan site bulunamadı. Cooldown: 2026-07-08 |
| FRI AGENCY | B | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | Havuz listesinden; doğrudan iletişim bulunamadı. Cooldown: 2026-07-08 |

## 3 · ROTASYON İŞARETİ (hangi listede nereye kadar gelindi)
*Her koşu, işlediği son hedefi buraya yazar; ertesi koşu BURADAN devam eder (baştan değil).*
- **Şerit A** (sıcak çember): işlenen son = — *(Ayhan onayı bekliyor; otomatik temas YOK)*
- **Şerit B** (ajanslar): işlenen son = DijiCrea *(tüm Şerit B havuzu işlendi — sonraki koşu yeni ajanslarla Pazartesi beslemeyle)*
- **Şerit C1** (Who's Next Paris): işlenen son = ZILBERMAN *(tüm doğrulanabilir C1 işlendi — KANAL-YOK/DOĞRULANAMADI cooldown bekliyor; 2026-07-08'den sonra tekrar dene)*
- **Şerit C2** (IFCO): işlenen son = NAGRADA *(tüm araştırılan C2 işlendi; HİLAY/MİANOTTE/EXQUISE/SBL/AHSEN/HALE AKKESE araştırılmadı — sonraki koşu bunlardan başlar)*
- **Pazartesi besleme kaynak sırası** (dönüşümlü): dijitalajanslar.com → İHKİB/fuar duyuruları → Bigumigu/MediaCat yeni iş haberleri → *(başa dön)*. Sıradaki = İHKİB/fuar duyuruları

## 4 · KOŞU GÜNLÜĞÜ (her koşu 1 satır — kalıcılık kanıtı / heartbeat)
*Bir koşu burada satır bırakmadıysa: o koşu persistence adımına VARAMADI (timeout / hata / sandbox / push reddi). Bu durumda çözülecek İLK şey budur — dedup defteri ancak inerse işe yarar.*

| Tarih | Yeni aday | Doğrulanan | Taslak (Gmail) | Yanıt | Takip | Push | Not |
|---|---|---|---|---|---|---|---|
| 2026-06-24 | 8 (5 marka/ajans + 3 DOĞRULANAMADI) | 5 | 5 (LUOKK/IT'SBASIC/BASAKLA/MeriCreative/ModaKreatif) | 0 | 0 | ✅ | İlk başarılı koşu. Dedup+push düzeltmesi çalışıyor. 3 C1 ihracatçı markası + 2 ajans. V1/V2 dönüşümü test ediliyor. |
| 2026-06-24 (ek) | +19 yeni isim havuza eklendi (IFCO tam liste + ddip) | 2 | 2 (VDR/ddip) | 0 | 0 | ✅ | "Yeni alternatifler" genişlemesi: IFCO sayfaları tarandı (78 katılımcıdan 30+), ddip Paris+İstanbul bulundu. Havuzda şimdi 40+ aktif C2 isim. |
| 2026-06-24 (tam genişleme) | +28 yeni hedef araştırıldı (Şerit B+C1+C2 toplu) | 14 | 14 (BİZE/VUQU/CrabsMedia/Istcode/BossyDigital/NOX/MAMULIER/KüreAjans/Ahtapot/CreativeDijital/ZILBERMAN/UKUŞ/DijiCrea/NAGRADA) | 0 | 0 | ✅ | "Hepsine taslak oluştur" komutu — havuzdaki tüm doğrulanabilir hedefler işlendi. 14 yeni taslak Gmail'de. 10+ KANAL-YOK/DOĞRULANAMADI cooldown'a alındı. Toplam oturum taslakları: 21. Önde gelen adaylar: MA MULIER ⭐⭐ (Paris/London/Milan), BossyDigital ⭐ (moda e-ticaret müşterileri), BİZE ⭐ (Wholesale+London). |

---
*Bağlı: `nakit-motoru-hedef-havuzu.md` (aday universe) · `soguk-iletisim-protokolu.md` (kurallar) · Notion Müşteri Panosu (yalnız görüşmeye dönenler terfi eder). Bu defter = "yapıldı" hafızası; havuz = "yapılabilir" listesi.*
