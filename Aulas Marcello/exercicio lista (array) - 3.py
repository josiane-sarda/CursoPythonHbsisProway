#Ler um vetor Q de 20 posições (aceitar somente números positivos). 
# Escrever a seguir o valor do maior elemento de Q e a respectiva posição que ele ocupa no vetor.

print('Maior valor e sua posição')

numeros = []
maior_num = 0


for i in range(0, 5):
    print('Digite o {}º valor'.format(i + 1))
    valores = (int(input()))
    if valores >= 0:
        numeros.append(valores)
    else:
        while valores < 0:
            print('Valor invalido. Digite um valor positivo.')
            valores = (int(input()))
        numeros.append(valores)
maior_num
for i in range(0, 5):
    if numeros [i] > maior_num:
        maior_num = numeros [i]
        posicao = i
    
    print(maior_num)
    print(posicao)
        
print('O valor do maior elemento é {} e esta na posicao {}'.format(maior_num, posicao))

print('Fim')
