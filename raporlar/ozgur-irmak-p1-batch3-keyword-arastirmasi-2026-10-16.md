# Özgür Irmak — P1 Batch 3: Anahtar Kelime + AI Sorgu Araştırması (+ Canlı Proklinik Sitemap Doğrulaması)

*Growth Ajanı · 16 Ekim 2026 · Kademe 1 — ARAŞTIRMA/BRİEF, hiçbir yazı yazılmadı/taslak oluşturulmadı*

**Devralınan:** `ozgur-irmak-icerik-hacmi-plani-2026-10-16.md` (P1 dalgası — 37 net başlık, 5 küme, DÜŞÜK gate) · `ozgur-irmak-p1-batch1-keyword-arastirmasi-2026-10-16.md` (6 yazıldı+yayınlandı) · `ozgur-irmak-p1-batch2-keyword-arastirmasi-2026-10-16.md` (7 taslak, Denetmen'de + statik sayfa duplicate-tarama yöntemi) · `marka-bulutu-os-medikal-protez-bagi.md` §A.3/§C.

> ⚖️ **ETİK SINIR (değişmeden taşındı):** Proklinik sayfaları yalnızca konu haritası/ilham — hiçbir metin/cümle alınmadı veya parafraz edilmedi. Metin Yazarı sıfırdan yazacak. Bu turda Proklinik'in **tam /bilgi sitemap'i** (`curl sitemap.xml`, canlı veri) okundu — bu, konu haritasını netleştirmek içindi, metin devşirmek için değil.

---

## 0 · İKİ VERİ ŞEFFAFLIĞI DÜZELTMESİ (§0.1 — görevden önce açık edilmesi gereken)

**Düzeltme 1 — "166 vs 207" artık çözüldü, 207 doğru çıktı:** Plan belgesinin §0'ı "iletilen ham liste 166 benzersiz slug içeriyor, 207 rakamı nereden geliyor teyit edilemedi" diyordu. Bu turda `curl https://www.proklinik.com.tr/sitemap.xml | grep '/bilgi/' | sort -u | wc -l` ile **canlı sitemap'ten doğrudan sayıldı: tam 207 URL.** Yani görev tanımındaki orijinal "207" rakamı **doğruymuş** — önceki oturumun 166'lık çalışma listesi muhtemelen bir ara-filtre veya kısmi tarama sonucuydu, eksikti. Bu turun seçimleri, önceki oturumun erişilemeyen (scratchpad'e özel, bu oturuma taşınmamış) 166-slug/classify.py çıktısına değil, **bu turda taze çekilen tam 207-slug listesine** dayanıyor — aşağıdaki küme eşlemesi bu nedenle yeni ve bağımsız bir sınıflandırma, önceki oturumun otomatik gruplamasının devamı değil. Fark gizlenmedi, burada açık.

**Düzeltme 2 — "~24 kaldı" değil, 21 kaldı:** Görev tanımı P1'den "13 yazıldı + 3 elendi = 16 çıkar, ~24 kalır" diyordu. Plan'ın kendi §6 tablosundaki 5 P1 kümesinin toplamı **37**'dir (9+8+9+6+5). 37 − 16 = **21**, 24 değil. Bu fark görev tanımının bir yaklaşıklamasıydı (işaretli "~"), düzeltme burada not edildi, yoksa 24'e zorla tamamlanmadı.

**Kümelere göre kalan (plan §6 dağılımından, bu turun kendi hesaplamasıyla):**
| Küme | P1 toplam | Kullanılan (B1+B2+elenen) | Kalan |
|---|---|---|---|
| Ortez-genel | 9 | 4 (Ortez Nedir·Malzemeleri·El-Kol Ortezleri·[Ortez Çeşitleri elendi]) | **5** |
| Alt ekstremite derinleştirme | 8 | 4 (Karbon Ayak·Bileşenleri·Seçim Kriterleri·[Kalça Dezartik. elendi]) | **4** |
| Üst ekstremite derinleştirme | 9 | 3 (Kozmetik Kol·Omuz Dezartik.·[Parmak Protezi elendi]) | **6** |
| Mikroişlemcili diz derinleştirme | 6 | 1 (vs Mekanik) | **5** |
| Teknoloji-vitrin DÜŞÜK | 5 | 4 (SGK·3D Tarama·CPM·FES) | **1** |
| **TOPLAM** | **37** | **16** | **21** |

---

## 1 · YÖNTEM — bu turda eklenen katman: statik sayfa WebFetch önce, araştırma sonra

