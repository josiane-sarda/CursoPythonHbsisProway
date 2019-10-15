# Ler 3 valores (considere que não serão informados valores iguais) e escrever a soma dos 2 maiores.

print('Soma dos dois numeros miores')
print('Digite o primeiro numero')
num1 = float(input())

print('Digite o segundo numero')
num2 = float(input())

print('Digite o terceiro numero')
num3 = float(input())

if num1 > num2 and num1 > num3 and num2 > num3:
    soma = num1 + num2
    print('A soma dos dois valores maiores é: {}'.format(soma))
else:
    if num1 > num2 and num1 > num3 and num3 > num2:
        soma = num1 + num3
        print('A soma dos dois valores maiores é: {}'.format(soma))
    else:
        if num2 > num1 and num2 > num3 and num1 > num3:
            soma = num2 + num1
            print('A soma dos dois valores maiores é: {}'.format(soma))
        else:
            if num2 > num1 and num2 > num3 and num3 > num1:
                soma = num2 + num3
                print('A soma dos dois valores maiores é: {}'.format(soma))
            else:
                if num3 > num1 and num3 > num2 and num1 > num2:
                    soma = num3 + num1
                    print('A soma dos dois valores maiores é: {}'.format(soma))
                else:
                    if num3 > num1 and num3 > num2 and num2 > num1:
                        soma = num3 + num2
                        print('A soma dos dois valores maiores é: {}'.format(soma))
        
        
        
    
