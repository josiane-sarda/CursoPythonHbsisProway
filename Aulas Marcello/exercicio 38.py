#Escreva um algoritmo para ler as notas da 1a. e 2a. avaliações de um aluno, 
# calcule e imprima a média (simples) desse aluno. Só devem ser aceitos valores 
# válidos durante a leitura (0 a 10) para cada nota.

print('Calculdora de média simples')
print('Digite a not 1')
n1 = float(input())
print('Digite a nota 2')
n2 = float(input())

while n1 < 0 or n1 > 10:
    print('Nota 1 invalida, digite um valor entre 0 e 10')
    n1 = float(input())

while n2 < 0 or n2 > 10:
    print('Nota 2 inválida, digite um valor entre 0 e 10')
    n2 = float(input())

media = (n1 + n2) / 2

print('Média: {:.2f}'.format(media))