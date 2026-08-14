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

## Aylık rollup

| Ay | Teslim | İlk turda kabul | Ort. tur | En sık red sebebi |
|---|---|---|---|---|
| Ağu 2026 | *(ay sonunda)* | | | |

## Şimdiden görünen örüntü (5 satır, temkinli okuma)
Redlerin **hiçbiri** biçim/format hatası değil — üçü de **kaynak yokluğu** ile ilgili: teyitsiz veriyle yazmak (4), yaşanmışlık olmadan hikâye kurmaya çalışmak (2), ölçülmemiş SERP niyetine yazmak (1). Kök neden kuralı bunu zaten söylüyordu: *somutluk kotası dolmazsa üslupla kapatma, müşteriden olgu iste.* Kural yazılıydı; **işin başında değil, redden sonra uygulanıyordu.**

**Bundan çıkan kapı (14 Ağu):** üretim başlamadan önce Metin Yazarı "elimdeki teyitli olgu sayısı" satırını yazar; kota dolmuyorsa metin yazılmaz, **önce soru seti müşteriye gider.**
