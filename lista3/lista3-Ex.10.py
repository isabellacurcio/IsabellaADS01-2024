#Faça um programa que
#simule dados de 4, 6, 8, 10, 12 ou 16 faces (apenas estes valores). Peça para o usuário informar no
#começo do programa quantas faces quer, para depois fazer o sorteio.
escolhadodado=int(input('Informe quantos lados deseja que o dado tenha:'))
import random
sorteiododado= random.randint(1,escolhadodado)
print('O número sorteado foi:',sorteiododado)