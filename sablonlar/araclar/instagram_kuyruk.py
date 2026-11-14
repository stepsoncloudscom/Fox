#!/usr/bin/env python3
"""Instagram haftalık döngü — kuyruk aracı.

Kuyruk dosyası (raporlar/instagram-kuyruk.md) tek doğruluk kaynağıdır. Bu araç onu okur,
tamponu ve kendini durdurma kararını hesaplar, "haftada en çok 1 video / en az 2 gönderi"
kuralını denetler, sabah brifingi satırını üretir.

Tasarım: raporlar/tasarim-instagram-haftalik-dongu-2026-11-14.md

Kullanım:
    python3 sablonlar/araclar/instagram_kuyruk.py ozet    [--kuyruk PATH] [--bugun YYYY-MM-DD]
    python3 sablonlar/araclar/instagram_kuyruk.py denetle [--kuyruk PATH]   # 0 temiz · 1 ihlal · 2 okuma hatası
    python3 sablonlar/araclar/instagram_kuyruk.py durum   [--kuyruk PATH] [--bugun YYYY-MM-DD]  # DURAKLAT | DEVAM
"""
import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date, timedelta
from pathlib import Path
from typing import List, Optional, Tuple

DURUMLAR = (
    "havuzda", "deneme karelerinde", "üretimde", "denetimde", "onay bekliyor",
    "onaylandı", "zamanlandı", "yayında", "revize", "park", "çıkarıldı", "yedek",
)
HAZIR = {"onaylandı", "zamanlandı", "yayında"}
KARTTA = {"onay bekliyor", "deneme karelerinde"}
PASIF = {"park", "çıkarıldı", "yedek"}

GOREV_DURUMLARI = {"AKTİF", "KURU", "DURAKLADI"}
BOLUMLER = {"sayaçlar", "slotlar", "kararlar", "heartbeat"}

SUTUN_SAYISI = 12
TIRE = {"—", "-", ""}
VARSAYILAN_KUYRUK = Path(__file__).resolve().parents[2] / "raporlar" / "instagram-kuyruk.md"


class KuyrukHatasi(ValueError):
    pass


@dataclass
class Slot:
    tarih: Optional[date]
    saat: str
    madde: str
    baslik: str
    hat: str
    yol: str
    video: bool
    durum: str
    tur: int
    kredi: int
    paket: str
    not_: str


@dataclass
class Kuyruk:
    gorev: str
    sebep: str
    bakiye: Optional[int]
    donem_harcama: int
    slotlar: List[Slot] = field(default_factory=list)
    kararlar: List[Tuple[date, str, str, str]] = field(default_factory=list)
    heartbeat: List[Tuple[date, str, str]] = field(default_factory=list)


def _tarih(metin: str, no: int) -> date:
    try:
        return date.fromisoformat(metin.strip())
    except ValueError:
        raise KuyrukHatasi(f"satır {no}: geçersiz tarih '{metin.strip()}'")


def _int(metin: str, no: int, ad: str) -> int:
    try:
        return int(metin.strip())
    except ValueError:
        raise KuyrukHatasi(f"satır {no}: {ad} sayı değil '{metin.strip()}'")


def _hucreler(satir: str) -> List[str]:
    return [h.strip() for h in satir.strip().strip("|").split("|")]


def _tablo_satiri_mi(satir: str) -> bool:
    s = satir.strip()
    return s.startswith("|") and not re.fullmatch(r"\|[\s\-:|]+\|?", s)


def oku(yol: Path) -> Kuyruk:
    try:
        satirlar = Path(yol).read_text(encoding="utf-8").splitlines()
    except UnicodeDecodeError as e:
        raise KuyrukHatasi(f"dosya UTF-8 değil ({e.reason}, bayt {e.start})")
    k = Kuyruk(gorev="?", sebep="", bakiye=None, donem_harcama=0)
    bolum = None
    baslik_gecti = False
    gorulen = set()
    for no, satir in enumerate(satirlar, start=1):
        if satir.startswith("## "):
            bolum = satir[3:].strip().lower()
            if bolum not in BOLUMLER:
                raise KuyrukHatasi(f"satır {no}: bilinmeyen bölüm '{satir[3:].strip()}' (beklenen: Sayaçlar, Slotlar, Kararlar, Heartbeat)")
            gorulen.add(bolum)
            baslik_gecti = False
            continue
        if bolum == "sayaçlar" and satir.startswith("- "):
            anahtar, _, deger = satir[2:].partition(":")
            anahtar, deger = anahtar.strip(), deger.strip()
            if anahtar == "görev":
                durum, _, sebep = deger.partition("—")
                k.gorev, k.sebep = durum.strip(), sebep.strip()
            elif anahtar == "bakiye":
                ilk = deger.split()[0] if deger else "?"
                k.bakiye = None if ilk == "?" else _int(ilk, no, "bakiye")
            elif anahtar == "dönem harcaması":
                if not deger:
                    raise KuyrukHatasi(f"satır {no}: dönem harcaması boş")
                k.donem_harcama = _int(deger.split()[0], no, "dönem harcaması")
            continue
        if not _tablo_satiri_mi(satir):
            continue
        if not baslik_gecti:  # her tablonun ilk satırı başlıktır
            baslik_gecti = True
            continue
        h = _hucreler(satir)
        if bolum == "slotlar":
            if len(h) != SUTUN_SAYISI:
                raise KuyrukHatasi(f"satır {no}: {SUTUN_SAYISI} sütun bekleniyor, {len(h)} var")
            durum = h[7]
            if durum not in DURUMLAR:
                raise KuyrukHatasi(f"satır {no}: bilinmeyen durum '{durum}'")
            if h[0] in TIRE:
                if durum not in PASIF:
                    raise KuyrukHatasi(f"satır {no}: geçersiz tarih '—' (yalnız park/çıkarıldı/yedek tarihsiz olabilir)")
                tarih = None
            else:
                tarih = _tarih(h[0], no)
            if h[6] not in ("evet", "hayır"):
                raise KuyrukHatasi(f"satır {no}: video 'evet' ya da 'hayır' olmalı, '{h[6]}' var")
            k.slotlar.append(Slot(
                tarih=tarih, saat=h[1], madde=h[2], baslik=h[3], hat=h[4], yol=h[5],
                video=h[6] == "evet", durum=durum, tur=_int(h[8], no, "tur"),
                kredi=_int(h[9], no, "kredi"), paket=h[10], not_=h[11],
            ))
        elif bolum == "kararlar":
            if len(h) < 4:
                raise KuyrukHatasi(f"satır {no}: karar satırı 4 sütun bekliyor")
            k.kararlar.append((_tarih(h[0], no), h[1], h[2], h[3]))
        elif bolum == "heartbeat":
            if len(h) < 3:
                raise KuyrukHatasi(f"satır {no}: heartbeat satırı 3 sütun bekliyor")
            k.heartbeat.append((_tarih(h[0], no), h[1], h[2]))
    eksik = BOLUMLER - gorulen
    if eksik:
        raise KuyrukHatasi(f"eksik bölüm: {', '.join(sorted(eksik))}")
    if k.gorev not in GOREV_DURUMLARI:
        raise KuyrukHatasi(f"görev satırı eksik ya da geçersiz: '{k.gorev}' (AKTİF, KURU ya da DURAKLADI olmalı)")
    return k


