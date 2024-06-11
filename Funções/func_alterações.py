def AlterarPassageiro():
    print("-"*50)
    print("Alteração de Passageiro")
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
        from Módulos.modAlterações import modAlterações
        modAlterações()
    
    # Exibe os dados do passageiro
    print("Dados Básicos:")
    print(f"Nome: {passageiro[0]}")
    print(f"CPF: {passageiro[1]}")
    print(f"RG: {passageiro[2]}")
    print(f"Sexo: {passageiro[3]}")
    print(f"Data de Nascimento: {passageiro[4]}")

    
    # Pergunta qual dado o usuário deseja alterar
    print("-"*50)
    print("1 - Nome")
    print("2 - CPF")
    print("3 - RG")
    print("4 - Sexo")
    print("5 - Data de Nascimento")
    print("6 - Alterar Todos os Dados")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        passageiro[0] = input("Nome: ")
    elif opção == "2":
        passageiro[1] = input("CPF: ")
    elif opção == "3":
        passageiro[2] = input("RG: ")
    elif opção == "4":
        passageiro[3] = input("Sexo: ")
    elif opção == "5":
        passageiro[4] = input("Data de Nascimento: ")
    elif opção == "6":
        passageiro[0] = input("Nome: ")
        passageiro[1] = input("CPF: ")
        passageiro[2] = input("RG: ")
        passageiro[3] = input("Sexo: ")
        passageiro[4] = input("Data de Nascimento: ")
        passageiro[5] = input("Telefone: ")
        passageiro[6] = input("Endereço: ")
        passageiro[7] = input("Setor: ")
        passageiro[8] = input("Complemento: ")
        passageiro[9] = input("Naturalidade: ")
        passageiro[10] = input("CEP: ")
        passageiro[11] = input("Cidade: ")
        passageiro[12] = input("UF: ")
        passageiro[13] = input("País: ")
    elif opção == "0":
        from Módulos.modAlterações import modAlterações
        modAlterações()
        
    # Salva os dados
    with open("Dados/passageiros.bin", "wb") as file:
        for i in listaPassageiros:
            file.write(";".join(i).encode("utf-8"))
            file.write("\n".encode("utf-8"))
            
    # Printa confirmação de alteração
    print("Alteração realizada com sucesso!")
    
    # Volta para o menu de alterações
    from Módulos.modAlterações import modAlterações
    modAlterações()
    
def modAlterarPiloto():
    print("-"*50)
    print("Alteração de Piloto")
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
        from Módulos.modAlterações import modAlterações
        modAlterações()
    
    # Exibe os dados do piloto
    print("Dados Básicos:")
    print(f"Nome: {piloto[0]}")
    print(f"CPF: {piloto[1]}")
    print(f"RG: {piloto[2]}")
    print(f"Sexo: {piloto[3]}")
    print(f"Data de Nascimento: {piloto[4]}")
    print(f"Telefone: {piloto[5]}")
    print(f"Endereço: {piloto[6]}")
    print(f"Setor: {piloto[7]}")
    print(f"Complemento: {piloto[8]}")
    print(f"Naturalidade: {piloto[9]}")
    print(f"CEP: {piloto[10]}")
    print(f"Cidade: {piloto[11]}")
    print(f"UF: {piloto[12]}")
    print(f"País: {piloto[13]}")
    
    # Pergunta qual dado o usuário deseja alterar
    print("-"*50)
    print("1 - Nome")
    print("2 - CPF")
    print("3 - RG")
    print("4 - Sexo")
    print("5 - Data de Nascimento")
    print("6 - Alterar Todos os Dados")
    print("0 - Voltar")
    
    opção = input("Opção: ")
    
    if opção == "1":
        piloto[0] = input("Nome: ")
    elif opção == "2":
        piloto[1] = input("CPF: ")
    elif opção == "3":
        piloto[2] = input("RG: ")
        
    elif opção == "4":
        piloto[3] = input("Sexo: ")
    elif opção == "5":
        piloto[4] = input("Data de Nascimento: ")
    elif opção == "6":
        piloto[0] = input("Nome: ")
        piloto[1] = input("CPF: ")
        piloto[2] = input("RG: ")
        piloto[3] = input("Sexo: ")
        piloto[4] = input("Data de Nascimento: ")
        piloto[5] = input("Telefone: ")
        piloto[6] = input("Endereço: ")
        piloto[7] = input("Setor: ")
        piloto[8] = input("Complemento: ")
        piloto[9] = input("Naturalidade: ")
        piloto[10] = input("CEP: ")
        piloto[11] = input("Cidade: ")
        piloto[12] = input("UF: ")
        piloto[13] = input("País: ")
    elif opção == "0":
        from Módulos.modAlterações import modAlterações
        modAlterações()
        
    # Salva os dados
    with open("Dados/pilotos.bin", "wb") as file:
        for i in listaPilotos:
            file.write(";".join(i).encode("utf-8"))
            file.write("\n".encode("utf-8"))
        
    # Printa confirmação de alteração
    print("Alteração realizada com sucesso!")
    
    # Volta para o menu de alterações
    from Módulos.modAlterações import modAlterações
    modAlterações()
            
