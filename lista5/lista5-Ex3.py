####################FUNÇÕES#####################
def mediaUnisinos(grauA,grauB):
    media=(grauA + (2* grauB)) /3.0
    return media




####################PROGRAMAPRINCIPAL###############

grauA=float(input('Digite sua média do grau A:'))
grauB=float(input('Digite sua média no grau B:'))

graufinal=mediaUnisinos(grauA,grauB)
print('Grau final é',graufinal)
#print('Grau final é', mediaUnisinos(grauA,grauB))
