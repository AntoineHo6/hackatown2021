import json
from datetime import datetime, date
from flask import request, jsonify

from models import Products, Categories
from __init__ import flask_app, db


# lists all the products
@flask_app.route('/products/list',methods=['GET'])
def list_products():
    products = db.query(Products).all()
    result = []
    for product in products:
        result.append(product._dump())

    return jsonify({'result':result})


# adds a new record to products collection
@flask_app.route('/products/add', methods=['POST'])
def add_new_product():
    body = json.loads(request.data)
    name = body.get('name',None)
    if name is None:
        return jsonify({'error':'name cannot be null'})
    description = body.get('description',None)
    imageLocation = body.get('imageLocation',None)
    price = body.get('price',None)
    discount = body.get('discount',None)
    new_product = Products(name=name, description=description, imageLocation=imageLocation, price=price, discount=discount)
    db.add(new_product)
    return jsonify({'result':new_product._dump()})


# edits record in products collection
@flask_app.route('/products/edit',methods=['PUT'])
def edit_product():
    body = json.loads(request.data)
    key = body.get('_key',None)
    if key is None:
        return jsonify({'error':'key cannot be null'})
    product = db.query(Products).by_key(key)

    # TODO this but programmatically if things change
    name = body.get('name',None)
    if name is not None:
        product.name = name
    description = body.get('description',None)
    if description is not None:
        product.description = description
    imageLocation = body.get('imageLocation',None)
    if imageLocation is not None:
        product.imageLocation = imageLocation
    price = body.get('price',None)
    if price is not None:
        product.price = price
    discount = body.get('discount',None)
    if discount is not None:
        product.discount = discount
    db.update(product)

    return jsonify({'result':product._dump()})


# deletes a record in products collection
@flask_app.route('/products/remove', methods=['DELETE'])
def delete_product():
    body = json.loads(request.data)
    key = body.get('_key', None)
    if key is None:
        return jsonify({'error': 'key cannot be null'})

    product = db.query(Products).by_key(key)
    db.delete(product)
    return jsonify({'result': 'success'})


# lists all the categories
@flask_app.route('/categories/list',methods=['GET'])
def list_categories():
    categories = db.query(Categories).all()
    result = []
    for category in categories:
        result.append(category._dump())

    return jsonify({'result':result})


# adds a new record to productCategories collection
@flask_app.route('/categories/add', methods=['POST'])
def add_new_category():
    body = json.loads(request.data)
    name = body.get('name',None)
    if name is None:
        return jsonify({'error':'name cannot be null'})
    description = body.get('description',None)
    new_category = Categories(name=name, description=description)
    db.add(new_category)
    return jsonify({'result':new_category._dump()})


# edits record in productCategories collection
@flask_app.route('/categories/edit',methods=['PUT'])
def edit_category():
    body = json.loads(request.data)
    key = body.get('_key',None)
    if key is None:
        return jsonify({'error':'key cannot be null'})
    category = db.query(Categories).by_key(key)

    # TODO this but programmatically if things change
    name = body.get('name',None)
    if name is not None:
        category.name = name
    description = body.get('description',None)
    if description is not None:
        category.description = description
    db.update(category)

    return jsonify({'result':category._dump()})


# deletes a record in productCategories collection
@flask_app.route('/categories/remove', methods=['DELETE'])
def delete_category():
    body = json.loads(request.data)
    key = body.get('_key', None)
    if key is None:
        return jsonify({'error': 'key cannot be null'})

    category = db.query(Categories).by_key(key)
    db.delete(category)
    return jsonify({'result': 'success'})


