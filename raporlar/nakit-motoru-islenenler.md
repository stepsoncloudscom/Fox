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

## 3 · ROTASYON İŞARETİ (hangi listede nereye kadar gelindi)
*Her koşu, işlediği son hedefi buraya yazar; ertesi koşu BURADAN devam eder (baştan değil).*
- **Şerit A** (sıcak çember): işlenen son = — *(Ayhan onayı bekliyor; otomatik temas YOK)*
- **Şerit B** (ajanslar): işlenen son = MODA KREATİF *(Moda Kreatif, Meri Creative → sonraki koşu Crabs Media'dan devam)*
- **Şerit C1** (Who's Next Paris): işlenen son = BASAKLA *(BASAKLA, BIRELIN, BİZE... → sonraki koşu BIRELIN'dan devam)*
- **Şerit C2** (IFCO): işlenen son = — *(baştan)*
- **Pazartesi besleme kaynak sırası** (dönüşümlü): dijitalajanslar.com → İHKİB/fuar duyuruları → Bigumigu/MediaCat yeni iş haberleri → *(başa dön)*. Sıradaki = dijitalajanslar.com

## 4 · KOŞU GÜNLÜĞÜ (her koşu 1 satır — kalıcılık kanıtı / heartbeat)
*Bir koşu burada satır bırakmadıysa: o koşu persistence adımına VARAMADI (timeout / hata / sandbox / push reddi). Bu durumda çözülecek İLK şey budur — dedup defteri ancak inerse işe yarar.*

| Tarih | Yeni aday | Doğrulanan | Taslak (Gmail) | Yanıt | Takip | Push | Not |
|---|---|---|---|---|---|---|---|
| 2026-06-24 | 8 (5 marka/ajans + 3 DOĞRULANAMADI) | 5 | 5 (LUOKK/IT'SBASIC/BASAKLA/MeriCreative/ModaKreatif) | 0 | 0 | ✅ | İlk başarılı koşu. Dedup+push düzeltmesi çalışıyor. 3 C1 ihracatçı markası + 2 ajans. V1/V2 dönüşümü test ediliyor. |
| 2026-06-24 (ek) | +19 yeni isim havuza eklendi (IFCO tam liste + ddip) | 2 | 2 (VDR/ddip) | 0 | 0 | ✅ | "Yeni alternatifler" genişlemesi: IFCO sayfaları tarandı (78 katılımcıdan 30+), ddip Paris+İstanbul bulundu. Havuzda şimdi 40+ aktif C2 isim. |

---
*Bağlı: `nakit-motoru-hedef-havuzu.md` (aday universe) · `soguk-iletisim-protokolu.md` (kurallar) · Notion Müşteri Panosu (yalnız görüşmeye dönenler terfi eder). Bu defter = "yapıldı" hafızası; havuz = "yapılabilir" listesi.*
