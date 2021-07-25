class DbConnection:
    dbInstance = None

    def __init__(self, connector):
        if self.dbInstance is None:
            self.dbInstance = connector.connect()

    def getInstance(self):
        return self.dbInstance

    def getCursor(self):
        return self.getInstance().cursor()

    def close(self):
        return self.getInstance().close()

    def commit(self):
        return self.dbInstance.commit()
