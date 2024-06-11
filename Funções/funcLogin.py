# Importações
import os, sys, time, random, requests, getpass, socket, colorama

# Módulos
from Módulos.modMenu import modMenu

def funcLogin():
    # Variáveis
    login = input("Login: ")
    senha = getpass.getpass("Senha: ")

    # Pega os dados de usuário e senha no arquivo users.bin
    with open("Dados/users.bin", "r", encoding="utf-8") as f:
        users = f.readlines()
        f.close()
    
    # Verifica se o login e senha estão corretos
    for i in range(len(users)):
        users[i] = users[i].replace("\n", "")
        users[i] = users[i].split(";")

        if login == users[i][0] and senha == users[i][1]:
            os.system("cls" if os.name == "nt" else "clear") 
            time.sleep(2)
            print(f"{colorama.Fore.GREEN}[+] Sucesso{colorama.Fore.RESET}")
            print(f"{colorama.Fore.BLUE}[+] Bem vindo, {login}{colorama.Fore.RESET}")
            funcLoginLog()
            time.sleep(2)
            return True
    
    else:
        print("Login ou senha incorretos!")
        return False



def funcLoginLog():
    # Variáveis locais
    pc = os.getlogin()
    sistema = sys.platform
    hora = time.strftime("%H:%M:%S")
    data = time.strftime("%d/%m/%Y")
    ip = 'teste'
    ip_pc = socket.gethostbyname(socket.gethostname())

    # Cria/Escreve o log de login
    with open("Logs/Login.log", "a", encoding="utf-8") as f:
        f.write('-' * 50 + '\n')
        f.write(f"PC: {pc}\n")
        f.write(f"Sistema: {sistema}\n")
        f.write(f"IP: {ip}\n")
        f.write(f"IP PC: {ip_pc}\n")
        f.write(f"Data: {data}\n")
        f.write(f"Hora: {hora}\n")
        f.write('-' * 50 + '\n')
        f.close()

    # Envia o log para o whatsapp dos administradores usando InfoBIP
    import requests

    BASE_URL = "https://k29j98.api.infobip.com"
    API_KEY = "eaa16d409b7425ab9016742a8b982478-cc34d0da-f10f-49e1-806b-de9b253ea6fe"

    SENDER = "447860099299"
    RECIPIENT = "5562984201618"

    MESSAGE_TEXT = f"LOG - LOGIN\nPC: {pc}\nSistema: {sistema}\nIP: {ip}\nIP PC: {ip_pc}\nData: {data}\nHora: {hora}"


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

    # send_message()


    return modMenu()