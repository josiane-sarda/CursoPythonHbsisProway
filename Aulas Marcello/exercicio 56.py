##Uma loja está levantando o valor total de todas as mercadorias em estoque. 
# Escreva um algoritmo que permita a entrada das seguintes informações: 
#a)	o número total de mercadorias no estoque; 
#b)	o valor de cada mercadoria. 
#Ao final imprimir o valor total em estoque e a média de valor das mercadorias.

print('Levantamento de estoque')
print('Digite a quantidade de mercadorias em estoque')
qtd_mercadoria = int(input())

valor_total_mercadorias = 0
for i in range(qtd_mercadoria):
    print('Digite o valor da {}ª mercadoria'.format(i+1))
    valor = float(input())

    valor_total_mercadorias = valor_total_mercadorias + valor

media_mercadorias = media_mercadorias = valor_total_mercadorias / qtd_mercadoria

print('Valor total em estoque: {}'. format(valor_total_mercadorias))
print('Valor medio do estoque: {}'. format(media_mercadorias))




