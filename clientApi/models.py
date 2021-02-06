from arango_orm import Collection, fields
from arango_orm.fields import String, Date,Integer,Field,DateTime,List,Boolean
from arango_orm import Graph, GraphConnection, Relation


class Clients(Collection):
    __collection__ = 'Clients'

    _key = String(required=True)
    name = String(required=True)
    username = String(required=True)
    password = String(required=True)
    courriel = String(required=True)

    def __str__(self):
        return "<Subject({}, {}, {}, {})>".format(self.name, self.username, self.password, self.courriel)
