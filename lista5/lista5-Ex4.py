#Implemente uma função sorteio que receba o intervalo de valores inteiros início e fim como parâmetro
#e sorteie um número dentro do intervalo (considerando intervalo fechado [início, fim])
import random
def sorteio(intervalo1,intervalo2):
   return random.randint(intervalo1,intervalo2)
   
    

    ##print('O número sorteado dentro do intervalo foi',num)
    
 

######################PRINCIPAL###################
    
intervalo1=int(input('Digite o primeiro intervalo:'))
intervalo2=int(input('Digite o segundo intervalo:'))
num=sorteio(intervalo1,intervalo2)
print('O número sorteado foi:',num)