Batch 2'nin kalıcı-checklist önerisi (kendi §9'u) burada uygulandı: **her kandidat önce ilgili statik ürün/kategori sayfasına karşı WebFetch ile test edildi, sonra WebSearch araştırmasına geçildi.** Ayrıca canlı blog listesi de güncellendi — `blog-posts-sitemap.xml` şu an **25 yazı** döndürüyor (batch 2'nin bulduğu 18'den, bugünkü 7 taslağın bir kısmı + öncesinde bilinmeyen 1-2 ek yazı dahil — tam liste aşağıda §2'de kullanıldı).

**Sonuç — bu tur, 3 bilinen duplicate'in ÜSTÜNE, 21 kalan içinde 6 YENİ duplicate/cannibalization riski buldu** (detay §2). Bunlar yazılmadı; geriye kalan temiz adaylardan 6'sı seçildi.

---

## 2 · DUPLICATE/CANNİBALİZASYON TARAMASI — 21 kalanın tamamı statik sayfaya karşı test edildi

| Aday (kümesi) | Test edilen statik sayfa | Sonuç (WebFetch, bugün okundu) |
|---|---|---|
| "Ortezlerin Kullanım Amaçları" (Ortez-genel) | `/ortezler` | ❌ **DUPLICATE.** Sayfa zaten "Ortezlerin Kullanım Amaçları" başlığı altında 6 maddelik işlevsel liste taşıyor (eklem/kas desteği, hareket kontrolü, denge/yürüyüş desteği vb.) — ayrı bir yazı bu listeyi tekrar edecekti. |
| "Bacak ve Diz Ortezleri" genel bakış (Ortez-genel) | `/ortezler` | ⚠️ **Yüksek risk, elendi.** Sayfa AFO/DAFO/GRAFO/KAFO'yu "alt ekstremite ortezleri genel" çerçevesinde zaten kapsıyor; ayrı bir "bacak/diz ortezleri" yazısı aynı çerçeveyi tekrarlardı. |
| "AFO Nedir" tekrar / genel tanım (Ortez-genel) | `/afo` | ❌ Zaten dedike statik sayfa var (H1: "AFO - DAFO - KAFO - GRAFO") — tanım+tıbbi gösterge düzeyinde dolu. **Ama** sayfa **günlük kullanım/bakım/değiştirme bilgisi içermiyor** → bu boşluk kullanılabilir (bkz. §3.2). |
| "Myoelektrik ve Biyonik Sistem Arasındaki Fark" (Üst ekstremite) | `/dirsek-üstü-biyonik-kol-protezleri` | ❌ **DUPLICATE.** Bu statik sayfanın kendi H2 alt-başlığı zaten tam bu ad: "Myoelektrik ve Biyonik Sistem Arasındaki Fark." |
| "Üst Ekstremite Protez Tipleri ve Uyum Süreci" genel bakış (Üst ekstremite) | `/kol-protezleri` + 6 dirsek-altı/üstü tip sayfası | ❌ **Yüksek risk, elendi.** Hub zaten 3 tip (Kozmetik Silikon/Myoelektrik/Biyonik) + 6 ayrı tip-sayfası (dirsek altı/üstü × 3) barındırıyor — genel bir "tipler ve uyum süreci" yazısı bunları tekrar özetlerdi. |
| "Dirsek Üstü Kol Protezi İçin Kapsamlı Kılavuz" (Üst ekstremite) | `/dirsek-üstü-biyonik-kol-protezleri`, `/dirsek-üstü-myoelektrik-protezler`, `/dirsek-üstü-kozmetik-silikon-protezler` | ❌ **Yüksek risk, elendi.** 3 ayrı dedike statik sayfa zaten bu seviyeyi (dirsek üstü protez) tip bazında kapsıyor. |
| "Protez Ayak Nedir, Çeşitleri" genel giriş (Alt ekstremite) | `/bacak-protezleri`, `/protezler` | ✅ **Temiz AMA dar.** İki sayfa da bileşenleri "basitçe sıralıyor", **tip karşılaştırması (hangi ayak hangi aktiviteye uygun) hiç yok** → bu spesifik açı kullanılabilir (bkz. §3.1), ama "protez ayak nedir" genel tanımı ayrı yazılmaz (zaten Karbon Ayak yazısı + bu iki hub kapsıyor). |
| Gait/yürüyüş-postür analizi genel (Teknoloji-vitrin kalan 1) | `/yürüyüş-analizi` | ❌ **Yüksek risk, elenmeye en yakın.** Sayfa basınç sensörü, 3D ayak taraması, basınç dağılımı, adım hızı, ağırlık merkezini zaten "orta" derinlikte kapsıyor. Sektör bağının TZP uyarısı (teyitsiz tedarikçi şartnamesi riski) burada hâlâ geçerli. **Bu turda güvenli bir ayrışma bulunamadı — slot açık bırakıldı (§4.6), 3D Tarama ve CPM/FES'in dürüstlük presedanı tekrarlandı.** |
| Dirsek eklemi / protez kol mekanizması (Üst ekstremite) | `/dirsek-üstü-biyonik-kol-protezleri` | ✅ **Temiz.** Sayfa "dirseği büküp açabilir" gibi kullanıcı-faydası diliyle kalıyor; dirsek mekanizmasının (kablo/motor/kilit tipi) teknik işleyişine girmiyor → kullanılabilir (bkz. §3.3). |
| Kol protezi takma/çıkarma günlük süreç (Üst ekstremite) | `/uygulama-ve-uyarlama` | ✅ **Temiz.** Sayfa genel klinik uyarlama sürecini (biyomekanik ayar, yürüme eğitimi) anlatıyor — günlük giyim/çıkarma pratiğine girmiyor → kullanılabilir (bkz. §3.4). |
| Miyoelektrik değerlendirme süreci (Üst ekstremite) | `/değerlendirme-ve-ölçü` | ✅ **Temiz.** Sayfa genel değerlendirme+ölçü sürecini anlatıyor, "myoelektrik/biyonik protezlere özgü değerlendirme (kas sinyali testi, aday kriterleri) açıklanmamaktadır" (WebFetch'in kendi ifadesi) → kullanılabilir (bkz. §3.5). |
| Mikroişlemcili diz pil/şarj/bakım (Mikroişlemcili diz) | `/mikroişlemcili-biyonik-protezler` + canlı "Protez Bacak ve Kol Bakımı" HUB yazısı | ✅ **Temiz.** Statik sayfa teknoloji/avantaj/seçim kriteri anlatıyor ama "pil/şarj yönetimi, günlük bakım, temizlik, ömür beklentisi... bulunmamaktadır" (WebFetch). HUB bakım yazısı genel soket/liner temizliğine odaklı, cihaz-spesifik pil yönetimine girmiyor → kullanılabilir (bkz. §3.6). |

**Sonuç — 12 aday test edildi, 6'sı duplicate/yüksek-risk nedeniyle elendi (5'i kesin DUPLICATE/yüksek-risk + 1'i Teknoloji-vitrin'in açık kalan slotu), 6'sı temiz çıktı.** Bu 6 temiz aday aşağıda işlendi.

---

## 3 · SEÇİLEN 6 BAŞLIK — klasik + AI sorgu + rakip gözlem + H1/FAQ

### 3.1 · Protez Ayak Çeşitleri: Hangi Tip Hangi Aktivite Seviyesine Uygun?
*(Küme: Alt ekstremite derinleştirme)*

**Duplicate notu:** `/bacak-protezleri` ve `/protezler` bileşenleri sıralıyor ama tip-karşılaştırması yok (§2). Zaten yayındaki "Karbon Fiber Protez Ayak" yazısından (batch 1) farkı: o yazı TEK bir tipi (karbon/enerji depolayan) derinleştiriyordu, bu yazı **tüm ayak tiplerini (pasif/SACH, tek eksenli, hidrolik, karbon) yan yana** koyup aktivite seviyesine göre karşılaştırıyor — iç link ile birbirine bağlanmalı, tekrar etmemeli. Ayrıca batch 2'nin "Protez Bacak/Ayak Seçerken Hangi Faktörler Dikkate Alınır" yazısından farkı: o yazı amputasyon seviyesi/yaşam tarzı gibi BÜTÜN-protez karar eksenlerini ele alıyordu, bu yazı yalnızca **ayak ünitesi tipi** karşılaştırması — dar ve spesifik.

**Klasik arama kalıbı:**
- "protez ayak çeşitleri"
- "protez ayak türleri karşılaştırma"
- "hangi protez ayak bana uygun"

**AI-konuşma kalıbı:**
- "Protez ayaklar birbirinden ne kadar farklı, hepsi aynı mı çalışıyor?"
- "Daha aktif biri için hangi protez ayak önerilir, yürüme hızı etkiler mi?"
- WebSearch cevabı **K-seviyesi (K0-K3) aktivite sınıflandırması** üzerinden geldi — bu, klinik dünyada (Medicare/uluslararası protez camiası) standart bir çerçeve; K1 düşük hareketlilik → SACH/temel ayak, K2 → tek eksenli, K3 → dinamik/hidrolik/karbon. AI-sentez bu tip yapılandırılmış sınıflandırmayı doğrudan tercih ediyor.

**Rakip başlık kalıbı (gözlemlenen, kopyalanmayacak):**
- **Proklinik: *"Protez Ayak Nedir? Çeşitleri Nelerdir?"*** (proklinik.com.tr/protez-ayak-nedir-cesitleri-nelerdir) — doğrudan rakip, aynı konu.
- best-reha.com: *"Protez Ayak Kılavuzu: Türler, Avantajlar ve En İyi Kullanım Alanları"* — tip+kullanım-alanı eşleştirmesi, EN pazardaki standart kalıp.
- **Gözlem:** TR rakiplerin çoğu "tip" listesi veriyor ama K-seviyesi gibi bir **aktivite-sınıflandırma çerçevesi** kullanan TR kaynak bu aramada çıkmadı — EN kaynaklarda (hangerclinic, celerityprosthetics) standart. Bu, batch 1'in "mikroişlemcili vs mekanik" bulgusuyla aynı örüntü: TR'de yapılandırılmış karşılaştırma eksik.

**Önerilen H1/title:**
> **"Protez Ayak Çeşitleri: Hangi Tip Hangi Aktivite Seviyesine Uygun?"**

**FAQ alt-başlıkları:**
- Protez ayaklar arasındaki temel fark nedir (malzeme, hareket aralığı, enerji geri dönüşü)?
- Aktivite seviyesi (K-seviyesi gibi klinik sınıflandırmalar) protez ayak seçimini nasıl etkiler?
- Hidrolik ayak kimler için, karbon ayaktan farkı ne?
- ⚠️ **K-seviyesi/aktivite sınıflandırması bir kendi-kendini-değerlendirme aracı gibi sunulmaz** — "siz hangi seviyedesiniz" testi değil, kararın protez-ortez uzmanı + hekimle birlikte verildiği çerçevesi korunur (TİTCK M.5).

---

### 3.2 · AFO Nasıl Kullanılır? Günlük Giyim, Bakım ve Değiştirme Zamanı
*(Küme: Ortez-genel)*

**Duplicate notu:** `/afo` statik sayfası (H1: "AFO - DAFO - KAFO - GRAFO") tanım+tıbbi gösterge düzeyinde dolu ama **WebFetch'in kendi ifadesiyle** "günlük bakım, kullanım teknikleri, uyum süreci veya bakım yönergelerine yer vermemektedir." Bu yazı o sayfanın TANIMLADIĞI cihazın PRATİK kullanım kılavuzu — tamamlama ilişkisi (batch 2'nin "Protez Bacağın Bileşenleri" ile `/bacak-protezleri` ilişkisiyle aynı desen), rekabet değil. Zaten yayındaki "Ortez Nedir/AFO-KAFO" yazısından (batch 1) farkı: o yazı tanım/fark, bu yazı kullanım/bakım.

