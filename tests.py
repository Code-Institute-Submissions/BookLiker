""" 
Tests conatining page loading and business logic

"""
import os
import unittest
import re

from flask_pymongo import PyMongo

import app as app_module

app = app_module.app

app.config["TESTING"] = True
app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

mongo = PyMongo(app)
app_module.mongo = mongo


class AppTests(unittest.TestCase):
    """Test, tyhe Index page loading"""
    
    def test_index(self):
        self.client = app.test_client()
        res = self.client.get('/')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'BookLiker' in data

    """Test, the books loading"""
    def test_books(self):
        self.client = app.test_client()
        res = self.client.get('/get_books')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Harry' in data

    """Test, about_book functioning"""
    def test_aboutbook(self):
        self.client = app.test_client()
        res = self.client.get('/about_book/5ea36c06abcc68c64191c278')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Chamber' in data

    """Test, edit book function"""
    def test_editbook(self):
        self.client = app.test_client()
        res = self.client.get('/edit_book/5ea36c06abcc68c64191c278')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert 'Chamber' in data

    """Test, add book function"""
    def test_addbook(self):
        self.client = app.test_client()
        res = self.client.post('/insert_book', follow_redirects=True, data={
            'title': 'My Test Book',
            'author': 'Me Myself and I',
            'description': 'Test Description',
            'url_to_buy': 'Test URL',
            'image_url': 'Test URL 2',
            'genre': 'Test Genre',
            'likes': '0' ,
            'dislikes': '0'
        })
        data = res.data.decode('utf-8')
        assert 'Harry' in data

    """Test, like book function"""
    def test_likethis(self):
        self.client = app.test_client()
        res = self.client.get('/like_this/5ea36c06abcc68c64191c278')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert '75' in data

    """Test, dislike book function"""
    def test_dislikethis(self):
        self.client = app.test_client()
        res = self.client.get('/dislike_this/5ea36c06abcc68c64191c278')
        data = res.data.decode('utf-8')
        assert res.status == '200 OK'
        assert '22' in data

    """Test, update book function"""
    def test_updatebook(self):
        self.client = app.test_client()
        res = self.client.post('/update_book/5ed14103458a2fe42c75931e', follow_redirects=True, data={
            'title': 'My Updated Test Book',
            'author': 'Me Myself and I',
            'description': 'Test Description',
            'url_to_buy': 'Test URL',
            'image_url': 'Test URL 2',
            'genre': 'Test Genre',
            'likes': '0' ,
            'dislikes': '0'
        })
        data = res.data.decode('utf-8')
        assert 'Harry' in data

    """Test, delete book function"""
    def test_deletebook(self):
        self.client = app.test_client()
        res = self.client.get('/delete_book/5ed142369c031fd5902c4b4c')
        data = res.data.decode('utf-8')
        assert res.status == '404'
        assert 'Chamber' in data


"""This is to run all tests with  "python3 tests.py" command"""
if __name__ == '__main__':
    unittest.main()


