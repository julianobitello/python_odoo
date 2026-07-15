class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int):
        self.nome = nome
        self.preco  = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }

    def atualizar_preco(self, preco: float  ):
        self.preco = preco
