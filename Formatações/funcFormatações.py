from validate_docbr import CPF

def formatar_data(data):
    """Formata a data separando por barras para dia, mês e ano."""
    return f"{data[:2]}/{data[2:4]}/{data[4:]}"

