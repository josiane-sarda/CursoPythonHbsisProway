#Faça um algoritmo que calcule e escreva a média aritmética dos números inteiros 
# entre 15 (inclusive) e 100 (inclusive).

soma = 0
divisor = (101 - 15)

for i in range(15,101,1):
    soma = soma + i 

media = (soma / divisor)
print('A media dos numeros inteiros do intervalo é {}'.format(media))


