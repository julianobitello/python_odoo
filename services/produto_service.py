from models.produto import Produto
from database import conectar

class ProdutoService:
    def __init__(self):
       self.produtos: list[Produto] = []

    def cadastrar(self, produto: Produto):
        conexao = conectar("sistema")
        cursor = conexao.cursor()
        cursor.execute(
            """
            INSERT INTO produtos(nome, preco, quantidade)
            VALUES (?, ?, ?)
            """,
            (
                produto.nome,
                produto.preco,
                produto.quantidade
            )
        )
        conexao.commit()

        produto.id = cursor.lastrowid
        cursor.close()
        conexao.close()

    def listar(self):
        conexao = conectar("sistema")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM produtos
        """)

        dados = cursor.fetchall()

        produtos = []

        for produto_banco in dados:
            produto = Produto(
                produto_banco[1],
                produto_banco[2],
                produto_banco[3],
                produto_banco[0]
            )

            produtos.append(produto)

        cursor.close()
        conexao.close()

        return produtos

    def buscar_por_nome(self, nome: str):
        conexao = conectar("sistema")
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT * FROM produtos WHERE nome LIKE ?
        """, (f"%{nome}%",))

        produto_banco = cursor.fetchone()

        if produto_banco:
            produto = Produto(
                produto_banco[1],
                produto_banco[2],
                produto_banco[3],
                produto_banco[0]
            )

            return produto

        return None


    def atualizar(self, produto: Produto):
        conexao = conectar("sistema")
        cursor = conexao.cursor()
        cursor.execute("""
            UPDATE produtos SET nome = ?, 
            preco = ?, 
            quantidade = ?
            WHERE id = ?
        """, (produto.nome, produto.preco, produto.quantidade, produto.id))
        conexao.commit()
        cursor.close()
        conexao.close()
        return produto

    def deletar(self, produto: Produto):
        conexao = conectar("sistema")
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM produtos WHERE id = ?
        """, (produto.id,))

        conexao.commit()

        deletado = cursor.rowcount > 0

        cursor.close()
        conexao.close()

        return deletado