# Red Lions — Web Sitesi Tasarım Belgesi v0.1

**Tarih:** 5 Kasım 2026 · **Hazırlayan:** Fox · **Onay:** Ayhan (bekliyor)
**Kaynaklar:** `raporlar/redlions-web-referans-taramasi-v01.md` (referans taraması) · memory: `redlions-sailing-projesi`, `redlions-kesif-sorgusu-cevaplari`, `redlions-sponsorluk-modeli`, `redlions-web-sitesi-plani`
**Prototip:** `.superpowers/brainstorm/6517-1793899629/content/sponsor-simulator-spike-v2.html` (atılabilir; yalnız fikir referansı)

İşaretler: **[Ayhan]** = Ayhan'ın kararı · **[Fox]** = Fox'un kararı, itiraz edilebilir · **[Açık]** = henüz karar yok.

---

## 1 · Niyet

Red Lions, tamamen engelli sporculardan kurulu bir yat yarış takımı. Site iki kişiye aynı anda konuşuyor:

1. **Yeni engelli olmuş biri:** akranlarını yarışırken görüp "bu teknede benim de yerim var" diyebilmeli.
2. **Bir marka yöneticisi:** "bu bir yarış takımı, buna adımı koyarım" diyebilmeli.

İkisinin de ilk hissetmesi gereken şey aynı: **burası gerçek bir yarış takımı.** Ayrım ilk ekranın altında başlıyor ("Takıma katıl" / "Destek ol"). [Ayhan]

"İlham" bu sitede "ne cesurlar" demek değil. Akranını yarışırken görüp "ben de yapabilirim" demek. Acıma ve ilham pornosu yasak (CLAUDE.md §9).

## 2 · Hedefler · Hedef olmayanlar · Başarısızlık sayılanlar

**Hedefler**
- Engelli sporcu başvurusu almak (form → Ayhan).
- Marka iletişim talebi almak (paket seçili form → Ayhan).
- Bireylerin takım ürünleri satın alarak destek olabilmesi (Shop; şimdilik şablon).
- Uluslararası sponsor için İngilizce sürüm.

**Hedef olmayanlar**
- Bağış toplamak. Site bir vakıf ya da STK sitesi değil; "Donate" yok.
- Haber sitesi olmak. Haber akışı ana sayfanın merkezinde değil.
- Fiyat yayınlamak.

**Başarısızlık sayılanlar** (teknik olarak çalışsa bile)
- Herhangi bir sporcunun "nasıl engelli oldu" hikâyesinin sitede yer alması.
- Acıma diliyle yazılmış metin ("engellerine rağmen", "ilham veren mücadele").
- Sponsorun sitenin yarış takımı mı yardım kuruluşu mu olduğunu anlayamaması.
- KVKK rızası olmadan sağlık verisi (engel bilgisi) toplanması ya da yayınlanması.

## 3 · Kısıtlar (pazarlıksız)

1. **Altın kural (Hüseyin, 7 yıl):** bireysel engellilik hikâyesi asla kullanılmaz. Sporcular başarı ve görevleriyle gösterilir. Formlarda "nasıl oldu" alanı yok.
2. **Sporcu kartında engel durumu görünür** [Ayhan, 2 Kas]: sınıflandırma bilgisi olarak ("sağ bacak diz üstü ampute"). **Yayın ön koşulu:** her sporcudan yazılı açık rıza (KVKK özel nitelikli veri) + Muhammed Sıraç Gündür (11 yaş) için veli rızası. Rıza toplanmadan kart canlıya çıkmaz; o sporcunun kartı rıza gelene kadar yalnız isim + görev ile kalır. [Fox]
3. **Fiyat yok** [Ayhan, 26 Eki kararının siteye uzantısı].
4. **Misafir Sporcu Kontenjanı yalnız Ana Sponsor paketinde** [Ayhan, 26 Eki].
5. **Kareleri Ayhan seçer.** Fox fotoğraf/video seçmez; yer tutucu koyar. Arşiv: `~/Desktop/Steps On Clouds/Clients/RedLions/` (TYF 2026 profesyonel 254 foto + 13 video; telefon; MIYC 360°; Kurumsal).
6. **Başka takımların mürettebatı/yüzü sitede yer almaz** (arşivdeki filo karelerinde var). Atmosfer karesi olarak uzak filo görüntüsü kullanılabilir. [Fox]
7. **Ödeme bağlamak Kademe 3:** Fox ödeme hesabı kurmaz/bağlamaz, Ayhan veya Hüseyin yapar. O zamana kadar Shop'ta satın alma kapalı.
8. **Fox Wix'e şifre girmez.** Ayhan oturumu açar; Fox editör erişimiyle veya Wix araçlarıyla çalışır (memory: `steps-on-clouds-wix-site`, `wix-sayfa-menu-api-yok`).
9. **Alan adı:** Ayhan sonra halledecek [Ayhan]. Not: takımın kendi hesabına, otomatik yenilemeli alınmalı (referans taramasındaki düşmüş alan adı dersi).

