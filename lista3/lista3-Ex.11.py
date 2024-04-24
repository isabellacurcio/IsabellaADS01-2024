#Crie um programa para informar quais e quantas notas são necessárias para entregar o mínimo de
# cédulas para um determinado valor informado pelo usuário considerando notas de R$ 100, R$ 50,
#R$ 20, R$ 10 e R$ 5 e R$ 1.
def contagemcedulas(valor):
    cedulas=[100,50,20,10,5,1]
    quantidade={}
    for cedula in cedulas:
     quantidadecedulas= valor// cedula
     valor%=cedula 
     if quantidadecedulas > 0:
        quantidade[cedula]= quantidadecedulas

    return quantidade

#####################ProgramaPrincipal####################
valor=int(input('Digite o valor desejado:'))
cedula=contagemcedulas(valor)
print('Quantidade notas necessárias para R$',valor,':')
for cedula,quantidade in cedula.items():
   print('R$',cedula,':',quantidade)




