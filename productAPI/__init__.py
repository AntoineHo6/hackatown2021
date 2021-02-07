from flask import Flask
from flask_cors import CORS
from arango import ArangoClient
from arango_orm import Database
from models import Products, Categories, Shops, Product_Graph

flask_app = Flask(__name__)
CORS(flask_app)

client = ArangoClient(hosts='http://hackatown-database:8529')

# Retrieve _system database from arangodb (_system database is default)
sys_db = client.db('_system', username='root', password='securepassword')

# Check if task database exist, create one if doesnt exist
if not sys_db.has_database('hackatown'):
    sys_db.create_database('hackatown')

# Initialize database
db_client = client.db('hackatown', username='root', password='securepassword')
db = Database(db_client)
product_graph = Product_Graph(connection=db)

db.create_all([Products, Categories, Shops, Product_Graph])
