from abc import ABC
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.fisica import Fisica

class Funcionario(Fisica, ABC):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, sexo: Sexo, estadocivil: EstadoCivil, datanascimento: str, cpf: str, rg: str, matricula: str, setor: Setor, salario: int) -> None:
        super().__init__(id, nome, telefone, email, endereco, sexo, estadocivil, datanascimento)
        self.cpf = self._verificar_cpf(cpf)
        self.rg = self._verificar_rg(rg)
        self.matricula = self._verificar_matricula(matricula)
        self.setor = setor
        self.salario = self._verificar_salario(salario)

    def _verificar_cpf(self,valor):
        self._verificar_cpf_tipo_invalido(valor)

        self.cpf = valor
        return self.cpf
    
    def _verificar_rg(self,valor):
        self._verificar_rg_tipo_invalido(valor)

        self.rg = valor
        return self.rg
    
    def _verificar_matricula(self,valor):
        self._verificar_matricula_tipo_invalido(valor)

        self.matricula = valor
        return self.matricula
    
    def _verificar_salario(self,valor):
        self._verificar_salario_tipo_invalido(valor)
        self._verificar_salario_negativo(valor)

        self.salario = valor
        return self.salario
    
    def _verificar_salario_negativo(self,valor):
        if valor <= 0:
            raise ValueError("Salário negativo!")
    
    def _verificar_salario_tipo_invalido(self,valor):
        if not isinstance(valor, float):
            raise TypeError("Salário inválido!")

    def _verificar_cpf_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("CPF inválido!")
        
    def _verificar_rg_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("RG inválido!")

    def _verificar_matricula_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Matrícula inválida!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nCpf: {self.cpf}"
                f"\nRg: {self.rg}"
                f"\nMatricula: {self.matricula}"
                f"\nSetor: {self.setor.name}"
                f"\nSalário: {self.salario}")