# Özgür Irmak — Şablon Artığı Sayfa Temizliği (plan)

*Fox · 3 Kasım 2026 · Kaynak: canlı site curl + sitemap'ler + Wix API (kurulu uygulamalar, blog yazarları, mevcut yönlendirmeler), hepsi salt-okuma. Siteye hiçbir şey yazılmadı.*

## Envanter (canlı, hepsi 200)

| URL | Kaynak uygulama | robots | Sitemap | GSC gösterim (6 Eki–2 Kas) |
|---|---|---|---|---|
| /group/traveling-to-india/discussion | Wix Groups | index | group-lists | 6 |
| /group/traveling-in-australia/discussion | Wix Groups | index | group-lists | 2 |
| /groups | Wix Groups (liste sayfası) | — | pages | ölçülmedi |
| /portfolio | Portfolio (dinamik sayfa) | — | pages | 28 |
| /portfolio/landscape-magazine | Portfolio | — | dynamic-portfolio | 8 |
| /portfolio/wild-spirit | Portfolio | — | dynamic-portfolio | ölçülmedi |
| /portfolio/espinas-mezcal-ad | Portfolio | — | dynamic-portfolio | ölçülmedi |
| /members | Wix Members Area | — | pages | 11 |

Ayrıca kurulu ama URL'si görünmeyen şablon uygulaması: **Wix Hotels**.

## Kısıt — Members Area kaldırılamaz

60 blog yazısının sahibi üye hesapları (54 + 6). Members Area uygulaması kaldırılırsa blog yazar bağı bozulur. `/members` sayfası yalnız gizlenir/yönlendirilir, uygulama yerinde kalır.

## Seçenekler

**A — 301 yönlendirme (Fox yapar, geri alınabilir).** Wix Redirect API ile:
- `/group/*` (grup yönlendirme) + `/groups` → `/blog`
- `/portfolio` (grup yönlendirme, alt sayfalar dahil) → `/`
- `/members` → `/`

Silme yok; yönlendirme tek çağrıyla geri alınır. Google 301'i görünce eski URL'leri indeksten düşürür. **Belirsizlik:** Wix dokümanı, hâlâ yayında olan bir sayfa üzerinde yönlendirmenin sayfayı ezip ezmediğini açıkça söylemiyor. Önce tek URL'de deneyip curl ile doğrularım. Çalışmazsa yönlendirmeyi geri alır, B'ye geçeriz. Sitemap'ten düşme garantisi yok.

**B — Kaynağında kaldırma (Ayhan yapar, Editör/Dashboard).**
- Wix Groups ve Wix Hotels uygulamalarını kaldırmak (Dashboard → Uygulamalar). Uygulamanın verisi silinir, bu yüzden **Kademe 3**: eylemi Ayhan yapar.
- Portfolio sayfalarını Editör'den silmek ya da gizlemek.
- `/members` sayfası: Editör → sayfa SEO ayarı → "arama motorlarında gösterme".
- Sayfalar ve sitemap girişleri kaynağından gider.

**C — A + B birlikte (öneri).** A hemen yapılır, Google'daki izi bugün keser. B, Ayhan'ın Editör penceresinde yapılır ve kökü temizler; B bitince A'daki yönlendirmeler zararsız biçimde kalabilir.

## Öneri

C. Bugün A (önce tek URL testi), Editör'e girildiğinde B. B'nin Editör adımları, Özgür Bey'e gidecek Editör yayın sorusuyla aynı pencerede yapılmalı (SEO verisinin geri dönme riski).

## Ek gözlem (karar gerektirmez, bilgi)

Yazar profil sitemap'inde 3 profil indeksli: ozgurirmakprotez, furkan-atc, stepsonclouds. Bu, büyüme turu raporundaki yazar-alanı kararına bağlı; burada dokunulmadı.
