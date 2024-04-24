#Fazer um programa que calcule e imprima o fatorial de um número fornecido pelo usuário. Repetir a
#execução do programa tantas até o usuário responder não. O fatorial de um número inteiro positivo é
#definido como o número multiplicado por ele menos 1, menos 2, etc até o valor 1.
#Por exemplo, o fatorial de 4 é 4x3x2x1=24. 
def calcularfatorial(num):
    fatorial=1
    for i in range(1,num+1):
        fatorial *=i 
    return fatorial 

while( pergunta != 'n' ):

  num=int(input('Digite um número por favor:')) 
  resultado=calcularfatorial(num)
  print('O fatorial de',num,'é de',resultado)
  pergunta=input('Deseja inserir outro número (s/n)?')

