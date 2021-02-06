import json
from datetime import datetime, date
from flask import request, jsonify

from models import Products
from __init__ import flask_app, db


# lists all the products
@flask_app.route('/products/list',methods=['GET'])
def list_products():
    products = db.query(Products).all()
    result = []
    for product in products:
        result.append(product._dump())

    return jsonify({'result':result})


# adds a new record to people collection
@flask_app.route('/products/add', methods=['POST'])
def add_new_product():
    body = json.loads(request.data)
    name = body.get('name',None)
    if name is None:
        return jsonify({'error':'name cannot be null'})
    new_product = Products(name=name)
    db.add(new_product)
    return jsonify({'result':new_product._dump()})


# edits record in people collection
@flask_app.route('/products/edit',methods=['PUT'])
def edit_product():
    body = json.loads(request.data)
    key = body.get('_key',None)
    if key is None:
        return jsonify({'error':'key cannot be null'})

    name = body.get('name',None)
    if name is None:
        return jsonify({'error':'name cannot be null'})

    product = db.query(Products).by_key(key)
    product.name = name
    db.update(product)

    return jsonify({'result':product._dump()})


# deletes a record in people collection
@flask_app.route('/products/remove', methods=['DELETE'])
def delete_person():
    body = json.loads(request.data)
    key = body.get('_key', None)
    if key is None:
        return jsonify({'error': 'key cannot be null'})

    product = db.query(Products).by_key(key)
    db.delete(product)
    return jsonify({'result': 'success'})
