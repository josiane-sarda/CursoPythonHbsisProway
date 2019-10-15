
print('Média aritmética entre numeros no intervalo')
print('Digite o numero de inicio')
inicio = int(input())
print('Digite o numero de fim')
fim = int(input())

acumulador = 0
for i in range(inicio, fim + 1, 1):
    acumulador = acumulador + 1

media = acumulador / (fim - inicio)
print('A media aritmetica é {}'.format(media))



