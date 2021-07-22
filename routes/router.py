class Router(object):
    routeDict = {}
    adapter = None

    def __init__(self, routesList: dict, contentAdapter):
        self.adapter = contentAdapter()
        for prop in routesList:
            self.routeDict[prop] = routesList[prop]()

    def add(self, resource, url):
        self.routeDict[url] = resource

    def getDict(self):
        return self.routeDict

    def getRouteByUrl(self, url):
        return self.routeDict.get(url)

    def content(self, url, method):
        if self.getRouteByUrl(url) is not None:
            return self.adapter.convert(getattr(self.getRouteByUrl(url), method)())
        else:
            raise ModuleNotFoundError('Route not found')
