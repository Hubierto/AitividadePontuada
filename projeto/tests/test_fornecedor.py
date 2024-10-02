import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def fornecedor_valido():
    fornecedor = Fornecedor(666, "f", "6666-6666", "f@gmail.com", Endereco("Rua F", "6", "Térreo", "6666", "São Paulo", UnidadeFederativa.SAO_PAULO), "33333", "44444", "Tênis")
    return fornecedor

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Tênis"

def test_mudar_produto_valido(fornecedor_valido):
    fornecedor_valido.produto = "Chinela"
    assert fornecedor_valido.produto == "Chinela"

def test_produto_tipo_invalido():
    with pytest.raises(TypeError, match="Produto é inválido!"):
        Fornecedor(666, "f", "6666-6666", "f@gmail.com", Endereco("Rua F", "6", "Térreo", "6666", "São Paulo", UnidadeFederativa.SAO_PAULO), "33333", "44444", 1)