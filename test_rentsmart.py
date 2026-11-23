"""Testes das regras de negócio. Rodar: python -m unittest -v"""
import csv
import os
import tempfile
import unittest

from rentsmart import Apartamento, Casa, Contrato, Estudio, Orcamento


class TestRegras(unittest.TestCase):
    def test_apartamento(self):
        self.assertEqual(Apartamento(1).aluguel_mensal(), 700)
        self.assertEqual(Apartamento(2, garagem=True).aluguel_mensal(), 1200)
        # desconto de 5% depois dos adicionais: (700 + 200 + 300) * 0,95
        self.assertEqual(Apartamento(2, True, possui_criancas=False).aluguel_mensal(), 1140)

    def test_casa(self):
        self.assertEqual(Casa(1).aluguel_mensal(), 900)
        self.assertEqual(Casa(2, garagem=True).aluguel_mensal(), 1450)

    def test_estudio(self):
        self.assertEqual(Estudio().aluguel_mensal(), 1200)
        self.assertEqual(Estudio(vagas=2).aluguel_mensal(), 1450)
        self.assertEqual(Estudio(vagas=4).aluguel_mensal(), 1570)

    def test_validacoes(self):
        for criar in (lambda: Casa(3), lambda: Estudio(vagas=1), lambda: Contrato(0), lambda: Contrato(6)):
            with self.assertRaises(ValueError):
                criar()

    def test_contrato_soma_sempre_2000(self):
        for n in range(1, 6):
            self.assertAlmostEqual(sum(Contrato(n).valor_parcela(m) for m in range(1, 13)), 2000)
        self.assertEqual(Contrato(3).valor_parcela(3), 666.66)

    def test_csv_12_meses(self):
        orc = Orcamento(Casa(1), Contrato(5))
        with tempfile.TemporaryDirectory() as pasta:
            caminho = orc.exportar_csv(os.path.join(pasta, "p.csv"))
            with open(caminho, encoding="utf-8-sig") as f:
                linhas = list(csv.reader(f, delimiter=";"))
        self.assertEqual(len(linhas), 13)
        self.assertEqual(linhas[1], ["1", "900,00", "400,00", "1300,00"])
        self.assertEqual(linhas[6], ["6", "900,00", "0,00", "900,00"])


if __name__ == "__main__":
    unittest.main()
