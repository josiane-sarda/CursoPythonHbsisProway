
print('Média geral dos alunos')
print('Qual a quantidade de alunos?')
qtd_alunos = int(input())
print('Quantas notas por aluno?')
qtd_notas = int(input())

soma_notas = 0
for aluno in range(0, qtd_alunos):
    # aluno [0, 1, 2]
    for nota in range(0, qtd_notas):
            # nota [0, 1]
            print('Aluno {} => Nota {}'.format(aluno, nota))
            soma_notas = soma_notas + float(input())

media = soma_notas / (qtd_alunos * qtd_notas)
print('Média feral = {}'.format(media))