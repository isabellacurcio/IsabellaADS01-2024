#Durante uma liquidação uma loja resolveu dar quinze por cento de desconto nas compras feitas
#pelos clientes. Faça um programa que leia o valor da compra e escreva o valor da compra com o
#desconto. 
valorsemdesconto=float(input('Digite o valor da sua compra:'))
desconto= 0.15
valorcomdesconto= (valorsemdesconto - (valorsemdesconto * desconto))


print('O valor total a se pagar com desconto é de''R$',valorcomdesconto)
                   