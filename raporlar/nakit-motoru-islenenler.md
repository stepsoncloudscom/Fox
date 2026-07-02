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
| LUOKK | C1 | 2026-06-24 | ARŞİV(G+10-GEÇMİŞ) | 2026-06-30 | info@luokk.co | V1 | ⚠️ PRE-MOTOR: Jun 15+16 gönderilmiş (2 farklı Gmail thread). G+10 = Jun 25 geçti. Jun 24 batch teyitsiz. ARŞİV. |
| IT'S BASIC | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-30 | info@itsbasic.com | V2 | 72K IG, 3 dil site (TR/EN/RU), denim/casual. Sent ✅ Jun 24. TAKİP-1 30 Haz Gmail'de (draft r-960553949907177161). Açı: 3 dil = ihracat sinyal = editorial değer. |
| BASAKLA | C1 | 2026-06-24 | ARŞİV(G+10-GEÇMİŞ) | 2026-06-30 | info@basakla.com | V1 | ⚠️ PRE-MOTOR: Jun 16 gönderilmiş (Gmail thread 19ed0b65d41983c3). G+10 = Jun 26 geçti. Jun 24 batch teyitsiz. ARŞİV. |
| MERI CREATIVE | B | 2026-06-24 | ARŞİV(G+10-GEÇMİŞ) | 2026-06-30 | info@mericreative.com | V1 | ⚠️ PRE-MOTOR: Jun 15 gönderilmiş (Gmail thread 19ecaae0b7bfcca3). G+10 = Jun 25 geçti. ARŞİV. |
| MODA KREATİF | B | 2026-06-24 | ARŞİV(G+10-GEÇMİŞ) | 2026-06-30 | hello@modakreatif.com | V2 | ⚠️ PRE-MOTOR: Jun 15 gönderilmiş (Gmail thread 19ecaade815f1c10). G+10 = Jun 25 geçti. ICP zayıf zaten (genel dijital ajans). ARŞİV. |
| VDR VIADELLEROSE | C2 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@viadellerose.com | V1 | 147K IG @vdrofficial, Macaristan mağazası (ihracatçı), IFCO 2026. Sent ✅. TAKİP-1 28 Haz Gmail'de. TAKİP-2 → 4 Temmuz (G+10 original). |
| ddip digital/design | B | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-30 | info@ddip.co | V1 | İstanbul+Paris, Golden Rose/Pastel güzellik müşterileri, uluslararası brief. Sent ✅ Jun 24. TAKİP-1 30 Haz (draft r-8704693325835550294). Açı: güzellik→moda kapasite köprüsü. |
| MARGITTES | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | 14 gün cooldown. Doğrudan site/Instagram bulunamadı. Tekrar: 2026-07-08 |
| FONEM | C1 | 2026-06-24 | DOĞRULANAMADI | 2026-06-24 | — | — | 14 gün cooldown. Doğrudan site/iletişim bulunamadı. Tekrar: 2026-07-08 |
| DOLCEZZA | C1 | 2026-06-24 | KANAL-YOK | 2026-06-24 | — | — | 14 gün cooldown. dczfashion.com 503 hatası, kanal doğrulanamadı. Tekrar: 2026-07-08 |
| BİZE FASHION | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@bizefashion.com | V2 | 39K IG, @bizelondon + Wholesale/Franchising = ihracatçı sinyali; Who's Next. Sent ✅. TAKİP-1 28 Haz Gmail'de. TAKİP-2 → 4 Temmuz (G+10 original). |
| VUQU | C1 | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@vuqu.com.tr | V1 | Deri çanta, 33K IG @vuquofficial, Bebek/Nişantaşı/Emaar. ⚠️ 2x gönderildi (10:27 + 10:44) — TAKİP atla, doğal sessizlik ver. |
| CRABS MEDIA | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-22 | info@crabsmedia.com | V2 | Şişli+Galata, Google Partners, 2014 kuruluş. ⚠️ 2x farklı tarih (22 Haz + 24 Haz) — TAKİP atla. |
| ISTCODE | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@istcode.com | V1 | Ford Otosan/Turk Telekom müşterileri; e-ticaret servisleri var, moda müşterisi yok. ⚠️ 2x gönderildi — TAKİP atla. |
| BossyDigital | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@bossydigital.com | V2 | Sevore/Sassy GO moda+e-ticaret müşterileri ⭐. ⚠️ 2x gönderildi — TAKİP atla; en güçlü B ICP ama duplicate riski var. |
| NOX İstanbul | B | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-30 | hello@noxistanbul.com | V1 | Bağımsız kreatif ajans, Titanic Hotels lüks müşteri. Sent ✅ Jun 24. TAKİP-1 30 Haz (draft r-8782048249986161373). Açı: premium mekân→moda köprüsü. |
| MA MULIER | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@mamulier.com | V2 | ⭐⭐ Paris+Londra+Milan gösterileri = en güçlü ihracatçı; Osmanbey showroom; bespoke atölye. Sent ✅. TAKİP-1 28 Haz Gmail'de. TAKİP-2 → 4 Temmuz (G+10 original). |
| KÜRE AJANS | B | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-30 | info@kureajans.com | V1 | 360° medya; kendi foto/video hizmeti de var — ICP zayıf (in-house çakışma şüphesi). Sent ✅ Jun 24. TAKİP-1 30 Haz (draft r-1579688571243028882). |
| AHTAPOT | B | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-30 | info@ahtapotsm.com | V2 | Şişli, 45 kişi — ICP üst sınırı; moda müşterisi bilinmiyor. Sent ✅ Jun 24. TAKİP-1 30 Haz (draft r1467664869965261657). |
| CREATIVE DİJİTAL İSTANBUL | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@creativedijital.istanbul | V1 | İstanbul+Aydın; moda müşterisi yok (Citroën/kafe/diş) — ICP zayıf. ⚠️ 2x gönderildi — TAKİP atla. |
| ZILBERMAN | C1 | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-28 | info@zilbermanwardrobe.com | V1 | Who's Next katılımcısı; @zilbermanwardrobe; linen/cotton/viscose koleksiyonlar. Sent ✅. TAKİP-1 28 Haz Gmail'de. TAKİP-2 → 4 Temmuz (G+10 original). |
| UKUŞ | B | 2026-06-24 | GÖNDERİLDİ ⚠️DUPLICATE | 2026-06-24 | info@ukusajans.com | V2 | "Hayallerden Hikayelere" — marka hikayeciliği odaklı; müşteri portföyü bilinmiyor. ⚠️ 2x gönderildi — TAKİP atla. |
| DijiCrea | B | 2026-06-24 | TAKİP-1 (taslak Gmail) | 2026-06-30 | hello@dijicrea.com.tr | V1 | Bakırköy, e-ticaret/web ağırlıklı; moda müşterisi bilinmiyor. Sent ✅ Jun 24. TAKİP-1 30 Haz (draft r7080969300895992354). |
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
| EXQUISE | C2 | 2026-06-28 | İŞLENDİ (taslak Gmail) | 2026-06-28 | shop@exquise.com | V1 | IFCO katılımcısı, Şişli/İstanbul, contemporary women's fashion (@exquiseofficial), corset/laces/double cuffs tasarım dili. ⚠️ Ayhan gönderim teyidi bekleniyor — gönderildiyse durumu GÖNDERİLDİ yap. |
| MİANOTTE | C2 | 2026-06-28 | DOĞRULANAMADI | 2026-06-28 | — | — | mianotte.com bağlantı hatası. IFCO'da Fanas Tekstil / A.Fatih Nasiroğlu. Cooldown: 2026-07-12 |
| AHSEN | C2 | 2026-06-28 | DOĞRULANAMADI | 2026-06-28 | — | — | IFCO AHSEN ile @ahsengiyimofficial (Ankara bazlı, 80K) eşleşmesi teyit edilemedi. Cooldown: 2026-07-12 |
| HALE AKKESE | C2 | 2026-06-28 | DOĞRULANAMADI | 2026-06-28 | — | — | Web'de bulunamadı (tasarımcı adı olarak arama sonuçsuz). Cooldown: 2026-07-12 |
| HİLAY | C2 | 2026-06-28 | ARŞİV(ICP-DÜŞÜK) | 2026-06-28 | — | — | hilay.com.tr modest fashion (ferace/abaya/tesettür). Ayhan'ın editorial tarzıyla segment uyuşmuyor. |
| SBL DESIGN | C2 | 2026-06-28 | ARŞİV(ICP-DÜŞÜK) | 2026-06-28 | — | — | Istanbul Fashion Center wholesale/B2B platform. İçerik ortaklığı hedef profili değil. |
| BASARIN LEATHER & FUR | C1 | 2026-06-29 | İŞLENDİ (taslak Gmail) | 2026-06-29 | info@basarin.com | V2 | 1984 kuruluş, Merter/İstanbul. Première Vision Paris katılımı = ihracatçı ⭐. basarin.com SSL süresi dolmuş = dijital içerik boşluğu kanıtı. Gmail taslağı ID r-17585630848522458. ⚠️ Ayhan gönderim teyidi bekleniyor. |
| PINK21 | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | Toptan (wholesale) marka — "The Most Ultra Cool Wholesale Brand". B2B/B2B2C model, içerik ortaklığı hedef profili değil. |
| MICCA | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | Tesettür/modest fashion (abaya, tunik). HİLAY ile aynı segment — Ayhan editorial tarzıyla uyuşmuyor. |
| BRAND FACTORY (C2) | C2 | 2026-06-29 | ARŞİV(ICP-YANLIŞ) | 2026-06-29 | — | — | DeFacto/LCW/US Polo için üretim yapan konfeksiyon fabrikası — marka değil, imalatçı. ICP tamamen yanlış. |
| CARMEN | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | 40 yıllık abiye markası, Nişantaşı mağazası, in-house prodüksiyon güçlü. Büyük/köklü = dış içerik ihtiyacı düşük. |
| SERABELLA | C2 | 2026-06-29 | DOĞRULANAMADI | 2026-06-29 | — | — | safamoda.com.tr SSL süresi dolmuş. Safa Moda (1955 kuruluş) büyük/köklü abiye ihracatçısı. Cooldown: 2026-07-13 |
| NAQİSHE (Nakish) | C2 | 2026-06-29 | KANAL-YOK | 2026-06-29 | — | — | nakishonline.com Nişantaşı atölye, couture, 36-80K TL. Instagram @nakishofficial. E-posta yok — form+IG DM only. Cooldown: 2026-07-13 |
| GAZE | C2 | 2026-06-29 | DOĞRULANAMADI | 2026-06-29 | — | — | IFCO katılımcısı; web'de doğrudan site/iletişim bulunamadı. Cooldown: 2026-07-13 |
| APRİDO | C2 | 2026-06-29 | DOĞRULANAMADI | 2026-06-29 | — | — | IFCO katılımcısı; web'de doğrudan site/iletişim bulunamadı. Cooldown: 2026-07-13 |
| 3H TEKSTİL | C2 | 2026-06-29 | ARŞİV(ICP-YANLIŞ) | 2026-06-29 | — | — | Güngören/Merter tekstil imalatçısı — konfeksiyon fabrikası, marka değil. |
| SERPİL EXCLUSIVE | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | 1988'den beri, Emaar mağazası, franchise modeli, %30 indirim kampanyaları = mid-market/mass occasion wear. Form only, e-posta yok. |
| VOLUMEX | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | İç giyim + çorap (Antebî Örme) — Ayhan editorial segmentiyle uyuşmuyor. |
| PUANE | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | Bağcılar/Merter, modern modest fashion (tesettür). Aynı segment. |
| ATINÇ İPEK | C2 | 2026-06-29 | DOĞRULANAMADI | 2026-06-29 | — | — | IFCO sayfa 2 katılımcısı; doğrudan site/iletişim bulunamadı. Cooldown: 2026-07-13 |
| MISS İNDİGO | C2 | 2026-06-29 | DOĞRULANAMADI | 2026-06-29 | — | — | IFCO katılımcısı; web'de bulunamadı. Cooldown: 2026-07-13 |
| ESCAREL | C2 | 2026-06-29 | KANAL-YOK | 2026-06-29 | — | — | Facebook @escarelofficial bulundu ama web/email yok. Cooldown: 2026-07-13 |
| MAYRA (IFCO) | C2 | 2026-06-29 | DOĞRULANAMADI | 2026-06-29 | — | — | IFCO sayfa 2; Mayra marka isimleri Hindistan/global — Türkiye bazlı IFCO markasıyla eşleşme teyit edilemedi. Cooldown: 2026-07-13 |
| MINT NEW FASHION | C2 | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | Toptan/wholesale odaklı, Hepsiburada/ihracat. Doğrudan içerik ortaklığı hedef profili değil. |
| ArtArda Reklam | B | 2026-06-29 | ARŞİV(ICP-DÜŞÜK) | 2026-06-29 | — | — | Ankara merkezli (HQ Şedat Simavi Sk, Ankara), genel dijital ajans (web+SEO+sosyal). Moda müşterisi sinyali yok. ICP düşük. |
| NUR KALAY COLLECTION | C2 | 2026-06-30 | İŞLENDİ (taslak Gmail) | 2026-06-30 | info@nurkalay.com.tr | V1 | IFCO Ağu 2026 katılımcısı. 60+ dağıtım noktası, Avrupa+Kuveyt ihracat ⭐. Beymen Club tasarımcısı geçmişi. Site profesyonel, editorial lookbook boşluğu görünür. Draft r-4880065117606088474. ⚠️ Ayhan gönderim teyidi bekleniyor. |
| İKOLL | C2 | 2026-06-30 | ARŞİV(ICP-DÜŞÜK) | 2026-06-30 | info@ikoll.com | — | 105K IG @ikoll_collection, Merter üretim+Hepsiburada dağıtım = mid-market/mass segment. Taslak yapılmadı (editorial ihtiyaç belirsiz). |
| MoorOfMoor | C2 | 2026-06-30 | ARŞİV(ICP-DÜŞÜK) | 2026-06-30 | — | — | Bomonti toptan+tedarik mağazası. Facebook var, email yok. B2B toptan = içerik ortaklığı profili değil. |
| MiArte & Neri | C2 | 2026-06-30 | ARŞİV(ICP-DÜŞÜK) | 2026-06-30 | — | — | Toptan büyük beden (@miarteoffical 28K), Telegram only, email yok. KANAL-YOK + ICP DÜŞÜK. |
| KK Design | C2 | 2026-06-30 | ARŞİV(ICP-DÜŞÜK) | 2026-06-30 | — | — | kkdesignn.com — modest fashion (hijab/tesettür/oversized). HİLAY/MICCA ile aynı segment. |
| VIADEL | C2 | 2026-06-30 | DOĞRULANAMADI | 2026-06-30 | — | — | MİSLE TEKS işletiyor, IFCO Hall 4/B-9. Doğrudan site/email bulunamadı. Cooldown: 2026-07-14 |

