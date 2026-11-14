"""instagram_onay_karti.py testleri — çalıştır: python3 -m unittest sablonlar.araclar.tests.test_instagram_onay_karti -v"""
import base64
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from sablonlar.araclar.instagram_kuyruk import oku
from sablonlar.araclar.instagram_onay_karti import kart_uret
from sablonlar.araclar.tests.test_instagram_kuyruk import kuyruk_metni

PNG_1X1 = base64.b64decode(
    "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="
)


def satir(slot, madde, durum, paket, baslik="Başlık", video="hayır", kredi=0):
    return f"| {slot} | 19:00 | {madde} | {baslik} | ürün | Higgsfield | {video} | {durum} | 0 | {kredi} | {paket} | — |\n"


class OnayKartiTestleri(unittest.TestCase):
    def setUp(self):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        self.kok = Path(d.name)
        self.paket_koku = self.kok / "Design " / "Paketler"
        self.cikti = self.kok / "kart"

    def paket(self, ad, metin="Metin", denetmen=None, yon=None, gorsel=True):
        p = self.paket_koku / ad
        p.mkdir(parents=True)
        (p / "metin.md").write_text(metin, encoding="utf-8")
        if gorsel:
            (p / "kare1.png").write_bytes(PNG_1X1)
        if denetmen:
            (p / "denetmen.md").write_text(denetmen, encoding="utf-8")
        if yon:
            (p / "yon-karti.md").write_text(yon, encoding="utf-8")
        return p

    def uret(self, slotlar, **kw):
        yol = self.kok / "kuyruk.md"
        yol.write_text(kuyruk_metni(slotlar), encoding="utf-8")
        index = kart_uret(oku(yol), self.cikti, paket_koku=self.paket_koku, **kw)
        return index.read_text(encoding="utf-8")

    def test_kartta_yalniz_bekleyenler(self):
        self.paket("a_04"); self.paket("a_05"); self.paket("a_01")
        html = self.uret([
            satir("2026-11-24", "04", "onay bekliyor", "a_04"),
            satir("2026-11-26", "05", "deneme karelerinde", "a_05"),
            satir("2026-11-19", "01", "onaylandı", "a_01"),
        ])
        self.assertIn('id="madde-04"', html)
        self.assertIn('id="madde-05"', html)
        self.assertNotIn('id="madde-01"', html)

    def test_baslik_ve_metin_birebir(self):
        self.paket("a_04", metin="İLK ADIMI ÖĞRETENE <b>kalın değil</b>")
        html = self.uret([satir("2026-11-24", "04", "onay bekliyor", "a_04", baslik="İLK ADIMI ÖĞRETENE")])
        self.assertIn("İLK ADIMI ÖĞRETENE", html)
        self.assertIn("&lt;b&gt;", html)
        self.assertNotIn("<b>kalın", html)

    def test_gorsel_kopyalanir_ve_baglanir(self):
        self.paket("a_04")
        html = self.uret([satir("2026-11-24", "04", "onay bekliyor", "a_04")])
        self.assertTrue((self.cikti / "medya" / "04" / "kare1.png").exists())
        self.assertIn('src="medya/04/kare1.png"', html)

    def test_asama_etiketi(self):
        self.paket("a_04"); self.paket("a_05", yon="Çizgi: spor")
        html = self.uret([
            satir("2026-11-24", "04", "onay bekliyor", "a_04"),
            satir("2026-11-26", "05", "deneme karelerinde", "a_05"),
        ])
        self.assertIn("Yayın onayı", html)
        self.assertIn("Yön onayı", html)
        self.assertIn("Çizgi: spor", html)

    def test_kredi_ve_denetmen_notu(self):
        self.paket("a_05", denetmen="DİKKAT: logo küçük kalmalı")
        html = self.uret([satir("2026-11-26", "05", "deneme karelerinde", "a_05", kredi=240)])
        self.assertIn("240 kredi", html)
        self.assertIn("DİKKAT: logo küçük kalmalı", html)

    def test_eksik_klasor_cokmez(self):
        html = self.uret([satir("2026-11-24", "04", "onay bekliyor", "yok_klasor")])
        self.assertIn("paket klasörü bulunamadı", html)
        self.assertIn('id="madde-04"', html)

    @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg yok")
    def test_buyuk_video_onizlemeye_cevrilir(self):
        p = self.paket("a_05", gorsel=False)
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc=size=1920x1080:rate=30",
             "-t", "3", "-pix_fmt", "yuv420p", str(p / "klip.mp4")],
            check=True,
        )
        esik = (p / "klip.mp4").stat().st_size - 1  # kaynak eşiğin üstünde → dönüştürme yolu
        html = self.uret([satir("2026-11-26", "05", "onay bekliyor", "a_05", video="evet")], video_esik_bayt=esik)
        onizleme = self.cikti / "medya" / "05" / "klip.mp4"
        self.assertTrue(onizleme.exists())
        self.assertLessEqual(onizleme.stat().st_size, esik)
        self.assertIn('src="medya/05/klip.mp4"', html)
        yukseklik = subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=height",
             "-of", "csv=p=0", str(onizleme)],
            capture_output=True, text=True,
        ).stdout.strip() if shutil.which("ffprobe") else "720"
        self.assertEqual(yukseklik, "720")

    @unittest.skipUnless(shutil.which("ffmpeg"), "ffmpeg yok")
    def test_onizleme_esigi_asmaz(self):
        # Son denetim: dönüştürülmüş önizleme de eşiği aşabiliyordu. Eşiği aşan dosya asla bağlanmaz.
        p = self.paket("a_08", gorsel=False)
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "testsrc2=size=1080x1920:rate=30",
             "-f", "lavfi", "-i", "anoisesrc=d=4", "-t", "4", "-pix_fmt", "yuv420p", "-shortest", str(p / "konusma.mp4")],
            check=True,
        )
        esik = 60_000
        html = self.uret([satir("2026-12-03", "08", "onay bekliyor", "a_08", video="evet")], video_esik_bayt=esik)
        onizleme = self.cikti / "medya" / "08" / "konusma.mp4"
        if 'src="medya/08/konusma.mp4"' in html:
            self.assertLessEqual(onizleme.stat().st_size, esik)
        else:
            self.assertIn("video önizlemesi üretilemedi", html)

    def test_html_tema_ve_baslik(self):
        self.paket("a_04")
        html = self.uret([satir("2026-11-24", "04", "onay bekliyor", "a_04")])
        self.assertIn("<title>Instagram Onay Kartı</title>", html)
        self.assertIn("prefers-color-scheme: dark", html)
        self.assertIn(':root[data-theme="dark"]', html)
        self.assertNotIn("<script src=", html)

    def test_artifact_sozlesmesi(self):
        self.paket("a_04")
        html = self.uret([satir("2026-11-24", "04", "onay bekliyor", "a_04")])
        for kalip in (r"<!doctype", r"<html[\s>]", r"<head[\s>]", r"<body[\s>]"):
            self.assertNotRegex(html.lower(), kalip)
        self.assertIn('<meta name="claude:viewport-fit-sides" content="cover">', html)
        self.assertIn("max(16px, env(safe-area-inset-left, 0px))", html)
        self.assertIn("max(16px, env(safe-area-inset-right, 0px))", html)
        self.assertIn("color-scheme: dark", html)

    def test_bos_kart(self):
        html = self.uret([satir("2026-11-19", "01", "onaylandı", "a_01")])
        self.assertIn("Kartta bekleyen paket yok", html)


if __name__ == "__main__":
    unittest.main()
