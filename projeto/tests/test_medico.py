import pytest
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def medico_valido():
    medico = Medico(222, "b", "2222-2222", "b@gmail.com", Endereco("Rua B", "2", "Térreo", "2222", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.SAUDE, 8000, "2222")
    return medico

def test_crm_valido(medico_valido):
    assert medico_valido.crm == "2222"

def test_mudar_crm_valido(medico_valido):
    medico_valido.crm = "3333"
    assert medico_valido.crm == "3333"

def test_crm_tipo_invalido():
    with pytest.raises(TypeError, match="CRM inválido!"):
        Medico(222, "b", "2222-2222", "b@gmail.com", Endereco("Rua B", "2", "Térreo", "2222", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.SAUDE, 8000, 2222)