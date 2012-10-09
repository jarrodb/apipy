
class Resource(object):
    def __init__(self):
        self.name = self.__class__.__name__.lower()

    def __repr__(self):
        return '<Resource(%s)>' % (self.name)

    # public:
    def get(self, **kwargs):
        return self._con.get(self.name, kwargs)

    def create(self, **kwargs):
        return self._con.post(self.name, kwargs or {})

    def update(self, **kwargs):
        return self._con.put(self.name, kwargs)

    def delete(self, **kwargs):
        return self._con.delete(self.name, kwargs)

