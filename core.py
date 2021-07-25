from config import models
from dependencyInjection.di import Di, injectable


class Core(object):
    def __init__(self, options):
        Di(options['dependencies'])
        self.initModels()

    def initModels(self):
        Di().addDependencies(models)
