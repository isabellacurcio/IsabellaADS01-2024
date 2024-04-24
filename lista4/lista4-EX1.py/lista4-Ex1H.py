#Ler n números e imprimir no final a soma dos números lidos (obs.: n é a quantidade de números
#que deverão ser lidos e também deve ser lido do teclado) 

n=int(input('Digite a quantidade números a serem lidos: '))
soma=0
for _ in range(n):
    numeros=float(input('Digite um número:')) 
    soma += numeros
print('A soma dos numeros lidos é:',soma) 
