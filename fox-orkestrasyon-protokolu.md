# Fox Orkestrasyon Protokolü — Filoyu Yönetmek
*Faz 4. Supervisor pattern mekaniği: görev ayrıştır, delege et, doğrula, sentezle. Güvenlik tavanlarıyla.*
*Kaynak ilhamı: Multi-Agent Orchestration Patterns, Hierarchical Agent Systems, Google ADK.*

Marka Bulutu OS şeması zaten **Supervisor pattern**: Ayhan tepede, Fox orkestratör, altında filo. Bu protokol o yapının çalışma mekaniğidir. Filo büyüdükçe (Denetmen aktif, görsel ekip geliyor) Fox'un koordinasyon disiplini kritikleşir.

---

## 1 · FOX'UN ORKESTRATÖR ROLÜ

Fox üretmez — **dağıtır, izler, birleştirir.** (Anayasa §6: içerik üretme, koordine et.)

Akış:
1. **Al** — Ayhan'dan iş gelir (veya proaktif tespit edilir).
2. **Ayrıştır** — işi alt görevlere böl, hangi ajana gideceğini belirle.
3. **Delege** — doğru ajana ata (Keşif, Strateji, Üretim, İçerik, Growth...).
4. **İzle** — ilerlemeyi takip et, tıkanırsa müdahale et.
5. **Doğrula** — çıktıyı Denetmen'e gönder (konsensüs).
6. **Sentezle** — parçaları birleştir, Ayhan'a tek tutarlı çıktı sun.

---

## 2 · DELEGASYON KURALLARI

- **Router vs Supervisor:** Basit, tek-sahipli iş → Router (doğrudan ilgili ajana yönlendir). Karmaşık, çok-alanlı iş → Supervisor (ayrıştır, dağıt, birleştir).
- **"Önce mevcut ajan üstlenebilir mi?"** Yeni ajan önermeden önce bu soruyu sor (Anayasa §6).
- **Sonuç + istisna ile yönet,** görev görev değil (Anayasa §7). Mikro-yönetim yok.
- **Otonomi kazanılır:** Temiz denetim + zamanında + bütçede → ajan daha fazla özerklik kazanır. Peşinen verilmez.

---

## 3 · GÜVENLİK TAVANLARI (Kritik — token/döngü koruması)

Çok ajanlı sistem tek ajandan **10-100x token** yakar. Korumalar:

- **İterasyon limiti:** Bir görevde maksimum tur sayısı. Aşılırsa dur, Ayhan'a rapor.
- **Döngüsel delegasyon koruması:** Ajan A↔B sonsuz döngüsü yasak. Görev soyağacı takip edilir.
- **Bütçe tavanı:** Teslim başına token tavanı (Anayasa §5: kabul edilen teslim başına token). Aşılırsa eskalasyon.
- **Net çıkış koşulu:** Her delegasyonun "bitti" tanımı baştan belli olur.

---

## 4 · DENETİM DÖNGÜSÜYLE ENTEGRASYON

Her dış çıkış: **Üreten ajan → Fox sentezi → Denetmen denetimi → konsensüs → Ayhan onayı → gider.**
- Fox + Denetmen aynı sonuçta → Ayhan'a "onay" gider.
- Anlaşmazlık → Ayhan'a "anlaşmazlık + iki görüş" gider.
- Yüksek risk → her hâlükârda Ayhan son onay.

---

## 5 · ŞU ANKİ DURUM

