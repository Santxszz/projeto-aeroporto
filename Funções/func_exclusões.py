def ExcluirPassageiro():
    print("-"*50)
    print("Excluir Passageiro")
    print("-"*50)
    
    cpf = input("CPF: ")
    
    # Busca o passageiro e seus dados
    listaPassageiros = []
    with open("Dados/passageiros.bin", "rb") as file:
        for i in file:
            listaPassageiros.append(i.decode("utf-8").split(";"))
    for i in listaPassageiros:
        if cpf in i:
            passageiro = i
            break
        
    else:
        print("Passageiro não encontrado!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    # Exibe os dados do passageiro
    print("Dados Básicos:")
    print(f"Nome: {passageiro[0]}")
    print(f"CPF: {passageiro[1]}")
    print(f"RG: {passageiro[2]}")
    print(f"Sexo: {passageiro[3]}")
    
    # Pergunta se o usuário deseja excluir o passageiro
    print("-"*50)
    print("1 - Excluir")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        listaPassageiros.remove(passageiro)
        with open("Dados/passageiros.bin", "wb") as file:
            for i in listaPassageiros:
                file.write(";".join(i).encode("utf-8"))
                file.write("\n".encode("utf-8"))
        print("Passageiro excluído com sucesso!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    elif opção == "0":
        from Módulos.modExclusões import modExclusões
        modExclusão()
        
def ExcluirPiloto():
    print("-"*50)
    print("Excluir Piloto")
    print("-"*50)
    
    cpf = input("CPF: ")
    
    # Busca o piloto e seus dados
    listaPilotos = []
    with open("Dados/pilotos.bin", "rb") as file:
        for i in file:
            listaPilotos.append(i.decode("utf-8").split(";"))
    for i in listaPilotos:
        if cpf in i:
            piloto = i
            break
        
    else:
        print("Piloto não encontrado!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    # Exibe os dados do piloto
    print("Dados Básicos:")
    print(f"Nome: {piloto[0]}")
    print(f"CPF: {piloto[1]}")
    print(f"RG: {piloto[2]}")
    print(f"Sexo: {piloto[3]}")
    
    # Pergunta se o usuário deseja excluir o piloto
    print("-"*50)
    print("1 - Excluir")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        listaPilotos.remove(piloto)
        with open("Dados/pilotos.bin", "wb") as file:
            for i in listaPilotos:
                file.write(";".join(i).encode("utf-8"))
                file.write("\n".encode("utf-8"))
        print("Piloto excluído com sucesso!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    elif opção == "0":
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
def ExcluirAeronave():
    print("-"*50)
    print("Excluir Aeronave")
    print("-"*50)
    
    codigo = input("Código: ")
    
    # Busca a aeronave e seus dados
    listaAeronaves = []
    with open("Dados/aviões.bin", "rb") as file:
        for i in file:
            listaAeronaves.append(i.decode("utf-8").split(";"))
    for i in listaAeronaves:
        if codigo in i:
            aeronave = i
            break
        
    else:
        print("Aeronave não encontrada!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    # Exibe os dados da aeronave
    print("Dados Básicos:")
    print(f"Nome: {aeronave[0]}")
    print(f"Codigo: {aeronave[1]}")
    print(f"Modelo: {aeronave[2]}")
    print(f"Companhia: {aeronave[9]}")
    
    # Pergunta se o usuário deseja excluir a aeronave
    print("-"*50)
    print("1 - Excluir")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        listaAeronaves.remove(aeronave)
        with open("Dados/aviões.bin", "wb") as file:
            for i in listaAeronaves:
                file.write(";".join(i).encode("utf-8"))
                file.write("\n".encode("utf-8"))
        print("Aeronave excluída com sucesso!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    elif opção == "0":
        from Módulos.modExclusões import modExclusão
        modExclusão()
        
        
def ExcluirViagem():
    print("-"*50)
    print("Excluir Viagem")
    print("-"*50)
    
    IsADirectoryError = input("ID: ")
    
    # Busca a viagem e seus dados
    listaViagens = []
    with open("Dados/viagens.bin", "rb") as file:
        for i in file:
            listaViagens.append(i.decode("utf-8").split(";"))
    for i in listaViagens:
        if IsADirectoryError in i:
            viagem = i
            break
        
    else:
        print("Viagem não encontrada!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    # Exibe os dados da viagem
    print("Dados Básicos:")
    print(f"ID: {viagem[0]}")
    print(f"Aeronave: {viagem[1]}")
    print(f"Destino: {viagem[3]}")
    print(f"Origem: {viagem[4]}")
    
    # Pergunta se o usuário deseja excluir a viagem
    print("-"*50)
    print("1 - Excluir")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        listaViagens.remove(viagem)
        with open("Dados/viagens.bin", "wb") as file:
            for i in listaViagens:
                file.write(";".join(i).encode("utf-8"))
                file.write("\n".encode("utf-8"))
        print("Viagem excluída com sucesso!")
        from Módulos.modExclusões import modExclusão
        modExclusão()
    
    elif opção == "0":
        from Módulos.modExclusões import modExclusão
        modExclusão()
