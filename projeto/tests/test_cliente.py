import pytest
from projeto.models.cliente import Cliente
from projeto.models.endereco import Endereco
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo 
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def cliente_valido():
    cliente = Cliente(444, "d", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", 111111)
    return cliente

def test_protocolo_de_atendimento_valido(cliente_valido):
    assert cliente_valido.protocoloatendimento == 111111

def test_mudar_protocolo_de_atendimento_valido(cliente_valido):
    cliente_valido.protocoloatendimento = 22222
    assert cliente_valido.protocoloatendimento == 22222

def test_protocolo_de_atendimento_tipo_invalido():
    with pytest.raises(TypeError, match="Protocolo de atendimento inválido!"):
        Cliente(444, "d", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "111111")