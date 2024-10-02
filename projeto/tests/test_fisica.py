import pytest
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def fisica_valida():
    fisica = Fisica(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01")
    return fisica

def test_data_de_nascimento_valido(fisica_valida):
    assert fisica_valida.datanascimento == "01/01/01"

def test_mudar_data_de_nascimento_valido(fisica_valida):
    fisica_valida.datanascimento = "02/02/02"
    assert fisica_valida.datanascimento == "02/02/02"

def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match="Data de nascimento é inválida!"):
        Fisica(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, 1)