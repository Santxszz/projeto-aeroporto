def func_checarCpf(cpf):
    try:
            listaCpf = []
            with open("Dados/passageiros.bin", "rb") as file:
                for i in file:
                    if i.strip():
                        cpf_lido = i.decode("utf-8").strip().split(";")[1]
                        listaCpf.append(cpf_lido)          
                if cpf in listaCpf:
                    return True
                else:
                    return False
    except:
        print("Erro ao checar CPF!")
        print("Causa: {}".format(Exception))
        cpf = input("CPF: ")
    

def ChecarCPFPiloto(cpf):
    listaCpf = []
    with open("Dados/pilotos.bin", "rb") as file:
        for i in file:
            
            if i.strip():
                cpf_lido = i.decode("utf-8").strip().split(";")[1]
                listaCpf.append(cpf_lido)            
    if cpf in listaCpf:
        return True
    else:
        return False