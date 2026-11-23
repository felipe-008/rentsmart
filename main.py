"""RentSmart - interface de terminal: coleta os dados, valida, mostra o orçamento e gera o CSV."""
from rentsmart import Apartamento, Casa, Contrato, Estudio, Orcamento


def perguntar_opcao(pergunta, opcoes):
    """Repete a pergunta até o usuário digitar uma das opções válidas."""
    while True:
        resposta = input(f"{pergunta} [{'/'.join(opcoes)}]: ").strip().upper()
        if resposta in opcoes:
            return resposta
        print(f"  Opção inválida. Escolha entre: {', '.join(opcoes)}.")


def perguntar_inteiro(pergunta, minimo, maximo):
    while True:
        resposta = input(f"{pergunta} ({minimo} a {maximo}): ").strip()
        if resposta.isdigit() and minimo <= int(resposta) <= maximo:
            return int(resposta)
        print(f"  Digite um número inteiro entre {minimo} e {maximo}.")


def sim(pergunta):
    return perguntar_opcao(pergunta, ["S", "N"]) == "S"


def coletar_imovel():
    print("\nTipos de imóvel:\n  A - Apartamento (R$ 700,00)\n  C - Casa (R$ 900,00)\n  E - Estúdio (R$ 1.200,00)")
    tipo = perguntar_opcao("Escolha o tipo", ["A", "C", "E"])
    if tipo == "E":
        if not sim("Deseja estacionamento (pacote de 2 vagas por R$ 250,00)?"):
            return Estudio()
        return Estudio(vagas=2 + perguntar_inteiro("Vagas adicionais a R$ 60,00 cada", 0, 10))
    quartos = perguntar_inteiro("Quantidade de quartos", 1, 2)
    garagem = sim("Deseja vaga de garagem (R$ 300,00)?")
    if tipo == "C":
        return Casa(quartos, garagem)
    return Apartamento(quartos, garagem, possui_criancas=sim("Possui crianças?"))


def main():
    print("=== RentSmart - R.M Imóveis ===")
    imovel = coletar_imovel()
    contrato = Contrato(perguntar_inteiro("\nParcelas da taxa contratual de R$ 2.000,00", 1, Contrato.MAX_PARCELAS))
    orcamento = Orcamento(imovel, contrato)
    print("\n" + orcamento.resumo())
    caminho = orcamento.exportar_csv("projecao_12_meses.csv")
    print(f"\nProjeção de 12 meses salva em: {caminho}")


if __name__ == "__main__":
    main()
