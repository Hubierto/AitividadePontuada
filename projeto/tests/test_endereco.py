import pytest
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def endereco_valido():
    endereco = Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO)
    return endereco

def test_logradouro_valido(endereco_valido):
    assert endereco_valido.logradouro == "Rua A"

def test_mudar_logradouro_valido(endereco_valido):
    endereco_valido.logradouro = "Rua B"
    assert endereco_valido.logradouro == "Rua B"

def test_numero_valido(endereco_valido):
    assert endereco_valido.numero == "1"

def test_mudar_numero_valido(endereco_valido):
    endereco_valido.numero = "2"
    assert endereco_valido.numero == "2"

def test_complemento_valido(endereco_valido):
    assert endereco_valido.complemento == "Térreo"

def test_mudar_complemento_valido(endereco_valido):
    endereco_valido.complemento = "1º Andar"
    assert endereco_valido.complemento == "1º Andar"

def test_cep_valido(endereco_valido):
    assert endereco_valido.cep == "1111"

def test_mudar_cep_valido(endereco_valido):
    endereco_valido.cep = "2222"
    assert endereco_valido.cep == "2222"

def test_cidade_valido(endereco_valido):
    assert endereco_valido.cidade == "São Paulo"

def test_mudar_cidade_valido(endereco_valido):
    endereco_valido.cidade = "Rio Grande do Sul"
    assert endereco_valido.cidade == "Rio Grande do Sul"

def test_logradouro_tipo_invalido():
    with pytest.raises(TypeError, match="Logradouro inválido!"):
        Endereco(1, "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO)

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="Número inválido!"):
        Endereco("Rua A", 1, "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO)

def test_complemento_tipo_invalido():
    with pytest.raises(TypeError, match="Complemento inválido!"):
        Endereco("Rua A", "1", 1, 1111, "São Paulo", UnidadeFederativa.SAO_PAULO)

def test_cep_tipo_invalido():
    with pytest.raises(TypeError, match="CEP inválido!"):
        Endereco("Rua A", "1", "Térreo", 1111, "São Paulo", UnidadeFederativa.SAO_PAULO)

def test_cidade_tipo_invalido():
    with pytest.raises(TypeError, match="Cidade inválida!"):
        Endereco("Rua A", "1", "Térreo", "1111", 1, UnidadeFederativa.SAO_PAULO)