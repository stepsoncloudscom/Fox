# Web Sitesi Şeması — Özgür Irmak Protez ve Ortez (Wix)
*İş kalemi B1. Tek-site mimarisi · 4 dil (TR/EN/AR/RU) · Wix Multilingual + AR RTL · Fox · 3 Tem 2026*

> **Mimari kararı:** Tek master-brand sitesi. **ozgurprotez.com + biyonikprotezler.com birleşir** → biyonik/myoelektrik protezler ayrı marka değil, **Çözümler altında öne çıkan bir bölüm/ürün hattı**. Eski domain 301 ile yeni siteye yönlendirilir (SEO devri korunur).

---

## 1. SİTE HARİTASI (sayfa ağacı)

- **Ana Sayfa**
  - **Hakkımızda** — kurucu/usta hikâyesi (Özgür Irmak, 1999, 20+ yıl), felsefe ("en iyi protez kişiye özel"), ekip, teknoloji vizyonu
  - **Çözümler** *(açılır menü)*
    - Bacak Protezleri (diz üstü mikroişlemcili · diz altı · aktif vakum)
    - Kol Protezleri
    - **Biyonik / Myoelektrik Protezler** ← eski biyonikprotezler.com burada erir
    - Silikon Protezler (parmak / kozmetik)
    - Ortezler (DAFO vb.)
  - **Teknoloji & Çözüm Ortakları** — Ottobock, Össur, Freedom, Bebionic, Touch Bionics, Ortotek (güven + premium)
  - **Özgürlük Hikâyeleri** ⚖️ — hasta hikâyeleri + kampanya filmi (onur-merkezli; izinli; testimonial hukuk gate)
  - **Uluslararası Hastalar** ★ — yurtdışı hasta funnel'ı (döviz); EN/AR/RU öne çıkar
  - **İletişim / Randevu** — form + WhatsApp + konum/harita
  - *(footer)* **Yasal** — KVKK · Gizlilik · Çerez Politikası · Kullanım Şartları

**Ana menü:** Ana Sayfa · Hakkımızda · Çözümler ▾ · Teknoloji · Özgürlük Hikâyeleri · Uluslararası Hastalar · İletişim · **[dil: TR/EN/AR/RU]**

## 2. SAYFA BAZINDA BÖLÜMLER (wireframe brief)

**Ana Sayfa**
1. Hero — "yenilenmiş öncü" mesajı + kampanya filmi/teaser + tek net CTA (randevu/danışma)
2. Güven şeridi — 1999'dan beri · çözüm ortağı logoları · rakam/kanıt (⚖️ ölçülü, doğrulanmış)
3. Çözümler özeti (kartlar → kategori sayfaları)
4. Neden Özgür Irmak — ustalık + teknoloji + kişiye özel (seçicilik DEĞİL)
5. Özgürlük Hikâyeleri kısa vitrin (1-2 hikâye + filme yönlendir)
6. Uluslararası hasta şeridi (EN/AR/RU görünür) → International sayfası
7. İletişim/randevu bandı

**Hakkımızda** — usta hikâyesi (Özgür Irmak) · felsefe · ekip/uzmanlık · teknoloji vizyonu · onur çerçevesi

**Çözüm (her kategori sayfası, ortak şablon)** — tanım · kimler için · kullanılan teknoloji/marka · süreç adımları · ilgili SSS · CTA. ⚖️ "kesin iyileşme/en iyi" iddiası YOK; kanıta dayalı, ölçülü.

