import os
from flask import Flask, render_template
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

# Define Flask app
app = Flask(__name__)


# Define mongo db connection using srv
app.config["MONGO_URI"]= os.environ.get('MONGO_URI')


# Define mongo connection method using PyMongo
mongo = PyMongo(app)

# Define app entry route and main page url
# using render template method and add db query
@app.route('/')
@app.route('/get_books')
def get_books():
    return render_template("books.html", books=mongo.db.Books.find())


# Creating like function what updates one book entry using it's _id
# use the update_one method with the $inc operator
@app.route('/like_this/<book_id>', methods=["GET", "POST"])
def like_this(book_id):
    book=mongo.db.Books.update_one({"_id": ObjectId(book_id)}, { "$inc": { 'likes': 1 } })
    return render_template("books.html", books=mongo.db.Books.find())


# Creating dislike function what updates one book entry using it's _id
# use the update_one method with the $inc operator
@app.route('/dislike_this/<book_id>', methods=["GET", "POST"])
def dislike_this(book_id):
    book=mongo.db.Books.update_one({"_id": ObjectId(book_id)}, { "$inc": { 'dislikes': 1 } })
    return render_template("books.html", books=mongo.db.Books.find())


# Define route for about book using the book's id from mongo
# using the find_one query with the _id
@app.route('/about_book/<book_id>')
def about_book(book_id):
    return render_template("aboutbook.html", 
    book=mongo.db.Books.find_one({"_id": ObjectId(book_id)}))


# Configuration of the app using env vars
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')), 
    debug=True)
