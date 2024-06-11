import os
import sys
import time


def PesquisarPassageiroCPF(cpf):
    # Busca o passageiro pelo CPF
    listaPassageiros = []
    with open("Dados/passageiros.bin", "rb") as file:
        for i in file:
            listaPassageiros.append(i.decode("utf-8").split(";")[1])
    # Se encontrar o CPF retorna os dados
    if cpf in listaPassageiros:
        print("Passageiro encontrado!")

        os.system("cls" if os.name == "nt" else "clear")

        # Se encontar o CPF retornar os dados Nome, CPF, RG, Sexo, Data de Nascimento, Telefone, Endereço, Setor, Complemento, Naturalidade, CEP, Cidade, Estado, País
        with open("Dados/passageiros.bin", "rb") as file:
            for i in file:
                if cpf in i.decode("utf-8"):
                    nome = i.decode("utf-8").split(";")[0]
                    cpf = i.decode("utf-8").split(";")[1]
                    rg = i.decode("utf-8").split(";")[2]
                    sexo = i.decode("utf-8").split(";")[3]
                    dataNascimento = i.decode("utf-8").split(";")[4]
                    telefone = i.decode("utf-8").split(";")[5]
                    endereco = i.decode("utf-8").split(";")[6]
                    setor = i.decode("utf-8").split(";")[7]
                    complemento = i.decode("utf-8").split(";")[8]
                    naturalidade = i.decode("utf-8").split(";")[9]
                    cep = i.decode("utf-8").split(";")[10]
                    cidade = i.decode("utf-8").split(";")[11]
                    uf = i.decode("utf-8").split(";")[12]
                    pais = i.decode("utf-8").split(";")[13]

                    print("-"*50)
                    print("Dados do Passageiro com base no CPF")
                    print("-"*50)
                    print(f"Nome: {nome}")
                    print(f"CPF: {cpf}")
                    print(f"RG: {rg}")
                    print(f"Sexo: {sexo}")
                    print(f"Data de Nascimento: {dataNascimento}")
                    print(f"Telefone: {telefone}")
                    print(f"Endereço: {endereco}")
                    print(f"Setor: {setor}")
                    print(f"Complemento: {complemento}")
                    print(f"Naturalidade: {naturalidade}")
                    print(f"CEP: {cep}")
                    print(f"Cidade: {cidade}")
                    print(f"Estado: {uf}")
                    print(f"País: {pais}")
                    print("-"*50)

        time.sleep(5)

        from Módulos.modPesquisa import PesquisarMenu
        PesquisarMenu()

    else:
        print("CPF não encontrado! Digite novamente: ")
        # Exibe os CPFs cadastrados
        listaPassageiros = []
        with open("Dados/passageiros.bin", "rb") as file:
            for i in file:
                listaPassageiros.append(i.decode("utf-8").split(";")[1])
        print("CPFs dos passageiros cadastrados: ")
        print(listaPassageiros)
        os.system(
            f"msg * CPFs dos passageiros cadastrados: {listaPassageiros}")

        from Módulos.modPesquisa import PesquisarMenu
        PesquisarMenu()


def PesquisarAviaoCodigo(codigo):
    # Busca o avião pelo código
    listaAvioes = []
    with open("Dados/aviões.bin", "rb") as file:
        for i in file:
            listaAvioes.append(i.decode("utf-8").split(";")[4])
    # Se encontrar o código retorna os dados
    if codigo in listaAvioes:
        print("Avião encontrado!")
        os.system("cls" if os.name == "nt" else "clear")

        nome = i.decode("utf-8").split(";")[0]
        modelo = i.decode("utf-8").split(";")[1]
        codigo = i.decode("utf-8").split(";")[4]

        print("-"*50)
        print("Dados do Avião com base no Código")
        print("-"*50)
        print(f"Nome: {nome}")
        print(f"Modelo: {modelo}")
        print(f"Código: {codigo}")
        print("-"*50)

        time.sleep(5)

        from Módulos.modPesquisa import PesquisarMenu
        PesquisarMenu()
    else:
        print("Código Não Encontrado!")
        # Exibe os código dos aviões cadastrados
        listaAvioes = []
        with open("Dados/aviões.bin", "rb") as file:
            for i in file:
                listaAvioes.append(i.decode("utf-8").split(";")[4])
        print("Códigos dos aviões cadastrados: ")
        print(listaAvioes)
        os.system(f"msg * Códigos dos aviões cadastrados: {listaAvioes}")

        from Módulos.modPesquisa import PesquisarMenu
        PesquisarMenu()


