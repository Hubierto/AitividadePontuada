import pytest
from projeto.models.prestacao_servico import PrestacaoServicos
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa

@pytest.fixture
def prestacao_servicos_valido():
    prestacaoservico = PrestacaoServicos(555, "e", "5555-5555", "e@gmail.com", Endereco("Rua E", "5", "Térreo", "5555", "São Paulo", UnidadeFederativa.SAO_PAULO), "11111", "22222", "01/01/01", "01/01/02")
    return prestacaoservico

def test_contrato_inicio_valido(prestacao_servicos_valido):
    assert prestacao_servicos_valido.contratoinicio == "01/01/01"

def test_mudar_contrato_inicio_valido(prestacao_servicos_valido):
    prestacao_servicos_valido.contratoinicio = "02/02/02"
    assert prestacao_servicos_valido.contratoinicio == "02/02/02"

def test_contrato_fim_valido(prestacao_servicos_valido):
    assert prestacao_servicos_valido.contratofim == "01/01/02"

def test_mudar_contrato_fim_valido(prestacao_servicos_valido):
    prestacao_servicos_valido.contratofim = "01/01/02"
    assert prestacao_servicos_valido.contratofim == "01/01/02"

def test_contrato_inicio_tipo_invalido():
    with pytest.raises(TypeError, match="Inicio de contratro inválido!"):
        PrestacaoServicos(555, "e", "5555-5555", "e@gmail.com", Endereco("Rua E", "5", "Térreo", "5555", "São Paulo", UnidadeFederativa.SAO_PAULO), "11111", "22222", 1, "01/01/02")

def test_contrato_fim_tipo_invalido():
    with pytest.raises(TypeError, match="Fim de contrato inválido!"):
        PrestacaoServicos(555, "e", "5555-5555", "e@gmail.com", Endereco("Rua E", "5", "Térreo", "5555", "São Paulo", UnidadeFederativa.SAO_PAULO), "11111", "22222", "01/01/01", 1)