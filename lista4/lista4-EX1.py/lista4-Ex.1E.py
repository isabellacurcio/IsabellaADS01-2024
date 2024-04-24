#Ler 15 números e escrever a soma e a média dos números lidos.
# Inicializa a variável de soma
soma = 0

# Lê os 15 números e adiciona à soma
for i in range(15):
    numero = float(input(f"Digite o",i+1,"º número: ")) 
    soma += numero

# Calcula a média
media = soma / 15

# Escreve a soma e a média na tela
print(f"A soma dos números é: ",soma)
print(f"A média dos números é:",media)


