#!/usr/bin/env python3
"""Levitate (letslevitate.com) ürün görselleri.

Levitate = protez ayak/blade üreticisi (Forever ayak ailesi, koşu blade'leri,
footshell, taban, adaptör). Özgür Protez ürün görseli hattının 5. markası.

Kaynak: Shopify mağazası. Shopify her mağazada açık bir katalog uçları verir:
  /products.json?limit=250  → tüm ürünler + görsel listesi (orijinal çözünürlük).
HTML kazımaya gerek yok; verilen `src` zaten master dosya (width/height alanları
onu doğruluyor), `?v=` yalnız önbellek damgası.

Össur/Ottobock/Proteor klasörleriyle aynı standart:
  ~/Desktop/Levitate-Protez-Gorselleri/<Kategori>_<ad>/
  Ozgur-protez-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak-<slug>-NN.<ext>
Tekilleştirme ÜRÜN İÇİNDE yapılır, ürünler arası yapılmaz (Össur dersi: markalar
aynı kareyi iki ürün sayfasında kullanabiliyor, global hash klasörü boş bırakır).
"""
import hashlib, json, os, re, shutil, subprocess, time, unicodedata
from urllib.parse import urlparse
import urllib.request

HEDEF = os.path.expanduser("~/Desktop/Levitate-Protez-Gorselleri")
PREFIX = "Ozgur-protez-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak"
API = "https://letslevitate.com/products.json?limit=250"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}

# Levitate'in kendi product_type'ı → klasör adındaki kategori jetonu
KATEGORI = {
    "Forever":   "Ayak",          # protez ayak ailesi
    "Blade":     "Blade",         # koşu/spor ayağı
    "Blade Kit": "Blade-Kit",
    "Footshell": "Ayak-Kilifi",
    "Sole":      "Taban",
    "Adapter":   "Adaptor",
}


def slug(s):
    s = s.replace("®", "").replace("™", "").replace("''", "-inc").replace('"', "-inc")
    s = unicodedata.normalize("NFKD", s.replace("ı", "i").replace("İ", "I")
                              .replace("ş", "s").replace("Ş", "S").replace("ğ", "g")
                              .replace("Ğ", "G").replace("ö", "o").replace("Ö", "O")
                              .replace("ü", "u").replace("Ü", "U").replace("ç", "c")
                              .replace("Ç", "C")).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower())


def temiz_ad(s):
    """Klasör adı: baştaki marka kelimesi düşer (kök klasör zaten Levitate diyor)."""
    s = re.sub(r"^\s*Levitate\s+", "", s)
    s = re.sub(r"[/:\\]", "-", s).replace("''", '"')
    return re.sub(r"\s+", " ", s).strip()


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
    return os.path.splitext(urlparse(url).path)[1].lower() or ".jpg"


def main():
    print("Katalog çekiliyor…", flush=True)
    urunler = json.loads(getir(API))["products"]
    urunler.sort(key=lambda u: (KATEGORI.get(u.get("product_type"), "Z"), u["title"]))
    print(f"{len(urunler)} ürün · {sum(len(u['images']) for u in urunler)} görsel kaydı\n", flush=True)

    if os.path.isdir(HEDEF):
        shutil.rmtree(HEDEF)
    os.makedirs(HEDEF)

    gorulen, rapor, paylasim = {}, [], []
    for u in urunler:
        ad = temiz_ad(u["title"])
        kat = KATEGORI.get(u.get("product_type"), "Diger")
        klasor = os.path.join(HEDEF, f"{kat}_{ad}")
        os.makedirs(klasor, exist_ok=True)

        n, enb, urun_hash = 0, 0, set()
        for im in u["images"]:
            g = im["src"]
            try:
                d = getir(g, ikili=True)
            except Exception as e:
                print(f"    [inmedi] {g} — {e}", flush=True)
                continue
            if len(d) < 2000:
                continue
            h = hashlib.md5(d).hexdigest()
            if h in urun_hash:
                continue
            urun_hash.add(h)
            if h in gorulen:
                paylasim.append((ad, gorulen[h]))
            else:
                gorulen[h] = ad
            n += 1
            yol = os.path.join(klasor, f"{PREFIX}-{slug(u['title'])}-{n:02d}{uzanti(d, g)}")
            with open(yol, "wb") as f:
                f.write(d)
            enb = max(enb, boyut(yol)[0])
            time.sleep(0.15)

        rapor.append((kat, ad, n, enb))
        print(f"[✓] {kat}_{ad}: {n} görsel · en büyük {enb}px", flush=True)

    print("\n=== ÖZET ===")
    print(f"{'KATEGORİ':12} {'ÜRÜN':34} {'görsel':>6} {'en büyük':>9}")
    top = eksik = dusuk = 0
    for kat, ad, n, e in rapor:
        top += n
        bayrak = ""
        if n == 0:
            eksik += 1; bayrak = "  ⚠ GÖRSEL YOK"
        elif e < 800:
            dusuk += 1; bayrak = "  ⚠ düşük çözünürlük"
        print(f"{kat:12} {ad[:34]:34} {n:6} {str(e)+'px':>9}{bayrak}")
    print(f"\nTOPLAM: {top} görsel / {len(urunler)} ürün")
    print(f"  ⚠ görsel bulunamayan: {eksik}   ⚠ 800px altında kalan: {dusuk}")
    if paylasim:
        print("  ⚠ kaynakta paylaşılan kare (aynı fotoğraf iki üründe):")
        for a, b in paylasim:
            print(f"      {a} ↔ {b}")
    print(f"→ {HEDEF}")


if __name__ == "__main__":
    main()
