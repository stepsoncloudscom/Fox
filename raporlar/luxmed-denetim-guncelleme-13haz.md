# LUXMED PROTEZ — DENETİM GÜNCELLEMESİ (Tazeleme Turu)

**Hazırlayan:** Keşif & Denetim Ajanı — Marka Bulutu OS
**Tarih:** 13 Haziran 2026
**Statü:** Kademe 2 — Denetmen denetimi + Ayhan onayı bekliyor
**Kapsam:** Tam denetim DEĞİL — 10 Haziran 2026 baseline'ının (`luxmed-marka-denetim-raporu.md`) tazeleme turu. Rubrik v1 §0.1 (İki Katman Kanıt) disiplini korunmuştur.
**Yöntem:** Site doğrudan taraması (WebFetch), web arama (SERP gözlemi), Bookimed/Yandex/Trustpilot 3. taraf platform kontrolü. Sosyal platformlara doğrudan erişim kısıtlı; kamuya açık arama verisi kullanıldı.

---

## 1. DELTA ÖZETİ — 10 Haziran → 13 Haziran

| Durum | Bulgu |
|---|---|
| **AYNI** | HTTP 403 devam ediyor: ana sayfa, /en, /hakkimizda bugün de doğrudan erişime kapalı (13 Haz testi). |
| **AYNI** | Google Maps **4.7/5 — 190 yorum** (Zavis dizin kaydı üzerinden teyit; doğrudan Maps erişimi araçla mümkün değil). Baseline Tip A metriği geçerli. |
| **AYNI** | @luxmedprosthetic 14K takipçi / 130 post. Konumlandırma ve görsel kimlik bulgularında aksini gösteren veri yok. |
| **RAFİNE** | 403 bulgusunun riski yeniden tanımlandı (aşağıda §2b). İndeksleme korunuyor; asıl maliyet AI görünürlüğü + 3. taraf senkron. **Bot koruması 13 Haz'da doğrudan test edildi — bkz. §2b.** |
| **DÜZELTME** | Baseline'daki "fiyat bilgisi yok" ifadesi hatalıymış (aşağıda §2a). Sitede güncel fiyat/SGK sayfaları VAR. |
| **YENİ** | Yandex Maps, Trustpilot, üçüncü Facebook hesabı (Arapça), TikTok hesabı, TR Instagram takipçi sayısı, Bookimed profil detayı (aşağıda §3-5). |

**Sonuç:** Site tarafında 3 günde anlamlı değişiklik yok (beklenen). Delta'nın değeri, baseline'da erişilemeyen 3. taraf görünümlerin netleşmesi + 2 baseline düzeltmesi.

---

## 2. BASELINE GEÇERLİLİĞİ

7 kategorinin niteliksel bantları **geçerliliğini koruyor**: 1 Kritik Açık (Dijital Altyapı) · 3 Orta (Mesaj/İçerik, İçerik&SEO, SEO/Görünürlük) · 2 Zayıf (Kimlik&Konumlandırma, Görsel Kimlik) · 1 İyi (Sosyal Medya/Güven Sinyali). Sayısal genel skor verilmemesi kararı (§0.1 — tek Tip A kategorisi) bugün de doğru: GSC/Analytics hâlâ bağlı değil.

İki revizyon notu:

### 2a. DÜZELTME — "Fiyat bilgisi yok" ifadesi
Baseline yönetici özetinde "Fiyat bilgisi yok" yazılmıştı. **Bugünkü SERP taraması aksini gösteriyor:** sitede özel fiyat sayfaları var ve indeksli:
- `luxmedprotez.com/protez-bacak-fiyatlari` — başlık: "2026 Protez Bacak Fiyatları (Mart Teklifi)" → **Mart 2026 güncel**
- `luxmedprotez.com/guncel-sgk-protez-odemeleri` — başlık: "[Şubat 2026]" → **Şubat 2026 güncel**
- Snippet içeriği somut: SGK biyonik bacak ödemesi 115.000 TL; biyonik kol 950.000 TL'den başlıyor (sitenin kendi beyanı)

