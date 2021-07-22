from db.connectors.dbBase import DbBase
from utils.Singleton import singleton

import mysql.connector


@singleton
class MsqlConnector(DbBase):

    def __init__(self, options):
        for prop in options:
            setattr(self, prop, options[prop])
        self.connect()

    def connect(self):
        if self.dbInstance is None:
            self.dbInstance = mysql.connector.connect(
                user=self.user,
                password=self.password,
                host=self.host,
                database=self.database
            )
        return self.dbInstance

    def close(self):
        self.dbInstance.close()

    def getInstance(self):
        return self.dbInstance
