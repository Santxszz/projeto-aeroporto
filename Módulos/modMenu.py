# Importações
import os, sys, time, random, requests, keyboard

# Módulos
from Módulos.modCadastros import modCadastros
from Módulos.modAlterações import modAlterações
from Módulos.modExclusões import modExclusão
# Funções

# Sistema
def modMenu():
    os.system("cls" if os.name == "nt" else "clear")
    print("-"*50)
    print("1 - Cadastros")
    print("2 - Alterar Dados")
    print("3 - Excluir Dados")
    print("4 - Pesquisar Dados")
    print("5 - Guichê")
    print("0 - Sair")
    print("-"*50)

    opcao = input("Opção: ")

    if opcao == "1": # Cadastros
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        modCadastros()
        
    elif opcao == "2": # Alterar Dados
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        modAlterações()
        
    elif opcao == "3": # Excluir Dados
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)

        modExclusão()
        
    elif opcao == "4": # Pesquisar Dados
        from Módulos.modPesquisa import PesquisarMenu
        PesquisarMenu()
        
    elif opcao == "5": # Guichê
        from Módulos.modGuiche import Guiche
        Guiche()
        
    elif opcao == "0": # Sair
        print("Saindo...")
        time.sleep(1)
        sys.exit()
        
    else: # Opção Inválida
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        modMenu()