# Soğuk İletişim Protokolü — Nakit Motoru'nun Dağıtım Sistemi
*v1 · 12 Haziran 2026 · Fox · Bağlam: 30 günlük runway, Çekim Günü kapı ürünü. Bu protokol her soğuk temasta uygulanır — istisna yok.*

---

## 0 · İlke
Soğuk iletişim toplu mail patlatma DEĞİLDİR. Az sayıda, doğrulanmış, gerçekten incelenmiş hedefe, insan eliyle gönderilen kişisel mesajdır. Günde 5-8 nitelikli temas > haftada 100 spam. Sistemin işi hacim değil, **isabet**.

## 1 · Huni Mimarisi

```
HAVUZ (araştırma) → DOĞRULAMA (kanal+kişi) → GÖZLEM (site+IG, 2 gerçek not)
→ TASLAK (şablon+gözlem) → AYHAN ONAY/GÖNDERİM (Kademe 2)
→ TAKİP KADANSI (G+4, G+10) → YANIT → GÖRÜŞME → Notion pipeline'a terfi
```

- **Havuz dosyası:** `raporlar/nakit-motoru-hedef-havuzu.md` — Fox'un çalışma alanı.
- **Notion Müşteri Panosu:** YALNIZCA yanıt verip görüşmeye dönenler terfi eder. Pano pipeline'dır, çöplük değil.

## 2 · Veri Modeli (havuz tablosu kolonları)
`Hedef · Şerit (A/B/C) · Segment · Site/IG · Kanal (doğrulanmış) · Kişi/Rol · Gözlem-1 · Gözlem-2 · Kanıt açısı (hangi portföy parçası) · Durum · Son temas · Sonraki adım`

**Durum değerleri:** HAVUZ → DOĞRULANDI → TASLAK → GÖNDERİLDİ → TAKİP-1 → TAKİP-2 → YANIT / GÖRÜŞME / ARŞİV(sebep)

## 3 · Kanal Doğrulama Kuralı (Mayıs bounce dersi — LCW vakası: 3 tahmin adres, 3 bounce)
1. **Adres TAHMİN EDİLMEZ.** Yalnızca: (a) sitede yayınlanan e-posta, (b) LinkedIn'de teyitli kişi+rol, (c) IG profilinde yazan adres.
2. Doğrulanmış e-posta yoksa kanal önceliği: **iletişim formu → IG DM → LinkedIn DM.**
3. Bounce gelirse aynı domain'e ikinci tahmin YASAK — kanal değiştir (§10 bounce kuralı).
4. Genel müdür/kurucu > pazarlama sorumlusu > info@ (info@ son çare, formdan iyidir o kadar).

## 4 · Kişiselleştirme Standardı (sahte kesinlik yasağı — Rubrik §0.1)
- Her hedefin sitesi + Instagram'ı GERÇEKTEN incelenir; 2 gözlem yazılır:
  - **Gözlem-1 (güç):** işin gerçekten iyi olan yanı — pohpohlama değil, spesifik.
  - **Gözlem-2 (boşluk):** GÖRÜLEBİLİR içerik boşluğu. ✅ "Son 3 ayda video içerik paylaşılmamış", "ürün fotoğrafları telefon çekimi görünümünde" · ❌ "dönüşümünüz düşük", "satışlarınız artmaz" (ölçülmemiş iddia YASAK).
- Gözlemsiz taslak gönderime ÇIKMAZ. Gözlem üretilemiyorsa hedef havuzda bekler.

## 5 · Mesaj Standardı
- Şablonlar: `raporlar/nakit-motoru-satis-kiti.md` §3 (A sıcak / B ajans / C marka-klinik).
- Mailde fiyat YOK — hedef görüşme. Portföy LİNK olarak (Drive), ek dosya yalnız istenirse.
- Konu satırı varyantları test edilir (haftalık skorla): V1 "[Marka] için İçerik Üretimi — Çekim Günü Önerisi" · V2 "[Marka]'nın görsellerine baktım — kısa bir önerim var". Kazanan kalır.
- Ses: Ayhan ses parmak izi. Kimlik kanıtı ilk paragrafta: Hummel/Defacto + Össur.

## 6 · Gönderim Ritmi & Hijyen
- **Günlük 5-8 temas, daha fazlası değil** (hesap sağlığı + kalite tabanı). Pencere: Salı-Perşembe 09:00-11:00 öncelikli; Pzt yoğunluk, Cum ölü.
- Gönderim Ayhan'da (Kademe 2): Fox taslakları Gmail Taslaklar'a koyar, Ayhan tek dokunuşla yollar.
- **Gmail etiketleri:** gönderilen → 🔵 Fırsat (Label_2) + 🟡 Takip Bekliyor (Label_3). Yanıt → Label_3 kalkar; görüşmeye dönerse Notion'a terfi.

## 7 · Takip Kadansı (3 dokunuş, fazlası yok)
- **G+0:** ilk mesaj.
- **G+4:** nazik takip — YENİ DEĞER ekleyerek (ör. ilgili tek iş örneği: "kliniğinize benzer bir iş: [link]"). "Maili gördünüz mü?" YASAK.
- **G+10:** son dokunuş — kapıyı açık bırak: "Gündeminizde değilse sorun değil; ihtiyaç doğduğunda buradayım." + arşiv.
- Yanıt gelirse kadans durur, insan modu başlar (Ayhan).

## 8 · Günlük Döngü (Fox nöbeti)
- **Sabah koşusu:** havuza 5-10 yeni hedef (doğrulama+gözlem) · günün taslakları Gmail'e · Ayhan'a tek mesajla "bugünün paketi: N taslak hazır".
- **Akşam koşusu:** inbox taraması (yanıt/bounce) · etiket güncelleme · havuz durumları · yarının takip listesi.
- **Cuma:** haftalık skor → `hedef-havuzu.md` altına: temas / yanıt / görüşme / satış + varyant karşılaştırma + öğrenimler.
- Not: Bu döngü şimdilik manuel ritim (oturum içinde). 1 hafta kalibrasyon sonrası scheduled task'a bağlanabilir — Ayhan kararı.

## 9 · Hukuki Çerçeve — Dikkat Bayrağı (ETK/İYS)
6563 sayılı ETK kapsamında ticari elektronik ileti kuralları tacirlere yapılan B2B iletişimde de İYS tartışması doğurabilir. Risk düşürücü pratiğimiz: (a) toplu/otomatik gönderim YOK — tekil, kişisel, insan-eliyle; (b) ilk tercih sitede kamuya açık kurumsal adresler + iletişim formları + sosyal medya DM (platform içi mesaj ETK kapsamı dışında daha güvenli alan); (c) her mailde gerçek kimlik+iletişim açık; (d) "istemiyorum" diyen anında arşiv + bir daha asla. Bu Dur değil Dikkat bayrağıdır — mevcut pratik makul risk bandında, ama Ayhan bilsin.

## 10 · Yasaklar (değişmez)
- Towdoo'ya satış teması (Ayhan kararı) · Uludağ'a satış (aktif müzakere) · protez/ortez sektörü (Luxmed çatışması).
- Adres tahmini · ölçülmemiş iddia · mailde fiyat · 3'ten fazla dokunuş · günde 8'den fazla soğuk temas.
- Rakam/taahhüt: yalnız onaylı ürün kartından (satış kiti §1).

---
*Bağlı dosyalar: `raporlar/nakit-motoru-satis-kiti.md` (ürün+şablon) · `raporlar/nakit-motoru-hedef-havuzu.md` (canlı havuz) · Notion Müşteri Panosu (terfi edenler).*
