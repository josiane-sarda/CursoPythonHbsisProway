# - Escreva um algoritmonpara ler um valor(do teclado) e
# escrever (na tela) o seu antecessor.

print('Digite um numero')
valor = int(input())

valor = valor - 1
print( 'Antecessor: {}, {}'.format (valor, 10) )
# print (Antecessor: ', valor, ',', 10)

#Outra forma: 
#valor_antes = valor - 1
#print ('o antecessor do {} é {}' .format()valor, valor_antes)
#print('o antecessor de ', valor , 'é' , valor_ntes)