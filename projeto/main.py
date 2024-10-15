import os
print(os.getcwd())
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
 
from projeto.models.medico import Medico
from projeto.models.endereco import Endereco
from projeto.models.enums.unidade_federativa import UnidadeFederativa 
from projeto.models.enums.estado_civil import EstadoCivil
from projeto.models.enums.sexo import Sexo
from projeto.models.enums.setor import Setor
from projeto.models.fornecedor import Fornecedor

os.system("cls || clear")

medico1 = Medico(123, "Romario", "71900000000", "R@gmail.com", Endereco("Praça do sol", "76", "A", "1256677", "Salvador", UnidadeFederativa.BAHIA), Sexo.MASCULINO, EstadoCivil.CASADO, "21/04/2000", "123453123-90", "874874874", "000001", Setor.JURIDICO, 8000, "1000") 
fornecedor1 = Fornecedor(101010, "Marta", "71901234567", "M@gmail.com", Endereco("Praça da Revolução", "98", "B", "57765554", "Salvador", UnidadeFederativa.BAHIA), "819589475", "00002", "Manga")

print(medico1)
print(fornecedor1)