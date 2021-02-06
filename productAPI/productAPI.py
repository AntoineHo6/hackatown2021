from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Product(Resource):
    def get(self):
        return {
            'product': ['Mechanical Keyboard',
                        'Euclid\'s The Elements',
                        'Handmade wooden bowl']
        }

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8393, debug=True)