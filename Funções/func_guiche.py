from tabulate import tabulate
import os, random


def Vendas():
    cpf = input("CPF: ")

    # Verifica se o CPF já está cadastrado
    listaCPF = []
    with open("Dados/passageiros.bin", "r") as arquivo:
        for linha in arquivo:
            if linha.strip():
                linhacpf = linha.strip().split(";")[1]
                listaCPF.append(linhacpf)
    if cpf in listaCPF:
        print("")
    else:
        print("CPF não cadastrado!")
        from Módulos.modGuiche import Guiche
        Guiche()

    # Puxa as viagens
    listaViagens = []
    with open("Dados/viagens.bin", "r") as arquivo:
        for linha in arquivo:
            listaViagens.append(linha.split(";"))

    header = ["Código", "Aeronave", "Piloto", "Destino", "Origem",
              "Data", "Horário", "V. E", "V. EC", "V. 1C", "R$", "R$", "R$"]

    print(tabulate(listaViagens, tablefmt="row", headers=header))

    # Pergunta qual viagem
    print("")
    código = input("Viagem: ")
    
    

    # Verifica se o código existe
    listaCódigo = []
    with open("Dados/viagens.bin", "r") as arquivo:
        for linha in arquivo:
            listaCódigo.append(linha.split(";")[0])
            vagaExecutiva = linha.split(";")[7]
            vagaEconomica = linha.split(";")[8]
            vaga1Classe = linha.split(";")[9]
            valorExecutiva = linha.split(";")[10]
            valorEconomica = linha.split(";")[11]
            valor1Classe = linha.split(";")[12]
    if código in listaCódigo:
        print("Selecione a Clase")
        print("1 - Executiva")
        print("2 - Econômica")
        print("3 - Primeira Classe")
        print("")
        classe = input("Classe: ")

        if classe == "1":
            os.system("cls" if os.name == "nt" else "clear")
            print("Valor: R$", valorExecutiva)
            print("Vagas Disponíveis: ", vagaExecutiva)
            print("")
            quantidade = input("Quantidade: ")
            if int(quantidade) > int(vagaExecutiva):
                print("Quantidade inválida!")
                from Módulos.modGuiche import Guiche
                Guiche()
            print("")
            print("Total: R$", float(valorExecutiva) * float(quantidade))
            print("")
            print("Confirmar?")
            print("1 - Sim")
            print("2 - Não")
            print("")
            confirmar = input("Opção: ")

            if confirmar == "1":
                
                numeraçãoVenda = random.randint(1000, 9999)
                print("")
                print(f"Venda Nº {numeraçãoVenda} foi realizada com sucesso!")
                print(f"Comprador: {cpf}")
                print(f"Viagem: {código}")
                print(f"Quantidade: {quantidade}")
                print("")
                # Altera o número de vagas do arquivo viagens
                with open("Dados/viagens.bin", "r") as arquivo:
                    linhas = arquivo.readlines()
                with open("Dados/viagens.bin", "w") as arquivo:
                    for linha in linhas:
                        if linha.split(";")[0] == código:
                            linha = linha.replace(vagaExecutiva, str(
                                int(vagaExecutiva) - int(quantidade)))
                        arquivo.write(linha)
                    
                    
                # Escreve a venda
                with open("Dados/vendas.bin", "a") as arquivo:
                    arquivo.write(f"EXECUTIVA;{numeraçãoVenda};{código};{cpf};{quantidade};{valorExecutiva}\n")

                from Módulos.modGuiche import Guiche
                Guiche()

        if classe == "2":
            os.system("cls" if os.name == "nt" else "clear")
            print("Valor: R$", valorEconomica)
            print("Vagas Disponíveis: ", vagaEconomica)
            print("")
            quantidade = input("Quantidade: ")
            if int(quantidade) > int(vagaEconomica):
                print("Quantidade inválida!")
                from Módulos.modGuiche import Guiche
                Guiche()
            print("")
            print("Total: R$", float(valorEconomica) * float(quantidade))
            print("")
            print("Confirmar?")
            print("1 - Sim")
            print("2 - Não")
            print("")
            confirmar = input("Opção: ")

            if confirmar == "1":
                numeraçãoVenda = random.randint(1000, 9999)
                print("")
                print(f"Venda Nº {numeraçãoVenda} foi realizada com sucesso!")
                print(f"Comprador: {cpf}")
                print(f"Viagem: {código}")
                print(f"Quantidade: {quantidade}")
                print("")
                # Altera o número de vagas
                with open("Dados/viagens.bin", "r") as arquivo:
                    linhas = arquivo.readlines()
                with open("Dados/viagens.bin", "w") as arquivo:
                    for linha in linhas:
                        if linha.split(";")[0] == código:
                            linha = linha.replace(vagaEconomica, str(
                                int(vagaEconomica) - int(quantidade)))
                        arquivo.write(linha)
                # Escreve a venda
                with open("Dados/vendas.bin", "a") as arquivo:
                    arquivo.write(f"ECONOMICA;{numeraçãoVenda};{código};{cpf};{quantidade};{valorEconomica}\n")

                from Módulos.modGuiche import Guiche
                Guiche()

        if classe == "3":
            os.system("cls" if os.name == "nt" else "clear")
            print("Valor: R$", valor1Classe)
            print("Vagas Disponíveis: ", vaga1Classe)
            print("")
            quantidade = input("Quantidade: ")
            if int(quantidade) > int(vaga1Classe):
                print("Quantidade inválida!")
                from Módulos.modGuiche import Guiche
                Guiche()
            print("")
            print("Total: R$", float(valor1Classe) * float(quantidade))
            print("")
            print("Confirmar?")
            print("1 - Sim")
            print("2 - Não")
            print("")
            confirmar = input("Opção: ")

            if confirmar == "1":
                numeraçãoVenda = random.randint(1000, 9999)
                print("")
                print(f"Venda Nº {numeraçãoVenda} foi realizada com sucesso!")
                print(f"Comprador: {cpf}")
                print(f"Viagem: {código}")
                print(f"Quantidade: {quantidade}")
                print("")
                # Altera o número de vagas
                with open("Dados/viagens.bin", "r") as arquivo:
                    linhas = arquivo.readlines()
                with open("Dados/viagens.bin", "w") as arquivo:
                    for linha in linhas:
                        if linha.split(";")[0] == código:
                            linha = linha.replace(vaga1Classe, str(
                                int(vaga1Classe) - int(quantidade)))
                        arquivo.write(linha)
                # Escreve a venda
                with open("Dados/vendas.bin", "a") as arquivo:
                    arquivo.write(f"1CLASSE;{numeraçãoVenda};{código};{cpf};{quantidade};{valor1Classe}\n")

                from Módulos.modGuiche import Guiche
                Guiche()

    else:
        from Módulos.modGuiche import Guiche
        Guiche()
