# Fox — DURUM / Kaldığımız Yer

**Son güncelleme: 24 Ağustos 2026** *(21-24 Ağu oturumu — Levitate hattı)*
**Kural: 40 satır tavanı.** Biriken geçmiş → [`raporlar/oturum-gunlugu.md`](raporlar/oturum-gunlugu.md). Bu dosya "şu an neredeyiz"i söyler, "ne yapmıştık"ı değil.

## AKTİF CEPHELER
| Cephe | Durum | Sıradaki adım | Kimde |
|---|---|---|---|
| **Özgür Irmak Protez ve Ortez** (medikal) | Canlı iş — web/blog/metin üretimi sürüyor | ↓ alt kalemler | karışık |
| · Levitate hattı (13 ürün) | **Wix'e YÜKLENDİ** — 13 ürün + metin + görsel (13/13), fiyat ₺0,00, hepsi Ayaklar kategorisinde, site Draft | ÜTS/TİTCK teyidi + 4 teknik teyit (yayın kapısı) | Fox / Özgür Bey |
| · Yürüme Analizi sayfası | v0.2 hazır, **YAYIN BLOKLU** — 11 teknik kalem tedarikçi şartnamesinden, envanter teyitsiz (Denetmen D1) | Teyit setini Özgür Bey'e ilet; teyitsiz kalem çıkarılır | Ayhan → Özgür Bey |
| · Blog (5 yazı) | İnsan Sesi Kapısı'ndan geçti, Wix'te **DRAFT** | Yayın onayı | Ayhan |
| · Hakkımızda v0.7 | Metin hazır | Üniversite adı/yıl **belgesi** gelmeden yayınlanmaz | Özgür Bey |
| · Sosyal biyografiler (IG/FB/LI×2/YT) | v0.2 hazır, Denetmen turu kapandı | Slot verisi (konum/tel/e-posta/link) + 2 karar (🕊 emoji · LinkedIn hesap tipi) | Ayhan |
| · KVKK politikası v01 | PDF + docx hazır | Avukat/Ayhan onayı | Ayhan |
| **Steps On Clouds** (kendi marka) | ⚠️ tazeliği teyitsiz (Haz kayıtları) | Wix copy · mağaza mekanizması kararı · Run For Empathy mailleri | Ayhan |
| **Orhan doğum günü kart oyunu** (kişisel) | Brief v01 hazır (9 Ağu) | Joker kart içerikleri + yaş teyidi | Ayhan |
| **Fox / Marka Bulutu OS gelişimi** | 14-15 Ağu A+B+C koştu, iskelet hazır | Ayhan'da 5 karar (fiyat kademeleri · K0 ücretli mi · platform maliyeti · para birimi · Pipeline ajanı) | Ayhan |

## AYHAN'DA BEKLEYENLER (bloklayan)
1. 🔴 **Özgür Protez sitesi yayında değil** — Wix planı kimin adına/bütçesiyle yükseltilecek + yayın öncesi hangi kapılar (avukat) kapanmalı? Cevaplanmadan içerik üretmek stok biriktirmektir.
2. Özgür Bey'e teknik teyit talepleri: Yürüme Analizi 11 kalem + **Levitate 4 kalem + ÜTS/TİTCK kaydı**.
3. Blog 5 yazı yayın onayı (Wix'te draft duruyor).
4. SOC mağaza mekanizması kararı.

## RİSK BAYRAKLARI
- 🔴 **TESLİM ≠ ERİŞİM (15 Ağu, ölçüldü):** site **Draft**, URL 404, `ozgurprotez.com` "YENİLENİYORUZ". 6 haftalık üretim (5 blog · Hakkımızda · ~85 ürün metni · KVKK) kamuya görünmüyor. Dil yalnız `tr`, plan **Free**. Ölçüm: `raporlar/ozgur-irmak-kanit-ucgeni.md` · Panzehir: Denetmen 10. mercek Erişilebilirlik.
- 🔴 **Döviz/global pipeline boş.** Özgür Protez aktif ama TL. Kuzey Yıldızı #3 (globalleşme) karşılıksız. *(20 Haz'ın "hiç iş yok" bayrağı geçersiz — Özgür Protez o tarihten sonra geldi.)*
- ⚠️ Özgür Protez'in hangi kalemi faturalandı — **sözleşme/ödeme durumu kayıtlı değil**, teyit edilmeli.
- ⚠️ **Medikal içerikte uydurma sıfır toleransı:** TİTCK + YMYL. Teyitsiz veri yumuşatılmaz, çıkarılır.
- ⚠️ **Levitate görselleri düzeltme turu görmedi** (Ayhan kararı) — Forever/Blade'de logo kalıntısı ihtimali; sitede canlıya çıkmadan gözden geçirilmeli.
- ⚠️ **IP açık:** üretici görselinden marka silme (telif + debranding) ve TİTCK ile marka hukukunun ters çekmesi. Avukat sorusu kapanmadı.

## DETAY HARİTASI (lazım oldukça oku)
- Geçmiş: `raporlar/oturum-gunlugu.md` · Maliyet: `raporlar/teslim-kutugu.md` · Vizyon: `fox-kuzey-yildizi.md` · Kişiler: `fox-iliski-hafizasi.md` · Kararlar: `fox-karar-gunlugu.md`
- Ses: `fox-ses-parmak-izi.md` + `fox-metin-insan-sesi-korpusu.md` · Görsel: `fox-gorsel-parmak-izi.md` · Ajanlar: `.claude/agents/*.md`
- Müşteri context: `sablonlar/*-marka-context.md` · Sektör: moda · medikal-protez · Notion: `f4c97159-9c85-4766-b122-760b00b9c321`

## SÜREKLİLİK (otomatik)
Hook'lar: SessionStart `git pull`+bu dosya · SessionEnd oto commit+push · PreCompact bayatlık uyarısı. **Hook disiplinin yerine geçmez — bu dosyayı Fox güncellemekle yükümlüdür.**
