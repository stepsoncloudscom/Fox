#!/usr/bin/env python3
"""Össur Türkiye — Linerler (tr-tr) ürün görselleri.

Kaynak: ossur.com/tr-tr ürün sayfalarını besleyen ürün API'si (bifrost).
Sayfalar client-side render edildiği için HTML'de görsel yok; veri buradan gelir.
Görseller Cloudinary'de; URL'deki dönüşüm bloğu (f_auto,q_auto,w_1400,h_1400,c_pad)
silinince ORİJİNAL (3000px) dosya iner — betik onu indirir.

Proteor/Ottobock klasörleriyle aynı standart:
  ~/Desktop/Ossur-Liner-Gorselleri/<Kategori>_<PN kodu> - <ad>/
  Ozgur-protez-liner-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak-<slug>-NN.<ext>
Ayrılan:  _Ikon-Piktogram/   ürüne değil özelliğe ait şema/ikonlar (markanın tamamında
                             ortak kullanıldığı için ürün klasörüne değil köke, tek kopya)
Aynı görsel iki üründen gelirse içerik hash'iyle tekilleştirilir.
"""
import hashlib, json, os, re, shutil, subprocess, time, unicodedata
import urllib.request

HEDEF = os.path.expanduser("~/Desktop/Ossur-Liner-Gorselleri")
PREFIX = "Ozgur-protez-liner-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak"
API = ("https://as-bifrost-web-ewh2gnbnaygub5a6.eastus2-01.azurewebsites.net"
       "/api/v2/products?limit=0&loadLevel=full&locale=tr-tr")
YOL = "/linerler/"          # tr-tr'de Linerler kategorisinin slug'ı
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
      "Referer": "https://www.ossur.com/"}

# Össur'un alt kategorisi → klasör adındaki kategori jetonu
KATEGORI = {
    "Liners": "Liner",
    "Liner socks": "Liner-Corap",
    "Accessories": "Liner-Aksesuar",
    "Tools and materials": "Liner-Arac",
}

# ürüne değil özelliğe ait görsel taşıyan alanlar → _Ikon-Piktogram
IKON_ALANLARI = ["characteristics", "impactLevels", "amputationLevel", "suspensionMethod",
                 "residualLimbShape", "residualLimbLength", "residualLimbCondition",
                 "softTissueCoverage", "softTissueStatus", "handDexterity"]


def slug(s):
    s = s.replace("®", "").replace("™", "").replace("©", "")
    s = unicodedata.normalize("NFKD", s.replace("ı", "i").replace("İ", "I")
                              .replace("ş", "s").replace("Ş", "S").replace("ğ", "g")
                              .replace("Ğ", "G").replace("ö", "o").replace("Ö", "O")
                              .replace("ü", "u").replace("Ü", "U").replace("ç", "c")
                              .replace("Ç", "C")).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower())


def temiz_ad(s):
    """Klasör adı için: ® ™ ve dosya sistemine uymayan karakterler dışarı."""
    return re.sub(r"\s+", " ", re.sub(r"[/:\\]", "-", s.replace("®", "").replace("™", ""))).strip()


def orijinal(url):
    """Cloudinary dönüşüm bloğunu at → orijinal çözünürlük."""
    return re.sub(r"/upload/[^/]*(?:f_auto|q_auto|w_\d+|c_pad)[^/]*/", "/upload/", url)


def getir(url, ikili=False, dene=3):
    for k in range(dene):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                d = r.read()
            return d if ikili else d.decode("utf-8", "ignore")
        except Exception:
            if k == dene - 1:
                raise
            time.sleep(2)


def boyut(yol):
    try:
        o = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", yol],
                           capture_output=True, text=True, timeout=30).stdout
        w = re.search(r"pixelWidth:\s*(\d+)", o)
        h = re.search(r"pixelHeight:\s*(\d+)", o)
        return (int(w.group(1)), int(h.group(1))) if w and h else (0, 0)
    except Exception:
        return (0, 0)