**Klasik arama kalıbı:**
- "AFO nasıl giyilir"
- "AFO bakımı nasıl yapılır"
- "AFO ne zaman değiştirilir"

**AI-konuşma kalıbı:**
- "Çocuğuma AFO verdiler, nasıl giydireceğim, ilk gün ne kadar süre takmalı?"
- "AFO'yu nasıl temizlerim, kaç yılda bir değiştirilir?"
- WebSearch cevabı somut ve adım-adım geldi: giyim tekniği (cırt sıkılığı, topuk pozisyonu), **kademeli alıştırma** ("ilk gün 1 saat gözlemle"), temizlik (sabunlu su, yumuşak bez, güneşten koru), **ortalama 1 yıl kullanım ömrü + 6 ayda bir kontrol.** Bu "adım-adım pratik rehber" formatı AI-cevabın tercih ettiği yapı, saf tanım sayfasından (zaten yayında) tamamen farklı.

**Rakip başlık kalıbı:**
- **Proklinik: *"AFO Kullanım Kılavuzu"*** (proklinik.com.tr listesinde `afo-kullanim-kilavuzu` slug'ı olarak teyitli) — doğrudan rakip, dedike sayfa.
- Provital: *"Afo Ortez Çeşitleri ve Kullanım Amaçları"* — tür+amaç karması, pratik kılavuz değil.
- DMD Warrior: *"...AFO: Faydaları, Kullanım Alanları ve Bakım İpuçları"* — hastalık-spesifik (DMD) ama bakım ipucu formatı bizim yazımızla örtüşüyor.
- medikalbdk.com: *"Ayak Bilekliği Nasıl Takılır? Ortez Seçim ve Kullanım Rehberi"* — ticari/ürün sitesi, protez-ortez merkezi değil.

**Önerilen H1/title:**
> **"AFO Nasıl Kullanılır? Günlük Giyim, Bakım ve Değiştirme Zamanı"**

**FAQ alt-başlıkları:**
- AFO ilk kez takıldığında nelere dikkat edilmeli (alıştırma süresi)?
- AFO nasıl temizlenir, günlük bakımı nasıl yapılır?
- AFO ortalama ne kadar süre kullanılır, ne zaman değiştirilir?
- Ciltte kızarıklık/tahriş olursa ne yapılmalı?
- ⚠️ "Ortalama 1 yıl" gibi süre bilgisi **genel/sektör bilgisi olarak** verilir, kesin taahhüt değil ("kişiye, modele, büyümeye göre değişir" çerçevesi korunur) — avukat/klinisyen teyidi gerekir (hafif-dokunuş, DÜŞÜK gate).

---

### 3.3 · Protez Kolun Dirsek Eklemi Nasıl Çalışır? Mekanik ve Elektronik Kilitleme
*(Küme: Üst ekstremite derinleştirme)*

**Duplicate notu:** `/dirsek-üstü-biyonik-kol-protezleri` (ve diğer dirsek-üstü tip sayfaları) kullanıcı-faydası diliyle kalıyor ("dirseği büküp açabilir") — dirsek ekleminin MEKANİZMASINI (kablo/motor/kilit tipi, kaç kilitleme pozisyonu) hiç açıklamıyor (§2). Bu yazı, batch 2'nin "Protez Bacağın Bileşenleri" ile aynı mantıkla, ürün-tipi sayfalarının değil **bileşen/mekanizma** düzeyinin derinleştirmesi.

**Klasik arama kalıbı:**
- "protez kol dirsek eklemi nasıl çalışır"
- "protez dirsek kilitleme sistemi"

**AI-konuşma kalıbı:**
- "Protez kolun dirseği nasıl bükülüyor, elle mi kontrol ediliyor?"
- "Elektronik dirsek ile mekanik dirsek arasındaki fark ne?"
- WebSearch cevabı iki ayrı mekanizmayı net ayırdı: **mekanik (kablo+omuz hareketiyle kumanda, 7-11 kilitleme pozisyonu)** vs **elektronik (motor+solenoid, kas sinyaliyle/switch ile kilitlenip açılabilir)** — bu "iki sistem karşılaştırması" kalıbı, batch 1'in mikroişlemcili-vs-mekanik dizdeki bulgusuyla aynı örüntü, ama kolda hiç işlenmemiş.

**Rakip başlık kalıbı:**
- **Proklinik'in kendi /bilgi listesinde `dirsek-eklemleri` adında ayrı bir slug var** — doğrudan rakip, aynı bileşen-odaklı konu.
- MEGEP (MEB eğitim modülü, akademik/devlet kaynağı): "Dirsek Üstü Protezi İmalatı" — teknik/imalat odaklı, protez-ortez merkezi değil.
- Proklinik: *"Dirsek Üstü Kol Protezleri"* — ürün sayfası, mekanizma değil.

**Önerilen H1/title:**
> **"Protez Kolun Dirsek Eklemi Nasıl Çalışır? Mekanik ve Elektronik Kilitleme Sistemleri"**

**FAQ alt-başlıkları:**
- Mekanik (kablo kontrollü) dirsek eklemi nasıl kilitlenir/açılır?
- Elektronik dirsek eklemi kas sinyaliyle mi, düğmeyle mi kontrol edilir?
- Dirsek kaç farklı pozisyonda kilitlenebilir, bu günlük kullanımı nasıl etkiler?
- ⚠️ Teknik mekanizma anlatımı **"hangisi daha iyi"** üstünlük diline kaymaz — ihtiyaca/aktiviteye göre farklı seçenek çerçevesi korunur.

---

### 3.4 · Kol Protezi Günlük Yaşamda Nasıl Takılır, Çıkarılır?
*(Küme: Üst ekstremite derinleştirme)*

**Duplicate notu:** `/uygulama-ve-uyarlama` genel KLİNİK uyarlama sürecini (biyomekanik ayar, yürüme eğitimi, hizalama) anlatıyor — kol protezine özgü günlük giyim/çıkarma pratiğine girmiyor (§2). Bu, Proklinik'in kendi "Kol Protezi Nasıl Takılır" başlığının (batch 1'de zaten gözlemlenmiş, bu turda alınan) doğrudan karşılığı.

