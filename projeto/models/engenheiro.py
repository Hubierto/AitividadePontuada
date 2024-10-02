from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
from projeto.models.funcionario import Funcionario

class Engenheiro(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: int, crea: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento, cpf, rg, matricula, setor, salario)
        self.crea = self._verificar_crea(crea)

    def _verificar_crea(self,valor):
        self._verificar_crea_tipo_invalido(valor)

        self.crea = valor
        return self.crea

    def _verificar_crea_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("CREA inválido!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCrea: {self.crea}")