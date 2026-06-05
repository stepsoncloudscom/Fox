#!/usr/bin/env python3
"""
Fox PDF Motoru v3 — Steps On Clouds / Marka Bulutu
Editorial, premium PDF üretimi. İKİ REGISTER (marka-kiti.md):
  • "ayhan-premium" (varsayılan) — İŞ register: Didot + Avenir Next, siyah/altın/krem.
      Teklif, sözleşme, kurumsal belge. Müşteri markası öne çıkar.
  • "soc-mavi" — MİSYON/MARKA register: Bebas Neue + Comfortaa, Phthalo/Sky Blue/Mist.
      Steps On Clouds marka sunumları, denetim raporu, kampanya, sosyal.

Türkçe-doğru (tüm fontlar İ/ı/ş/ç/ğ/ö/ü taşır — doğrulandı 5 Haz 2026).
İçerik Ajanı görsel kolu + estetik müfredatı + görsel parmak izi zemini.

Kullanım: python3 pdf-motoru.py <icerik.json> <cikti.pdf>

JSON yapısı:
{
  "tema": "soc-mavi",                            // "ayhan-premium" (varsayılan) | "soc-mavi"
  "baslik": "STEPS ON CLOUDS",
  "alt_baslik": "Marka Denetim Raporu",
  "eyebrow": "MARKA BULUTU · DENETİM",           // opsiyonel üst etiket
  "meta": "Hazırlayan: ... · tarih",
  "skor": "40/100",                              // opsiyonel büyük skor vurgusu
  "skor_not": "D — Büyük revizyon gerekli",      // opsiyonel skor açıklaması
  "partner_logo": "/yol/partner.png",            // opsiyonel
  "bolumler": [
    {"tip":"baslik","metin":"..."},
    {"tip":"paragraf","metin":"..."},
    {"tip":"madde","maddeler":[...]},
    {"tip":"tablo","basliklar":[...],"satirlar":[[...]]},
    {"tip":"fiyat","satirlar":[["Kalem","Tutar"]]},
    {"tip":"ayrac"}
  ],
  "imzalar": [["Steps On Clouds","Ayhan Erden"]]  // opsiyonel
}
KURAL: Türkçe içerikte Unicode font zorunlu. Helvetica yasak.
"""
import sys, json, os
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm, mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                 TableStyle, HRFlowable, Image as RLImage, KeepTogether)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ── Font kayıt yardımcısı ──────────────────────────────────────
_FONT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'assets', 'fonts')

def _reg(name, path, idx=None):
    try:
        pdfmetrics.registerFont(TTFont(name, path, subfontIndex=idx) if idx is not None else TTFont(name, path))
        return True
    except Exception:
        return False

# Marka fontları (repo assets/fonts — her ortamda var)
_reg('Bebas',         os.path.join(_FONT_DIR, 'BebasNeue-Regular.ttf'))
_reg('Comfortaa',     os.path.join(_FONT_DIR, 'Comfortaa-Regular.ttf'))
_reg('Comfortaa-Bold',os.path.join(_FONT_DIR, 'Comfortaa-Bold.ttf'))
# İş register fontları (macOS sistem — varsa)
_reg('Didot',      '/System/Library/Fonts/Supplemental/Didot.ttc', 0)
_reg('Didot-Bold', '/System/Library/Fonts/Supplemental/Didot.ttc', 1)
_reg('Avenir',     '/System/Library/Fonts/Avenir Next.ttc', 0)
_reg('Avenir-Bold','/System/Library/Fonts/Avenir Next.ttc', 1)
# Türkçe-güvenli yedekler (her zaman var)
_reg('ArialTR',      '/System/Library/Fonts/Supplemental/Arial.ttf')
_reg('ArialTR-Bold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf')

def _f(preferred, fallback='ArialTR'):
    return preferred if preferred in pdfmetrics.getRegisteredFontNames() else fallback

