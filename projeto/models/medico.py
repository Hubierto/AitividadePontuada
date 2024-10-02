from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
from projeto.models.funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: int, crm: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento, cpf, rg, matricula, setor, salario)
        self.crm = self._verificar_crm(crm)

    def _verificar_crm(self,valor):
        self._verificar_crm_tipo_invalido(valor)

        self.crm = valor
        return self.crm

    def _verificar_crm_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("CRM inválido!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCrea: {self.crm}")