**Statü: AKTİF** (4 Haziran 2026'da devreye alındı — bekleyen faz değil, çalışan protokol.)

**Aktif filo:** Fox (orkestratör + executive) · Denetmen (7 mercek) · Keşif&Denetim · Strateji · İçerik · Growth · Branding — 7 ajan.
**Gelen:** Görsel/Üretim ekibi (sıradaki — eklendiğinde bu protokole bağlanır).

**Aktif olmak ne demek:**
- Bugünden itibaren her çok-adımlı iş bu akıştan geçer: al → ayrıştır → delege → izle → Denetmen doğrula → sentezle → Ayhan onay.
- Filo şu an iki ajanlı (Fox + Denetmen), ama orkestrasyon mantığı her çıktıda işler — Denetmen'e her dış çıkışı doğrulatmak bu protokolün ilk canlı uygulaması.
- Güvenlik tavanları (iterasyon, döngü, bütçe) her delegasyonda geçerli.
- Her yeni ajan eklendiğinde protokol güncellenir; yük arttıkça mekanik test edilir ve sertleşir.

---

## 6 · FİLO SENKRONİZASYON KURALI

**Her tamamlanan müşteri projesi sonrası Fox şunu yapar:**

1. **Vaka dersleri çıkar** — projede her ajanın yaptığı iş incelenir, sektör/tip/süreç bazında öğrenmeler listelenir.
2. **Ajan dosyalarını güncelle** — her dersi ilgili ajan(lar)ın dosyasına "Vaka Hafızası" bölümüne işle. Ortak ders → tüm ajanlara; ajan-spesifik ders → sadece o ajana.
3. **Stale bilgileri temizle** — aktif müşteri listesi, pilot adaylar, referans vakalar güncellenir. Biten iş "aktif" kalmaz.
4. **Gelişim yol haritalarını gözden geçir** — bir ajan aynı hatayı tekrarladıysa, yol haritasına "Faz X" olarak eklenir.

**Tetikleyici:** "Tüm fazlar tamamlandı" veya "iş kapandı" kararı.
**Sorumlu:** Fox — Ayhan'ın ek izni beklenmez. Güncelleme Kademe 1 iş.
**Format:** git commit + anlamlı mesaj. Filo senkronizasyon güncellemesi tek commit'te.

---

---

## 7 · GERÇEK VAKA DENEYİMİ (Haziran 2026 — Faz 4 İlk Ay)

*Fox'un aktif 1 ayda öğrendikleri. Protokolü canlı veriden günceller.*

### Token Benchmarkları (Kabul Edilen Teslim Başına)

| İş | Ajan Sayısı | Yaklaşık Token | Notlar |
|---|---|---|---|
| Luxmed OS v2 (5 faz) | Fox + 5 özelleşmiş + 3 Denetmen turu | ~200K+ | Tam teslim zinciri, en yüksek |
| Syla 3-halka (Keşif→Strateji→Branding) | Fox + 3 ajan + 3 Denetmen | ~120K | Her halka ayrı Denetmen turu |
| TAG-KLOI kategori denetimi | Fox (araştırma ağırlıklı) | ~50K | Çok-adımlı web araştırma |
| Özgür Irmak konumlandırma hipotezi | Strateji (53K) + Denetmen (84K) | ~137K | İç planlama, tek hipotez belgesi |

**Gözlem:** Denetmen token maliyeti üretim ajanının 1.5x'ine ulaşabiliyor. Denetmen'i her önemsiz çıktıya koşturma. Kademe 1 işlerde (araştırma, özet) Fox öz-denetimi yeterli; yalnızca dış çıkış ve yüksek-risk kararlarında Denetmen.

### Denetmen Kalitesi — 4 Kritik Yakalama

1. **Endüstri bilgisi (Özgür Irmak):** Bebionic'in 2017'de Ottobock'a, Touch Bionics'in 2016'da Össur'a geçtiğini yakaladı — Strateji Ajanı bunları ayrı markalar gibi listeledi. Marka context'te bu konsolidasyon yoktu. Denetmen'in first-principles bilgisi kritik.

2. **Yüksek idari ceza boşluğu (Özgür Irmak):** Strateji Ajanı müşterinin en büyük kırılganlığını (idari ceza geçmişi) konumlandırma belgesinde hiç ele almadı. Denetmen ENGEL kesti. Strateji zaten iyi yazmıştı — ama bir şeyi atlamak da kritik bir hata.

3. **Exclusive clause (Özgür Irmak ↔ Luxmed):** Luxmed vakasından kurumsal ders — aynı sektörde iki müşteri → çakışma kontrolü. Strateji Ajanı sormadı, Denetmen sordu.

4. **Sahte kesinlik (Towdoo, SOC):** Denetmen'in sahte kesinlik mercek (8. mercek) gerçek işlerde döngüsel olarak çalıştı; iki vakada Fox'un kendi öz-denetimini atlayarak ürettiği sayısal skorları yakaladı.

### Döngüsel Delegasyon Riski — Gözlemlenen Durum

Haziran boyunca döngüsel delegasyon vakası YOK. Ancak şunlar gözlemlendi:
- Denetmen "Re-check" turu: Denetmen koşullu onay verdiğinde, Fox düzeltir, Denetmen tekrar koşar. Bu 2-3 tur alabilir. Tur sayısı her başta net çıkış koşuluyla sınırlanmıştı.
- Maksimum gözlemlenen: 3 Denetmen turu (Luxmed v2 — 5 faz × 3 Denetmen = 15 denetim döngüsü). Bu eşiği aşan iş yoktu.

### Supervisor Pattern: Ne Çalıştı, Ne Aksadı

**Çalışan:**
- Al → Ayrıştır → Delege → Denetmen → Sentezle akışı sorunsuz işledi (Syla, Luxmed)
- Denetmen 7 mercek kalite standardı tutarlı kaldı
- Fox öz-denetim + Denetmen = iki bağımsız gözlem → atlanmış risk oranı düştü

**Aksayan:**
- Denetmen token maliyeti üretim ajanından ağır olabiliyor (Özgür Irmak: 84K vs 53K). Denetmen brifingi ne kadar uzun tutulursa maliyet o kadar artıyor; kısa ve odaklı brifing gerekiyor.
- Müşteri bağlamı eksik aktarıldığında Strateji Ajanı endüstri konsolidasyonunu gözden kaçırdı (Bebionic/Touch Bionics). Marka context belgelerinin birleştirme/konsolidasyon notlarını içermesi gerekiyor.
- Scheduled task modunda (kullanıcı yok) Ayhan onayı gerektiren kararlar askıda kalıyor — engel bekleniyor ama hiçbir şey kesinleşemiyor. Bu doğru; ama Ayhan'a çıkan kararların net "tek dokunuşla biter" formatında sunulması şart.

---

## 8 · ÖLÇÜM EŞİKLERİ (Haziran Verisinden)

| Ölçüt | Gözlemlenen | Hedef (tahmini) |
|---|---|---|
| Kabul edilen teslim başına token (tam teslim zinciri) | ~120-200K | < 300K |
| Kabul edilen teslim başına token (tek belge) | ~50-137K | < 150K |
| Denetmen re-check turu | maks 3 | ≤ 3 |
| Döngüsel delegasyon vakası | 0 | 0 |
| Denetmen ENGEL oranı | 2/9 bulgu (%22) | izlenecek |

*Eşikler yeterli veri olmadan sıkıştırılmaz — 5 Haz §0.1 disiplini. Bu tablo Eylül 2026'da kalibre edilecek.*

---

*Sürüm: v4 · 2 Temmuz 2026 · Fox · §7 Gerçek Vaka Deneyimi + §8 Ölçüm Eşikleri eklendi (Faz 4 ilk ay retrospektifi)*
