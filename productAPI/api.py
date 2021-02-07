import json
from datetime import datetime, date
from flask import request, jsonify

from models import Products, Categories, Shops, Category_Relation, Shop_Relation
from __init__ import flask_app, db, product_graph


# lists all the products
@flask_app.route('/products/list',methods=['GET'])
def list_products():
    products = db.query(Products).all()
    result = []
    for product in products:
        product_dict = product._dump()
        product_graph.expand(product, depth=1, direction='any')
        shop_name = product._relations['shop_relation'][0]._object_to.name
        category_name = product._relations['category_relation'][0]._object_from.name
        product_dict['shop'] = shop_name
        product_dict['category'] = category_name
        result.append(product_dict)

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

    #add relations
    shop_key = body.get('shop_key',None)
    if shop_key is not None:
        shop = db.query(Shops).by_key(shop_key)
        if shop is not None:
            db.add(product_graph.relation(new_product, Shop_Relation(), shop))
    category_key = body.get('category_key',None)
    if category_key is not None:
        category = db.query(Categories).by_key(category_key)
        if category is not None:
            db.add(product_graph.relation(relation_from=category, relation=Shop_Relation(), relation_to=new_product))

    return jsonify({'result':new_product._dump()})


# edits record in products collection
@flask_app.route('/products/edit',methods=['PUT'])
def edit_product():
    body = json.loads(request.data)
    key = body.get('_key',None)
    if key is None:
        return jsonify({'error':'key cannot be null'})
    product = db.query(Products).by_key(key)
    if product is None:
        return jsonify({'error':'product not found'})

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

    #relations
    category_key = body.get('category_key', None)
    category = db.query(Categories).by_key(category_key)
    if category is not None:
        # find old category relation and delete it
        old_category_relation = db.query(Category_Relation).filter('_to==@_to',_to=product._id).first()
        db.delete(old_category_relation)
        # add new category relation
        db.add(product_graph.relation(relation_from=category, relation=Category_Relation(), relation_to=product))
    shop_key = body.get('shop_key', None)
    shop = db.query(Shops).by_key(shop_key)
    if shop is not None:
        # find old assignee relation and delete it
        old_shop_relation = db.query(Shop_Relation).filter('_from==@_from',_from=product._id).first()
        db.delete(old_shop_relation)
        # add new assignee relation
        db.add(product_graph.relation(relation_from=product, relation=Shop_Relation(), relation_to=shop))

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


#TODO seperate this out into another API
# lists all the shops
@flask_app.route('/shops/list',methods=['GET'])
def list_shops():
    shops = db.query(Shops).all()
    result = []
    for shop in shops:
        result.append(shop._dump())

    return jsonify({'result':result})


# adds a new record to shops collection
@flask_app.route('/shops/add', methods=['POST'])
def add_new_shop():
    body = json.loads(request.data)
    name = body.get('name',None)
    if name is None:
        return jsonify({'error':'name cannot be null'})
    slogan = body.get('slogan',None)
    description = body.get('description',None)
    logoLocation = body.get('logoLocation',None)
    geolocation = body.get('geolocation',None)
    foundingDate = body.get('foundingDate',None)
    new_shop = Shops(name=name, slogan=slogan, description=description, logoLocation=logoLocation, geolocation=geolocation, foundingDate=foundingDate)
    db.add(new_shop)
    return jsonify({'result':new_shop._dump()})


# edits record in shops collection
@flask_app.route('/shops/edit',methods=['PUT'])
def edit_shop():
    body = json.loads(request.data)
    key = body.get('_key',None)
    if key is None:
        return jsonify({'error':'key cannot be null'})
    shop = db.query(Shops).by_key(key)

    # TODO this but programmatically if things change
    name = body.get('name',None)
    if name is not None:
        shop.name = name
    slogan = body.get('slogan',None)
    if slogan is not None:
        shop.slogan = slogan
    description = body.get('description',None)
    if description is not None:
        shop.description = description
    logoLocation = body.get('logoLocation',None)
    if logoLocation is not None:
        shop.logoLocation = logoLocation
    geolocation = body.get('geolocation',None)
    if geolocation is not None:
        shop.geolocation = geolocation
    foundingDate = body.get('foundingDate',None)
    if foundingDate is not None:
        shop.foundingDate = foundingDate
    db.update(shop)

    return jsonify({'result':shop._dump()})


# deletes a record in products collection
@flask_app.route('/shop/remove', methods=['DELETE'])
def delete_shop():
    body = json.loads(request.data)
    key = body.get('_key', None)
    if key is None:
        return jsonify({'error': 'key cannot be null'})

    shop = db.query(Shops).by_key(key)
    db.delete(shop)
    return jsonify({'result': 'success'})
