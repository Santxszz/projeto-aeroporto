# Importações
import os
import sys
import time
import socket
import requests
import colorama
from validate_docbr import CPF

# Registros
from Registros.regPassageiros import regPassageiros

# Módulos
import Módulos.modCadastros as modCadastros

# Funções Globais
from Formatações.funcFormatações import formatar_data
from Funções.func_checarCpf import func_checarCpf


def func_cadPassageiros():
    passageiros = []

    print("-" * 50)
    print("Cadastro de Passageiros".center(50))
    print("")
    print(f"ATENÇÃO:  O CPF só pode ser usado 1 vez. ")
    print(f"ATENÇÃO: Para voltar tecle 0 no campo NOME.")
    print("-" * 50)
    print("")

    nome = input("Nome: ")

    if nome == "0":
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        modCadastros.modCadastros()
    elif nome == "":
        print("Nome inválido!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        nome = input("Nome: ")

    # Verifica se o CPF é válido usando a biblioteca validate_docbr
    cpf = input("CPF: ")
    while not CPF().validate(cpf):
        print("CPF inválido. Por favor, digite novamente.")
        cpf = input("Digite o seu CPF: ")

    # Verifica se o CPF já foi cadastrado no arquivo passageiros.bin
    while func_checarCpf(cpf) == True:
        print("CPF já cadastrado. Por favor, digite novamente.")
        cpf = input("Digite o seu CPF: ")
        while not CPF().validate(cpf):
            print("CPF inválido. Por favor, digite novamente.")
            cpf = input("Digite o seu CPF: ")
        if func_checarCpf(cpf) == False:
            break
        else:
            continue


    # Transforma o CPF para o padrão 000.000.000-00
    validador = CPF()
    cpf_formatado = validador.mask(cpf)

    rg = int(input("RG: "))
    sexo = input("Sexo: (M ou F)")
    
    # Transforma o sexo para maiúsculo
    sexo = sexo.upper()

    # Se o sexo for diferente de "M" ou "F" ele entra no loop
    while sexo != "M" and sexo != "F":
        print("Sexo inválido!")
        sexo = input("Sexo: (M ou F)")

    datanascimento = input("Data de Nascimento: ")
    
    # Transforma a data de nascimento para o padrão 00/00/0000
    data_formatada = formatar_data(datanascimento)

    telefone = int(input("Nº Telefone: "))
    endereco = input("Endereço: ")
    setor = input("Setor: ")
    complemento = input("Complemento: ")
    naturalidade = input("Naturalidade: ")
    cep = int(input("CEP: "))
    cidade = input("Cidade: ")
    uf = input("Estado: ")
    pais = input("País: ")

    os.system("cls" if os.name == "nt" else "clear")

    passageiros.append(
        regPassageiros(
            nome=nome,
            cpf=cpf,
            rg=rg,
            sexo=sexo,
            dataNascimento=data_formatada,
            telefone=telefone,
            endereco=endereco,
            setor=setor,
            complemento=complemento,
            naturalidade=naturalidade,
            cep=cep,
            cidade=cidade,
            uf=uf,
            pais=pais,
        )
    )

    dados = f"Nome: {nome}\nCPF: {cpf}\nRG: {rg}\nSexo: {sexo}\nData de Nascimento: {data_formatada}\nTelefone: {telefone}\nEndereço: {
        endereco}\nSetor: {setor}\nComplemento: {complemento}\nNaturalidade: {naturalidade}\nCEP: {cep}\nCidade: {cidade}\nEstado: {uf}\nPaís: {pais}"
    func_cadPassageirosLog(dados)

    # Atualiza no arquivo de passageiros
    with open("Dados/passageiros.bin", "a", encoding="utf-8") as f:
        for i in passageiros:
            f.write(
                f"{i.nome};{i.cpf};{i.rg};{i.sexo};{i.dataNascimento};{i.telefone};{i.endereco};{
                    i.setor};{i.complemento};{i.naturalidade};{i.cep};{i.cidade};{i.uf};{i.pais}\n"
            )
            f.close()

    print("Passageiro cadastrado com sucesso!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)
    modCadastros.modCadastros()


def func_cadPassageirosLog(dados):
    # Variáveis locais
    pc = os.getlogin()
    sistema = sys.platform
    hora = time.strftime("%H:%M:%S")
    data = time.strftime("%d/%m/%Y")
    ip = requests.get("https://api.ipify.org").text
    ip_pc = socket.gethostbyname(socket.gethostname())
    dados = dados

    # Cria/Escreve o log de cadastro de passageiros
    with open("Logs/Cadastro de Passageiros.log", "a", encoding="utf-8") as f:
        f.write("-" * 50 + "\n")
        f.write(f"PC: {pc}\n")
        f.write(f"Sistema: {sistema}\n")
        f.write(f"IP: {ip}\n")
        f.write(f"IP PC: {ip_pc}\n")
        f.write(f"Data: {data}\n")
        f.write(f"Hora: {hora}\n")
        f.write(f"Dados: {dados}\n")
        f.write("-" * 50 + "\n")
        f.close()

    # Envia o log para o whatsapp dos administradores usando InfoBIP
    BASE_URL = "https://k29j98.api.infobip.com"
    API_KEY = "eaa16d409b7425ab9016742a8b982478-cc34d0da-f10f-49e1-806b-de9b253ea6fe"

    SENDER = "447860099299"
    RECIPIENT = "5562984201618"

    MESSAGE_TEXT = f"LOG - LOGIN\nPC: {pc}\nSistema: {sistema}\nIP: {
        ip}\nIP PC: {ip_pc}\nData: {data}\nHora: {hora}\nDados: {dados}"

    def send_message():
        url = f"{BASE_URL}/sms/2/text/single"
        payload = {"from": SENDER, "to": RECIPIENT, "text": MESSAGE_TEXT}
        headers = {"Authorization": f"App {API_KEY}"}
        response = requests.post(url, json=payload, headers=headers)
        print(response.json())

    # send_message()



