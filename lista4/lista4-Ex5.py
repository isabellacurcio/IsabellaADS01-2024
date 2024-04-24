#Para x alunos da Unisinos, ler as notas do grau A e grau B e calcular a média considerando o sistema
#de notas da Unisinos. Se o aluno estiver aprovado escrever “APROVADO”. Caso contrário, ler o grau C
#e pedir qual o grau que deve ser substituído (A ou B, maiúsculo ou minúsculo), recalcular a média. Se
#estiver aprovado, escrever “APROVADO”, caso contrário escrever “REPROVADO”. No final escrever a
#média geral dos alunos.
x=int(input('Digite a quantidade de alunos:'))
# Criar uma lista para as médias dos alunos
medias=[]
for i in range(x):
    grauA=float(input(f'Digite a nota do Grau A do {1+i}° aluno:'))
    grauB=float(input(f'Digite a nota do Grau B do {1+i}° aluno:'))
    media=(grauA+(grauB*2))/3
    medias.append(media)
    if media >=6:
        print('APROVADO')
    else:
        print('REPROVADO')
        grauC=float(input('Digite sua nota do Grau C:'))
        substituir=input('Qual Grau deseja substituir?')
        if substituir=='A':
            media2=(grauC+ (grauB*2))/3
            if media2>=6:
                print('APROVADO')
            else:
                print('REPROVADO')
        else:
            substituir=='B'
            media3=(grauA+ (grauC*2))/3
            if media3>= 6:
                print('APROVADO')
            else:
                print('REPROVADO')
mediageral= sum(medias) / x 
print('A média geral dos alunos é de',mediageral)

