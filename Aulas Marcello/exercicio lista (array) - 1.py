#Escreva um algoritmo que permita a leitura dos nomes de 10 pessoas e armazene 
# os nomes lidos em um vetor. Após isto, o algoritmo deve permitir a 
# leitura de mais 1 nome qualquer de pessoa e depois escrever a mensagem ACHEI, 
# se o nome estiver entre os 10 nomes lidos anteriormente (guardados no vetor), ou NÃO ACHEI caso contrário.

print('Patota pasa a bola tito')
print('quem vai?')
print('precisa de 10 negada')

jogadores = []
for i in range(0, 10):
    print('jogador {}'.format(i + 1))
    jogadores.append(input())

print('Digite o nome que deseja verificar se vai na patota')
nome = input()

confirmacao = 'MOIO'
for i in range(0, 10):
    if jogadores [i] == nome:
        confirmacao = 'VAI IR'

print(confirmacao)