"""Entidades de imóvel da R.M Imóveis: cada tipo sabe calcular o próprio aluguel."""
from abc import ABC, abstractmethod


class Imovel(ABC):
    """Base comum: guarda o aluguel-base e monta a lista de itens do aluguel mensal."""

    tipo = "Imóvel"
    aluguel_base = 0.0

    def __init__(self, quartos=1):
        if quartos not in (1, 2):
            raise ValueError("Quantidade de quartos deve ser 1 ou 2.")
        self.quartos = quartos

    @abstractmethod
    def adicionais(self):
        """Lista de (descrição, valor) somados ao aluguel-base."""

    def desconto(self, subtotal):
        """Valor a abater do subtotal. Por padrão, nenhum."""
        return 0.0

    def itens(self):
        """Composição do aluguel mensal: base, adicionais e desconto (negativo)."""
        itens = [(f"Aluguel-base ({self.tipo})", self.aluguel_base)] + self.adicionais()
        subtotal = sum(valor for _, valor in itens)
        desconto = self.desconto(subtotal)
        if desconto:
            itens.append(("Desconto 5% (sem crianças)", -desconto))
        return itens

    def aluguel_mensal(self):
        return round(sum(valor for _, valor in self.itens()), 2)


class ImovelComGaragem(Imovel):
    """Casas e apartamentos: adicional por 2º quarto e vaga de garagem opcional."""

    adicional_segundo_quarto = 0.0
    valor_garagem = 300.0

    def __init__(self, quartos=1, garagem=False):
        super().__init__(quartos)
        self.garagem = garagem

    def adicionais(self):
        itens = []
        if self.quartos == 2:
            itens.append(("Adicional 2 quartos", self.adicional_segundo_quarto))
        if self.garagem:
            itens.append(("Vaga de garagem", self.valor_garagem))
        return itens


class Apartamento(ImovelComGaragem):
    tipo = "Apartamento"
    aluguel_base = 700.0
    adicional_segundo_quarto = 200.0
    taxa_desconto = 0.05

    def __init__(self, quartos=1, garagem=False, possui_criancas=True):
        super().__init__(quartos, garagem)
        self.possui_criancas = possui_criancas

    def desconto(self, subtotal):
        # Regra da R.M: 5% sobre o aluguel já com os adicionais, só para quem não tem crianças.
        return 0.0 if self.possui_criancas else round(subtotal * self.taxa_desconto, 2)


class Casa(ImovelComGaragem):
    tipo = "Casa"
    aluguel_base = 900.0
    adicional_segundo_quarto = 250.0


class Estudio(Imovel):
    """Estúdio: sem 2º quarto; estacionamento é pacote de 2 vagas + vagas extras."""

    tipo = "Estúdio"
    aluguel_base = 1200.0
    valor_pacote = 250.0
    vagas_no_pacote = 2
    valor_vaga_extra = 60.0

    def __init__(self, vagas=0):
        super().__init__(quartos=1)
        if vagas < 0 or vagas == 1:
            raise ValueError("Estúdio aceita 0 vagas ou o pacote a partir de 2 vagas.")
        self.vagas = vagas

    def adicionais(self):
        if not self.vagas:
            return []
        itens = [(f"Pacote estacionamento ({self.vagas_no_pacote} vagas)", self.valor_pacote)]
        extras = self.vagas - self.vagas_no_pacote
        if extras:
            itens.append((f"{extras} vaga(s) adicional(is) x R$ 60,00", extras * self.valor_vaga_extra))
        return itens
