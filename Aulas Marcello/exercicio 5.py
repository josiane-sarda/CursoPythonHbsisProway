#Escreva um algoritmo para ler o salario mensal atual de um funcionario e o percentual de reajuste.
#Calcular e escrever o valor do novo salario.

print('Calculo de reajuste salarial')
salario_atual = float(input('Qual o salario atual')) 
percentual_reajuste = float(input('Qual o percentual de reajuste'))

valor_aumento = salario_atual * percentual_reajuste / 100
novo_salario = salario_atual + valor_aumento
print('Salario atual: {} => Novo salario: {}'.format(salario_atual, novo_salario))