## 4 · Platform ve yapım

- **Wix, görsel editörle kurulan site** [Fox]. Gerekçe: ince ayarı Ayhan editörde yapacak [Ayhan: "sen kur, ben ince ayara bakarım"]. Kodla yüklenen (headless/deploy) bir site Ayhan'ın editörde düzenlemesine izin vermez.
- **Diller:** TR (ana) + EN [Fox]. Wix Multilingual.
- **Renkler:** logodan — kırmızı `#d7262e` (yaklaşık, logodan ölçülmeli), lacivert `#0d1b3a`, beyaz, kum `#f4f1ec` ara zemin [Fox]. Logo: `Kurumsal/` klasöründen.
- **Tipografi:** kalın, büyük harf, kondanse başlık + sade grotesk gövde [Fox]. Türkçe glyph kontrolü (İ, ğ, ş) zorunlu.

## 5 · Site haritası

| Menü | Sayfa | Durum |
|---|---|---|
| — | Ana sayfa | §6 [Ayhan onayladı] |
| Takım | Kadro + Hüseyin + "biz kimiz" uzun hâli | §7 [Fox] |
| Yarışlar | Takvim + sonuçlar | §7 [Fox] |
| Takıma katıl | Sporcu başvuru formu + kısa açıklama | §8 [Ayhan] |
| Destek ol | Markalar (paketler + simülatör + form) · Bireyler (→ Shop) | §9 [Ayhan] |
| Shop | Takım ürünleri, şablon | §10 [Ayhan] |
| Alt menü | Basın kiti · Instagram · İletişim · KVKK/Gizlilik · TR/EN | §7 [Fox] |

Not: Referans taramasındaki "Akademi" sayfası bu sürümde **"Takıma katıl"** olarak sadeleşti — başvuru kapısı. Eğitim programı anlatısı istenirse sonra genişler. [Fox]

## 6 · Ana sayfa [Ayhan onayladı, 5 Kas]

Yukarıdan aşağı:

