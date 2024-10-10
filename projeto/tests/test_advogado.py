import pytest
from projeto.models.advogado import Advogado
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def advogado_valido():
    advogado = Advogado(
        777,
        "Carlos Silva",
        "8888-7777",  
        "carlos.silva@example.com",  
        Endereco("Rua das Palmeiras", "200", "2º andar", "3333", "Recife", UnidadeFederativa.BAHIA),
        Sexo.MASCULINO, 
        EstadoCivil.SOLTEIRO,
        "1111", 
        "2222", 
        "3333", "90000", Setor.ENGENHARIA, 8000,"9000")
    return advogado

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "9000"

def test_mudar_oab_valido(advogado_valido):
    advogado_valido.oab = "99999"
    assert advogado_valido.oab == "99999"

def test_oab_tipo_invalido():
    with pytest.raises(TypeError, match="Oab inválido!"):
        Advogado(777, "Carlos Silva", "8888-7777", "carlos.silva@example.com", Endereco("Rua das Palmeiras", "200", "2º andar", "3333", "Recife", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.SOLTEIRO, "1111", "2222", "3333", "90000", Setor.ENGENHARIA, 8000, 9000  
    )
