from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.pessoa import Pessoa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

class Fisica(Pessoa, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str) -> None:
        super().__init__(id, nome, telefone, email, endereco)
        self.sexo = sexo
        self.estadocivil = estadocivil
        self.datanascimento = self._verificar_data_de_nascimento(datanascimento)

    def _verificar_data_de_nascimento(self,valor):
        self._verificar_data_de_nascimento_tipo_invalido(valor)

        self.datanascimento = valor
        return self.datanascimento

    def _verificar_data_de_nascimento_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Data de nascimento é inválida!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nSexo: {self.sexo.nome}"
                f"\nEstado Civil: {self.estadocivil.name}"
                f"\nData de nascimento: {self.datanascimento}")