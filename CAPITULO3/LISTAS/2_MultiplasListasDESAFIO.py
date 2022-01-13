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

for i in range(0,len(equipamentos)):
    if equipamentos[i].upper() == "IMPRESSORA":
        valores[i] = valores[i] * 0.90

for j in range (0, len(equipamentos)):
    print("====== Equipamento "+str(j + 1)+" ======")
    print("Nome:",equipamentos[j])
    print("Valor:",valores[j])
    print("Serial:",seriais[j])
    print("Departamento:",departamentos[j])