def PesquisarPilotoCPF(cpf):
    # Busca o piloto pelo CPF
    listaPilotos = []
    with open("Dados/pilotos.bin", "rb") as file:
        for i in file:
            listaPilotos.append(i.decode("utf-8").split(";")[1])

    # Se encontrar o CPF retorna os dados
    if cpf in listaPilotos:
        print("Piloto encontrado!")
        os.system("cls" if os.name == "nt" else "clear")

        # Se encontar o CPF retornar os dados Nome, CPF, RG, Sexo, Data de Nascimento, Telefone, Endereço, Setor, Complemento, Naturalidade, CEP, Cidade, Estado, País
        with open("Dados/pilotos.bin", "rb") as file:
            for i in file:
                if cpf in i.decode("utf-8"):
                    nome = i.decode("utf-8").split(";")[0]
                    cpf = i.decode("utf-8").split(";")[1]
                    cht = i.decode("utf-8").split(";")[2]
                    sexo = i.decode("utf-8").split(";")[3]
                    dataNascimento = i.decode("utf-8").split(";")[4]
                    telefone = i.decode("utf-8").split(";")[5]
                    endereco = i.decode("utf-8").split(";")[6]
                    setor = i.decode("utf-8").split(";")[7]
                    complemento = i.decode("utf-8").split(";")[8]
                    numerocasa = i.decode("utf-8").split(";")[9]
                    naturalidade = i.decode("utf-8").split(";")[10]
                    cep = i.decode("utf-8").split(";")[11]
                    cidade = i.decode("utf-8").split(";")[12]
                    uf = i.decode("utf-8").split(";")[13]
                    pais = i.decode("utf-8").split(";")[14]

                    print("-"*50)
                    print("Dados do Piloto com base no CPF")
                    print("-"*50)
                    print(f"Nome: {nome}")
                    print(f"CPF: {cpf}")
                    print(f"CHT: {cht}")

                    if sexo == "M":
                        sexo = "Masculino"
                    elif sexo == "F":
                        sexo = "Feminino"

                    print(f"Sexo: {sexo}")
                    print(f"Data de Nascimento: {dataNascimento}")
                    print(f"Telefone: {telefone}")
                    print(f"Endereço: {endereco}")
                    print(f"Setor: {setor}")
                    print(f"Complemento: {complemento}")
                    print(f"Número da Casa: {numerocasa}")
                    print(f"Naturalidade: {naturalidade}")
                    print(f"CEP: {cep}")
                    print(f"Cidade: {cidade}")
                    print(f"Estado: {uf}")
                    print(f"País: {pais}")
                    print("-"*50)

                    from Módulos.modPesquisa import PesquisarMenu
                    PesquisarMenu()

                else:
                    print("CPF não encontrado! Digite novamente: ")
                    # Exibe os CPFs cadastrados
                    listaPilotos = []
                    with open("Dados/pilotos.bin", "rb") as file:
                        for i in file:
                            listaPilotos.append(
                                i.decode("utf-8").split(";")[1])
                    print("CPFs dos pilotos cadastrados: ")
                    print(listaPilotos)
                    os.system(
                        f"msg * CPFs dos pilotos cadastrados: {listaPilotos}")

                    from Módulos.modPesquisa import PesquisarMenu
                    PesquisarMenu()


def PesquisarViagemID(id):
    # Busca a viagem pelo ID
    listaViagens = []
    with open("Dados/viagens.bin", "rb") as file:
        for i in file:
            listaViagens.append(i.decode("utf-8").split(";")[0])

    # Se encontrar o ID retorna os dados
    if id in listaViagens:
        print("Viagem encontrada!")
        os.system("cls" if os.name == "nt" else "clear")

        # Se encontar o ID retornar os dados ID, Aeronave, Piloto, Destino, Origem, Data, Hora, Classe Executiva, Classe Econômica
        with open("Dados/viagens.bin", "rb") as file:
            for i in file:
                if id in i.decode("utf-8"):
                    id = i.decode("utf-8").split(";")[0]
                    aeronave = i.decode("utf-8").split(";")[1]
                    piloto = i.decode("utf-8").split(";")[2]
                    destino = i.decode("utf-8").split(";")[3]
                    origem = i.decode("utf-8").split(";")[4]
                    data = i.decode("utf-8").split(";")[5]
                    hora = i.decode("utf-8").split(";")[6]
                    classeExecutiva = i.decode("utf-8").split(";")[7]
                    classeEconomica = i.decode("utf-8").split(";")[8]
                    primeiraClasse = i.decode("utf-8").split(";")[9]

                    print("-"*50)
                    print("Dados da Viagem com base no ID")
                    print("-"*50)
                    print(f"ID: {id}")
                    print(f"Aeronave: {aeronave}")
                    print(f"Piloto: {piloto}")
                    print(f"Destino: {destino}")
                    print(f"Origem: {origem}")
                    print(f"Data: {data}")
                    print(f"Hora: {hora}")
                    print(f"Qtd. Acentos Executiva: {classeExecutiva}")
                    print(f"Qtd. Acentos Econômica: {classeEconomica}")
                    print(f"Qtd. Acentos 1º Classe: {primeiraClasse}")
                    print("-"*50)

                time.sleep(5)

                from Módulos.modPesquisa import PesquisarMenu
                PesquisarMenu()
    else:
        print("ID Não Encontrado!")
        # Exibe os IDs das viagens cadastradas
        listaViagens = []
        with open("Dados/viagens.bin", "rb") as file:
            for i in file:
                listaViagens.append(i.decode("utf-8").split(";")[0])
        print("IDs das viagens cadastradas: ")
        print(listaViagens)
        os.system(f"msg * IDs das viagens cadastradas: {listaViagens}")

        from Módulos.modPesquisa import PesquisarMenu
        PesquisarMenu()
