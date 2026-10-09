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

## MÜFREDAT (6 Ekim 2026 — Ayhan talebiyle kuruldu)
Günde 30 dk, 12 hafta (6 Ekim → 1 Ocak 2027), eğitmen çerçevesinde. Tam program, gerçek kaynaklar (Higgsfield Academy 9 kurs + sinematografi + prompt guide'lar): → `fox-ai-director-mufredati.md`.

## YARDIMCI YÖNETMEN — ASTRID NİLSEN (10 Ekim 2026 kuruldu)
Ayhan'ın (Yönetmen) yürütme kolu — vizyonu sahne kırılımına/çekim listesine çevirir, sürekliliği (Soul ID, kıyafet/mekân/stil) takip eder, prodüksiyon sırasını yönetir. Geleneksel sette ayrı olan AD + Script Supervisor işlevleri Ayhan'ın kararıyla tek ajanda birleşti. Tanım: `.claude/agents/astrid-nilsen.md`.

---
*v0.1 · 6 Ekim 2026 · Fox · Açık/devam eden çalışma notu — kapanmış bir karar belgesi değil.*
