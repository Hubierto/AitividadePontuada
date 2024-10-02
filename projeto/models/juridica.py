from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa

class Juridica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.cnpj = self._verificar_cnpj(cnpj)
        self.inscricaoestadual = self._verificar_inscricao_estadual(inscricaoestadual)

    def _verificar_cnpj(self,valor):
        self._verificar_cnpj_tipo_invalido(valor)

        self.cnpj = valor
        return self.cnpj

    def _verificar_inscricao_estadual(self,valor):
        self._verificar_inscricao_estadual_tipo_invalido(valor)

        self.inscricaoestadual = valor
        return self.inscricaoestadual
    
    def _verificar_cnpj_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("CNPJ inválido!")
        
    def _verificar_inscricao_estadual_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Inscrição estadual inválida!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCnpj: {self.cnpj}"
                f"\nInscrição Estadual: {self.inscricaoestadual}")