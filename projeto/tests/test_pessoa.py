import pytest
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa(444, "d", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))
    return pessoa

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 444

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "d"

def test_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "e"
    assert pessoa_valida.nome == "e"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "4444-4444"

def test_mudar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "5555-5555"
    assert pessoa_valida.telefone == "5555-5555"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "d@gmail.com"

def test_mudar_email_valido(pessoa_valida):
    pessoa_valida.email = "e@gmail.com"
    assert pessoa_valida.email == "e@gmail.com"

def test_id_negativo():
    with pytest.raises(ValueError, match="ID negativo!"):
        Pessoa(-444, "d", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_id_tipo_invalido():
    with pytest.raises(TypeError, match="ID inválido!"):
        Pessoa("444", "d", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="Nome inválido!"):
        Pessoa(444, 1, "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_nome_vazio():
    with pytest.raises(TypeError, match="Nome vazio!"):
        Pessoa(444, "", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_numero_tipo_valido():
    with pytest.raises(TypeError, match="Telefone inválido!"):
        Pessoa(444, "d", 44444444, "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))

def test_email_tipo_valido():
    with pytest.raises(TypeError, match="Email inválido!"):
        Pessoa(444, "d", "4444-4444", 1, Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO))