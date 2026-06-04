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

## KURULUM SIRASI
1. ✅ Keşif & Denetim Ajanı (zubair tabanlı)
2. ✅ Müşteri Marka Context şablonu (Corey product-marketing tabanlı)
3. **Strateji Ajanı** (Corey product-marketing + pricing + positioning + Dunford) — SIRADAKİ
4. İçerik Ajanı (Corey copywriting/emails/social + parmak izleri)
5. Growth Ajanı
6. Branding Ajanı

Her ajan: uyarla → Denetmen'le test → Darya/Luxmed pilot → sistemleştir.

---

## GÜVENLİK NOTU
Corey reposu en temiz senaryo: markdown skills + JSON manifest + zararsız validate scriptleri. Kod çalıştırma/veri sızdırma yok. `curl|bash` yok. /tmp'de incelendi. Plugin olarak kurulması da değerlendirilebilir (resmi format) — ama önce bizim uyarlamamız.

---
*Sürüm: v2 · 4 Haziran 2026 · Fox · Corey Haines birincil, zubair ikincil.*
