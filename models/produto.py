class Produto:
    def __init__(self, nome: str, preco: float, quantidade: int, id=None):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "preco": self.preco,
            "quantidade": self.quantidade
        }