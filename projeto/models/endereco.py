
from projeto.models.enums.unidade_federativa import UnidadeFederativa

class Endereco:
    def __init__(self, logradouro: str, numero: str, complemento: str, cep: str, cidade: str, uf: UnidadeFederativa) -> None:
        self.logradouro = self._verificar_logradouro(logradouro)
        self.numero = self._verificar_numero(numero)
        self.complemento = self._verificar_complemento(complemento)
        self.cep = self._verificar_cep(cep)
        self.cidade = self._verificar_cidade(cidade)
        self.uf = uf

    def _verificar_logradouro(self, valor):
        self._verificar_logradouro_tipo_invalido(valor)

        self.logradouro = valor
        return self.logradouro
    
    def _verificar_numero(self,valor):
        self._verificar_numero_tipo_invalido(valor)

        self.numero = valor
        return self.numero

    def _verificar_complemento(self,valor):
        self._verificar_complemento_tipo_invalido(valor)

        self.complemento = valor
        return self.complemento

    def _verificar_cep(self,valor):
        self._verificar_cep_tipo_invalido(valor)

        self.cep = valor
        return self.cep
    
    def _verificar_cidade(self,valor):
        self._verificar_cidade_tipo_invalido(valor)

        self.cidade = valor
        return self.cidade
    
    def _verificar_logradouro_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Logradouro inválido!")

    def _verificar_numero_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Número inválido!")

    def _verificar_complemento_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Complemento inválido!")

    def _verificar_cep_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("CEP inválido!")
        
    def _verificar_cidade_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Cidade inválida!")

    def __str__(self) -> str:
        return (f"\nLogradouro: {self.logradouro}"
                f"\nNúmero: {self.numero}"
                f"\nComplemento: {self.complemento}"
                f"\nCep: {self.cep}"
                f"\nCidade: {self.cidade}"
                f"\nUnidade Federativa: {self.uf.nome}/{self.uf.sigla}")
