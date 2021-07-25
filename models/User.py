from db.BaseDbModel import BaseDbModel
from db.dbconnection import DbConnection
from dependencyInjection.di import injectable


class User(BaseDbModel):
    dbConnection = None

    tableName = 'Users'

    @injectable(DbConnection)
    def __init__(self, DbConnection):
        self.dbConnection = DbConnection

    def select(self):
        # TODO make safety
        sql = "SELECT * FROM {table}".format(table=self.tableName)
        cur = self.dbConnection.getCursor().execute(sql)
        return self.convertDataFromTable(cur)

    def create(self, valuesDict):
        keys = tuple(valuesDict.keys())
        values = tuple(valuesDict.values())
        # TODO make safety
        sql = """
            INSERT INTO {table} {rows}
            VALUES{values}
        """.format(table=self.tableName, rows=keys, values=values)
        cur = self.dbConnection.getCursor()
        cur.execute(sql)
        self.dbConnection.commit()
        return cur.lastrowid


    def update(self, valuesDict, param):
        # TODO make safety
        sql = ''' UPDATE {table}
              SET name='{name}' ,
                  email='{email}',
                  password ='{password}'
              WHERE id='{id}' '''.format(table=self.tableName, **valuesDict, id=param)
        cur = self.dbConnection.getCursor()
        cur.execute(sql)
        self.dbConnection.commit()
        return param

    def remove(self, param):
        # TODO make safety
        sql = """ DELETE from {table} WHERE id={id} """.format(table=self.tableName, id=param)
        cur = self.dbConnection.getCursor()
        cur.execute(sql)
        self.dbConnection.commit()
        return param

    def convertDataFromTable(self, SQLcursor):
        rows = tuple([x[0] for x in SQLcursor.description])
        result = []
        for values in SQLcursor.fetchall():
            result.append(dict(zip(rows, values)))
        return result
