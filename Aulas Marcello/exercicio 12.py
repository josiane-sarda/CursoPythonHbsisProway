#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se 
# forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, 
# calcule e escreva o custo total da compra.

print('Calculo compra de macas')

print('Digite a quantidade de macas compradas')
quantidade_macas = int(input())

if quantidade_macas >= 12:
    custo_da_compra = (quantidade_macas * 1.00)
    print('O custo total da compra é {:.2f}'.format(custo_da_compra))
else:
    custo_da_compra = (quantidade_macas * 1.30)
    print('O custo total da compra é {:.2f}'.format(custo_da_compra))
print('Obrigada!')

