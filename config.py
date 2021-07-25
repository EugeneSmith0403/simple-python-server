from adapters.json import JsonAdapter
from classes.test import Test
from classes.test2 import Test2
from db.connectors.sqlLiteConnector import SqlLiteConnector
from db.dbconnection import DbConnection
from models.User import User
from routes.example import Example
from routes.router import Router

routesList = {
    '/': Example
}


dependencies = [
    Test(),
    Test2(),
    DbConnection(SqlLiteConnector({"fileName": "db.db"})),
    Router(routesList, JsonAdapter)
]

models = [
    User
]
