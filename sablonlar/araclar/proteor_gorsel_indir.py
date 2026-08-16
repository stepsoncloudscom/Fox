#!/usr/bin/env python3
"""Proteor ürün görselleri — birleşik geçiş (proteor.com + us.proteor.com modern/eski sayfalar).

Össur/Ottobock klasörleriyle aynı standart:
  ~/Desktop/Proteor-Protez-Gorselleri/<Kategori>_<Ürün>/
  Ozgur-protez-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak-<slug>-NN.<ext>
Ayrılanlar (silinmez):  _Yasam-Kareleri/   insanlı-ortam kareleri
                        _Ikon-Piktogram/   200px altı ikon/şema artıkları
Aynı görsel farklı host/sayfadan gelirse içerik hash'iyle tekilleştirilir.
"""
import hashlib, os, re, shutil, subprocess, time, unicodedata
from urllib.parse import urlparse
import urllib.request

HEDEF = os.path.expanduser("~/Desktop/Proteor-Protez-Gorselleri")
PREFIX = "Ozgur-protez-ossur-ottobock-luxmed-nesa-proklinik-teknik-ortopedi-bacak-ayak"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
G = "https://proteor.com/components/"
U = "https://us.proteor.com/"

# (kategori, ürün, [aday sayfa yolları])
URUNLER = [
    ("Sistem", "SYNSYS", [G+"synsys-prosthetic-knee-ankle-foot-synergetic-system/", U+"knees/synsys/"]),
    ("Diz", "Quattro", [G+"proteor-quattro/", U+"knees/proteor-quattro/"]),
    ("Diz", "Plie 3", [G+"plie-3-knee-prosthesis/", U+"knees/plie-3/", U+"composants/freedom-plie-3-prosthesis/"]),
    ("Diz", "ALLUX 2", [G+"allux-2-polycentric-hydraulic-knee-prosthesis/", U+"composants/allux-2-polycentric-hydraulic-knee-prosthesis/"]),
    ("Diz", "Hytrek", [G+"hytrek-knee-prosthesis/", U+"knees/hytrek/", U+"composants/hytrek-knee-prosthesis/"]),
    ("Diz", "Hydeal II", [G+"hydeal-2-knee-prothesis/", U+"composants/hydeal-2-knee-prothesis/"]),
    ("Diz", "Matik", [G+"pneumatic-knee-prosthesis-matik/", U+"knees/matik/", U+"composants/pneumatic-knee-prosthesis-matik/"]),
    ("Diz", "Symphony", [G+"6-bar-knee-prosthesis-with-stance-flex-symphony/", U+"knees/symphony/", U+"composants/6-bar-knee-prosthesis-with-stance-flex-symphony/"]),
    ("Diz", "1M112-1M113", [G+"knee-prosthesis-children-adolescent-women-1m112-1m113/", U+"knees/1m112/", U+"knees/1m-series/"]),
    ("Diz", "Easy Ride", [G+"easy-ride-sport-knee-prosthesis/", U+"knees/easyride/", U+"composants/easy-ride-sport-knee-prosthesis/"]),
    ("Ayak", "Kinnex 2.0", [G+"kinnex-2-0-prosthesis/", U+"ankles/kinnex-2-0/", U+"composants/freedom-kinnex-2-0-prosthesis/"]),
    ("Ayak", "Kinterra", [G+"kinterra-prosthesis-ankle/", U+"ankles/kinterra/", U+"composants/freedom-kinterra-2-0-prosthesis/"]),
    ("Ayak", "Shockwave", [G+"shockwave-prosthetic-foot/", U+"feet/shockwave/"]),
    ("Ayak", "Dynatrek", [G+"dynatrek-foot-prosthesis/", U+"composants/dynatrek-foot-prosthesis/"]),
    ("Ayak", "Sierra", [G+"sierra-prosthtetic-foot/", U+"feet/sierra/", U+"composants/freedom-sierra-prosthtetic-foot/"]),
    ("Ayak", "Highlander - Highlander Max", [G+"highlander-and-highlander-max-foot-prosthesis/", U+"feet/highlander/", U+"composants/highlander-and-highlander-max-foot-prosthesis/"]),
    ("Ayak", "Agilix", [G+"agilix-foot-prosthesis/", U+"feet/agilix/", U+"composants/freedom-agilix-foot-prosthesi/"]),
    ("Ayak", "DynAdapt", [G+"dynadapt/", U+"feet/dynadapt/"]),
    ("Ayak", "Exalto", [G+"exalto/"]),
    ("Ayak", "ETHOS LP", [G+"ethos-lp/", U+"feet/ethos-lp/"]),
    ("Ayak", "ETHOS LP for Kids", [G+"ethos-lp-for-kids/"]),
    ("Ayak", "Pacifica - Pacifica LP", [G+"pacifica-and-pacifica-lp-prosthesis/", U+"feet/pacifica/", U+"composants/freedom-pacifica-and-pacifica-lp-prosthesis/"]),
    ("Ayak", "Dynacity", [G+"dynacity-prosthetic-foot/", U+"composants/dynacity-prosthetic-foot/"]),
    ("Ayak", "Dynastep", [G+"dynastep-foot-prosthesis/", U+"feet/proteor-dyna-step/", U+"composants/dynastep-foot-prosthesis/"]),
    ("Ayak", "Gery", [G+"gery-prothetic-foot/", U+"feet/gery/", U+"composants/gery-prothetic-foot/"]),
    ("Ayak", "RUSH HiPro", [G+"rush-hipro-prothesis-foot/", U+"feet/hipro/", U+"composants/rush-hipro-prothesis/"]),
    ("Ayak", "RUSH ROGUE 2", [G+"rush-hipro-rogue-amputated-foot-prosthesis/", U+"feet/rogue-2/", U+"composants/rush-hipro-rogue-amputated-foot-prosthesis/"]),
    ("Ayak", "RUSH RAMPAGE LP", [G+"rush-rampage-lp-foot-prothesis/", U+"feet/rampage-lp-2/", U+"feet/rampage/", U+"composants/rush-rampage-lp-foot-prothesis/"]),
    ("Ayak", "RUSH EVAQ8", [G+"prosthetic-foot-evaq8/", U+"composants/prosthetic-foot-evaq8/"]),
    ("Ayak", "RUSH ROVER", [G+"rush-rover-ultra-low-profile-foot-prothesis/", U+"feet/rover/", U+"composants/rush-rover-ultra-low-profile-foot-prothesis/"]),
    ("Ayak", "RUSH Chopart", [G+"prothesis-rush-foot-chopart/", U+"feet/chopart/", U+"composants/prothesis-rush-foot-chopart/"]),
    ("Ayak", "RUSH Kid", [G+"rush-kid-amputated-foot-prosthesis/", U+"feet/kid/", U+"composants/rush-kid-amputated-foot-prosthesis/"]),
    ("Ayak", "RUSH H2O", [G+"rush-h2o-collection-feet-prothesis/", U+"composants/rush-h2o-collection-prothesis/"]),
    ("Ayak", "Hopper Blade", [G+"hopper-blade/", U+"feet/hopper/"]),
    ("Ayak", "Easy Run", [G+"sport-blade-easy-run-running-prosthesis/", U+"feet/easyrun-blade/", U+"composants/sport-blade-easy-run-running-prosthesis/"]),
]

