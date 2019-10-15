#Acrescente uma mensagem 'NOVO CÁLCULO (S/N)?' ao final do exercício [48]. 
#Se for respondido 'S' deve retornar e executar um novo cálculo, caso contrário deverá encerrar o algoritmo.

repet = 'S'

while (repet == 'S'):
    n1 = float(input('Digite a primeira nota'))
    while ((n1 < 0) or (n1 > 10)):
        n1 = float(input('Digite a primeira nota'))

    n2 = float(input('Digite a segunda nota'))
    while ((n2 < 0) or (n2 > 10)):
        n2 = float(input('Digite a segunda nota'))

    resultado = (n1 + n2) / 2

    print('Reseultado da divisao> {:.2f}'.format(resultado))
    repet = str(input('Novo calculo (S/N)?'))
