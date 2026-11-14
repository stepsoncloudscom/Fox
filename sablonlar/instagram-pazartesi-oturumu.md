# Instagram — Pazartesi Oturumu Protokolü
*Tetik: Ayhan "Instagram" der (ya da sabah brifingi pazartesi hatırlatması). Hedef süre ~30 dk. Tasarım: `raporlar/tasarim-instagram-haftalik-dongu-2026-11-14.md`. Kuyruk: `raporlar/instagram-kuyruk.md`.*

Fox bu oturumda **yayınlamaz ve zamanlamaz** — yayın tuşu Ayhan'da (Kademe 2). Fox kartı açar, kararları yazar, kuyruğu tutar.

## Sıra

1. **Güncelle.** `cd /Users/ayhanerden/Fox && git pull --ff-only origin main`. Oturumun başlangıç saatini not et.
2. **Durumu oku.**
   - `python3 sablonlar/araclar/instagram_kuyruk.py ozet` ve `python3 sablonlar/araclar/instagram_kuyruk.py denetle` (1 → ihlali Ayhan'a tek satırla söyle; 2 → kuyruğu düzelt, sonra devam).
   - **Kaçan koşu:** Heartbeat'te bu haftanın perşembesine (ya da geçen perşembeye) ait satır yoksa perşembe görevi koşmamıştır (Mac kapalıydı). Önce hazırlığı **bu oturumda**, zamanlanmış görevin (`~/.claude/scheduled-tasks/instagram-haftalik-hazirlik/SKILL.md`) adımlarıyla yap; Ayhan'a "perşembe koşusu kaçmış, hazırlık şimdi yapılıyor" de.
3. **Kartı aç.**
   - `python3 sablonlar/araclar/instagram_onay_karti.py <scratchpad>/instagram-kart` (her hafta **aynı yol** → aynı Artifact URL'si).
   - Çıktıyı Artifact olarak yayınla (`index.html` + `medya/` dosyaları `files` ile), Ayhan'a aç. İlk yayında artifact-design becerisini yükle.
4. **Kararları yaz.** Her paket için Ayhan'ın kararını Kararlar tablosuna **bugünün tarihiyle** ekle ve durumu güncelle:
   | Ayhan der | Kararlar satırı | Durum |
   |---|---|---|
   | Onay (yayın kartı) | `onay` | `onaylandı` |
   | Onay (deneme kartı, Yön onayı) | `yön onayı` — not **mutlaka** `tavan N` ile başlar (kartta yazan tam üretim maliyeti; 1080p yeniden üretim onaylandıysa "1080p üretim, tavan N"). Tavansız satırla perşembe görevi üretmez. | `üretimde` |
   | Revize + not | `revize` — not: Ayhan'ın sözü | `revize`, tur +1; tur 3 olursa `park` ve slot yedekten dolar |
   | Çıkar | `çıkar` | `çıkarıldı` |
5. **Zamanlama.** Ayhan onaylananları Meta Business Suite'te (bu Mac'in tarayıcısı) zamanlar. Paket klasörü: `~/Desktop/Steps On Clouds/Design /Instagram/Paketler/<slot>_<madde>/`. Her zamanlanan için `zamanlandı` kararı + durum `zamanlandı`.
6. **Ayın ilk pazartesisi (+10 dk).** Havuz önerisini (`raporlar/instagram-havuz-YYYY-MM.md`) onayla: her madde `havuz evet` / `havuz hayır`, evetler kuyruğa `havuzda` olarak girer. Insights ekranlarını al (v5 §6), ham sayıları heartbeat'e yaz.
   - **İstisna — ilk oturum, 16 Kas 2026:** K0 (mağaza sayfası), K4 (Steps On Mela hakları), K8 (YZ etiketi), K10 (bio) kararları + v5 listesinin havuz onayı (20 madde evet/hayır; Denetmen'in 12 madde önerisi ve madde 09 dahil; `havuz hayır` olan `çıkarıldı`) + T0 Insights ekranları (v5 §6) + **yüz şartlarının teyidi** (14 Kas "Evet, görünsün": kameraya bakan portre yok, YZ etiketi, gerçek kullanıcı gibi sunulmaz — bunlar Fox'un şartları, Ayhan açıkça onaylamadı) + **05 yön kararı** (A / B / C; Fox + Denetmen önerisi B) + **yorumlara kim, kaç saat içinde cevap verir** (tasarım kapsam dışı bıraktı; 02 kargo sorusu çekebilir).
7. **Süreyi yaz.** İlk dört pazartesi oturumun gerçek süresini heartbeat'e yaz (`pazartesi | oturum <dk> dk, <n> karar`). 30 dk'yı sürekli aşarsa kart sadeleştirilir.
8. **Kapat.** `denetle` 0 dönmeli. `git add raporlar/instagram-kuyruk.md && git commit` (Türkçe mesaj + Co-Authored-By) `&& git push origin main`.

## Görev durumu
- Görev `DURAKLADI` ise (iki hafta kararsız kart): bu oturumdaki ilk karar onu çözer — sayaç satırını `görev: AKTİF — ` yap.
- Görev `KURU` ise: kuru koşu henüz geçmemiştir; Ayhan'a söyle, hazırlığı oturumda yap.
