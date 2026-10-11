# AI Director İnşa Süreci — Çalışma Notu
*Açık/devam eden konuşma. 6 Ekim 2026 başladı. Burada kapanmadı — "daha sonra devam" notuyla kaydedildi.*

---

## MOTİVASYON (Ayhan'ın kendi sözleri)
Fotoğrafçı/yönetmen tarafı uzun süredir arka planda, sanatsal doyum/üretim yok. Mesele prodüksiyon mekaniğiyle (editör, makyaj, saç, stüdyo, model) uğraşmak değil — **zihindeki vizyonla çıktı arasındaki aracı katmanı kaldırmak.** Türkiye'de prodüksiyon sektörü giderek zorlaşıyor. "Bu birikim benden çıksın" istiyor — şu an isimsiz, tanımlanmak istenmiyor ama **görülebilir** olacak (portföy/vaka, sadece özel pratik değil).

**1 Ocak 2027 termini var** (~12 hafta, 6 Ekim itibarıyla).

## ARAŞTIRMA ÖZETİ
- **İki "AI Director" arketipi:** (1) Teknik/Kurumsal Director of AI (ML altyapı — Ayhan'ın yolu DEĞİL), (2) Yaratıcı/Pazarlama AI Creative Director (AI ajan/araç orkestrasyonu — Ayhan'ın yolu). Çekirdek beceri: "AI'ı yöneten" — Fox filosunu yönetmekle zaten pratik ediliyor.
- **Pazar kanıtı gerçek:** Mango/H&M/VENUS/bitStudio tam-AI kampanyalar yayınladı/üretti (2024-26). AI Creative Director ilanları $125K-273K/yıl bandında (ABD).
- **İki risk:** (1) Şeffaflık — Guess/Vogue Ağustos 2025 AI model skandalı, gizlemenin bedeli ağır (moda paketi zaten "AI-destekli" dilini açık tutuyor — doğru refleks). (2) Fiyat komoditeleşmesi — düz AI ürün fotoğrafı $0.16-0.98/görsele düştü; **yazarlık/imza satmak gerekiyor, komodite değil.** (3) İşsizlik anlatısı/tepki — ama ICP (emerging/DTC, zaten çekim yapamayan marka) bu çatışmanın dışında.
- Kaynaklar: bkz. sohbet geçmişi 6 Ekim 2026 (WebSearch, çok sayıda — buraya tek tek taşınmadı, gerekirse tekrar aranır).

## AÇIK KARAR — kapanmadı
CMM (Creative Marketing Manager, moda paketi) ile "AI Director" ilişkisi netleşmedi. Üç seçenek masada: (1) AI Director CMM'in yerine geçer, (2) AI Director üst/genel kimlik, CMM moda-vertical'e özel kalır [Fox önerisi], (3) önce iç beceri, kimlik kararı sonra.

