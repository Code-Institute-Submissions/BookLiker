import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


app = Flask(__name__)


app.config["MONGO_URI"]= os.environ.get('MONGO_URI')


mongo = PyMongo(app)

@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.Books.find())


@app.route('/about_book/<book_id>')
def about_book(book_id):
    return render_template("aboutbook.html", 
    book=mongo.db.Books.find_one({"_id": ObjectId(book_id)}))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)
