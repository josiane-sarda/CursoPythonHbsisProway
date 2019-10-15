#Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um 
# novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero e imprimir o resultado 
# da divisão do primeiro valor lido pelo segundo valor lido. (utilizar a estrutura WHILE).

print('digite o valor de n1')
n1 = int(input())
print('digite o valor de n2')
n2 = int(input())

while n2 == 0:
    print('n2 não pode ser zero, forneca um novo valor')
    n2 = int(input())

    resultado = n1 / n2
    print('n1 / n2 = {}'.format(resultado))