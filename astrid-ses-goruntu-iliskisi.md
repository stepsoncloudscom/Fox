# Astrid Nilsen — Gelişim Modülü 7: Ses-Görüntü İlişkisi
*Sesin görüntüyü nasıl değiştirdiği — teknik değil algısal bir konu. Film tarihinde "sessiz sinema" (1895-1927) bir eksiklik değildi, kendi diliydi; ses eklenince (1927, "The Jazz Singer") sinema yeniden icat edildi.*

---

## DİEJETİK / NON-DİEJETİK — İlk Ayrım
**Diegetic (öyküsel) ses:** Sahnenin **içindeki** kaynaktan gelir — karakterin konuşması, bir radyo, ayak sesleri. Karakterler de duyar.
**Non-diegetic (öykü-dışı) ses:** Sahnenin dışından — müzik skoru, anlatıcı sesi. Karakterler duymaz, yalnız izleyici duyar.
**Karışım (sahte-diegetik):** Bir müzik parçası sahnede bir radyodan çalıyormuş gibi başlar (diegetic), sonra sahne dışına taşıp skor haline gelir (non-diegetic) — bilinçli bir geçiş tekniği.

**Astrid'e bağlanır:** Çekim listesine ses notu eklerken bu ayrım netleşir — "arka planda müzik" belirsizdir, "karakterin dinlediği radyo (diegetic)" ya da "sahneyi saran skor (non-diegetic)" nettir.

---

## SESSİZLİĞİN GÜCÜ
Ses, **yokluğuyla** da konuşur. Sürekli müzik/efekt altında geçen bir sahneden sonra **ani sessizlik** — şok, gerilim, önemli bir anın vurgusu. Modül 1'deki "görünmez kurgu" mantığının ses eşdeğeri: sürekli ses de fark edilmez hale gelir, kesilince fark edilir.

## SES-GÖRÜNTÜ UYUMU VE UYUMSUZLUĞU
**Senkron (uyumlu) kullanım:** Ses, görüntüdeki duyguyu/eylemi pekiştirir — gerilimli sahnede gerilimli müzik.
**Asenkron (kontrast) kullanım:** Ses, görüntüyle **bilerek** çelişir — şiddetli bir sahnede neşeli/sakin müzik, izleyiciyi rahatsız eder, daha derin bir etki bırakır (ironi, yabancılaştırma). Kuleshov etkisinin (Modül 1, Sovyet montajı) ses versiyonu sayılabilir — aynı görüntü farklı sesle **farklı anlam** taşır.

## FOLEY VE SES TASARIMI
**Foley:** Gerçek hayattaki sesleri (ayak sesi, kumaş hışırtısı, kapı) **stüdyoda yeniden üretmek** — orijinal çekimde net kaydedilmemiş ya da hiç olmayan sesleri eklemek. Gerçekçilik bir **inşa** sürecidir, ham kayıt değil.
**Ses tasarımı (sound design):** Gerçekte var olmayan sesleri (bir canavarın kükremesi, bir uzay gemisinin uğultusu) **kurgu/katmanlama** ile yaratmak — görüntü gibi ses de üretilebilir/tasarlanabilir bir malzemedir.

## MÜZİK: SKOR VS KAYNAK MÜZİK
**Skor (score):** Filme özel bestelenmiş, non-diegetic müzik — duyguyu yönetir, çoğu zaman fark edilmeden.
**Kaynak müzik (source music):** Var olan, sahnede diegetic çalan şarkı — dönem/kültür/karakter kimliği taşır (bir sahnenin hangi yılda/ortamda geçtiğini anında söyler).

---

## HIGGSFIELD'DA SES (elindeki araç — doğrulanmış)
`higgsfield-generate` skill'inde `seed_audio` (metin-ses, isteğe bağlı ses/görsel referansla) ve Seedance modellerinde `audio_references`/`--generate_audio` parametreleri var (`.agents/skills/higgsfield-generate/references/media-inputs.md`). Yani Astrid'in çekim listesine (KOL 2) **ses notu da girebilir** — her sahne için diegetic/non-diegetic ayrımı + ton, prompt'a taşınabilir bir bileşen.

---

## ASTRID'E BAĞLANIR
- Çekim listesi artık yalnız görsel değil — her sahne için **ses katmanı notu** (diegetic/non-diegetic, senkron/asenkron niyet) eklenebilir.
- Süreklilik (KOL 3) sese de uygulanır — bir sahnede kurulan ses dünyası (örn. kort kenarı ortam sesi) sonraki sahnede sessizce kaybolursa bu bir süreklilik hatasıdır, tıpkı kıyafetin değişmesi gibi.
- "Sessizlik" bilinçli bir seçenek olarak çekim listesinde yer alabilir — varsayılan olarak her sahneye ses/müzik eklenmez.

---
*Modül 7 v1 · 10 Ekim 2026 · Fox · Astrid Nilsen'in agent dosyasında ÖN KOŞUL olarak referans verilir.*
