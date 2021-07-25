from dependencyInjection.di import injectable
from models.User import User
from routes.resource import Resource
from utils.Request import Request


class Example(Resource):

    @injectable(User)
    def post(self, User):
        body = Request().getRequestData()['body']
        return {
            "method": "post",
            "result": {
                "status": 'Ok',
                "data": {
                    "id": User.create(body)
                }
            }
        }

    @injectable(User)
    def get(self, User):
        return {
            "method": 'get',
            "result": User.select()
        }

    @injectable(User)
    def delete(self, User):
        data = Request().getRequestData()
        param = data['param']
        print(param)
        return {
            "method": "delete",
            "result": {
                "status": 'Ok',
                "data": {
                    "id": User.remove(param)
                }
            }
        }

    @injectable(User)
    def put(self, User):
        data = Request().getRequestData()
        body = data['body']
        param = data['param']
        return {
            "method": "put",
            "result": {
                "status": 'Ok',
                "data": {
                    "id": User.update(body, param)
                }
            }
        }

    @injectable(User)
    def getOne(self):
        return {
            "put": True
        }
