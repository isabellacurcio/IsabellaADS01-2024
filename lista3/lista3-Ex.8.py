#Um comerciante comprou um produto e quer vendê-lo com lucros diferentes dependendo do valor
#da compra. Ele quer um lucro de 45% se o valor da compra for menor que R$ 20,00, 35% se o preço
#for de até 50 reais e lucro de 25% se valor for maior. Entrar com o valor do produto e imprimir na
#tela o valor de venda.

valorproduto=float(input('Digite o valor do produto escolhido:'))

if valorproduto < 20.0:
    lucro=(valorproduto * 0.45) + valorproduto
    print('Valor fianl da venda''R$',lucro)

elif valorproduto <= 50:
     lucro2=(valorproduto * 0.35) + valorproduto
     print('Valor final da venda:''R$',lucro2)
    
    
else:
   valorproduto > 50
   lucro3=(valorproduto * 0.25) + valorproduto
   print(' Valor final da venda:''R$',lucro3)


