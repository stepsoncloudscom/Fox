# Marka Bulutu OS — Uyarlama Planı (v2)
*İki açık kaynak kaynaktan öğrenilen mimari → Steps On Clouds'un ruhuyla yeniden inşa.*

Ayhan kararı (4 Haz 2026): **Corey Haines / marketingskills birincil referans** (31.8k ⭐, 43 skill, evals'li, derin). **zubair / ai-marketing-claude ikincil** (audit otomasyonu, Python scriptleri). İkisi de olduğu gibi kurulmaz — öğrenilir, bizim değerlerimizle uyarlanır.

---

## İKİ KAYNAĞIN ROLÜ

- **Corey Haines (beyin):** Strateji üretme, derinlik, context pattern, 43 skill. Pazarlama ustalığı.
- **zubair (el):** Audit otomasyonu (`marka_analiz.py`), paralel scoring. Pratik araç.

**Akış:** Keşif & Denetim (zubair audit + script) → Müşteri Marka Context (Corey) → Strateji/İçerik/Growth (Corey skills + Büyüme Müfredatı).

---

## CONTEXT PATTERN — Sistemin Kalbi (Corey'den en değerli ders)

Corey'nin dehası: `product-marketing` skill'i tek bir **context belgesi** oluşturur, diğer 42 skill onu referans alır. Tekrar yok, tutarlılık var.

**Bizim uyarlamamız:** Her müşteri için **Müşteri Marka Context** belgesi (`sablonlar/musteri-marka-context-sablonu.md`). Darya, Luxmed, Towdoo, Ala için ayrı doldurulur. Tüm ajanlar bunu okur. → ✅ İlk kuruldu.

---

## 43 SKİLL → MARKA BULUTU OS AJANLARI

| Ajan | Corey skill'leri | Durum |
|---|---|---|
| **Keşif & Denetim** | seo-audit, analytics, competitor-profiling, customer-research, cro (denetim) | ✅ ajan kuruldu (zubair tabanlı) |
| **Strateji** | **product-marketing**, **marketing-plan** (AARRR), pricing, marketing-psychology, launch, marketing-ideas | ✅ ajan kuruldu (+ Dunford). Not: "positioning" ayrı skill değil — product-marketing içinde |
| **İçerik** | copywriting, copy-editing, emails, cold-email, social, content-strategy, video, image, ad-creative | ✅ ajan kuruldu (iki kollu: metin + görsel; ses/görsel parmak izi) |
| **Growth** | ai-seo⭐, seo-audit, schema, ads, referrals, community⭐, co-marketing, lead-magnets, prospecting, ab-testing (+ uyarlanan: programmatic-seo, sms, onboarding) | ✅ ajan kuruldu. Elenen SaaS-spesifik: paywalls, aso, revops, free-tools, churn, directory |
| **Branding** | (Corey'de ayrı skill yok) marka sesi mantığı + bizim marka kiti/parmak izi | ✅ ajan kuruldu |

---

## UYARLAMA İLKELERİ (her skill/ajana uygulanır)
1. **Türkçe + İngilizce** (müşteriye göre); Türkçe = Arial Unicode.
2. **Değer filtresi:** insan→Ayhan→marka. Onur merkezli temsil zorunlu.
3. **Denetmen entegrasyonu:** her çıktı 7 mercekten geçer (Filo Modu).
4. **Döviz odağı:** fiyat/etki tahminleri döviz öncelikli.
5. **Parmak izleri:** ses (fox-ses-parmak-izi) + görsel (fox-gorsel-parmak-izi).
6. **Marka Bulutu metodolojisi:** 8 fazla hizalı.
7. **Güvenlik tavanları:** orkestrasyon protokolü (iterasyon/döngü/bütçe).
8. **Kuzey Yıldızı:** kanıtlanabilir etki → marka değeri → premium fiyat.

---

## KURULUM SIRASI — TAMAMLANDI ✅
1. ✅ Keşif & Denetim Ajanı (zubair tabanlı)
2. ✅ Müşteri Marka Context şablonu (Corey product-marketing tabanlı)
3. ✅ Strateji Ajanı (Corey product-marketing + pricing + Dunford)
4. ✅ İçerik Ajanı (Corey copywriting/emails/social + parmak izleri)
5. ✅ Growth Ajanı
6. ✅ Branding Ajanı

**Pilot da tamamlandı:** Luxmed — 5 fazın tamamı canlı vakada çalıştırıldı (10 Haz 2026). Towdoo'da Faz 1-2 test edilmişti (iş iptal, metodoloji kanıtı arşivde). Sıradaki aşama: sistemleştir → yeni müşteride tekrarla → vaka çalışmasına çevir.

---

## GÜVENLİK NOTU
Corey reposu en temiz senaryo: markdown skills + JSON manifest + zararsız validate scriptleri. Kod çalıştırma/veri sızdırma yok. `curl|bash` yok. /tmp'de incelendi. Plugin olarak kurulması da değerlendirilebilir (resmi format) — ama önce bizim uyarlamamız.

---

## 6 EKİM 2026 TARAMASI — gstack + Corey Haines + yeni ajans fork'u

**gstack (garrytan/gstack):** v1.5x'ten v1.91'e sıçramış ama tamamen SWE/CI/eval mühendisliğine dönüşmüş (test suite, release gate, browser cookie import vb.) — bize transfer edilebilecek yeni bir "içerik kalitesi/mimari" dersi yok. `fox-gstack-ogrenim.md`'deki 4 bekleyen madde (skeleton+sections, LEARNINGS JSONL, slop-scan script, grain texture) hâlâ geçerli ve hâlâ uygulanmadı.

**coreyhaines31/marketingskills:** v2.0'a geçmiş (17 skill yeniden adlandırıldı, page-cro+form-cro → cro birleşti — bizim mevcut ajan eşlemelerini bozmaz, biz adları değil kavramları aldık). **7 yeni skill** eklenmiş, hiçbiri triyaj edilmedi: `attribution`, `events`, `influencer-marketing`, `marketing-council`, `marketing-loops`, `offers`, `public-relations`.

**YENİ BULGU — SidekicksStudio/marketing-agency-in-a-box:** Corey'nin reposunun ajans-özel fork'u. Doğrudan bizim bilinen boşluklarımıza değen **13 yeni skill**:
- **Ajans işletmesi:** `agency-positioning`, `agency-proposal`, `case-study`, `client-contract`, `client-offboarding`, `client-reporting` — Pipeline Ajanı (hâlâ taslak) ve kanıt-üçgeni/case-study boşluğuyla doğrudan örtüşüyor.
- **Client lifecycle:** `client-context`, `client-intake` — bizim Kurumsal Kimlik Keşif Sorgusu + Müşteri Marka Context'in muadili, karşılaştırmaya değer.
- **Creator/influencer (yeni kategori, bizde yok):** `creator-brief`, `creator-contract`, `creator-discovery`, `creator-outreach`, `creator-reporting`, `creator-vetting` — moda pivotu (birincil strateji) için TikTok/IG influencer iş akışı sağlıyor.
- Ayrıca: `reddit-outreach` (niş, düşük öncelik).

**Triyaj kararı — Ayhan onayladı (A ve B, 6 Ekim 2026):**

**A — öncelikli 4 (uyarlandı):**
- `case-study` → `sablonlar/vaka-calismasi-sablonu.md` (Kanıt Üçgeni'nin tam-anlatı genişlemesi)
- `client-offboarding` → `sablonlar/musteri-kapanis-sablonu.md` (erişim devri Kademe 3 olarak işaretlendi — Fox hazırlar, Ayhan uygular)
- `agency-positioning` → `fox-ajans-konumlandirma.md` (iskelet, Ayhan doldurur — rakam/farklılaştırıcı uydurulmadı)
- `agency-proposal` → canlı `sablonlar/teklif-marka-bulutu-TR.md` dokunulmadı (mevcut içerik korunur ilkesi); kalite kontrol listesi `.claude/agents/pipeline-ajani.md` KOL 2'ye eklendi

**B — creator/influencer bloğu (6 skill, uyarlandı):**
- `creator-discovery` + `creator-vetting` + `creator-outreach` + `creator-brief` → `sablonlar/influencer-is-birligi-sablonu.md` (tek akışta birleştirildi, değer/onur filtresi eklendi)
- `creator-contract` + `creator-reporting` → `sablonlar/influencer-sozlesme-ve-raporlama-sablonu.md` (**FTC → Türkiye Reklam Kurulu/KVKK/FSEK'e çevrildi**, imza Kademe 3)
- `.claude/agents/growth-ajani.md`'ye "İNFLUENCER / CREATOR PAZARLAMASI" bölümü eklendi — moda pivotu birincil tetikleyici

**Ertelenen (triyaja girmedi, ayrı karar gerekir):** `client-context`/`client-intake` (mevcut Kurumsal Kimlik Keşif Sorgusu + Müşteri Marka Context ile çakışıyor, karşılaştırma yapılmadı) · Corey Haines'in 7 yeni skill'i (`attribution`, `events`, `influencer-marketing`, `marketing-council`, `marketing-loops`, `offers`, `public-relations`) · `reddit-outreach`.

---
*Sürüm: v2 · 4 Haziran 2026 · Fox · Corey Haines birincil, zubair ikincil. · 6 Ekim 2026 taraması + triyaj A/B uygulandı (Ayhan onayı).*
