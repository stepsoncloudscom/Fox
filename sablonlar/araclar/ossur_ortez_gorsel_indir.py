#!/usr/bin/env python3
"""Össur Türkiye — Ortezler (tr-tr) ürün görselleri + veri dökümü.

Kaynak: ossur.com/tr-tr ürün sayfalarını besleyen ürün API'si (bifrost).
Sayfalar client-side render edildiği için HTML'de görsel yok; veri buradan gelir.
Görseller Cloudinary'de; URL'deki dönüşüm bloğu (f_auto,q_auto,w_1400,h_1400,c_pad)
silinince ORİJİNAL dosya iner — betik onu indirir.

`ossur_liner_gorsel_indir.py`nin ortez uyarlaması (28 Ağu 2026). Farklar:
  · YOL = /ortezler/ (109 ürün, 7 kategori)
  · Kategori jetonu slug'ın 2. seviyesinden gelir (diz, omurga, ust-ektremite…)
  · Dosya adı öneki rakip isimleri taşımaz (Linerlerdeki sarı bayrak) —
    "ozgur-protez-ortez-<kategori>-<urun>-NN". Ürün adı Ayhan onayıyla kalır (28 Ağu).
  · Ürün verisi ayrıca CSV + Markdown olarak dökülür (metin turunun ham zemini).

Tekilleştirme ÜRÜN İÇİNDE yapılır. Ürünler ARASI yapılmaz: Össur bazı ürünlerde aynı
stüdyo karesini paylaşıyor; global hash kullanılırsa ikinci ürünün klasörü boş kalır.
Paylaşımlı kareler çalışma sonunda listelenir.
"""
import csv, hashlib, json, os, re, shutil, subprocess, threading, time, unicodedata
from concurrent.futures import ThreadPoolExecutor
import urllib.request

HEDEF = os.path.expanduser("~/Desktop/Ossur-Ortez-Gorselleri")
PREFIX = "ozgur-protez-ortez"
API = ("https://as-bifrost-web-ewh2gnbnaygub5a6.eastus2-01.azurewebsites.net"
       "/api/v2/products?limit=0&loadLevel=full&locale=tr-tr")
YOL = "/ortezler/"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
      "Referer": "https://www.ossur.com/"}

# slug 2. seviyesi → klasör adındaki kategori jetonu (sıra = raporda görünecek sıra)
KATEGORI = {
    "diz": "Diz",
    "ayak-ve-ayakbilegi": "Ayak-Ayakbilegi",
    "omurga": "Omurga",
    "ust-ektremite": "Ust-Ekstremite",
    "kalca": "Kalca",
    "soguk-terapi": "Soguk-Terapi",
    "kalip-odasi-malzemeleri": "Kalip-Odasi",
}
SIRA = {k: i for i, k in enumerate(KATEGORI)}

# ürün görseli değil, özelliğe ait şema/ikon taşıyan alanlar → _Ikon-Piktogram
GORSEL_DISI_ALAN = {"productImages", "productItems", "documents", "productResources",
                    "channels", "channelGeneralOrder", "channelWeb", "channelPortal",
                    "slugs", "options"}

# veri dökümünde taşınacak düz metin alanları
METIN_ALAN = ["shortDescription", "technicalDescription", "featuresAndBenefits",
              "indications", "contraindications", "sizingInformation"]


def slug(s):
    s = s.replace("®", "").replace("™", "").replace("©", "")
    s = unicodedata.normalize("NFKD", s.replace("ı", "i").replace("İ", "I")
                              .replace("ş", "s").replace("Ş", "S").replace("ğ", "g")
                              .replace("Ğ", "G").replace("ö", "o").replace("Ö", "O")
                              .replace("ü", "u").replace("Ü", "U").replace("ç", "c")
                              .replace("Ç", "C")).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower())


def temiz_ad(s):
    return re.sub(r"\s+", " ", re.sub(r"[/:\\]", "-", s.replace("®", "").replace("™", ""))).strip()


def orijinal(url):
    return re.sub(r"/upload/[^/]*(?:f_auto|q_auto|w_\d+|c_pad)[^/]*/", "/upload/", url)


def getir(url, ikili=False, dene=2, sure=75):
    for k in range(dene):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=sure) as r:
                d = r.read()
            return d if ikili else d.decode("utf-8", "ignore")
        except Exception:
            if k == dene - 1:
                raise
            time.sleep(3)


