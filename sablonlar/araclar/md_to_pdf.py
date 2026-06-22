#!/usr/bin/env python3
"""md_to_pdf.py — Markdown raporu pdf-motoru.py JSON şemasına çevirip PDF üretir.
Türkçe-doğru (pdf-motoru fontları). Emoji/sembol (≥U+2600) temizlenir; ok (→) ve
tipografik işaretler korunur. Kullanım: python3 md_to_pdf.py (docs listesi içeride).
Tekrar kullanılabilir — her md rapor için."""
import re, json, subprocess, os

REPO = '/Users/ayhanerden/Fox'
MOTOR = os.path.join(REPO, 'sablonlar', 'pdf-motoru.py')

def strip_sym(t):
    # Emoji/checkmark/uyarı sembollerini at; Türkçe + ok (→,U+2192<U+2600) + tipografi korunur
    return ''.join(c for c in t if ord(c) < 0x2600)

def inline(t):
    t = strip_sym(t)
    t = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', t)   # [text](url) -> text
    t = t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)     # bold
    t = re.sub(r'\*([^*]+)\*', r'<i>\1</i>', t)       # italic (bold sonrası kalan tek *)
    t = re.sub(r'`([^`]+)`', r'\1', t)               # inline code -> düz
    return t.strip()

def parse_table(block):
    def cells(r): return [c.strip() for c in r.strip().strip('|').split('|')]
    head = [inline(h) for h in cells(block[0])]
    body = [[inline(c) for c in cells(r)] for r in block[2:]]  # 0=başlık,1=---
    return {"tip": "tablo", "basliklar": head, "satirlar": body}

def parse_md(path, eyebrow):
    raw = open(path, encoding='utf-8').read().split('\n')
    n = len(raw); i = 0
    baslik = ''; meta = []; bolumler = []
    while i < n:
        if raw[i].startswith('# '):
            baslik = inline(raw[i][2:]); i += 1; break
        i += 1
    while i < n:
        s = raw[i].strip()
        if s.startswith('#') or s.startswith('---'): break
        if s.startswith('**'): meta.append(re.sub(r'\*\*', '', s).strip())
        i += 1
    while i < n:
        s = raw[i].strip()
        if not s: i += 1; continue
        if s.startswith('|'):
            blk = []
            while i < n and raw[i].strip().startswith('|'):
                blk.append(raw[i]); i += 1
            if len(blk) >= 2: bolumler.append(parse_table(blk))
            continue
        if s.startswith('#### '): bolumler.append({"tip":"baslik","metin":inline(s[5:])}); i+=1; continue
        if s.startswith('### '):  bolumler.append({"tip":"baslik","metin":inline(s[4:])}); i+=1; continue
        if s.startswith('## '):   bolumler.append({"tip":"baslik","metin":inline(s[3:])}); i+=1; continue
        if s.startswith('# '):    i+=1; continue
        if s.startswith('---') or s.startswith('***'): bolumler.append({"tip":"ayrac"}); i+=1; continue
        if re.match(r'^([-*]|\d+\.) ', s):
            items = []
            while i < n:
                ss = raw[i].strip()
                m = re.match(r'^(?:[-*]|\d+\.) (.+)', ss)
                if m: items.append(inline(m.group(1))); i += 1
                else: break
            bolumler.append({"tip": "madde", "maddeler": items}); continue
        if s.startswith('> '): bolumler.append({"tip":"paragraf","metin":inline(s[2:])}); i+=1; continue
        if s.startswith('```'):
            i += 1
            while i < n and not raw[i].strip().startswith('```'): i += 1
            i += 1; continue
        bolumler.append({"tip": "paragraf", "metin": inline(s)}); i += 1
    return {"tema": "ayhan-premium", "baslik": baslik, "eyebrow": strip_sym(eyebrow),
            "meta": " · ".join(meta[:3]), "bolumler": bolumler}

docs = [
    ('raporlar/syla-atelier-marka-denetim-raporu.md',
     'raporlar/syla-atelier-marka-denetim-raporu.pdf',
     'MARKA BULUTU OS · KEŞİF & DENETİM'),
    ('raporlar/syla-atelier-strateji.md',
     'raporlar/syla-atelier-strateji.pdf',
     'MARKA BULUTU OS · STRATEJİ'),
]

for md, pdf, eb in docs:
    data = parse_md(os.path.join(REPO, md), eb)
    jp = os.path.join('/tmp', os.path.basename(md) + '.json')
    json.dump(data, open(jp, 'w', encoding='utf-8'), ensure_ascii=False)
    r = subprocess.run(['python3', MOTOR, jp, os.path.join(REPO, pdf)],
                       capture_output=True, text=True)
    print(f"{md} -> {pdf} | rc={r.returncode} | bolum={len(data['bolumler'])}")
    if r.stdout.strip(): print("  out:", r.stdout.strip()[-200:])
    if r.stderr.strip(): print("  ERR:", r.stderr.strip()[-400:])
