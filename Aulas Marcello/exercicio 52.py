#Ler 2 valores, calcular e escrever a soma dos inteiros existentes entre os 2 valores lidos 
# (incluindo os valores lidos na soma). Considere que o segundo valor lido será sempre 
# maior que o primeiro valor lido.

print('Digite o primeiro valor')
valor1 = int(input())
print('Digite o segundo valor')
valor2 = int(input())
soma = 0
if (valor2 <= valor1):
    print('Valor invalido. Digite um novo valor')
    valor2 = int(input())
    
for i in range(valor1, valor2 + 1, 1):    
    soma = soma + i

print('A soma dos inteiros é {}'.format(soma))

