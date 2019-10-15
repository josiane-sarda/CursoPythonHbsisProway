#- A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que 
# trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular 
# com um acréscimo de 50%. Escreva um algoritmo que leia o número de horas trabalhadas em 
# um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser 
# acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

print('Calculo Salario - hora extra')
print('Digite o numero de horas trabalhadas no mes')
total_hora_mes = int(input())

print('Digite o salario por hora')
salario_por_hora = int(input())

hora_extra = (total_hora_mes - 160)

salario_total = (salario_por_hora * 160) + (hora_extra * salario_por_hora * 1.5)

print('O salario total do funcionario é {}'.format(salario_total))




