#!/usr/bin/env python3
"""Instagram haftalık döngü — pazartesi onay kartı üretici.

Kuyrukta kartta bekleyen paketleri (onay bekliyor · deneme karelerinde) tek bir HTML sayfasına
dizer. Görseller en çok 1600 px'e küçültülür, büyük videolar 720p önizlemeye çevrilir.
Çıktı dizini Artifact olarak yayınlanır (pazartesi protokolü).

Kullanım:
    python3 sablonlar/araclar/instagram_onay_karti.py <cikti_dizini> [--kuyruk PATH] [--paket-koku PATH]
"""
import argparse
import html
import shutil
import subprocess
import sys
from datetime import date
from pathlib import Path

try:
    from sablonlar.araclar.instagram_kuyruk import KARTTA, TIRE, VARSAYILAN_KUYRUK, Kuyruk, KuyrukHatasi, oku, ozet_satiri
except ImportError:  # betik doğrudan çalıştırıldığında
    sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
    from sablonlar.araclar.instagram_kuyruk import KARTTA, TIRE, VARSAYILAN_KUYRUK, Kuyruk, KuyrukHatasi, oku, ozet_satiri

PAKET_KOKU = Path.home() / "Desktop" / "Steps On Clouds" / "Design " / "Instagram" / "Paketler"
GORSEL = {".jpg", ".jpeg", ".png", ".webp"}
VIDEO = {".mp4", ".mov"}
GORSEL_MAKS_PX = 1600
FFMPEG_YEDEK = Path.home() / ".local" / "bin" / "ffmpeg"

CSS = """
:root { --bg:#f7f6f3; --kart:#ffffff; --metin:#1c1c1a; --soluk:#6b6a66; --cizgi:#e3e1dc; --vurgu:#0a8ea0; --uyari:#b4471c; }
@media (prefers-color-scheme: dark) { :root:not([data-theme="light"]) { --bg:#141413; --kart:#1f1f1d; --metin:#ecebe7; --soluk:#a3a29d; --cizgi:#33322f; --vurgu:#3cc3d4; --uyari:#f08a5d; } }
:root[data-theme="dark"] { --bg:#141413; --kart:#1f1f1d; --metin:#ecebe7; --soluk:#a3a29d; --cizgi:#33322f; --vurgu:#3cc3d4; --uyari:#f08a5d; }
* { box-sizing:border-box; }
body { margin:0; background:var(--bg); color:var(--metin); font:16px/1.5 -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
main { max-width:900px; margin:0 auto; padding:24px 16px 64px; }
header p { color:var(--soluk); margin:4px 0 0; }
section { background:var(--kart); border:1px solid var(--cizgi); border-radius:12px; padding:20px; margin-top:20px; }
h1 { font-size:1.5rem; margin:0; } h2 { font-size:1.2rem; margin:0 0 4px; } h3 { font-size:.95rem; margin:16px 0 6px; color:var(--soluk); }
.meta { color:var(--soluk); font-size:.9rem; }
.asama { display:inline-block; font-weight:600; color:var(--vurgu); }
.medya { display:grid; grid-template-columns:repeat(auto-fill, minmax(220px, 1fr)); gap:10px; margin-top:12px; }
.medya img, .medya video { width:100%; height:auto; border-radius:8px; background:var(--cizgi); }
pre { white-space:pre-wrap; word-wrap:break-word; background:var(--bg); border:1px solid var(--cizgi); border-radius:8px; padding:12px; font:inherit; margin:0; }
.uyari { color:var(--uyari); font-weight:600; }
.karar { margin-top:16px; padding-top:12px; border-top:1px solid var(--cizgi); font-weight:600; }
@media (max-width:600px) { .medya { grid-template-columns:1fr; } section { padding:16px; } }
"""


def _ffmpeg():
    yol = shutil.which("ffmpeg")
    if yol:
        return yol
    return str(FFMPEG_YEDEK) if FFMPEG_YEDEK.exists() else None


def _gorsel_kopyala(kaynak: Path, hedef: Path) -> None:
    shutil.copy2(kaynak, hedef)
    try:
        cikti = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(hedef)],
                               capture_output=True, text=True, check=True).stdout
        boyutlar = [int(s.split(":")[1]) for s in cikti.splitlines() if "pixel" in s]
        if boyutlar and max(boyutlar) > GORSEL_MAKS_PX:
            subprocess.run(["sips", "--resampleHeightWidthMax", str(GORSEL_MAKS_PX), str(hedef)],
                           capture_output=True, check=True)
    except (OSError, subprocess.CalledProcessError, ValueError):
        pass  # sips yoksa ya da okuyamazsa özgün kopya kalır


def _video_hazirla(kaynak: Path, hedef_dizin: Path, esik: int):
    """Önizleme dosyasının yolunu döndürür; üretilemezse None."""
    if kaynak.stat().st_size <= esik:
        hedef = hedef_dizin / kaynak.name
        shutil.copy2(kaynak, hedef)
        return hedef
    ffmpeg = _ffmpeg()
    if not ffmpeg:
        return None
    hedef = hedef_dizin / (kaynak.stem + ".mp4")
    r = subprocess.run(
        [ffmpeg, "-y", "-loglevel", "error", "-i", str(kaynak), "-vf", "scale=-2:720",
         "-c:v", "libx264", "-crf", "28", "-preset", "veryfast", "-pix_fmt", "yuv420p",
         "-movflags", "+faststart", "-an", str(hedef)],
        capture_output=True,
    )
    return hedef if r.returncode == 0 and hedef.exists() else None


