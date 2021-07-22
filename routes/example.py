from routes.resource import Resource


class Example(Resource):

    def post(self):
        return {
            "post": True
        }

    def get(self):
        return {
            "get": True
        }

    def delete(self):
        return {
            "delete": True
        }

    def put(self):
        return {
            "put": True
        }

    def getOne(self):
        return {
            "put": True
        }