**Klasik arama kalıbı:**
- "kol protezi nasıl takılır"
- "protez kol günlük kullanım"

**AI-konuşma kalıbı:**
- "Protez kolu her gün kendim mi takıyorum, yardım gerekir mi?"
- "Protez kolu gece çıkarmak gerekir mi, güdüğe zararı olur mu?"
- WebSearch cevabı somut bir günlük-rutin verdi: takma/ayarlama protezci tarafından kişiye özel yapılır, günlük aktivitede (yazı yazma, kavrama, yemek) kullanılır, **gece çıkarılması genellikle önerilir** (güdük dokusunun havalanması/cildin dinlenmesi için) — ama kesin uygulama uzman/hekim önerisine bağlı.

**Rakip başlık kalıbı:**
- **Proklinik: *"Kol Protezi Nasıl Takılır"*** — doğrudan rakip (batch 1 §5'te zaten not edilmişti, bu turda konu olarak alındı).
- protezci.net, egelimedikal.com — ticari/fiyat odaklı sayfalar, günlük-pratik rehber değil.

**Önerilen H1/title:**
> **"Kol Protezi Günlük Yaşamda Nasıl Takılır, Çıkarılır?"**

**FAQ alt-başlıkları:**
- Protez kol ilk takıldığında kendi başına mı takılıyor, yardım gerekiyor mu?
- Protez kol gece çıkarılmalı mı, güdük cildi nasıl dinlendirilir?
- Günlük aktivitelerde (yazı, kavrama, yemek) protez kolun rolü nasıl öğreniliyor?
- ⚠️ "Gece çıkarma" önerisi genel bilgi olarak verilir, kesin talimat değil — "en doğru uygulama uzman teknisyen ve hekimin önerisi" çerçevesi korunur (WebSearch'ün kendi vurgusu).

---

### 3.5 · Üst Ekstremite Protezlerinde Miyoelektrik Değerlendirme Süreci Nasıl İşler?
*(Küme: Üst ekstremite derinleştirme)*

**Duplicate notu:** `/değerlendirme-ve-ölçü` genel değerlendirme+ölçü sürecini (güdük durumu, yaşam biçimi, soket ölçümü, 3D tarama) anlatıyor ama **WebFetch'in kendi ifadesiyle** "myoelektrik/biyonik protez türlerine özgü bir değerlendirme süreci (kas sinyali testi, aday kriterleri gibi) açıklanmamıştır." Zaten yayındaki "Miyoelektrik (Biyonik) El Nasıl Çalışır" yazısından farkı: o yazı CİHAZIN çalışma mantığı, bu yazı KİŞİNİN bu cihaza aday olup olmadığının DEĞERLENDİRME süreci.

**Klasik arama kalıbı:**
- "miyoelektrik protez değerlendirme"
- "kas sinyali testi protez kol"

**AI-konuşma kalıbı:**
- "Miyoelektrik kol bana uygun mu, nasıl karar veriliyor?"
- "Kas sinyalim yeterli mi, bunu nasıl test ediyorlar?"
- WebSearch cevabı çok-faktörlü bir değerlendirme süreci verdi: amputasyon seviyesi + kas kontrolü + cilt durumu + mesleki ihtiyaç + rehabilitasyon süreci birlikte değerlendiriliyor; **kas sinyali kalitesi** klinik testle belirleniyor, zayıf sinyal/cilt sorunu/soket stabilite sorunu performansı düşürebiliyor; fizyoterapiyle sinyal-kontrol eğitimi alınıyor.

**Rakip başlık kalıbı:**
- **Proklinik'in kendi /bilgi listesinde `ust-ekstremite-protezlerinde-miyoelektrik-degerlendirme` adında ayrı bir slug var** — doğrudan rakip, birebir aynı konu.
- Luxmed: *"İlk Protez Kol Nasıl Seçilir? Çeşitleri ve Seçim Rehberi"* — genel seçim rehberi, değerlendirme-süreci-spesifik değil.
- mardinortopedi.com: *"Myoelektrik Kol Protezi İnceleme Rehberi"* — ürün inceleme, süreç değil.

**Önerilen H1/title:**
> **"Üst Ekstremite Protezlerinde Miyoelektrik Değerlendirme Süreci Nasıl İşler?"**

**FAQ alt-başlıkları:**
- Miyoelektrik protez için "aday" olmak ne anlama gelir, hangi kriterlere bakılır?
- Kas sinyali kalitesi nasıl test edilir, bu testi kim yapar?
- Cilt durumu veya soket stabilitesi değerlendirmeyi nasıl etkiler?
- Değerlendirme sonucu olumsuzsa alternatif seçenek var mı (kozmetik/body-powered)?
- ⚠️ **Yüksek dikkat gerektiren başlık:** "aday kriterleri" listesi bir **kendi-kendini-teşhis/uygunluk testi** gibi sunulmaz — her zaman "nihai karar klinik değerlendirmeyle, hekim+protez-ortez uzmanı ekibiyle verilir" çerçevesi korunur (TİTCK M.5'e en yakın başlık bu turda — Denetmen'e özellikle işaretli gitmeli, batch 2'nin "Seçim Kriterleri" başlığıyla aynı hassasiyet düzeyinde).

---

### 3.6 · Mikroişlemcili Dizin Pil/Şarj Yönetimi ve Günlük Bakımı
*(Küme: Mikroişlemcili diz derinleştirme — bu kümenin P1'de İLK kez dolan slotu, batch 2 tamamen boş bırakmıştı)*

**Duplicate notu:** `/mikroişlemcili-biyonik-protezler` teknoloji/avantaj/seçim kriterini anlatıyor ama **WebFetch'in kendi ifadesiyle** "pil/şarj yönetimi, günlük bakım, temizlik, ömür beklentisi gibi kullanıcı rehberi konuları bulunmamaktadır." Canlı "Protez Bacak ve Kol Bakımı" HUB yazısı genel soket/liner temizliğine odaklı, elektronik/pil-spesifik değil. Zaten yayındaki "Mikroişlemcili Diz ile Mekanik Diz Farkı" (batch 1) ve eski "Mikroişlemcili Diz Nedir" yazılarından farkı: onlar CİHAZIN ne olduğu/farkı, bu yazı **sahip olduktan SONRA günlük pil/bakım rutini.**

**Klasik arama kalıbı:**
- "mikroişlemcili diz protez pil şarj"
- "protez diz bakımı su geçirmez mi"

**AI-konuşma kalıbı:**
- "Mikroişlemcili dizimi her gün şarj etmem gerekiyor mu, kaç gün gider?"
- "Mikroişlemcili diz ile duşa girebilir miyim, suya dayanıklı mı?"
- WebSearch cevabı model bazlı somut aralıklar verdi: bazı modeller **geceleri her gün şarj** gerektiriyor, bazıları **birkaç günde bir**; bazı modeller **belirli bir su geçirmezlik derecesine** sahip (model bazlı değişir); yılda/6 ayda bir **bakım kontrolü** öneriliyor. **Bu rakamlar marka/modele göre değişir — Özgür Irmak'ın yazısı tek bir marka/model rakamı vermez**, "modelinize göre değişir, cihazınızın kullanım kılavuzuna/uzmana danışın" çerçevesini korur (aşağıdaki öz-denetimde tekrar vurgulandı).

**Rakip başlık kalıbı:**
- Proklinik'in /bilgi listesinde bu spesifik açı (pil/şarj/bakım) için **dedike bir sayfa bulunamadı** — `mikroislemcili-diz-eklemleri-rehberi`, `mikroislemcili-protezler` gibi slug'lar var ama WebSearch'te bunların pil/bakım derinliğinde olduğuna dair kanıt çıkmadı.
- EN kaynaklarda (hangerclinic, primecareprosthetics) bu konu işleniyor ama TR'de protez-ortez merkezi kaynaklı dedike bir "pil/bakım" yazısı bu aramada bulunamadı.
- **Dürüstlük notu (batch 1'in 3D Tarama presedanıyla aynı):** Bu, "rakip yok çünkü talep zayıf" ihtimalini de taşıyabilir — ama günlük kullanıcı sorunu (şarj unutma, su geçirmezlik belirsizliği) somut ve gerçek, sadece henüz TR'de dedike içerik üretilmemiş bir alan.

**Önerilen H1/title:**
> **"Mikroişlemcili Dizin Pil/Şarj Yönetimi ve Günlük Bakımı Nasıl Yapılır?"**

**FAQ alt-başlıkları:**
- Mikroişlemcili diz günlük şarj gerektirir mi, şarj süresi nasıl planlanır?
- Mikroişlemcili diz ile duş alınabilir mi, suya dayanıklılık modelden modele değişir mi?
- Pil bitince/düşük uyarısı verince ne yapılmalı?
- Düzenli bakım kontrolü ne sıklıkta önerilir?
- ⚠️ **Marka/model-spesifik rakam (saat, su derinliği) yazıya KONMAZ** — "modelinize göre değişir, kullanım kılavuzunuza ve protez-ortez uzmanınıza danışın" çerçevesi korunur (Anayasa §11.5, rakam uydurma yok; bu WebSearch'te görülen rakamlar farklı markalara ait, Özgür Irmak'ın hangi markaları sağladığı bu oturumda teyit edilmedi).

---

## 4 · DİĞER 6 KÜME SLOTUNUN DURUMU (şeffaflık, zorla doldurulmadı)

1. **Ortezlerin Kullanım Amaçları** → elendi, `/ortezler` zaten kapsıyor (§2).
2. **Bacak ve Diz Ortezleri genel** → elendi, `/ortezler` zaten kapsıyor (§2).
3. **Myoelektrik vs Biyonik Sistem Farkı** → elendi, `/dirsek-üstü-biyonik-kol-protezleri`'nin kendi alt-başlığı (§2).
4. **Üst Ekstremite Protez Tipleri ve Uyum Süreci (genel)** → elendi, hub + 6 tip-sayfası zaten kapsıyor (§2).
5. **Dirsek Üstü Kol Protezi İçin Kapsamlı Kılavuz** → elendi, 3 dedike tip-sayfası zaten kapsıyor (§2).
6. **Teknoloji-vitrin'in son DÜŞÜK slotu** (gait/postür analizi) → **açık bırakıldı.** `/yürüyüş-analizi` zaten orta-derinlikte kapsıyor + TZP'nin teyitsiz-şartname uyarısı hâlâ geçerli. Batch 1'in CPM/FES'i açık bırakma, batch 2'nin mikroişlemcili-diz-kümesini boş bırakma presedanıyla aynı: zayıf/riskli sinyal zorla doldurulmadı.

**Pratik sonuç:** P1'in 21 kalanından bu turda **6'sı yazılabilir** bulundu (3.1-3.6), **5'i duplicate/cannibalization nedeniyle kapandı**, **1'i (Teknoloji-vitrin) hâlâ açık karar**, geriye **9 aday** (Ortez-genel'in kalan 2'si henüz test edilmedi çünkü §2'deki 2 test sonucu zaten o kümenin pratik sınırını gösterdi; Alt ekstremite'nin kalan 3'ü ve Üst ekstremite'nin kalan 3'ü) **batch 4'e** taşınır — bunlar bu turda hiç test edilmedi, duplicate olduğu iddia edilmiyor, sadece zaman/kapsam sınırı nedeniyle incelenmedi (uydurma yok).

---

## 5 · EN ÇARPICI BULGU

**Bu turun asıl bulgusu konu değil, yöntemin kendisi: statik sayfa duplicate taraması P1'in "kalan 21"ini neredeyse yarıya indirdi.** Batch 2, 3 duplicate bulup bunu istisna gibi ele almıştı; bu turda test edilen 12 adayın **6'sı** (yarısı) duplicate/yüksek-risk çıktı — özellikle **Üst ekstremite kümesi**, Özgür Irmak'ın kendi ürün mimarisinin (dirsek altı/üstü × kozmetik/myoelektrik/biyonik = 6 ayrı statik sayfa) OLDUĞU gibi, "tip tanımı" açısından artık doygun. Geriye kalan güvenli alan sistematik olarak **TİP TANIMI değil MEKANİZMA/SÜREÇ/BAKIM** düzeyinde çıktı (dirsek ekleminin NASIL çalıştığı, protezin NASIL takıldığı, değerlendirmenin NASIL işlediği, bakımın NASIL yapıldığı) — statik sayfalar "ne" sorusunu cevaplıyor, blog'un gerçek boşluğu "nasıl" sorusunda. Bu, **batch 4 ve sonrası için somut bir arama stratejisi:** yeni aday önerirken önce "bu TİP tanımı mı (muhtemelen hub'da var) yoksa SÜREÇ/MEKANİZMA mı (muhtemelen boşluk)" sorusu sorulmalı.

**İkincil bulgu:** 166 vs 207 sayım farkı (plan §0'da açık bırakılmıştı) bu turda **207'nin doğru olduğu** yönünde çözüldü (§0, Düzeltme 1) — canlı sitemap doğrudan sayıldı, tahmin değil.

---

## ÖZ-DENETİM NOTU (§0.1 — veri dürüstlüğü)

- **Proklinik'in 207 /bilgi URL'si bugün `curl` ile sitemap.xml'den doğrudan sayıldı** — tahmin değil, gerçek HTTP yanıtı (§0).
- **Özgür Irmak'ın 63 statik sayfa + 25 canlı blog listesi bugün `curl` ile yeniden doğrulandı** (batch 2'nin 59/18 rakamlarından küçük artış — 6-7 yeni taslak/yayın + önceden envantere girmemiş yazılar nedeniyle, fark gizlenmedi).
- **Hiçbir arama hacmi/zorluk rakamı yok** — yine Tip B (WebSearch'ün döndürdüğü gerçek başlık/cevap yapısı + K-seviyesi gibi tanınmış klinik çerçeveler), Ahrefs/Semrush erişimi yok.
- **Mikroişlemcili diz pil/şarj rakamları (şarj aralığı, su geçirmezlik derecesi) marka/modele göre değişen WebSearch sonuçlarıdır** — Özgür Irmak'ın hangi markaları sağladığı bu oturumda teyit edilmedi, yazıya marka-spesifik rakam KONMAYACAK şekilde §3.6'da işaretlendi.
- **Rakip başlıkları yalnızca gözlem** — hiçbiri yazıya kopyalanmadı/parafraz edilmedi; Proklinik'in tam /bilgi sitemap'i bu turda okundu ama bu, konu haritası netleştirme amaçlıydı (§ETİK SINIR).
- **Bu belge bir yazı değil** — Metin Yazarı bu brief'i alıp sıfırdan yazacak; H1 önerileri taslak, kesin değil.
- **6 aday bilerek elendi, zorla 7. veya 8. başlık eklenmedi** — görev tanımı "6-8" aralığı verdi, bu tur rigorous duplicate-taramasından sağ çıkan 6 ile sınırlı kaldı; sayıyı 8'e tamamlamak için zayıf/riskli bir aday eklemek dürüstlük ilkesine (§0.1) aykırı olurdu.

---

## SIRADAKİ ADIM (Ayhan/Fox kararı)

1. Bu 6 başlık Denetmen'e taşınabilir — özellikle **3.5 (Miyoelektrik Değerlendirme — TİTCK M.5'e en yakın)** ve **3.6 (Mikroişlemcili Diz Pil/Bakım — marka-spesifik rakam riski)** işaretli gitmeli.
2. Onaylanırsa Metin Yazarı'na 6 ayrı brief olarak devredilir.
3. **Batch 4 kapsamı:** Ortez-genel'in kalan 3'ü (test edilmedi) + Alt ekstremite'nin kalan 3'ü (test edilmedi) + Üst ekstremite'nin kalan 3'ü (test edilmedi) + Teknoloji-vitrin'in açık kalan 1 slotu (§4.6) — toplam ~9-10 aday, henüz statik sayfaya karşı test edilmedi.
4. **Kalıcı checklist önerisi (batch 2'den devam, güçlendirilmiş):** "TİP tanımı mı, SÜREÇ/MEKANİZMA mı" sorusu, statik-sayfa WebFetch adımından ÖNCE bir ön-filtre olarak eklenebilir — bu turun §5 bulgusu, hangi adayların muhtemelen duplicate çıkacağını önceden işaretlemeye yardımcı olabilir.

---
*Growth Ajanı · 16 Ekim 2026 · Kademe 1 (araştırma/brief, iç rapor) — dışarı gönderim yok, hiçbir yazı yazılmadı. Kaynak: WebSearch + WebFetch + canlı `curl sitemap.xml` taraması (16 Ekim, bugünkü oturum) + `ozgur-irmak-icerik-hacmi-plani-2026-10-16.md` + batch 1-2 raporları. Rakamsal arama hacmi/zorluk uydurulmadı. 166 vs 207 sayım farkı çözüldü (§0).*
