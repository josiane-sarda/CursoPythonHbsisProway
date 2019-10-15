#Faca um algoritmo para ler um valor N qualquer (que será o tamanho dos vetores). Após, ler dois valores A e B
#de tamanho N cada um) e depois armazenar em um terceiro vetor_soma, a soma dos elementos do vetor A 
#com os do vetor B (respeitando as mesmas posições) e escrever o vetor soma.

tamanho_vetor = 0
vetorA = []
vetorB = []
vetorSoma = []
soma = 0
valores = 0

print('Digite um numero')
tamanho_vetor = int(input())

for A in range(0, tamanho_vetor):
    print('Digite o {}º valor do Vetor A'.format(A + 1))
    vetorA.append(int(input()))

for B in range(0, tamanho_vetor):
    print('Digite o {}º valor do Vetor B'.format(B + 1))
    vetorB.append(int(input()))

for i in range(0, tamanho_vetor):
    soma = vetorA[i] + vetorB[i]
    vetorSoma.append(soma)

print('O vetor soma é: {}'.format(vetorSoma))

    
