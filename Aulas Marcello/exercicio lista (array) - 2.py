#Escreva um algoritmo que permita a leitura das notas de uma turma de 20 alunos. 
# Calcular a média da turma e contar quantos alunos obtiveram nota acima desta média calculada. 
# Escrever a média da turma e o resultado da contagem.

print('Média 20 notas')

notas = []
soma = 0
nota_maior = 0

for i in range(0, 20):
    print('Nota do {}º aluno'.format(i + 1))
    notas.append(float(input()))
    soma = soma + notas[i]

media = soma / 4

for i in range(0, 20):               # O que foi feito nesta linha, faz com que se passe em cada uma das 20 posições
    if notas [i] > media:                 # fazendo a validação do if. Se for maior vai contabilizar, caso contrario, 
        nota_maior = nota_maior + 1           #passsa reto e faz o lup novamente.

print('A media da turma é {}'.format(media))
print('Neste caso, {} alunos obtiveram nota acima da media'.format(nota_maior))

