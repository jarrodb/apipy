from apipy.engine import Engine
from apipy.resource import Resource

class Apipy(object):
    def __init__(self):
        self._engines = []

    def __setattr__(self, name, value):
        elem = getattr(type(self), name, None)
        if elem and isinstance(elem, Engine):
            self._add_engine(name, elem)
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        """ access api engines """
        for e in self._engines:
            if name == e.name:
                return e
        raise NotImplemented('engine does not exist')

    def __repr__(self):
        return '<Apipy>'

    # private:
    def _add_engine(self, name, obj):
        obj.name = name
        self._engines.append(obj)

