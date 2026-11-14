"""sozdizim_tarama.py kapısı — kısa metin "ölçülemedi" (çıkış 3), --bolum ile yalnız bir bölüm ölçülür.
Çalıştır: python3 -m unittest sablonlar.araclar.tests.test_sozdizim_tarama -v
Kaynak: Denetmen'in 3. kaydı (14 Kas 2026) — caption'a alt metin karışınca SERT, kısa caption sessizce "temiz" sayılıyordu.
"""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ARAC = Path(__file__).resolve().parents[1] / "sozdizim_tarama.py"

KISA_CAPTION = "Yeşil kort, zeminde raketin gölgesi. Sabah antrenmanı erken başladı ve kimse acele etmedi.\n\nSenin sporun ne? Yorumlara yaz."

UZUN_ALT_METIN = (
    "Kare 1: Yeşil kortta yandan görünen tek bir bacak, beyaz uzun konçlu çorabın üstünde turkuaz bulut logosu duruyor. "
    "Kare 2: Kortta yürüyen iki bacak var ve arkada sarkan bir raket görünüyor, iki çorapta da aynı logo seçiliyor. "
    "Kare 3: Bir tenis topu raketin ucuyla beyaz ayakkabının arasında duruyor, arkada çoraplı iki bacak kadraja giriyor. "
    "Kare 4: Önde dik tutulmuş bir raket var, arkasında beyaz çoraplı ve beyaz ayakkabılı iki bacak görünüyor. "
    "Kare 5: Kortta adım atan iki bacak, beyaz çoraplar ve beyaz spor ayakkabılar, arkada yine bir raket duruyor.\n\n"
    "Kare 6: Gölge zemine uzun düşüyor ve çizgiler kadrajı çaprazlama kesiyor, ışık sol üstten geliyor."
)


def metin_md(caption=KISA_CAPTION, alt=UZUN_ALT_METIN):
    return f"# 01 · Kort\n\n## Caption (TR)\n{caption}\n\n## Hashtag\n#CloudOne\n\n## Alt metin\n{alt}\n\n## YZ etiketi\nhayır\n"


class SozdizimKapisiTestleri(unittest.TestCase):
    def setUp(self):
        d = tempfile.TemporaryDirectory()
        self.addCleanup(d.cleanup)
        self.dizin = Path(d.name)

    def yaz(self, ad, metin):
        p = self.dizin / ad
        p.write_text(metin, encoding="utf-8")
        return p

    def cli(self, *args):
        return subprocess.run([sys.executable, str(ARAC), *args], capture_output=True, text=True)

    def test_kisa_metin_olculemedi_cikis_3(self):
        r = self.cli(str(self.yaz("kisa.md", KISA_CAPTION)))
        self.assertEqual(r.returncode, 3)
        self.assertIn("ÖLÇÜLEMEDİ — kısa", r.stdout)
        self.assertNotIn("Sözdizimi temiz", r.stdout)
        self.assertIn("Temiz sayılmaz", r.stdout)

    def test_bolum_yalniz_caption_olcer(self):
        dosya = self.yaz("metin.md", metin_md())
        tum = self.cli(str(dosya))
        self.assertNotEqual(tum.returncode, 3)          # alt metin karışınca ölçüm yapılıyor
        bolum = self.cli("--bolum", "Caption (TR)", str(dosya))
        self.assertEqual(bolum.returncode, 3)           # yalnız caption: kısa → ölçülemedi
        self.assertIn("ÖLÇÜLEMEDİ — kısa", bolum.stdout)
        self.assertIn("[Caption (TR)]", bolum.stdout)

    def test_bolum_bulunamadi(self):
        r = self.cli("--bolum", "Yok Böyle Bölüm", str(self.yaz("metin.md", metin_md())))
        self.assertEqual(r.returncode, 3)
        self.assertIn("bölüm bulunamadı", r.stdout)

    def test_uzun_bolum_olculur(self):
        r = self.cli("--bolum", "Alt metin", str(self.yaz("metin.md", metin_md())))
        self.assertIn(r.returncode, (0, 1, 2))
        self.assertNotIn("ÖLÇÜLEMEDİ", r.stdout)

    def test_sert_olculemediyi_ezer(self):
        # Bir dosya SERT, öbürü kısa: çıkış SERT'in kodu (1) olmalı, ölçülemedi onu gizlememeli.
        sert = ("Bu bir ürün değil, bir yaşam biçimi. " * 3 + "Bu bir çorap değil, bir duruş. " * 3 +
                "Bu bir hediye değil, bir söz. " * 3 + "Bu bir marka değil, bir hareket. " * 3)
        r = self.cli(str(self.yaz("sert.md", sert)), str(self.yaz("kisa.md", KISA_CAPTION)))
        if "SERT" in r.stdout:
            self.assertEqual(r.returncode, 1)
        self.assertIn("ÖLÇÜLEMEDİ — kısa", r.stdout)

    def test_json_olculemedi_kaydi(self):
        r = self.cli("--json", "--bolum", "Caption (TR)", str(self.yaz("metin.md", metin_md())))
        veri = json.loads(r.stdout)
        self.assertEqual(len(veri), 1)
        self.assertTrue(veri[0]["olculemedi"])
        self.assertEqual(veri[0]["bolum"], "Caption (TR)")
        self.assertEqual(r.returncode, 3)


if __name__ == "__main__":
    unittest.main()
