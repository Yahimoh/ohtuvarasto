import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.vaara_tilavuus_varasto = Varasto(-1)
        self.vaara_saldo_varasto = Varasto(10, -1)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
    
    def test_varaston_asettaminen_vaaralla_tilavuudella(self):
        self.assertEqual(self.vaara_tilavuus_varasto.tilavuus, 0)
    
    def test_varaston_asettaminen_vaaralla_saldolla(self):
        self.assertEqual(self.vaara_saldo_varasto.saldo, 0)

    def test_varastoon_lisataan_vaara_maara(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)
    
    def test_maara_pienempi_kuin_mita_mahtuu(self):
        self.varasto.lisaa_varastoon(5)
        self.assertEqual(self.varasto.saldo, 5)
    
    def test_maara_sama_kuin_mita_mahtuu(self):
        self.varasto.lisaa_varastoon(10)
        self.assertEqual(self.varasto.saldo, 10)

    def test_maara_enemman_kuin_mita_mahtuu(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, 10)

    def test_varastosta_otetaan_vaara_maara(self):
        otettu = self.varasto.ota_varastosta(-1)
        self.assertEqual(otettu, 0.0)
    
    def test_otetaan_kaikki_mita_voidaan(self):
        otettu = self.varasto.ota_varastosta(1)
        self.assertEqual(otettu, 0)

    def test_str(self):
        self.assertEqual(self.varasto.__str__(), "saldo = 0, vielä tilaa 10")

