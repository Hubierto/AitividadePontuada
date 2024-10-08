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

os.system("cls || clear")

medico1 = Medico(999, "Ray", "71988228822", "ray@gmail.com", Endereco("praça do sol", "1230", "E", "61243", "Salvador", UnidadeFederativa.BAHIA), Sexo.FEMININO, EstadoCivil.CASADO, "01/04/2002","12354354212", "85890238985", "0i9090909", Setor.ENGENHARIA, 100.000, "10.000")

print(medico1)