inventario = []

resposta = "S"
while resposta == "S":
    equipamento = [input("Equipamento: "),
                   float(input("Valor: ")),
                   int(input("Numero Serial: ")),
                   input("Departamento: ")]
    
    inventario.append(equipamento)
    resposta = input("Digite \"S\" para continuar: ").upper()

for elemento in inventario:
    print("===== Equipamento =====")
    print("Nome: ",elemento[0])
    print("Valor:",elemento[1])
    print("Serial:",elemento[2])
    print("Departamento: ",elemento[3])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for elemento in inventario:
    if busca.upper() == elemento[0].upper():
        print("Valor:",equipamento[1])
        print("Serial:",equipamento[2])

diminuir_preco = input("Digite o nome do equipamento para diminuir o preço: ")

for elemento in inventario:
    if diminuir_preco == elemento[0]:
        print("Valor antigo: ",elemento[1])
        elemento[1] = elemento[1] * 0.90
        print("Novo valor: ",elemento[1])

resposta = input("Deseja remover um item? ").upper()
while resposta == "S":
    equipamento_danificado = int(input("Digite o serial do equipamento danificado: "))
    for elemento in inventario:
        if elemento[2] == equipamento_danificado:
            inventario.remove(elemento)
            break
    
    resposta = input("Deseja remover mais um item? ").upper()

for elemento in inventario:
    print("Nome:",elemento[0])
    print("Valor:",elemento[1])
    print("Serial:",elemento[2])
    print("Departamento:",elemento[3])

valores = []
for elemento in inventario:
    valores.append(elemento[1])

if len(valores) > 0:
    print("O equipamento mais caro custa: ", max(valores))
    print("O equipamento mais barato custa: ",min(valores))
    print("O valor de todos equipamentos juntos é de: ", sum(valores))





 
