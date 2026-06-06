#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ala Skateboards × Steps On Clouds — Fiziksel satış noktası materyalleri.
Baskıya hazır PDF üretici (3mm bleed, gömülü marka fontları, soc-mavi register).
Çıktı: hang tag, shelf talker (A5), poster (A2), QR kart.
Register: soc-mavi · Fontlar: Bebas Neue + Comfortaa · Görsel Üretim Standardı uyumlu.
"""
import os, numpy as np
from PIL import Image, ImageChops
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = "/Users/ayhanerden/Fox"
FONTS = os.path.join(ROOT, "assets/fonts")
LOGO_SRC = "/Users/ayhanerden/Desktop/Steps On Clouds/Legal/assets/soc_logo.png"
OUT = os.path.join(ROOT, "raporlar/ala-materyaller")
os.makedirs(OUT, exist_ok=True)
TMP = os.path.join(OUT, "_assets"); os.makedirs(TMP, exist_ok=True)

# ---- Marka renkleri (marka-kiti.md) ----
PHTHALO = HexColor("#040D7E")
SKY     = HexColor("#72CBDF")
WHITE   = HexColor("#FFFFFF")
MIDNIGHT= HexColor("#101010")
MIST    = HexColor("#EAF6EB")

# ---- Fontlar ----
# Comfortaa-Bold.ttf iç PostScript adı kalıcı düzeltildi (6 Haz 2026) → doğrudan kayıt
# yeterli; reportlab Regular ile çakışmadan gerçek bold'u gömer.
pdfmetrics.registerFont(TTFont("Bebas", os.path.join(FONTS, "BebasNeue-Regular.ttf")))
pdfmetrics.registerFont(TTFont("Comf", os.path.join(FONTS, "Comfortaa-Regular.ttf")))
pdfmetrics.registerFont(TTFont("ComfB", os.path.join(FONTS, "Comfortaa-Bold.ttf")))

BLEED = 3*mm

# ---- Logo temizle + kırp ----
def prep_logo():
    # Beyaz zemin + nötr-gri çerçeve çizgisini sil; mavi içeriği (yüksek doygunluk) koru.
    im = Image.open(LOGO_SRC).convert("RGB")
    a = np.array(im).astype(int)
    mx = a.max(axis=2); mn = a.min(axis=2)
    neutral_light = (mx - mn <= 16) & (mn >= 195)   # beyaz + gri çerçeve → beyaz
    a[neutral_light] = [255,255,255]
    im2 = Image.fromarray(a.astype("uint8"))
    bg = Image.new("RGB", im2.size, (255,255,255))
    bbox = ImageChops.difference(im2, bg).getbbox()
    im3 = im2.crop(bbox)
    p = os.path.join(TMP, "logo_clean.png")
    im3.save(p, dpi=(300,300))
    return p, im3.size[0]/im3.size[1]  # path, aspect (w/h)

LOGO_CLEAN, LOGO_AR = prep_logo()
LOGO_RDR = ImageReader(LOGO_CLEAN)

# ---- QR üret (Instagram @ayhanerden_) ----
def prep_qr():
    qr = qrcode.QRCode(border=1, box_size=14,
                       error_correction=qrcode.constants.ERROR_CORRECT_M)
    qr.add_data("https://www.instagram.com/ayhanerden_/")
    qr.make(fit=True)
    img = qr.make_image(fill_color=(4,13,126), back_color="white").convert("RGB")
    p = os.path.join(TMP, "qr.png"); img.save(p, dpi=(300,300))
    return p

QR_RDR = ImageReader(prep_qr())

# ---- yardımcılar ----
def tracked_w(s, font, size, char):
    base = pdfmetrics.stringWidth(s, font, size)
    return base + char*(len(s)-1) if len(s) > 1 else base

def fit_size(c, text, font, max_w, start, lo=6, char=0):
    s = start
    while s > lo and tracked_w(text, font, s, char) > max_w:
        s -= 0.5
    return s

def t_left(c, x, y, s, font, size, color, char=0):
    to = c.beginText(); to.setTextOrigin(x, y); to.setFont(font, size)
    to.setFillColor(color)
    if char: to.setCharSpace(char)
    to.textOut(s); c.drawText(to)

def t_center(c, cx, y, s, font, size, color, char=0):
    w = tracked_w(s, font, size, char)
    t_left(c, cx - w/2, y, s, font, size, color, char)

def wrap(text, font, size, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        test = (cur+" "+w).strip()
        if pdfmetrics.stringWidth(test, font, size) <= max_w:
            cur = test
        else:
            if cur: lines.append(cur)
            cur = w
    if cur: lines.append(cur)
    return lines

def chip_logo(c, cx, cy, chip_w):
    """Koyu zeminde resmi logo: temiz beyaz yuvarlak chip içinde."""
    pad = chip_w*0.14
    inner_w = chip_w - 2*pad
    inner_h = inner_w / LOGO_AR
    chip_h = inner_h + 2*pad
    c.setFillColor(WHITE)
    c.roundRect(cx-chip_w/2, cy-chip_h/2, chip_w, chip_h, chip_w*0.07, fill=1, stroke=0)
    c.drawImage(LOGO_RDR, cx-inner_w/2, cy-inner_h/2, inner_w, inner_h, mask="auto")
    return chip_h

def page(c, trim_w, trim_h):
    W = trim_w + 2*BLEED; H = trim_h + 2*BLEED
    c.setPageSize((W, H))
    for box in ("setTrimBox","setBleedBox","setArtBox"):
        try:
            if box=="setTrimBox": c.setTrimBox((BLEED,BLEED,BLEED+trim_w,BLEED+trim_h))
            if box=="setBleedBox": c.setBleedBox((0,0,W,H))
            if box=="setArtBox":  c.setArtBox((BLEED,BLEED,BLEED+trim_w,BLEED+trim_h))
        except Exception: pass
    return W, H

def bg(c, W, H, color):
    c.setFillColor(color); c.rect(0,0,W,H, fill=1, stroke=0)

# ================= 1) HANG TAG 60×90mm, 2 yüz =================
def hang_tag():
    tw, th = 60*mm, 90*mm
    c = canvas.Canvas(os.path.join(OUT,"1_hang_tag.pdf"))
    # --- ÖN: beyaz zemin ---
    W,H = page(c, tw, th); bg(c, W, H, WHITE)
    cx = W/2
    # delik (ip için) — ince outline kılavuz
    hole_y = BLEED + th - 7*mm
    c.setStrokeColor(HexColor("#B8C0D9")); c.setLineWidth(0.8)
    c.circle(cx, hole_y, 2.4*mm, stroke=1, fill=0)
    # logo — yükseklikle sabit (üst bölge), fiyatla çakışmaz
    lh = 30*mm; lw = lh*LOGO_AR
    lcy = BLEED + 60*mm
    c.drawImage(LOGO_RDR, cx-lw/2, lcy-lh/2, lw, lh, mask="auto")
    # fiyat (alt-orta, net ayrık)
    t_center(c, cx, BLEED + 26*mm, "600 TL", "Bebas", 38, PHTHALO, char=1.5)
    # alt site
    t_center(c, cx, BLEED + 8*mm, "stepsonclouds.com", "Comf", 7, MIDNIGHT, char=0.3)
    c.showPage()
    # --- ARKA: phthalo full-bleed ---
    W,H = page(c, tw, th); bg(c, W, H, PHTHALO)
    cx = W/2
    yz = BLEED + th*0.62
    t_center(c, cx, yz,            "DÜŞ, KALK,", "Bebas", 30, WHITE, char=1)
    t_center(c, cx, yz - 11.5*mm,  "YENİDEN", "Bebas", 30, WHITE, char=1)
    t_center(c, cx, yz - 23*mm,    "DENE.", "Bebas", 30, SKY, char=1)
    # CTA
    for i,l in enumerate(["Sen de adım at,","hareketi sürdür."]):
        t_center(c, cx, BLEED + 20*mm - i*5.2*mm, l, "Comf", 8.5, WHITE, char=0.2)
    t_center(c, cx, BLEED + 7*mm, "stepsonclouds.com", "Comf", 6.5, SKY, char=0.3)
    c.showPage(); c.save()

# ================= 2) SHELF TALKER A5 148×210mm =================
def shelf_talker():
    tw, th = 148*mm, 210*mm
    c = canvas.Canvas(os.path.join(OUT,"2_shelf_talker.pdf"))
    W,H = page(c, tw, th); bg(c, W, H, PHTHALO)
    ml = BLEED + 16*mm                 # sol marj
    mr = BLEED + tw - 16*mm            # sağ sınır
    colw = mr - ml
    # başlık
    y = BLEED + th - 34*mm
    t_left(c, ml, y,            "STEPS ON CLOUDS", "Bebas", 50, WHITE, char=1)
    t_left(c, ml, y - 16*mm,    "NEDİR?", "Bebas", 50, SKY, char=1)
    # gövde
    body = ("Moda yalnızca ne giydiğimizle değil; kendimizi nasıl taşıdığımızla, "
            "hayatta nasıl yer aldığımızla da ilgilidir.")
    body2 = ("Steps On Clouds; hareket eden, denemekten korkmayan, düşse de her "
             "seferinde yeniden kalkan insanlar için bir marka.")
    body3 = "Buradasın; çünkü sen de bu dünyanın bir parçasısın."
    by = y - 30*mm
    for para in (body, body2, body3):
        for line in wrap(para, "Comf", 11.5, colw):
            t_left(c, ml, by, line, "Comf", 11.5, WHITE, char=0.1)
            by -= 7.2*mm
        by -= 4*mm
    # motto (kapanış vurgu)
    by -= 2*mm
    t_left(c, ml, by,         "Düş, kalk, yeniden dene.", "ComfB", 12.5, SKY, char=0.1)
    t_left(c, ml, by - 7*mm,  "Sen de adım at, hareketi sürdür.", "ComfB", 12.5, SKY, char=0.1)
    # footer: chip logo solda, künye sağda (overlap yok)
    chip_w = 34*mm; cy = BLEED + 19*mm
    chip_logo(c, ml + chip_w/2, cy, chip_w)
    kx = ml + chip_w + 8*mm
    t_left(c, kx, cy + 2*mm,   "stepsonclouds.com", "Comf", 9.5, WHITE, char=0.2)
    t_left(c, kx, cy - 5*mm,   "@ayhanerden_", "Comf", 9.5, SKY, char=0.2)
    c.showPage(); c.save()

# ================= 3) POSTER A2 420×594mm =================
def poster():
    tw, th = 420*mm, 594*mm
    c = canvas.Canvas(os.path.join(OUT,"3_poster_A2.pdf"))
    W,H = page(c, tw, th); bg(c, W, H, PHTHALO)
    ml = BLEED + 42*mm
    colw = tw - 84*mm
    # eyebrow (üst)
    t_left(c, ml, BLEED + th - 52*mm,
           "STEPS ON CLOUDS  ×  ALA SKATEBOARDS", "Comf", 19, SKY, char=2)
    # hero motto — genişliğe otomatik sığdır
    s1 = fit_size(c, "DÜŞ, KALK,",   "Bebas", colw, 240, char=4)
    s2 = fit_size(c, "YENİDEN DENE.", "Bebas", colw, 240, char=4)
    hs = min(s1, s2)
    hy = BLEED + th*0.52
    t_left(c, ml, hy,             "DÜŞ, KALK,",   "Bebas", hs, WHITE, char=4)
    t_left(c, ml, hy - hs*1.06,   "YENİDEN DENE.", "Bebas", hs, SKY, char=4)
    # CTA
    t_left(c, ml, hy - hs*1.06 - 32*mm,
           "Sen de adım at, hareketi sürdür.", "ComfB", 34, WHITE, char=0.4)
    # alt: chip logo solda + künye sağda (overlap yok)
    chip_w = 66*mm; cy = BLEED + 80*mm
    chip_logo(c, ml + chip_w/2, cy, chip_w)
    kx = ml + chip_w + 16*mm
    t_left(c, kx, cy + 6*mm,  "stepsonclouds.com", "Comf", 20, SKY, char=1)
    t_left(c, kx, cy - 9*mm,  "@ayhanerden_", "Comf", 20, WHITE, char=1)
    c.showPage(); c.save()

# ================= 4) QR KART 90×50mm, 2 yüz =================
def qr_card():
    tw, th = 90*mm, 50*mm
    c = canvas.Canvas(os.path.join(OUT,"4_qr_kart.pdf"))
    # --- ÖN: beyaz, logo + QR ---
    W,H = page(c, tw, th); bg(c, W, H, WHITE)
    # logo sol
    lw = 33*mm; lh = lw/LOGO_AR
    c.drawImage(LOGO_RDR, BLEED + 7*mm, H/2 - lh/2, lw, lh, mask="auto")
    # QR sağ
    qsz = 30*mm
    qx = BLEED + tw - 7*mm - qsz
    qy = H/2 - qsz/2 + 2.5*mm
    c.drawImage(QR_RDR, qx, qy, qsz, qsz)
    t_center(c, qx + qsz/2, qy - 5*mm, "@ayhanerden_", "Comf", 7.5, PHTHALO, char=0.3)
    c.showPage()
    # --- ARKA: phthalo, ADIM AT ---
    W,H = page(c, tw, th); bg(c, W, H, PHTHALO)
    cx = W/2
    t_center(c, cx, H/2 + 1*mm, "ADIM AT.", "Bebas", 40, WHITE, char=2)
    t_center(c, cx, BLEED + 9*mm, "STEPS ON CLOUDS  ×  ALA SKATEBOARDS",
             "Comf", 7, SKY, char=0.8)
    c.showPage(); c.save()

if __name__ == "__main__":
    hang_tag(); shelf_talker(); poster(); qr_card()
    print("OK — 4 PDF üretildi:", OUT)
