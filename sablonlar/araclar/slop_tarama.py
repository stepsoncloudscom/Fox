#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
slop_tarama.py — Metin çıktılarında AI-klişe / placeholder / eksiklik taraması.

Kaynak kural seti: marka-bulutu-os-gorsel-uretim-standardi.md §11.E (AI Kopya
Klişeleri Yasağı), §11.B placeholder yasağı, §11.H eksiksizlik kuralı.
gstack öğreniminden "slop-scan" fikri (fox-gstack-ogrenim.md) — 3 Tem 2026'da kuruldu.

Kullanım:
    python3 slop_tarama.py dosya1.md [dosya2.txt ...]
    python3 slop_tarama.py raporlar/          # klasördeki .md/.txt/.html dosyaları

Çıkış kodu: 0 = temiz · 1 = YASAK bulgu var · 2 = yalnız ŞÜPHELİ bulgu var.

Not: Bu tarama Denetmen'in yerine geçmez — dışarı çıkan metnin İLK süzgecidir.
ŞÜPHELİ seviye bağlama bakılmadan silinmez (ör. "leverage" finans metninde meşru).
"""

import re
import sys
from pathlib import Path

# ── YASAK: "AI yazdı" sinyali — marka brief'i açıkça istemedikçe kullanılmaz ──
YASAK = [
    # EN klişeler (§11.E)
    r"\belevate[sd]?\b", r"\bseamless(?:ly)?\b", r"\bunleash(?:ed|ing)?\b",
    r"\bnext[- ]gen(?:eration)?\b", r"\bgame[- ]chang(?:er|ing)\b",
    r"\bdelve[sd]?\b", r"\bempower(?:ing|ed|s)?\b",
    r"\brevolutioni[sz]e[sd]?\b", r"\bcutting[- ]edge\b",
    # TR klişeler (§11.E)
    r"bir adım öteye taşı", r"kusursuz deneyim", r"oyunun kurallarını değiştir",
    r"yeni nesil", r"potansiyelini(?:zi)? ortaya çıkar", r"devrim niteliğinde",
    r"zahmetsizce",
    # Placeholder yasağı (§11.B laziness)
    r"\bjohn doe\b", r"\bjane doe\b", r"\bacme\b", r"lorem ipsum",
    r"örnek metin", r"\[placeholder\]", r"\bplaceholder\b",
    # Eksiksizlik ihlali (§11.H)
    r"\[devam[^\]]*\]", r"//\s*kalan", r"geri kalanı aynı", r"\.\.\.\s*\[",
    r"\[buraya .{0,30}(?:ekle|gelecek)\]",
]

# ── ŞÜPHELİ: bağlama bak — pazarlama dolgusuysa sil, teknik/meşru kullanımsa kalsın ──
SUPHELI = [
    r"\bleverage[sd]?\b",          # pazarlama anlamında yasak; finans/teknik meşru
    r"\brevolutionary\b",
    r"\btbd\b", r"\bTBD\b",
    r"benzersiz",                   # TR dolgu adayı — gerçek farklılaştırıcıya bağlıysa meşru
    r"kesintisiz",                  # "seamless" çevirisi olarak dolguysa sil
    r"güçlendir(?:in|iyoruz|ir)",   # "empower" kalıp çevirisi adayı
]

UZANTILAR = {".md", ".txt", ".html", ".htm"}


def dosyalari_topla(argv):
    dosyalar = []
    for arg in argv:
        p = Path(arg)
        if p.is_dir():
            dosyalar += [f for f in sorted(p.rglob("*")) if f.suffix.lower() in UZANTILAR]
        elif p.is_file():
            dosyalar.append(p)
        else:
            print(f"⚠️  bulunamadı: {arg}", file=sys.stderr)
    return dosyalar


def tara(dosya, desenler):
    bulgular = []
    try:
        metin = dosya.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError) as e:
        print(f"⚠️  okunamadı: {dosya} ({e})", file=sys.stderr)
        return bulgular
    for no, satir in enumerate(metin.splitlines(), 1):
        for desen in desenler:
            for es in re.finditer(desen, satir, re.IGNORECASE):
                bulgular.append((no, es.group(0), satir.strip()[:100]))
    return bulgular


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    dosyalar = dosyalari_topla(sys.argv[1:])
    yasak_var, supheli_var = False, False

    for dosya in dosyalar:
        yasak = tara(dosya, YASAK)
        supheli = tara(dosya, SUPHELI)
        if not yasak and not supheli:
            continue
        print(f"\n📄 {dosya}")
        for no, kelime, baglam in yasak:
            print(f"  ❌ YASAK   satır {no}: «{kelime}» → {baglam}")
            yasak_var = True
        for no, kelime, baglam in supheli:
            print(f"  ⚠️  ŞÜPHELİ satır {no}: «{kelime}» → {baglam}")
            supheli_var = True

    if not yasak_var and not supheli_var:
        print(f"✅ Temiz — {len(dosyalar)} dosya tarandı, klişe/placeholder/eksiklik bulunamadı.")
        sys.exit(0)
    print("\nÖzet: YASAK bulgular yeniden yazılır; ŞÜPHELİ bulgular bağlamıyla değerlendirilir.")
    sys.exit(1 if yasak_var else 2)


if __name__ == "__main__":
    main()
