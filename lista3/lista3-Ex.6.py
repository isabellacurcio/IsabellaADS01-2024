#Brincadeira do PAR ou ÍMPAR. Pergunte para o usuário se ele aposta em PAR ou ÍMPAR. Depois
#disso, peça para ele digitar um número de 0 a 5 (como se fosse mostrar os dedos da mão. Sorteie
#um número de 0 a 5 e some com o que o usuário digitou. Se o usuário escolheu PAR e o valor da
#soma for par OU se ele escolheu ÍMPAR e o valor da soma é ímpar, diga que ele venceu. Senão, diga
#que o programa venceu 

escolhausuario=input('Escolha entre Par ou Impar:')
numerousuario=int(input('Agora digite um número de 0 a 5:'))
import random
sorteio= random.randint(0,5)
soma= numerousuario + sorteio 
print(' Você escolheu',escolhausuario,'e digitou número',numerousuario,'.')

if (soma % 2==0 and escolhausuario == 'Par') or (soma % 2 != 0 and escolhausuario== 'Impar'):
    print('Você ganhou!!!')

else:
    print('O programa ganhou!!!!')


