#Faça um algoritmo para ler um vetor de 20 números. Após isto, deverá ser lido mais um 
# número qualquer e verificar se esse número existe no vetor ou não. Se existir, 
# o algoritmo deve gerar um novo vetor sem esse número. (Considere que não haverá números repetidos no vetor).

print('')

numeros1 = []
numeros2 = []
num = 0
numeros = 0


for i in range(0, 4):
    print('Digite o {}º valor'.format(i + 1))
    valores = (int(input()))
    numeros1.append(valores)

print('Digite um valor')
num = int(input())
    
for i in range(0, 4):
    if num != numeros1[i]:       # != significa diferente
        # print('O numero {} existe no vetor'.format(num))
        numeros2.append(numeros1[i]) 
print(numeros2)





    
       
