# Importações
import datetime, time, os, sys, keyboard, socket

# Módulos
import Módulos.modCadastros as modCadastros

# Registros
from Registros.regAviões import RegAviao

# Funções
from Funções.func_checarRegistro import func_checarRegistro

def func_cadAvião():
    avioes = []

    # Dados Aeronave
    nome = input('Digite o nome do avião: ')
    modelo = input('Digite o modelo do avião: ')
    datafabri = int(input('Digite o ano em que o avião foi fabricado: '))
    anoservi = int(input('Digite o ano em que o avião entrou em serviço: '))
    
    if datafabri > anoservi:
        print("Ano de fabricação não pode ser maior que o ano de entrada em serviço!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        func_cadAvião()
    
    numregistro = int(input('Digite o número de registro do avião: '))

    while func_checarRegistro(numregistro) == True:
        print("Número de registro já cadastrado! Tente outro número.")
        numregistro = int(input('Digite o número de registro do avião: '))
    else:
        pass

    fabricante = input('Digite o fabricante do avião: ')
    try:
        assentos = int(input('Digite a quantidade de assentos disponíveis: '))
    except ValueError:
        # Se o usuário digitar algo que não seja um número inteiro, o programa irá pedir para digitar novamente
        print("APENAS NÚMEROS INTEIROS!!!!!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        func_cadAvião()

    
    comprimento = float(input('Digite o comprimento do avião: '))
    largura = float(input('Digite a largura do avião: '))
    companhia = input('Digite o nome da companhia à qual o avião é filiado: ')

    # Alimentação do Registro
    aviao = RegAviao(nome, modelo, datafabri, anoservi, numregistro, fabricante, assentos, comprimento, largura, companhia)

    # Adiciona o registro à lista
    avioes.append(aviao)

    # Adiciona ao arquivo os dados da lista
    with open('Dados/aviões.bin', 'a') as file:
        file.write(f'{aviao.nome};{aviao.modelo};{aviao.datafabri};{aviao.anoservi};{aviao.numregistro};{aviao.fabricante};{aviao.assentos};{aviao.comprimento};{aviao.largura};{aviao.companhia}\n')
    
    dados = aviao
    func_cadAviãoLog(dados)

    print("Passageiro cadastrado com sucesso!")
    time.sleep(1)
    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(1)
    modCadastros.modCadastros()
    

    
def func_cadAviãoLog(dados):

    pc = os.getlogin()
    sistema = sys.platform
    hora = time.strftime("%H:%M:%S")
    data = time.strftime("%d/%m/%Y")
    ip = 'teste'
    ip_pc = socket.gethostbyname(socket.gethostname())

   # Cria/Escreve o log de cadastro
    with open("Logs/cadAviões.log", "a", encoding="utf-8") as f:
        f.write('-' * 50 + '\n')
        f.write(f"PC: {pc}\n")
        f.write(f"Sistema: {sistema}\n")
        f.write(f"IP: {ip}\n")
        f.write(f"IP PC: {ip_pc}\n")
        f.write(f"Data: {data}\n")
        f.write(f"Hora: {hora}\n")
        f.write('-' * 50 + '\n')
        f.write(f"Nome do Avião: {dados.nome}\n")
        f.write(f"Modelo do Avião: {dados.modelo}\n")
        f.write(f"Ano de Fabricação: {dados.datafabri}\n")
        f.write(f"Ano de Entrada em Serviço: {dados.anoservi}\n")
        f.write(f"Número de Registro: {dados.numregistro}\n")
        f.write(f"Fabricante: {dados.fabricante}\n")
        f.write(f"Assentos: {dados.assentos}\n")
        f.write(f"Comprimento: {dados.comprimento}\n")
        f.write(f"Largura: {dados.largura}\n")
        f.write(f"Companhia: {dados.companhia}\n")
        f.write('-' * 50 + '\n')
        f.close()       

    # Envia o log para o whatsapp dos administradores usando InfoBIP
    import requests

    BASE_URL = "https://k29j98.api.infobip.com"
    API_KEY = "eaa16d409b7425ab9016742a8b982478-cc34d0da-f10f-49e1-806b-de9b253ea6fe"

    SENDER = "447860099299"
    RECIPIENT = "5562984201618"

    MESSAGE_TEXT = f"[+] Cadastro: Aeronave (Log)\nPC: {pc}\nSistema: {sistema}\nIP: {ip}\nIP PC: {ip_pc}\nData: {data}\nHora: {hora}\nNome do Avião: {dados.nome}\nModelo do Avião: {dados.modelo}\nAno de Fabricação: {dados.datafabri}\nAno de Entrada em Serviço: {dados.anoservi}\nNúmero de Registro: {dados.numregistro}\nFabricante: {dados.fabricante}\nAssentos: {dados.assentos}\nComprimento: {dados.comprimento}\nLargura: {dados.largura}\nCompanhia: {dados.companhia}"


    def send_message():
        url = f"{BASE_URL}/sms/2/text/single"
        payload = {
            "from": SENDER,
            "to": RECIPIENT,
            "text": MESSAGE_TEXT
        }
        headers = {
            "Authorization": f"App {API_KEY}"
        }
        response = requests.post(url, json=payload, headers=headers)
        print(response.json())

    send_message()