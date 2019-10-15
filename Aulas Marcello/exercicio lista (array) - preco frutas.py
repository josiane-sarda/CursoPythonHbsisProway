# Almir vende frutas na sua barraca na feira
# e com o sucesso do ultimo ano ele planeja criar
# preços diferentes para alta e baixa temporada.
# A sua ideia é que cada fruta tenha 2 preços: alta temporada e baixa temporada
# Crie um algoritmo que permita a Almir cadastras os preços de cada uma
# das sua frutas e em seguida imprima a listagem de preços cadastrada por ele.
# Considere que Almir vende 3 frutas em sua barraca: Laranja, Goiaba e Banana.

# [
#   [ 3.0, 2.0 ]
#   [ 4.5, 3.2 ]
#   [ 1.8, 1.5 ]
# ]

nomes_frutas = []
precos_frutas = []
qtd_frutas = int(input('Quantidade de frutas: '))
qtd_precos_fruta = int(input('Quantidade de preços por frutas: '))

for i in range(0, qtd_frutas):
    nome = input('Digite o nome da {}ª fruta: '.format(i + 1))
    nomes_frutas.append(nome)

for i in range(0, qtd_frutas):
    precos_fruta = []
    precos_frutas.append(precos_fruta)

    preco_alta = float(input('Digite o preco da {} na alta: '.format(nomes_frutas[i])))
    precos_fruta.append(preco_alta)
    preco_baixa = float(input('Digite o preco da {} na baixa: '.format(nomes_frutas[i])))
    precos_fruta.append(preco_baixa)

for i in range(0, qtd_frutas):
    print("Preço da {}".format(nomes_frutas[i]))
    # o eh alta temporada
    print("Preço na alta {}".format(nomes_frutas[i][0]))
    # o eh baixa temporada
    print("Preço na baixa {}".format(nomes_frutas[i][1]))
    