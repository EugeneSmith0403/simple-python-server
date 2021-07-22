class DbConnection:
    dbInstance = None

    def __init__(self, connector):
        if self.dbInstance is None:
            self.dbInstance = connector.connect()

    def getInstance(self):
        return self.dbInstance
