# Müşteri Kapanış Şablonu (Offboarding)
*Kaynak: SidekicksStudio/marketing-agency-in-a-box `client-offboarding` skill'i, 6 Ekim 2026 taraması → süzülüp uyarlandı. Fox'ta önceden eksikti — Teslim Zinciri Paketi ajanlar-arası devri kapsar, bu şablon müşteri ilişkisinin sonunu kapsar.*

---

## NEDEN VAR

Bir müşteri ilişkisi nasıl bittiği, bir sonraki referansı, vaka çalışmasını ve (ayrılık iyi geçtiyse) geri dönüşünü belirler. Temiz kapanış olmayan hiçbir açık uç bırakmaz; dağınık kapanış itibar riskine döner (Anayasa §4 savunma doktrini — bu da bir "hamle dizisi", son hamle dahil).

Her neden bitişte (doğal bitiş, yenilenmeme, erken fesih) aynı sırayla işlenir.

---

## BAŞLAMADAN ÖNCE

1. **Bitiş sebebi** — doğal bitiş / yenilenmeme / erken fesih / kapsam tamamlandı.
2. **Son tarih** — ilişkinin resmen bittiği gün.
3. **Bekleyen teslimler** — sözleşmeden kalan ne var.
4. **Hesap & erişim envanteri** — Fox/Ayhan'ın müşteri adına tuttuğu her şey (aşağıdaki liste).

---

## SIRA — atlanmaz, özellikle ilişki gerginse

### 1. Son Teslimler
- [ ] Sözleşmede yazan her teslim tamam ve iletildi
- [ ] Tüm dönemi kapsayan son performans raporu (sadece son ay değil)
- [ ] Yarım kalan iş ya tamamlandı ya net durum notuyla devredildi
- [ ] Açık değişiklik talepleri yazılı kapatıldı (tamamlandı veya iptal)

İlişki kötü bitiyorsa: sözleşmenin gerektirdiğini eksiksiz teslim et — ne fazla ne eksik. Teslimi yazıyla belgele.

### 2. Erişim Devri — **KADEME 3, Fox yapmaz**

> **Sert sınır:** Erişim/yetki paylaşma ve devri Anayasa §2 Kademe 3'tür — "asla yapma, sadece uyar." Fox bu bölümü **kontrol listesi olarak hazırlar**; devri fiilen Ayhan yapar (hesaplardan çıkma, yetki devretme, şifre değiştirme).

**Devredilecek / iptal edilecek (kontrol listesi, Ayhan uygular):**
- [ ] GA4 / Google Analytics — ajans kullanıcısı kaldırılır, müşterinin admin erişimi teyit edilir
- [ ] Google Ads / Meta Ads — sahiplik devredilir veya ajans erişimi kaldırılır
- [ ] Google Search Console — ajans erişimi kaldırılır
- [ ] Sosyal medya hesapları — tüm ajans ekibi üyelerinin erişimi iptal edilir
- [ ] E-posta/pazarlama platformu (varsa) — ajans kullanıcısı kaldırılır
- [ ] CMS/web sitesi (Wix vb.) — ajans admin hesapları kaldırılır
- [ ] Domain kayıt sağlayıcı — müşterinin tam kontrolü teyit edilir
- [ ] Müşteri adına kurulan 3. parti araçlar

**İade/devredilecek varlıklar:**
- [ ] Marka varlıkları, kaynak dosyalar — müşteriye teslim
- [ ] Reklam kreatifleri — kaynak dosyalar müşteriye
- [ ] İçerik dosyaları — teslim
- [ ] Ajans tarafından oluşturulmuş şifre/erişim bilgileri — müşteriye devredilir, Fox'ta tutulmaz

Her devir yazılı onay/bildirimle belgelenir — sessizce erişim kesilmez.

### 3. Son Belgelendirme
Aşağıdaki şablonla kapanış özeti üretilir (Kademe 2 — Ayhan onayından geçer, müşteriye öyle gider).

### 4. Kapanış Görüşmesi
20-30 dakikalık görüşme talep edilir:

> "Resmi olarak kapatmadan önce, neler yaptığımızı birlikte gözden geçirmek ve son sorularınızı yanıtlamak isteriz. Dürüst geri bildiriminiz bizim için de değerli olur."

Üç işi birden görür: ilişkiyi insani notla kapatır, şikayete dönüşmeden son endişeleri yüzeye çıkarır, referans/gelecek iş kapısını açık tutar.

Görüşme kabul edilmezse: yazılı kısa özet gönderilir.

### 5. Referans & Vaka Çalışması Talebi
İlişki iyi gittiyse **şimdi** sorulur — müşteri ilerledikçe isteksizleşir:

> "Birlikte yaptığımızla gurur duyuyoruz. Kısa bir referans paylaşır mısınız? İsterseniz bunu bir vaka çalışmasına da dönüştürmek isteriz — yayınlamadan önce taslağı sizinle paylaşırız."

Vaka çalışması için → `vaka-calismasi-sablonu.md`.

### 6. Müşteri Dosyasını Kapat
- Müşteri context dosyası son sonuç + derslerle güncellenir
- İlişki "kapandı" + bitiş tarihiyle işaretlenir
- Dosya **arşivlenir, silinmez** — geçmiş müşteri context'i değerlidir (gelecekte geri dönerse, benzer bir müşteri gelirse referans)

---

## KAPANIŞ ÖZETİ BELGESİ (müşteriye gider — Kademe 2)

```markdown
# [Müşteri Adı] — İlişki Özeti
Ajans: Steps On Clouds
Dönem: [BAŞLANGIÇ] – [BİTİŞ]
Hazırlayan: [İsim]
Tarih: [TARİH]

## Ne Hedefledik
[Orijinal teklif/intake'ten 2-3 cümle]

## Ne Teslim Ettik
- [Teslim] — [ne olduğu, amacı]
- ...

## Sonuçlar
| Metrik | Başlangıç | Kapanış | Değişim |
|---|---|---|---|
| | | | |

## Sizde Kalan Sistem
[Arkanızda çalışmaya devam eden içerik/kampanya/altyapı]

## İleriye Dönük Öneriler
[3-5 somut adım — ajansın kapsamı olmasa bile dürüstçe]

## Hesap & Erişim Teyidi
[Tüm erişimlerin [TARİH] itibarıyla devredildiğinin teyidi]

## Teşekkür
[Gerçek, şablon olmayan, ilişkiye özgü bir not]
```

---

## ZOR KAPANIŞLAR

İlişki hedefe ulaşamadan, sürtünmeyle veya erken bittiyse:

- **Kaybolma yok.** En kötü sonuç budur — kötü referansı garantiler.
- **Kapanış görüşmesinde dürüst ol.** "X beklediğimiz gibi gitmedi — ne öğrendik, farklı ne yapardık" sözü müşteri söylemeden önce söylenir.
- **Borçlu olunanı eksiksiz teslim et**, ilişki bozulmuş olsa da.
- **Her şeyi yazıyla belgele** — anlaşmazlık riski varsa.

---

## İLGİLİ DOSYALAR
- `teslim-zinciri-paketi-sablonu.md` — ajanlar-arası devir (bu, müşteri-ajans ilişkisinin sonu)
- `kanit-ucgeni-olcum-sablonu.md` — kapanış raporu T+90 ölçümüyle örtüşüyorsa aynı veri kullanılır
- `vaka-calismasi-sablonu.md` — adım 5'te tetiklenir

---
*v1 · 6 Ekim 2026 · Fox · Kaynak: Corey Haines marketingskills → SidekicksStudio ajans fork'u, Fox Kademe sistemine uyarlandı.*
