import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
     pessoa1 = Pessoa(12345, "Ana", "71988888888", "A@gmail.com", Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))
     return pessoa1

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 12345

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Ana"

def test_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Marta"
    assert pessoa_valida.nome == "Marta"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "71988888888"

def test_mudar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "71908080808"
    assert pessoa_valida.telefone == "71908080808"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "A@gmail.com"

def test_mudar_email_valido(pessoa_valida):
    pessoa_valida.email = "M@gmail.com"
    assert pessoa_valida.email == "M@gmail.com"

def test_id_negativo():
    with pytest.raises(ValueError, match="ID negativo!"):
        Pessoa(-12345, "Ana", "71988888888", "A@gmail.com", Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))

def test_id_tipo_invalido():
    with pytest.raises(TypeError, match="ID inválido!"):
        Pessoa("12345", "Ana", "71988888888", "A@gmail.com", Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="Nome inválido!"):
        Pessoa(12345, "Ana", "71988888888", "A@gmail.com", Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))

def test_nome_vazio():
    with pytest.raises(TypeError, match="Nome vazio!"):
        Pessoa(12345, "", "71988888888", "A@gmail.com", Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="Telefone inválido!"):
        Pessoa(12345, "Ana", 71988888888, "A@gmail.com", Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))

def test_email_tipo_valido():
    with pytest.raises(TypeError, match="Email inválido!"):
        Pessoa(12345, "Ana", "71988888888", 0, Endereco("Praça do sol", 123, "07e", "1212121", "Salvador", UnidadeFederativa.BAHIA))