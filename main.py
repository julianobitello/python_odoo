from models.produto import Produto
from services.produto_service import ProdutoService

produto1 = Produto("Mouse Gamer", 150.90, 30)
produto2 = Produto("Monitor Gamer", 1500.90, 5)


produtoService = ProdutoService() #Criando isntancia
produtoService.cadastrar(produto1)
produtoService.cadastrar(produto2)
produtos = produtoService.listar()
for produto in produtos:
    print(produto.to_dict())

print("---------------------------------------------------------------------------------")
# produto_encontrado = produtoService.buscar_por_nome("teclado")
# print(produto_encontrado.nome if produto_encontrado else "Produto não encontrado")

print("---------------------------------------------------------------------------------")

produtoService.atualizar(
    "Mouse Gamer",
    Produto("Webcam", 50.90, 10)
)

produtos = produtoService.listar()

for produto in produtos:
    print(produto.to_dict())