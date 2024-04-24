#Faça um programa que leia a nota do Grau A e do Grau B do aluno e calcule a média final conforme
#as regras da Unisinos. Imprima a média final na tela e diga se o aluno passou por média ou se ficou
#em recuperação (grau C). Se o aluno ficou em recuperação, pergunte se ele quer substituir o Grau
#A ou o Grau B (ele deve digitar ‘a’ ou ‘b’). Leia a nota do Grau C, recalcule a média de acordo com o
#grau substituído e imprima na tela o resultado, informando se ele foi aprovado ou reprovado.
A=float(input('Digite sua nota no Grau A:'))
B= float(input('Agora digite sua nota no Grau B:'))
media= (A + (2 * B)) /3
if media<6:
    print('Sua média foi',media,'.''Ficou de recuperação.:()')
    recup=(input('Gostaria de substituir o Grau A ou Grau B: '))
    C=float(input('Digite sua nota no Grau C:'))
    if recup=='a':
        media2=(C + ( 2 * B)) /3
        if media2>= 6:
            print('Você passou!')
        else:
            print('Você não passou:()')
    else:
        recup=='b'
        media3=(A + ( 2 * C))/3
        if media3>= 6:
            print('Você passou!')
        else:
            print('Você não passou :()')
else:
    print('Você foi aprovado!!')



    
