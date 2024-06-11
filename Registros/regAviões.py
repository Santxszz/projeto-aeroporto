from dataclasses import dataclass

@dataclass
class RegAviao:
    nome: str = ''
    modelo: str = ''
    datafabri: int = 0
    anoservi: int = 0
    numregistro: int = 0
    fabricante: str = ''
    assentos: int = 0
    comprimento: float = 0.0
    largura: float = 0.0
    companhia: str = ''