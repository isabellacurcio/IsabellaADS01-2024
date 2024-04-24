#Implemente um programa que sorteia um número de 1 a 10 e dá ao usuário 3 tentativas de acertá-lo.
#A cada tentativa errada, o programa informa se o número a adivinhar está abaixo ou acima. 
import random

resposta=''

sorteio=random.randint(1,10)
tentativas= 0
while  (tentativas < 3 and tentativas >= 0): 
    resposta=int (input('Digite um número de 1 a 10 :') )
    if resposta == sorteio:

        print('Você Acertou!!!!!!')
        break        

    elif resposta > sorteio:
        tentativas= tentativas + 1
        print('Resposta errada o número sorteado esta acima. Você tem',3- tentativas,'tentativas')
    else:
        resposta< sorteio
        tentativas= tentativas + 1
        print('Resposta errada o número sorteado esta a baixo.Você tem',3- tentativas,'tentativas')
    

