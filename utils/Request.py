import json

from utils.Singleton import singleton


@singleton
class Request:
    headersDict = {}
    body = {}
    method = ''
    query = ''
    url = ''

    def init(self, data):
        self.parseHeaders(data)
        self.parseBody(data['wsgi.input'])
        self.method = data['REQUEST_METHOD'].lower()
        self.query = data['QUERY_STRING']
        self.url = data['RAW_URI']

    def parseHeaders(self, headersDict):
        headers = {}
        for prop in headersDict:
            if prop.find('HTTP_') != -1:
                newProp = prop.replace('HTTP_', '').lower()
                headers[newProp] = headersDict[prop]
        self.headersDict = headers

    def parseBody(self, body):
        value = body.read().decode("utf-8")
        self.body = json.loads(value) if value else value

    def getRequestData(self):
        parsedUrl = self.url.split('/')
        url = '/' + parsedUrl[0]
        return {
            "headers": self.headersDict,
            "body": self.body,
            "method": self.method,
            "query": self.query,
            "url": url,
            "param": parsedUrl[-1]
        }
