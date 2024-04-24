#Sortear 20 números inteiros entre -10 e 10 e imprimi-los acompanhados da mensagem
#“POSITIVO”, “NEGATIVO”, ou “NULO”, conforme o caso. No final, imprimir a quantidade de
#números positivos e negativos lidos. 
import random


positivo=0
negativo=0 

for i in range(20):
    sorteio= random.randint(-10,10)

    if sorteio > 0:
        print(sorteio,'- positivo') 
        positivo= positivo + 1
    elif sorteio==0:
        print(sorteio,'- nulo')
    else:
        sorteio< 0
        print(sorteio,'- negativo')
        negativo=negativo + 1 
print('Números positivos:',positivo,'.''Números negativos:',negativo)
 
    