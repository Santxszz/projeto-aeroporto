# Importações
import os
import sys
import time
import random
import requests
import keyboard

# Funções
from Módulos.modMenu import modMenu
from Funções.func_pesquisas import PesquisarPassageiroCPF
from Funções.func_pesquisas import PesquisarPilotoCPF
from Funções.func_pesquisas import PesquisarAviaoCodigo
from Funções.func_pesquisas import PesquisarViagemID

# Funções


def PesquisarMenu():
    print("-"*50)
    print("1 - Pesquisar Passageiro")
    print("2 - Pesquisar Piloto")
    print("3 - Pesquisar Aeronave")
    print("4 - Pesquisar Viagem")
    print("0 - Voltar")
    print("-"*50)

    opcao = input("Opção: ")

    if opcao == "1": # Pesquisar Passageiro
        cpf = input("CPF: ")
        PesquisarPassageiroCPF(cpf)
        
    elif opcao == "2": # Pesquisar Piloto
        cpf = input("CPF: ")
        PesquisarPilotoCPF(cpf)
        
    elif opcao == "3": # Pesquisar Aeronave
        codigo = input("Código: ")
        PesquisarAviaoCodigo(codigo)
        
    elif opcao == "4": # Pesquisar Viagem
        id = input("ID: ")
        PesquisarViagemID(id)
        
    elif opcao == "0": # Voltar
        modMenu()
        
    else:
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        PesquisarMenu()
