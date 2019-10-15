#Ler as notas da 1ª e 2ª avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem 
# que diga se o aluno foi ou não aprovado (considerar que nota igual ou maior que 6 o aluno é aprovado). 
# Escrever também a média calculada.

print('Calculo media simpes')

print('Digite a nota da avaliacao 1')
avaliacao_1 = float(input())

print('Digite a nota da avaliacao 2')
avaliacao_2 = float(input())

media = ((avaliacao_1 + avaliacao_2) / 2)
print('A media do aluno é {:.2f}'.format(media))

if media >= 6:
    print('O aluno foi APROVADO')
else:
    print('O aluno foi REPROVADO')
