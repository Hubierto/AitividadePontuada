import pytest  
from projeto.models.engenheiro import Engenheiro
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.setor import Setor

@pytest.fixture
def engenheiro_valido():
    engenheiro = Engenheiro(
        333,
        "Fernanda Lima",
        "3333-3333",
        "fernanda.lima@gmail.com",
        Endereco("Rua do Progresso", "150", "3º andar", "3333", "Curitiba", UnidadeFederativa.BAHIA),
        Sexo.FEMININO,
        EstadoCivil.DIVORCIADO,
        "25/12/80",
        "3333",
        "4444",
        "5555",
        Setor.ENGENHARIA,
        8500,
        "3333"
    )
    return engenheiro

def test_crea_valido(engenheiro_valido):
    assert engenheiro_valido.crea == "3333"

def test_mudar_crea_valido(engenheiro_valido):
    engenheiro_valido.crea = "44444"
    assert engenheiro_valido.crea == "44444"

def test_crea_tipo_invalido():
    with pytest.raises(TypeError, match="CREA inválido!"):
        Engenheiro(
            333,
            "Fernanda Lima",
            "3333-3333",
            "fernanda.lima@gmail.com",
            Endereco("Rua do Progresso", "150", "3º andar", "3333", "Curitiba", UnidadeFederativa.BAHIA),
            Sexo.FEMININO,
            EstadoCivil.DIVORCIADO,
            "25/12/80",
            "3333",
            "4444",
            "5555",
            Setor.ENGENHARIA,
            "8500",
            "CREA inválido!"  # Tipo inválido para o CREA
        )
