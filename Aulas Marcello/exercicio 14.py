#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se 
#ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

print('Calculo Idade para votação')

print('Digite o ano atual')
ano_atual = int(input())

print('Digite o ano de nascimento')
ano_nascimento = int(input())

idade = (ano_atual - ano_nascimento)

if idade >= 16:
    print('A pessoa pode votar este ano!')
else:
    print('A pessoa não pode votar este ano!')