## TEKNİK ÇÖZÜM — Soul ID (Higgsfield)
Model sürekliliği sorunu (Ayhan'ın kendi tespiti) → endüstri standardı çözüm: kimlik eğitimi. `higgsfield-soul-id` skill'i (bu oturumda zaten kurulu) tam bunu yapıyor.

**İş akışı:** (1) İcat — saf prompt'la yüzü bir kere üret. (2) Çoğalt — o görseli `--image` referans vererek 7-11 varyasyon (açı/ışık/ifade) üret, 8-12'lik set oluştur. (3) Eğit — `higgsfield soul-id create --name "Claudia" --soul-2 --image ...`. (4) Kullan — `--soul-id <id>` ile her üretimde aynı kimlik.

**Hesap durumu (6 Ekim 2026):** Workspace seçili (`cfa226cc-...`), **starter plan, 140 kredi**. Soul eğitimi "Basic+" gerektiriyor diye skill belgesinde yazıyor — starter'ın yeterli olup olmadığı **test edilmedi** (gerçek kredi harcar, önce Ayhan onayı).

## KİMLİK KARARI — gerçek kişi değil, icat
İlk seçenek (gerçek model/kişi fotoğraflayıp eğitmek) reddedildi — KVKK/rıza + "AI kimliği sonsuza dek kullanılacak" sözleşme riski ağır. **Karar: sıfırdan icat edilen karakter.**

⚠️ **İki kalibrasyon notu (bu oturumda işlendi):** Gerçek/ünlü kişi (Naomi Osaka) ve telif korumalı kurgu karakter (Lagertha/Vikings dizisi + oyuncu Katheryn Winnick) **yüz/likeness referansı olarak kullanılmadı** — yalnız enerji/vibe/arketip dili çıkarıldı. Claudia'nın yüzü ikisinden de bağımsız, tanınmaz olmalı.

## CLAUDIA — karakter briefi (6 Ekim 2026, tamamlandı)
| Alan | Değer |
|---|---|
| Yaş | 27 |
| Köken | İskandinav |
| Burun | Kemerli, belirgin |
| Saç | Açık/küllü sarı, örgülü |
| Ten | Soluk, soğuk ton, hafif çil |
| Çene/elmacık | Belirgin, keskin hatlı |
| Göz rengi | Buz mavisi / gri-mavi |
| Enerji | Sakin-yoğun, savaşçı-regal — komuta eden bakış, "sahneyi kuran" (poz veren değil) |
| Referans (vibe, yüz değil) | Osaka (felsefe: her görünüm bir hikâye, kendi imajının yazarı) + Lagertha arketipi (duruş, örgü) |
| Marka bağlamı | Cloud One (SOC çorap ürünü) testleri — palet/ışık henüz konuşulmadı (bilerek ertelendi) |

## SIRADAKİ ADIM (konuşma kaldığı yer)
Kıyafet/stil + ifade detayı konuşulacak. Sonra ilk test üretimi (kredi harcar — Ayhan onayı net istendi, henüz verilmedi).

**Termin (10 Ekim 2026, Ayhan belirledi):** İlk deneme **Ekim'in son haftası** — müfredatın Faz 1 bitişi/Faz 2 başına doğal denk geliyor. Özgür Irmak rutine düşünce zaman/bütçe baskısı gevşedi, "AI üretime zaman ve para ayırabilir hale geliyorum" (Ayhan'ın kendi ifadesi).

