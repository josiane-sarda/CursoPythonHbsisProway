#Modifique o exercício anterior para aceitar somente valores maiores que 0 para N. 
# Caso o valor informado (para N) não seja maior que 0, deverá ser lido um novo valor para N.

print('Digite um valor N')
valor_n = int(input())

while (valor_n <= 0):
    print('Valor invalido. Digite um novo valor')
    valor_n = int(input())

for i in range(1, valor_n ):
    print(i)
