# Claudia × Cloud One — 7 Sahne, Final Prompt Seti
*11 Ekim 2026 · Ayhan talimatı: "tüm öğrendiklerinle her kare için ayrı prompt çıkart. her kare için karakter, mekan ve kıyafetler aynı olsun." Bu dosya o çıktı — henüz ÜRETİLMEDİ, hepsi taslak. Ateşleme tek tek Kademe 2 (Ayhan onayı).*

## SAHNE 1 — üretildi, onaylı (11 Ekim, job `ebed3000`)
Kompozisyon sorunu **çözüldü** — Claudia artık yakın plana çökmüyor, geniş kort/tribün hakim, tam boy görünür (hedeflenen %15-20 kadar küçük değil ama net bir iyileşme). Elbise/çorap doğru. **Bulunan gerçek sorun:** ayakkabıdaki "Babolat" yazısı bozuk render edilmiş ("Babolit" gibi okunuyor, metin garbling — AI'ın bilinen zayıflığı), yalnızca dijital yakınlaştırmada görülüyor, normal boyutta fark edilmiyor. Aşağıdaki tüm promptlardan **okunur marka yazısı talebi çıkarıldı** (yalnız logo şekli/rengi isteniyor artık) — bu riski 2-7 sahnelerde tekrarlamamak için. Sahne 1'in kendisi bu haliyle kabul edilebilir (yazı normal görünümde seçilmiyor) ya da düzeltilmiş promptla tekrar üretilebilir — Ayhan'ın kararı.

## Sahne 5 — önce dürüst not (bu set onu da kapsıyor, ayrı düzeltme gerekmiyor)
Üretilen Sahne 5 (job `6f7c70c6`) kıyafet/çorap/kort açısından temiz ama **"mid-serve" talebini karşılamıyor**: kol öne/omuz hizasında uzanmış, gerçek bir servis değil — yaklaşma/forehand duruşuna benziyor. Ayakkabı markasız (Babolat talebinden önce üretildi). Aşağıdaki Sahne 5 promptu bunu düzeltmek için servis pozunu daha katı tarif ediyor (kol doğrudan baş üstünde, arka topuk kalkık).

## DEĞİŞEN KARARLAR (bu set neden önceki plandan farklı)
- **Kıyafet kilidi değişti:** Astrid'in ilk planı polo + koyu yeşil pileli etek + headband'di. Gerçek üretimde Sahne 3'ün 3 sorunundan biri (çok dar/leotard görünümü) **beyaz pileli tenis elbisesiyle** düzeltildi ve onaylandı (Sahne 4-5). Bu set o gerçek kararı kilitliyor — polo/headband değil, **elbise**. Ayhan'ın "tenis bodysuit ya da tenis kıyafeti" talimatına da uyuyor (elbise = tenis kıyafeti).
- **Babolat ayakkabı eklendi** — Ayhan'ın yeni talimatı, 7 sahnenin hepsine şimdi baştan işlendi (geriye dönük yama değil).
- **Model: `nano_banana_pro`, hepsi için** — `text2image_soul_v2`'nin `--image` + `--soul-id` kombinasyonundaki `enhance_prompt` hatasından (prompt'u sessizce siliyor) kaçınmak için. İki referans: Claudia yüz referansı + Cloud One ürün referansı.
- **Sahne 1'e Claudia eklendi** — önceki onaylı versiyon kişisiz (`soul_location`) bir kuruluş kareydi (kompozisyon çöküşü sorunu yüzünden). Ayhan'ın "her karede karakter aynı olsun" talimatı Claudia'nın 1'de de görünmesini gerektiriyor. Nano Banana Pro'nun Sahne 3-5'te geniş/tam-boy çekimlerde iyi çalıştığını gördük — aynı riski burada da taşıyor, **bu yüzden ilk üretimde özellikle gözden geçirilmeli** (eski kompozisyon-çöküşü sorunu geri gelebilir).
- **Not (şeffaflık, engelleyici değil):** Babolat gerçek bir marka. Stilistik/editorial referans olarak kullanmak (Lacoste-adjacent register'da zaten yaptığımız gibi) düşük riskli, ama bu bir onay değil — bilgin olsun istedim.

---

## KİLİTLİ BLOKLAR (7 sahnenin hepsinde birebir aynı)

**[KARAKTER]**
> a young Scandinavian woman in her late twenties, with a strong prominent aquiline nose, sharp defined cheekbones and a sharp jaw, ice-blue/grey-blue eyes, calm-intense composed "warrior-regal" expression — commanding rather than posing. Pale cool-toned skin with faint natural freckles. Ash-blonde hair worn in a single tight neat braid. Her facial identity should match the provided face reference image closely.

**[KIYAFET]**
> Wearing a fitted white pleated tennis dress with a modest classic heritage silhouette (not a high-cut leotard), plain and unbranded with no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo clearly visible at the ankle, matching the product reference image exactly in shape, color and placement — reproduce the logo faithfully, do not redesign it. White Babolat-style tennis shoes, clean low-top athletic silhouette, with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe.

**[MEKÂN]**
> The same heritage tennis stadium throughout the series: green hard court surface with worn white line markings (consistent green, never grey asphalt), faded teal and coral stadium seating with visible wear and patina, tall trees silhouetted behind the upper tier.

**[GLOBAL STİL]**
> Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft Kodak-style highlights, gentle halation, light 35mm film grain, realistic photographic skin texture with visible pores, natural micro-imperfections, no plastic skin, no digital artifacts, no CGI smoothness, no over-sharpened digital sheen. Locked-off static camera, no handheld blur.

**Ortak CLI kuyruğu (hepsinde aynı):**
```
--image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
--image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
--aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SAHNE 1 — Kuruluş

```
higgsfield generate create nano_banana_pro \
  --prompt "Extreme wide establishing shot at dawn on a completely empty tennis court. [a young Scandinavian woman in her late twenties, with a strong prominent aquiline nose, sharp defined cheekbones and a sharp jaw, ice-blue/grey-blue eyes, calm-intense composed warrior-regal expression, pale cool-toned skin with faint natural freckles, ash-blonde hair in a single tight neat braid, facial identity matching the provided face reference image] enters the frame from the far left edge, small in the frame — occupying roughly 15-20% of frame height — she has just stepped onto the court, racket held low at her side, not yet raised. The vastness of the empty court and stadium dominates the composition; do not crop in to a medium or close shot, do not center her, keep the empty court as the dominant subject. Wearing a fitted white pleated tennis dress with a modest classic heritage silhouette, plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo visible at the ankle, matching the product reference image exactly. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text or lettering anywhere on the shoe. Setting: green hard court surface with worn white line markings, faded teal and coral stadium seating with visible wear and patina, tall trees silhouetted behind the upper tier. Low dawn sun from behind the stadium seating, long cast shadow stretching toward camera, cool pre-dawn ambient fill balancing the warm key. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft Kodak-style highlights, gentle halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Locked-off static wide camera, deep depth of field, no handheld blur." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```
**Risk notu:** Claudia küçük/uzak kalmazsa (yakın plana çökerse) bu, eski kompozisyon sorununun nano_banana_pro'da da çıktığı anlamına gelir — tek kare test edip gözle bakmadan diğerlerine geçmeyelim.

---

## SAHNE 2 — Ritüel (çorap, Çehov kurulumu)

```
higgsfield generate create nano_banana_pro \
  --prompt "Close-up detail shot: [a young Scandinavian woman in her late twenties, strong prominent aquiline nose, sharp defined cheekbones and jaw, ice-blue/grey-blue eyes, calm-intense expression, pale cool-toned skin with faint freckles, ash-blonde hair in a single tight braid, facial identity matching the provided face reference image] seated on a weathered teal-painted wooden courtside bench, bent forward, hands pulling on one Cloud One sock over her ankle — a quiet, private preparation ritual, face partially visible, turned down toward her hands. Wearing a fitted white pleated tennis dress with a modest classic heritage silhouette, plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo clearly visible at the ankle, matching the product reference image exactly in shape, color and placement — reproduce the logo faithfully. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe — one shoe resting beside the bench if natural to the pose. Setting: the same heritage tennis stadium — green hard court, worn white line markings, faded teal and coral stadium seating softly blurred behind. Same warm dawn key light as the establishing frame, soft rim light along the ankle and sock ribbing. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Macro push-in on the ankle/sock/logo, shallow depth of field, soft blurred court and stadium behind, locked-off camera." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SAHNE 3 — Geçiş (yürüyüş, raket elde)

```
higgsfield generate create nano_banana_pro \
  --prompt "Editorial sports photograph, mid-full shot: [a young Scandinavian woman in her late twenties, strong prominent aquiline nose, sharp defined cheekbones and jaw, ice-blue/grey-blue eyes, calm-intense composed expression, pale cool-toned skin with faint freckles, ash-blonde hair in a single tight braid, facial identity matching the provided face reference image] rises from the courtside bench and walks toward the court, racket held loosely in one hand, an unhurried confident stride — the private ritual is over, she moves toward the public court. Wearing a fitted white pleated tennis dress with a modest classic heritage silhouette (not a high-cut leotard), plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo clearly visible at the ankle, matching the product reference image exactly. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe. Setting: the same heritage tennis stadium — green hard court with worn white line markings, faded teal and coral stadium seating with visible wear and patina, tall trees silhouetted behind the upper tier. Morning light now slightly higher than the dawn establishing frame, same direction. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Mid-full body shot, slight tilt-up as she rises, she occupies the center-right of frame with meaningful court space around her, static eye-level camera, no handheld motion." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SAHNE 4 — Eşik (çizgiyi geçiş) — onaylı versiyonla aynı, yalnız ayakkabı eklendi

```
higgsfield generate create nano_banana_pro \
  --prompt "Editorial sports photograph, low-angle detail shot at the court's baseline edge: [a young Scandinavian woman in her late twenties, strong prominent aquiline nose, sharp defined cheekbones and jaw, ice-blue/grey-blue eyes, calm-intense composed expression, ash-blonde hair in a single tight braid, facial identity matching the provided face reference image]'s foot and ankle cross the white baseline chalk line of a green heritage tennis court, racket trailing in the same frame near her hand, the threshold moment just before play begins, racket held normally by its grip handle, strings facing forward naturally. Wearing a modest fitted white tennis dress with a pleated skirt (not a high-cut leotard), classic heritage silhouette, plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo clearly visible at the ankle, matching the product reference image exactly in shape, color, and placement. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe — crossing the baseline in sharp focus. Setting: the same heritage tennis stadium — green hard court surface with worn white line markings (consistent green court color, not grey asphalt), faded teal and coral stadium seating with visible wear and patina in the soft background, warm morning light. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Low angle, camera near ground level, foot/shoe and line crossing in sharp focus in the lower-mid frame, racket and partial leg visible, shallow depth of field with court/stadium softly blurred behind." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SAHNE 5 — Zirve (servis) — pozu daha sıkı tarif edildi, önceki deneme tam servis vermedi

```
higgsfield generate create nano_banana_pro \
  --prompt "Editorial sports action photograph, full-body dynamic shot: [a young Scandinavian woman in her late twenties, strong prominent aquiline nose, sharp defined cheekbones and jaw, ice-blue/grey-blue eyes, intense focused expression, ash-blonde hair in a single tight braid whipping slightly with the motion, facial identity matching the provided face reference image] mid-serve on a heritage tennis court — racket arm fully extended straight overhead, directly above her head, at the peak of the service motion (not forward, not at shoulder height — vertically overhead), non-racket arm extended upward and slightly forward tracking the ball, eyes and chin tilted up locked on the ball above her, body coiled in classic tennis serve stance, front foot planted, back heel lifted off the ground, visible athletic tension through the torso. Wearing a fitted white pleated tennis dress, classic heritage silhouette, plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo clearly visible at the ankle, matching the product reference image exactly. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe — back shoe heel clearly lifted off the court surface. Setting: the same heritage tennis stadium — green hard court with worn white line markings, faded teal and coral stadium seating with visible wear and patina, warm mid-morning light, brighter and higher than the earlier dawn frames. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Full body visible head to toe, dynamic action captured in a frozen instant, she occupies the center of the frame with court and stadium clearly visible around her, athletic motion blur limited to the racket tip only, everything else sharp." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SAHNE 6 — Duraklama (sahneyi kuran bakış, yeni)

```
higgsfield generate create nano_banana_pro \
  --prompt "Editorial sports portrait, a stillness beat: [a young Scandinavian woman in her late twenties, strong prominent aquiline nose, sharp defined cheekbones and jaw, ice-blue/grey-blue eyes, pale cool-toned skin with faint freckles, ash-blonde hair in a single tight braid, facial identity matching the provided face reference image] stands upright at the baseline, racket lowered to her side, all motion stopped. She turns her gaze directly toward the camera/horizon — calm, composed, commanding, the one who sets the scene rather than performs for it. No action, just presence, composed warrior-regal expression. Wearing a fitted white pleated tennis dress, classic heritage silhouette, plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo visible at the ankle, matching the product reference image exactly. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe. Setting: the same heritage tennis stadium — green hard court with worn white line markings, faded teal and coral stadium seating with visible wear and patina. Same mid-morning light as the serve frame, slightly softened. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Static medium-close portrait from the waist up, camera at eye level, minimal background, locked-off camera, no handheld motion." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SAHNE 7 — Çözüm/hero shot (Sahne 2'nin kafiyesi, yeni)

```
higgsfield generate create nano_banana_pro \
  --prompt "Editorial sports photograph, closing hero shot that rhymes with the opening ritual: [a young Scandinavian woman in her late twenties, strong prominent aquiline nose, sharp defined cheekbones and jaw, ice-blue/grey-blue eyes, calm-intense warrior-regal expression, pale cool-toned skin with faint freckles, ash-blonde hair in a single tight braid, facial identity matching the provided face reference image] stands in full confident stance on the court, racket resting at her side, the Cloud One sock and logo at her ankle clearly legible in full daylight — the same ankle/sock detail as the opening preparation ritual, now shown in full public daylight rather than private preparation. Wearing a fitted white pleated tennis dress, classic heritage silhouette, plain and unbranded, no logo on the garment. White Cloud One crew socks with the teal embroidered cloud-figure logo clearly visible and sharply legible at the ankle, matching the product reference image exactly in shape, color, and placement — this is the hero product beat, logo must be crisp. White Babolat-style tennis shoes with a dark angular flame-shaped logo accent on the white upper — logo shape and color only, no readable brand text anywhere on the shoe. Setting: the same heritage tennis stadium — green hard court with worn white line markings, faded teal and coral stadium seating with visible wear and patina. The warmest, most mature light of the series — late morning sun, fullest exposure of the day's arc. Heritage sportswear editorial, warm sun-faded 1970s film color grading, soft halation, light 35mm film grain, realistic photographic skin texture with visible pores, no plastic skin, no digital artifacts, no CGI smoothness. Medium framing, her full stance centered, sock and logo still legible at the ankle, racket resting at her side, locked-off camera, no handheld motion." \
  --image-references e30cfa20-6e9a-4492-bf87-7e218d6d3086 \
  --image-references c93d6868-55a9-47b6-9cba-8c4856e13e50 \
  --aspect_ratio 3:4 --resolution 2k --wait --json
```

---

## SIRADAKİ ADIM
Hepsi taslak (Kademe 1 — hazırlık). Ateşleme Kademe 2: Ayhan hangi sahne(ler)den başlanacağını onaylar. Önerim: önce **Sahne 1** tek başına test edilsin (kompozisyon riski), sonra geri kalan 6'sı toplu onayla art arda üretilir.

---
*v1 · 11 Ekim 2026 · Fox (Astrid'in KOL1/KOL2/KOL3 metodolojisiyle, bu oturumun üretim derslerine dayanarak doğrudan sentezlendi) · İlgili: `fox-ai-director-insa.md`, `.claude/agents/astrid-nilsen.md`, `astrid-ai-gercekcilik.md` (Modül 16).*
