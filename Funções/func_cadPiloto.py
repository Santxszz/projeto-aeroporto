from Registros.regPiloto import regPiloto
from validate_docbr import CPF
from Funções.func_checarCpf import ChecarCPFPiloto

import os, sys, time, random, requests, socket

def cadastrarPiloto():
    regPiloto.nome = input("Nome: ")
    regPiloto.cpf = input("CPF: ")
    while not CPF().validate(regPiloto.cpf):
        print("CPF inválido. Por favor, digite novamente.")
        regPiloto.cpf = input("Digite o seu CPF: ")
        
    if ChecarCPFPiloto(regPiloto.cpf) == True:
        print("CPF Já Cadastrado")
        
    while ChecarCPFPiloto(regPiloto.cpf) == True:
        regPiloto.cpf = input("CPF: ")
        if ChecarCPFPiloto(regPiloto.cpf) == False:
            break
        
    regPiloto.rg = int(input("RG: "))
    regPiloto.cht = int(input("CHT: "))
    regPiloto.sexo = input("Sexo (M ou F): ")
    
    sexo = regPiloto.sexo.upper()
    
    while sexo != "M" and sexo != "F":
        print("Sexo inválido. Por favor, digite novamente.")
        regPiloto.sexo = input("Sexo: ")
        
    regPiloto.dataNascimento = input("Data de Nascimento: ")
    regPiloto.telefone = input("Telefone: ")
    regPiloto.endereco = input("Endereço: ")
    regPiloto.setor = input("Setor: ")
    regPiloto.complemento = input("Complemento: ")
    regPiloto.numerocasa = input("Número da Casa: ")
    regPiloto.naturalidade = input("Naturalidade: ")
    regPiloto.cep = input("CEP: ")
    regPiloto.cidade = input("Cidade: ")
    regPiloto.uf = input("Estado: ")
    regPiloto.pais = input("País: ")
    
    # Checa se todos os campos foram preenchidos
    if regPiloto.nome == "" or regPiloto.cpf == "" or regPiloto.rg == "" or regPiloto.cht == "" or regPiloto.sexo == "" or regPiloto.dataNascimento == "" or regPiloto.telefone == "" or regPiloto.endereco == "" or regPiloto.setor == "" or regPiloto.complemento == "" or regPiloto.numerocasa == "" or regPiloto.naturalidade == "" or regPiloto.cep == "" or regPiloto.cidade == "" or regPiloto.uf == "" or regPiloto.pais == "":
        print("Todos os campos devem ser preenchidos!")
        cadastrarPiloto()

    # Salva os dados no arquivo pilotos.bin
    with open("Dados/pilotos.bin", "ab") as file:
        file.write(f"{regPiloto.nome};{regPiloto.cpf};{regPiloto.rg};{regPiloto.cht};{regPiloto.sexo};{regPiloto.dataNascimento};{regPiloto.telefone};{regPiloto.endereco};{regPiloto.setor};{regPiloto.complemento};{regPiloto.numerocasa};{regPiloto.naturalidade};{regPiloto.cep};{regPiloto.cidade};{regPiloto.uf};{regPiloto.pais}\n".encode("utf-8"))
        file.close()
    
    print("Piloto cadastrado com sucesso!")
    
    pc = os.getlogin()
    sistema = sys.platform
    hora = time.strftime("%H:%M:%S")
    data = time.strftime("%d/%m/%Y")
    ip = requests.get("https://api.ipify.org").text
    ip_pc = socket.gethostbyname(socket.gethostname())
    dados = regPiloto()

    # Cria/Escreve o log de cadastro de passageiros
    with open("Logs/Cadastro_de_Pilotos.log", "a", encoding="utf-8") as f:
        f.write("-" * 50 + "\n")
        f.write(f"PC: {pc}\n")
        f.write(f"Sistema: {sistema}\n")
        f.write(f"IP: {ip}\n")
        f.write(f"IP PC: {ip_pc}\n")
        f.write(f"Data: {data}\n")
        f.write(f"Hora: {hora}\n")
        f.write(f"Dados: {regPiloto}\n")
        f.write("-" * 50 + "\n")
        f.close()

    # Envia o log para o whatsapp dos administradores usando InfoBIP
    BASE_URL = "https://k29j98.api.infobip.com"
    API_KEY = "eaa16d409b7425ab9016742a8b982478-cc34d0da-f10f-49e1-806b-de9b253ea6fe"

    SENDER = "447860099299"
    RECIPIENT = "5562984201618"

    MESSAGE_TEXT = f"LOG - CAD. PILOTO\nPC: {pc}\nSistema: {sistema}\nIP: {
        ip}\nIP PC: {ip_pc}\nData: {data}\nHora: {hora}\nDados: {dados}"

    def send_message():
        url = f"{BASE_URL}/sms/2/text/single"
        payload = {"from": SENDER, "to": RECIPIENT, "text": MESSAGE_TEXT}
        headers = {"Authorization": f"App {API_KEY}"}
        response = requests.post(url, json=payload, headers=headers)
        print(response.json())

    send_message()
    
    # Volta ao MENU
    from Módulos.modCadastros import modCadastros
    modCadastros()