# ── TEMALAR (iki register) ─────────────────────────────────────
# Her tema: fontlar + palet + tipografik ayarlar.
# Boşluk ve hiyerarşi editorial; AI-slop (gereksiz dekoratif öğe) yok.
TEMALAR = {
    'ayhan-premium': {
        'title':   _f('Didot'),
        'title_b': _f('Didot-Bold', _f('Didot')),
        'body':    _f('Avenir', 'ArialTR'),
        'body_b':  _f('Avenir-Bold', 'ArialTR-Bold'),
        'ink':     colors.HexColor('#1A1C22'),   # koyu mürekkep
        'slate':   colors.HexColor('#4A5563'),   # gövde grisi
        'muted':   colors.HexColor('#8A8578'),   # sıcak gri
        'accent':  colors.HexColor('#A8814B'),   # imza altını
        'accent2': colors.HexColor('#A8814B'),
        'line':    colors.HexColor('#E2DDD3'),   # sıcak ince çizgi
        'paper':   colors.HexColor('#FCFBF8'),   # sıcak beyaz
        'surface': colors.HexColor('#F4F1EA'),   # krem yüzey
        'title_caps': False,
        'title_size': 30, 'title_lead': 32,
        'h_size': 15, 'h_lead': 18,
        'body_size': 9.5, 'body_lead': 15,
        'accent_label': colors.HexColor('#A8814B'),
        'on_accent': colors.white,
    },
    'soc-mavi': {
        'title':   _f('Bebas'),
        'title_b': _f('Bebas'),                  # Bebas tek ağırlık (display caps)
        'body':    _f('Comfortaa', 'ArialTR'),
        'body_b':  _f('Comfortaa-Bold', 'ArialTR-Bold'),
        'ink':     colors.HexColor('#101010'),   # Midnight Black (metin)
        'slate':   colors.HexColor('#3A4450'),   # gövde
        'muted':   colors.HexColor('#6B7785'),   # nötr gri
        'accent':  colors.HexColor('#040D7E'),   # Phthalo Blue (ana marka)
        'accent2': colors.HexColor('#72CBDF'),   # Sky Blue (aksan)
        'line':    colors.HexColor('#D5E6EC'),   # açık mavi ince çizgi
        'paper':   colors.white,                 # White Cloud
        'surface': colors.HexColor('#EAF6EB'),   # Mist yüzey
        'title_caps': True,                      # Bebas zaten caps; Türkçe İ için _caps()
        'title_size': 46, 'title_lead': 46,      # Bebas kompakt → büyük punto
        'h_size': 22, 'h_lead': 24,
        'body_size': 9, 'body_lead': 15,         # Comfortaa geniş → 9pt
        'accent_label': colors.HexColor('#040D7E'),
        'on_accent': colors.white,
    },
}

SOC_LOGO = '/Users/ayhanerden/Desktop/Steps On Clouds/Legal/assets/soc_logo.png'
_base = getSampleStyleSheet()['Normal']

def _caps_tr(t):
    # Türkçe-doğru uppercase (i→İ, ı→I) — Bebas/eyebrow için
    return t.replace('i','İ').replace('ı','I').upper()

def _make_styles(T):
    """Temaya göre ParagraphStyle sözlüğü kur."""
    c = [0]
    def ps(font, size, col, al=0, sb=0, sa=0, ld=None, track=0):
        c[0]+=1
        kw = dict(parent=_base, fontName=font, fontSize=size, textColor=col,
                  alignment=al, spaceBefore=sb, spaceAfter=sa)
        if ld: kw['leading']=ld
        if track: kw['charSpace']=track
        return ParagraphStyle(f'p{c[0]}', **kw)
    return {
      'eyebrow':  ps(T['body_b'], 8.5, T['accent_label'], al=1, sa=7, track=1.5),
      'title':    ps(T['title'], T['title_size'], T['ink'], al=1, sa=5, ld=T['title_lead']),
      'subtitle': ps(T['title'], T['h_size']-4, T['accent'], al=1, sa=6, ld=T['h_size']-2),
      'meta':     ps(T['body'], 8.5, T['muted'], al=1, sa=2, ld=12),
      'scorebig': ps(T['title'], T['title_size']+18, T['accent'], al=1, sa=0, ld=T['title_size']+20),
      'scorelbl': ps(T['body_b'], 8, T['muted'], al=1, sa=2, track=1),
      'scornot':  ps(T['body_b'], 10, T['ink'], al=1, sa=2),
      'h':        ps(T['title'], T['h_size'], T['accent'], sb=22, sa=9, ld=T['h_lead']),
      'body':     ps(T['body'], T['body_size'], T['slate'], sa=5, ld=T['body_lead']),
      'bold':     ps(T['body_b'], T['body_size'], T['ink'], ld=T['body_lead']),
      'th':       ps(T['body_b'], 8.5, T['on_accent'], ld=12),
      'td':       ps(T['body'], 8.5, T['slate'], ld=13),
      'accent':   ps(T['body_b'], T['body_size'], T['accent']),
      'price':    ps(T['title'], T['h_size']-2, T['accent']),
      'small':    ps(T['body'], 7.5, T['muted'], ld=11),
      'foot':     ps(T['body'], 7.5, T['muted'], al=1, ld=11),
    }

