#Escreva um algoritmo para ler o numero total de eleitores de um municipio, o numero de votos brancos, nulos e validos. 
#Calcular e escrever o percentual que cada um representa em relacao ao total de eleitores. 

print('Calculo de saldo de eleicao')
print('Qual o numero total de eleitores:::')
eleitores = int(input())
print('Qual o numero de votos brancos:::')
brancos = int(input())
print('Qual o numero de votos nulos:::')
nulos = int(input())
print('Qual o numero de votos validos:::')
validos = int(input())

perc_brancos = brancos / eleitores * 100
perc_nulos = nulos / eleitores * 100
perc_validos = validos / eleitores * 100

print('% Brancos: {:.2f}\n% Nulos: {:.2f}\n% Validos: {:.2f}'
.format(perc_brancos, perc_nulos, perc_validos))
