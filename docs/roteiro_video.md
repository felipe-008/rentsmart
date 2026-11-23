# Roteiro do vídeo pitch (até 4 minutos)

Gravar a tela (Win + Alt + R na Xbox Game Bar, ou OBS). Publicar no YouTube como **Não listado**.

| Tempo | Tela | Fala (resumo) |
|---|---|---|
| 0:00–0:25 | README no GitHub | "A R.M Imóveis calcula orçamentos de locação à mão, o que é lento e gera erro. O RentSmart aplica as regras sozinho, mostra como o valor foi formado e gera a projeção de 12 meses em CSV." |
| 0:25–0:55 | Fluxograma (PDF, página 3) | Ler e validar o tipo; estúdio vai para o estacionamento; casa/apartamento leem quartos e garagem; apartamento pergunta por crianças; depois parcelas, cálculo, resumo e CSV. Toda entrada inválida repete a pergunta. |
| 0:55–1:40 | `rentsmart/imoveis.py` | `Imovel` é abstrata: base + adicionais − desconto num só método (`itens`). `ImovelComGaragem` junta a regra comum de casa e apartamento. `Apartamento` só sobrescreve o desconto de 5%. `Casa` não tem nenhum método, só valores. `Estudio` tem o pacote de vagas. |
| 1:40–2:05 | `rentsmart/orcamento.py` | `Contrato` cuida da taxa de R$ 2.000 e das parcelas (a última ajusta os centavos). `Orcamento` recebe imóvel e contrato, monta o resumo, a projeção e o CSV. Aluguel e taxa nunca se misturam. |
| 2:05–3:00 | Terminal: `python main.py` | Digitar uma opção inválida (ex.: X) para mostrar a validação. Depois: Apartamento, 2 quartos, garagem S, crianças N, 3 parcelas. Mostrar o resumo: 700 + 200 + 300 − 60 = R$ 1.140,00; taxa 3x de 666,67 com ajuste para 666,66. |
| 3:00–3:25 | `projecao_12_meses.csv` aberto no Excel | Meses 1 a 3 com a parcela do contrato; 4 a 12 só o aluguel. |
| 3:25–3:55 | `test_rentsmart.py` + `python -m unittest -v` | "Usar orientação a objetos deixou cada regra num lugar só: herança evita repetir a regra de casa e apartamento, polimorfismo deixa o orçamento funcionar para qualquer imóvel, e um novo tipo entra sem mexer no resto. Os testes confirmam os valores." |