SABLON = re.compile(
    r"(logo|favicon|placeholder|avatar|flag|drapeau|banniere|sprite|arrow|fleche|^bg-|pattern|"
    r"newsletter|linkedin|facebook|youtube|instagram|twitter|cookie|loader|spinner|human-?first)", re.I)
YASAM = re.compile(r"(lifestyle|life-?style|ambiance|^FI_|_FI_|hero|cover|team|patient)", re.I)
GORSEL_RE = re.compile(
    r'https?://(?:[a-z0-9-]+\.)?proteor\.com/wp-content/uploads/[^\s"\'<>)\\]+?\.(?:jpg|jpeg|png|webp)', re.I)


def slug(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower())


def normalize(u):
    return re.sub(r"-\d{2,4}x\d{2,4}(\.(?:jpg|jpeg|png|webp))$", r"\1", u, flags=re.I).replace("http://", "https://")


def getir(url, ikili=False, dene=2):
    for k in range(dene):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45) as r:
                d = r.read()
            return d if ikili else d.decode("utf-8", "ignore")
        except Exception:
            if k == dene - 1:
                raise
            time.sleep(1.5)


def kendi_bolgesi(html):
    a = html.find("main-content")
    a = a if a >= 0 else 0
    sonlar = [x for x in (html.find("Complementary Products", a), html.find("<footer", a)) if x > a]
    return html[a:min(sonlar)] if sonlar else html[a:]


