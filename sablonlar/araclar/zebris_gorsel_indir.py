#!/usr/bin/env python3
"""Yürüme Analizi sayfasının donanım zinciri — üç üreticiden SEO adlı görsel indirme.

Zincir:  Zebris (sensörlü band + basınç ölçümü) → Contemplas (video/yazılım katmanı)
         → Amfit (dijital ayak kalıbı + CAD/CAM tabanlık üretimi)

Hedefler: ~/Desktop/Zebris-Yurume-Analizi-Gorselleri/     (10 kare)
          ~/Desktop/Contemplas-Yurume-Analizi-Gorselleri/ (3 kare)
          ~/Desktop/Amfit-Tabanlik-Uretim-Gorselleri/     (3 kare)

Not: zebris.de TYPO3 kullanıyor; sayfada görseller 576px türev olarak duruyor,
orijinal yalnız lightbox href'inde ya da srcset'in son adımında görünüyor.
Aşağıdaki yollar o orijinallerdir. contemplas.com WordPress (uploads = orijinal),
amfit.com düz webp servis ediyor.

Kardeş betik: proteor_gorsel_indir.py (aynı disiplin, farklı kaynak)
"""
import os, urllib.parse, urllib.request

BASE = "https://www.zebris.de"
HEDEF = os.path.expanduser("~/Desktop/Zebris-Yurume-Analizi-Gorselleri")
PREFIX = "ozgur-protez-yurume-analizi"
UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
                    "(KHTML, like Gecko) Chrome/126.0 Safari/537.36"}

# --- Contemplas: video/yazılım katmanı. Seçim ilkesi: tesis kimliği taşımayan,
#     yazılımın ne ölçtüğünü gösteren kareler öncelikli. (SEO slug, tam URL)
CONTEMPLAS_HEDEF = os.path.expanduser("~/Desktop/Contemplas-Yurume-Analizi-Gorselleri")
CONTEMPLAS = [
    ("contemplas-yazilim-olcum-modulleri",
     "https://contemplas.com/wp-content/uploads/2025/12/gait-analysis-parameters.png"),
    ("contemplas-cok-kamerali-video-analizi",
     "https://contemplas.com/wp-content/uploads/2021/12/multicamera-systems.jpg"),
    ("contemplas-templo-yazilimi-ekrani",
     "https://contemplas.com/wp-content/uploads/2020/11/Bildschirm_new.png"),
]

# --- Amfit: dijital kalıp + freze. Şartname "pimli sayısallaştırıcı" diyor; bu yüzden
#     iMPRESS (köpük kalıp tarayıcı) kareleri ALINMADI — farklı ölçüm yöntemi.
AMFIT_HEDEF = os.path.expanduser("~/Desktop/Amfit-Tabanlik-Uretim-Gorselleri")
AMFIT_PREFIX = "ozgur-protez-kisiye-ozel-tabanlik"
AMFIT = [
    ("amfit-pimli-dijitizer-ve-cad-cam-freze",
     "https://amfit.com/images/products/mill-and-digi.webp"),
    ("amfit-freze-tabanlik-uretimi",
     "https://amfit.com/images/products/mill-5811pb-insole-ko.webp"),
    ("amfit-cam-yazilimi-tabanlik-yerlesimi",
     "https://amfit.com/images/products/amfitcam-hero.webp"),
]

