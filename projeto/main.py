from models.enums.estado_civil import EstadoCivil
from models.enums.sexo import Sexo
from models.enums.setor import Setor
from models.enums.unidade_federativa import UnidadeFederativa
from models.endereco import Endereco
from models.engenheiro import Engenheiro
from models.medico import Medico
from models.advogado import Advogado
from models.cliente import Cliente
from models.prestacao_servico import PrestacaoServicos
from models.fornecedor import Fornecedor

engenheiro = Engenheiro(111, "a", "1111-1111", "a@gmail.com", Endereco("Rua A", "1", "Térreo", "1111", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.ENGENHARIA, 6000, "1111")
medico = Medico(222, "b", "2222-2222", "b@gmail.com", Endereco("Rua B", "2", "Térreo", "2222", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.SAUDE, 8000, "2222")
advogado = Advogado(333, "c", "3333-3333", "c@gmail.com", Endereco("Rua C", "3", "Térreo", "3333", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", "1111", "2222", "3333", Setor.JURIDICO, 7000, "3333")
cliente = Cliente(444, "d", "4444-4444", "d@gmail.com", Endereco("Rua D", "4", "Térreo", "4444", "São Paulo", UnidadeFederativa.SAO_PAULO), Sexo.FEMININO, EstadoCivil.SOLTEIRO, "01/01/01", 111111)
prestacao_servico = PrestacaoServicos(555, "e", "5555-5555", "e@gmail.com", Endereco("Rua E", "5", "Térreo", "5555", "São Paulo", UnidadeFederativa.SAO_PAULO), "11111", "22222", "01/01/01", "01/01/02")
fornecedor = Fornecedor(666, "f", "6666-6666", "f@gmail.com", Endereco("Rua F", "6", "Térreo", "6666", "São Paulo", UnidadeFederativa.SAO_PAULO), "33333", "44444", "Tênis")

print(engenheiro)
print(medico)
print(advogado)
print(cliente)
print(prestacao_servico)
print(fornecedor)
