#Ler 10 valores e escrever quantos desses valores lidos estão no intervalo [10,20] 
#(incluindo os valores 10 e 20 no intervalo) e quantos deles estão fora deste intervalo.

dentro_intervalo = 0
fora_intervalo = 0
valor = 0

for i in range(10):

    valor = float(input('Escreva o {}º valor:'.format(i + 1)))

    if (valor >= 10) and (valor <= 20):
        dentro_intervalo = dentro_intervalo + 1
    else:
        fora_intervalo = fora_intervalo + 1

print('{} numeros estao no intervalo [10,20]'.format(dentro_intervalo))
print('{} numeros estao nao no intervalo [10,20]'.format(fora_intervalo))





