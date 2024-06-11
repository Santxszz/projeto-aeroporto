def func_checarRegistro(numregistro):
    listaAvioes = []
    with open("Dados/aviões.bin", "rb") as file:
        for i in file:
            if i.strip():
                numregistro = i.decode("utf-8").strip().split(";")[4]
                listaAvioes.append(numregistro)
    # Se o CPF já estiver cadastrado retorna True
    if numregistro in listaAvioes:
        return True
    else:
        return False