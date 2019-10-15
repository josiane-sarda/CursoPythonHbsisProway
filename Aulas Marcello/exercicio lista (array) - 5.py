#Ler um vetor A de 10 numeros. Após, ler mais um número e guardar em uma variável X.
#Armazenar em um vetor M o resultado de cada elemento de A multiplicando pelo valor X.
#Logo após, imprimir o vetor M.

vetorA = []
variavel_x = 0
vetorM = []
produtos = 0

for i in range(0, 10):
    print('Digite o {}º valor'.format(i + 1))
    valores = (int(input()))
    vetorA.append(valores)

print('Digite um numero')
variavel_x = int(input())

for i in range(0, 10):
    produtos = ((i + 1) * variavel_x)
    vetorM.append(produtos)

print('O vetor M é: {}'.format(vetorM))

    
