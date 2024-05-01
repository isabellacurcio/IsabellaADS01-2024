import random 
import os 
###############FUNCÕES###############
sorteiodado=random.randint(1,6)
ncasa1=0
ncasa2=0
sorteiodado=random.randint(1,6)
filhosjogador1=0
filhosjogador2=0
casamento1=0
casamento2=0
divorcio1=0
divorcio2=0
formado1=0
formado2=0
famoso1=0
famoso2=0
loteria1=0
loteria2=0
posjogador1= ncasa1 + sorteiodado 
posjogador2= ncasa2 + sorteiodado 
def Menu():
    print('JOGO DA VIDA!')
    print('Escolha uma opção para começar a jogar:')
    print('1-Apenas um jogador.')
    print('2-Dois jogadores.')
    escolha=input('Digite sua escolha:')
    return escolha 


def Dado():
    girarroleta= random.randint(1,6)
    if girarroleta==1:
        ncasa= ncasa +1
    elif girarroleta==3:
          ncasa= ncasa - 1 
    else:
        girarroleta==6
        pass 

def Morreu():
    print("GAME OVER!!!")
    print("informacões do jogador:")
    if casamento1==1:
        print('Você se casou')
    else:
        print('Você não se casou')
    if filhosjogador1==1 or filhosjogador1==2:
        print('Você teve filho(s)')
    else: 
        filhosjogador1==0
        print('Você não teve filhos')
    if formado1==1:
        print('Você se formou na faculdade.')
    else:
        print('Você não se formou em nenhum curso')
    if famoso1==1:
        print('Você ficou famoso')
    else:
        print('Você não ficou famoso')
    if divorcio1==1:
        print('Você se divorciou')
    if loteria1==1:
        print('Você ganhou dinheiro na loteria')
    
    if casamento2==1:
        print('Você se casou')
    else:
        print('Você não se casou')
    if filhosjogador2==1 or filhosjogador2==2:
        print('Você teve filho(s)')
    else: 
        filhosjogador2==0
        print('Você não teve filhos')
    if formado2==1:
        print('Você se formou na faculdade.')
    else:
        print('Você não se formou em nenhum curso')
    if famoso2==1:
        print('Você ficou famoso')
    else:
        print('Você não ficou famoso')
    if divorcio2==1:
        print('Você se divorciou')
    if loteria2==1:
        print('Você ganhou dinheiro na loteria')
     
    #dar print dos dados do jogador e dizer quem venceu  o jogo se for em dupla
def DesafioMatematico():
    
       girarroleta= random.randint(1,6)
       if girarroleta== 1:
          def Primos(numero):
             if numero <2:
                return False
             for numero in range(2,101):
               print('-',numero)
             Primos(numero)
       elif girarroleta==2:
          def Somatorio(somatorio):
              somatorio = 0
              for num in range(1, 11):
                 somatorio += num   
                 print("O somatório dos números de 1 até 10 é:", somatorio)
              Somatorio(somatorio)
       elif girarroleta== 3:
           def Fibo(fibonacci):
              fibonacci = [0, 1]          
              for _ in range(8):  # Precisamos calcular mais 8 números para ter um total de 10
                fibonacci.append(fibonacci[-1] + fibonacci[-2])
                print("Os dez primeiros números da sequência de Fibonacci são:", fibonacci) 
              Fibo(fibonacci)
       elif girarroleta== 4:
           def AreaCirculo(a):
             #Considere PI = 3.14
              a= 3.14 * (2.5 * 2.5)
              print('A área da circunferência de raio 2.5 é:',a)
              AreaCirculo(a)
       elif girarroleta==5:
            def Fatorial(n):
              n=5 
              fatorial=1
              for i in range(1,n + 1):
                fatorial *= i 
                print('O fatorial de 5 é',fatorial)
              Fatorial(n)
       elif girarroleta==6:
           def Div25():
             contador2=0
             contador5=0
             numero=1

             print('Primeiros cincos números divisíveis por 2')
             while contador2 <5:
               if numero % 2==0:
                  print(numero)
                  contador2 += 1
               numero +=1  
            
             numero=1
             print('Primeiros cincos números divisíveis por 5')
             while contador5 < 5:
              if numero % 5==0:
                  print(numero)
                  contador5 +=1
              numero +=1
             Div25()
def Formatura():
    girarroleta= random.randint(1,6)
    if girarroleta== 1:
        print('Você se formou em Direito!!!')
    elif girarroleta==2:
        print('Você se formou em Medicina!!!')
    elif girarroleta==3:
        print('Você se formou em Desenvolvimento de sistemas!!!')
    elif girarroleta==4:
        print('Você se formou em Nutrição!!!')
    elif girarroleta==5:
        print('Você se formou em Biomedicina!!!')
    elif girarroleta==6:
        print('Você se formou Ciência da Computação!!!')
def TerFilho(filhosjogador1):
    sorteiodado
    if sorteiodado==5:
        print('Você teve gemêos!!!!')
        filhosjogador1= filhosjogador1 + 2
    else:
        print('Você teve um filho!!!')
        filhosjogador1= filhosjogador1 + 1
def TerFilho2(filhosjogador2):
    if sorteiodado==5:
        print('Você teve gemêos!!!!')
        filhosjogador2= filhosjogador2 + 2
    else:
        print('Você teve um filho!!!')
        filhosjogador2= filhosjogador2 + 1
def Casar(casamento1):
    casamento1=casamento1+1
    if casamento1==1:
       print('Parabéns você se casou!')
