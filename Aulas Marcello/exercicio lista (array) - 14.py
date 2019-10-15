#Faça um algoritmo para ler 50 números e armazenar em um vetor VET, 
#verificar e escrever se existem números repetidos no vetor VET e em que posições se encontram.

numeros = []
qtd_numeros = 4 
for i in range(0, qtd_numeros):
    print('Digite o {}ª número'.format(i+1))
    num = int(input())
    numeros.append(num)

numeros_repetidos = []
for i in range(0, qtd_numeros - 1):
    for j in range(i + 1, qtd_numeros):
        if numeros[i] == numeros[j]:           #se o numero da posicao i for igual ao numero da posicao j

            nao_existe = True                    #verificar se este numero ainda não esta adicionado no vetor
            for k in range(0, len(numeros_repetidos)):  
                if numeros[i] == numeros_repetidos[k]:   #se o numero da posicao i for igual a algum numero k (q esta sendo verificado)
                    nao_existe = False                      #a informacao nao_existe sera falsa
            if nao_existe:                                 #se não, jogar esse numero nos numeros_repetidos
                numeros_repetidos.append(numeros[i])

for i in range(0, len(numeros_repetidos)):
    print("O número {} aparece nas seguintes posições".format(numeros_repetidos[i]))
    for j in range(0, len(numeros)):
        if numeros_repetidos[i] == numeros[j]:     #se o numero na posicao i for igual ao numero da posicao j
            print(j)