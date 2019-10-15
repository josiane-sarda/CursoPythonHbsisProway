#Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', 
# senão escrever a mensagem 'Saldo Negativo'.

print('Digite o numero da conta do cliente')
conta = int(input())

print('Digite o saldo')
saldo = float(input())

print('Digite o valor de debito')
debito = float(input())

print('Digite o valor de credito')
credito = float(input())

saldo_atual = (saldo - debito + credito)
print('Saldo atual {}'.format(saldo_atual))

if (saldo_atual >= 0):
    print('Saldo positivo')
else:
    print('Saldo negativo')

