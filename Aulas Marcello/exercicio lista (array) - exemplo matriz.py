
#produtos = ['Omo',  'Ariel',  'Brilhante']
#preco    = [   50,       12,         37  ]
#desconto = [   5,        2,          3   ]

#desc = preco[2] * desconto[1] / 100
#print(desc)


#notas = [
#    [7.0, 5.0, 9.0], João
#    [6.3, 5.0, 8.0], Maria
#    [8.0, 8.5, 9.2]  Ana
# ] 
# print(notas[0][2])     
# 
#                                                                                                
#notas_joao = [7.0, 5.0, 9.0, 8.0 7.2, 5.6]
#for i in range(0, len(notas_joao))
#   print(notas_joao[i])


#notas = [
#    [7.0, 5.0, 9.0], João
#    [6.3, 5.0, 8.0], Maria
#    [8.0, 8.5, 9.2]  Ana
# ]
#
#for i in range(0, len(notas)):                       (percorre a linha)
#   for j in range(0, len(notas[0])):                 (percorre todas as coluna de cada linha)
#       print( '{} '.format(notas[i][j]), end='')      (end=''  - faz com que todas as coluna da linha sejam 
#print('')   #serve para pular uma linha a cada         impressas na mesma linha, não vai quebrando.)
#                #linha da matriz impressa
#
#
#Para digitar varias notas por aluno, cria-se uma lista:

#notas = []                   #cria uma lista vazia de notas, para ir colocando as listas de notas digitadas no for.
#qtd_alunos = int(input('Quantidade de alunos: '))
#qtd_notas_aluno = int(input('Quantidade de notas por aluno: '))
#
#for i in range(0, qtd_alunos):
#   notas_aluno = []           #para i ate qtd_alunos(digitada), vai guardar os alunos e as notas digitadas nesta  
#   notas.append(notas_aluno)    linha provisoria, para deipois jogar na linha principal: notas = [].
#   for j in range(0, qtd_notas_aluno)
#       nota = float(input('Digite a {}ª do aluno {}º'.format(j, i)))
#       notas_aluno.append(nota)
#
#