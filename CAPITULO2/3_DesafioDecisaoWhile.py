    
resposta = "SIM"
while resposta == "SIM":
    nivel_acesso = input("Digite o nivel de acesso: ").upper()

    if(nivel_acesso == "ADM" or nivel_acesso == "USR"):
        genero = input("Digite o seu genero: ").upper()
        if(genero == "MASCULINO"):
            print("Olá administrador")
        else:
            print("Olá administradora")
    elif(nivel_acesso == "GUEST"):
        print("Olá visitante")
    else:
        print("Olá desconhecido(a)")
    
    resposta = input("Digite SIM para continuar: ").upper()