#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SOC Marka Denetim Raporu — grafik üretimi (radar + yatay bar).
Marka paleti (soc-mavi): Phthalo #040D7E · Sky #72CBDF · Mist #EAF6EB.
DejaVu Sans (Türkçe-güvenli). Yüksek DPI. AI-slop yok.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm

# DejaVu Sans — Türkçe karakterleri taşır, matplotlib varsayılanı
plt.rcParams["font.family"] = "DejaVu Sans"
plt.rcParams["axes.unicode_minus"] = False

PHTHALO = "#040D7E"
SKY     = "#72CBDF"
MIST    = "#EAF6EB"
INK     = "#101010"
GRID    = "#C9D6DC"   # açık nötr — referans kesikli

# Renk kodu (bar): <50 kırmızı, 50-59 turuncu, 60-69 sarı, 70+ yeşil
KIRMIZI = "#D90000"
TURUNCU = "#FF8000"
SARI    = "#FFC000"
YESIL   = "#2E7D32"

# 7 kategori — kaynak rapordan birebir
KATEGORILER = [
    "İçerik & Mesaj",
    "Dönüşüm",
    "Görünürlük / SEO",
    "Konumlandırma",
    "Marka & Güven",
    "Onur & Temsil",
    "Büyüme & Strateji",
]
DEGERLER = [32, 38, 45, 28, 55, 62, 30]


def renk_kodu(v):
    if v < 50:  return KIRMIZI
    if v < 60:  return TURUNCU
    if v < 70:  return SARI
    return YESIL


# ── 1. RADAR CHART ─────────────────────────────────────────────
def radar(path):
    n = len(KATEGORILER)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    vals = DEGERLER + DEGERLER[:1]
    ang = angles + angles[:1]

    fig, ax = plt.subplots(figsize=(7.4, 6.4), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # eksen yönü: tepeden başla, saat yönü
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)

    # 100 referans halkası — gri kesikli
    ref = [100] * n + [100]
    ax.plot(ang, ref, color=GRID, linewidth=1.1, linestyle=(0, (4, 3)), zorder=1)

    # skor alanı
    ax.plot(ang, vals, color=PHTHALO, linewidth=2.2, zorder=3)
    ax.fill(ang, vals, color=SKY, alpha=0.45, zorder=2)
    ax.scatter(angles, DEGERLER, color=PHTHALO, s=34, zorder=4, edgecolors="white", linewidths=1.0)

    # değer etiketleri — noktanın hemen dışında
    for a, v in zip(angles, DEGERLER):
        ax.annotate(str(v), xy=(a, v), xytext=(a, v + 9),
                    ha="center", va="center", fontsize=11,
                    fontweight="bold", color=PHTHALO, zorder=5)

    # kategori etiketleri
    ax.set_xticks(angles)
    ax.set_xticklabels(KATEGORILER, fontsize=10.5, color=INK)
    ax.tick_params(axis="x", pad=14)

    # radyal ızgara
    ax.set_ylim(0, 100)
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(["25", "50", "75", "100"], fontsize=8, color="#9AA7B0")
    ax.set_rlabel_position(90)
    ax.grid(color="#E4ECEF", linewidth=0.8)
    ax.spines["polar"].set_color("#E4ECEF")

    fig.tight_layout(pad=1.2)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("radar:", path)


# ── 2. YATAY BAR CHART ─────────────────────────────────────────
def bar(path):
    # yukarıdan aşağı kaynak sırası için ters çevir
    kat = KATEGORILER[::-1]
    val = DEGERLER[::-1]
    renkler = [renk_kodu(v) for v in val]
    y = np.arange(len(kat))

    fig, ax = plt.subplots(figsize=(8.6, 5.0))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    bars = ax.barh(y, val, color=renkler, height=0.62, zorder=3,
                   edgecolor="white", linewidth=0.6)

    # Hedef 70 dikey kesikli çizgi
    ax.axvline(70, color=PHTHALO, linewidth=1.4, linestyle=(0, (5, 3)), zorder=4)
    ax.text(70, len(kat) - 0.35, "Hedef 70", color=PHTHALO, fontsize=9.5,
            fontweight="bold", ha="center", va="bottom",
            bbox=dict(boxstyle="round,pad=0.25", fc="white", ec=PHTHALO, lw=0.8))

    # bar ucunda değer
    for b, v in zip(bars, val):
        ax.text(v + 1.4, b.get_y() + b.get_height() / 2, str(v),
                va="center", ha="left", fontsize=10.5, fontweight="bold", color=INK)

    ax.set_yticks(y)
    ax.set_yticklabels(kat, fontsize=10.5, color=INK)
    ax.set_xlim(0, 100)
    ax.set_xticks([0, 25, 50, 75, 100])
    ax.tick_params(axis="x", labelsize=8.5, colors="#9AA7B0")
    ax.tick_params(axis="y", length=0)

    # temiz çerçeve — sadece alt eksen ince
    for s in ["top", "right", "left"]:
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#E4ECEF")
    ax.xaxis.grid(True, color="#EEF3F5", linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)

    fig.tight_layout(pad=1.0)
    fig.savefig(path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("bar:", path)


if __name__ == "__main__":
    base = "/Users/ayhanerden/Fox/raporlar/_assets"
    radar(f"{base}/soc-radar.png")
    bar(f"{base}/soc-bar.png")
