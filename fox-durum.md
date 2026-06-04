# Fox — DURUM / Kaldığımız Yer
*Yeni oturumda İLK okunan belge. "Şu an neredeyiz" — tek bakışta devral. Her önemli gelişmede güncellenir.*

**Son güncelleme:** 4 Haziran 2026 · **Statü:** Çırak / Filo Modu (Denetmen + orkestrasyon aktif)

---

## ŞU AN NEREDEYİZ (özet)
4 Haziran'da devasa bir kuruluş günü yaşandı. Marka Bulutu OS'un Teslim Zinciri kuruldu, Fox 6 protokol + 2 parmak izi kazandı, operasyon altyapısı (Notion pano, Gmail etiket, 8 rutin, pdf-motoru v2) ayağa kalktı. İki açık kaynak repo (Corey Haines birincil, zubair ikincil) özümsendi.

## FİLO (aktif)
Fox (orkestratör) · Denetmen (7 mercek) · Keşif&Denetim · Strateji · İçerik · Growth · Branding.
**Yok:** İş Katmanı (Satış/Finans/Hukuk/Operasyon), Görev Ajanı, Kendi Markan Ajanı.

## AÇIK İŞLER — Ayhan'ın masasında
1. **Darya takip maili** — taslak hazır (Gmail draft), gönderim Ayhan'da
2. **gmail-personal** (stepsonclouds@) — OAuth yarım
3. **Scheduled task'lar** — bir kez "Run now" ile onayla (izin otursun)
4. **Canva brand kit** — manuel kurulum
5. **Towdoo teklifi + Ala dosyaları** — v2 estetiğine geçirilsin mi? (açık)
6. **Nesa/Luxmed** — çıkar çatışması, sözleşme öncesi stratejik karar
7. **Çırak→Kalfa terfisi** — Ayhan zamanı gelince

## YAKLAŞAN TAKVİM
- **Cuma 5 Haz:** 12:00 Towdoo (Tuğba+Furkan) — denetim PDF+45K teklif+AI projeksiyon hazır · 14:00 Melek→Tuncay (Ala)
- **Pazar 7 Haz:** 07:30-14:00 Empati Koşusu
- **Pzt 8 Haz:** 10:00 Enes/Luxmed araması

## RİSK BAYRAKLARI
- Nesa↔Luxmed çatışması · SOC kendi tracking'i yok · Towdoo'da Sanem hassasiyeti + "global=teklif değil dayatma" + kurucu hikâyesi gerçek olmalı

## SIRADAKİ BÜYÜK ADIM (öneri)
Ya İş Katmanı ajanlarını tamamla, ya bir müşteride (Darya ideal) uçtan uca **gerçek pilot** yap (sistem sahada kanıtlansın). En acil tekil aksiyon: Darya takip maili.

## DETAY HARİTASI (lazım oldukça oku — hepsini birden yükleme)
- Kim/vizyon: `fox-kuzey-yildizi.md`
- Kişiler/ilişki: `fox-iliski-hafizasi.md` (Tuğba=anne figürü, Tuncay=Ala/kaykay, Darya, Enes, Melek, Sanem-gerilim)
- Kararlar+gerekçe: `fox-karar-gunlugu.md`
- Ayhan'ın sesi: `fox-ses-parmak-izi.md` · estetiği: `fox-gorsel-parmak-izi.md`
- Ajan tanımları: `.claude/agents/*.md`
- Üretim: `sablonlar/pdf-motoru.py` (v2, Didot), `sablonlar/araclar/marka_analiz.py`
- Müşteri context şablonu: `sablonlar/musteri-marka-context-sablonu.md`
- Protokoller: hafıza, orkestrasyon, öz-denetim/nöbet · Müfredatlar: gelişim, büyüme, estetik
- Notion pano data source: `f4c97159-9c85-4766-b122-760b00b9c321`

## SÜREKLİLİK & GİT
- **SSH push kurulu** (ed25519, github.com:stepsoncloudscom/Fox) — kimlik derdi yok, `git push origin main` doğrudan çalışır.
- **Checkpoint emri:** Context dolunca/oturum biterken → bu dosyayı güncelle + commit + push (izin bekleme). Bkz. CLAUDE.md Disiplin.
- **Ses kuralı:** Ayhan'a motivasyon/övgü cümlesi YOK — doğrudan işe geç.

---
*Disiplin: Her oturum sonu bu dosyayı güncel tut + commit + push. Yeni Fox bunu + CLAUDE.md okuyunca tam devralır.*