1. **Hero — sinematik video (yön A)** [Ayhan]. Tam ekran, sessiz döngü, 10-15 sn, drone + yarış klipleri (Ayhan seçer). Üzerinde tek cümle (yer tutucu: "Tamamen engelli bir yarış takımı.") + iki buton: **Takıma katıl** (kırmızı) / **Destek ol** (çerçeveli). Risk: filoda Red Lions kaybolur → döngünün son saniyeleri Red Lions teknesine yaklaşmalı [Fox önerisi]. Mobilde video yerine durağan kare (Wix'in mobil video davranışına göre). [Fox]
2. **Sonuç bandı** (kırmızı): TYF 2026 Türkiye Yat Şampiyonası · Marmaris · Kategori 1.
3. **Biz kimiz:** başlık + 2-3 cümle. Kaynak: keşif S1 ("sakatların denizde işi yok" cevabı), S2 ("tekne kararlarını sporcu verir"), %100 engelli kadro kararı. Metni Metin Yazarı ajanı yazar, Denetmen'den geçer.
4. **Kadro şeridi:** 4 kart (foto + isim + görev; ikinci satır şehir + engel durumu) + "Tüm kadro →".
5. **2027 takvimi:** Ocak — MIYC Kış Trofesi · Eylül — Kinidos Cup · Ekim — Marmaris Uluslararası Yarış Haftası.
6. **İki kapı** (lacivert zemin): "Bu teknede senin de yerin var" → Takıma katıl · "Adını bir yarış takımına koy" → Destek ol.
7. **Partnerler, kademeli:** kademe adları §9'daki paketlerle aynı. Mevcut sponsorların hangi kademede gösterileceği **[Açık]**: Netsel Marina, Seajet, Raymarine, Alutek Metal, Joyful Yachting, Eternal Sailing, Acarkent Rotary, Steps On Clouds.
8. **Alt bilgi.**

Görsel referans: `.superpowers/brainstorm/62615-1793702158/content/anasayfa-akis.html`.

## 7 · Diğer sayfalar [Fox — konuşulmadı, varsayılan]

- **Takım:** "Biz kimiz" uzun hâli (misyon/vizyon, değerler: özgüven, cesaret, güven, açıklık) · Hüseyin Akbulut genişletilmiş kartı (başarı listesi memory'de) · 10 sporcu kartı (SailGP kalıbı). Veri: memory `redlions-sponsorluk-modeli` §Takım Üyeleri.
- **Yarışlar:** 2027 takvimi + geçmiş sonuçlar (TYF 2026 kategori 1.; Hüseyin'in kişisel başarıları Takım sayfasında kalır).
- **Basın kiti** (alt menü): onaylı görseller + kısa takım bilgisi + basın için not: "Sporcularımız başarılarıyla konuşulur; bireysel sağlık geçmişi sorulmaz/yazılmaz." İndirilebilir dosya Ayhan hazırlar.
- **KVKK / Gizlilik / Aydınlatma metni:** formlar sağlık verisi topladığı için zorunlu. Taslak Fox, son okuma avukat.

## 8 · Sporcu Başvuru Formu [Ayhan, 5 Kas]

Sayfa: **Takıma katıl.** Kısa giriş (1-2 cümle, acıma yok) + form.

| Alan | Tip | Zorunlu |
|---|---|---|
| Ad | metin | ✓ |
| Soyad | metin | ✓ |
| Yaş | sayı | ✓ |
| Şehir | metin | ✓ |
| Telefon | telefon | ✓ |
| E-posta | e-posta | ✓ |
| Engel bilgisi | serbest metin (örn. "sol bacak diz altı ampute") | ✓ |
| Engel derecesi | metin/yüzde — tahmin: sağlık kurulu raporu oranı, Ayhan düzeltmedi | ✓ [Fox: zorunlu] |
| Spor geçmişi | serbest metin | — (isteğe bağlı) [Ayhan + Fox] |
| Acil durum kişisi — ad soyad | metin | ✓ |
| Acil durum kişisi — yakınlık | metin | ✓ |
| Acil durum kişisi — telefon | telefon | ✓ |
| **Yaş < 18 ise:** Veli ad soyad | metin | ✓ (koşullu) |
| **Yaş < 18 ise:** Veli telefonu | telefon | ✓ (koşullu) |
| **Yaş < 18 ise:** Veli onay kutusu | onay | ✓ (koşullu) |
| KVKK açık rıza + aydınlatma metni linki | onay | ✓ |

- **Yok:** "Nasıl oldu?" ya da benzeri hiçbir alan.
- **Alıcı:** Ayhan [Ayhan]. Bildirim e-postası Ayhan'ın adresine. Başvurular Wix panelinde (Forms) saklanır.
- **Gönderim sonrası mesaj:** kısa, sıcak, net ("Başvurunu aldık. Seni arayacağız.") — Metin Yazarı.

## 9 · Destek ol [Ayhan, 5 Kas]

Menü adı **Destek ol**. İki bölüm:

### 9.1 Markalar
1. Kısa giriş (1-2 cümle).
2. **Sponsorluk Simülatörü** (aşağıda).
3. **Paket listesi** (fiyatsız):

| Paket | Kapsam | Görünürlük zonları |
|---|---|---|
| Ana Sponsor | Yıllık giderin tamamı | Ana yelken · cenova/balon · gövde geniş alan (iki yön) · kıyafet göğüs + sırt · **+ Misafir Sporcu Kontenjanı** |
| Yelken / Gövde Sponsoru | Yelkenler | Seçenek: yelkenler (ana yelken + cenova/balon) **veya** gövde geniş alan |
| Kalem Sponsoru | Tek gider kalemi (ulaşım, konaklama…) | Gövdede bütçeyle orantılı alan: küçük / orta / büyük |
| Giyim Sponsoru | Takım kıyafeti | Su üzeri (T-shirt, polar, yelek, salopet, mont, şapka, buff, bere) + seremoni (gömlek, pantolon, T-shirt) |
| Teknik Partner | Ekipman/ürün | Kıç küçük logo · kıyafet kolu |

Kademe adları ve zon eşleşmesi Fox'un sponsorluk görüşmesinden çıkardığı taslak; Ayhan "yanlış/eksik yok" dedi [Ayhan, 5 Kas].

4. **Reklam alanları görselleri:** Ayhan'ın hazırladığı iki TUR 1948 görseli (dokunulmaz).
5. **2027 takvimi.**
6. **İletişim formu:** ad soyad · şirket · unvan · e-posta · telefon · ilgilendiği paket (açılır liste, simülatörden gelirse dolu) · mesaj · KVKK onayı. Alıcı: Ayhan [Fox — sporcu formuyla aynı varsayıldı].

### 9.2 Sponsorluk Simülatörü [Ayhan: "basit ama çalışır"]
- Ziyaretçi logosunu yükler (PNG/SVG/JPG/WebP). **Logo yalnız tarayıcıda işlenir, sunucuya gitmez** [Fox]. Form gönderilene kadar Red Lions'a ulaşmaz.
- Çizilmiş **jenerik yelkenli** (TUR 1948'in fotoğrafı değil) + takım kıyafeti (tişört).
- Paket seçimi → logo o paketin zonlarına oturur; altta zon listesi. Paket listesi §9.1 ile birebir.
- Yelken/Gövde paketinde "Yelkenler / Gövde" alt seçimi; Kalem paketinde "Küçük / Orta / Büyük".
- **Orsa / Pupa** düğmesi: cenova ↔ balon (balon açıkken logo balona geçer).
- "Bu paketle iletişime geç" → seçili paket ve zonlar iletişim formuna dolu gelir.
- Yapım: Wix'e gömülü özel HTML bileşeni (custom element / embed) [Fox]. Formla bağlantı: bileşen, seçilen paketi sayfadaki Wix formuna aktarır (Velo `postMessage` veya URL parametresi; kurucu seçer).
- Prototipten bilinen zayıflıklar: balon çizimi kaba → kurulumda düzgün spinnaker çizimi; şeffaf olmayan JPG yelkende kutu gibi görünür → yükleme alanında "şeffaf PNG en iyisi" notu (prototipte var).
- Mobil: dikey düzen, tekne üstte, paketler altta.

### 9.3 Bireyler
- "Takımın ürünlerini giy, takımı taşı" türünde kısa bölüm → **Shop**. Bağış dili yok. *(14 Kas: Shop kaldırıldı — bu bölüm sitede hiç kurulmamıştı, kurulmayacak.)*

## 10 · Shop [KALDIRILDI — 14 Kas 2026]
> **14 Kas 2026 — Shop kaldırıldı (Ayhan kararı).** Menüden SHOP, header'dan sepet ikonu ve Wix Stores'un site sayfaları (ürün, kategori, sepet, teşekkür) editörden silindi. Aşağıdaki Shop maddeleri geçersizdir; kayıt için duruyor. Wix Stores API'de hâlâ kurulu görünüyor — panel tarafı Ayhan'da.

- Wix Stores, kurgusal yer tutucu ürünlerle iskelet (örn. tişört, şapka, buff — isim/görsel yer tutucu, fiyat yer tutucu).
- **Satın alma kapalı** ta ki ödeme Ayhan/Hüseyin tarafından bağlanana kadar (Kademe 3). Ürünler "yakında" durumunda ya da sayfa gizli; kurucu Wix'te en temiz yolu seçer.
- Gerçek ürünler, üretici ve fiyatlar **[Açık]** — Ayhan sonra.

## 11 · Kurucuya bırakılanlar
- Wix'te şablonsuz/boş başlangıç mı, şablon üzerinden mi — en temiz editör deneyimini veren yol.
- Bölüm boşlukları, animasyon, hover davranışları — sade, gösterişsiz.
- Simülatör ile form arasındaki teknik köprü.
- Mobil kırılımlar.
- SEO temel ayarları (sayfa başlıkları, açıklamalar, TR/EN hreflang).

## 12 · Açık kalanlar
1. Mevcut sponsorların kademelere dağılımı (§6.7).
2. Gerçek metinler (biz kimiz, giriş cümleleri, form mesajları) — Metin Yazarı → Denetmen → Ayhan.
3. Fotoğraf/video seçimi — Ayhan.
4. Sporcu rızaları (KVKK) — Ayhan/Hüseyin toplar; şablon metni Fox hazırlayabilir.
5. Alan adı — Ayhan.
6. Shop ürünleri ve ödeme — Ayhan.