def uzanti(veri, url):
    if veri[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    if veri[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if veri[:4] == b"RIFF" and veri[8:12] == b"WEBP":
        return ".webp"
    return os.path.splitext(url)[1].lower() or ".jpg"


def main():
    print("Ürün verisi çekiliyor…", flush=True)
    veri = json.loads(getir(API))
    urunler = [u for u in veri["results"] if YOL in (u.get("slug") or "")]
    urunler.sort(key=lambda u: (KATEGORI.get((u.get("subCategory") or {}).get("value"), "Z"),
                                u["productNumber"]))
    print(f"{len(urunler)} liner ürünü bulundu (toplam katalog: {veri['total_size']})\n", flush=True)

    if os.path.isdir(HEDEF):
        shutil.rmtree(HEDEF)
    os.makedirs(HEDEF)
    ikon_dizin = os.path.join(HEDEF, "_Ikon-Piktogram")
    os.makedirs(ikon_dizin)

    genel_hash, ikon_hash = set(), set()
    rapor, ikon_say = [], 0

    for u in urunler:
        pn = u["productNumber"]
        ad = temiz_ad(u.get("commercialName") or u.get("internalReferenceName") or pn)
        kat = KATEGORI.get((u.get("subCategory") or {}).get("value"), "Liner")
        klasor = os.path.join(HEDEF, f"{kat}_{pn} - {ad}")
        os.makedirs(klasor, exist_ok=True)

        adaylar = []
        for g in [u.get("mainPictureUrl")] + list(u.get("productImages") or []):
            if g:
                o = orijinal(g)
                if o not in adaylar:
                    adaylar.append(o)

        n, enb = 0, 0
        for g in adaylar:
            try:
                d = getir(g, ikili=True)
            except Exception as e:
                print(f"    [inmedi] {g} — {e}", flush=True)
                continue
            if len(d) < 2000:
                continue
            h = hashlib.md5(d).hexdigest()
            if h in genel_hash:
                continue
            genel_hash.add(h)
            n += 1
            yol = os.path.join(klasor, f"{PREFIX}-{slug(ad)}-{n:02d}{uzanti(d, g)}")
            with open(yol, "wb") as f:
                f.write(d)
            enb = max(enb, boyut(yol)[0])
            time.sleep(0.2)

        # özellik ikonları — köke, tek kopya
        for alan in IKON_ALANLARI:
            for oge in (u.get(alan) or []):
                g = oge.get("mainPictureUrl") if isinstance(oge, dict) else None
                if not g:
                    continue
                try:
                    d = getir(orijinal(g), ikili=True)
                except Exception:
                    continue
                h = hashlib.md5(d).hexdigest()
                if h in ikon_hash:
                    continue
                ikon_hash.add(h)
                ikon_say += 1
                etiket = slug(f"{alan}-{oge.get('value') or oge.get('key') or ''}")
                with open(os.path.join(ikon_dizin, f"{etiket}{uzanti(d, g)}"), "wb") as f:
                    f.write(d)
                time.sleep(0.15)

        rapor.append((kat, pn, ad, n, enb))
        print(f"[✓] {kat}_{pn} - {ad}: {n} görsel · en büyük {enb}px", flush=True)

    print("\n=== ÖZET ===")
    print(f"{'KATEGORİ':16} {'KOD':9} {'ÜRÜN':34} {'görsel':>6} {'en büyük':>9}")
    top = eksik = dusuk = 0
    for kat, pn, ad, n, e in rapor:
        top += n
        bayrak = ""
        if n == 0:
            eksik += 1; bayrak = "  ⚠ GÖRSEL YOK"
        elif e < 800:
            dusuk += 1; bayrak = "  ⚠ düşük çözünürlük"
        print(f"{kat:16} {pn:9} {ad[:34]:34} {n:6} {str(e)+'px':>9}{bayrak}")
    print(f"\nTOPLAM: {top} ürün görseli + {ikon_say} ikon / {len(urunler)} ürün")
    print(f"  ⚠ görsel bulunamayan: {eksik}   ⚠ 800px altında kalan: {dusuk}")
    print(f"→ {HEDEF}")


if __name__ == "__main__":
    main()
