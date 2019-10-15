#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem
#do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual do
#distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de
#fábrica de um carro, calcular e escrever o custo final ao consumidor.

print('Calculo do custo final de um carro')
custo_fabrica = float(input('Qual o custo de fabria do carro')) 
custo_final = (custo_fabrica + (custo_fabrica * 28 + custo_fabrica * 45) / 100)

print('Custo final ao consumidor: {} '.format(custo_final))