def turev(url, genislik=3000):
    """Cloudinary yüksek çözünürlüklü türev — CDN'den hızlı gelir."""
    return re.sub(r"/upload/[^/]*/", f"/upload/f_auto,q_auto:best,w_{genislik}/", url, count=1)


def gorsel_indir(ham):
    """Önce ORİJİNAL denenir (Ayhan kuralı, 20 Ağu). Cloudinary dönüşümsüz URL'i
    istek anında üretiyor ve bağlantı bazen veri akıtmadan asılı kalıyor — bu yüzden
    kısa zaman aşımı + w_3000 türevine düşüş. Düşenler raporda ayrıca listelenir.
    Döner: (veri, "orijinal"|"turev-3000") ya da (None, sebep)."""
    try:
        return getir(orijinal(ham), ikili=True), "orijinal"
    except Exception as e:
        try:
            return getir(turev(ham), ikili=True, dene=2, sure=90), "turev-3000"
        except Exception as e2:
            return None, f"{type(e).__name__}/{type(e2).__name__}"


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


def kategori_jetonu(u):
    parcalar = (u.get("slug") or "").strip("/").split("/")
    return KATEGORI.get(parcalar[1] if len(parcalar) > 1 else "", "Diger")


def deger(v):
    """API'nin dict/list sarmalayıcılarından okunabilir metin çıkar."""
    if isinstance(v, dict):
        return v.get("value") or v.get("key") or ""
    if isinstance(v, list):
        return " · ".join(x for x in (deger(i) for i in v) if x)
    return str(v) if v is not None else ""


