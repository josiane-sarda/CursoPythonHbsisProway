#Ler um valor e escrever se é positivo, negativo ou zero.

print('Numero positivo, negativo ou zero')
print('Digite um numero')
num = float(input())

if (num > 0):
    print('O número é positivo')
else:
    if (num == 0):
        print('O número é zero')
    else:
        if (num < 0 ):
            print ('O número é negativo')
    
