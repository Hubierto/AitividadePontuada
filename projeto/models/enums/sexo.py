from enum import Enum

class Sexo(Enum):
    MASCULINO = ("M" ,"Masculino")
    FEMININO = ("F" ,"Feminino")

    def __init__(self, caractere: str, nome: str) -> None:
        self.caractere = caractere
        self.nome = nome