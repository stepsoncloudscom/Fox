# gstack Öğrenim Notları
*Kaynak: github.com/garrytan/gstack — 5 Haziran 2026 incelemesi*
*Kategori: Ajan mimarisi + içerik kalitesi + sistem tasarımı*

gstack, tek bir geliştirici tarafından Claude Code üzerine inşa edilmiş, kalıcı tarayıcı + skill sistemi ekleyen bir araç. İnceleme amacımız: bizim sistemimize transfer edilebilecek prensip ve mimari kalıplar. Bunlar doğrudan kopyalanmaz — §1 süzgecinden geçirilerek uyarlandı.

---

## 1. ETİK: Üç Temel İlke (ETHOS.md)

### 1A. Boil the Lake — Eksiksizlik İlkesi
AI, eksiksizliğin marjinal maliyetini neredeyse sıfıra indirdi. "Yaklaşık doğru" ile "tam doğru" arasındaki fark artık saatler değil dakikalar. Bu değişti:

> "Yaklaşık yapayım" = eskiden savunulabilir verimlilik kararı. Bugün = tembellik.

**Lake vs Ocean ayrımı:**
- **Lake (göl):** Tamamlanabilir, kapsamlı bir modül/teslimat. Boil et — her zaman.
- **Ocean (okyanus):** Sistemi baştan yazma, çeyrek-yıllık platform göçü. Flag et — kapsam dışı.

Pratik uygulama (bizim sistemimiz için):
- İçerik Ajanı bir copy seti ürettiğinde: başlık alternatifleri + gerekçe + CTA varyantları = aynı iş. Bir tanesini bırakıp gerisini "isteğe göre" deme — hepsini ver.
- Strateji Ajanı bir konumlandırma ürettiğinde: 3 rakip alternatif, 2 varyant, counterargument = işin parçası.
- Denetmen bir hata bulduğunda: sadece bayrak değil, önerilen düzeltme de ver.

### 1B. Önce Ara, Sonra Yap — 3 Katman Bilgi Kalitesi
Her araştırmada/tavsiyede bilginin hangi katmandan geldiği önemlidir:

| Katman | Ne | Risk |
|--------|-----|------|
| 1 — Proven/Tried | Standart, savaşta test edilmiş yaklaşımlar | Nadir de olsa temel varsayım yanlış olabilir |
| 2 — New/Popular | Güncel blog, trend, sektör görüşü | İnsan manyasına açık; kalabalık yanılabilir |
| 3 — First Principles | Özgün gözlem + o işe özgü çıkarım | Üretilmesi en zor, değeri en yüksek |

**En değerli çıktı:** "Herkesin yaptığını anladım (Katman 1+2) + neden yanlış olduğunu gördüm (Katman 3)" — bu 11/10.

Pratik uygulama:
- Keşif Ajanı rakip analizi yaparken: sektör standardını bul (K1), trend oku (K2), müşterinin özgün bağlamını buna uygula (K3).
- Strateji Ajanı konumlandırma üretirken: Dunford'ın çerçevesi (K1), sektörün yaptığı (K2), bu markanın başkasının terk ettiği alanda ne görebileceği (K3).
- İçerik Ajanı copy üretirken: kanıtlanmış yapı (K1), benzer markanın tonu (K2), bu müşterinin verbatim müşteri sesinden çıkan özgün çerçeveleme (K3).

### 1C. Kullanıcı Egemenliği — Üret-Doğrulat Döngüsü
İki AI aynı şeyi söylüyor diye doğru değildir.

> "İki model aynı fikirdeyse bu güçlü bir sinyal. Emir değil."

Kullanıcı (Ayhan) her zaman modelin göremeyeceği bağlam taşır: alan bilgisi, ilişki, zamanlama, paylaşılmamış gelecek planlar. Modelin ikna edici argümanı bile Ayhan'ın "hayır"ını geçersiz kılmaz.

**Üret-Doğrulat döngüsü:** AI üretir → kullanıcı doğrular ve karar verir → AI doğrulama adımını asla atlamaz.

Bu Fox CLAUDE.md §3 ile zaten örtüşüyor. gstack bunu bir etik ilke olarak net formüle ediyor.

---

## 2. MİMARİ: Skill Sistemi (SKILL.md)

### 2A. Skeleton + On-Demand Sections
gstack v1.56'da büyük bir token optimizasyonu yaptı: ağır skill'lerin her zaman yüklenen kısmı (~%40 daha küçük skeleton) + sadece gerektiğinde okunan `sections/` dosyaları.

Bizim için çeviri:
- Ajan tanımları büyüdükçe aynı sorun çıkacak. Çözüm: Her ajanın "her zaman yüklenen çekirdek" + "işe başlayınca okunan bölümler" olarak yapılandırılması.
- Örnek: Keşif Ajanı'nın Puanlama Rubriği referansı şu an "oku" diyor ama ağır. Çözüm: "Faz 2'ye geçince rubriği oku" şeklinde on-demand.

