###################FUNÇÃO#################
def tabuada(n):
    for i in range(1,11):
        print(n,'x',i,'=',n*i)

################PROGRAMA PRINCIPAL##############
    n=int(input('Digite um número inteiro:'))
    tabuada(n)
    