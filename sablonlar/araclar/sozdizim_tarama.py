#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
sozdizim_tarama.py — "AI yazmış" hissinin SÖZDİZİMİ katmanı taraması (Türkçe).

Neden ayrı bir araç: `slop_tarama.py` KELİME düzeyinde çalışır ("elevate",
"yeni nesil", "kusursuz deneyim"). Ama bir metin tek bir klişe kelime
içermeden de "AI yazmış" diye okunabilir — çünkü tell kelimede değil
CÜMLE MİMARİSİNDE'dir: karşıtlık kalıbı bağımlılığı, aforizma kapanışları,
tek tip cümle uzunluğu, somut çapa yokluğu.

Kaynak vaka: Özgür Irmak Protez — Hakkımızda v0.5 (4 Ağu 2026). Müşteri
"yapay zekâya mı yazdırdın" dedi. Metin slop_tarama.py'den TEMİZ geçmişti.
275 kelimede 5 "X değil Y" karşıtlığı vardı.

Kullanım:
    python3 sozdizim_tarama.py dosya.md [dosya2.txt ...]
    python3 sozdizim_tarama.py raporlar/            # klasör tarar
    python3 sozdizim_tarama.py --json dosya.md      # makine okunur çıktı

Çıkış kodu: 0 = temiz · 1 = en az bir SERT eşik aşıldı · 2 = yalnız uyarı.

