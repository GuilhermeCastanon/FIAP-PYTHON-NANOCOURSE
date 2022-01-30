def preencherInventario(lista):
    resposta = "S"
    while resposta == "S":
        equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Numero Serial: ")),
                   input("Departamento: ")]
        lista.append(equipamento)
        resposta = input("Digite \"S\" para continuar: ").upper()

def exibirInventario(lista):
    for elemento in lista:
        print("===== Equipamento =====")
        print("Nome: ",elemento[0])
        print("Valor:",elemento[1])
        print("Serial:",elemento[2])
        print("Departamento: ",elemento[3])

def localizarPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca.upper() == elemento[0].upper():
            print("Valor:",elemento[1])
            print("Serial:",elemento[2])

def depreciarPorNome(lista,porcentagem):
    diminuir_preco = input("Digite o nome do equipamento para diminuir o preço: ")
    for elemento in lista:
        if diminuir_preco == elemento[0]:
            print("Valor antigo: ",elemento[1])
            elemento[1] = elemento[1] * (porcentagem/100)
            print("Novo valor: ",elemento[1])
    print("Item depreciado com sucesso!")

def excluirPorSerial(lista):
    resposta = input("Deseja remover um item? ").upper()
    while resposta == "S":
        equipamento_danificado = int(input("Digite o serial do equipamento danificado: "))
        for elemento in lista:
            if elemento[2] == equipamento_danificado:
                lista.remove(elemento)
                break
    
        resposta = input("Deseja remover mais um item? ").upper()

    print("Itens excluidos com sucesso!")


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])

    if len(valores) > 0:
        print("O equipamento mais caro custa: ", max(valores))
        print("O equipamento mais barato custa: ",min(valores))
        print("O valor de todos equipamentos juntos é de: ", sum(valores))




