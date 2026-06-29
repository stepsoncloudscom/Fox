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
| LUOKK | C1 | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@luokk.co | V1 | Who's Next ihracatçı, büyük beden nişi, stüdyo→editorial boşluk. Sent search boş ama IT'S BASIC aynı batch'te doğrulandı — muhtemel gönderildi. |
| IT'S BASIC | C1 | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@itsbasic.com | V2 | 72K IG, 3 dil site (TR/EN/RU), denim/casual. Sent ✅ teyitli. |
| BASAKLA | C1 | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@basakla.com | V1 | London/Istanbul kimliği, deri+denim nişi, 3.8K IG. Sent (muhtemel, aynı batch). |
| MERI CREATIVE | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@mericreative.com | V1 | 2015, butik kreatif, 300+ proje, in-house foto/video yok. Sent (muhtemel, aynı batch). |
| MODA KREATİF | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | hello@modakreatif.com | V2 | ICP zayıf (moda müşterisi yok, isim aldatıcı), genel dijital ajans. Sent (muhtemel, aynı batch). |
| VDR VIADELLEROSE | C2 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@viadellerose.com | V1 | 147K IG @vdrofficial, Macaristan mağazası (ihracatçı), IFCO 2026. Sent ✅. TAKİP-1 28 Haz Gmail'de. |
| ddip digital/design | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@ddip.co | V1 | İstanbul+Paris, Golden Rose/Pastel güzellik müşterileri, uluslararası brief. Sent ✅. |
| MARGITTES | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | 14 gün cooldown. Doğrudan site/Instagram bulunamadı. Tekrar: 2026-07-08 |
| FONEM | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | 14 gün cooldown. Doğrudan site/iletişim bulunamadı. Tekrar: 2026-07-08 |
| DOLCEZZA | C1 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | 14 gün cooldown. dczfashion.com 503 hatası, kanal doğrulanamadı. Tekrar: 2026-07-08 |
| BİZE FASHION | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@bizefashion.com | V2 | 39K IG, @bizelondon + Wholesale/Franchising = ihracatçı sinyali; Who's Next. Sent ✅. TAKİP-1 28 Haz Gmail'de. |
| VUQU | C1 | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@vuqu.com.tr | V1 | Deri çanta, 33K IG @vuquofficial, Bebek/Nişantaşı/Emaar. ⚠️ 2x gönderildi (10:27 + 10:44) — TAKİP atla, doğal sessizlik ver. |
| CRABS MEDIA | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-22 | info@crabsmedia.com | V2 | Şişli+Galata, Google Partners, 2014 kuruluş. ⚠️ 2x farklı tarih (22 Haz + 24 Haz) — TAKİP atla. |
| ISTCODE | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@istcode.com | V1 | Ford Otosan/Turk Telekom müşterileri; e-ticaret servisleri var, moda müşterisi yok. ⚠️ 2x gönderildi (10:27 + 10:44) — TAKİP atla. |
| BossyDigital | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@bossydigital.com | V2 | Sevore/Sassy GO moda+e-ticaret müşterileri ⭐. ⚠️ 2x gönderildi (10:27 + 10:44) — TAKİP atla; en güçlü B ICP ama duplicate riski var. |
| NOX İstanbul | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | hello@noxistanbul.com | V1 | Bağımsız kreatif ajans, Titanic Hotels lüks müşteri. Sent ✅. |
| MA MULIER | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@mamulier.com | V2 | ⭐⭐ Paris+Londra+Milan gösterileri = en güçlü ihracatçı; Osmanbey showroom; bespoke atölye. Sent ✅. TAKİP-1 28 Haz Gmail'de (Who's Next Paris sonbahar sezon açısı). |
| KÜRE AJANS | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@kureajans.com | V1 | 360° medya; kendi foto/video hizmeti de var — ICP zayıf (in-house çakışma şüphesi). Sent ✅. |
| AHTAPOT | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | info@ahtapotsm.com | V2 | Şişli, 45 kişi — ICP üst sınırı; moda müşterisi bilinmiyor. Sent ✅. |
| CREATIVE DİJİTAL İSTANBUL | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@creativedijital.istanbul | V1 | İstanbul+Aydın; moda müşterisi yok (Citroën/kafe/diş) — ICP zayıf. ⚠️ 2x gönderildi — TAKİP atla. |
| ZILBERMAN | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@zilbermanwardrobe.com | V1 | Who's Next katılımcısı; @zilbermanwardrobe; linen/cotton/viscose koleksiyonlar. Sent ✅. TAKİP-1 28 Haz Gmail'de (malzeme dili + sezon timing). |
| UKUŞ | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@ukusajans.com | V2 | "Hayallerden Hikayelere" — marka hikayeciliği odaklı; müşteri portföyü bilinmiyor. ⚠️ 2x gönderildi — TAKİP atla. |
| DijiCrea | B | 2026-06-24 | GÖNDERİLDİ | 2026-06-24 | hello@dijicrea.com.tr | V1 | Bakırköy, e-ticaret/web ağırlıklı; moda müşterisi bilinmiyor. Sent ✅. |
| NAGRADA | C2 | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@nagrada.com.tr | V2 | IFCO katılımcısı, Şişli, B2B iş ortaklıkları, düzenli koleksiyon. ⚠️ 2x gönderildi — TAKİP atla. |
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
| EXQUISE | C2 | 2026-06-28 | İŞLENDİ (taslak Gmail) | 2026-06-28 | shop@exquise.com | V1 | IFCO katılımcısı, Şişli/İstanbul, contemporary women's fashion (@exquiseofficial), corset/laces/double cuffs tasarım dili. |
| MİANOTTE | C2 | 2026-06-28 | DOĞRULANAMADI | 2026-06-28 | — | — | mianotte.com bağlantı hatası. IFCO'da Fanas Tekstil / A.Fatih Nasiroğlu. Cooldown: 2026-07-12 |
| AHSEN | C2 | 2026-06-28 | DOĞRULANAMADI | 2026-06-28 | — | — | IFCO AHSEN ile @ahsengiyimofficial (Ankara bazlı, 80K) eşleşmesi teyit edilemedi. Cooldown: 2026-07-12 |
| HALE AKKESE | C2 | 2026-06-28 | DOĞRULANAMADI | 2026-06-28 | — | — | Web'de bulunamadı (tasarımcı adı olarak arama sonuçsuz). Cooldown: 2026-07-12 |
| HİLAY | C2 | 2026-06-28 | ARŞİV(ICP-DÜŞÜK) | 2026-06-28 | — | — | hilay.com.tr modest fashion (ferace/abaya/tesettür). Ayhan'ın editorial tarzıyla segment uyuşmuyor. |
| SBL DESIGN | C2 | 2026-06-28 | ARŞİV(ICP-DÜŞÜK) | 2026-06-28 | — | — | Istanbul Fashion Center wholesale/B2B platform. İçerik ortaklığı hedef profili değil. |

