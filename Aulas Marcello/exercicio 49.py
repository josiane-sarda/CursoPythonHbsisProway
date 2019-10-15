#Ler o número de alunos existentes em uma turma e, após isto, ler as notas destes alunos, 
# calcular e escrever a média aritmética dessas notas lidas.

print('Dgite quantos alunos tem na turma')
qtd_alunos = int(input())

nota = 0
soma = 0

for i in range(0, qtd_alunos):
    print('Digite a nota do {}º aluno '.format(i + 1))
    nota = float(input())
    soma = soma + nota

media = soma / qtd_alunos
print('A media das notas dos aluno é {:.2f}'.format(media))
