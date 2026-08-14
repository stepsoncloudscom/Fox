# Fox — DURUM / Kaldığımız Yer

**Son güncelleme: 15 Ağustos 2026** *(14-15 Ağu oturumu)*
**Kural: bu dosya 40 satırı geçmez.** Biriken geçmiş → [`raporlar/oturum-gunlugu.md`](raporlar/oturum-gunlugu.md). Bu dosya "şu an neredeyiz"i söyler, "ne yapmıştık"ı değil.

## AKTİF CEPHELER
| Cephe | Durum | Sıradaki adım | Kimde |
|---|---|---|---|
| **Özgür Irmak Protez ve Ortez** (medikal) | Canlı iş — web/blog/metin üretimi sürüyor | ↓ alt kalemler | karışık |
| · Yürüme Analizi sayfası | v0.2 hazır, **YAYIN BLOKLU** — 11 teknik kalem tedarikçi şartnamesinden geldi, merkezin envanteri teyitli değil (Denetmen D1) | Teyit soru setini Özgür Bey'e ilet; teyitsiz kalem cümlesiyle birlikte çıkarılır | Ayhan → Özgür Bey |
| · Blog (5 yazı) | İnsan Sesi Kapısı'ndan geçti, Wix'te **DRAFT** | Yayın onayı | Ayhan |
| · Hakkımızda v0.7 | Metin hazır | Üniversite adı/yıl **belgesi** gelmeden yayınlanmaz | Özgür Bey |
| · KVKK politikası v01 | PDF + docx hazır | Avukat/Ayhan onayı | Ayhan |
| **Steps On Clouds** (kendi marka) | ⚠️ *Bu blok 10–20 Haz kayıtlarından taşındı, tazeliği teyit edilmedi* | Wix Editor'a copy yapıştırma · mağaza mekanizması kararı ("destekler" mi "finanse eder" mi) · Run For Empathy mailleri | Ayhan |
| **Orhan doğum günü kart oyunu** (kişisel, Ayhan+Melek) | Brief v01 hazır (9 Ağu) | Joker kart içerikleri + yaş teyidi | Ayhan |
| **Fox / Marka Bulutu OS gelişimi** | 14-15 Ağu: A + B + C üçü de koştu | **A ✅** · **B ✅** (TZP + Kanıt Üçgeni T0 — site yayın bulgusu çıktı) · **C ✅ iskelet** → Ayhan'da 5 karar (fiyat kademeleri · K0 ücretli mi · platform maliyeti kimde · para birimi · Pipeline ajanı kurulsun mu) | Ayhan |

## AYHAN'DA BEKLEYENLER (bloklayan)
1. 🔴 **Özgür Protez sitesi yayında değil** — Wix planı kimin adına/bütçesiyle yükseltilecek + yayın öncesi hangi kapılar (avukat) kapanmalı? Cevaplanmadan içerik üretmek stok biriktirmektir.
2. Özgür Bey'e **11 kalemlik teknik teyit** talebi — Yürüme Analizi sayfasının tek kapısı.
3. Blog 5 yazı yayın onayı (Wix'te draft duruyor).
4. SOC mağaza mekanizması kararı.

## RİSK BAYRAKLARI
- 🔴 **TESLİM ≠ ERİŞİM (15 Ağu, ölçüldü):** Özgür Protez Wix sitesi **Draft** — URL **404**; `ozgurprotez.com` hâlâ "YENİLENİYORUZ". 6 haftalık üretim (5 blog · Hakkımızda · ~70 ürün metni · KVKK) **kamuya görünmüyor**. Site dili yalnız `tr` (4-dil hedefi uygulanmamış), plan **Free** (özel alan adı bağlanamaz). Ölçüm: `raporlar/ozgur-irmak-kanit-ucgeni.md`. Panzehir: Denetmen 10. mercek **Erişilebilirlik**.
- 🔴 **Döviz/global pipeline boş.** Özgür Protez aktif ama TL. Kuzey Yıldızı #3 (globalleşme) karşılıksız. *(20 Haz'ın "hiç iş yok" bayrağı geçersiz — Özgür Protez o tarihten sonra geldi.)*
- ⚠️ **Sözleşme/ödeme durumu bu dosyada kayıtlı değil** — Özgür Protez'in hangi kalemi faturalandı, teyit edilmeli.
- ⚠️ **Medikal içerikte uydurma sıfır toleransı:** TİTCK + YMYL. Teyitsiz teknik veri "yumuşatılarak" bırakılmaz, çıkarılır.
- ⚠️ Her görsel çıktı render-and-review'den geçer (5 Haz dersi).

## DETAY HARİTASI (lazım oldukça oku — hepsini birden yükleme)
- Geçmiş oturumlar: `raporlar/oturum-gunlugu.md` · Teslim/maliyet kaydı: `raporlar/teslim-kutugu.md`
- Vizyon: `fox-kuzey-yildizi.md` · Kişiler: `fox-iliski-hafizasi.md` · Kararlar: `fox-karar-gunlugu.md`
- Ses: `fox-ses-parmak-izi.md` + `fox-metin-insan-sesi-korpusu.md` · Görsel: `fox-gorsel-parmak-izi.md`
- Ajanlar: `.claude/agents/*.md` · Ortak sistemler: puanlama rubriği · görsel üretim standardı · TZP · Kanıt Üçgeni
- Müşteri context: `sablonlar/*-marka-context.md` · Sektör bağları: moda · medikal-protez
- Notion pano data source: `f4c97159-9c85-4766-b122-760b00b9c321`

## SÜREKLİLİK (otomatik)
- **SessionStart hook:** `git pull` + bu dosyayı yükler.
- **SessionEnd hook:** `.claude/hooks/fox-checkpoint.sh` — değişiklik varsa otomatik commit + push. Fox unutsa bile iş kaybolmaz.
- **PreCompact hook:** `.claude/hooks/fox-durum-uyari.sh` — context dolarken bu dosyanın kaç gün bayat olduğunu yüzüne söyler.
- Hook'lar ağ değil disiplin yedeğidir: **bu dosyayı Fox güncellemekle yükümlüdür**, hook yalnız kaybı önler.
