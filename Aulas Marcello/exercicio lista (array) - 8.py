#Faca um algoritmo para ler e armazenar em um vetor a temperatura média de todos os dias do ano. Calcular e escrever:
#menor temperatura do ano
#maior temperatura do ano
#temperatura media anual
#o numero de dias no ano em que a temperatura foi inferior a media anual

print('Análise tempo semanal')

temperauras = []
for i in range(0 + 1, 7):
    print('Digite a temperatura do {}º dia'.format(i))
    temp = float(input())

    temperauras.append(temp)

menor_temperatura = 999999
maior_temperatura = 0
soma_temperatura = 0

for i in range(0 + 1, len(temperauras)):
    if temperauras[i] < menor_temperatura:         #Se essa temperatura da posicao i for menor q a menor temperatura
        menor_temperatura = temperauras[i]           #a minha menor temperatura vai ser esta temperatura da posicao i
    if temperauras[i] > maior_temperatura:
        maior_temperatura = temperauras[i]
    soma_temperatura += temperauras[i]

media_temperatura = soma_temperatura / len(temperauras)
qtd_dias_abaixo_media = 0
for i in range(0 + 1, len(temperauras)):
    if temperauras[i] < media_temperatura:
        qtd_dias_abaixo_media += 1


print('A menor temperatura do ano foi {}° '.format(menor_temperatura))
print('A maior temperatura do ano foi {}° '.format(maior_temperatura))
print('A temperatura média anual foi de {:.2f}°'.format(media_temperatura))
print('Quantidade de dias abaixo da media: {} '.format(qtd_dias_abaixo_media))





