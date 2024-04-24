#Elabore um algoritmo que calcule o que deve ser pago por um produto, considerando o preço
#normal de etiqueta e a escolha da condição de pagamento. Utilize os códigos da tabela a seguir
#para ler qual a condição de pagamento escolhida e efetuar o cálculo adequado.
preço=float(input('Digite o preço do produto:'))
pagamento=input('Digite a forma de pagamento:')

if pagamento=='A vista em dinheiro':
    total=preço - (preço * 0.15)
    print('Valor a ser pago é de''R$',total)
else:
    pagamento=='A vista no cartão'
    total2=preço-(preço * 0.10)
    print('O valor a ser pago é de''R$',total2)

if pagamento==('Em duas vezes'):
    total3= preço 
    print('Total a pagar é de''R$',total3)

else:
    pagamento=='Em três vezes'
    total4= preço + (preço * 0.10)
    print('Total a ser pago é de''R$',total4)

