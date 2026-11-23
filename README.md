# RentSmart — Orçamento de Locação (R.M Imóveis)

Aplicação de terminal em Python que calcula o orçamento de locação da R.M Imóveis aplicando as regras comerciais (adicionais, desconto, estacionamento e taxa contratual), exibe um resumo detalhado e gera um arquivo CSV com a projeção dos 12 primeiros meses.

Trabalho da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**.

🎥 Vídeo pitch: https://youtu.be/3TI2eH1Kdfc

## Requisitos

- Python 3.8 ou superior (só biblioteca padrão, nada para instalar).

## Como executar

```bash
git clone https://github.com/felipe-008/rentsmart.git
cd rentsmart
python main.py
```

O programa pergunta, nesta ordem: tipo do imóvel, quartos, garagem/estacionamento, se possui crianças (apartamento) e em quantas parcelas pagar a taxa contratual. Respostas inválidas repetem a pergunta.

Ao final, mostra o orçamento e grava `projecao_12_meses.csv` na pasta atual (separador `;`, abre direto no Excel).

## Testes

```bash
python -m unittest -v
```

## Regras implementadas

| Imóvel | Aluguel-base | Adicionais | Desconto |
|---|---|---|---|
| Apartamento | R$ 700,00 | 2 quartos +R$ 200,00; garagem +R$ 300,00 | 5% se não possui crianças, após os adicionais |
| Casa | R$ 900,00 | 2 quartos +R$ 250,00; garagem +R$ 300,00 | — |
| Estúdio | R$ 1.200,00 | pacote 2 vagas R$ 250,00; vaga extra +R$ 60,00 | — |

Taxa contratual de R$ 2.000,00 em 1 a 5 parcelas, mostrada separada do aluguel. Quando a divisão não é exata, a última parcela ajusta os centavos (ex.: 3x = 666,67 + 666,67 + 666,66).

## Estrutura

```
rentsmart/
├── main.py               # interface de terminal: entradas e validação
├── rentsmart/
│   ├── imoveis.py        # Imovel (abstrata), ImovelComGaragem, Apartamento, Casa, Estudio
│   └── orcamento.py      # Contrato, Orcamento (resumo, projeção, CSV)
├── test_rentsmart.py     # testes das regras
└── docs/                 # parte teórica (PDF) e roteiro do vídeo
```

## Exemplo de saída

Apartamento, 2 quartos, garagem, sem crianças, contrato em 3x:

```
Aluguel mensal:
  Aluguel-base (Apartamento)               R$ 700,00
  Adicional 2 quartos                      R$ 200,00
  Vaga de garagem                          R$ 300,00
  Desconto 5% (sem crianças)               -R$ 60,00
  TOTAL ALUGUEL MENSAL                   R$ 1.140,00
Taxa contratual (cobrada à parte do aluguel):
  Valor da taxa                          R$ 2.000,00
  Parcelamento                                    3x
  Valor da parcela                         R$ 666,67
  Última parcela (ajuste centavos)         R$ 666,66
  Total previsto em 12 meses            R$ 15.680,00
```
