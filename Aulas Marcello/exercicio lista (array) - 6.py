#Faça um algoritmo para ler 20 números e armazenar em um vetor. Após a leitura total dos 20 números, 
# o algoritmo deve escrever esses 20 números lidos na ordem inversa.

print('Números na ordem inversa')

numeros = []
for i in range(0, 5, 1):
    print('Digite o {}º número'.format(i + 1))
    num = int(input())

    numeros.append(num)

for i in range(4, -1, -1):
    print(numeros[i])