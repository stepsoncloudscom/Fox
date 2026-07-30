# Teslim Zinciri Paketi (TZP) — Ajanlar Arası Devir Sözleşmesi
*Marka Bulutu OS teslim zinciri bağ dokusu. Keşif → Strateji → (Metin Yazarı + İçerik) → Growth → Branding halkaları arasında context'in erimeden taşınmasını garanti eder.*

---

## NEDEN VAR (kanıt)

Ajanlar tek tek güçlü; zincir gevşek. Gerçek vakalarda kaçaklar oldu:
- **Bebionic/Touch Bionics (Özgür Irmak):** Strateji Ajanı iki markayı ayrı sandı — konsolidasyon bilgisi context'te vardı ama devredilmedi. Denetmen yakaladı, ama zincir yakalamalıydı.
- **Exclusive clause (Luxmed↔Nesa):** Rakip/çakışma riski bir halkadan diğerine taşınmadı, ortada patladı, gecikme yarattı.
- **YMYL/compliance uyarıları:** Her medikal halkanın kendi başına yeniden keşfettiği kısıtlar. Taşınsaydı bir kez yazılırdı.

TZP bunu kapatır: her halka bir sonrakine **sabit alanlı bir paket** devreder. `musteri-marka-context` = statik doğruluk (marka ne); TZP = akan devir (zincirde ne oluyor, ne taşınıyor, neye dikkat).

---

## NASIL ÇALIŞIR

- **Tek dosya, biriken defter.** Müşteri başına tek TZP dosyası: `/raporlar/[musteriadi]-teslim-zinciri-paketi.md`.
- Her halka **kendi katmanını EKLER** (üstündekini silmez). Aşağı doğru büyür.
- **ÖN KOŞUL:** Bir ajan işe başlarken önce TZP'nin **kendinden önceki tüm katmanlarını OKUR.** TZP yoksa (ilk halka Keşif) başlatır.
- **ÇIKTI:** Ajan işini bitirince kendi katmanını yazar, sonra çıktısını Denetmen'e/Fox'a verir.
- Fox sentez sırasında TZP'yi okur — atlanmış devir varsa yakalar (orkestrasyon §7 "context eksik aktarıldı" dersinin panzehiri).

---

## KATMAN ŞABLONU (her ajan doldurur)

Her halka aşağıdaki bloğu TZP dosyasının sonuna ekler. Boş alan bırakılmaz — yoksa "yok/uygulanmaz" yazılır (sessiz boşluk = kaçak).

```markdown
## [HALKA ADI] KATMANI — [tarih] · [ajan]
**Devreden:** [bu ajan] → **Devralan:** [sonraki ajan]

### ÜRETİLEN
[Bu halkanın çıktısı, 2-4 satır özet + dosya yolu. Sonraki halka bunu girdi alır.]

### DOĞRULANMIŞ GERÇEKLER (Tip A / kaynaklı)
[Kaynağı olan, kesin bilgiler — rakam, tarih, kurumsal gerçek, konsolidasyon.
Örn: "Touch Bionics 2016'da Össur'a geçti (kaynak: X)." Kaynaksızsa buraya YAZILMAZ.]

### DOĞRULANMAMIŞ İDDİALAR (beyana dayalı)
[Müşteri/dış beyan, henüz teyit yok. Örn: "2.000+ hasta — Enes teyidi bekliyor."
Sonraki halka bunu mesaj mimarisinin merkezine KOYMAZ, teyide kadar hipotez sayar.]

### VARSAYIMLAR
[Bu halkanın çalışırken varsaydığı, doğrulanmamış her şey. Sonraki halka test eder.]

### AÇIK KARARLAR (Ayhan/müşteri bekliyor)
[Kilitlenmemiş, karar bekleyen konular. Örn: renk yönü, segment, DTC-toptan dengesi,
exclusive clause. "Tek dokunuşla biter" formatında — ne soruluyor, seçenekler ne.]

### TAŞINAN UYARILAR (compliance / IP / YMYL / hukuki)
[Zincir boyunca ölmemesi gereken kısıtlar. Bir kez yazılır, aşağı taşınır:
- YMYL/Reklam Kurulu: "en iyi/garantili/%X/kesin sonuç" yasağı (medikal)
- IP/kullanım hakkı: logo/isim/görsel sahiplik, üçüncü taraf telif (Össur/stok)
- Exclusive/çakışma: aynı sektörde rakip müşteri var mı?
- İndirim/kıtlık: lüks konumlandırma sınırı, FTC/TKHK]

### KIRILGANLIKLAR (bu müşterinin riskleri)
[Müşteriye özgü zayıf noktalar. Örn: idari ceza geçmişi, kanal tutarsızlığı (2 IG+2 FB),
tracking açığı, placeholder sızıntısı. Sonraki halka bunları konumlandırma/üretimde ele alır.]

### SONRAKİ HALKAYA NOT
[Devralan ajana özel dikkat çağrısı. "Şuna dikkat et, şunu atlama."]
```

---

## ALAN-BAŞINA KAÇAK KAPATMA (hangi alan hangi hatayı önler)

| Alan | Kapattığı gerçek hata |
|---|---|
| Doğrulanmış Gerçekler | Bebionic/Touch Bionics konsolidasyon kaçağı |
| Doğrulanmamış İddialar | "2.000+ hasta / çok dilli" beyanının kanıt gibi kullanılması |
| Açık Kararlar | Özgür Irmak renk yönü belirsizliğinin teslimde patlaması |
| Taşınan Uyarılar | Her medikal halkanın YMYL kısıtını sıfırdan keşfetmesi |
| Kırılganlıklar | İdari ceza boşluğunun konumlandırmada hiç ele alınmaması |
| Sonraki Halkaya Not | Kanal tutarsızlığının halkalar arası kaybolması |

---

## GÜVENLİK & DİSİPLİN
- TZP **iç belgedir** — müşteriye gitmez. Ham kırılganlık/açık karar içerir. Müşteri çıktısı ayrı (rapor/strateji/brand book).
- Katman **silinmez, eklenir.** Bir önceki halkanın yazdığı yanlışsa → düzeltme notu olarak yeni katmanda belirt, üstünü çizme.
- **Değer filtresi:** TZP'de kişisel/hassas veri minimumda; KVKK/onur gözetilir.
- **Kademe 1:** TZP güncelleme geri alınabilir iç iş — Ayhan onayı beklemez.

---
*TZP v1 · Marka Bulutu OS · 27 Temmuz 2026 · Fox · Orkestrasyon §7 "context eksik aktarıldı" dersinden doğdu*
