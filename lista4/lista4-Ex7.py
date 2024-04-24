#Descubra, dentre cinco nomes informados pelo usuário, qual o primeiro em ordem alfabética.
nomes=[]
for i in range(5):
    nome=input(f'Digite o {i+1}° nome:')
    nomes.append(nome)

primeironome= sorted(nomes)
print('Em ordem alfabética o primeiro nome seria:',primeironome)