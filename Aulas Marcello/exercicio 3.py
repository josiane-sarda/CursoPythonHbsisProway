#Faca um algoritmo que leia a idade de uma pessoa expressa em anos, meses e dias e esceva a idade dessa pessoa
#expressa apenas em dias. Considderar ano com 365 dias e mes com 30 dias.

print('Digite quantos anos voce tem')
anos = int(input())

print('Digite o saldo de meses da sua idade')
meses = int(input())

print('Digite o saldo de dias da sua idade')
dias = int(input())

idade = ((anos*365) + (meses*30) + dias) 
print('A sua idade é {}'.format(idade))