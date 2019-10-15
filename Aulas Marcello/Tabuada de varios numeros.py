
print('Tabuada de varios numeros')
print('Qual a quantidade de tabuadas')
qtd_tabuadas = int(input())
print('Quantas multiplicacoes por tabuada')
qtd_multiplicacoes= int(input())


for tabuada in range(1, qtd_tabuadas + 1, 1):
    # tabuada [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Tabuada do {}'.format(tabuada))
    print('')
    for produto in range(1, qtd_multiplicacoes + 1):
            # produto[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            resultado = tabuada * produto
            print('{} x {} = {}'.format(tabuada, produto, resultado))
    print('')

print('Fim')
            
  