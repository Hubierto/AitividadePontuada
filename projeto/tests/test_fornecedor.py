import pytest
from projeto.models.fornecedor import Fornecedor
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def fornecedor_valido():
    fornecedor1 = Fornecedor(
        456789,
        "Ana Silva",
        "71987654321",
        "ana@gmail.com",
        Endereco("Avenida Central", "100", "A", "456789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO),
        "987654321",
        "2222222",
        "Bolo"
    )
    return fornecedor1

def test_produto_valido(fornecedor_valido):
    assert fornecedor_valido.produto == "Bolo"

def test_mudar_produto_valido(fornecedor_valido):
    fornecedor_valido.produto = "Torta"
    assert fornecedor_valido.produto == "Torta"

def test_produto_tipo_invalido():
    with pytest.raises(TypeError, match="Produto é inválido!"):
        Fornecedor(
            456789,
            "Ana Silva",
            "71987654321",
            "ana@gmail.com",
            Endereco("Avenida Central", "100", "A", "456789", "Rio de Janeiro", UnidadeFederativa.RIO_DE_JANEIRO),
            "987654321",
            "2222222",
            12345  # Tipo inválido para o produto
        )
