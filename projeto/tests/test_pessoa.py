import pytest 
from projeto.models.pessoa import Pessoa
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def pessoa_valida():
    pessoa1 = Pessoa(
        67890,
        "Roberto Silva",
        "71999999999",
        "roberto.silva@gmail.com",
        Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO)
    )
    return pessoa1

def test_id_valido(pessoa_valida):
    assert pessoa_valida.id == 67890

def test_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Roberto Silva"

def test_mudar_nome_valido(pessoa_valida):
    pessoa_valida.nome = "Mariana Costa"
    assert pessoa_valida.nome == "Mariana Costa"

def test_numero_valido(pessoa_valida):
    assert pessoa_valida.telefone == "71999999999"

def test_mudar_numero_valido(pessoa_valida):
    pessoa_valida.telefone = "71977777777"
    assert pessoa_valida.telefone == "71977777777"

def test_email_valido(pessoa_valida):
    assert pessoa_valida.email == "roberto.silva@gmail.com"

def test_mudar_email_valido(pessoa_valida):
    pessoa_valida.email = "mariana.costa@gmail.com"
    assert pessoa_valida.email == "mariana.costa@gmail.com"

def test_id_negativo():
    with pytest.raises(ValueError, match="ID negativo!"):
        Pessoa(-67890, "Roberto Silva", "71999999999", "roberto.silva@gmail.com", Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_id_tipo_invalido():
    with pytest.raises(TypeError, match="ID inválido!"):
        Pessoa("67890", "Roberto Silva", "71999999999", "roberto.silva@gmail.com", Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_nome_tipo_invalido():
    with pytest.raises(TypeError, match="Nome inválido!"):
        Pessoa(67890, 12345, "71999999999", "roberto.silva@gmail.com", Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_nome_vazio():
    with pytest.raises(ValueError, match="Nome vazio!"):
        Pessoa(67890, "", "71999999999", "roberto.silva@gmail.com", Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_numero_tipo_invalido():
    with pytest.raises(TypeError, match="Telefone inválido!"):
        Pessoa(67890, "Roberto Silva", 71999999999, "roberto.silva@gmail.com", Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))

def test_email_tipo_invalido():
    with pytest.raises(TypeError, match="Email inválido!"):
        Pessoa(67890, "Roberto Silva", "71999999999", 0, Endereco("Avenida Brasil", 456, "12A", "2222222", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO))
