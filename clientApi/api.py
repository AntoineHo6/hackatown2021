import json
from datetime import datetime, date
from flask import request, jsonify

from models import Clients
from __init__ import flask_app, db


# lists all the clients
@flask_app.route('/clients/list',methods=['GET'])
def list_clients():
    clients = db.query(Clients).all()
    result = []
    for client in clients:
        result.append(client._dump())

    return jsonify({'result':result})


# adds a new record to people collection
@flask_app.route('/clients/add', methods=['POST'])
def add_new_client():
    body = json.loads(request.data)

    name = body.get('name',None)
    username = body.get('username',None)
    password = body.get('password',None)
    courriel = body.get('courriel',None)

    if name is None:
        return jsonify({'error':'name cannot be null'})

    if username is None:
        return jsonify({'error':'username cannot be null'})

    if password is None:
        return jsonify({'error':'password cannot be null'})

    if courriel is None:
        return jsonify({'error':'courriel cannot be null'})

    new_clients = Clients(name=name, username=username, password=password, courriel=courriel)
    db.add(new_client)
    return jsonify({'result':new_client._dump()})


# edits record in people collection
@flask_app.route('/clients/edit',methods=['PUT'])
def edit_client():
    body = json.loads(request.data)
    key = body.get('_key',None)
    if key is None:
        return jsonify({'error':'key cannot be null'})

    name = body.get('name',None)
    username = body.get('username',None)
    password = body.get('password',None)
    courriel = body.get('courriel',None)

    if name is None:
        return jsonify({'error':'name cannot be null'})

    if username is None:
        return jsonify({'error':'username cannot be null'})

    if password is None:
        return jsonify({'error':'password cannot be null'})

    if courriel is None:
        return jsonify({'error':'courriel cannot be null'})

    client = db.query(Clients).by_key(key)
    client.name = name
    client.username = username
    client.password = password
    client.courriel = courriel

    db.update(client)

    return jsonify({'result':client._dump()})


# deletes a record in people collection
@flask_app.route('/clients/remove', methods=['DELETE'])
def delete_clients():
    body = json.loads(request.data)
    key = body.get('_key', None)
    if key is None:
        return jsonify({'error': 'key cannot be null'})

    client = db.query(Clients).by_key(key)
    db.delete(client)
    return jsonify({'result': 'success'})