ÖNEMLİ — ölçünün statüsü (Tip A/B kanıt kuralı):
Buradaki eşikler DIŞ KAYNAKLI BENCHMARK DEĞİLDİR. Marka Bulutu OS'un kendi
çalışma eşikleridir; onaylı/reddedilen metin korpusundan kalibre edilir ve
korpus büyüdükçe güncellenir. Rapora yazarken "iç çalışma eşiği" diye geçir,
"sektör standardı" diye değil. Tarama Denetmen'in ve insan kulağının yerine
geçmez — ilk süzgeçtir.
"""

import json
import re
import statistics
import sys
from pathlib import Path

UZANTILAR = {".md", ".txt", ".html", ".htm"}
BUYUK = "A-ZÇĞİÖŞÜ"

# Cümle sonu: . ! ? … — kısaltma/ondalık kaynaklı yanlış bölmeyi azaltmak için
# nokta sonrası boşluk + büyük harf ya da satır sonu aranır.
CUMLE_SONU = re.compile(rf"(?<=[.!?…])(?=\s+[{BUYUK}\"«(]|\s*$)")

# Gövde dışı satırlar: markdown başlığı, meta/etiket bloğu, tablo, liste işareti,
# kod, alıntı, ayraç. Ölçüm yalnız DÜZ PROSA üzerinde yapılır.
ATLA = re.compile(
    r"^\s*(#{1,6}\s|>\s|\||```|---|===|\*{3}|_{3}|\[|═|─|\d+\.\s|[-*+]\s)"
)

# ── 1. KARŞITLIK KALIBI (en güçlü tell) ────────────────────────────────────
KARSITLIK = [
    (r"\bdeğil\b", "değil"),
    (r"\byerine\b", "yerine"),
    (r"\bziyade\b", "ziyade"),
    (r"\baksine\b", "aksine"),
]
# ── 2. SİMETRİ KALIPLARI ───────────────────────────────────────────────────
SIMETRI = [
    (r"\bhem\b[^.!?]{2,60}\bhem\b", "hem…hem"),
    (r"\bne\b[^.!?]{2,60}\bne de\b", "ne…ne de"),
    (r"\bsadece\b[^.!?]{2,80}\bdeğil\b", "sadece…değil"),
    (r"\byalnızca\b[^.!?]{2,80}\bdeğil\b", "yalnızca…değil"),
    (r"\bbir yandan\b[^.!?]{2,80}\böte yandan\b", "bir yandan…öte yandan"),
]
# ── 3. META-ANLATIM (metnin kendini tarif etmesi) ──────────────────────────
META = [
    (r"bu (?:rehber|yazı|makale|içerik|bölüm|sayfa)\b[^.!?]{0,80}\b(?:anlat|ele al|özetle|inceler|sunar)", "metin kendini tarif ediyor"),
    (r"^\s*(?:özetle|sonuç olarak|kısacası|özetlemek gerekirse)\b", "kapanış kalıbı"),
    (r"\bunutmayın(?:ız)?\b", "didaktik hitap"),
]
# ── 4. FORMÜLER BAĞLAÇ (cümle başı) ────────────────────────────────────────
BAGLAC = [
    "Bu yüzden", "Bu nedenle", "Dolayısıyla", "Ayrıca", "Öte yandan",
    "Bununla birlikte", "Ancak", "Yine de", "Aynı şekilde", "Buna karşın",
]
# ── 5. AFORİZMA KAPANIŞI ───────────────────────────────────────────────────
# Paragrafın son cümlesi: kısa + geniş zaman genelleme fiili + sıfır somut çapa.
GENIS_ZAMAN = re.compile(r"\w+(?:ir|ır|ur|ür|er|ar|maz|mez)\b[.!?…]?\s*$")

# ── 6. İNSAN İŞARETİ (metinde konuşan bir özne var mı) ─────────────────────
# Korpus bulgusu: köşe yazılarında birinci şahıs + soru + alıntı HER ZAMAN var;
# "AI yazmış" denen kendi metinlerimizde üçü de SIFIRDI.
BIRINCI_SAHIS = re.compile(
    r"\b(ben|bana|beni|benim|bence|biz|bize|bizi|bizim)\b"
    r"|\w+(?:yorum|yoruz|dım|dim|dum|düm|dık|dik|duk|dük|mışım|miştik)\b",
    re.IGNORECASE,
)

# ── EŞİKLER — KORPUSTAN KALİBRE (uydurma değil) ────────────────────────────
# Kaynak korpus: 18 köşe yazısı · 12.568 kelime · 3 yazar (Zülal Kalkandelen —
# Cumhuriyet · Fatih Altaylı — fatihaltayli.com.tr · Yılmaz Özdil — Sözcü/arşiv),
# 8 Ağu 2026'da ölçüldü. Ayrıntı: fox-metin-insan-sesi-korpusu.md
#   UYARI = korpusun p90 (alt-yönlü ölçüde p10) → insan aralığının kenarı
#   SERT  = korpusta hiçbir yazarda GÖRÜLMEMİŞ bölge (max/min ötesi)
# Not: korpus gazete köşe yazısıdır; marka/kurum metni ayrı bir türdür. Eşikler
# "insan Türkçesi tabanı" içindir, tür taklidi için değil. Korpus büyüdükçe güncellenir.
ESIK = {
    "karsitlik_bin_kelime":  {"uyari": 6.0,  "sert": 8.0},
    "karsitlik_cumle_orani": {"uyari": 0.09, "sert": 0.13},
    "cv_min":                {"uyari": 0.47, "sert": 0.42},
    "somut_yuz_kelime":      {"uyari": 5.5,  "sert": 3.0},
    "kisa_cumle_orani":      {"uyari": 0.05, "sert": 0.02},
    # korpusta min 16.9 / medyan 31.0 — marka metni türü daha sessizdir, eşik
    # bilinçli olarak korpusun altına çekildi (tür farkı payı)
    "insan_isareti_bin":     {"uyari": 12.0, "sert": 5.0},
    "noktali_virgul_yuz":    {"uyari": 0.7,  "sert": 1.2},
    "aforizma_orani":        {"uyari": 0.15, "sert": 0.25},
    "simetri_bin_kelime":    {"uyari": 3.0,  "sert": 5.0},
    "baglac_cumle_orani":    {"uyari": 0.05, "sert": 0.08},
    "paragraf_cv_min":       {"uyari": 0.44, "sert": 0.30},
}


def govde_metni(ham: str) -> str:
    """Markdown/meta gürültüsünü ayıklayıp yalnız düz prosa satırlarını döndürür."""
    satirlar = []
    kod = False
    for satir in ham.splitlines():
        if satir.strip().startswith("```"):
            kod = not kod
            continue
        if kod or ATLA.match(satir):
            continue
        if not satir.strip():
            satirlar.append("")
            continue
        # satır içi markdown işaretlerini temizle
        temiz = re.sub(r"[*_`#]", "", satir)
        satirlar.append(temiz.strip())
    return "\n".join(satirlar)


def paragraflar(metin: str):
    return [p.strip() for p in re.split(r"\n\s*\n", metin) if len(p.split()) >= 8]


def cumleler(metin: str):
    parcalar = [c.strip() for c in CUMLE_SONU.split(metin) if c.strip()]
    return [c for c in parcalar if len(c.split()) >= 3]


def somut_capalar(cumle_listesi):
    """Sayı, tarih, ölçü birimi ve cümle-içi özel ad = doğrulanabilir somut çapa."""
    capalar = []
    for c in cumle_listesi:
        capalar += re.findall(r"\b\d[\d.,:/]*\b", c)                     # sayı/tarih/saat
        capalar += re.findall(r"\b\d+\s?(?:kg|cm|mm|m|km|yıl|ay|gün|saat|dk|adet|kişi|TL|€|\$|%)", c)
        jetonlar = c.split()[1:]                                          # ilk jeton hariç
        capalar += [j for j in jetonlar if re.match(rf"^[{BUYUK}][a-zçğıöşü]{{2,}}", j)]
    return capalar


def bul(metin: str, desenler):
    vurus = []
    for desen, etiket in desenler:
        for es in re.finditer(desen, metin, re.IGNORECASE | re.MULTILINE):
            vurus.append((etiket, es.group(0)[:60]))
    return vurus


def analiz(dosya: Path):
    ham = dosya.read_text(encoding="utf-8")
    metin = govde_metni(ham)
    paras = paragraflar(metin)
    cums = cumleler(" ".join(paras))
    kelime_sayisi = sum(len(c.split()) for c in cums)
    if kelime_sayisi < 60 or len(cums) < 5:
        return None  # ölçüm için çok kısa

    uzunluklar = [len(c.split()) for c in cums]
    ort = statistics.mean(uzunluklar)
    cv = statistics.pstdev(uzunluklar) / ort if ort else 0.0

    p_uz = [len(p.split()) for p in paras]
    p_cv = statistics.pstdev(p_uz) / statistics.mean(p_uz) if len(p_uz) > 1 and statistics.mean(p_uz) else 0.0

    karsitlik = bul(" ".join(cums), KARSITLIK)
    karsit_cumle = [c for c in cums if any(re.search(d, c, re.I) for d, _ in KARSITLIK)]
    simetri = bul(" ".join(cums), SIMETRI)
    meta = bul(metin, META)
    baglac = [c for c in cums if any(c.startswith(b) for b in BAGLAC)]
    capalar = somut_capalar(cums)
    govde = " ".join(cums)
    nokvir = govde.count(";")

    kisa_cumle = [c for c in cums if len(c.split()) <= 6]
    sorular = [c for c in cums if c.rstrip().endswith("?")]
    alintilar = govde.count("“") + govde.count("«") + govde.count('"') // 2
    insan_isareti = len(BIRINCI_SAHIS.findall(govde)) + len(sorular) + alintilar

    aforizma = []
    for p in paras:
        pc = cumleler(p)
        if not pc:
            continue
        son = pc[-1]
        if (len(son.split()) <= 14
                and GENIS_ZAMAN.search(son)
                and not somut_capalar([son])):
            aforizma.append(son)

    return {
        "dosya": str(dosya),
        "kelime": kelime_sayisi,
        "cumle": len(cums),
        "paragraf": len(paras),
        "olcumler": {
            "karsitlik_bin_kelime": round(len(karsitlik) / kelime_sayisi * 1000, 1),
            "karsitlik_cumle_orani": round(len(karsit_cumle) / len(cums), 3),
            "cv_min": round(cv, 3),
            "somut_yuz_kelime": round(len(capalar) / kelime_sayisi * 100, 1),
            "kisa_cumle_orani": round(len(kisa_cumle) / len(cums), 3),
            "insan_isareti_bin": round(insan_isareti / kelime_sayisi * 1000, 1),
            "noktali_virgul_yuz": round(nokvir / kelime_sayisi * 100, 1),
            "aforizma_orani": round(len(aforizma) / len(paras), 3) if paras else 0.0,
            "simetri_bin_kelime": round(len(simetri) / kelime_sayisi * 1000, 1),
            "baglac_cumle_orani": round(len(baglac) / len(cums), 3),
            "paragraf_cv_min": round(p_cv, 3),
        },
        "ornekler": {
            "karsitlik": [c[:110] for c in karsit_cumle[:6]],
            "aforizma": [a[:110] for a in aforizma[:6]],
            "simetri": [f"{e}: {v}" for e, v in simetri[:4]],
            "meta": [f"{e}: {v}" for e, v in meta[:4]],
        },
        "ortalama_cumle_kelime": round(ort, 1),
    }


# Eşiği aşma yönü: "ust" = büyükse kötü, "alt" = küçükse kötü
YON = {
    "karsitlik_bin_kelime":  ("ust", "Karşıtlık kalıbı yoğunluğu (X değil Y)"),
    "karsitlik_cumle_orani": ("ust", "Karşıtlık taşıyan cümle oranı"),
    "cv_min":                ("alt", "Cümle uzunluğu değişkenliği (monotonluk)"),
    "somut_yuz_kelime":      ("alt", "Somut çapa yoğunluğu (sayı/ad/ölçü)"),
    "kisa_cumle_orani":      ("alt", "Kısa cümle oranı (≤6 kelime — vuruş)"),
    "insan_isareti_bin":     ("alt", "İnsan işareti (birinci şahıs + soru + alıntı)"),
    "noktali_virgul_yuz":    ("ust", "Noktalı virgül yoğunluğu"),
    "aforizma_orani":        ("ust", "Aforizmayla kapanan paragraf oranı"),
    "simetri_bin_kelime":    ("ust", "Simetri kalıbı (hem…hem / sadece…değil)"),
    "baglac_cumle_orani":    ("ust", "Cümle başı formüler bağlaç oranı"),
    "paragraf_cv_min":       ("alt", "Paragraf uzunluğu değişkenliği"),
}


def degerlendir(sonuc):
    """Her ölçüyü iki kademeli eşiğe vurur: SERT (insanda görülmemiş) > UYARI (kenar)."""
    bulgular = []
    for anahtar, deger in sonuc["olcumler"].items():
        yon, ad = YON[anahtar]
        esik = ESIK[anahtar]
        asti = (lambda e: deger > e) if yon == "ust" else (lambda e: deger < e)
        if asti(esik["sert"]):
            seviye = "SERT"
        elif asti(esik["uyari"]):
            seviye = "UYARI"
        else:
            continue
        isaret = ">" if yon == "ust" else "<"
        esik_degeri = esik["sert"] if seviye == "SERT" else esik["uyari"]
        karsilastirma = f"{deger} {isaret} {esik_degeri} ({seviye.lower()} eşiği)"
        bulgular.append((seviye, ad, karsilastirma, anahtar))
    return bulgular


def main():
    argv = [a for a in sys.argv[1:] if a != "--json"]
    json_cikti = "--json" in sys.argv
    if not argv:
        print(__doc__)
        sys.exit(0)

    dosyalar = []
    for arg in argv:
        p = Path(arg)
        if p.is_dir():
            dosyalar += [f for f in sorted(p.rglob("*")) if f.suffix.lower() in UZANTILAR]
        elif p.is_file():
            dosyalar.append(p)
        else:
            print(f"⚠️  bulunamadı: {arg}", file=sys.stderr)

    sert_var = uyari_var = False
    toplu = []

    for dosya in dosyalar:
        try:
            sonuc = analiz(dosya)
        except (UnicodeDecodeError, OSError) as e:
            print(f"⚠️  okunamadı: {dosya} ({e})", file=sys.stderr)
            continue
        if sonuc is None:
            continue
        bulgular = degerlendir(sonuc)
        sonuc["bulgular"] = [
            {"seviye": s, "olcu": a, "karsilastirma": k} for s, a, k, _ in bulgular
        ]
        toplu.append(sonuc)
        if json_cikti:
            continue

        print(f"\n📄 {dosya}")
        print(f"   {sonuc['kelime']} kelime · {sonuc['cumle']} cümle · "
              f"{sonuc['paragraf']} paragraf · ort. cümle {sonuc['ortalama_cumle_kelime']} kelime")
        if not bulgular:
            print("   ✅ Sözdizimi temiz — insan sesi eşiklerinin içinde.")
            continue
        for seviye, ad, karsilastirma, anahtar in bulgular:
            isaret = "❌ SERT " if seviye == "SERT" else "⚠️  UYARI"
            print(f"   {isaret} {ad}: {karsilastirma}")
            if seviye == "SERT":
                sert_var = True
            else:
                uyari_var = True
        for baslik, satirlar in sonuc["ornekler"].items():
            if satirlar:
                print(f"   ↳ {baslik}:")
                for s in satirlar:
                    print(f"      · {s}")

    if json_cikti:
        print(json.dumps(toplu, ensure_ascii=False, indent=2))

    if sert_var:
        sys.exit(1)
    sys.exit(2 if uyari_var else 0)


if __name__ == "__main__":
    main()
