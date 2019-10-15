#Faça um algoritmo que leia três notas de um aluno, calcule e escreva a média final deste
#aluno. Considerar que a média é ponderada e que o peso das notas é 2, 3 e 5. Fórmula para o
#cálculo da média final é:

print('Calculo para media ponderada')
n1 = float(input('Digite a nota 1 '))
n2 = float(input('Digite a nota 2' ))
n3 = float(input('Digite a nota 3 '))

media_final = (((n1 * 2) + (n2 * 3) + (n3 * 5))/10)
print('A media final é: {} '.format(media_final))
