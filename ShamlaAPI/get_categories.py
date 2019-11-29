#! getcategories-API using flask
from flask import Flask, jsonify, abort, make_response, request
from types import *
from DBhandling import *
import logging

logging.basicConfig(level=logging.DEBUG)


SERVER_URL = 'booksapi.islam-db.com'
app = Flask(__name__)


def validate_get_categories_request(req):
    if not req.json or not 'keywords' in req.json:
        print ('no json')
        return -1
    if 'keywords' in req.json and type(req.json['keywords']) != str:
        print('title is not string')
        return -2
    if 'limit' in req.json and type(req.json['limit']) is not int:
        print ('description not str')
        return -3
    return 0

@app.route('/api/v1.0/getcategories/<int:parentid>/more/<int:id>', methods = ['POST'])
def get_categories(parentid, id):

    status = validate_get_categories_request(request)
    if status != 0:
        abort(400, status)

    if 'limit' in request.json:
        limit = request.json['limit']
    else:
        limit =1

    cmd = f"SELECT id, name FROM cat WHERE catord = {parentid} LIMIT {limit}"
    #cmd = f"SELECT id, name FROM cat WHERE catord = {parentid}"
    logging.debug(cmd)
    categs = get_categories_db(cmd)
    return jsonify({'Getgories': categs})


if __name__ == '__main__':
    app.run(debug = True)



