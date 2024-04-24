#Crie um algoritmo que sorteie 5 valores entre 0 e 100 e depois imprima o menor, o maior e a média
#dos valores sorteados.
import random
#menor=-1
#maior=101
valores_sorteados=[]
for i in range(5):
    sorteio=random.randint(0,100)
    valores_sorteados.append(sorteio)

    maiorvalor=int(max(valores_sorteados))
    menorvalor=int(min(valores_sorteados))
    media= int(sum(valores_sorteados)/ len(valores_sorteados))
    print('Maior valor:',maiorvalor)
    print('Menor valor:',menorvalor)
    print('Média dos valores:',media)

        
        
