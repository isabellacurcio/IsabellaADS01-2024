#Faça um conversor de câmbio de reais/dólar/euro. O usuário deve informar inicialmente a cotação
#de cada moeda em relação ao real. Depois apresente o seguinte menu: 

taxaRealEuro= float(input('Digite a cotação do Euro em relação ao Real:'))
taxaRealDolar= float(input('Digite a cotação do Dólar em relação ao Real:'))
taxaEuroDolar= float(input('Digite a cotação do Euro em relação ao Dólar:'))

print('Menu:')
print('1) Converter de Real para Euro')
print('2) Converter de Real para Dólar')
print('3) Converter de Euro para Dólar')
print('4) Converter de Euro para Real')
print('5) Converter de Dólar para Euro')
print('6) Converter de Dólar para Real')
escolhausuario=input('Escolha uma das opções do Menu:')
resposta=float(input('Digite o valor a ser convertido:'))
if escolhausuario== '1':
    E=resposta / taxaRealEuro
    print('Você receberá',E,'euros.')
elif escolhausuario== '2':
    D= resposta / taxaRealDolar
    print('Você receberá',D,'dólares')
elif escolhausuario== '3':
    ED= resposta * taxaEuroDolar
    print('Você receberá',ED,'dólares')
elif escolhausuario== '4':
    ER= resposta * taxaRealEuro
    print('Você receberá',ER,'reais')
elif escolhausuario== '5':
    DE= resposta / taxaEuroDolar
    print('Você receberá',DE,'euros')
else:
    escolhausuario== '6'
    DR= resposta * taxaRealDolar
    print('Você receberá',DR,'reais')
