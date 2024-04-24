#Encontrar o dobro de um número caso ele seja positivo e o seu triplo caso seja negativo, imprimindo
#o resultado.
num=int(input('Digite um número inteiro:'))

if num< 0:
    triplo=num * 3
    print('Seu resultado é de:',triplo)

    
else:
    dobro=num * 2
    print( 'Seu resultado foi de:',dobro)