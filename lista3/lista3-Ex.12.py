#A confederação brasileira de natação irá promover eliminatórias para o próximo mundial. Fazer um
#algoritmo que receba a idade de um nadador e imprima a sua categoria segundo a tabela a seguir:
idade=int(input('Digite a idade do atleta:'))
if (5<= idade <=7):
    print('Categoria Infantil A')
elif( 8 <= idade <=10):
    print('Categoria Infantil B')

elif( 11 <= idade <= 13):
    print('Categoria Juvenil A')
elif(14<= idade <= 17):
    print('Categoria Juvenil B')

else:
    ( 18 <= idade)
    print('Categoria Sênior')


