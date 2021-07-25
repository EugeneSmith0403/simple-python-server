class BaseDbModel(object):
    tableName = ''

    def select(self):
        pass

    def update(self, valuesDict, param):
        pass

    def remove(self, param):
        pass

    def create(self, data):
        pass

    def execute(self):
        pass

    def getById(self, param):
        pass
