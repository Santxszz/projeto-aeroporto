def Iniciar():
    # Cria todos os arquivos necessários para o funcionamento do sistema caso não existam
    try:
        # Abre o arquivo para leitura
        with open('Dados/aviões.bin', 'r') as arquivo_leitura:
            for linha in arquivo_leitura:
                pass

        with open('Dados/passageiros.bin', 'r') as arquivo_leitura:
            for linha in arquivo_leitura:
                pass

        with open('Dados/pilotos.bin', 'r') as arquivo_leitura:
            for linha in arquivo_leitura:
                pass

        with open('Dados/viagens.bin', 'r') as arquivo_leitura:
            for linha in arquivo_leitura:
                pass

        with open('Dados/vendas.bin', 'r') as arquivo_leitura:
            for linha in arquivo_leitura:
                pass

    except FileNotFoundError:
        print(f"O Arquivo aviões.bin não foi encontrado! Criando arquivo...")
        # Cria o arquivo aviões.bin
        with open('Dados/aviões.bin', 'w') as arquivo:
            arquivo.write("")
        print(f"Arquivo aviões.bin criado com sucesso!")

        print(f"O Arquivo passageiros.bin não foi encontrado! Criando arquivo...")
        # Cria o arquivo passageiros.bin
        with open('Dados/passageiros.bin', 'w') as arquivo:
            arquivo.write("")
        print(f"Arquivo passageiros.bin criado com sucesso!")

        print("O Arquivo pilotos.bin não foi encontrado! Criando arquivo...")
        # Cria o arquivo pilotos.bin

        with open('Dados/pilotos.bin', 'w') as arquivo:
            arquivo.write("")

        print("Arquivo pilotos.bin criado com sucesso!")

        print("O Arquivo viagens.bin não foi encontrado! Criando arquivo...")
        # Cria o arquivo viagens.bin
        with open('Dados/viagens.bin', 'w') as arquivo:
            arquivo.write("")
        print("Arquivo viagens.bin criado com sucesso!")

        print("O Arquivo vendas.bin não foi encontrado! Criando arquivo...")
        # Cria o arquivo vendas.bin
        with open('Dados/vendas.bin', 'w') as arquivo:
            arquivo.write("")
        print("Arquivo vendas.bin criado com sucesso!")
