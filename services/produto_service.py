from models.produto import Produto

class ProdutoService:
    def __init__(self):
       self.produtos: list[Produto] = []

    def cadastrar(self, produto: Produto):
        self.produtos.append(produto)

    def listar(self):
        return self.produtos

    def buscar_por_nome(self, nome: str):
        for produto in self.produtos:
            produto_nome = produto.nome.lower()
            if nome.lower() in produto_nome:
                return produto

        return None

    def atualizar(self, nome, produto: Produto):
        for indice, produto_lista in enumerate(self.produtos):
            if produto_lista.nome.lower() == nome.lower():
                self.produtos[indice] = produto
                return True

        return False

    def remover(self, nome: str) -> bool:
        for indice, produto_lista in enumerate(self.produtos):
            if produto_lista.nome.lower() == nome.lower():
                self.produtos.pop(indice)
                return True

        return False

