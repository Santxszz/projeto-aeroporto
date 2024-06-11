# Importações
import os, sys, time, random, requests, keyboard

# Funções
from Funções.func_cadPassageiros import func_cadPassageiros
from Funções.func_cadAviões import func_cadAvião
from Funções.func_cadPiloto import cadastrarPiloto

def modCadastros():
    print("-"*50)
    print("1 - Cadastro de Passageiros")
    print("2 - Cadastro de Pilotos")
    print("3 - Cadastro de Aeronaves")
    print("4 - Cadastro de Viagens")
    print("0 - Voltar")
    print("-"*50)

    opcao = input('Opção: ')

    if opcao == "1":
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        func_cadPassageiros()
    elif opcao == "2":
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        cadastrarPiloto()
        
    elif opcao == "3":
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        func_cadAvião()
        
    elif opcao == "4":
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_cadViagens import CadastrarViagem
        CadastrarViagem()
    
    elif opcao == "0":
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Módulos.modMenu import modMenu
        modMenu()
    
    else:
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        modCadastros()
    