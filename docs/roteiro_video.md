# Roteiro do vídeo pitch (RentSmart)

Duração-alvo: **3:40 a 3:55** (limite 4:00). Fala em ritmo normal, sem correr.
Gravar a tela inteira (OBS). Publicar no YouTube como **Não listado**.

**Antes de gravar, deixe abertas nesta ordem:** README no GitHub → PDF na página do fluxograma → `imoveis.py` → `orcamento.py` → terminal na pasta do projeto → Excel (o CSV é gerado na hora) → terminal para os testes.

O que está em _itálico_ é ação na tela, não é para falar.

---

## 1. O problema — 0:00 a 0:30
_Tela: README do repositório no GitHub._

> Olá, eu sou o Felipe Campos Avila e este é o RentSmart. A R.M Imóveis aluga apartamentos, casas e estúdios, e hoje os atendentes calculam os orçamentos de locação à mão. Isso deixa o atendimento lento e abre espaço para erro nos adicionais, nos descontos e na taxa de contrato. O RentSmart resolve isso: recebe as características da locação, aplica as regras da imobiliária sozinho, mostra como o valor foi formado e gera uma planilha com os pagamentos do primeiro ano.

## 2. O fluxograma — 0:30 a 1:05
_Tela: PDF na página 3 (fluxograma). Acompanhe com o mouse._

> Antes de programar, montei o fluxograma. O programa mostra os tipos de imóvel e lê a escolha; se a opção for inválida, pergunta de novo, e isso vale para todas as perguntas. Se for estúdio, pergunta se o cliente quer estacionamento. Se for casa ou apartamento, pergunta os quartos e a garagem, e, no apartamento, se o cliente tem crianças, por causa do desconto. Depois lê em quantas parcelas vai a taxa de contrato, calcula tudo, mostra o resumo e gera o CSV.

## 3. As classes de imóvel — 1:05 a 1:45
_Tela: `rentsmart/imoveis.py`. Role devagar de cima para baixo._

> No arquivo imoveis ponto py ficam os imóveis. A classe Imovel é abstrata: ela define que todo aluguel é a base, mais os adicionais, menos um desconto, e faz essa conta num método só. Casa e apartamento têm a mesma regra de segundo quarto e garagem, então as duas herdam da classe ImovelComGaragem. Repara que a Casa não tem nenhum método, só os valores. O Apartamento só muda o desconto, de cinco por cento para quem não tem crianças. E o Estudio tem a regra do pacote de vagas.

## 4. Contrato e orçamento — 1:45 a 2:10
_Tela: `rentsmart/orcamento.py`._

> No orcamento ponto py, a classe Contrato cuida da taxa de dois mil reais em até cinco vezes; quando a divisão não fecha, a última parcela ajusta os centavos. A classe Orcamento recebe o imóvel e o contrato, monta o resumo e gera a projeção de doze meses. Aluguel e taxa ficam sempre separados.

## 5. Execução — 2:10 a 3:00
_Tela: terminal na pasta do projeto. Digite `python main.py`._

> Vamos rodar. _(digite X e Enter)_ Se eu digito uma opção que não existe, ele pergunta de novo. _(A, 2, S, N, 3)_ Agora: apartamento, dois quartos, com garagem, sem crianças, e a taxa em três vezes.
>
> _(aponte o resumo)_ Setecentos de base, mais duzentos do quarto e trezentos da garagem dá mil e duzentos; com o desconto de cinco por cento, o aluguel fica em mil cento e quarenta. Separada, vem a taxa: três parcelas, e a última fica um centavo menor para fechar os dois mil.

## 6. O CSV — 3:00 a 3:20
_Tela: abra `projecao_12_meses.csv` no Excel._

> Este é o CSV gerado. Nos três primeiros meses o cliente paga o aluguel mais a parcela do contrato, e depois só o aluguel. No primeiro ano são quinze mil seiscentos e oitenta reais.

## 7. Testes e fechamento — 3:20 a 3:50
_Tela: terminal. Digite `python -m unittest -v`._

> Os testes automáticos conferem cada regra, e todos passam. A orientação a objetos deixou cada regra num lugar só: a herança evita repetir código, e o orçamento funciona com qualquer imóvel sem saber qual é. Um tipo novo de imóvel é só uma classe nova. Obrigado!

---

**Dicas**
- Leia o texto em voz alta uma vez antes de gravar, cronometrando no celular.
- Se passar de 4:00, corte a última frase do trecho 3 ("E o Estudio...") e a do trecho 6 ("No primeiro ano...").
- Se gravar em partes (um arquivo por trecho), mande os arquivos que eu junto num vídeo só.
