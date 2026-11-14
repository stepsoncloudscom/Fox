# Instagram Haftalık Döngü — Uygulama Planı

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** @stepsoncloudscom için haftada 3 gönderiyi (en çok 1 video) kendi kendine hazırlayan, pazartesi ~30 dk'lık onay oturumuyla dönen düzeni 16 Kasım oturumuna hazır, 19 Kasım ilk otomatik koşuya açık hale getirmek.

**Architecture:** Tek doğruluk kaynağı bir markdown kuyruk dosyası (`raporlar/instagram-kuyruk.md`). Küçük bir Python aracı kuyruğu okur, kuralları denetler, tampon/durdurma kararını ve brifing satırını üretir; ikinci bir araç onay kartını (HTML) üretir. Perşembe zamanlanmış görevi ve pazartesi oturum protokolü bu iki aracı çağırır; üretimi mevcut ajanlar (Metin Yazarı, İçerik, Astrid, Denetmen) yapar.

**Tech Stack:** Python 3.9 standart kütüphane (`unittest`, `dataclasses`, `html`, `subprocess`) · macOS `sips` (görsel küçültme) · `ffmpeg` (`~/.local/bin/ffmpeg`, video önizleme) · Higgsfield CLI (`higgsfield account status --json`) · Claude zamanlanmış görevler (`~/.claude/scheduled-tasks/<id>/SKILL.md`) · Artifact (özel sayfa).

**Spec:** `raporlar/tasarim-instagram-haftalik-dongu-2026-11-14.md` (Ayhan onayı, 14 Kas 2026). Uygulayıcı önce onu okur.

## Global Constraints