def main():
    print("Ürün verisi çekiliyor…", flush=True)
    veri = json.loads(getir(API))
    urunler = [u for u in veri["results"] if (u.get("slug") or "").startswith(YOL)]
    urunler.sort(key=lambda u: (SIRA.get((u.get("slug") or "").strip("/").split("/")[1], 9),
                                u["productNumber"]))
    print(f"{len(urunler)} ortez ürünü bulundu (toplam katalog: {veri['total_size']})\n", flush=True)

    devam = os.environ.get("FOX_DEVAM") == "1"
    if os.path.isdir(HEDEF) and not devam:
        shutil.rmtree(HEDEF)
    os.makedirs(HEDEF, exist_ok=True)
    ikon_dizin = os.path.join(HEDEF, "_Ikon-Piktogram")
    os.makedirs(ikon_dizin, exist_ok=True)

    ikon_hash, gorulen = set(), {}
    rapor, ikon_say, paylasim, tablo = [], 0, [], []
    dusen, basarisiz, ikon_etiket = [], [], set()
    sayac = {"ikon": 0}

    kilit = threading.Lock()

    def urun_isle(u):
        pn = u["productNumber"]
        ad = temiz_ad(u.get("commercialName") or u.get("internalReferenceName") or pn)
        kat = kategori_jetonu(u)
        klasor = os.path.join(HEDEF, f"{kat}_{pn} - {ad}")
        os.makedirs(klasor, exist_ok=True)
        atla = devam and bool(os.listdir(klasor))

        adaylar = []
        for g in [u.get("mainPictureUrl")] + list(u.get("productImages") or []):
            if isinstance(g, dict):
                g = g.get("url") or g.get("mainPictureUrl")
            if g and g not in adaylar:
                adaylar.append(g)

        n, enb, urun_hash = 0, 0, set()
        for g in ([] if atla else adaylar):
            d, kaynak = gorsel_indir(g)
            if d is None:
                with kilit:
                    basarisiz.append((pn, g, kaynak))
                continue
            if len(d) < 2000:
                continue
            h = hashlib.md5(d).hexdigest()
            if h in urun_hash:
                continue
            urun_hash.add(h)
            with kilit:
                if h in gorulen:
                    paylasim.append((f"{pn} {ad}", gorulen[h]))
                else:
                    gorulen[h] = f"{pn} {ad}"
                if kaynak == "turev-3000":
                    dusen.append((pn, ad))
            n += 1
            dosya = f"{PREFIX}-{slug(kat)}-{slug(ad)}-{n:02d}{uzanti(d, g)}"
            yol = os.path.join(klasor, dosya)
            with open(yol, "wb") as f:
                f.write(d)
            enb = max(enb, boyut(yol)[0])

        if atla:
            mevcut = sorted(f for f in os.listdir(klasor) if not f.startswith("."))
            n = len(mevcut)
            enb = max((boyut(os.path.join(klasor, f))[0] for f in mevcut), default=0)

        # özellik ikonları — köke, tek kopya
        for alan, oge_listesi in ([] if atla else list(u.items())):
            if alan in GORSEL_DISI_ALAN or not isinstance(oge_listesi, list):
                continue
            for oge in oge_listesi:
                g = oge.get("mainPictureUrl") if isinstance(oge, dict) else None
                if not g:
                    continue
                etiket = slug(f"{alan}-{oge.get('value') or oge.get('key') or ''}")
                with kilit:
                    if etiket in ikon_etiket:
                        continue
                    ikon_etiket.add(etiket)
                d, _ = gorsel_indir(g)
                if d is None:
                    continue
                h = hashlib.md5(d).hexdigest()
                with kilit:
                    if h in ikon_hash:
                        continue
                    ikon_hash.add(h)
                    sayac["ikon"] += 1
                with open(os.path.join(ikon_dizin, f"{etiket}{uzanti(d, g)}"), "wb") as f:
                    f.write(d)

        satir = {
            "kategori": kat, "pn": pn, "ad": ad,
            "alt_kategori": deger(u.get("subCategory")),
            "slug": u.get("slug") or "",
            "ce": "evet" if u.get("isCEMarking") else "hayır",
            "ozel_yapim": "evet" if u.get("isCustom") else "hayır",
            "bedenler": deger(u.get("availableSizes")),
            "belge_sayisi": len(u.get("documents") or []),
            "gorsel": n, "en_buyuk_px": enb,
        }
        for m in METIN_ALAN:
            satir[m] = re.sub(r"\s*\n\s*", " / ", (u.get(m) or "")).strip()
        with kilit:
            tablo.append(satir)
            rapor.append((kat, pn, ad, n, enb))
            print(f"[{'atla' if atla else '✓'}] {kat}_{pn} - {ad}: {n} görsel · en büyük {enb}px "
                  f"({len(rapor)}/{len(urunler)})", flush=True)

    with ThreadPoolExecutor(max_workers=8) as havuz:
        list(havuz.map(urun_isle, urunler))
    tablo.sort(key=lambda r: (SIRA.get(r["slug"].strip("/").split("/")[1], 9), r["pn"]))
    rapor.sort(key=lambda r: (r[0], r[1]))

    # --- veri dökümü ---
    csv_yol = os.path.join(HEDEF, "_ortez-urun-verisi.csv")
    with open(csv_yol, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(tablo[0].keys()))
        w.writeheader()
        w.writerows(tablo)
    with open(os.path.join(HEDEF, "_ortez-urun-verisi.json"), "w", encoding="utf-8") as f:
        json.dump(tablo, f, ensure_ascii=False, indent=1)

    print("\n=== ÖZET ===")
    print(f"{'KATEGORİ':17} {'KOD':9} {'ÜRÜN':38} {'görsel':>6} {'en büyük':>9}")
    top = eksik = dusuk = 0
    for kat, pn, ad, n, e in rapor:
        top += n
        bayrak = ""
        if n == 0:
            eksik += 1; bayrak = "  ⚠ GÖRSEL YOK"
        elif e < 800:
            dusuk += 1; bayrak = "  ⚠ düşük çözünürlük"
        print(f"{kat:17} {pn:9} {ad[:38]:38} {n:6} {str(e)+'px':>9}{bayrak}")
    print(f"\nTOPLAM: {top} ürün görseli + {sayac['ikon']} ikon / {len(urunler)} ürün")
    print(f"  ⚠ görsel bulunamayan: {eksik}   ⚠ 800px altında kalan: {dusuk}")
    if dusen:
        print(f"  ⚠ orijinal yerine w_3000 türeviyle inen: {len(dusen)} görsel")
        for a, b in dusen[:20]:
            print(f"      {a} {b}")
    if basarisiz:
        print(f"  ⛔ hiç inmeyen: {len(basarisiz)}")
        for a, g, sbp in basarisiz:
            print(f"      {a} — {sbp}")
    if paylasim:
        print(f"  ⚠ kaynakta paylaşılan kare ({len(paylasim)} adet):")
        for a, b in paylasim[:15]:
            print(f"      {a} ↔ {b}")
    print(f"→ {HEDEF}")
    print(f"→ veri: {csv_yol}")


if __name__ == "__main__":
    main()
