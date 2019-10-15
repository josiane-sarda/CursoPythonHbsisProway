#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

print('Calculo valor maior')

print('Digite o valor 1')
valor_1 = int(input())

print('Digite o valor 2')
valor_2 = int(input())

if valor_1 > valor_2:
    print('O valor {} é maior'.format(valor_1))
else:
    print('O valor {} é maior'.format(valor_2))
