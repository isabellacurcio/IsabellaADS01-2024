#. Utilizando o template de menus mostrado em aula, faça um programa que simule uma calculadora
#simples, mostrando ao usuário as opções somar, subtrair, multiplicar e dividir dois números reais. Cada
#uma das operações deve ser executada em funções que recebam como parâmetro os dois números,
#lidos do usuário. As funções devem retornar o resultado para o programa principal, que o exibirá na
#tela. OBS.: Apenas chame a função de dividir se o divisor for diferente de zero (divisão por zero não
#existe!).
def menu():
    print('CALCULADORA')
    print('1- somar:')
    print('2- subtrair:')
    print('3- multiplicar:')
    print('4- divisão:')
    item= input('Escolha uma opção:')
    return item
def opçao1(num1,num2):
    print('Opção escolhida foi a 1.')
    num1=int(input('Digite um número:'))
    num2=int(input('Digite o próximo número:'))
    soma=num1+num2
    print('Resposta é',soma)
def opçao2():
    print('Opçao escolhida foi a 2')
    num1=int(input('Digite um número:'))
    num2=int(input('Digite o próximo número:'))
    sub= num1 - num2
    print('Resposta é:',sub)
def opçao3():
    print('Opção escolhida foi a 3')
    num1=int(input('Digite um número:'))
    num2=int(input('Digite o próximo número:'))
    multi= num1* num2 
    print('A resposta é:',multi)
def opçao4():
    print('Opção escolhida foi a 4')
    num1=int(input('Digite um número:'))
    num2=int(input('Digite o próximo número:'))
    divisao= num1/num2 
    print('A resposta é:',divisao) 
    if num1 and num2==0:
        print('Não é possivel realizar a divisão')
        

escolha=''
while escolha != 0:
    escolha=menu()
    if escolha=='1':
        opçao1()
        
    elif escolha=='2':
        opçao2()
        
    elif escolha=='3':
        opçao3()
    
    elif escolha=='4':
        opçao4()
     
    else:
        escolha==0
        print('Saindo do programa...')
        break 
