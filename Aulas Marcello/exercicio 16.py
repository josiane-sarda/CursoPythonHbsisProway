#Ler dois valores (considere que não serão lidos valores iguais) e escrevê-los em ordem crescente.

print('Valores em ordem crescente')

print('Digite o valor 1')
valor_1 = int(input())

print('Digite o valor 2')
valor_2 = int(input())

if valor_1 > valor_2:
    print('Ordem crescente: {} , {}'.format(valor_2, valor_1))
else:
    print('Ordem crescente: {} , {}'.format(valor_1, valor_2))
    
