# Importações
import os, sys, time, random, requests, keyboard

# Funções
from Funções.func_alterações import AlterarPassageiro

def modAlterações():
    print("-"*50)
    print("1 - Alterar Passageiro")
    print("2 - Alterar Piloto")
    print("3 - Alterar Aeronave")
    print("4 - Alterar Viagem")
    print("0 - Voltar")
    print("-"*50)

    opcao = input("Opção: ")

    if opcao == "1": # Alterar Passageiro
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        AlterarPassageiro()
        
    elif opcao == "2": # Alterar Piloto
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_alterações import modAlterarPiloto
        modAlterarPiloto()

    elif opcao == "3": # Alterar Aeronave
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_alterações import modAlterarAeronave
        modAlterarAeronave()
    
    elif opcao == "4": # Alterar Viagem
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        from Funções.func_alterações import modAlterarViagem
        modAlterarViagem()
        
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
        modAlterações()
        