## MÜFREDAT (6 Ekim 2026 — Ayhan talebiyle kuruldu)
Günde 30 dk, 12 hafta (6 Ekim → 1 Ocak 2027), eğitmen çerçevesinde. Tam program, gerçek kaynaklar (Higgsfield Academy 9 kurs + sinematografi + prompt guide'lar): → `fox-ai-director-mufredati.md`.

## HIGGSFIELD KAYITLARI (11 Ekim 2026)
- **Claudia Soul ID:** `4bdd93e9-3183-44be-ad91-be0070ccaf35` (tip `soul_2`) — Ayhan tarafından oluşturuldu, durum **completed** (11 Ekim öğleden sonra eğitim bitti). İki Sahne 1 test üretimi yapıldı (text2image_soul_v2): kimlik/mekân iyileşti ama **kompozisyon** (model ısrarla yakın plana kayıyor, "geniş kare" talebini dinlemiyor) ve **istenmeyen ceket logosu** (muhtemelen eğitim setinden geliyor) iki denemede de tutmadı. Kredi: ~115 (starter plan, iki deneme ~25 kredi harcadı).
- **Cloud One ürünü (Marketing Studio):** `2d613640-d2af-43da-91b9-f8de56a8889b` — 10 gerçek ürün fotoğrafı (`~/Desktop/Steps On Clouds/Store/CloudOne/Ghost/`), manuel kayıt, durum completed. `product_ids` parametresiyle Marketing Studio modellerinde (`marketing_studio_video`/`image`) kullanılabilir.
- Kaynak klasör yapısı: `Steps On Clouds/Store/CloudOne/` altında `Ghost/` (ghost mannequin ürün çekimleri, kayıtlı) + `Steps On Mela/` (gerçek fotoğraf çekimi, henüz kullanılmadı) + `CloudOne Etiket.jpg` (etiket görseli). Ayrıca `Steps On Clouds/Visual /Görseller/Tenis/` klasörü var — muhtemelen daha önce gösterilen tenis-kort referans görseliyle ilişkili, henüz teyit edilmedi.

## 7 SAHNE ÜRETİMİ (11 Ekim 2026 — devam ediyor)
Astrid'in 7-sahne tenis hikayesi (kuruluş→ritüel→geçiş→eşik→zirve→duraklama→çözüm) gerçek üretime geçti. **Model: `nano_banana_pro`** (text2image_soul_v2 + `--image` kombosu `enhance_prompt` hatası veriyor — bkz. aşağı). Sahne 1 (soul_location, kişisiz) ve Sahne 2/4 onaylı; Sahne 3'te 3 sorun bulundu (kıyafet/raket/kort), seride sona bırakıldı; Sahne 5 kıyafet/çorap temiz ama servis pozu brief'i karşılamıyor (yakın/forehand gibi duruyor, tam servis değil).
**Teknik ders (Astrid'in Modül 16'sına işlenecek):** `text2image_soul_v2` + `--soul-id` + `--image` birlikte kullanılınca model sessizce `enhance_prompt: true` tetikliyor ve tüm prompt'u referans görselin otomatik açıklamasıyla değiştiriyor — sahneyi yok ediyor. Çözüm: bu modelde `--image` hiç kullanılmıyor; çoklu-referans gereken sahnelerde `nano_banana_pro` (`image_references`, max 14) kullanılıyor — `enhance_prompt` alanı şemasında bile yok, prompt birebir korunuyor.
**11 Ekim — Ayhan talimatı:** "her kare için ayrı prompt çıkar, karakter/mekân/kıyafet hepsinde aynı olsun" + "ayakkabısız olmaz, Babolat ayakkabı kullan." Bütün 7 sahne tek kılıkla (beyaz pileli tenis elbisesi + Cloud One çorap + Babolat ayakkabı, polo/headband planı terk edildi) yeniden yazıldı → `fox-claudia-cloudone-7-sahne-prompt-seti.md`. Üretildi, ayakkabı tutarlılığı 3. görsel referansla kesin çözüldü (teknik detay: `astrid-ai-gercekcilik.md` Modül 16).

**12 Ekim — "genel olarak memnun değilim" + kök sebep teşhisi:** Teknik kutu (tutarlılık) kapandı ama Ayhan sonuçtan memnun değil. Teşhis: **poz dili "stok" duruyor** — prompt'lar "commanding," "confident stance," "frozen instant, composed" gibi idealize edilmiş/kontrollü dil kullanıyor, bu da tam olarak stok fotoğrafçılığın formülü. Ayhan'ın kendi tanımı: **"hareketin kendisini vermemiz gerekiyor, hareketin öncesi veya sonrasını değil"** — yani Sahne 5'in "sıçrayan servis"i bile aslında dengeli/güzel/kontrollü bir duruş, gerçek bir 150km/s vuruşun kaotik fiziği değil. Düzeltme yönü (gerçek hareket bulanıklığı, dengesizlik, yüzde gerçek efor izi) konuşuldu ve not edildi ama **Ayhan'ın açık kararıyla şimdilik uygulanmadı** — "şu an için böyle kalalım, bişey denemeyelim." Seri bu haliyle (v2, tutarlı ama "stok poz" eleştirisiyle) duraklatılmış durumda. Bu, ayrı/teknik bir sorun değil — **Ayhan'ın yönetmenlik sesinin kendisiyle ilgili, daha derin bir açık konu** ("Ruh" muhabbetiyle aynı damar): AI'ın varsayılan "iyi görünen" çıktısı ile Ayhan'ın kendi spesifik bakışı arasındaki fark henüz kapanmadı.

## YARDIMCI YÖNETMEN — ASTRID NİLSEN (10 Ekim 2026 kuruldu)
Ayhan'ın (Yönetmen) yürütme kolu — vizyonu sahne kırılımına/çekim listesine çevirir, sürekliliği (Soul ID, kıyafet/mekân/stil) takip eder, prodüksiyon sırasını yönetir. Geleneksel sette ayrı olan AD + Script Supervisor işlevleri Ayhan'ın kararıyla tek ajanda birleşti. Tanım: `.claude/agents/astrid-nilsen.md`.

---
*v0.1 · 6 Ekim 2026 · Fox · Açık/devam eden çalışma notu — kapanmış bir karar belgesi değil.*
