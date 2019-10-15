#A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes. 
# Faça um algoritmo para coletar dados sobre o salário e número de filhos de 
# cada habitante e após as leituras, escrever: 
#a)	Média de salário da população 
#b)	Média do número de filhos 
#c)	Maior salário dos habitantes 
#d)	Percentual de pessoas com salário menor que R$ 150,00 
#Obs.: O final da leitura dos dados se dará com a entrada de um “salário negativo”.

print('Quantas pessoas participaram da pesquisa?')
participantes = int(input())

salario = 0
filhos = 0
maior_salario = 0
salario_total = 0
qtd_filhos = 0
menor_salario = 0

for i in range(0, participantes, 1):
    print('Digite o salario do {}º participante'.format(i + 1 ))
    salario = float(input())
    if salario > maior_salario: 
        maior_salario = salario
    if salario < 150:
        menor_salario = menor_salario + 1

    print('Digite o numero de filhos do {}º participante'.format(i + 1 ))
    filhos = int(input())

    salario_total = salario_total + salario
    qtd_filhos = qtd_filhos + filhos

media_salarial = salario_total / participantes
media_filhos = qtd_filhos / participantes
salario_menor_150 = (menor_salario * 100) / participantes


print('A média salarial dos habitantes é {:.2f} reais'.format(media_salarial))
print('A média do numeros de filhos dos habitantes é {}'.format(media_filhos))
print('O maior valor é {}'.format(maior_salario))
print('O percentual de habitantes que recebe menos que 150,00 é {:.1f}'.format(salario_menor_150))

