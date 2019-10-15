#- Ler 3 valores (considere que não serão informados valores iguais) e escrevê-los em ordem crescente.

print('Calculo ordenar 3 valores')
print('Digite um valor')
valor_1 = float(input())

print('Digite outro valor')
valor_2 = float(input())

print('Digite outro valor')
valor_3 = float(input())

if valor_1 < valor_2 and valor_1 < valor_3 and valor_2 < valor_3:
    print('Ordem: {},{}, {}'.format(valor_1, valor_2, valor_3))
else: 
    if valor_1 < valor_2 and valor_1 < valor_3 and valor_3 < valor_2:
        print('Ordem: {},{}, {}'.format(valor_1, valor_2, valor_2))
    else:
        if valor_2 < valor_1 and valor_2 < valor_3 and valor_1 < valor_3:
            print('Ordem: {},{}, {}'.format(valor_2, valor_1, valor_3))
        else:
            if valor_3 < valor_1 and valor_3 < valor_2 and valor_1 < valor_2:
                print('Ordem: {},{}, {}'.format(valor_3, valor_1, valor_2))
            else:
                if valor_2 < valor_3 and valor_2 < valor_1 and valor_3 < valor_1:
                    print('Ordem: {},{}, {}'.format(valor_2, valor_3, valor_1))
                else:
                    if valor_3 < valor_2 and valor_3 < valor_1 and valor_2 < valor_1:
                        print('Ordem: {},{}, {}'.format(valor_3, valor_2, valor_1))

