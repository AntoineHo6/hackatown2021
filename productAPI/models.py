from arango_orm import Collection, fields
from arango_orm.fields import String, Date,Integer,Field,DateTime,List,Boolean
from arango_orm import Graph, GraphConnection, Relation


class Products(Collection):
    __collection__ = 'products'

    _key = String(required=True, allow_none=False)
    name = String(required=True, allow_none=False)
    description = String()
    imageLocation = String()
    price = float()
    discount = float()

    def __str__(self):
        return "<Subject({})>".format(self.name)

class Categories(Collection):
    __collection__ = 'productCategories'

    _key = String(required=True, allow_none=False)
    name = String(required=True, allow_none=False)
    description = String()

    def __str__(self):
        return "<Subject({})>".format(self.name)
 

#TODO seperate this into another api?
class Shops(Collection):
    __collection__ = 'shops'

    _key = String(required=True, allow_none=False)
    name = String(required=True, allow_none=False)
    slogan = String()
    description = String()
    logoLocation = String()
    geolocation = Field()       #what kind of datatype is geolocal data?
    foundingDate = Date()

    def __str__(self):
        return "<Subject({})>".format(self.name)

class Category_Relation(Relation):
    __collection__ = 'category_relation'
    _key = String(required=True)

class Shop_Relation(Relation):
    __collection__ = 'shop_relation'
    _key = String(required=True)

class Product_Graph(Graph):
    __graph__ = 'product_graph'
    graph_connections = [
            GraphConnection(Products, Shop_Relation, Shops),
            GraphConnection(Categories, Category_Relation, Products)
    ]