def boyut(yol):
    try:
        o = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", yol],
                           capture_output=True, text=True, timeout=20).stdout
        w = re.search(r"pixelWidth:\s*(\d+)", o)
        h = re.search(r"pixelHeight:\s*(\d+)", o)
        return (int(w.group(1)), int(h.group(1))) if w and h else (0, 0)
    except Exception:
        return (0, 0)


def main():
    if os.path.isdir(HEDEF):
        shutil.rmtree(HEDEF)
    os.makedirs(HEDEF)

    rapor = []
    for kategori, ad, sayfalar in URUNLER:
        adaylar = []
        for s in sayfalar:
            try:
                html = getir(s)
            except Exception as e:
                print(f"    [sayfa yok] {s} — {e}", flush=True)
                continue
            for u in GORSEL_RE.findall(kendi_bolgesi(html)):
                t = normalize(u)
                if SABLON.search(os.path.basename(t)):
                    continue
                if t not in adaylar:
                    adaylar.append(t)
            time.sleep(0.3)

        klasor = os.path.join(HEDEF, f"{kategori}_{ad}")
        os.makedirs(klasor, exist_ok=True)
        hashler, n, y, ikon = set(), 0, 0, 0
        for g in adaylar:
            try:
                veri = getir(g, ikili=True)
            except Exception:
                continue
            if len(veri) < 2000:
                continue
            h = hashlib.md5(veri).hexdigest()
            if h in hashler:                      # aynı görsel başka host/sayfadan
                continue
            hashler.add(h)
            ext = os.path.splitext(urlparse(g).path)[1].lower()
            gecici = os.path.join(klasor, f".gecici{ext}")
            with open(gecici, "wb") as f:
                f.write(veri)
            w, hh = boyut(gecici)
            if bool(YASAM.search(os.path.basename(g))):
                alt = os.path.join(klasor, "_Yasam-Kareleri"); y += 1
                hedef = os.path.join(alt, os.path.basename(g))
            elif w and w < 200:                   # ikon / piktogram artığı
                alt = os.path.join(klasor, "_Ikon-Piktogram"); ikon += 1
                hedef = os.path.join(alt, os.path.basename(g))
            else:
                alt = klasor; n += 1
                hedef = os.path.join(klasor, f"{PREFIX}-{slug(ad)}-{n:02d}{ext}")
            os.makedirs(alt, exist_ok=True)
            shutil.move(gecici, hedef)
            time.sleep(0.25)

        enb = max([boyut(os.path.join(klasor, f))[0]
                   for f in os.listdir(klasor) if f.startswith(PREFIX)] or [0])
        rapor.append((kategori, ad, n, y, ikon, enb))
        print(f"[✓] {kategori}_{ad}: {n} ürün · {y} yaşam · {ikon} ikon · en büyük {enb}px", flush=True)

    print("\n=== ÖZET ===")
    print(f"{'':7} {'ÜRÜN':32} {'ürün':>5} {'yaşam':>6} {'ikon':>5} {'en büyük':>9}")
    top = yas = eksik = dusuk = 0
    for k, a, n, y, i, e in rapor:
        top += n; yas += y
        bayrak = ""
        if n == 0:
            eksik += 1; bayrak = "  ⚠ ÜRÜN ÇEKİMİ YOK"
        elif e < 800:
            dusuk += 1; bayrak = "  ⚠ düşük çözünürlük"
        print(f"{k:7} {a:32} {n:5} {y:6} {i:5} {str(e)+'px':>9}{bayrak}")
    print(f"\nTOPLAM: {top} ürün görseli + {yas} yaşam karesi / {len(URUNLER)} ürün")
    print(f"  ⚠ ürün çekimi bulunamayan: {eksik}   ⚠ 800px altında kalan: {dusuk}")
    print(f"→ {HEDEF}")


if __name__ == "__main__":
    main()
