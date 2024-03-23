#Cada smartphone custa R$ 1000,00 e cada tablet custa R$ 1500,00. Ao final
#do dia, o dono quer saber quanto arrecadou com a venda dos smartphones e dos tablets. Escreva
#um programa que leia o número de smartphones e tablets vendidos em um dia e calcule o total
#arrecadado.

smartphones=float(input('Digite a quantidade vendida no dia de smartphones:'))
tablets=float(input('Digite a quantidade vendida no dia de tablets: '))
S=1000
T=1.500
totaldodia= ((S* smartphones) + (T* tablets))
print('Seu total arrecadado no dia foi de''R$',totaldodia)
