import csv

arquivoCSV = open('gatos.csv',encoding='utf-8') 
leitor = csv.reader(arquivoCSV,delimiter=';')
dados = list(leitor) #aqui já temos uma tabela, mas apenas com strings
dadosONG = [] # dadosONG é a matriz que vai mesmo armazenar nossos dados para as consultas
listaMenu = [ # lista das opcoes do menu
            "1) Cadastrar felino",
            "2) Alterar status de felino", 
            "3) Consultar informações sobre felino", 
            "4) Apresentar estatísticas gerais", 
            "5) Filtragem de dados", 
            "6) Salvar", 
            "7) Sair do programa"
        ]


# funcoes -------------------

def OperacoesMenu (listaMenu): # dividir funcoes!!

    print("Menu:")
    for i in range (len(listaMenu)):
        print(listaMenu[i])

    while True:
        opcao = int(input("Insira o numero da acao que deseja realizar: ")) # opcao do menu selecionada pelo usuario 
        if opcao in [1, 2, 3, 4, 5, 6, 7]: # condicao q verifica se a opcao e valida
            if opcao == 1:
                CadastrarFelino()
            elif opcao == 2:
                AlterarStatus()
            elif opcao == 3:
                ConsultarInformacoes()
            elif opcao == 4:
                EstatisticasGerais()
            elif opcao == 5:
                FiltragemDados()
            elif opcao == 6:
                Salvar()
            elif opcao == 7: #esse nao precisa de funcao
                Salvar()
                print("Saindo...")
                break
        else: 
            print("Opção inválida!")

# funcao opcao 1
def CadastrarFelino():
    global dadosONG
    nome = input("Digite o nome do felino: ")
    raça = input("Digite a raça do felino: ")
    idade = int(input("Digite a idade do felino: "))
    status = input("Digite o status do felino (disponível/adotado): ")
    novo_felino = [nome, raça, idade, status]
    dadosONG.append(novo_felino)
    print("Felino cadastrado com sucesso!") 

# funcao opcao 2
def AlterarStatus():
     global dadosONG
     nome = input("Digite o nome do felino para alterar o status: ")
     for felino in dadosONG:
        if felino[0].lower() == nome.lower():
            novo_status = input(f"Digite o novo status para {nome} (disponível/adotado): ")
            felino[3] = novo_status
            print(f"Status do felino {nome} alterado para {novo_status}")
            return
     print(f"Felino com nome {nome} não encontrado.")

# funcao opcao 3
def ConsultarInformacoes():
    nome = input("Digite o nome do felino para consultar as informações: ")
    for felino in dadosONG:
        if felino[0].lower() == nome.lower():
            print(f"Informações do felino {nome}:")
            print(f"Raça: {felino[1]}")
            print(f"Idade: {felino[2]}")
            print(f"Status: {felino[3]}")
            return
    print(f"Felino com nome {nome} não encontrado.")

# funcao opcao 4
def EstatisticasGerais():
    total_felinos = len(dadosONG)
    total_disponiveis = sum(1 for felino in dadosONG if felino[3].lower() == 'disponível')
    total_adotados = sum(1 for felino in dadosONG if felino[3].lower() == 'adotado')
    print(f"Total de felinos: {total_felinos}")
    print(f"Felinos disponíveis: {total_disponiveis}")
    print(f"Felinos adotados: {total_adotados}")

# funcao opcao 5
def FiltragemDados():
     filtro = input("Digite o critério de filtragem (nome, raça, idade ou status): ").lower()
     valor = input(f"Digite o valor para filtrar por {filtro}: ").lower()
     resultados = []
     for felino in dadosONG:
        if filtro == "nome" and felino[0].lower() == valor:
            resultados.append(felino)
        elif filtro == "raça" and felino[1].lower() == valor:
            resultados.append(felino)
        elif filtro == "idade" and str(felino[2]) == valor:
            resultados.append(felino)
        elif filtro == "status" and felino[3].lower() == valor:
            resultados.append(felino)
     if resultados:
        print(f"Resultados da filtragem por {filtro} = {valor}:")
        for felino in resultados:
            print(f"Nome: {felino[0]}, Raça: {felino[1]}, Idade: {felino[2]}, Status: {felino[3]}")
     else:
        print(f"Nenhum felino encontrado com {filtro} = {valor}")


# funcao opcao 6
def Salvar():
    with open('gatos_atualizado.csv', 'w', newline='', encoding='utf-8') as arquivoCSV:
        escritor = csv.writer(arquivoCSV, delimiter=';')
        escritor.writerows(dadosONG)
    print("Dados salvos com sucesso!")

print(dados)


# Preenchendo dadosONG, fazendo as conversões de tipo necessárias
#percorrer, linha a linha, nossa matriz (tabela) de dados
for i in range(len(dados)): #percorrendo as linhas (esse csv não tem cabeçalho)
    linha = [] #linha auxiliar
    for j in range(len(dados[0])): #percorrendo as colunas
        if j == 2: #terceira coluna é a idade
            linha.append(int(dados[i][j]))
        else:
            linha.append(dados[i][j])
    dadosONG.append(linha)


def Main():
    OperacoesMenu(listaMenu)

print(Main())
