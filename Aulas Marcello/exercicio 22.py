#Faça um algoritmo para ler: quantidade atual em estoque, quantidade máxima em estoque e quantidade 
# mínima em estoque de um produto. Calcular e escrever a quantidade 
# média ((quantidade média = quantidade máxima + quantidade mínima)/2). 
# Se a quantidade em estoque for maior ou igual a quantidade média escrever a mensagem 'Não efetuar compra', 
# senão escrever a mensagem 'Efetuar compra'.

print('Digite a quantidade atual em estoque')
quantidade_atual_estoque = int(input())

print('Digite a quantidade maxima')
quantidade_maxima = int(input())

print('Digite a quantidade minima')
quantidade_minima = int(input())

quantidade_media = ((quantidade_maxima + quantidade_minima) / 2)
print('A quantidade media é {}'.format(quantidade_media))

if (quantidade_atual_estoque >= quantidade_media):
    print('Não efetuar compra')
else:
    print('Efetuar compra')

