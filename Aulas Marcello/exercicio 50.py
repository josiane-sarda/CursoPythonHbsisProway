#Escreva um algoritmo para ler 10 números e ao final da leitura escrever a soma total dos 10 números lidos.

num = 0
soma = 0

for i in range(0, 10, 1):
    print('Digite o {}º numero'.format(i + 1))
    num = float(input())
    soma = soma + num

print('A soma dos dez numeros é {:.2f}'.format(soma))