def modAlterarAeronave():
    print("-"*50)
    print("Alteração de Aeronave")
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
        from Módulos.modAlterações import modAlterações
        modAlterações()
       
    
    # Exibe os dados da aeronave
    print("Dados Básicos:")
    print(f"Nome: {aeronave[0]}")
    print(f"Modelo: {aeronave[1]}")
    print(f"Data Fabricação: {aeronave[2]}")
    print(f"Anos de Serviço: {aeronave[3]}")
    print(f"Nº Registro: {aeronave[4]}")
    
    # Pergunta qual dado o usuário deseja alterar
    print("-"*50)
    print("1 - Nome")
    print("2 - Modelo")
    print("3 - Data de Fabricação")
    print("4 - Anos de Serviço")
    print("5 - Nº Registro")
    print("6 - Alterar Todos os Dados")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        aeronave[0] = input("Nome: ")
    elif opção == "2":
        aeronave[1] = input("Modelo: ")
    elif opção == "3":
        aeronave[2] = input("Data de Fabricação: ")
    elif opção == "4":
        aeronave[3] = input("Anos de Serviço: ")
    elif opção == "5":
        aeronave[4] = input("Nº Registro: ")
    elif opção == "6":
        aeronave[0] = input("Nome: ")
        aeronave[1] = input("Modelo: ")
        aeronave[2] = int(input("Data de Fabricação: *Apenas Números*"))
        aeronave[3] = int(input("Anos de Serviço: *Apenas Números*"))
        aeronave[4] = input("Nº Registro: ")
        aeronave[5] = input("Fabricante: ")
        aeronave[6] = int(input("Assentos: *Apenas Números*"))
        aeronave[7] = float(input("Comprimento: *Apenas Números*"))
        aeronave[8] = float(input("Largura: *Apenas Números*"))
        aeronave[9] = input("Companhia: ")
    elif opção == "0":
        from Módulos.modAlterações import modAlterações
        modAlterações()
        
    # Salva os dados
    with open("Dados/aeronaves.bin", "wb") as file:
        for i in listaAeronaves:
            file.write(";".join(i).encode("utf-8"))
            file.write("\n".encode("utf-8"))
            
    # Printa confirmação de alteração
    print("Alteração realizada com sucesso!")
    
    # Volta para o menu de alterações
    from Módulos.modAlterações import modAlterações
    modAlterações()
            
def modAlterarViagem():
    print("-"*50)
    print("Alteração de Viagem")
    print("-"*50)
    
    id = input("ID: ")
    
    # Busca a viagem e seus dados
    listaViagens = []
    with open("Dados/viagens.bin", "rb") as file:
        for i in file:
            listaViagens.append(i.decode("utf-8").split(";"))
    for i in listaViagens:
        if id in i:
            viagem = i
            break
    else:
        print("Viagem não encontrada!")
        from Módulos.modAlterações import modAlterações
        modAlterações()
        
    
    # Exibe os dados da viagem
    print("Dados Básicos:")
    print(f"Código: {viagem[0]}")
    print(f"Avião: {viagem[1]}")
    print(f"Piloto: {viagem[2]}")
    print(f"Destino: {viagem[3]}")
    print(f"Origem: {viagem[4]}")
    print(f"Data: {viagem[5]}")
    print(f"Hora: {viagem[6]}")
    
    # Pergunta qual dado o usuário deseja alterar
    print("-"*50)
    print("1 - Avião")
    print("2 - Piloto")
    print("3 - Destino")
    print("4 - Origem")
    print("5 - Alterar Todos os Dados")
    print("0 - Voltar")
    print("-"*50)
    
    opção = input("Opção: ")
    
    if opção == "1":
        viagem[1] = input("Avião: ")
    elif opção == "2":
        viagem[2] = input("Piloto: ")
    elif opção == "3":
        viagem[3] = input("Destino: ")
    elif opção == "4":
        viagem[4] = input("Origem: ")
    elif opção == "5":
        viagem[1] = input("Avião: ")
        viagem[2] = input("Piloto: ")
        viagem[3] = input("Destino: ")
        viagem[4] = input("Origem: ")
        viagem[5] = input("Data: ")
        viagem[6] = input("Hora: ")
        viagem[10] = float(input("Valor Executiva: "))
        viagem[11] = float(input("Valor Econômica: "))
        viagem[12] = float(input("Valor Primeira Classe: "))
        
    elif opção == "0":
        from Módulos.modAlterações import modAlterações
        modAlterações()
        
    # Salva os dados
    with open("Dados/viagens.bin", "wb") as file:
        for i in listaViagens:
            file.write(";".join(i).encode("utf-8"))
            file.write("\n".encode("utf-8"))
        
    # Printa confirmação de alteração
    print("Alteração realizada com sucesso!")
    
    # Volta para o menu de alterações
    from Módulos.modAlterações import modAlterações
    modAlterações()