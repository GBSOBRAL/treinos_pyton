# API - É um lugar para disponibilizar recursos e/ou funcionalidades
# 1. Objetivo Criar um api de disponibiliza a consulta, criação, edição e exclusão de livros
# 2. URL base - localhost
# 3. Endpoints
# - localhost/livros (GET)
# - localhost/livros/id (GET)
# - localhost/livro/id (PUT)
# - localhost/livro/id (DELETE)
# 4. Quais recursos - Livros

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
    'id': 1,
    'título': 'O Senhor dos Anéis - A Sociedade do Anel',
    'autor': 'J.R.R Tolkien'
    },
    {
    'id': 2,
    'título': 'Harry Potter e a Pedra Filosofal',
    'autor': 'J.K Howling'
    },
    {
    'id': 3,
    'título': 'James Clear',
    'autor': 'Hábitos Atômicos'
    }
]

#Consultar Todos
@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

#Consultar por id
@app.route('/books/<int:id>',methods=['GET'])
def get_books_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)

#Editar livro por id
@app.route('/books/<int:id>',methods=['PUT'])
def edit_books_by_id(id):
    book_edit = request.get_json()
    for indice,book in enumerate(books):
        if book.get('id') == id:
            books[indice].update(book_edit)
            return jsonify(books[indice])
        
#Incluir Livro
@app.route('/books',methods=['POST'])
def include_books():
    new_book = request.get_json()
    books.append(new_book)

    return jsonify(books)

#Apagar Livro
@app.route('/books/<int:id>',methods=['DELETE'])
def delete_books_by_id(id):
    for indice,book in enumerate(books):
        if book.get('id') == id:
            del books[indice]
            
    return jsonify(books)
        
app.run(port=5000,host='localhost',debug=True)