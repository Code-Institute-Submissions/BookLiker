import os
from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Define Flask app
app = Flask(__name__)


# Define mongo db connection using srv
app.config["MONGO_URI"] = os.environ.get('MONGO_URI')


# Define mongo connection method using PyMongo
mongo = PyMongo(app)


# Define app entry route and main page url
# using render template method and add db query
@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html",
                           books=mongo.db.Books.find(), genres=mongo.db.Genres.find())


# Creating like function what updates one book entry using it's _id
# use the update_one method with the $inc operator
@app.route('/like_this/<book_id>', methods=["GET", "POST"])
def like_this(book_id):
    book = mongo.db.Books.update_one(
        {"_id": ObjectId(book_id)}, {"$inc": {'likes': 1}})
    return redirect(request.referrer)


# Creating dislike function what updates one book entry using it's _id
# use the update_one method with the $inc operator
@app.route('/dislike_this/<book_id>', methods=["GET", "POST"])
def dislike_this(book_id):
    book = mongo.db.Books.update_one({"_id": ObjectId(book_id)}, {
                                     "$inc": {'dislikes': 1}})
    return redirect(request.referrer)


# Define route for about book using the book's id from mongo
# using the find_one query with the _id
@app.route('/about_book/<book_id>')
def about_book(book_id):
    return render_template("aboutbook.html",
                           book=mongo.db.Books.find_one({"_id": ObjectId(book_id)}), genres=mongo.db.Genres.find())


# Create add_book method to redirect to the form page where can add new book to the library
# then call insert_book method to insert to the collection
# Called from the top nav bar
@app.route('/add_book')
def add_book():
    return render_template("addbook.html", gens=mongo.db.Genres.find(), genres=mongo.db.Genres.find())

# Create insert_book to be called from the add book form
@app.route('/insert_book', methods=["POST"])
def insert_book():
    books = mongo.db.Books
    books.insert_one(request.form.to_dict())
    return redirect(url_for('get_books'))


# Create edit book where can update or delete a book methods can be called from
@app.route('/edit_book/<book_id>', methods=["GET"])
def edit_book(book_id):
    return render_template("editbook.html",
                           book=mongo.db.Books.find_one({"_id": ObjectId(book_id)}), gens=mongo.db.Genres.find())

# Create update book method so can be called from the edit book page
@app.route('/update_book/<book_id>', methods=["POST"])
def update_book(book_id):
    book = mongo.db.Books.update_one(
        {"_id": ObjectId(book_id)},
        {"$set": {
            'title': request.form.get('title'),
            'author': request.form.get('author'),
            'description': request.form.get('description'),
            'url_to_buy': request.form.get('url_to_buy'),
            'image_url': request.form.get('image_url'),
            'genre': request.form.get('genre'),
        }}
    )
    return redirect(url_for("get_books"))


# Create delete_book to remove book from the db can be called from edit_book
@app.route('/delete_book/<book_id>', methods=["GET", "POST"])
def delete_book(book_id):
    mongo.db.Books.remove({'_id': ObjectId(book_id)})
    return redirect(url_for("get_books"))


# Create add_genre
@app.route('/add_genre')
def add_genre():
    return render_template("addgenre.html", genres=mongo.db.Genres.find())


# Create insert genre method to add new genre to the db
@app.route('/insert_genre', methods=["POST"])
def insert_genre():
    genres = mongo.db.Genres
    genres.insert_one(request.form.to_dict())
    return redirect(url_for('get_books'))


# Create filter method to filter books by genre
@app.route('/filtered_books/<genre>')
def filtered_books(genre):
    books = mongo.db.Books
    results = books.find({"genre": genre})
    return render_template("books.html",
                           books=results, genres=mongo.db.Genres.find())


# Create filtered view for the mosted liked 9 books
@app.route('/most_liked')
def most_liked():
    books = mongo.db.Books
    results = books.find().sort([('likes', -1)]).limit(9)
    return render_template("books.html", books=results, genres=mongo.db.Genres.find())

# Create alphabetical ordered book list
@app.route('/alphabetical_title')
def alphabetical_title():
    return render_template("books.html", books=mongo.db.Books.find().sort("title"), genres=mongo.db.Genres.find())


# Create alphabetical ordered book list
@app.route('/alphabetical_author')
def alphabetical_author():
    return render_template("books.html", books=mongo.db.Books.find().sort("author"), genres=mongo.db.Genres.find())


# Create route for sort form
@app.route('/sort')
def sort():
    # create instance from the full db
    books = mongo.db.Books.find().sort("author")
    genres = mongo.db.Genres.find().sort("genre")
    book_count = books.count()
    booklist = list(books)
    authors = ["All"]
    cats = ["All"]
    limit = 0
    for i in range(0, book_count):
        if booklist[i]["author"] not in authors:
            authors.append(booklist[i]["author"])
        if booklist[i]["genre"] not in cats:
            cats.append(booklist[i]["genre"])
    print(cats)
    return render_template("sortbooks.html", books=books, genres=genres, names=authors, cats=cats)


# Configuration of the app using env vars
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
