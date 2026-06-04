#!/usr/bin/env python3
"""
Fox PDF Motoru v2 — Steps On Clouds / Marka Bulutu
Editorial, premium PDF üretimi. Didot (başlık) + Avenir Next (gövde), Türkçe-doğru.
İçerik Ajanı görsel kolu + estetik müfredatı + görsel parmak izi zemini.

Kullanım: python3 pdf-motoru.py <icerik.json> <cikti.pdf>

JSON yapısı (v1 ile uyumlu):
{
  "baslik": "TOWDOO",
  "alt_baslik": "Marka Denetim Raporu",
  "eyebrow": "MARKA BULUTU · DENETİM",         // opsiyonel üst etiket
  "meta": "Hazırlayan: ... · tarih",
  "skor": "65/100",                              // opsiyonel büyük skor vurgusu
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
KURAL: Türkçe içerikte Unicode font zorunlu (Didot/Avenir/Arial). Helvetica yasak.
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

# --- Fontlar: editorial (Didot başlık) + sofistike sans (Avenir gövde) + Türkçe yedek ---
def _reg(name, path, idx=None):
    try:
        pdfmetrics.registerFont(TTFont(name, path, subfontIndex=idx) if idx is not None else TTFont(name, path))
        return True
    except Exception:
        return False

_reg('Didot', '/System/Library/Fonts/Supplemental/Didot.ttc', 0)
_reg('Didot-Bold', '/System/Library/Fonts/Supplemental/Didot.ttc', 1)
_reg('Avenir', '/System/Library/Fonts/Avenir Next.ttc', 0)
_reg('Avenir-Bold', '/System/Library/Fonts/Avenir Next.ttc', 1)
# Türkçe-güvenli yedekler (her zaman var)
_reg('ArialTR', '/System/Library/Fonts/Supplemental/Arial.ttf')
_reg('ArialTR-Bold', '/System/Library/Fonts/Supplemental/Arial Bold.ttf')

def _font(preferred, fallback='ArialTR'):
    return preferred if preferred in pdfmetrics.getRegisteredFontNames() else fallback

F_TITLE = _font('Didot')           # editorial başlık
F_TITLE_B = _font('Didot-Bold', F_TITLE)
F_BODY = _font('Avenir', 'ArialTR')        # sofistike gövde
F_BODY_B = _font('Avenir-Bold', 'ArialTR-Bold')

# --- Palet (görsel parmak izi: sıcak, premium, editorial) ---
INK    = colors.HexColor('#1A1C22')   # koyu mürekkep
SLATE  = colors.HexColor('#4A5563')   # gövde grisi
MUTED  = colors.HexColor('#8A8578')   # sıcak gri
GOLD   = colors.HexColor('#A8814B')   # imza altını
LINE   = colors.HexColor('#E2DDD3')   # sıcak ince çizgi
PAPER  = colors.HexColor('#FCFBF8')   # sıcak beyaz
CREAM  = colors.HexColor('#F4F1EA')   # krem yüzey
WHITE  = colors.white

SOC_LOGO = '/Users/ayhanerden/Desktop/Steps On Clouds/Legal/assets/soc_logo.png'

_base = getSampleStyleSheet()['Normal']
_c = [0]
def _ps(font, size, col=INK, al=0, sb=0, sa=0, ld=None, track=0):
    _c[0]+=1
    kw = dict(parent=_base, fontName=font, fontSize=size, textColor=col,
              alignment=al, spaceBefore=sb, spaceAfter=sa)
    if ld: kw['leading']=ld
    return ParagraphStyle(f'p{_c[0]}', **kw)

def _eyebrow_text(t):
    # harf aralığı hissi için boşluklu uppercase
    return t.replace('i','İ').replace('ı','I').upper()

S = {
  'eyebrow': _ps(F_BODY_B, 8, GOLD, al=1, sa=6),
  'title':   _ps(F_TITLE, 30, INK, al=1, sa=4, ld=32),
  'subtitle':_ps(F_TITLE, 13, GOLD, al=1, sa=6, ld=16),
  'meta':    _ps(F_BODY, 8.5, MUTED, al=1, sa=2, ld=12),
  'scorebig':_ps(F_TITLE, 40, INK, al=1, sa=0, ld=42),
  'scorelbl':_ps(F_BODY_B, 8, MUTED, al=1, sa=2),
  'h':       _ps(F_TITLE, 15, INK, sb=20, sa=8, ld=18),
  'body':    _ps(F_BODY, 9.5, SLATE, sa=5, ld=15),
  'bold':    _ps(F_BODY_B, 9.5, INK, ld=15),
  'th':      _ps(F_BODY_B, 8.5, INK, ld=12),
  'td':      _ps(F_BODY, 8.5, SLATE, ld=12.5),
  'gold':    _ps(F_BODY_B, 9.5, GOLD),
  'price':   _ps(F_TITLE, 13, GOLD),
  'small':   _ps(F_BODY, 7.5, MUTED, ld=11),
  'foot':    _ps(F_BODY, 7.5, MUTED, al=1, ld=11),
}

def _section_heading(metin):
    # ince altın çizgi + Didot başlık (editorial)
    return [Spacer(1,0.1*cm),
            HRFlowable(width=34, thickness=1.4, color=GOLD, spaceAfter=5, hAlign='LEFT'),
            Paragraph(metin, S['h'])]

def _zebra_table(basliklar, satirlar, col_widths):
    rows = [[Paragraph(h, S['th']) for h in basliklar]]
    for sat in satirlar:
        rows.append([Paragraph(str(c), S['td']) for c in sat])
    t = Table(rows, colWidths=col_widths, repeatRows=1)
    style = [
        ('BACKGROUND',(0,0),(-1,0), CREAM),
        ('LINEBELOW',(0,0),(-1,0), 1, GOLD),      # başlık altı altın çizgi
        ('LINEBELOW',(0,1),(-1,-2), 0.4, LINE),   # satır araları ince
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('TOPPADDING',(0,0),(-1,-1),7),
        ('BOTTOMPADDING',(0,0),(-1,-1),7),
        ('LEFTPADDING',(0,0),(-1,-1),9),
        ('RIGHTPADDING',(0,0),(-1,-1),9),
    ]
    t.setStyle(TableStyle(style))
    return t

def build(data, out_path):
    doc = SimpleDocTemplate(out_path, pagesize=A4,
        rightMargin=2.4*cm, leftMargin=2.4*cm, topMargin=2*cm, bottomMargin=2*cm,
        title=data.get('baslik',''), author='Steps On Clouds')
    story = []

    # — Üst başlık alanı: logo(lar) —
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

    # — Kapak bloğu: eyebrow / title / subtitle / skor / meta —
    if data.get('eyebrow'):
        story.append(Paragraph(_eyebrow_text(data['eyebrow']), S['eyebrow']))
    if data.get('baslik'):
        story.append(Paragraph(data['baslik'], S['title']))
    if data.get('alt_baslik'):
        story.append(Paragraph(data['alt_baslik'], S['subtitle']))

    if data.get('skor'):
        story.append(Spacer(1, 0.5*cm))
        story.append(Paragraph(data['skor'], S['scorebig']))
        story.append(Paragraph(_eyebrow_text('Genel Marka Skoru'), S['scorelbl']))

    if data.get('meta'):
        story.append(Spacer(1, 0.4*cm))
        story.append(Paragraph(data['meta'], S['meta']))

    story.append(Spacer(1, 0.5*cm))
    story.append(HRFlowable(width='100%', thickness=0.5, color=LINE))

    # — Bölümler —
    avail = 16.2*cm
    for b in data.get('bolumler', []):
        t = b.get('tip')
        if t == 'baslik':
            for el in _section_heading(b['metin']): story.append(el)
        elif t == 'paragraf':
            story.append(Paragraph(b['metin'], S['body']))
        elif t == 'madde':
            for m in b['maddeler']:
                story.append(Paragraph(f'<font color="#A8814B">—</font>&nbsp;&nbsp;{m}', S['body']))
        elif t == 'tablo':
            n = len(b['basliklar'])
            # ilk sütun biraz dar, son sütun (genelde açıklama) geniş
            if n == 3:
                cw = [4.2*cm, 2.6*cm, avail-6.8*cm]
            elif n == 2:
                cw = [avail*0.32, avail*0.68]
            else:
                cw = [avail/n]*n
            story.append(Spacer(1,0.15*cm))
            story.append(_zebra_table(b['basliklar'], b['satirlar'], cw))
        elif t == 'fiyat':
            rows = [[Paragraph('Kalem', S['th']), Paragraph('Tutar', S['th'])]]
            for k,v in b['satirlar']:
                rows.append([Paragraph(k, S['bold']), Paragraph(v, S['price'])])
            ft = Table(rows, colWidths=[avail*0.62, avail*0.38])
            ft.setStyle(TableStyle([
                ('BACKGROUND',(0,0),(-1,0),CREAM),
                ('LINEBELOW',(0,0),(-1,0),1,GOLD),
                ('LINEBELOW',(0,1),(-1,-2),0.4,LINE),
                ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
                ('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),
                ('LEFTPADDING',(0,0),(-1,-1),9),
            ]))
            story.append(Spacer(1,0.15*cm)); story.append(ft)
        elif t == 'ayrac':
            story.append(Spacer(1,0.3*cm))
            story.append(HRFlowable(width=34, thickness=1.4, color=GOLD, hAlign='LEFT'))
            story.append(Spacer(1,0.15*cm))

    # — İmzalar —
    if data.get('imzalar'):
        story.append(Spacer(1,0.8*cm))
        story.append(HRFlowable(width='100%', thickness=0.5, color=LINE))
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
    story.append(HRFlowable(width='100%', thickness=0.5, color=LINE))
    story.append(Spacer(1,0.2*cm))
    story.append(Paragraph('Steps On Clouds&nbsp;&nbsp;·&nbsp;&nbsp;Ayhan Erden&nbsp;&nbsp;·&nbsp;&nbsp;ayhanerden@stepsonclouds.com', S['foot']))

    doc.build(story)
    return out_path

if __name__ == '__main__':
    if len(sys.argv)!=3:
        print('Kullanım: python3 pdf-motoru.py <icerik.json> <cikti.pdf>'); sys.exit(1)
    with open(sys.argv[1], encoding='utf-8') as f:
        data=json.load(f)
    print('✓ PDF üretildi (v2):', build(data, sys.argv[2]))
