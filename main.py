# This is a sample Python script.
from config import dependencies
from core import Core
from dependencyInjection.di import injectable
from routes.router import Router
from utils.Request import Request


options = {
    "dependencies": dependencies
}

Core(options)


@injectable(Router)
def app(environ, start_response, Router):

    try:
        request = Request()
        request.init(environ)
        requestData = request.getRequestData()
        resources = Router.content(requestData['url'], requestData['method'])
        status = '200 OK'
        response_headers = [
            ('Content-type', 'text/json'),
            ('Content-Length', str(len(resources)))
        ]
        start_response(status, response_headers)
        return iter([resources])
    except():
        print('herer')
        raise EOFError()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app()
