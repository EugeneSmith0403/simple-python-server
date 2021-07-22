from utils.Singleton import singleton


@singleton
class Di(object):
    dependencyDict = {}

    def __init__(self, depList):
        self.initDependency(depList)

    def initDependency(self, depList):
        for item in depList:
            if item.__class__.__name__ is not self.dependencyDict:
                self.dependencyDict[item.__class__.__name__] = item

    def getDependencies(self):
        return self.dependencyDict

    def setDependency(self, dep):
        self.dependencyDict[dep.__name__] = dep


def injectable(*arguments):
    def inner(func):
        def deepInner(*args):
            results = {}
            for argument in arguments:
                name = argument.__name__
                if name in Di().dependencyDict:
                    curInstance = Di().dependencyDict.get(name)
                    results[name] = curInstance
                else:
                    msg = '{name} dependency doesn\'t add to configuration'.format(name=name)
                    raise KeyError(msg)
            return func(*args, **results)
        return deepInner

    return inner