- Haftada 3 gönderi hedef, **2 taban**, **haftada en çok 1 video** (Reels). Hafta = pazartesi–pazar.
- Video yayın sürümü **1080p**. Görsel 2 kredi, 720p klip 35, 1080p klip 80.
- Görev Higgsfield maddesi başına **en çok 3 deneme karesi**ni onaysız üretebilir; tam üretim yalnız Kararlar tablosunda o madde için `yön onayı` satırı varsa.
- Fox yayınlamaz, zamanlamaz, hiçbir hesaba şifre girmez. Yayın tuşu Ayhan'da.
- Tampon eşikleri: **< 7 gün → DİKKAT, < 3 gün → DUR.**
- Kendini durdurma: bekleyen kart varken **son iki haftada (bu haftanın ve geçen haftanın pazartesisinden bugüne) hiç karar yoksa** görev `DURAKLADI`.
- Revize en çok 2; üçüncüde `park`. Kuyrukta her zaman 2 `yedek` paket.
- Durum dosyası tavanı: **≤ 40 satır ve ≤ 6144 bayt.**
- Paket kökü: `~/Desktop/Steps On Clouds/Design /Instagram/Paketler/` (**"Design " sonunda boşluk var**). YZ ham çıktıları `~/Desktop/Steps On Clouds/Görseller/Yapay Zeka Görselleri/` altında kalır.
- Tüm dosyalar UTF-8; Türkçe glyph (İ, ı, ğ, ş, ö, ç, ü) bozulmadan taşınır.
- Commit: anlamlı Türkçe mesaj + son satır `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Push: `git push origin main`.
- Kütükte "ölçülmedi" yasak; token kesin değilse "~tahmin".

## Review Focus

1. **Paket klasörü yok ya da yol yanlış** ("Design " boşluğu, elle taşınmış klasör) → kart çökmeden o paketi "paket klasörü bulunamadı: <yol>" diye gösterir. → Task 3 testi.
2. **Video önizlemesi Artifact dosya sınırını (15 MB) aşar** → kart, büyük videoyu 720p H.264 önizlemeye çevirir; önizleme 15 MB altında. → Task 3 testi (ffmpeg yoksa atlanır).
3. **Kuyruk dosyası elle düzenlenip bozulur** (eksik sütun, geçersiz tarih, bilinmeyen durum) → `oku()` satır numaralı `KuyrukHatasi` fırlatır; CLI 2 ile çıkar; perşembe görevi üretim yapmadan heartbeat yazar. → Task 1 testi.
4. **Higgsfield bakiyesi okunamaz** (oturum düşmüş) → bakiye `?` olarak yazılır, özet "bakiye bilinmiyor" der, görev yalnız kredisiz paket hazırlar. → Task 1 testi + Task 6 SKILL.md kuralı.
5. **Türkçe büyük harf ve yıl dönümü** — "İLK ADIMI ÖĞRETENE" karta birebir geçer; 28 Ara–3 Oca haftası tek hafta sayılır (ISO W53 karışıklığı yok). → Task 1 ve Task 3 testleri.

---

### Task 1: Kuyruk aracı

**Files:**
- Create: `sablonlar/araclar/instagram_kuyruk.py`
- Create: `sablonlar/araclar/tests/__init__.py` (boş)
- Test: `sablonlar/araclar/tests/test_instagram_kuyruk.py`

**Interfaces:**
- Produces — kuyruk dosya biçimi (Task 2 bunu yazar, Task 6/7 okur):
  ```
  # Instagram Kuyruğu — @stepsoncloudscom
  ## Sayaçlar
  - görev: AKTİF | KURU | DURAKLADI — <sebep>
  - bakiye: <int | ?> (<YYYY-MM-DD>)
  - dönem harcaması: <int>
  ## Slotlar
  | slot | saat | madde | başlık | hat | yol | video | durum | tur | kredi | paket | not |
  ## Kararlar
  | tarih | madde | karar | not |
  ## Heartbeat
  | tarih | mod | özet |
  ```
  `slot` = `YYYY-MM-DD` ya da `—` (yalnız PASIF durumlar: `yedek`, `park`, `çıkarıldı`; başka durumda `—` → `KuyrukHatasi`). `video` = `evet|hayır`. `paket` = paket kökü altındaki klasör adı ya da `—`. `karar` ∈ `onay, revize, çıkar, yön onayı, zamanlandı, havuz evet, havuz hayır`.
- Produces — Python:
  - `DURUMLAR: tuple[str, ...]` = `("havuzda","deneme karelerinde","üretimde","denetimde","onay bekliyor","onaylandı","zamanlandı","yayında","revize","park","çıkarıldı","yedek")`
  - `HAZIR = {"onaylandı","zamanlandı","yayında"}` · `KARTTA = {"onay bekliyor","deneme karelerinde"}` · `PASIF = {"park","çıkarıldı","yedek"}`
  - `@dataclass Slot(tarih: Optional[date], saat: str, madde: str, baslik: str, hat: str, yol: str, video: bool, durum: str, tur: int, kredi: int, paket: str, not_: str)`
  - `@dataclass Kuyruk(gorev: str, sebep: str, bakiye: Optional[int], donem_harcama: int, slotlar: list[Slot], kararlar: list[tuple[date, str, str, str]], heartbeat: list[tuple[date, str, str]])`
  - `class KuyrukHatasi(ValueError)` — mesajı `"satır <n>: <neden>"` içerir
  - `oku(yol: Path) -> Kuyruk`
  - `hafta_baslangici(g: date) -> date` (o haftanın pazartesisi)
  - `tampon_gun(k: Kuyruk, bugun: date) -> int`
  - `tampon_bayrak(gun: int) -> str` → `"DUR" | "DİKKAT" | "TEMİZ"`
  - `durdurulmali(k: Kuyruk, bugun: date) -> bool`
  - `kural_ihlalleri(k: Kuyruk) -> list[str]`
  - `ozet_satiri(k: Kuyruk, bugun: date) -> str`
  - CLI: `python3 sablonlar/araclar/instagram_kuyruk.py {ozet|denetle|durum} [--kuyruk PATH] [--bugun YYYY-MM-DD]` — varsayılan kuyruk `raporlar/instagram-kuyruk.md` (repo köküne göre), varsayılan bugün = sistem tarihi. `denetle`: ihlal yoksa 0, ihlal varsa her birini yazıp 1, okuma hatasında 2. `durum`: `DURAKLAT` ya da `DEVAM` yazar.

- [ ] **Step 1: Testleri yaz** — `test_instagram_kuyruk.py`, `unittest`, her test geçici dosyaya fixture yazar. Fixture: 2026-11-16 pazartesi bugünü; slotlar 19 Kas `onaylandı`, 21 Kas `zamanlandı`, 24 Kas `onay bekliyor`, 26 Kas `deneme karelerinde` video, bir `yedek` (`—` tarihli).
  ```python
  def test_tampon_ilk_hazir_olmayan_slota_kadar(self):
      self.assertEqual(tampon_gun(k, date(2026,11,16)), 8)        # 24 Kas - 16 Kas
  def test_tampon_hepsi_hazirsa_son_slot_arti_bir(self):
      # yalnız 19 ve 21 Kas, ikisi hazır
      self.assertEqual(tampon_gun(k2, date(2026,11,16)), 6)       # (21-16)+1
  def test_tampon_gelecek_slot_yoksa_sifir(self): ...  -> 0
  def test_bayrak_esikleri(self):
      self.assertEqual(tampon_bayrak(2), "DUR"); self.assertEqual(tampon_bayrak(6), "DİKKAT"); self.assertEqual(tampon_bayrak(7), "TEMİZ")
  def test_durdur_iki_hafta_karar_yoksa(self):
      # karar yalnız 2026-11-16; heartbeat 2026-11-12'den beri; bugün 2026-12-03 (perşembe), kartta paket var
      self.assertTrue(durdurulmali(k, date(2026,12,3)))
  def test_durdurma_yok_gecen_hafta_karar_varsa(self):
      self.assertFalse(durdurulmali(k, date(2026,11,26)))         # pencere 16 Kas–26 Kas, 16 Kas kararı içinde
  def test_durdurma_yok_kartta_paket_yoksa(self): ...  -> False
  def test_durdurma_yok_sistem_yeniyse(self):
      # hiç karar yok, ilk heartbeat 2026-11-19, bugün 2026-11-26
      self.assertFalse(durdurulmali(k, date(2026,11,26)))
  def test_ihlal_haftada_iki_video(self):
      # 10 Ara ve 12 Ara ikisi video=evet
      self.assertIn("2026-12-07 haftası: 2 video (en çok 1)", kural_ihlalleri(k))
  def test_ihlal_haftada_tek_gonderi(self):
      self.assertIn("2026-12-14 haftası: 1 gönderi (taban 2)", kural_ihlalleri(k))
  def test_pasifler_sayilmaz(self):  # çıkarıldı + yedek video sayımına ve tabana girmez
  def test_yil_donumu_tek_hafta(self):
      # 2026-12-31 ve 2027-01-02 aynı hafta: 2 gönderi, ihlal yok
      self.assertEqual(kural_ihlalleri(k), [])
  def test_bozuk_tarih_satir_numarasi(self):
      with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: geçersiz tarih"): oku(bozuk)
  def test_bilinmeyen_durum(self):
      with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: bilinmeyen durum"): oku(bozuk2)
  def test_eksik_sutun(self):
      with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: 12 sütun bekleniyor"): oku(bozuk3)
  def test_bakiye_bilinmiyor(self):
      # "- bakiye: ? (2026-11-19)"
      self.assertIsNone(k.bakiye); self.assertIn("bakiye bilinmiyor", ozet_satiri(k, date(2026,11,16)))
  def test_ozet_satiri(self):
      self.assertEqual(ozet_satiri(k, date(2026,11,16)),
          "Instagram: kartta 2 paket · tampon 8 gün (TEMİZ) · kredi bakiye 623, dönem harcaması 0 · görev AKTİF")
  def test_turkce_baslik_korunur(self):
      self.assertEqual(k.slotlar[2].baslik, "İLK ADIMI ÖĞRETENE")
  def test_cli_denetle_cikis_kodlari(self):  # subprocess: temiz → 0, ihlalli → 1, bozuk → 2
  ```
- [ ] **Step 2: Çalıştır, kırıldığını gör** — `cd /Users/ayhanerden/Fox && python3 -m unittest sablonlar.araclar.tests.test_instagram_kuyruk -v` → `ModuleNotFoundError` ya da `ImportError`. (Gerekirse `sablonlar/__init__.py` ve `sablonlar/araclar/__init__.py` boş dosyaları eklenir; mevcut betiklerin doğrudan çalıştırılmasını bozmaz.)
- [ ] **Step 3: `instagram_kuyruk.py`'yi yaz** — markdown tabloları `|` ile bölünür, başlık ve `|---|` satırı atlanır; bölümler `## ` başlığından tanınır. `tampon_gun`: `tarih >= bugun` ve durumu PASIF olmayan slotlar tarihe göre sıralanır; ilk HAZIR-olmayan slotun `(tarih - bugun).days`'i; hepsi hazırsa `(son.tarih - bugun).days + 1`; slot yoksa 0. `durdurulmali`: KARTTA'da slot yoksa False; ilk heartbeat tarihi `hafta_baslangici(bugun) - 7 gün`'den sonraysa False; `[hafta_baslangici(bugun) - 7 gün, bugun]` aralığında karar yoksa True. `kural_ihlalleri`: PASIF olmayan, tarihli slotlar `hafta_baslangici` anahtarıyla gruplanır; ilk ve son hafta arasındaki her hafta kontrol edilir (boş hafta = 0 gönderi ihlali). Mesaj biçimleri testtekiyle birebir.
- [ ] **Step 4: Çalıştır, geçtiğini gör** — aynı komut → tüm testler `OK`.
- [ ] **Step 5: Commit**
  ```bash
  git add sablonlar/araclar/instagram_kuyruk.py sablonlar/araclar/tests/ sablonlar/__init__.py sablonlar/araclar/__init__.py
  git commit -m "Instagram kuyruk aracı: tampon, durdurma, kural denetimi, brifing satırı (+testler)"
  ```

