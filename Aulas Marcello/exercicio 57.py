#Faça um algoritmo para ler o código e o preço de 15 produtos, calcular e escrever: 
#o maior preço lido.
#a média aritmética dos preços dos produtos.


print('Codigo e preco de 15 produtos')

preco_total = 0
maior_valor = 0


for i in range(0, 15,1):
    print('Digite o codigo do {}º produto'.format(i+1))
    codigo = int(input())
    print('Digite o preco do {}º produto'.format(i+1))
    preco = float(input())
    if preco > maior_valor:
        maior_valor = preco

    preco_total = preco_total + preco

media_dos_precos = preco_total / 15

print('A media dos precos dos produtos é {} reais'.format(media_dos_precos))
print('O maior valor é {}'.format(maior_valor))