# (SEO slug, kaynak yolu)
# ⚠️ Render-and-review turunda elenenler (17 Ağu): Laufbaender/TLR4_h.jpg = Reebok
# tüketici koşu bandı (klinik cihaz değil, medikal sayfada marka karışıklığı) ·
# Trittschaum_Aufsicht_260520.jpg = üstü boş teal plaka (basınç haritası DEĞİL).
SECIM = [
    ("zebris-fdm-t-klinik-yurume-bandi",
     "/fileadmin/Editoren/Fotos-Bereiche/Laufbaender_12_2020/FDM_THQ.jpeg"),
    ("zebris-fdm-t-yurume-bandi-tutamakli",
     "/fileadmin/Editoren/Fotos-Bereiche/Laufbaender_12_2020/FDM_THL.jpeg"),
    ("zebris-yurume-analizi-yazilimi-kamera-gorunumu",
     "/fileadmin/Editoren/Fotos-Bereiche/FDM-T/EN Ganganalyse FDM-T Kamera mit-Schuhen.jpg"),
    ("zebris-ayak-yuvarlanma-basinc-dagilimi-ekrani",
     "/fileadmin/Editoren/Fotos-Bereiche/FDM-T/EN Ganganalyse FDM-T Kamera Abrollansicht-MPP mit-Schuhen.jpg"),
    ("zebris-yurume-analizi-raporu",
     "/fileadmin/Editoren/Fotos-Bereiche/FDM-T/FDM_T_Software_Report.jpg"),
    ("zebris-ayak-tabani-basinc-haritasi-3d",
     "/fileadmin/Editoren/Fotos-Bereiche/FDM-T/Druckgebirge_Reebok.png"),
    ("zebris-yurume-yolu-basinc-olcum-platformu",
     "/fileadmin/Editoren/Fotos-Bereiche/FDM/Gangstrecke.jpg"),
    ("zebris-pdm-c-basinc-olcum-platformu",
     "/fileadmin/Editoren/Fotos-Bereiche/PDM/PDM-C.jpg"),
    ("zebris-statik-durus-analizi-ciplak-ayak",
     "/fileadmin/Editoren/Fotos-Bereiche/FDM/EN Standanalyse barfuss.jpg"),
    ("zebris-ayak-basinc-dagilimi-3d-model",
     "/fileadmin/Editoren/Content-2026/Trittschaum/Trittschaum_Druckgebirge_260520.jpg"),
]


def boyut(veri):
    """PNG/JPEG genişlik-yükseklik (harici bağımlılık yok)."""
    try:
        if veri[:8] == b"\x89PNG\r\n\x1a\n":
            return int.from_bytes(veri[16:20], "big"), int.from_bytes(veri[20:24], "big")
        if veri[:2] == b"\xff\xd8":
            i = 2
            while i < len(veri) - 9:
                if veri[i] != 0xFF:
                    i += 1
                    continue
                m = veri[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    return (int.from_bytes(veri[i + 7:i + 9], "big"),
                            int.from_bytes(veri[i + 5:i + 7], "big"))
                i += 2 + int.from_bytes(veri[i + 2:i + 4], "big")
    except Exception:
        pass
    return 0, 0


def indir(klasor, onek, kalemler):
    os.makedirs(klasor, exist_ok=True)
    for slug, yol in kalemler:
        url = yol if yol.startswith("http") else BASE + urllib.parse.quote(yol, safe="/:%")
        try:
            veri = urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=45).read()
        except Exception as e:
            print(f"  ✗ {slug}: {e}")
            continue
        uzanti = ".jpg" if yol.lower().endswith((".jpg", ".jpeg")) else os.path.splitext(yol)[1].lower()
        ad = f"{onek}-{slug}{uzanti}"
        with open(os.path.join(klasor, ad), "wb") as f:
            f.write(veri)
        w, h = boyut(veri)
        olcu = f"{w}×{h}" if w else "webp"
        print(f"  ✓ {ad}  {olcu}  {len(veri)//1024}KB")
    print(f"  → {klasor}\n")


def main():
    print("ZEBRIS — sensörlü band + basınç ölçümü")
    indir(HEDEF, PREFIX, SECIM)
    print("CONTEMPLAS — video/yazılım katmanı")
    indir(CONTEMPLAS_HEDEF, PREFIX, CONTEMPLAS)
    print("AMFIT — dijital ayak kalıbı + CAD/CAM tabanlık")
    indir(AMFIT_HEDEF, AMFIT_PREFIX, AMFIT)


if __name__ == "__main__":
    main()