def hafta_baslangici(g: date) -> date:
    return g - timedelta(days=g.weekday())


def _aktif_tarihli(k: Kuyruk) -> List[Slot]:
    return [s for s in k.slotlar if s.tarih is not None and s.durum not in PASIF]


def tampon_gun(k: Kuyruk, bugun: date) -> int:
    gelecek = sorted((s for s in _aktif_tarihli(k) if s.tarih >= bugun), key=lambda s: s.tarih)
    if not gelecek:
        return 0
    for s in gelecek:
        if s.durum not in HAZIR:
            return (s.tarih - bugun).days
    return (gelecek[-1].tarih - bugun).days + 1


def tampon_bayrak(gun: int) -> str:
    if gun < 3:
        return "DUR"
    if gun < 7:
        return "DİKKAT"
    return "TEMİZ"


def durdurulmali(k: Kuyruk, bugun: date) -> bool:
    if not any(s.durum in KARTTA for s in k.slotlar):
        return False
    pencere_basi = hafta_baslangici(bugun) - timedelta(days=7)
    if not k.heartbeat or min(t for t, _, _ in k.heartbeat) > pencere_basi:
        return False  # sistem iki haftadan yeni
    return not any(pencere_basi <= t <= bugun for t, _, _, _ in k.kararlar)


def kural_ihlalleri(k: Kuyruk) -> List[str]:
    slotlar = _aktif_tarihli(k)
    if not slotlar:
        return []
    haftalar = {}
    for s in slotlar:
        haftalar.setdefault(hafta_baslangici(s.tarih), []).append(s)
    ihlaller = []
    h = min(haftalar)
    son = max(haftalar)
    while h <= son:
        grup = haftalar.get(h, [])
        video = sum(1 for s in grup if s.video)
        if video > 1:
            ihlaller.append(f"{h.isoformat()} haftası: {video} video (en çok 1)")
        if len(grup) < 2:
            ihlaller.append(f"{h.isoformat()} haftası: {len(grup)} gönderi (taban 2)")
        h += timedelta(days=7)
    return ihlaller


def ozet_satiri(k: Kuyruk, bugun: date) -> str:
    kartta = sum(1 for s in k.slotlar if s.durum in KARTTA)
    t = tampon_gun(k, bugun)
    bakiye = "bakiye bilinmiyor" if k.bakiye is None else f"bakiye {k.bakiye}"
    gorev = k.gorev + (f" ({k.sebep})" if k.gorev == "DURAKLADI" and k.sebep else "")
    satir = (
        f"Instagram: kartta {kartta} paket · tampon {t} gün ({tampon_bayrak(t)}) · "
        f"kredi {bakiye}, dönem harcaması {k.donem_harcama} · görev {gorev}"
    )
    if k.heartbeat:
        tarih, mod, ozet = k.heartbeat[-1]
        if mod == "HATA":
            satir += f" · son koşu HATA ({tarih.isoformat()})"
        if "push başarısız" in ozet:
            satir += f" · push başarısız ({tarih.isoformat()})"
    return satir


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description="Instagram kuyruk aracı")
    p.add_argument("komut", choices=["ozet", "denetle", "durum"])
    p.add_argument("--kuyruk", type=Path, default=VARSAYILAN_KUYRUK)
    p.add_argument("--bugun", type=date.fromisoformat, default=date.today())
    a = p.parse_args(argv)
    try:
        k = oku(a.kuyruk)
    except (KuyrukHatasi, OSError, ValueError, IndexError) as e:
        print(f"Instagram: kuyruk okunamadı — {e}")
        return 2
    if a.komut == "ozet":
        print(ozet_satiri(k, a.bugun))
        return 0
    if a.komut == "durum":
        print("DURAKLAT" if durdurulmali(k, a.bugun) else "DEVAM")
        return 0
    ihlaller = kural_ihlalleri(k)
    for i in ihlaller:
        print(i)
    return 1 if ihlaller else 0


if __name__ == "__main__":
    sys.exit(main())
