# Roteiro do vídeo pitch — RentSmart (passo a passo)

Duração: **cerca de 3:45** (limite 4:00). YouTube: **Não listado**.

Como ler este roteiro, em cada trecho:
- 🖥️ **TELA** = o que precisa estar na tela antes de começar a falar.
- 👉 **FAZER** = o que clicar ou digitar.
- 🎤 **FALAR** = o texto para ler.

Para trocar de janela durante a gravação, use **Alt + Tab**.

---

## PARTE 0 — Preparar tudo (antes de gravar, sem pressa)

1. **Feche o Excel**, se estiver aberto. Se o CSV estiver aberto no Excel, o programa não consegue gravar o arquivo e dá erro.
2. **Navegador, aba 1:** abra `https://github.com/felipe-008/rentsmart`. Role até o topo da página.
3. **Navegador, aba 2:** abra o PDF. No Explorador de Arquivos, vá em `Documentos\RentSmart\docs\` e dê dois cliques em `RentSmart_Parte_Teorica.pdf`. Vá até a **página 3** (fluxograma) e ajuste o zoom para o fluxograma inteiro caber na tela.
4. **VS Code:** abra a pasta `Documentos\RentSmart` (Arquivo → Abrir Pasta).
   - Na barra da esquerda, abra `rentsmart/imoveis.py` e `rentsmart/orcamento.py` (ficam como abas lá em cima).
   - Aperte **Ctrl + =** duas vezes para aumentar a letra.
   - Abra o terminal com **Ctrl + '**. Digite `python --version` e Enter: tem que aparecer `Python 3.14...`. Depois digite `cls` e Enter para limpar.
   - Deixe a aba `imoveis.py` selecionada, rolada até o topo.
5. **OBS:** em Fontes, use **Captura de Tela** (não Captura de Janela), para gravar tudo enquanto você troca de janela. Confira se o microfone está com volume.
6. Deixe a **aba do GitHub** na frente (Alt + Tab até ela).
7. No OBS, clique em **Iniciar Gravação**. Espere 2 segundos e comece.

---

## TRECHO 1 — O problema (0:00 a 0:30)

🖥️ **TELA:** navegador, aba do GitHub (README).

👉 **FAZER:** nada; se quiser, role a página devagar enquanto fala.

🎤 **FALAR:**
> Olá, eu sou o Felipe Campos Avila e este é o RentSmart. A R.M Imóveis aluga apartamentos, casas e estúdios, e hoje os atendentes calculam os orçamentos de locação à mão. Isso deixa o atendimento lento e abre espaço para erro nos adicionais, nos descontos e na taxa de contrato. O RentSmart resolve isso: recebe as características da locação, aplica as regras da imobiliária sozinho, mostra como o valor foi formado e gera uma planilha com os pagamentos do primeiro ano.

---

## TRECHO 2 — O fluxograma (0:30 a 1:05)

👉 **FAZER antes de falar:** clique na **aba do PDF** (página 3, fluxograma).

🖥️ **TELA:** fluxograma inteiro visível.

👉 **FAZER enquanto fala:** passe o mouse pelos quadros, de cima para baixo, acompanhando o que você fala.

🎤 **FALAR:**
> Antes de programar, montei o fluxograma. O programa mostra os tipos de imóvel e lê a escolha; se a opção for inválida, pergunta de novo, e isso vale para todas as perguntas. Se for estúdio, pergunta se o cliente quer estacionamento. Se for casa ou apartamento, pergunta os quartos e a garagem, e, no apartamento, se o cliente tem crianças, por causa do desconto. Depois lê em quantas parcelas vai a taxa de contrato, calcula tudo, mostra o resumo e gera o CSV.

---

## TRECHO 3 — As classes de imóvel (1:05 a 1:45)

👉 **FAZER antes de falar:** **Alt + Tab** até o **VS Code**, na aba `imoveis.py`, no topo do arquivo.

🖥️ **TELA:** código do `imoveis.py`.

👉 **FAZER enquanto fala:** role devagar para baixo. Quando falar de cada classe, deixe ela na tela:
- "classe Imovel" → `class Imovel(ABC)` (começo do arquivo)
- "ImovelComGaragem" → `class ImovelComGaragem`
- "Casa" → `class Casa` (são só 3 linhas)
- "Apartamento" → `def desconto` dentro de `class Apartamento`
- "Estudio" → `class Estudio` (fim do arquivo)

🎤 **FALAR:**
> No arquivo imoveis ponto py ficam os imóveis. A classe Imovel é abstrata: ela define que todo aluguel é a base, mais os adicionais, menos um desconto, e faz essa conta num método só. Casa e apartamento têm a mesma regra de segundo quarto e garagem, então as duas herdam da classe ImovelComGaragem. Repara que a Casa não tem nenhum método, só os valores. O Apartamento só muda o desconto, de cinco por cento para quem não tem crianças. E o Estudio tem a regra do pacote de vagas.

---

## TRECHO 4 — Contrato e orçamento (1:45 a 2:10)

👉 **FAZER antes de falar:** no VS Code, clique na aba **`orcamento.py`** (lá em cima).

🖥️ **TELA:** código do `orcamento.py`.

👉 **FAZER enquanto fala:** comece em `class Contrato`; quando falar "a classe Orcamento", role até `class Orcamento`.

🎤 **FALAR:**
> No orcamento ponto py, a classe Contrato cuida da taxa de dois mil reais em até cinco vezes; quando a divisão não fecha, a última parcela ajusta os centavos. A classe Orcamento recebe o imóvel e o contrato, monta o resumo e gera a projeção de doze meses. Aluguel e taxa ficam sempre separados.

---

## TRECHO 5 — Rodando o programa (2:10 a 3:00)

👉 **FAZER antes de falar:** clique dentro do **terminal do VS Code** (parte de baixo). Se ele estiver pequeno, arraste a borda dele para cima até ocupar metade da tela.

🖥️ **TELA:** terminal do VS Code, limpo.

👉 **FAZER e FALAR, nesta ordem:**

1. Digite `python main.py` e aperte **Enter**.
   🎤 "Vamos rodar."
2. Aparece `Escolha o tipo [A/C/E]:`. Digite **X** e Enter. Aparece "Opção inválida".
   🎤 "Se eu digito uma opção que não existe, ele pergunta de novo."
3. Responda as perguntas assim, apertando Enter depois de cada uma:

   | Pergunta na tela | Digite |
   |---|---|
   | `Escolha o tipo [A/C/E]:` | **A** |
   | `Quantidade de quartos (1 a 2):` | **2** |
   | `Deseja vaga de garagem (R$ 300,00)? [S/N]:` | **S** |
   | `Possui crianças? [S/N]:` | **N** |
   | `Parcelas da taxa contratual de R$ 2.000,00 (1 a 5):` | **3** |

   🎤 Enquanto digita: "Agora: apartamento, dois quartos, com garagem, sem crianças, e a taxa em três vezes."
4. O orçamento aparece. Passe o mouse em cada linha enquanto fala:
   🎤 "Setecentos de base, mais duzentos do quarto e trezentos da garagem dá mil e duzentos; com o desconto de cinco por cento, o aluguel fica em mil cento e quarenta. Separada, vem a taxa: três parcelas, e a última fica um centavo menor para fechar os dois mil."

---

## TRECHO 6 — O CSV (3:00 a 3:20)

👉 **FAZER antes de falar:** na barra da esquerda do VS Code, clique com o botão direito em **`projecao_12_meses.csv`** → **Revelar no Explorador de Arquivos**. Na pasta que abrir, dê dois cliques no arquivo para abrir no **Excel**.

> Para não perder tempo no vídeo, você pode deixar essa pasta do Explorador já aberta na Parte 0 e só dar dois cliques no CSV aqui.

🖥️ **TELA:** Excel com as 12 linhas.

👉 **FAZER enquanto fala:** aponte os meses 1 a 3 e depois os meses 4 a 12.

🎤 **FALAR:**
> Este é o CSV gerado. Nos três primeiros meses o cliente paga o aluguel mais a parcela do contrato, e depois só o aluguel. No primeiro ano são quinze mil seiscentos e oitenta reais.

---

## TRECHO 7 — Testes e fechamento (3:20 a 3:50)

👉 **FAZER antes de falar:** **Alt + Tab** de volta ao **VS Code**. Clique no terminal, digite `cls` e Enter. Depois digite `python -m unittest -v` e Enter.

🖥️ **TELA:** terminal com os 6 testes e o `OK` no final.

🎤 **FALAR:**
> Os testes automáticos conferem cada regra, e todos passam. A orientação a objetos deixou cada regra num lugar só: a herança evita repetir código, e o orçamento funciona com qualquer imóvel sem saber qual é. Um tipo novo de imóvel é só uma classe nova. Obrigado!

👉 **FAZER:** espere 2 segundos e clique em **Parar Gravação** no OBS.

---

## Depois de gravar

1. Assista o vídeo e confira se tem menos de 4:00. Se passou, regrave cortando a frase "E o Estudio tem a regra do pacote de vagas." (trecho 3) e a frase "No primeiro ano são quinze mil seiscentos e oitenta reais." (trecho 6).
2. Suba no YouTube como **Não listado** e copie o link.
3. Mande o link para o Claude colocar na capa do PDF.
4. Entregue: o **PDF**, o **link do GitHub** e o **link do YouTube**.

## Se algo der errado
- **`python` não é reconhecido:** feche e abra o VS Code de novo; se continuar, use `py main.py`.
- **Erro de permissão ao gravar o CSV:** o Excel está com o arquivo aberto. Feche o Excel e rode de novo.
- **Errou uma fala:** pare, respire e repita só a frase. Se gravar em partes, o Claude junta e corta depois.
