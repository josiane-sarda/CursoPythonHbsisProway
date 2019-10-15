#O mesmo exercicio anterior, mas agora deve escrever o menor elemento de vetor 
#e a respectiva posição #dele neste vetor.

print('Maior valor e sua posição')

numeros = []
menor_num = 1000000
posicao = 0

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
menor_num
for i in range(0, 5):
    if numeros [i] < menor_num:
        menor_num = numeros [i]
        posicao = i
    
    print(menor_num)
    print(posicao)
          
print('O valor do menor elemento é {} e esta na posicao {}'.format(menor_num, posicao))

print('Fim')
