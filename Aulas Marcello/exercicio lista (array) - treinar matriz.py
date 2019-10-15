#Almir vende frutas na sua barraca na feira e com sucesso do ultimo ano ele planeja criar precos diferentes
#para alta e baixa temporada. A sua ideia é que cada fruta tenha dois precos: alta temorada e baixa temporada.
#Crie um allgritmo que permita a Almir cadastrar os precos de cada uma das frutas e em seguida imprima a listagem 
#de precos cadastrada por ele. Considere que Almir vende 3 frutas em sua barraca: laranja, goiabae banana.

print('Preco fruta alta e baixa temporada')

preco_alta_baix_temp = []  #nao é possivel fazer preco e nome da fruta na mesma matriz

for i in range(0, 2):
    nome_frutas = []
    preco_frutas = []
    preco_alta_baix_temp.append(nome_frutas)
    preco_alta_baix_temp.append(preco_frutas)
    for j in range(0, 3):
        nome = (input('Digite o nome da {}ª fruta '.format(j)))
        nome_frutas.append(nome)
        preco = float(input('Digite o preco da {}ª fruta R$ '.format(j)))
        preco_frutas.append(preco)

for i in range(0, len(preco_alta_baix_temp)):
    print(preco_alta_baix_temp[i][0])
    for j in range(1, len(preco_alta_baix_temp[0])):
        print( '{} '.format( preco_alta_baix_temp[i][j]))  
print('')

