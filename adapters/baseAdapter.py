from abc import ABC


class BaseAdapter(ABC):
    def convert(self, data):
        pass
