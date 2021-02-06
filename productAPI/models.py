from arango_orm import Collection, fields
from arango_orm.fields import String, Date,Integer,Field,DateTime,List,Boolean
from arango_orm import Graph, GraphConnection, Relation


class Products(Collection):
    __collection__ = 'products'

    _key = String(required=True)
    name = String(required=True)

    def __str__(self):
        return "<Subject({})>".format(self.name)
