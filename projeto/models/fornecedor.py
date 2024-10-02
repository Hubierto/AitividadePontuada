from projeto.models.endereco import Endereco
from projeto.models.juridica import Juridica

class Fornecedor(Juridica):
    def __init__(self, id: int, nome: str, telefone: str, email: str, endereco: Endereco, cnpj: str, inscricaoestadual: str, produto: str) -> None:
        super().__init__(id, nome, telefone, email, endereco, cnpj, inscricaoestadual)
        self.produto = self._verificar_produto(produto)

    def _verificar_produto(self,valor):
        self._verificar_produto_tipo_invalido(valor)

        self.produto = valor
        return self.produto

    def _verificar_produto_tipo_invalido(self,valor):
        if not isinstance(valor, str):
            raise TypeError("Produto é inválido!")

    def __str__(self) -> str:
        return (f"{super().__str__()}"
                f"\nProduto: {self.produto}")