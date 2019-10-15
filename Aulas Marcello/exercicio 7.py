#Uma revendedora de carros usados paga a seus funcionários vendedores um salário fixo por
#mês, mais uma comissão também fixa para cada carro vendido e mais 5% do valor das vendas
#por ele efetuadas. Escrever um algoritmo que leia o número de carros por ele vendidos, o valor
#total de suas vendas, o salário fixo e o valor que ele recebe por carro vendido. Calcule e
#escreva o salário final do vendedor.

print('Calculo do salario final de um vendedor')
carros_vendidos = int(input('Quantos carros o vendedor vendeu')) 
valor_total_vendas = float(input('Qual o valor total das vendas'))
salario_fixo = float(input('Qual o valor do salario fixo'))
comissao_fixa = float(input('Qual o valor da comissao fixa'))

salario_final = (salario_fixo + (carros_vendidos * comissao_fixa) + (valor_total_vendas * 0.05) )
print('O salario final do vendedor eh: {:.2f} '.format(salario_final))
