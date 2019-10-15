#Ler 10 valores, calcular e escrever a média aritmética desses valores lidos.

soma_numeros = 0
qtd_num_digitados = 0

while qtd_num_digitados < 10:
    print('Digite o {}º numero'.format(qtd_num_digitados + 1))
    num = float(input())
    soma_numeros = soma_numeros + num

    qtd_num_digitados = qtd_num_digitados + 1

media = soma_numeros / 10
print('Média: {:.2f}'.format(media))