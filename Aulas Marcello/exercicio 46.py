#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

print('Digite um valor entre 1 e 10')
tabuada = int(input())

for multiplicador in range(1, 11, 1):
    resultado = tabuada * multiplicador
    print('{} x {} = {}'.format(tabuada,multiplicador,resultado))



