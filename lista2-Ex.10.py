#Dessa vez ele quer que
#você calcule quanto cada cliente gastou na loja apenas informando o número de camisetas, calças
#e cintos comprados. As camisetas custam R$ 25,00, as calças cem reais e os cintos 40 reais. Some o
#valor da compra e ao final dê um desconto de 10 por cento sobre o total. Exiba na tela o valor do
#desconto e o valor da compra.
camisetas=float(input('Digite a quantidade de camisetas compradas:'))
calças=float(input('Digite a quantidade de calças compradas:'))
cintos=float(input('Agora digite a quantidade de cintos comprados:'))

valorcamiseta=25 * camisetas
valorcalça=100 * calças
valorcinto= 40 * cintos

compradocliente= valorcamiseta + valorcalça + valorcinto 

valorfinal= (compradocliente-(compradocliente * 0.10))

print('O valor final da compra foi de ''R$',compradocliente,'.''Mas adicionando um desconto de 10% o valor a se pagar fica de''R$',valorfinal)