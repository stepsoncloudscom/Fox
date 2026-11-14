"""instagram_kuyruk.py testleri — çalıştır: python3 -m unittest sablonlar.araclar.tests.test_instagram_kuyruk -v"""
import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path

from sablonlar.araclar.instagram_kuyruk import (
    KuyrukHatasi,
    durdurulmali,
    kural_ihlalleri,
    oku,
    ozet_satiri,
    tampon_bayrak,
    tampon_gun,
)

ARAC = Path(__file__).resolve().parents[1] / "instagram_kuyruk.py"

BASLIK = "| slot | saat | madde | başlık | hat | yol | video | durum | tur | kredi | paket | not |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n"


def satir(slot, madde, durum, video="hayır", baslik="Başlık", not_="—"):
    return f"| {slot} | 19:00 | {madde} | {baslik} | ürün | arşiv | {video} | {durum} | 0 | 0 | — | {not_} |\n"


def kuyruk_metni(slotlar, kararlar="", heartbeat="| 2026-11-12 | kurulum | ilk |\n", bakiye="623 (2026-11-14)", gorev="AKTİF — "):
    return (
        "# Instagram Kuyruğu — @stepsoncloudscom\n\n"
        "## Sayaçlar\n"
        f"- görev: {gorev}\n"
        f"- bakiye: {bakiye}\n"
        "- dönem harcaması: 0\n\n"
        "## Slotlar\n" + BASLIK + "".join(slotlar) + "\n"
        "## Kararlar\n| tarih | madde | karar | not |\n|---|---|---|---|\n" + kararlar + "\n"
        "## Heartbeat\n| tarih | mod | özet |\n|---|---|---|\n" + heartbeat
    )


TEMEL = [
    satir("2026-11-19", "01", "onaylandı"),
    satir("2026-11-21", "02", "zamanlandı"),
    satir("2026-11-24", "04", "onay bekliyor", baslik="İLK ADIMI ÖĞRETENE"),
    satir("2026-11-26", "05", "deneme karelerinde", video="evet"),
    satir("—", "Y1", "yedek"),
]


