# SOC Web — "Bize Ulaş, Yalnız Değilsin" Formu · Final Dil Metni

*14 Haziran 2026 · Denetmen onaylı (KOŞULLU ONAY → 3 düzeltme uygulandı) · Ayhan kararlarıyla kilitlendi*

**✅ UYGULAMA (14 Haz — Fox Chrome MCP ile Wix Editör'ü sürdü):** Form içeriği Wix Editör'de **TASLAK olarak uygulandı + Save edildi** (Publish Ayhan'da — Kademe 2). Wix Forms panel-editörü kullanıldı (kanvas üç-tıkla değil; daha güvenilir). Uygulananlar: Email→**E-posta** · Telefon Numarası→**Telefon (isteğe bağlı)** · Konu Başlığı **silindi** → **"Ne hakkında ulaşıyorsun?"** açılır liste (6 seçenek + "Seçin" placeholder) · eski Mesaj **silindi** → yeni "Long answer" **"Mesajın"** + placeholder "İhtiyacını ya da fikrini birkaç cümleyle anlat…" (doğru sıraya geldi) · **gönderim sonrası onay mesajı** eklendi · başlık korundu. ⚠️ Alan silmelerinde **kalıcı silme kutusu İŞARETLENMEDİ** — geçmiş gönderimler Submissions tablosunda duruyor.
- **ASKIDA — açıklama metni:** Başlık ile ilk alan arası dar; Wix klasik kanvasta kutu büyüyünce forma çakışıyor, sürükleme bu editörde güvenilmez. **Ayhan kararı: "şimdilik açıklamasız yayınla"** → ayrı oturuma kaldı.
- **ASKIDA — a11y:** görme engelli/ekran okuyucu için gerçek label (Kademe 1).
- Teknik not: Form adı Wix'te **"İletişim"**, ana sayfada gömülü. Editör erişimi memory [[steps-on-clouds-wix-site]].

Form, **ampüte ve engelli bireylerin çözüme/desteğe ihtiyaç duyduklarında kullanacakları** alandır. Steps On Clouds ana sayfasında. Dil onur merkezli: acıma/ilham pornosu yok; güç + fail + birliktelik.

---

## UYGULAMA KILAVUZU (Wix Editör'de elle)

### 1 · Başlık — DEĞİŞMİYOR
> Bize Ulaş, Yalnız Değilsin

*(Mevcut başlık zaten güçlü ve virgüllü; korundu. Dokunma.)*

### 2 · Açıklama — YENİ (başlığın hemen altına metin kutusu)
> Bir ihtiyaç, bir soru ya da paylaşmak istediğin bir hikâye — ne olursa olsun buradan başlayabilirsin. Yaz, biz okuyalım, sana dönelim. Bu yolda yalnız değilsin.

### 3 · Alan etiketleri
| # | Eski | Yeni |
|---|---|---|
| 1 | Ad* | **Ad*** *(aynı)* |
| 2 | Soyad* | **Soyad*** *(aynı)* |
| 3 | Email* | **E-posta*** |
| 4 | Telefon Numarası | **Telefon (isteğe bağlı)** |
| 5 | Konu Başlığı *(serbest metin)* | **Ne hakkında ulaşıyorsun?** → **açılır liste (dropdown)** yap, seçenekler ↓ |
| 6 | "Mesajını buraya yaz…" | **"İhtiyacını ya da fikrini birkaç cümleyle anlat…"** |

**5 numaralı listenin seçenekleri (sırayla):**
1. Protez / hareket desteği
2. Destek ve danışmanlık
3. Hikâyemi paylaşmak istiyorum
4. İş birliği / proje
5. Etkinlik & topluluk
6. Diğer

> ⚙️ Wix ipucu: "Konu Başlığı" serbest metin alanını **açılır liste**ye çevirmek için alan ayarlarından tipi değiştir; izin vermezse o alanı sil, yerine **"Açılır liste / Dropdown"** alanı ekle ve seçenekleri gir.

### 4 · Buton — DEĞİŞMİYOR
> Gönder

### 5 · Gönderim sonrası mesaj — YENİ
*(Wix: Form seçili → Ayarlar → "Gönderimden sonra ne olur" / Onay mesajı)*
> Mesajın bize ulaştı, teşekkür ederiz. En kısa sürede sana dönüş yapacağız. Yalnız değilsin.

---

## Denetmen bulguları (uygulandı)
1. **Onur — TEMİZ.** Fail ziyaretçide; engelli "ihtiyaç sahibi"ne indirgenmiyor.
2. **Kapsayıcılık düzeltmesi:** Liste yalnız ampüteye daralıyordu → **"Destek ve danışmanlık"** eklendi (görme/işitme/kronik engelli "Diğer"e itilmesin).
3. **Taahhüt:** "Yakında" çıkarıldı → "En kısa sürede dönüş" (Ayhan seçti). Uydurma süre yok.
4. **Başlık:** tire değil virgül (mevcut korundu).
5. **Türkçe:** temiz ("hikâye" â, "İhtiyacını" doğru).

## AÇIK İŞ — Erişilebilirlik (a11y) · Kademe 1 · sonraya bırakıldı
Ayhan "şimdilik sadece dil" dedi. Ama Denetmen'in misyon-kritik notu:
**Görme engelli birey bu formu ekran okuyucuyla dolduramayabilir** — alanlar gerçek `<label>` yerine sadece placeholder kullanıyor (ekran okuyucu boş alan okur). Yapılacak: her alana gerçek etiket; dropdown'a etiket; onay mesajına `aria-live`. Wix Editör'de alan ayarlarından "alan başlığını göster/label" açılarak büyük ölçüde çözülür. Ayrı oturumda ele alınacak.
