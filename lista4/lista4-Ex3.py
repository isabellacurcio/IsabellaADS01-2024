#Elabore um programa que lê um número de 1 a 9 e mostra a tabuada de multiplicação do número. 

num=int(input('Digite um número de 1 a 9:'))
for i in range(1,11):
       tabuada= num * i 
       print('-',num, 'X',i,'=',tabuada,)