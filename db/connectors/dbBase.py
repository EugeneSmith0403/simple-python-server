class DbBase(object):
    database = ''
    port = None
    host = '127.0.0.1'
    user = ''
    password = ''
    dbInstance = None

    def __init__(self, options):
        pass

    @classmethod
    def connect(cls):
        pass

    @classmethod
    def close(cls):
        pass

    @classmethod
    def getInstance(cls):
        return cls.dbInstance