### 2B. LEARNINGS Sistemi (JSONL)
gstack her proje için `~/.gstack/projects/<slug>/learnings.jsonl` tutuyor. Her oturumda bu öğrenmeler yükleniyor, yeni öğrenmeler ekleniyor. "Bu hatayı daha önce yapmıştık" sinyali.

Bizim sistemde: `fox-gelisim-mufredati.md` Aktif Rotasyon Kuyruğu aynı amacı taşıyor ama yapılandırılmamış. Kuyruğa JSONL formatı eklemek veya hata → çözüm → tarih kaydını otomatikleştirmek bant genişliği açtıkça değerlendirilebilir.

### 2C. Slop Scan Altyapısı
gstack'in `slop-scan.config.json` + `bun run slop` komutu var. Çıktılarda AI-slop kelimelerini sistematik tarıyor.

Bizim için çeviri: Görsel Üretim Standardı §11.E'deki kara liste zaten var ama sadece "bildir" diyor, "tara" demiyor. Bir `slop-check.sh` script'i ileride değerlendirilebilir.

---

## 3. DOKÜMANTASYON: Diataxis Çerçevesi

### 4 Quadrant
```
                    TEORİK                      PRATİK
                    (anlama)                    (yapma)

  ÖĞRENME          Açıklama                     Tutorial
  (çalışma)        "X neden var?"               "X'i ilk kez bana göster"
                   → tartışır                   → öğretir

  KULLANIM         Referans                     How-to
  (çalışırken)     "Y'nin tam imzası nedir?"    "X kullanarak Y'yi nasıl yaparım?"
                   → tanımlar                   → uygular
```

Her içerik türü belirli bir okuyucu amacına hizmet eder. Aynı içerik 4'üne birden hizmet edemez.

**Bizim içerik sistemimize uyarlaması:** → bkz. İçerik Ajanı §Diataxis Bölümü (bu dosyadan uyarlandı).

---

## 4. TASARIM: Referans Değerler (DESIGN.md)

gstack'in kendi sitesi için oluşturduğu tasarım sistemi. Doğrudan kullanmıyoruz (farklı estetik) ama ilkeler değerli:

**"Grain texture for materiality":** Düz yüzeylere SVG feTurbulence ile çok düşük opacity (%2-3) noise overlay → "generic SaaS template" hissini kırar. Steps On Clouds'un editorial ruhuna uyan bir detay.

**"Monospace as personality font":** JetBrains Mono, gstack'te sadece kod için değil veri/tablo gösteriminde de kullanılıyor — kişilik katıyor. Bizde pdf-motorunda Bebas/Comfortaa bu rolü oynuyor; benzer mantık.

**"Restrained accent":** Amber vurgu rengi nadir ve anlamlı yerlerde. Krom nötr kalır. Biz de zaten bu prensipte çalışıyoruz — phthalo yeşil vurgu, nötr zemin.

**Motion ilkesi — "Only transitions that aid comprehension":** Anlamaya yardımcı olmayan hareket yok. Bizim PDF ve dijital içerik standartlarımıza girer.

---

## 5. KARAR: Ne Uyarlandı, Ne Uyarlanmadı

| gstack konsepti | Uyarlama kararı | Nereye |
|----------------|-----------------|--------|
| Boil the Lake | ✅ Uyarlandı | İçerik Ajanı + Denetmen |
| 3 Katman bilgi kalitesi | ✅ Uyarlandı | Keşif + Strateji + İçerik + Denetmen Ajanları |
| Kullanıcı Egemenliği | ✅ Zaten var, güçlendirildi | CLAUDE.md §3 ile örtüşüyor |
| Diataxis (4 quadrant) | ✅ Uyarlandı | İçerik Ajanı |
| Skeleton + sections | 🟡 İleride — Değerlendirme: öncelik düşük | Ajan tanımları büyüyünce; şu an yeterli küçüklükte |
| LEARNINGS JSONL | 🟡 İleride — fox-gelisim-mufredati.md Aktif Kuyruk aynı amacı görüyor | Otomasyona geçilince |
| Slop scan script | 🟡 İleride — §11.E kara liste + render-and-review şimdilik yeterli | Görsel Üretim Standardı'na eklenebilir |
| Grain texture | 🟡 Değerlendirilebilir — pdf-motoru v4'te dene | Branding Ajanı / pdf-motoru v4 |
| gstack browser/QA altyapısı | ❌ Uygulanamaz | Yazılım değil, marka ajansı |

---

*Bu dosya bir özettir. Birincil kaynaklar: gstack ETHOS.md, DESIGN.md, ARCHITECTURE.md, docs/explanation-diataxis-in-gstack.md — inceleme tarihi 5 Haz 2026. Uyarlama durumu güncellendi: 6 Haz 2026.*
