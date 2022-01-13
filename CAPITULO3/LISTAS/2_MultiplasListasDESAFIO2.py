equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper()


resposta = input("Deseja remover um item? ").upper()
while resposta == "S":
    equipamento_danificado = int(input("Digite o serial do equipamento danificado: "))
    for i in range(0,len(equipamentos)):
        if seriais[i] == equipamento_danificado:
            del equipamentos[i]
            del valores[i]
            del seriais[i]
            del departamentos[i]
            break
    
    resposta = input("Deseja remover mais um item? ").upper()

for j in range (0, len(equipamentos)):
    print("====== Equipamento "+str(j + 1)+" ======")
    print("Nome:",equipamentos[j])
    print("Valor:",valores[j])
    print("Serial:",seriais[j])
    print("Departamento:",departamentos[j])

