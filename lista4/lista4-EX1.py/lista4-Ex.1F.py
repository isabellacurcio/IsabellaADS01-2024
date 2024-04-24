#Ler 10 números inteiros e escrever a quantidade de números pares e a quantidade de números
#ímpares lidos.
numpar=0
numimpar=0

for i in range(10):
    num=int(input('Digite um número inteiro:'))
    if num % 2==0:
        numpar= numpar + 1
    else:
        numimpar= numimpar + 1
print('Quantidade de números pares',numpar,'quantidade de números ímpares',numimpar) 
