#O mesmo exercício anterior, mas agora, considere que o segundo valor lido poderá 
#ser maior ou menor que o primeiro valor lido, ou seja, deve-se testá-los.

print('Digite o primeiro valor')
valor1 = int(input())
print('Digite o segundo valor')
valor2 = int(input())
soma = 0
while (valor2 <= valor1):
    print('Valor invalido. Digite um novo valor')
    valor2 = int(input())
    
for i in range(valor1, valor2 + 1, 1):    
    soma = soma + i

print('A soma dos inteiros é {}'.format(soma))

