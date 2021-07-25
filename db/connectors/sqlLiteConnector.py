import sqlite3

from db.connectors.dbBase import DbBase


class SqlLiteConnector(DbBase):
    fileName = ''

    def __init__(self, options):
        self.fileName = options['fileName']
        self.connect()

    def connect(self):
        if self.dbInstance is None:
            self.dbInstance = sqlite3.connect(self.fileName)
        return self.dbInstance

    def getInstance(self):
        return self.dbInstance

    def close(self):
        self.dbInstance.close()

    def getCursor(self):
        return self.dbInstance.cursor()