def _section_heading(metin, T, S):
    # ince aksan çizgi (amaçlı, tutarlı — slop değil) + başlık
    cap = _caps_tr(metin) if T['title_caps'] else metin
    return [Spacer(1,0.12*cm),
            HRFlowable(width=38, thickness=2, color=T['accent2'], spaceAfter=6, hAlign='LEFT'),
            Paragraph(cap, S['h'])]

def _zebra_table(basliklar, satirlar, col_widths, T, S):
    rows = [[Paragraph(h, S['th']) for h in basliklar]]
    for sat in satirlar:
        rows.append([Paragraph(str(c), S['td']) for c in sat])
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), T['accent']),       # başlık şeridi marka rengi
        ('LINEBELOW',(0,1),(-1,-2), 0.4, T['line']),    # satır araları ince
        ('ROWBACKGROUNDS',(0,1),(-1,-1), [T['paper'], T['surface']]),  # zebra
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),7),
        ('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),
    ]))
    return t

# Glyph-güvenli temizlik: bazı marka fontları (Comfortaa) ₺ U+20BA taşımaz → kutu çıkar.
# Riskli sembolleri güvenli yazıma çevir. (5 Haz 2026 — Comfortaa ₺ bug'ından öğrenildi.)
_GLYPH_SAFE = {'₺': ' TL', '₺': ' TL'}
def _clean(obj):
    if isinstance(obj, str):
        for k, v in _GLYPH_SAFE.items():
            obj = obj.replace(k, v)
        return obj
    if isinstance(obj, list):  return [_clean(x) for x in obj]
    if isinstance(obj, dict):  return {k: _clean(v) for k, v in obj.items()}
    return obj