def Casar2(casamento2):
    casamento2= casamento2 +1 
    print('Parabens! Você se casou!!')
    
def FicarFamoso(famoso1):
    famoso1= famoso1 + 1
    print('Você ficou famoso!!')
def FicarFamoso2(famoso2):
    famoso2= famoso2 + 1
def Divorciar(divorcio1):
    if casamento1==1:
        print('Seu status de relacionamento mudou, você se divorciou.')
        casamento1= casamento1-1
        divorcio1= divorcio1+1
    else:
        print(' Casa do divorcio, como não se casou nada acontece.Espere a próxima jogada.')
def divorciar2(divorcio2):
    if casamento2==1:
        print('Seu status de relacionamento mudou, você se divorciou')
        casamento2= casamento2 - 1
        divorcio2= divorcio2 + 1
    else:
        print('Casa do divorcio, como não se casou nada acontece.Espere a próxima jogada.')

def Loteria():
    girarroleta= random.randint(1,6)
    if girarroleta==1:
        print('Ganhou 2,50 no bolão.')
    elif girarroleta==2:
        print('Ganhou R$ 5000,00!')
    elif girarroleta==3:
        print('Ganhou R$ 50 000,00!!')
    elif girarroleta==4:
        print('Ganhou R$ 500 000,00!!')
    elif girarroleta==5:
        print('Ganhou R$ 5 000 000,00')
    else:
        girarroleta==6
        print('Ganhou R$ 100 000 000,00 ')
def Loteria2():
    girarroleta= random.randint(1,6)
    if girarroleta==1:
        print('Ganhou 2,50 no bolão.')
    elif girarroleta==2:
        print('Ganhou R$ 5000,00!')
    elif girarroleta==3:
        print('Ganhou R$ 50 000,00!!')
    elif girarroleta==4:
        print('Ganhou R$ 500 000,00!!')
    elif girarroleta==5:
        print('Ganhou R$ 5 000 000,00')
    else:
        girarroleta==6
        print('Ganhou R$ 100 000 000,00 ')
def Novoamor():
    if casamento1==0 and divorcio1==0:
        casamento1= casamento1+ 1
        print('Nova chance no amor! Você se casou.')
def Novoamor2():
    if casamento2==0 and divorcio2==0:
        casamento2= casamento2 + 1
        print('Nova chance no amor,você se casou!!')

def MaquinaDoTempo(njogador):
    print('Volte para o início do jogo!')
    casamento1=casamento1-1
    filhosjogador1= - filhosjogador1
    divorcio1= - divorcio1
    ncasa1= - ncasa1
    famoso1= - famoso1
    formado1= - formado1
    loteria1= - loteria1 
def MaquinaDoTempo2(njogador):
    print('Volte para o início do jogo!')
    casamento2=casamento2-1
    filhosjogador2= - filhosjogador2
    divorcio2= - divorcio2
    ncasa2= - ncasa2
    famoso2= - famoso2
    formado2= - formado2
    loteria2= - loteria2 






###############################Programa principal######################################
item=''
item=Menu()
if item=='1':
    input('Vamos jogar! Aperte ENTER para jogar o dado e começar a partida.')
    sorteiodado
    posjogador1=ncasa1 + sorteiodado 
    if posjogador1== 1 or posjogador1==3 or posjogador1==10:
         Dado() 
         print('Você está na',posjogador1, 'posição. Está no dado')
    input('Aperte ENTER para jogar o dado novamente')
    sorteiodado
    if posjogador1==2 or posjogador1==8 or posjogador1==18:
        Morreu()
        input('Jogue o dado apertando ENTER')
    sorteiodado
    posjogador1=ncasa1 + sorteiodado
    if posjogador1== 4 or posjogador1== 11 or posjogador1==19:
        print('Sua posição é',posjogador1, 'Você caiu em Desafio Matemático!!')
        DesafioMatematico()
        input('Jogue o dado apertando ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado 
    if posjogador1== 5:
        print('Sua posição é', posjogador1,)
        Formatura()
        input('Jogue o dado apertando ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado
    if posjogador1==6 or posjogador1==9 or posjogador1==13:
        print('Sua posição é',posjogador1,)
        TerFilho(filhosjogador1)
        input('Jogue o dado apertando ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado 
    if posjogador1==7:
        print('Sua posição é',posjogador1)
        Casar(casamento1)
        input('Jogue o dado apertando o ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado
    if posjogador1== 12 or posjogador1==16:
        print('Sua posição é',posjogador1)
        Divorciar(divorcio1)
        input('Jogue o dado apertando ENTER')
    sorteiodado
    posjogador1=ncasa1 + sorteiodado
    if posjogador1==14:
        print('Sua posição é',posjogador1)
        Loteria()
        input('Jogue o dado apertando ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado
    if posjogador1== 15:
        print('Sua posição é',posjogador1)
        FicarFamoso(famoso1)
        input('Jogue o dado apertando o ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado
    if posjogador1==16:
        print('Sua posição é',posjogador1)
        Novoamor()
        input('Jogue o dado apertando o ENTER')
    sorteiodado
    posjogador1= ncasa1 + sorteiodado
    if posjogador1==20:
        print('Sua posição é',posjogador1)
        MaquinaDoTempo()


    ##################vericação da vitoria################
    if posjogador1==21:
        print('Parabéns você teve uma vida longa e própera!')














            
          

                 
             





  
        


  
