import os,sys,time,datetime

from Registros.regViagens import RegViagens


def CadastrarViagem():
    RegViagens.id = int(input("ID: "))
    
    # Verifica se o ID já existe
    listaViagens = []
    idsViagens = []
    
    with open("Dados/viagens.bin", "rb") as file:
        for i in file:
            if i.strip():
                ids_lidos = i.decode("utf-8").strip().split(";")[0]
                idsViagens.append(ids_lidos)

    if RegViagens.id in listaViagens:
        print("ID já cadastrado! Tente outro ID.")
        CadastrarViagem()
    
    # Puxa as aeronaves cadastradas
    listaAeronaves = []
    with open("Dados/aviões.bin", "rb") as file:
        for i in file:
            listaAeronaves.append(i.decode("utf-8").split(";")[0])
    print("Aeronaves Cadastradas: {}".format(listaAeronaves, end= "\n\n"))
    RegViagens.aeronave = input("Aeronave: ")
    
    # Verifica se a aeronave existe
    listaAeronaves = []
    listaVagas = []
    with open("Dados/aviões.bin", "rb") as file:
        for i in file:
            listaAeronaves.append(i.decode("utf-8").split(";")[0])
            listaVagas.append(i.decode("utf-8").split(";")[6])
    if RegViagens.aeronave in listaAeronaves:
        print("Aeronave encontrada!")
        vagas = listaVagas[listaAeronaves.index(RegViagens.aeronave)]
        
    else:
        print("Aeronave não encontrada!")
        # Exibe as aeronaves cadastradas
        
        os.system("cls" if os.name == "nt" else "clear")
        
        listaAeronaves = []
        with open("Dados/aviões.bin", "rb") as file:
            for i in file:
                listaAeronaves.append(i.decode("utf-8").split(";")[0])
        print("Aeronaves cadastradas: ")
        print(listaAeronaves)
        os.system(f"msg * Aeronaves cadastradas: {listaAeronaves}")
        CadastrarViagem()
    
    # Puxa os pilotos cadastrados
    listaPilotos = []
    with open("Dados/pilotos.bin", "rb") as file:
        for i in file:
            listaPilotos.append(i.decode("utf-8").split(";")[0])
    print("Pilotos Cadastrados: {}".format(*listaPilotos, end= "\n\n"))
    RegViagens.piloto = input("Piloto: ")
    
    # Veirifica se o piloto existe
    listaPilotos = []
    with open("Dados/pilotos.bin", "rb") as file:
        for i in file:
            listaPilotos.append(i.decode("utf-8").split(";")[0])
    if RegViagens.piloto in listaPilotos:
        print("Piloto encontrado!")
    else:
        print("Piloto não encontrado!")
        
        os.system("cls" if os.name == "nt" else "clear")
        
        # Exibe os pilotos cadastrados
        listaPilotos = []
        with open("Dados/pilotos.bin", "rb") as file:
            for i in file:
                listaPilotos.append(i.decode("utf-8").split(";")[0])
        print("Pilotos cadastrados: ")
        print(listaPilotos)
        os.system(f"msg * Pilotos cadastrados: {listaPilotos}")
        CadastrarViagem()
    
    
    RegViagens.destino = input("Destino: ")
    RegViagens.origem = input("Origem: ")
    RegViagens.data = input("Data: ")
    RegViagens.hora = input("Hora: ")
    
    
    # print(vagas)
    
    print("Assentos Disponíveis: ", vagas)
    RegViagens.classeExecutiva = int(input("Assentos Classe Executiva: "))
    vagas = int(vagas) - RegViagens.classeExecutiva
    
    print("Assentos Disponíveis: ", vagas)
    RegViagens.classeEconomica = int(input("Assentos Classe Econômica: "))
    vagas = int(vagas) - RegViagens.classeEconomica
    
    print("Assentos Disponíveis: ", vagas)
    RegViagens.primeiraClasse = int(input("Assentos Primeira Classe: "))
    vagas = int(vagas) - RegViagens.primeiraClasse
    
    RegViagens.valorExecutiva = float(input("Valor Executiva: "))
    RegViagens.valorEconomica = float(input("Valor Econômica: "))
    RegViagens.valorPrimeira = float(input("Valor Primeira: "))
    
    # Salvando os dados no arquivo
    with open("Dados/viagens.bin", "a", encoding="utf-8") as file:
        file.write(f"{RegViagens.id};{RegViagens.aeronave};{RegViagens.piloto};{RegViagens.destino};{RegViagens.origem};{RegViagens.data};{RegViagens.hora};{RegViagens.classeExecutiva};{RegViagens.classeEconomica};{RegViagens.primeiraClasse};{RegViagens.valorExecutiva};{RegViagens.valorEconomica};{RegViagens.valorPrimeira}\n")
        
    # Salvando os dados no log
    with open("Logs/cadViagens.log", "a", encoding="utf-8") as f:
        f.write('-' * 50 + '\n')
        f.write(f"ID: {RegViagens.id}\n")
        f.write(f"Aeronave: {RegViagens.aeronave}\n")
        f.write(f"Piloto: {RegViagens.piloto}\n")
        f.write(f"Destino: {RegViagens.destino}\n")
        f.write(f"Origem: {RegViagens.origem}\n")
        f.write(f"Data: {RegViagens.data}\n")
        f.write(f"Hora: {RegViagens.hora}\n")
        f.write(f"Classe Executiva: {RegViagens.classeExecutiva}\n")
        f.write(f"Classe Econômica: {RegViagens.classeEconomica}\n")
        f.write(f"Primeira Classe: {RegViagens.primeiraClasse}\n")
        f.write(f"Valor Executiva: {RegViagens.valorExecutiva}\n")
        f.write(f"Valor Econômica: {RegViagens.valorEconomica}\n")
        f.write(f"Valor Primeira: {RegViagens.valorPrimeira}\n")
        f.write('-' * 50 + '\n')
        
    print("Viagem cadastrada com sucesso!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)
    from Módulos.modCadastros import modCadastros
    modCadastros()