def build(data, out_path):
    data = _clean(data)
    tema = data.get('tema', 'ayhan-premium')
    T = TEMALAR.get(tema, TEMALAR['ayhan-premium'])
    S = _make_styles(T)
    avail = 16.2*cm

    doc = SimpleDocTemplate(out_path, pagesize=A4,
        rightMargin=2.4*cm, leftMargin=2.4*cm, topMargin=2*cm, bottomMargin=2*cm,
        title=data.get('baslik',''), author='Steps On Clouds')
    story = []

    # — Üst başlık alanı: logo(lar) —
    if os.path.exists(SOC_LOGO):
        soc = RLImage(SOC_LOGO, width=3*cm, height=2.6*cm)
        if data.get('partner_logo') and os.path.exists(data['partner_logo']):
            partner = RLImage(data['partner_logo'], width=2.6*cm, height=2.6*cm)
            head = Table([[soc, '', partner]], colWidths=[3.5*cm, 9.2*cm, 3.5*cm])
            head.setStyle(TableStyle([('ALIGN',(0,0),(0,0),'LEFT'),('ALIGN',(2,0),(2,0),'RIGHT'),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
        else:
            head = Table([[soc, '']], colWidths=[3.5*cm, 12.7*cm])
            head.setStyle(TableStyle([('ALIGN',(0,0),(0,0),'LEFT'),('VALIGN',(0,0),(-1,-1),'MIDDLE')]))
        story.append(head)
        story.append(Spacer(1, 1.0*cm))

    # — Kapak bloğu —
    if data.get('eyebrow'):
        story.append(Paragraph(_caps_tr(data['eyebrow']), S['eyebrow']))
    if data.get('baslik'):
        bt = _caps_tr(data['baslik']) if T['title_caps'] else data['baslik']
        story.append(Paragraph(bt, S['title']))
    if data.get('alt_baslik'):
        story.append(Paragraph(data['alt_baslik'], S['subtitle']))

    if data.get('skor'):
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph(data['skor'], S['scorebig']))
        story.append(Paragraph(_caps_tr('Genel Marka Skoru'), S['scorelbl']))
        if data.get('skor_not'):
            story.append(Paragraph(data['skor_not'], S['scornot']))

    if data.get('meta'):
        story.append(Spacer(1, 0.4*cm))
        story.append(Paragraph(data['meta'], S['meta']))

    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=T['line']))

    # — Bölümler —
    for b in data.get('bolumler', []):
        t = b.get('tip')
        if t == 'baslik':
            for el in _section_heading(b['metin'], T, S): story.append(el)
        elif t == 'paragraf':
            story.append(Paragraph(b['metin'], S['body']))
        elif t == 'madde':
            ac = T['accent'].hexval()[2:]  # '0x040D7E' → '040D7E'
            for m in b['maddeler']:
                story.append(Paragraph(f'<font color="#{ac}">—</font>&nbsp;&nbsp;{m}', S['body']))
        elif t == 'tablo':
            n = len(b['basliklar'])
            if n == 3:
                cw = [4.2*cm, 2.6*cm, avail-6.8*cm]
            elif n == 2:
                cw = [avail*0.32, avail*0.68]
            else:
                cw = [avail/n]*n
            story.append(Spacer(1,0.15*cm))
            story.append(_zebra_table(b['basliklar'], b['satirlar'], cw, T, S))
        elif t == 'fiyat':
            rows = [[Paragraph('Kalem', S['th']), Paragraph('Tutar', S['th'])]]
            for k,v in b['satirlar']:
                rows.append([Paragraph(k, S['bold']), Paragraph(v, S['price'])])
            ft = Table(rows, colWidths=[avail*0.62, avail*0.38])
            ft.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),T['accent']),
                ('LINEBELOW',(0,1),(-1,-2),0.4,T['line']),
                ('ROWBACKGROUNDS',(0,1),(-1,-1),[T['paper'],T['surface']]),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),
                ('LEFTPADDING',(0,0),(-1,-1),9),
            ]))
            story.append(Spacer(1,0.15*cm)); story.append(ft)
        elif t == 'ayrac':
            story.append(Spacer(1,0.3*cm))
            story.append(HRFlowable(width=38, thickness=2, color=T['accent2'], hAlign='LEFT'))
            story.append(Spacer(1,0.15*cm))

    # — İmzalar —
    if data.get('imzalar'):
        story.append(Spacer(1,0.8*cm))
        story.append(HRFlowable(width='100%', thickness=0.5, color=T['line']))
        story.append(Spacer(1,0.4*cm))
        head=[Paragraph(x[0],S['bold']) for x in data['imzalar']]
        nm=[Paragraph(x[1],S['body']) for x in data['imzalar']]
        sig=[Paragraph('İmza: _______________',S['small']) for _ in data['imzalar']]
        dt=[Paragraph('Tarih: _______________',S['small']) for _ in data['imzalar']]
        w=avail/len(data['imzalar'])
        it=Table([head,nm,sig,dt], colWidths=[w]*len(data['imzalar']))
        it.setStyle(TableStyle([('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),('LEFTPADDING',(0,0),(-1,-1),0)]))
        story.append(it)

    # — Footer —
    story.append(Spacer(1,0.9*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=T['line']))
    story.append(Spacer(1,0.2*cm))
    story.append(Paragraph('Steps On Clouds&nbsp;&nbsp;·&nbsp;&nbsp;Ayhan Erden&nbsp;&nbsp;·&nbsp;&nbsp;ayhanerden@stepsonclouds.com', S['foot']))

    doc.build(story)
    return out_path

if __name__ == '__main__':
    if len(sys.argv)!=3:
        print('Kullanım: python3 pdf-motoru.py <icerik.json> <cikti.pdf>'); sys.exit(1)
    with open(sys.argv[1], encoding='utf-8') as f:
        data=json.load(f)
    print('✓ PDF üretildi (v3 ·', data.get('tema','ayhan-premium'), '):', build(data, sys.argv[2]))
