from classes.test import Test
from classes.test2 import Test2
from db.dbconnection import DbConnection
from db.connectors.sqlLiteConnector import SqlLiteConnector
from dependencyInjection.di import Di, injectable

listDependencies = [
    Test(),
    Test2(),
    DbConnection(SqlLiteConnector({"fileName": ""})),
]

test = DbConnection(SqlLiteConnector({"fileName": ""}))

print(listDependencies)

instanceDi = Di(listDependencies)


@injectable(DbConnection)
def callBack(*args, DbConnection):
    print('callback')
    print(args)
    print(DbConnection.getInstance())


callBack(1, 23, 4)
