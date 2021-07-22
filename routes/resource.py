from abc import ABC


class Resource(ABC):
    def __init__(self):
        pass

    @classmethod
    def post(self):
        pass

    @classmethod
    def get(self):
        pass

    @classmethod
    def delete(self):
        pass

    @classmethod
    def put(self):
        pass

    @classmethod
    def getOne(self):
        pass
