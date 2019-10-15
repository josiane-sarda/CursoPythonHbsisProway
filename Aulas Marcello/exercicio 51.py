#Escreva um algoritmo para ler 10 números. Todos os números lidos com valor inferior a 40 
#devem ser somados. Escreva o valor final da soma efetuada.

num = 0
soma = 0

for i in range(0, 10, 1):
    print('Digite o {}º numero'.format(i + 1))
    num = float(input())
    if num < 40:
       soma = soma + num

print('A soma de todos os numeros menores que 40 é: {:.2f}'.format(soma))