Bu bir **güç**: fiyat/SGK şeffaflığı YMYL'de güven sinyali + AI Overview'a uygun yapılandırılmış içerik. Baseline'ın bu kalemi 403 nedeniyle eksik gözlemlenmiş; düzeltildi.

### 2b. RAFİNE — HTTP 403'ün gerçek maliyeti
Baseline "Googlebot da etkileniyorsa indeksleme kaybı" senaryosunu açık bırakmıştı. **Bugünkü kanıt: indeksleme korunuyor.** Şubat/Mart 2026 tarihli sayfa başlıkları Google SERP'te taze görünüyor → Googlebot'a izin verilmiş seçici bot koruması.

**13 Haz — DOĞRUDAN TEST (birinci el kanıt):** Ana sayfaya 4 farklı kimlikle `curl` isteği atıldı:

| İstemci kimliği (User-Agent) | Sonuç |
|---|---|
| Normal tarayıcı (Chrome/Mac) | **403** |
| GPTBot (OpenAI) | **403** |
| ClaudeBot (Anthropic) | **403** (`cf-ray` header → **Cloudflare doğrulandı**) |
| Kimliksiz | **403** |
| `robots.txt` | **403** (erişilemedi) |

Yorum: Blok **UA-bazlı değil** — JS çalıştırmayan/Cloudflare challenge'ı geçemeyen her otomatik istemci 403 alıyor. Gerçek tarayıcı (JS + çerez) ve Cloudflare'in IP'den doğruladığı Googlebot geçer; AI asistan crawler'ları (JS render etmez, çoğu verified-bot listesinde değil) geçemez. "Büyük olasılıkla blokta" çıkarımı → **test edilmiş gerçek.** (Not: gerçek Googlebot IP-doğrulamasıyla geçtiği için curl ile taklit edilemez; indeksleme kanıtı SERP tazeliğinden geliyor, çelişki yok.)

