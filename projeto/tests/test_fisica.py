import pytest 
from projeto.models.fisica import Fisica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.estado_civil import EstadoCivil

@pytest.fixture
def fisica_valida():
    fisica = Fisica(
        222,
        "Maria Oliveira",
        "2222-2222",
        "maria.oliveira@gmail.com",
        Endereco("Avenida Brasil", "100", "5º andar", "2222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO),
        Sexo.FEMININO,
        EstadoCivil.CASADO,
        "15/05/90"
    )
    return fisica

def test_data_de_nascimento_valido(fisica_valida):
    assert fisica_valida.datanascimento == "15/05/90"

def test_mudar_data_de_nascimento_valido(fisica_valida):
    fisica_valida.datanascimento = "20/10/95"
    assert fisica_valida.datanascimento == "20/10/95"

def test_data_de_nascimento_tipo_invalido():
    with pytest.raises(TypeError, match="Data de nascimento é inválida!"):
        Fisica(
            222,
            "Maria Oliveira",
            "2222-2222",
            "maria.oliveira@gmail.com",
            Endereco("Avenida Brasil", "100", "5º andar", "2222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO),
            Sexo.FEMININO,
            EstadoCivil.CASADO,
            12345  # Tipo inválido para a data de nascimento
        )
