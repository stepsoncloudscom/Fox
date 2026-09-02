#!/usr/bin/env python3
"""bayat_tarama — Fox talimat yüzeylerinde çürüme taraması (aylık budama aracı).

Üç ölçülebilir kusuru arar. Yorum yapmaz, sayar:
  1. ÖLÜ YOL      — dosyada anılan ama diskte olmayan dosya/dizin
  2. BAYAT FAZ    — geçmiş bir ayı gösterip hâlâ "aktif/planlı" diyen satır
  3. ÇİFT KAYIT   — aynı olgunun (rakam/istatistik) tek dosyada 3+ tekrarı

Kullanım:  python3 sablonlar/araclar/bayat_tarama.py [--kok .]
Çıkış kodu: bulgu varsa 1, temizse 0 (kapı olarak kullanılabilir).
"""
import re, sys, os, argparse
from datetime import date

AYLAR = {"Oca":1,"Şub":2,"Mar":3,"Nis":4,"May":5,"Haz":6,"Tem":7,"Ağu":8,"Eyl":9,"Eki":10,"Kas":11,"Ara":12}
HEDEF = ("CLAUDE.md", "fox-durum.md")
DESENLER = ("fox-*.md", "marka-bulutu-os-*.md", ".claude/agents/*.md")

def dosyalar(kok):
    import glob
    out = [os.path.join(kok, h) for h in HEDEF if os.path.exists(os.path.join(kok, h))]
    for d in DESENLER:
        out += sorted(glob.glob(os.path.join(kok, d)))
    return out

def olu_yollar(kok, yol, metin):
    bulgu = []
    for m in re.finditer(r'`?((?:raporlar|fox-raporlar|sablonlar|assets|\.claude)/[A-Za-z0-9._/-]+)', metin):
        hedef = m.group(1).rstrip('.,);:`')
        satir_metni = metin[metin.rfind('\n', 0, m.start())+1 : metin.find('\n', m.start())]
        # yanlış pozitifleri ele: glob, placeholder, komut örneği, harici (Drive) atıf
        if hedef.endswith(('/', '*')) or '[' in hedef:
            continue
        if metin[m.end():m.end()+1] == '*' or 'Drive' in satir_metni:
            continue
        if satir_metni.lstrip().startswith(('python3', 'python', '$', 'bash')):
            continue
        if not os.path.exists(os.path.join(kok, hedef)):
            satir = metin[:m.start()].count('\n') + 1
            bulgu.append((satir, hedef))
    return sorted(set(bulgu))

def bayat_faz(yol, metin, bugun):
    bulgu = []
    ay_re = "|".join(AYLAR)
    desen = re.compile(rf'({ay_re})[a-zışçöüğ]*\s+(20\d\d)[^\n)]{{0,60}}?(aktif|AKTİF|planlı|PLANLI)', re.I)
    for i, satir in enumerate(metin.split('\n'), 1):
        for m in desen.finditer(satir):
            yil, ay = int(m.group(2)), AYLAR[m.group(1)]
            yas = (bugun.year - yil) * 12 + (bugun.month - ay)
            if yas >= 2:  # 2+ ay geçmiş ve hâlâ "aktif" diyor
                bulgu.append((i, yas, satir.strip()[:110]))
    return bulgu

def cift_kayit(metin):
    # aynı sayısal olgu (%88, 37 doktor gibi) tek dosyada 3+ kez
    sayac = {}
    for satir in metin.split('\n'):
      if satir.count('|') >= 2:   # tablo satırı: rubrik ağırlıkları meşru tekrardır
        continue
      for m in re.finditer(r'%\s?(\d{1,3})|(\d{1,3})\s?%', satir):
        d = m.group(1) or m.group(2)
        if int(d) > 5:
            sayac[d] = sayac.get(d, 0) + 1
    return [(d, n) for d, n in sorted(sayac.items(), key=lambda x: -x[1]) if n >= 3]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--kok", default=".")
    a = ap.parse_args()
    bugun = date.today()
    toplam = 0
    for yol in dosyalar(a.kok):
        metin = open(yol, encoding="utf-8").read()
        ad = os.path.relpath(yol, a.kok)
        satirlar = []
        for s, h in olu_yollar(a.kok, yol, metin):
            satirlar.append(f"  ÖLÜ YOL    {ad}:{s}  →  {h}")
        for s, yas, txt in bayat_faz(yol, metin, bugun):
            satirlar.append(f"  BAYAT FAZ  {ad}:{s}  ({yas} ay önce)  {txt}")
        for d, n in cift_kayit(metin):
            satirlar.append(f"  ÇİFT KAYIT {ad}  →  %{d} istatistiği {n} yerde (drift riski)")
        if satirlar:
            print("\n".join(satirlar))
            toplam += len(satirlar)
    print(f"\n=== {bugun.isoformat()} — toplam {toplam} bulgu ===")
    print("Kural: BAYAT FAZ ya kapatılır ya tarihi yenilenir; ÖLÜ YOL düzeltilir; ÇİFT KAYIT tek yere indirilir.")
    return 1 if toplam else 0

if __name__ == "__main__":
    sys.exit(main())
