import json
from adapters.baseAdapter import BaseAdapter


class JsonAdapter(BaseAdapter):
    def convert(self, data=""):
        return json.dumps(data).encode()
