#Ler o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa. 
# Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00 
# mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.

print('Digite o salario fixo do vendedor')
salario_fixo = float(input())

print('Digite o valor das vendas efetudas pelo vendedor')
vendas_efetuadas = float(input())

vendas_a_mais = (vendas_efetuadas - 1500)

if (vendas_efetuadas <= 1500):
    salario_total = (salario_fixo + vendas_efetuadas * 0.03)
    print('o salario total é {}'.format(salario_total))
else:
    salario_total = (salario_fixo + vendas_efetuadas * 0.03 + vendas_a_mais * 0.05)
    print('o salario total é {}'.format(salario_total))