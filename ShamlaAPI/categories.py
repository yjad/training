#! getcategories-API using flask
from flask import Flask, jsonify, abort, make_response, request
from types import *
from DBhandling import *
import logging

logging.basicConfig(level=logging.DEBUG)


SERVER_URL = 'booksapi.islam-db.com'
app = Flask(__name__)

def validate_request_pagination(req):
    keywords = ""
    limit = 10
    offset = 0

    if 'keywords' in req.json and type(req.json['keywords']) != str:
        print('keywords is not string')
        return -1

    if 'limit' in req.json and type(req.json['limit']) is not int:
        print ('limit is not int')
        return -1

    if 'offset' in req.json and type(req.json['offset']) is not int:
        print ('offset is not int')
        return -1

    if 'keywords' in request.json:
        keywords = request.json['keywords']

    if 'limit' in request.json:
        limit = request.json['limit']

    if 'offset' in request.json:
        offset = request.json['offset']

    return 0, keywords, limit, offset

def validate_categories_request(req):
    return validate_request_pagination(req)


def validate_books_request(req):
    return validate_request_pagination(req)


@app.route('/api/v1.0/categories/<int:parentid>/more/<int:id>', methods = ['POST'])
def get_categories(parentid, id):
    status, keywords, limit, offset = validate_books_request(request)

    if status != 0:
        abort(400, status)

    sql = f"SELECT id, name FROM cat WHERE catord = {parentid} LIMIT {limit}"
    #cmd = f"SELECT id, name FROM cat WHERE catord = {parentid}"
    logging.debug(sql)
    categs = categories_db(sql)
    return jsonify({'Getgories': categs})

@app.route('/api/v1.0/books/<int:id>', methods = ['POST'])
def books(id):

    status, keywords,limit, offset = validate_books_request(request)
    if status != 0:
        abort(400, status)

# case 1: id =0, return all book details
    if id != 0:
        sql = f"SELECT * FROM bok WHERE bkid = {id}"
        logging.debug(sql)
        book_list = books_db(sql)
        return jsonify({'books': book_list})
    else:
        sql = f"SELECT bkid, bk FROM bok WHERE bk like '%{keywords}%' LIMIT {limit} OFFSET {offset} "
        logging.debug(sql)
        book_list = books_db(sql)
        return jsonify({'books': book_list})
    # case 2: no id is provided, return book short details with proper pagination
# case 3:

    sql = f"SELECT id, name FROM cat WHERE catord = {parentid} LIMIT {limit}"
    #cmd = f"SELECT id, name FROM cat WHERE catord = {parentid}"
    logging.debug(sql)
    categs = categories_db(sql)
    return jsonify({'Getgories': categs})

if __name__ == '__main__':
    app.run(debug = True)



