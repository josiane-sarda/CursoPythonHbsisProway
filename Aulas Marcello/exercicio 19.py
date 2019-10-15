#Tendo como dados de entrada o nome, a altura e o sexo (M ou F) de uma pessoa, calcule e mostre 
# seu peso ideal, utilizando as seguintes fórmulas: 
#para sexo masculino: peso ideal = (72.7 * altura) - 58
#para sexo feminino: peso ideal = (62.1 * altura) - 44.7

print('digite seu nome')
nome = str(input())

print('digite sua altura')
altura = float(input())

print('digite o genero: M ou F')
genero = str(input()) 

if genero == 'M':
    peso_ideal = ((72.7 * altura) - 58)
    print('seu peso ideal é {}'.format(peso_ideal))
else:
    peso_ideal = ((62.1 * altura) - 44.7)
    print('seu peso ideal é {}'.format(peso_ideal))