### Task 2: Kuyruk dosyası (ilk havuz)

**Files:**
- Create: `raporlar/instagram-kuyruk.md`

**Interfaces:**
- Consumes: Task 1 dosya biçimi ve CLI.
- Produces: Task 6/7/8'in okuduğu kuyruk.

- [ ] **Step 1: Dosyayı yaz.** Sayaçlar: `görev: KURU — kuru koşu bekleniyor` · `bakiye: 623 (2026-11-14)` (`higgsfield account status --json` ile o an yeniden oku) · `dönem harcaması: 0`. Slotlar (saat hepsi `19:00`, tur 0, kredi 0, paket `—`, durum `havuzda` aksi yazılmadıkça; başlık/hat/yol v5 §4'ten):

  | slot | madde | yol | video |  | slot | madde | yol | video |
  |---|---|---|---|---|---|---|---|---|
  | 2026-11-19 | 01 | arşiv | hayır | | 2026-12-12 | 12 | gerçek çekim | evet |
  | 2026-11-21 | 02 | arşiv | hayır | | 2026-12-15 | 13 | tipografik | hayır |
  | 2026-11-22 | 03 | arşiv | hayır | | 2026-12-17 | 14 | arşiv | hayır |
  | 2026-11-24 | 04 | Higgsfield | hayır | | 2026-12-19 | 10 | Higgsfield | evet |
  | 2026-11-26 | 05 | Higgsfield | evet | | 2026-12-21 | 16 | Higgsfield | evet |
  | 2026-11-28 | 06 | Higgsfield | hayır | | 2026-12-23 | 17 | davetli | hayır |
  | 2026-12-02 | 07 | tipografik | hayır | | 2026-12-25 | 18 | Higgsfield | hayır |
  | 2026-12-03 | 08 | gerçek çekim | evet | | 2026-12-29 | 19 | arşiv | hayır |
  | 2026-12-06 | 09 | arşiv | hayır | | 2026-12-31 | 20 | Higgsfield | hayır |
  | 2026-12-10 | 11 | orijinal+tipografik | hayır | | — | 15 | Higgsfield | evet |

  15'in durumu `çıkarıldı`, notu `haftada 1 video — 10 bu slota taşındı (tasarım §6)`. 10'un notu `v5'te 8 Ara idi`. İsteğe bağlı maddelerin (03, 09, 17, 19, 20) notuna `İ — 16 Kas havuz onayına bağlı`. Kararlar boş; Heartbeat'e `2026-11-14 | kurulum | kuyruk oluşturuldu`.
- [ ] **Step 2: Doğrula** — `python3 sablonlar/araclar/instagram_kuyruk.py denetle` → çıkış 0, çıktı yok. `python3 sablonlar/araclar/instagram_kuyruk.py ozet --bugun 2026-11-16` → `Instagram: kartta 0 paket · tampon 3 gün (DİKKAT) · kredi bakiye 623, dönem harcaması 0 · görev KURU`.
- [ ] **Step 3: Commit** — `git add raporlar/instagram-kuyruk.md && git commit -m "Instagram kuyruğu: v5 havuzu haftada-1-video kuralına göre dizildi"`

### Task 3: Onay kartı üretici

**Files:**
- Create: `sablonlar/araclar/instagram_onay_karti.py`
- Test: `sablonlar/araclar/tests/test_instagram_onay_karti.py`

**Interfaces:**
- Consumes: `oku`, `Kuyruk`, `Slot`, `KARTTA` (Task 1).
- Produces:
  - `PAKET_KOKU = Path.home() / "Desktop" / "Steps On Clouds" / "Design " / "Instagram" / "Paketler"`
  - `kart_uret(k: Kuyruk, cikti: Path, paket_koku: Path = PAKET_KOKU, video_esik_bayt: int = 14 * 1024 * 1024) -> Path` → `cikti/index.html` yolunu döndürür; medya `cikti/medya/<madde>/` altına.
  - CLI: `python3 sablonlar/araclar/instagram_onay_karti.py <cikti_dizini> [--kuyruk PATH] [--paket-koku PATH]` → index.html yolunu yazar.
- Paket klasörü sözleşmesi (Task 6/8 üretir): görseller `*.jpg|*.jpeg|*.png|*.webp`, videolar `*.mp4|*.mov`, metin `metin.md`, isteğe bağlı `denetmen.md`, isteğe bağlı `yon-karti.md` (deneme aşaması).

- [ ] **Step 1: Testleri yaz** (`unittest`, geçici dizinde sahte paket kökü; PNG'yi `sips -s format png` ile 1×1 TIFF'ten ya da sabit 67 baytlık geçerli PNG baytlarından üret):
  ```python
  def test_kartta_yalniz_bekleyenler(self):   # onay bekliyor + deneme karelerinde var, onaylandı yok
  def test_baslik_ve_metin_birebir(self):
      self.assertIn("İLK ADIMI ÖĞRETENE", html); self.assertIn("&lt;b&gt;", html)   # metin.md'deki "<b>" kaçışlı
  def test_gorsel_kopyalanir_ve_baglanir(self):
      self.assertTrue((cikti/"medya"/"04"/"kare1.png").exists()); self.assertIn('src="medya/04/kare1.png"', html)
  def test_asama_etiketi(self):
      self.assertIn("Yön onayı", html_deneme); self.assertIn("Yayın onayı", html_onay)
  def test_kredi_ve_denetmen_notu(self):     # slot.kredi ve denetmen.md içeriği sayfada
  def test_eksik_klasor_cokmez(self):
      self.assertIn("paket klasörü bulunamadı", html)
  @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg yok")
  def test_buyuk_video_onizlemeye_cevrilir(self):
      # ffmpeg -f lavfi -i testsrc=size=1920x1080:rate=30 -t 3 ile mp4 üret; eşiği testte 1 bayta indir (parametre)
      self.assertTrue(onizleme.exists()); self.assertLess(onizleme.stat().st_size, 15*1024*1024)
  def test_html_tema_ve_baslik(self):
      self.assertIn("<title>Instagram Onay Kartı</title>", html); self.assertIn("prefers-color-scheme: dark", html)
  ```
- [ ] **Step 2: Çalıştır, kırıldığını gör** — `python3 -m unittest sablonlar.araclar.tests.test_instagram_onay_karti -v` → ImportError.
- [ ] **Step 3: `instagram_onay_karti.py`'yi yaz** — görseller `sips -Z 1600 <kaynak> --out <hedef>` ile kopyalanır; videolar `video_esik_bayt` (varsayılan 14 MB) üstündeyse `ffmpeg -y -i <kaynak> -vf scale=-2:720 -c:v libx264 -crf 28 -preset veryfast -an <hedef>.mp4`, altındaysa düz kopya; ffmpeg yoksa video yerine yol yazılır. Her paket bir bölüm: madde, slot tarihi+saat, başlık, aşama ("Yön onayı" deneme karelerinde / "Yayın onayı" onay bekliyor), kredi, medya, `metin.md` (`html.escape`, `<pre>`), `yon-karti.md`, `denetmen.md`, en altta "Karar: Onay · Revize (not) · Çıkar — oturumda söyle". Sayfa: `<title>Instagram Onay Kartı</title>`, `:root` renk değişkenleri + `@media (prefers-color-scheme: dark)` (`:root:not([data-theme="light"])` ve `:root[data-theme="dark"]` korumalı), `body` arka planı açık, 16px yan boşluk, telefonda tek sütun, harici script yok.
- [ ] **Step 4: Çalıştır, geçtiğini gör** — aynı komut → `OK` (ffmpeg testi çalışmış olmalı: ffmpeg `~/.local/bin`'de var).
- [ ] **Step 5: Commit** — `git add sablonlar/araclar/instagram_onay_karti.py sablonlar/araclar/tests/test_instagram_onay_karti.py && git commit -m "Instagram onay kartı üretici (+testler)"`

### Task 4: Durum dosyası kapısı

**Files:**
- Create: `.claude/hooks/fox-durum-boyut.sh`
- Modify: `.claude/settings.json` (SessionStart komutu)
- Modify: `fox-durum.md` (yeniden yazım), `raporlar/oturum-gunlugu.md` (taşınan ayrıntı en üste, tarihli)

**Interfaces:**
- Produces: `fox-durum-boyut.sh <dosya>` — dosya 6144 baytı aşarsa tek satır `⚠️ fox-durum.md <N> bayt — tavan 6144 bayt, oturum başında kesiliyor. Ayrıntıyı raporlar/oturum-gunlugu.md'ye indir.` yazar; aşmıyorsa hiçbir şey yazmaz; her durumda 0 ile çıkar.

- [ ] **Step 1: Kırıldığını gör** — `head -c 7000 /dev/zero | tr '\0' 'a' > "$TMPDIR/b.md"; bash .claude/hooks/fox-durum-boyut.sh "$TMPDIR/b.md"` → "No such file".
- [ ] **Step 2: Betiği yaz** (`stat -f %z`, `set -u`, çalıştırılabilir).
- [ ] **Step 3: Doğrula** — 7000 baytlık dosyada çıktı `⚠️ fox-durum.md 7000 bayt — tavan 6144 bayt` ile başlar; 6144 baytlık dosyada çıktı boş (sınır dahil); 100 baytlık dosyada çıktı boş; ikisinde de `echo $?` → 0.
- [ ] **Step 4: SessionStart komutuna bağla** — `.claude/settings.json`'daki komutta `echo '=== FOX HAFIZA ...'`'dan **önce** `bash /Users/ayhanerden/Fox/.claude/hooks/fox-durum-boyut.sh /Users/ayhanerden/Fox/fox-durum.md;` eklenir (uyarı çıktının en başında kalır). `python3 -m json.tool .claude/settings.json` hatasız.
- [ ] **Step 5: `fox-durum.md`'yi yeniden yaz** — aynı başlıklar (AKTİF CEPHELER / AYHAN'DA BEKLEYENLER / RİSK BAYRAKLARI / DETAY HARİTASI / SÜREKLİLİK), her cephe tek satır, hücre başına en çok ~200 karakter; çıkan ayrıntı `raporlar/oturum-gunlugu.md`'nin başına "14 Kas — durum dosyasından taşınan ayrıntı" başlığıyla, **hiçbir bilgi silinmeden**. Yeni cephe satırı: `**SoC Instagram — haftalık döngü** | Tasarım onaylı (14 Kas), kurulum sürüyor · kuyruk: raporlar/instagram-kuyruk.md · pazartesi protokolü: sablonlar/instagram-pazartesi-oturumu.md | 16 Kas ilk oturum: K0/K4/K8/K10 + havuz onayı + T0 Insights | Ayhan`. Tarihi geçmiş satırlar (ör. "Editör günü Pzt 9 Kas") güncel durumla değişir.
- [ ] **Step 6: Doğrula** — `wc -l fox-durum.md` ≤ 40, `wc -c fox-durum.md` ≤ 6144, `bash .claude/hooks/fox-durum-boyut.sh fox-durum.md` çıktısı boş. Eski dosyadaki her cephe adı yeni dosyada ya da günlükte geçiyor (`grep` ile: Özgür Irmak, Steps On Clouds, Claudia, Ecem Yaşar, Red Lions, Park, S11, GBP, GA4).
- [ ] **Step 7: Commit** — `git add -A .claude/hooks/fox-durum-boyut.sh .claude/settings.json fox-durum.md raporlar/oturum-gunlugu.md && git commit -m "Durum dosyası 6 KB kapısı: boyut uyarısı hook'a bağlandı, dosya 40 satır / 6 KB'a indi"`

### Task 5: Kararlar, Nakit Motoru, hafıza ve pazartesi protokolü

**Files:**
- Create: `sablonlar/instagram-pazartesi-oturumu.md`
- Modify: `fox-karar-gunlugu.md` (en üste 14 Kas girdisi)
- Modify: `~/.claude/projects/-Users-ayhanerden-Fox/memory/kredi-harcayan-uretim-ayhan-yapar.md`
- Create: `~/.claude/projects/-Users-ayhanerden-Fox/memory/instagram-haftalik-dongu.md` + `MEMORY.md` pointer
- Zamanlanmış görev: `nakit-motoru-gunluk-kosu` → `enabled: false`

**Interfaces:**
- Consumes: Task 1 CLI, Task 3 CLI.
- Produces: pazartesi protokolü (Task 7 brifingi ve gelecek Fox oturumları buna yönlendirir).

- [ ] **Step 1: Nakit Motoru'nu duraklat** — `mcp__scheduled-tasks__update_scheduled_task` (`taskId: nakit-motoru-gunluk-kosu`, `enabled: false`). Doğrula: `list_scheduled_tasks` çıktısında `"enabled": false`.
- [ ] **Step 2: Pazartesi protokolünü yaz** — Ayhan "Instagram" dediğinde sırayla: (1) `git pull`; (2) `instagram_kuyruk.py ozet` + `denetle`; heartbeat'te bu haftanın perşembesine ait satır yoksa hazırlığı **oturumda** zamanlanmış görevin adımlarıyla yap (kaçan koşu); (3) `instagram_onay_karti.py <scratchpad>/instagram-kart` → Artifact yayınla (aynı dosya yolu her hafta, böylece aynı URL) → aç; (4) her paket için Ayhan'ın kararını Kararlar tablosuna tarihle yaz ve durumu güncelle (`onay`→`onaylandı`, `revize`→`revize` + tur+1, 3. revizede `park`, `çıkar`→`çıkarıldı`, deneme kartında onay → `yön onayı` kararı + durum `üretimde`); (5) Ayhan zamanladıkça `zamanlandı`; (6) ayın ilk pazartesisi: havuz önerisi (`raporlar/instagram-havuz-YYYY-MM.md`) onayı + Insights ekranları — **istisna, ilk oturum 16 Kas:** K0 / K4 / K8 / K10 kararları + v5 listesinin havuz onayı (20 madde evet/hayır, Denetmen'in 12 madde önerisi ve 09 dahil; `havuz evet|havuz hayır` kararı, `hayır` olan `çıkarıldı`) + T0 Insights ekranları (v5 §6); (7) oturumun gerçek süresini heartbeat'e yaz (ilk dört pazartesi); (8) `denetle` 0 → commit + push.
- [ ] **Step 3: Karar günlüğüne yaz** — "14 Kas 2026 — Instagram haftalık döngü": Ayhan'ın 8 kararı (tasarım §2 tablosu, sözcükleri aynen), Nakit Motoru duraklatması ve gerekçesi, kredi istisnası, tasarım ve plan yolları.
- [ ] **Step 4: Hafızayı güncelle** — `kredi-harcayan-uretim-ayhan-yapar.md`'yi oku, gövdeye istisna ekle: "İstisna (14 Kas 2026, Ayhan): Instagram haftalık döngüsünde görev, Higgsfield maddesi başına en çok 3 deneme karesini onaysız üretebilir; tam üretim yalnız kartta maliyeti yazılı yön onayından sonra. Başka işe geçmez." Yeni memory `instagram-haftalik-dongu.md` (type: project): "Ayhan 'Instagram' dediğinde `sablonlar/instagram-pazartesi-oturumu.md` izlenir; kuyruk `raporlar/instagram-kuyruk.md`; perşembe 10:00 görevi `instagram-haftalik-hazirlik`." `MEMORY.md`'ye iki satır pointer (yeni dosya + mevcut kredi satırının açıklamasına "(Instagram istisnası var)").
- [ ] **Step 5: Commit** — `git add sablonlar/instagram-pazartesi-oturumu.md fox-karar-gunlugu.md && git commit -m "Instagram pazartesi protokolü; karar günlüğü 14 Kas; Nakit Motoru duraklatıldı"`

### Task 6: Perşembe zamanlanmış görevi + kuru koşu

**Files:**
- Create (tool ile): `~/.claude/scheduled-tasks/instagram-haftalik-hazirlik/SKILL.md`
- Modify: `raporlar/instagram-kuyruk.md` (heartbeat, görev modu)

**Interfaces:**
- Consumes: Task 1 CLI (`durum`, `denetle`), Task 2 kuyruk, Task 3 paket klasörü sözleşmesi, Task 5 hafıza istisnası.
- Produces: her perşembe güncellenmiş kuyruk + paket klasörleri + heartbeat + kütük satırları.

- [ ] **Step 1: Görevi oluştur** — `mcp__scheduled-tasks__create_scheduled_task`, `taskId: instagram-haftalik-hazirlik`, cron `0 10 * * 4`, açıklama "Perşembe 10:00 — Instagram haftalık hazırlık (kuyruk → paketler → Denetmen), yayın yok". SKILL.md'nin bağlayıcı içeriği (uygulayıcı düzyazıyla yazar, sıra bu):
  1. Fox kimliği; CLAUDE.md, tasarım belgesi ve kuyruk okunur. `git pull --ff-only`.
  2. `higgsfield account status --json` → `credits` sayacına `bakiye: N (tarih)`; komut başarısızsa `bakiye: ? (tarih)` ve bu koşuda **Higgsfield adımı yok**.
  3. Görev `KURU` ise: yalnız araç kontrolü — Agent aracıyla Denetmen'e tek cümlelik "erişim testi" çağrısı, Higgsfield bakiye okuması, `instagram_kuyruk.py denetle`. Heartbeat'e `KURU — Agent: var/yok · Higgsfield: N/okunamadı · denetle: 0/1/2`. Üretim yok, kredi yok. Commit+push, çık.
  4. `denetle` 2 dönerse: üretim yok, heartbeat `HATA — kuyruk okunamadı: <mesaj>`, commit+push, çık.
  5. `durum` `DURAKLAT` derse: sayaç `görev: DURAKLADI — 2 hafta kararsız kart`, heartbeat, commit+push, çık. Kararlar'da yeni satır görülürse sayaç yeniden `AKTİF`.
  6. Geçmiş tarihli `zamanlandı` slotlar → `yayında` (notuna "Meta zamanlaması, doğrulanmadı"); her biri için `raporlar/teslim-kutugu.md`'ye satır.
  7. Pencereler (bugün = perşembe *d*): **W** = [d+11, d+17], **W+1** = [d+18, d+24]. W'deki arşiv/tipografik/orijinal maddeler → paket hazırla. W'deki Higgsfield maddelerinden Kararlar'da `yön onayı` olanlar → tam üretim (görseller, video 1080p); maliyeti bakiyeyi aşıyorsa üretme, nota yaz, slotu yedekten doldur. W+1'deki Higgsfield maddeleri → **en çok 3 deneme karesi** + `yon-karti.md` (5 satır: çizgi / styling / kadraj / referans markalar / ne DEĞİL) + tam üretim maliyeti → durum `deneme karelerinde`. Gerçek çekim maddeleri → çekim listesi `yon-karti.md`'ye, durum `onay bekliyor`. Revize kararı almış maddeler → notu işle, tur+1.
  8. Üretim zinciri her pakette: Metin Yazarı (metin.md) → İçerik Ajanı ya da Astrid → render, gözle denetim → Denetmen (`denetmen.md`; DUR → `revize`, karta çıkmaz). Paket klasörü `PAKET_KOKU/<slot>_<madde>/`; YZ ham çıktısı `Yapay Zeka Görselleri` altında.
  9. `yedek` sayısı 2'nin altındaysa kredisiz yedek paket hazırla (arşiv/tipografik, Red Lions yalnız SoC görünen).
  10. Ayın son perşembesiyse `raporlar/instagram-havuz-YYYY-MM.md` (12–13 madde, en çok haftada 1 video).
  11. Sayaçları güncelle; `denetle` 0 olmalı (1 ise ihlali nota yaz, slotları düzelt); heartbeat `AKTİF — <hazırlanan> paket, <deneme> deneme, <kredi> kredi, ~<token> token`; commit + push; push başarısızsa heartbeat'e yaz.
  12. Yasaklar: yayın/zamanlama yok; Higgsfield madde başına deneme karesi > 3 yok; yön onayı olmadan tam üretim yok; v5 §2.1 görsel kuralları; acıma/ilham dili, "protez uyumlu", uydurma rakam yok.
- [ ] **Step 2: 1080p yükseltme yolunu kontrol et** (tasarım §7.4 riski) — `higgsfield model list --video --json` ve `higgsfield workflow list --json` çıktısında var olan bir klibi yükselten (upscale) model/iş akışı aranır. Varsa adı ve kredi maliyeti (`higgsfield generate cost`) SKILL.md adım 7'ye "onaylı 720p klip → bu yolla 1080p" diye yazılır; yoksa "1080p yeniden üretim yeni aday sayılır, yayın onayında 720p ile yan yana" yazılır. Sonuç kuyruk heartbeat'ine bir satır.
- [ ] **Step 3: Kuru koşu** — `mcp__scheduled-tasks__run_scheduled_task` (`instagram-haftalik-hazirlik`). Bittiğinde `git pull` ve kuyruğun Heartbeat'inde `KURU — Agent: var · Higgsfield: <sayı> · denetle: 0` satırı aranır. `Agent: yok` çıkarsa SKILL.md'ye tasarım §10'daki sapma kuralı yazılır (görev yalnız kredisiz paket; Higgsfield adımları pazartesi oturumunda) ve Ayhan'a bildirilir.
- [ ] **Step 4: Commit** — kuru koşunun kendi commit'i yeterli; yoksa `git add raporlar/instagram-kuyruk.md && git commit -m "Instagram görevi kuru koşu sonucu"`.

### Task 7: Sabah brifingi entegrasyonu

**Files:**
- Modify: `~/.claude/scheduled-tasks/morning-brief/SKILL.md` (PART A.0 — Komuta Kartı, "Cephe Tek-Bakış" maddesi)

**Interfaces:**
- Consumes: `instagram_kuyruk.py ozet` (Task 1).

- [ ] **Step 1: Ekle** — "Cephe Tek-Bakış"a: `cd /Users/ayhanerden/Fox && python3 sablonlar/araclar/instagram_kuyruk.py ozet` çıktısını satır olarak koy; çıktıda `(DİKKAT)` ya da `(DUR)` veya `görev DURAKLADI` varsa "Bugünün 3 Hamlesi"ne Instagram hamlesi (DUR'da yedek havuzdan acil doldurma önerisiyle); pazartesiyse "Bugün Instagram oturumu (~30 dk) — Fox'a 'Instagram' de" satırı. Komut hata verirse satır "Instagram: kuyruk okunamadı — <mesaj>".
- [ ] **Step 2: Doğrula** — komutu elle çalıştır, tek satır döndüğünü gör; SKILL.md'de yeni metnin PART A.0 içinde olduğunu `grep -n "instagram_kuyruk.py ozet"` ile gör.

### Task 8: Başlangıç paketleri (Hafta 1–2) ve kart provası

**Files:**
- Create: `PAKET_KOKU/2026-11-19_01/`, `…/2026-11-21_02/`, `…/2026-11-22_03/`, `…/2026-11-24_04/`, `…/2026-11-26_05/`, `…/2026-11-28_06/`
- Modify: `raporlar/instagram-kuyruk.md` (durumlar, tur, kredi, paket)

**Interfaces:**
- Consumes: Task 3 paket sözleşmesi ve kart CLI, Task 2 kuyruk.

- [ ] **Step 1: Paketleri hazırla** — v5 §4 Hafta 1–2 tanımlarıyla: 01, 02, 03 arşiv (`Steps On Mela` kareleri v5'te dosya adlarıyla yazılı; 02'nin tipografi karesi Bebas Neue + Comfortaa, marka renkleri); 04 ve 06 14 Kas aday karelerinden (`Görseller/Yapay Zeka Görselleri/Instagram 2026-11_12/`); 05 = **yön onayı paketi**: onaylı 720p klipler (bank, kort kapısı + v5'teki üçüncü plan) + `yon-karti.md` + 1080p tam üretim maliyeti (3 klip × 80 = 240). Zincir: Metin Yazarı → İçerik → render + gözle → Denetmen. **Kredi harcanmaz** (yeni üretim yok).
- [ ] **Step 2: Kuyruğu güncelle** — 01–04 ve 06 `onay bekliyor`, 05 `deneme karelerinde`; `paket` sütunları dolu; `denetle` → 0.
- [ ] **Step 3: Kart provası** — `python3 sablonlar/araclar/instagram_onay_karti.py <scratchpad>/instagram-kart` → Artifact olarak yayınla (artifact-design becerisi yüklenir), tarayıcıda telefon genişliğinde (375 px) ve masaüstünde ekran görüntüsüyle gözle bak: Türkçe glyph, görsel/video oynuyor, metin okunuyor. `ozet --bugun 2026-11-16` → `kartta 6 paket`.
- [ ] **Step 4: Commit** — `git add raporlar/instagram-kuyruk.md && git commit -m "Instagram başlangıç paketleri (Hafta 1–2) karta hazır"`

### Task 9: Kapanış

**Files:**
- Modify: `raporlar/instagram-kuyruk.md` (görev `AKTİF`), `raporlar/teslim-kutugu.md`, `fox-durum.md`

- [ ] **Step 1: Görevi aç** — kuru koşu `Agent: var` ve `denetle: 0` verdiyse sayaç `görev: AKTİF`.
- [ ] **Step 2: Kütük** — tek satır: "2026-11-14 · Instagram haftalık döngü — tasarım + kurulum" · tur sayısı · Denetmen: bu kurulumda çağrılmadı ya da çağrıldıysa kararı · Ayhan: tasarım onayı ("Onaylıyorum") · red sebebi (yoksa "yok — red olmadı"; Ayhan'ın 4 düzeltmesi: sıklık 3, 1080p, deneme izni, haftada 1 video) · token (~tahmin) · kredi 0.
- [ ] **Step 3: Tam test** — `python3 -m unittest discover -s sablonlar/araclar/tests -v` → OK; `instagram_kuyruk.py denetle` → 0; `fox-durum-boyut.sh fox-durum.md` → boş.
- [ ] **Step 4: Commit + push** — `git add -A && git commit -m "Instagram haftalık döngü kuruldu: görev AKTİF, kütük işlendi" && git push origin main`.
