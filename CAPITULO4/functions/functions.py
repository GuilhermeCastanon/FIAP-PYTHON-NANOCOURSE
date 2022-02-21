def perguntar():
    opcao = input("O que dezeja realizar?\n" +
              "<I> - Para inserir um usuario\n" +
              "<P> - Para pesquisar um usuario\n" +
              "<E> - Para excluir um usuario\n" +
              "<L> - Para listar um usuario\n" +
              "<N> - Nada\n").upper()
    return opcao

def inserir(dicionario):
    codLancamento = input("Digite o codigo do lançamento: ").upper()
    login = input("Digite o login: ").upper()
    nome = input("Digite o nome: ").upper()
    data = input("Digite a ultima data de acesso: ")
    hora = input("Digite a hora do login: ")
    nivel = input("Digite seu nivel: ").upper()
    estacao = input("Qual a ultima estação acessada: ").upper()
    if codLancamento not in dicionario:
        dicionario[codLancamento] = [login,nome,data,hora,estacao,nivel]

def pesquisar(dicionario, chave):
    lista = dicionario.get(chave)

    if lista!=None:
        print("Login: " + lista[0])
        print("Nome: " + lista[1])
        print("Ultimo acesso: " + lista[2])
        print("Hora do acesso: " + lista[3])
        print("Estacao: " + lista[4])
        print("Nivel do usuario: " + lista[5])
    
def excluir(dicionario,chave):
    if dicionario.get(chave) != None:
        del dicionario[chave]
    print("Objeto Excluido")

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto......")
        print("Login: ",chave)
        print("Dados: ",valor)


