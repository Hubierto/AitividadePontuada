import pytest
from projeto.models.funcionario import Funcionario
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def funcionario_valido():
    funcionario = Funcionario(111, "a", "1111-2222", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111-1111", "2222-2222", "3333", Setor.ENGENHARIA, 6000)
    return funcionario

def test_salario_valido(funcionario_valido: Funcionario):
    assert funcionario_valido.salario == 6000

def test_mudar_salario_valido(funcionario_valido: Funcionario):
    funcionario_valido.salario = 7000
    assert funcionario_valido.salario == 7000

def test_cpf_valido(funcionario_valido: Funcionario):
    assert funcionario_valido.cpf == "1111-1111"

def test_mudar_cpf_valido(funcionario_valido: Funcionario):
    funcionario_valido.cpf = "2222-2222"
    assert funcionario_valido.cpf == "2222-2222"

def test_rg_valido(funcionario_valido: Funcionario):
    assert funcionario_valido.rg == "2222-2222"

def test_mudar_rg_valido(funcionario_valido: Funcionario):
    funcionario_valido.rg = "3333-3333"
    assert funcionario_valido.rg == "3333-3333"

def test_matricula_valido(funcionario_valido: Funcionario):
    assert funcionario_valido.matricula == "3333"

def test_mudar_matricula_valido(funcionario_valido: Funcionario):
    funcionario_valido.matricula = "4444"
    assert funcionario_valido.matricula == "4444"

def test_salario_negativo():
    with pytest.raises(ValueError, match="Salário negativo!"):
        Funcionario(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.ENGENHARIA, -6000)

def test_salario_tipo_invalido():
    with pytest.raises(TypeError, match="Salário inválido!"):
        Funcionario(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.ENGENHARIA, "6000")

def test_cpf_tipo_invalido():
    with pytest.raises(TypeError, match="CPF inválido!"):
        Funcionario(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", 1111, "2222", "3333", Setor.ENGENHARIA, 6000)
    
def test_rg_tipo_invalido():
    with pytest.raises(TypeError, match="RG inválido!"):
        Funcionario(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", 2222, "3333", Setor.ENGENHARIA, 6000)

def test_matricula_tipo_invalido():
    with pytest.raises(TypeError, match="Matrícula inválida!"):
        Funcionario(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", 3333, Setor.ENGENHARIA, 6000)