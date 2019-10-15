#Escreva um algoritmo para ler uma temperatura em graus Fahrenheit, calcular e escrever o
#valor correspondente em graus Celsius

print('Calculo para transformar Fahrenheit para Celsius')
temperatura_F = float(input('Qual a temperatura em Fahrenheit'))

temperatura_C = (((temperatura_F - 32)*5) / 9)

print('A temperatura em graus Celsius eh: {} '.format(temperatura_C))
