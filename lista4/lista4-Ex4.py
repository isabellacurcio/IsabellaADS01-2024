#Escrever um programa que calcule todos os números divisíveis por certo valor indicado pelo usuário (o
#resto da divisão por este número deve ser igual a zero), compreendidos em um intervalo também
#especificado pelo usuário. O usuário deve entrar com um primeiro valor correspondente ao divisor e
#após ele vai fornecer o valor inicial do intervalo, seguido do valor final deste intervalo. 
divisor= int(input('Digite o valor do divisor:'))

int1=int(input('Digite o valor do primeiro intervalo:'))
int2= int(input('Digite o valor do final do intervalo:'))

for i in range(int1 , int2 , 1):
    if i % divisor == 0:
        print('Os números divisíveis por {} de acordo com o intervalo dado são: {}'.format( i , i,  end= ', ' ))
        

    