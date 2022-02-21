from functions.functions import*

usuarios = {}

opcao = perguntar()

while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        inserir(usuarios)
    elif opcao == "P":
        pesquisar(usuarios, input("Digite a chave a ser pesquisada: "))
    elif opcao == "E":
        excluir(usuarios, input("Digite a chave a ser excluida: "))
    elif opcao == "L":
        listar(usuarios)
    opcao = perguntar()

    