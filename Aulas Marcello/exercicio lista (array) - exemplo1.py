
print('Bem vindo ao controle de estoque')

print('Inserir um novo item? S - Sim, N - Não ')
inserir_item = input()


itens_nome = []
itens_preco = []
while(inserir_item == 'S'):
    print('Nome do item?')
    nome = input()
    print('Preco do item')
    preco = float(input())

    itens_nome.append(nome)
    itens_preco.append(preco)

    print('Inserir um novo item? S - Sim, N - Não')

#append - guarda os itens digitados na lista determinada
#len - quantidade de itens contidos na lista
#
# n[i] < n[i + 1]
# aux = n[i]
# n[i] = n[i+1]
# n[i+1] = aux