# Python Odoo - CRUD de Produtos

Projeto desenvolvido para praticar os fundamentos de Python, Programação Orientada a Objetos (POO) e integração com banco de dados SQLite.

## Tecnologias

- Python 3
- SQLite
- Programação Orientada a Objetos (POO)

## Funcionalidades

- Cadastrar produto
- Listar produtos
- Buscar produto por nome
- Atualizar produto
- Deletar produto

## Estrutura do Projeto

```
python_odoo/
│
├── database.py
├── main.py
├── sistema.db
│
├── models/
│   └── produto.py
│
└── services/
    └── produto_service.py
```

## Modelo Produto

Cada produto possui os seguintes atributos:

- id
- nome
- preco
- quantidade

## Conceitos praticados

- Classes e Objetos
- Instanciação
- Métodos
- Encapsulamento
- CRUD
- SQLite
- SQL (CREATE, INSERT, SELECT, UPDATE e DELETE)
- Cursor
- Commit
- Conversão de dados do banco em objetos Python

## Como executar

Clone o repositório:

```bash
git clone https://github.com/julianobitello/python_odoo.git
```

Acesse a pasta:

```bash
cd python_odoo
```

Execute o projeto:

```bash
python main.py
```

## Objetivo

Este projeto foi desenvolvido com o objetivo de reforçar os fundamentos de Python e servir como preparação para oportunidades na área de desenvolvimento Python e Odoo.
