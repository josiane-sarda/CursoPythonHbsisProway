#Escreva um algoritmo para calcular a media
# n numeros informados pelo usuario

print('Calcladora de média simples')
print('Qual a qtd de números que deseja calcular a média')
qtd_numeros = int(input())

soma_numeros = 0
qtd_num_digitados = 0
while qtd_num_digitados < qtd_numeros:
    print('Digite o {}º numero'.format(qtd_num_digitados + 1))
    num = float(input())
    soma_numeros = soma_numeros + num

    qtd_num_digitados = qtd_num_digitados + 1

media = soma_numeros / qtd_numeros
print('Média: {:.2f}'.format(media())


#USANDO O FOR 

#soma_numeros = 0
#for i in range(0, qtd_numeros):
    #print('Digite o {}º numero'.format(i + 1))
    #num = flot(input())
    #soma_numeros / qtd_numeros + num

#media = soma_numeros / qtd_numeros
#print('Média: {.:2f}'.format(media))

### Nesse caso é melhor fazer por for, pois sabe-se quantas vezes vai repetir.
