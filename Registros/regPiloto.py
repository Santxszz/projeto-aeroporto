from dataclasses import dataclass
@dataclass
class regPiloto:
    nome: str = ''
    cpf: int = 0 
    rg: int = 0 
    cht : int = 0 

    sexo: str = ''
    dataNascimento: str = '' 

    # Dados de Contato
    telefone: int = 0 

    # Dados de Endereço
    endereco: str = ''
    setor: str = ''
    complemento: str = ''
    numerocasa : int = 0 
    # Dados de Localização
    naturalidade: str = ''
    cep: int = 0 
    cidade: str = ' '
    uf: str = ''
    pais: str = ''