## 3 · ROTASYON İŞARETİ (hangi listede nereye kadar gelindi)
*Her koşu, işlediği son hedefi buraya yazar; ertesi koşu BURADAN devam eder (baştan değil).*
- **Şerit A** (sıcak çember): işlenen son = — *(Ayhan onayı bekliyor; otomatik temas YOK)*
- **Şerit B** (ajanslar): işlenen son = DijiCrea *(tüm havuz işlendi; 28 Haz'da ArtArda Reklam araştırılmadı — Pazartesi besleme kaynağından yeni isimler eklenmeli)*
- **Şerit C1** (Who's Next Paris): işlenen son = ZILBERMAN → TAKİP-1 *(tüm doğrulanabilir C1 işlendi; cooldown bekleyenler 2026-07-08'den sonra; BASARIN LEATHER&FUR kanal bulunamadı — IFCO page'de email yok, SSL süresi dolmuş)*
- **Şerit C2** (IFCO): işlenen son = EXQUISE (28 Haz yeni). Sonraki araştırılacaklar: PINK21 · MICCA · NAQİSHE · BRAND FACTORY · CARMEN · SERABELLA · INCITY · KATAMINO · 3H TEKSTİL · GAZE · APRİDO
- **Pazartesi besleme kaynak sırası** (dönüşümlü): dijitalajanslar.com → İHKİB/fuar duyuruları → Bigumigu/MediaCat yeni iş haberleri → *(başa dön)*. Sıradaki = İHKİB/fuar duyuruları *(28 Haz Pazar; Pazartesi koşusu Şerit B için yeni isim ekler)*

## 4 · KOŞU GÜNLÜĞÜ (her koşu 1 satır — kalıcılık kanıtı / heartbeat)
*Bir koşu burada satır bırakmadıysa: o koşu persistence adımına VARAMADI (timeout / hata / sandbox / push reddi). Bu durumda çözülecek İLK şey budur — dedup defteri ancak inerse işe yarar.*

| Tarih | Yeni aday | Doğrulanan | Taslak (Gmail) | Yanıt | Takip | Push | Not |
|---|---|---|---|---|---|---|---|
| 2026-06-24 | 8 (5 marka/ajans + 3 DOĞRULANAMADI) | 5 | 5 (LUOKK/IT'SBASIC/BASAKLA/MeriCreative/ModaKreatif) | 0 | 0 | ✅ | İlk başarılı koşu. Dedup+push düzeltmesi çalışıyor. 3 C1 ihracatçı markası + 2 ajans. V1/V2 dönüşümü test ediliyor. |
| 2026-06-24 (ek) | +19 yeni isim havuza eklendi (IFCO tam liste + ddip) | 2 | 2 (VDR/ddip) | 0 | 0 | ✅ | "Yeni alternatifler" genişlemesi: IFCO sayfaları tarandı (78 katılımcıdan 30+), ddip Paris+İstanbul bulundu. Havuzda şimdi 40+ aktif C2 isim. |
| 2026-06-24 (tam genişleme) | +28 yeni hedef araştırıldı (Şerit B+C1+C2 toplu) | 14 | 14 (BİZE/VUQU/CrabsMedia/Istcode/BossyDigital/NOX/MAMULIER/KüreAjans/Ahtapot/CreativeDijital/ZILBERMAN/UKUŞ/DijiCrea/NAGRADA) | 0 | 0 | ✅ | "Hepsine taslak oluştur" komutu — havuzdaki tüm doğrulanabilir hedefler işlendi. 14 yeni taslak Gmail'de. 10+ KANAL-YOK/DOĞRULANAMADI cooldown'a alındı. |
| 2026-06-28 | 1 doğrulanan (EXQUISE) + 3 DOĞRULANAMADI (MİANOTTE/AHSEN/HALE AKKESE) + 2 ARŞİV-ICP (HİLAY/SBL) | 1 | 5 (4 TAKİP-1: MA MULIER/VDR/BİZE/ZILBERMAN + 1 yeni: EXQUISE) | 0 (Nakit M.) | 4 | ✅ | ⚠️ RISK-BAYRAK: 6 hedef 2x gönderildi (BossyDigital/VUQU/Ukuş/CreativeDijital/NAGRADA/CrabsMedia) — bu hedeflere TAKİP atlandı. Tüm "İŞLENDİ" statüleri "GÖNDERİLDİ" olarak güncellendi (sent search teyit). Jendue yanıtı (TAG-KLOI kanalı — Nakit Motoru değil) mevcut — Ayhan takibi gerekli. |

---
*Bağlı: `nakit-motoru-hedef-havuzu.md` (aday universe) · `soguk-iletisim-protokolu.md` (kurallar) · Notion Müşteri Panosu (yalnız görüşmeye dönenler terfi eder). Bu defter = "yapıldı" hafızası; havuz = "yapılabilir" listesi.*
