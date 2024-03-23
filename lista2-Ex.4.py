#Faça um algoritmo que permita ao aluno calcular a sua média final na Unisinos. Leia a nota do grau
#A e do grau B e escreva o resultado na tela.
grauA=float(input('Digite sua nota tirada no Grau A:'))
grauB=float(input('Agora digite sua nota no Grau B:'))

media= ((grauA + (grauB*2)) /3)

print('Sua média final nesta disciplina é de',media,'.')