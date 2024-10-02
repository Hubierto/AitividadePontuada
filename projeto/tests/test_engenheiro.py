import pytest
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.ENGENHARIA, 6000, "1111")
    return engenheiro

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "1111"

def test_mudar_crea_valido(engenheiro_valido):
    engenheiro_valido.crea = "22222"
    assert engenheiro_valido.crea == "22222"

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="CREA inválido!"):
        Engenheiro(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.ENGENHARIA, 6000, 1111)