## 3 · ROTASYON İŞARETİ (hangi listede nereye kadar gelindi)
*Her koşu, işlediği son hedefi buraya yazar; ertesi koşu BURADAN devam eder (baştan değil).*
- **Şerit A** (sıcak çember): işlenen son = — *(Ayhan onayı bekliyor; otomatik temas YOK)*
- **Şerit B** (ajanslar): işlenen son = ArtArda Reklam (ARŞİV, Ankara). ⚠️ Tüm B havuzu tükendi. TAKİP-1 koşusu yapıldı Jun 30 (IT'S BASIC/ddip/NOX/KÜRE/AHTAPOT/DijiCrea). Sıradaki B besleme: dijitalajanslar.com → yeni isimler eklenmeli (Pazartesi koşusu). Bigumigu/MediaCat: moda-odaklı içerik üretim ajansı bulunamadı.
- **Şerit C1** (Who's Next Paris): işlenen son = BASARIN LEATHER & FUR (29 Haz, taslak). C1 havuzu tamamlandı — cooldown bekleyenler 2026-07-08'den sonra (MARGITTES/FONEM/DOLCEZZA/SOFISA/NILMARK/YXL/L'ATELIER/MON REVE/MILOU/BIRELIN/CLANDE/LAMANTE/PUNKQUEEN/HİSSET/TERZİ DÜKKANI). LUOKK/BASAKLA/MERI CREATIVE/MODA KREATİF ARŞİVE alındı (pre-motor G+10 geçmiş).
- **Şerit C2** (IFCO): işlenen son = NUR KALAY COLLECTION (30 Haz, taslak). Sonraki araştırılacaklar: CARDUCCI/SİMONİ CLUB · MİMYA · NESİL · EXPLOSION · PARK HANDE · PUREVA · ACREPRIVE (IFCO sayfa 2-3 kalan).
- **Pazartesi besleme kaynak sırası** (dönüşümlü): dijitalajanslar.com → İHKİB/fuar duyuruları → Bigumigu/MediaCat yeni iş haberleri → *(başa dön)*. Sıradaki = dijitalajanslar.com *(29 Haz Pazartesi: Bigumigu/MediaCat denendi, moda ajans yok → döngü başa döndü)*.
- **Kritik yaklaşan tarihler:** TAKİP-2 → 4 Temmuz: MA MULIER / VDR / BİZE FASHION / ZILBERMAN (G+10 original). C1 cooldown bitiyor: 2026-07-08.

## 4 · KOŞU GÜNLÜĞÜ (her koşu 1 satır — kalıcılık kanıtı / heartbeat)
*Bir koşu burada satır bırakmadıysa: o koşu persistence adımına VARAMADI (timeout / hata / sandbox / push reddi). Bu durumda çözülecek İLK şey budur — dedup defteri ancak inerse işe yarar.*

| Tarih | Yeni aday | Doğrulanan | Taslak (Gmail) | Yanıt | Takip | Push | Not |
|---|---|---|---|---|---|---|---|
| 2026-06-24 | 8 (5 marka/ajans + 3 DOĞRULANAMADI) | 5 | 5 (LUOKK/IT'SBASIC/BASAKLA/MeriCreative/ModaKreatif) | 0 | 0 | ✅ | İlk başarılı koşu. Dedup+push düzeltmesi çalışıyor. 3 C1 ihracatçı markası + 2 ajans. V1/V2 dönüşümü test ediliyor. |
| 2026-06-24 (ek) | +19 yeni isim havuza eklendi (IFCO tam liste + ddip) | 2 | 2 (VDR/ddip) | 0 | 0 | ✅ | "Yeni alternatifler" genişlemesi: IFCO sayfaları tarandı (78 katılımcıdan 30+), ddip Paris+İstanbul bulundu. Havuzda şimdi 40+ aktif C2 isim. |
| 2026-06-24 (tam genişleme) | +28 yeni hedef araştırıldı (Şerit B+C1+C2 toplu) | 14 | 14 (BİZE/VUQU/CrabsMedia/Istcode/BossyDigital/NOX/MAMULIER/KüreAjans/Ahtapot/CreativeDijital/ZILBERMAN/UKUŞ/DijiCrea/NAGRADA) | 0 | 0 | ✅ | "Hepsine taslak oluştur" komutu — havuzdaki tüm doğrulanabilir hedefler işlendi. 14 yeni taslak Gmail'de. 10+ KANAL-YOK/DOĞRULANAMADI cooldown'a alındı. |
| 2026-06-28 | 1 doğrulanan (EXQUISE) + 3 DOĞRULANAMADI (MİANOTTE/AHSEN/HALE AKKESE) + 2 ARŞİV-ICP (HİLAY/SBL) | 1 | 5 (4 TAKİP-1: MA MULIER/VDR/BİZE/ZILBERMAN + 1 yeni: EXQUISE) | 0 (Nakit M.) | 4 | ✅ | ⚠️ RISK-BAYRAK: 6 hedef 2x gönderildi (BossyDigital/VUQU/Ukuş/CreativeDijital/NAGRADA/CrabsMedia) — bu hedeflere TAKİP atlandı. Tüm "İŞLENDİ" statüleri "GÖNDERİLDİ" olarak güncellendi (sent search teyit). Jendue yanıtı (TAG-KLOI kanalı — Nakit Motoru değil) mevcut — Ayhan takibi gerekli. |
| 2026-06-29 | 1 doğrulanan (BASARIN) + 5 DOĞRULANAMADI + 4 KANAL-YOK + 9 ARŞİV-ICP | 1 | 1 (BASARIN — Gmail taslak r-17585630848522458) | 0 | 0 | ✅ | ⚠️ POOL UYARI: C2 IFCO havuzunun büyük çoğunluğu ICP uyumsuz (toptan/tesettür/imalatçı/büyük-köklü). Pazartesi B besleme: Bigumigu/MediaCat denendi → moda ajans yok. B havuzu tükendi — dijitalajanslar.com yeniden taranmalı. C1'den son aday: BASARIN (Première Vision Paris ihracatçı). C2'den kalan: İKOLL/KK DESIGN/MİARTE/CARDUCCI/MİMYA/VIADEL vb. Takip zamanları: MA MULIER/VDR/BİZE/ZILBERMAN TAKİP-2 → 4 Temmuz (G+10 original). |
| 2026-06-30 | 1 yeni (NUR KALAY) · 6 araştırıldı/ARŞİV (İKOLL/MoorOfMoor/MiArte/KK Design/VIADEL + NUR KALAY) | 1 (NUR KALAY) | 7 (6 TAKİP-1 + 1 yeni NUR KALAY) | 0 nakit motoru | 6 | ✅ | TAKİP-1 yapılanlar: IT'S BASIC/ddip/NOX/KÜRE/AHTAPOT/DijiCrea (Jun 24 gönderim G+6). ARŞİV: LUOKK/BASAKLA/MERİ CREATIVE/MODA KREATİF (pre-motor Jun 15-16 gönderim, G+10 geçmiş). Yanıt: 0 nakit motoru (3 TAG-KLOI thread aktif — Ayhan yönetiyor). C2 havuzu daralıyor: kalan = CARDUCCI/MİMYA/NESİL/EXPLOSION/PARK HANDE/PUREVA/ACREPRIVE. ⚠️ EXQUISE+BASARIN taslakları hâlâ Gmail'de — Ayhan gönderim teyidi bekleniyor. |

---
*Bağlı: `nakit-motoru-hedef-havuzu.md` (aday universe) · `soguk-iletisim-protokolu.md` (kurallar) · Notion Müşteri Panosu (yalnız görüşmeye dönenler terfi eder). Bu defter = "yapıldı" hafızası; havuz = "yapılabilir" listesi.*
