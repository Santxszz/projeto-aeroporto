# Importações
import os, sys, time, random, requests, keyboard

# Funções
from Funções.func_alterações import AlterarPassageiro

def modExclusão():
    print("-"*50)
    print("1 - Excluir Passageiro")
    print("2 - Excluir Piloto")
    print("3 - Excluir Aeronave")
    print("4 - Excluir Viagem")
    print("0 - Voltar")
    print("-"*50)

    opcao = input("Opção: ")

    if opcao == "1": # Excluir Passageiro
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_exclusões import ExcluirPassageiro
        ExcluirPassageiro()
    
    elif opcao == "2": # Excluir Piloto
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_exclusões import ExcluirPiloto
        ExcluirPiloto()
    
    elif opcao == "3": # Excluir Aeronave
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_exclusões import ExcluirAeronave
        ExcluirAeronave()
    
    elif opcao == "4": # Excluir Viagem
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_exclusões import ExcluirViagem
        ExcluirViagem()
    
    elif opcao == "0": # Voltar
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Módulos.modMenu import modMenu
        modMenu()
    
    else:
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        modExclusão()
        