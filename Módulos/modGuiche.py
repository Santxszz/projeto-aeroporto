# Importações
import time, os, sys



def Guiche():
    print("-"*50)
    print("1 - Venda de Passagens")
    print("0 - Voltar")
    print("-"*50)
    
    opcao = input("Opção: ")
    
    if opcao == "1": # Venda de Passagens
        from Funções.func_guiche import Vendas
        Vendas()
    
    elif opcao == "0":
        from Módulos.modMenu import modMenu
        modMenu()
        
    else:
        print("Opção inválida!")
        time.sleep(1)
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(1)
        Guiche()