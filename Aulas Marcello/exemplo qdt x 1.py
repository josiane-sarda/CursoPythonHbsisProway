#Peca ao usuario para digitar 5 numeros entre 1 e 3 
#Ao final, informe quantas vezes o 1 foi digitado,
#quantas vezes o 2 foi digitado, e quantas vezes 
#o 3 foi digitado.

print('Qtd numero digitado')
print('Digite números entre 1 e 3')

qtd_x_1 = 0
qtd_x_2 = 0
qtd_x_3 = 0

for num_atual in range(0,5, 1):
    print('Digite o {}º número'.format(num_atual+1))
    num = int(input())

    while num < 1 or num > 3:
        print('número invalido, digite um numero entre 1 e 3')
        num = int(input())
    
    if num == 1:
        qtd_x_1 + 1
    if num == 2:
        qtd_x_2 + 1
    if num == 3:
        qtd_x_3 + 1

print('Qtd 1: {} \nQtd 2: {} \nQtd 3:{}'.format(qtd_x_1, qtd_x_2, qtd_x_3))