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
        444,
        "Juliana Souza",
        "4444-4444",
        "juliana.souza@gmail.com",
        Endereco("Avenida dos Trabalhadores", "400", "5º andar", "4444", "Belo Horizonte", UnidadeFederativa.BAHIA),
        Sexo.FEMININO,
        EstadoCivil.CASADO,
        "10/10/85",
        "2222",
        "3333",
        "4444",
        Setor.JURIDICO,
        8500,
        "4444"
    )
    return advogado

def test_oab_valido(advogado_valido):
    assert advogado_valido.oab == "4444"

def test_mudar_oab_valido(advogado_valido):
    advogado_valido.oab = "55555"
    assert advogado_valido.oab == "55555"

def test_oab_tipo_invalido():
    with pytest.raises(TypeError, match="Oab inválida!"):
        Advogado(
            444,
            "Juliana Souza",
            "4444-4444",
            "juliana.souza@gmail.com",
            Endereco("Avenida dos Trabalhadores", "400", "5º andar", "4444", "Belo Horizonte", UnidadeFederativa.BAHIA),
            Sexo.FEMININO,
            EstadoCivil.CASADO,
            "10/10/85",
            "2222",
            "3333",
            "4444",
            Setor.JURIDICO,
            8500,
            4444  # Tipo inválido para a OAB
        )
