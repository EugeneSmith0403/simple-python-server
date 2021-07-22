from dependencyInjection.di import Di


class Core(object):
    def __init__(self, options):
        Di(options['dependencies'])