**Uluslararası Hastalar** ★ (döviz funnel'ın kalbi)
1. Neden İstanbul / Özgür Irmak (uzmanlık + teknoloji + değer)
2. Süreç adımları (ilk temas → değerlendirme → üretim/uygulama → takip)
3. Dil/iletişim kolaylığı (AR/RU/EN destek)
4. Danışma talebi formu (uluslararası — WhatsApp/e-posta)

**Özgürlük Hikâyeleri** ⚖️ — film + hikâye kartları; her biri izinli, hukuk onaylı; onur-merkezli (özne, kurban değil)

**İletişim** — form (kısa, düşük sürtünme) · WhatsApp · telefon · adres + harita · çalışma saatleri

## 3. ÇOK DİLLİLİK (Wix Multilingual)
- **Ana dil:** TR · **Çeviriler:** EN · AR · RU
- **AR = RTL** — Wix Multilingual RTL düzeni destekler; tipografi Arap glyph'i taşımalı (marka fontuyla uyum — bkz. kimlik A9)
- Dil değiştirici header'da; her dilde SEO slug'ı ayrı
- ⚠️ Çeviri = lokalizasyon (birebir değil); medikal terimler + kültürel ton dile göre kalibre

## 4. SEO / AI-SEO
- Her sayfa: hedef arama niyeti (TR yerel + EN/AR/RU yurtdışı hasta)
- Teknik temel: meta, başlık hiyerarşisi, hız, mobil, sitemap.xml, schema.org (MedicalOrganization/MedicalClinic)
- Eski domain **301 → yeni** (biyonikprotezler otoritesi korunur)
- AI-SEO: SSS + eğitici içerik (AI Overview/asistan görünürlüğü)

## 5. ⚖️ HUKUK GATE / UYUM (medikal)
- Sağlık Bakanlığı sağlık reklamı mevzuatı: abartılı iddia / "en iyi" / garantili sonuç / izinsiz öncesi-sonrası ve testimonial **YOK**
- Tüm içerik (özellikle Çözümler + Özgürlük Hikâyeleri) **avukat onayından** geçer → yayın
- Yasal sayfalar zorunlu (KVKK/aydınlatma, çerez, gizlilik)

## 6. ♿ ERİŞİLEBİLİRLİK (bu kitlede zorunlu — onur meselesi)
- WCAG uyumu: kontrast, klavye navigasyonu, ekran okuyucu (alt-text, ARIA), okunur tipografi
- Form etiketleri + hata mesajları erişilebilir
- Bu marka *erişilebilirlik* satıyor — sitesi de erişilebilir olmalı (tutarlılık = güven)

## 7. RANDEVU / DÖNÜŞÜM
- Birincil CTA: danışma/randevu talebi (kısa form) + WhatsApp
- Uluslararası: e-posta/WhatsApp + dil desteği vurgusu
- (Opsiyon) Wix Bookings — süreç netleşince

## 8. UYGULAMA DURUMU (3 Tem 2026)
- **Taslak site kuruldu** — Wix Harmony AI, Steps on Clouds hesabı altında (ajans-build), 7 sayfalık yapı, şema brief'inden.
- **siteId:** `f1afaa27-4baf-40f9-b9ac-4cd220b7c151`
- **Önizleme:** https://stepsonclouds.wixsite.com/my-site-2
- **Editör:** https://editor.wix.com/edit/od/c521f8bd-c45e-4c05-b5dd-8f0193a5a1ce?metaSiteId=f1afaa27-4baf-40f9-b9ac-4cd220b7c151
- **Görsel kararı (Ayhan 3 Tem):** AI **placeholder/referans görseller ŞİMDİLİK KALIYOR**; gerçek görsel (SOC arşivi + D1 çekimi) kimlik onayından (CP1) sonra. SOC medya taraması yapıldı: AI görselleri (ChatGPT Image) + TagKloi/moda client işleri elendi; protez/ampüte seti Wix kütüphanesinde net değil (muhtemelen Drive `Profile.pdf`/Össur).
- ⚠️ **Otomatik yayınlandı** (wixsite.com subdomain — görünmez/indekssiz). Hukuk gate: gerçek yayın/domain öncesi avukat onayı; şimdilik paylaşılmaz/indekslenmez.
- **Sonraki (kimlik CP1 sonrası):** şemaya hizalama — Uluslararası Hastalar sayfası, biyonik birleşme, 4 dil (Wix Multilingual + AR RTL), yasal sayfalar, erişilebilirlik, marka kimliği kaplaması + gerçek görsel.

---
*Sıradaki: kimlik onayı (CP1) sonrası Wix'te tasarım/geliştirme (B4-B5). Görsel harita: ayrı.*
