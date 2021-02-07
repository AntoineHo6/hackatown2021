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
