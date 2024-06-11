from dataclasses import dataclass

@dataclass
class RegViagens:
    id: int
    aeronave: str
    piloto: str
    destino: str
    origem: str
    data: str
    hora: str
    classeExecutiva: int
    classeEconomica: int
    primeiraClasse: int
    valorExecutiva: float
    valorEconomica: float
    valorPrimeira: float