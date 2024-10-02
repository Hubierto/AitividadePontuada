from projeto.models.endereco import Endereco
from projeto.models.juridica import Juridica

class PrestacaoServicos(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str, contratoinicio: str, contratofim: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoestadual)
        self.contratoinicio = self._verificar_contrato_inicio(contratoinicio)
        self.contratofim = self._verificar_contrato_fim(contratofim)

    def _verificar_contrato_inicio(self,valor):
        self._verificar_contrato_inicio_tipo_invalido(valor)

        self.contratoinicio = valor
        return self.contratoinicio
    
    def _verificar_contrato_fim(self,valor):
        self._verificar_contrato_fim_tipo_invalido(valor)

        self.contratofim = valor
        return self.contratofim

    def _verificar_contrato_inicio_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Inicio de contratro inválido!")

    def _verificar_contrato_fim_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Fim de contrato inválido!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nContrato Inicio: {self.contratoinicio}"
                f"\nContrato Fim: {self.contratofim}")
