#O mesmo exercício anterior, mas depois de ordenar os elementos do vetor em ordem crescente, 
# deve ser lido mais um número qualquer e inserir esse novo número na posição correta, 
# ou seja, mantendo a ordem crescente do vetor.

print('Ordenar lista')

numeros = []
for i in range(0, 10):
    print('Digite o {}º numero'.format(i + 1))
    numero = int(input())

    numeros.append(numero)

for i in range(0, 10):
    for j in range(i, 10):
        if numeros[j] < numeros[i]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print('Digite um numero')
num = int(input())

for i in range(0, 10):
    for j in range(i, 11):               #11 pq será adicionadao um numero a mais no vetor.
        if num <= numeros[i]:
            aux = numeros[i]
            numeros[i] = num
            num = aux

print(numeros)