def _metin_blogu(baslik: str, yol: Path) -> str:
    if not yol.exists():
        return ""
    return f"<h3>{html.escape(baslik)}</h3><pre>{html.escape(yol.read_text(encoding='utf-8'))}</pre>"


def _bolum(s, paket_koku: Path, cikti: Path, esik: int) -> str:
    e = html.escape
    asama = "Yön onayı" if s.durum == "deneme karelerinde" else "Yayın onayı"
    kredi = f"{s.kredi} kredi" if s.kredi else "kredi harcanmadı"
    parcalar = [
        f'<section id="madde-{e(s.madde)}">',
        f"<h2>{e(s.madde)} · {e(s.baslik)}</h2>",
        f'<p class="meta"><span class="asama">{asama}</span> · {e(s.tarih.isoformat() if s.tarih else "—")} {e(s.saat)}'
        f" · {e(s.hat)} · {e(s.yol)}{' · video' if s.video else ''} · {e(kredi)} · tur {s.tur}</p>",
    ]
    if s.not_ and s.not_ not in TIRE:
        parcalar.append(f'<p class="meta">{e(s.not_)}</p>')
    paket = None if s.paket in TIRE else paket_koku / s.paket
    if paket is None or not paket.is_dir():
        parcalar.append(f'<p class="uyari">paket klasörü bulunamadı: {e(str(paket_koku / s.paket))}</p>')
    else:
        hedef_dizin = cikti / "medya" / s.madde
        hedef_dizin.mkdir(parents=True, exist_ok=True)
        medya = []
        for dosya in sorted(paket.iterdir()):
            uzanti = dosya.suffix.lower()
            if uzanti in GORSEL:
                _gorsel_kopyala(dosya, hedef_dizin / dosya.name)
                medya.append(f'<img src="medya/{e(s.madde)}/{e(dosya.name)}" alt="{e(s.madde)} · {e(dosya.name)}" loading="lazy">')
            elif uzanti in VIDEO:
                onizleme = _video_hazirla(dosya, hedef_dizin, esik)
                if onizleme is None:
                    medya.append(f'<p class="uyari">video önizlemesi üretilemedi: {e(str(dosya))}</p>')
                else:
                    medya.append(f'<video src="medya/{e(s.madde)}/{e(onizleme.name)}" controls playsinline preload="metadata"></video>')
        if medya:
            parcalar.append('<div class="medya">' + "".join(medya) + "</div>")
        parcalar.append(_metin_blogu("Yön kartı", paket / "yon-karti.md"))
        parcalar.append(_metin_blogu("Metin", paket / "metin.md"))
        parcalar.append(_metin_blogu("Denetmen", paket / "denetmen.md"))
    parcalar.append('<p class="karar">Karar: Onay · Revize (not) · Çıkar — oturumda söyle</p>')
    parcalar.append("</section>")
    return "\n".join(p for p in parcalar if p)


def kart_uret(k: Kuyruk, cikti: Path, paket_koku: Path = PAKET_KOKU, video_esik_bayt: int = 14 * 1024 * 1024) -> Path:
    cikti = Path(cikti)
    cikti.mkdir(parents=True, exist_ok=True)
    eski_medya = cikti / "medya"
    if eski_medya.exists():
        shutil.rmtree(eski_medya)
    bekleyen = sorted((s for s in k.slotlar if s.durum in KARTTA), key=lambda s: (s.tarih or date.max, s.madde))
    govde = [_bolum(s, Path(paket_koku), cikti, video_esik_bayt) for s in bekleyen]
    if not govde:
        govde = ['<section><p>Kartta bekleyen paket yok.</p></section>']
    sayfa = (
        '<!doctype html>\n<html lang="tr">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        "<title>Instagram Onay Kartı</title>\n"
        f"<style>{CSS}</style>\n</head>\n<body>\n<main>\n"
        "<header><h1>Instagram Onay Kartı</h1>"
        f"<p>{html.escape(ozet_satiri(k, date.today()))}</p></header>\n"
        + "\n".join(govde)
        + "\n</main>\n</body>\n</html>\n"
    )
    index = cikti / "index.html"
    index.write_text(sayfa, encoding="utf-8")
    return index


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Instagram onay kartı üretici")
    p.add_argument("cikti", type=Path)
    p.add_argument("--kuyruk", type=Path, default=VARSAYILAN_KUYRUK)
    p.add_argument("--paket-koku", type=Path, default=PAKET_KOKU)
    a = p.parse_args(argv)
    try:
        k = oku(a.kuyruk)
    except (KuyrukHatasi, OSError) as e:
        print(f"Instagram: kuyruk okunamadı — {e}")
        return 2
    print(kart_uret(k, a.cikti, paket_koku=a.paket_koku))
    return 0


if __name__ == "__main__":
    sys.exit(main())
