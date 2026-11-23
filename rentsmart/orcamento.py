"""Orçamento: junta o imóvel e o contrato, mostra o resumo e gera a projeção de 12 meses."""
import csv


def brl(valor):
    """Formata em reais: 1234.5 -> 'R$ 1.234,50'."""
    texto = f"{abs(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{'-' if valor < 0 else ''}R$ {texto}"


class Contrato:
    """Taxa contratual, separada do aluguel, paga em 1 a 5 parcelas."""

    TAXA = 2000.0
    MAX_PARCELAS = 5

    def __init__(self, parcelas=1):
        if not 1 <= parcelas <= self.MAX_PARCELAS:
            raise ValueError(f"Parcelas devem ser de 1 a {self.MAX_PARCELAS}.")
        self.parcelas = parcelas

    def valor_parcela(self, mes):
        """Parcela devida no mês (1..12); a última absorve o arredondamento dos centavos."""
        if mes > self.parcelas:
            return 0.0
        parcela = round(self.TAXA / self.parcelas, 2)
        if mes == self.parcelas:
            return round(self.TAXA - parcela * (self.parcelas - 1), 2)
        return parcela


class Orcamento:
    MESES = 12

    def __init__(self, imovel, contrato):
        self.imovel = imovel
        self.contrato = contrato

    def projecao(self):
        """Lista de dicionários, um por mês, com aluguel, parcela do contrato e total."""
        aluguel = self.imovel.aluguel_mensal()
        linhas = []
        for mes in range(1, self.MESES + 1):
            parcela = self.contrato.valor_parcela(mes)
            linhas.append({"mes": mes, "aluguel": aluguel, "parcela_contrato": parcela,
                           "total_mes": round(aluguel + parcela, 2)})
        return linhas

    def resumo(self):
        linhas = ["=" * 52, "ORÇAMENTO DE LOCAÇÃO - R.M IMÓVEIS (RentSmart)", "=" * 52,
                  "Aluguel mensal:"]
        for descricao, valor in self.imovel.itens():
            linhas.append(f"  {descricao:<36}{brl(valor):>14}")
        linhas.append(f"  {'TOTAL ALUGUEL MENSAL':<36}{brl(self.imovel.aluguel_mensal()):>14}")
        linhas += ["-" * 52, "Taxa contratual (cobrada à parte do aluguel):",
                   f"  {'Valor da taxa':<36}{brl(self.contrato.TAXA):>14}",
                   f"  {'Parcelamento':<36}{self.contrato.parcelas:>13}x",
                   f"  {'Valor da parcela':<36}{brl(self.contrato.valor_parcela(1)):>14}"]
        if self.contrato.valor_parcela(self.contrato.parcelas) != self.contrato.valor_parcela(1):
            linhas.append(f"  {'Última parcela (ajuste centavos)':<36}"
                          f"{brl(self.contrato.valor_parcela(self.contrato.parcelas)):>14}")
        total_ano = sum(l["total_mes"] for l in self.projecao())
        linhas += ["-" * 52, f"  {'Total previsto em 12 meses':<36}{brl(total_ano):>14}", "=" * 52]
        return "\n".join(linhas)

    def exportar_csv(self, caminho):
        # utf-8-sig + ';' para o Excel em português abrir com acentos e colunas certas.
        with open(caminho, "w", newline="", encoding="utf-8-sig") as arquivo:
            escritor = csv.writer(arquivo, delimiter=";")
            escritor.writerow(["Mês", "Aluguel (R$)", "Parcela contrato (R$)", "Total do mês (R$)"])
            for l in self.projecao():
                escritor.writerow([l["mes"]] + [f"{l[c]:.2f}".replace(".", ",")
                                                for c in ("aluguel", "parcela_contrato", "total_mes")])
        return caminho
