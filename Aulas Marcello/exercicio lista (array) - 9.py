#Faca um algoritmo para ler 10 numeros e armazenar em um vetor. Após isso, o algoritimo deve 
#ordenar os numeros no vetor na ordem crescente. Escrever o vetor ordensdo.

print('Ordenar lista')

numeros = []
for i in range(0, 10):
    print('Digite o {}º numero'.format(i + 1))
    numero = int(input())

    numeros.append(numero)

for i in range(0, 10):
    for j in range(i + 1, 10):
        if numeros[j] < numeros[i]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

for i in range(0, 10):
    print(numeros[i])