from database import criar_tabelas
from models.produto import Produto
from services.produto_service import ProdutoService

criar_tabelas()

produto_service = ProdutoService()

# CREATE
produto = Produto("Teclado Mecânico", 300.00, 15)

produto_service.cadastrar(produto)

print("========== PRODUTOS APÓS CADASTRO ==========")

produtos = produto_service.listar()

for produto in produtos:
    print(produto.to_dict())


# READ
print("========== BUSCAR PRODUTO ==========")

produto_encontrado = produto_service.buscar_por_nome("Teclado")

if produto_encontrado:
    print(produto_encontrado.to_dict())
else:
    print("Produto não encontrado")


# UPDATE
print("========== ATUALIZANDO ==========")

produto_encontrado.nome = "Teclado RGB"
produto_encontrado.preco = 450.00
produto_encontrado.quantidade = 10

produto_service.atualizar(produto_encontrado)

print("Produto atualizado!")


# LISTAR APÓS UPDATE
print("========== APÓS UPDATE ==========")

produtos = produto_service.listar()

for produto in produtos:
    print(produto.to_dict())


# DELETE
print("========== DELETANDO ==========")

produto_service.deletar(produto_encontrado)


# LISTAR APÓS DELETE
print("========== APÓS DELETE ==========")

produtos = produto_service.listar()

for produto in produtos:
    print(produto.to_dict())