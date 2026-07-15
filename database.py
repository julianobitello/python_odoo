import sqlite3

def conectar(nome_banco):
    conexao = sqlite3.connect(f'{nome_banco}.db')
    return conexao


def criar_tabelas():
    conexao = conectar("sistema")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS produtos(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            preco REAL,
            quantidade INTEGER
        )
    """)
    conexao.commit()
    conexao.close()