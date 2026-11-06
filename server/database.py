# Simulação de base de dados no servidor
LIVROS_DB = [
    {"id": 1, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "preco": 45.0, "estoque": 3},
    {"id": 2, "titulo": "1984", "autor": "George Orwell", "genero": "Ficção", "preco": 30.0, "estoque": 5},
    {"id": 3, "titulo": "Senhor dos Anéis", "autor": "J.R.R. Tolkien", "genero": "Fantasia", "preco": 60.0, "estoque": 1},
]


def buscar_livros(genero=None):
    if not genero:
        return LIVROS_DB
    return [l for l in LIVROS_DB if l["genero"].lower() == genero.lower()]


def buscar_por_id(livro_id):
    return next((l for l in LIVROS_DB if l["id"] == livro_id), None)


def listar_generos():
    return sorted({l["genero"] for l in LIVROS_DB})
