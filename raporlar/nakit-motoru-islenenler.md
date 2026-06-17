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
| *(boş — ilk koşu dolduracak)* | | | | | | | |

## 3 · ROTASYON İŞARETİ (hangi listede nereye kadar gelindi)
*Her koşu, işlediği son hedefi buraya yazar; ertesi koşu BURADAN devam eder (baştan değil).*
- **Şerit A** (sıcak çember): işlenen son = — *(Ayhan onayı bekliyor; otomatik temas YOK)*
- **Şerit B** (ajanslar): işlenen son = — *(baştan)*
- **Şerit C1** (Who's Next Paris): işlenen son = — *(baştan)*
- **Şerit C2** (IFCO): işlenen son = — *(baştan)*
- **Pazartesi besleme kaynak sırası** (dönüşümlü): dijitalajanslar.com → İHKİB/fuar duyuruları → Bigumigu/MediaCat yeni iş haberleri → *(başa dön)*. Sıradaki = dijitalajanslar.com

## 4 · KOŞU GÜNLÜĞÜ (her koşu 1 satır — kalıcılık kanıtı / heartbeat)
*Bir koşu burada satır bırakmadıysa: o koşu persistence adımına VARAMADI (timeout / hata / sandbox / push reddi). Bu durumda çözülecek İLK şey budur — dedup defteri ancak inerse işe yarar.*

| Tarih | Yeni aday | Doğrulanan | Taslak (Gmail) | Yanıt | Takip | Push | Not |
|---|---|---|---|---|---|---|---|
| *(ilk koşu buraya yazacak)* | | | | | | | |

---
*Bağlı: `nakit-motoru-hedef-havuzu.md` (aday universe) · `soguk-iletisim-protokolu.md` (kurallar) · Notion Müşteri Panosu (yalnız görüşmeye dönenler terfi eder). Bu defter = "yapıldı" hafızası; havuz = "yapılabilir" listesi.*