class KuyrukTestleri(unittest.TestCase):
    def setUp(self):
        self.dizin = tempfile.TemporaryDirectory()
        self.addCleanup(self.dizin.cleanup)

    def yaz(self, metin, ad="kuyruk.md"):
        yol = Path(self.dizin.name) / ad
        yol.write_text(metin, encoding="utf-8")
        return yol

    def kuyruk(self, *args, **kw):
        return oku(self.yaz(kuyruk_metni(*args, **kw)))

    # --- tampon ---
    def test_tampon_ilk_hazir_olmayan_slota_kadar(self):
        self.assertEqual(tampon_gun(self.kuyruk(TEMEL), date(2026, 11, 16)), 8)

    def test_tampon_hepsi_hazirsa_son_slot_arti_bir(self):
        k = self.kuyruk([satir("2026-11-19", "01", "onaylandı"), satir("2026-11-21", "02", "zamanlandı")])
        self.assertEqual(tampon_gun(k, date(2026, 11, 16)), 6)

    def test_tampon_gelecek_slot_yoksa_sifir(self):
        k = self.kuyruk([satir("2026-11-10", "01", "yayında")])
        self.assertEqual(tampon_gun(k, date(2026, 11, 16)), 0)

    def test_bayrak_esikleri(self):
        self.assertEqual(tampon_bayrak(2), "DUR")
        self.assertEqual(tampon_bayrak(6), "DİKKAT")
        self.assertEqual(tampon_bayrak(7), "TEMİZ")

    # --- kendini durdurma ---
    def test_durdur_iki_hafta_karar_yoksa(self):
        k = self.kuyruk(TEMEL, kararlar="| 2026-11-16 | 01 | onay | — |\n")
        self.assertTrue(durdurulmali(k, date(2026, 12, 3)))

    def test_durdurma_yok_gecen_hafta_karar_varsa(self):
        k = self.kuyruk(TEMEL, kararlar="| 2026-11-16 | 01 | onay | — |\n")
        self.assertFalse(durdurulmali(k, date(2026, 11, 26)))

    def test_durdurma_yok_kartta_paket_yoksa(self):
        k = self.kuyruk([satir("2026-12-20", "01", "havuzda")])
        self.assertFalse(durdurulmali(k, date(2026, 12, 3)))

    def test_durdurma_yok_sistem_yeniyse(self):
        k = self.kuyruk(TEMEL, heartbeat="| 2026-11-19 | AKTİF | ilk |\n")
        self.assertFalse(durdurulmali(k, date(2026, 11, 26)))

    # --- kurallar ---
    def test_ihlal_haftada_iki_video(self):
        k = self.kuyruk([
            satir("2026-12-08", "07", "havuzda"),
            satir("2026-12-10", "10", "havuzda", video="evet"),
            satir("2026-12-12", "12", "havuzda", video="evet"),
        ])
        self.assertIn("2026-12-07 haftası: 2 video (en çok 1)", kural_ihlalleri(k))

    def test_ihlal_haftada_tek_gonderi(self):
        k = self.kuyruk([
            satir("2026-12-08", "07", "havuzda"),
            satir("2026-12-10", "11", "havuzda"),
            satir("2026-12-15", "13", "havuzda"),
            satir("2026-12-22", "16", "havuzda"),
            satir("2026-12-23", "17", "havuzda"),
        ])
        self.assertIn("2026-12-14 haftası: 1 gönderi (taban 2)", kural_ihlalleri(k))

    def test_bos_hafta_ihlal(self):
        k = self.kuyruk([
            satir("2026-12-08", "07", "havuzda"),
            satir("2026-12-10", "11", "havuzda"),
            satir("2026-12-22", "16", "havuzda"),
            satir("2026-12-23", "17", "havuzda"),
        ])
        self.assertIn("2026-12-14 haftası: 0 gönderi (taban 2)", kural_ihlalleri(k))

    def test_pasifler_sayilmaz(self):
        k = self.kuyruk([
            satir("2026-12-08", "07", "havuzda"),
            satir("2026-12-10", "10", "havuzda", video="evet"),
            satir("2026-12-12", "12", "çıkarıldı", video="evet"),
            satir("—", "15", "çıkarıldı", video="evet"),
            satir("—", "Y1", "yedek", video="evet"),
        ])
        self.assertEqual(kural_ihlalleri(k), [])

    def test_yil_donumu_tek_hafta(self):
        k = self.kuyruk([satir("2026-12-31", "20", "havuzda"), satir("2027-01-02", "21", "havuzda")])
        self.assertEqual(kural_ihlalleri(k), [])

    # --- okuma hataları ---
    def test_bozuk_tarih_satir_numarasi(self):
        yol = self.yaz(kuyruk_metni([satir("2026-13-40", "01", "havuzda")]))
        with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: geçersiz tarih"):
            oku(yol)

    def test_tire_tarih_yalniz_pasifte(self):
        yol = self.yaz(kuyruk_metni([satir("—", "01", "havuzda")]))
        with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: geçersiz tarih"):
            oku(yol)

    def test_bilinmeyen_durum(self):
        yol = self.yaz(kuyruk_metni([satir("2026-11-19", "01", "hazır")]))
        with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: bilinmeyen durum"):
            oku(yol)

    def test_eksik_sutun(self):
        yol = self.yaz(kuyruk_metni(["| 2026-11-19 | 19:00 | 01 | Başlık |\n"]))
        with self.assertRaisesRegex(KuyrukHatasi, r"satır \d+: 12 sütun bekleniyor"):
            oku(yol)

    # --- özet ---
    def test_bakiye_bilinmiyor(self):
        k = self.kuyruk(TEMEL, bakiye="? (2026-11-19)")
        self.assertIsNone(k.bakiye)
        self.assertIn("bakiye bilinmiyor", ozet_satiri(k, date(2026, 11, 16)))

    def test_ozet_satiri(self):
        self.assertEqual(
            ozet_satiri(self.kuyruk(TEMEL), date(2026, 11, 16)),
            "Instagram: kartta 2 paket · tampon 8 gün (TEMİZ) · kredi bakiye 623, dönem harcaması 0 · görev AKTİF",
        )

    def test_turkce_baslik_korunur(self):
        self.assertEqual(self.kuyruk(TEMEL).slotlar[2].baslik, "İLK ADIMI ÖĞRETENE")

    # --- CLI ---
    def cli(self, *args):
        return subprocess.run([sys.executable, str(ARAC), *args], capture_output=True, text=True)

    def test_cli_denetle_cikis_kodlari(self):
        temiz = self.yaz(kuyruk_metni([satir("2026-12-08", "07", "havuzda"), satir("2026-12-09", "08", "havuzda")]), "t.md")
        ihlalli = self.yaz(kuyruk_metni([satir("2026-12-08", "07", "havuzda")]), "i.md")
        bozuk = self.yaz(kuyruk_metni([satir("2026-11-19", "01", "hazır")]), "b.md")
        self.assertEqual(self.cli("denetle", "--kuyruk", str(temiz)).returncode, 0)
        r = self.cli("denetle", "--kuyruk", str(ihlalli))
        self.assertEqual(r.returncode, 1)
        self.assertIn("1 gönderi (taban 2)", r.stdout)
        self.assertEqual(self.cli("denetle", "--kuyruk", str(bozuk)).returncode, 2)

    def test_cli_durum_ve_ozet(self):
        yol = self.yaz(kuyruk_metni(TEMEL, kararlar="| 2026-11-16 | 01 | onay | — |\n"))
        self.assertEqual(self.cli("durum", "--kuyruk", str(yol), "--bugun", "2026-12-03").stdout.strip(), "DURAKLAT")
        self.assertEqual(self.cli("durum", "--kuyruk", str(yol), "--bugun", "2026-11-26").stdout.strip(), "DEVAM")
        self.assertIn("tampon 8 gün", self.cli("ozet", "--kuyruk", str(yol), "--bugun", "2026-11-16").stdout)


if __name__ == "__main__":
    unittest.main()
