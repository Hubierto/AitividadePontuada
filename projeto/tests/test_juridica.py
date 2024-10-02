import pytest
from projeto.models.juridica import Juridica
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def juridica_valido():
    juridica = Juridica(666, "f", "6666-6666", "f@gmail.com", Endereco("Rua F", "6", "Térreo", "6666", "São Paulo", UnidadeFederativa.SAO_PAULO), "33333", "44444")
    return juridica

def test_cnpj_valido(juridica_valido):
    assert juridica_valido.cnpj == "33333"

def test_mudar_cnpj_valido(juridica_valido):
    juridica_valido.cnpj = "44444"
    assert juridica_valido.cnpj == "44444"

def test_inscricao_estadual_valido(juridica_valido):
    assert juridica_valido.inscricaoestadual == "44444"

def test_mudar_inscricao_estadual_valido(juridica_valido):
    juridica_valido.inscricaoestadual = "55555"
    assert juridica_valido.inscricaoestadual == "55555"

def test_cnpj_tipo_invalido():
    with pytest.raises(TypeError, match="CNPJ inválido!"):
        Juridica(666, "f", "6666-6666", "f@gmail.com", Endereco("Rua F", "6", "Térreo", "6666", "São Paulo", UnidadeFederativa.SAO_PAULO), 33333, "44444")

def test_inscricao_estadual_tipo_invalido():
    with pytest.raises(TypeError, match="Inscrição estadual inválida!"):
        Juridica(666, "f", "6666-6666", "f@gmail.com", Endereco("Rua F", "6", "Térreo", "6666", "São Paulo", UnidadeFederativa.SAO_PAULO), "33333", 44444)