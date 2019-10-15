#Ler dois valores (considere que não serão lidos valores iguais) e escrever o maior deles.

print('Temporizador xadrez')
print('Digite a hora de inicio')
inicio =int(input())
print('Digite a hora de fim')
fim =int(input())
duracao = 0
if inicio < fim:
    duracao = fim - inicio
else:
    duracao = (fim + 24) - inicio
print('duracao {} horas'.format(duracao))

#duraco = 0, para que a variavel exista fora do if.