Yeniden tanımlanan risk alanı:
1. **AI görünürlüğü (GEO):** AI asistan crawler'ları (GPTBot, ClaudeBot, PerplexityBot vb.) **test edildi — blokta** (yukarıdaki tablo). Sektör analizleri sağlık aramalarının giderek büyüyen bir bölümünün AI özetiyle karşılandığını gösteriyor (kesin oran için doğrulanmış kaynak gerekli — bu turda WebSearch limiti nedeniyle adlandırılamadı; müşteri belgesine sayı KONULMADI). Uluslararası hasta "best prosthetic clinic Istanbul"u artık AI'ya soruyor; site AI'ya kapalıysa anlatının kaynağı kendi sitesi olamaz, üçüncü taraf kayıtlarına (bayat Bookimed) kalır.
2. **3. taraf platform senkronu:** Bookimed/Zavis gibi platformlar site verisini çekemez → profiller bayatlıyor (Bookimed'de doğrulandı, §3).
3. **Ölçümsüzlük sürüyor:** PageSpeed/CWV dışarıdan ölçülemiyor.

Aksiyon değişmedi (bot koruması yapılandırması gözden geçirilmeli) ama gerekçe netleşti: sorun "Google'dan düşmek" değil, **AI çağında görünmezlik + platform bayatlaması.**

---

## 3. BOOKIMED GÖRÜNÜRLÜK BULGUSU (görev sorusu)

**Profil CANLI:** `us-uk.bookimed.com/clinic/luxmed-protez/` — "Luxmed Protez Clinic" olarak listeleniyor. Detay (13 Haz görünümü):

| Alan | Durum | Not |
|---|---|---|
| Puan | 4.6/5 (Google kaynaklı) | **Yalnızca 5 Google yorumu gösteriliyor** — gerçek varlık 190 yorum. Profil, en güçlü sosyal kanıtın %3'ünü yansıtıyor. |
| Fiyat | Limb prosthetics **$2.460** · Bone Fracture Treatment $2.735 | **Son güncelleme: 29.03.2025 — ~15 ay bayat.** "Bone Fracture Treatment" kalemi protez merkezi profili için yabancı görünüyor (platform oto-kategorisi olabilir). |
| Doktor | "3 doktor" sayısı var, **bireysel profil yok** | E-E-A-T açısından boş — uzman kimliği görünmüyor. |
| Fotoğraf | 5 adet (dış cephe, resepsiyon, rehabilitasyon) | Yandex'te 48 foto varken Bookimed'de 5. |
| Doğrulama | "Verified" rozeti görünmüyor | |
| Hasta kaynağı (platform beyanı) | "En sık BDT, Balkanlar ve Arap Ligi ülkelerinden hasta" | Uluslararası konumlandırma için alıntılanabilir platform verisi. |

**⚠️ Teyit sorusu (Enes'e):** Görüşme notlarındaki **€11.200 paket kamuya açık profilde görünmüyor.** Girilen paket yayına alınmamış olabilir, farklı bir sayfada olabilir veya profil önbelleği eski olabilir — Enes'in Bookimed panelinden kontrol etmesi gerekiyor. (Rakam doğrulanmamış; masa özetine alınmadı.)

**Özet:** Uluslararası kanal kapısı açık ama vitrin yarım: bayat fiyat, 5/190 yorum, profilsiz doktorlar, az fotoğraf. Düşük eforlu/yüksek etkili tazeleme adayı.

---

## 4. YENİ DOĞRULANAN VARLIKLAR — Tip A: Yandex · gözlem (Tip B): Trustpilot, IG-TR (baseline'da yoktu)

1. **Yandex Maps: 4.9/5 — 25 yorum** (`yandex.com.tr/maps/org/luxmed_protez/40364500883/`). Zengin kayıt: 48 fotoğraf, tam erişilebilirlik beyanı (tekerlekli sandalye erişimi, rampa, erişilebilir tuvalet/otopark), ödeme yöntemleri, panorama. **Stratejik değer: Yandex = Rusya/BDT pazarının arama motoru.** Rus hastanın doğal arama yolunda 4.9 hazır duruyor — baseline'ın "Rusça dijital varlık yetersiz" bulgusunu kısmen dengeleyen, kaldıraçlanmamış varlık.
2. **Trustpilot: 7 yorum** (`trustpilot.com/review/luxmedprotez.com`). Skor arama üzerinden doğrulanamadı (Trustpilot kendi bot koruması fetch'i engelliyor — Luxmed'den bağımsız). Görünen yorum içerikleri olumlu: havalimanı karşılama, konaklama, fizyoterapi süreci anlatılıyor. Üçüncü bağımsız güven platformu — düşük hacimli, işlenmemiş.
3. **Instagram TR hesabı netleşti:** @luxmedprotez **1.521 takipçi** (baseline'da "bilinmiyor — muhtemelen düşük" idi; doğrulandı). Bölünme rakamla kanıtlı: 14.000 (EN) vs 1.521 (TR).

---

## 5. KANAL ENVANTERİ GÜNCELLEMESİ

Baseline 5 kanal saymıştı (2 IG + 2 FB + YT + LinkedIn). Bugünkü tarama **8 varlık** gösteriyor:

| Kanal | Hesap | Gözlem |
|---|---|---|
| Instagram | @luxmedprosthetic | 14K — ana hesap, EN ağırlıklı |
| Instagram | @luxmedprotez | 1.521 — TR, zayıf |
| Facebook | /luxmedprosthetic | Baseline: 8.4K (bugün yeniden doğrulanamadı — platform erişimi kısıtlı; baseline değeri korunuyor) |
| Facebook | /luxmedprotez | Varlığı baseline'dan; bugün ayrıca listelenmedi |
| Facebook | **/luxmedprotez.ar — YENİ TESPİT** | Arapça sayfa ("Luxmed Prosthesis Center"). Dil stratejisi olarak mantıklı OLABİLİR ama plansız çoğalmanın parçasıysa bölünmeyi derinleştirir. Aktiflik/takipçi ölçülemedi. |
| YouTube | @luxmedprotez | Aktif; hasta içerikli Shorts mevcut |
| TikTok | **@luxmedprosthetic — YENİ TESPİT** | Varlık doğrulandı; metrik gözlemlenemedi |
| LinkedIn | (baseline'dan) | Değişiklik gözlemlenmedi |
| Diğer | WhatsApp Business (wa.me kaydı) | Aktif dizin kaydı; +90 537 349 84 03 |

**Kimlik tutarsızlığı bulgusu güçlenerek geçerli:** soru artık "2 Instagram" değil, "8 vitrinlik plansız dağılım mı, bilinçli dil-pazar mimarisi mi?" Görüşme sorusu olarak not edildi.

---

## 6. İÇERİK GÖZLEMİ — Hasta hikâyesi mevcut durumu (Tip B)

YouTube'da hasta içerikli Shorts tespit edildi (örnek başlıklar): *"We offered our patient from Iraq a new start!"*, *"More courageous and free with Luxmed prosthetic leg"*. Gözlemlenebilen kadarıyla:
- Format: kısa klip / ürün-an odaklı; **bütünlüklü anlatı (hastanın kendi sesiyle hikâye) görünmüyor.**
- Ton notu: acıma dili yok (olumlu) ancak yer yer **klinik-kahraman çerçevesi** ("hastamıza yeni bir başlangıç sunduk") — özne hasta değil kurum. Onur-merkezli üretimde özne hastaya kayar; mevcut malzeme bunun ham hali olarak değerli.
- Bu gözlem, "güven rakamları güçlü / marka anlatısı eksik" bulgusunun (baseline Açık #4-6 hattı) bugünkü teyidi. Masa özetinde "ilk adım" gerekçesine veri olarak girdi — zorlamadan, mevcut durum neyse o.

---

## 7. YENİ RİSK & FIRSAT KAYITLARI

**Fırsatlar:**
- **F1 — Yandex 4.9/25:** RU/BDT hasta yolculuğunun arama katmanında güçlü kanıt hazır; site RU içeriğiyle desteklenirse zincir tamamlanır.
- **F2 — Bookimed hasta-kaynak beyanı:** "BDT, Balkan, Arap Ligi" — uluslararası konumlandırma cümlesi için platform doğrulamalı dayanak.
- **F3 — Fiyat/SGK şeffaflık içeriği:** Şubat-Mart 2026 güncel; AI Overview'a uygun yapı. 403 çözülürse AI görünürlüğünde erken davranma şansı.

**Riskler:**
- **R1 — Sayfa tazeliği tutarsızlığı:** `/protez-kol-fiyatlari` başlığı "✅ 2025 ... Nisan Ayı Teklifi"nde kalmış; kardeş sayfa `/protez-bacak-fiyatlari` "2026 (Mart)". Bayat başlık hem CTR hem güven kaybı. (Hızlı kazanım — başlık güncelleme.)
- **R2 — Bookimed bayatlığı:** 15 aylık fiyat + 5/190 yorum + profilsiz doktor → uluslararası hastanın ilk temas noktasında zayıf izlenim.
- **R3 — Rakip iddia dili:** SERP'te `protezayak.com` "**Garantili** Protez Ayak Tedavisi" başlığıyla çıkıyor. Sağlıkta sonuç garantisi Reklam Kurulu açısından riskli iddia — Luxmed bu dile ÖZENMEMELİ; tersine "uyumlu + kanıtlı güven" konumlandırmasıyla ayrışma fırsatı.
- **R4 (devam):** Baseline R1-R9 açıkları geçerliliğini koruyor; en kritik ikisi hâlâ 403 yapılandırması ve kanal tekleştirme.

---

## 8. SONRAKİ ADIM

1. Bu güncelleme + `luxmed-masa-ozeti.md` → **Denetmen 7 mercek** → Ayhan onayı.
2. Onay sonrası PDF üretimi İçerik Ajanı'na brief'lenir (bu turda PDF üretilmedi — talimat gereği).
3. Görüşmede teyit edilecekler: (a) Bookimed €11.200 paketinin yayın durumu, (b) kanal çoğalması plan mı/organik mi, (c) bot koruması kimin yönetiminde (hosting/ajans?), (d) GSC + Analytics erişimi — sayısal baseline'ın ön koşulu.

---
*Keşif & Denetim Ajanı — tazeleme turu, 13 Haziran 2026. Tüm yeni bulgular kamuya açık kaynaklardan; erişilemeyen alanlar açıkça işaretlendi. Sayısal genel skor §0.1 gereği verilmedi.*
