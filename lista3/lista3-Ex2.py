#Faça um algoritmo que leia os valores A, B, C e imprima na tela se a soma de A + B é menor que A
#+ C.
A=int(input('Digite um valor inteiro para A:'))
B=int(input('Digite um valor inteiro para B:'))
C=int(input('Digite um valor inteiro para C:'))

if (A + B) < (A + C): 
    print('Sim, o resultado de A + B é menor que A + C.')

else:
    print('Não, o resultado de A + B é maior A + C.' )