from apipy.connection import Connection
from apipy.resource import Resource

class Engine(object):

    class _Meta:
        name = 'Engine'
        url = None
        token = None
        secret = None
        version = 1

    def __init__(self):
        """ Registers an API engine hosted on a distributed system

        """
        self._Meta.name = self.__class__.__name__.lower()

        self._con = self._connection()
        self._resources = []
        self._load_resources()

    def __setattr__(self, name, value):
        elem = getattr(type(self), name, None)
        if elem and isinstance(elem, Resource):
            self._add_resource(name, elem)
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        """ access engine resources """
        for r in self._resources:
            if name == r.name:
                return r
        raise NotImplemented('resource does not exist')

    def __repr__(self):
        return '<Engine(%s)>' % (self._Meta.name)

    def __iter__(self):
        return iter(self._resources)

    # public:
    @property
    def name(self):
        return self._Meta.name

    # private:
    def _connection(self, **kwargs):
        return Connection(
            self._Meta.url,
            self._Meta.name,
            self._Meta.version,
            headers = {
                'Token': self._Meta.token,
                'Secret': self._Meta.secret,
            })

    def _load_resources(self):
        for name in dir(self):
            obj = object.__getattribute__(self, name)
            if isinstance(obj, Resource):
                self._add_resource(name, obj)

    def _add_resource(self, name, obj):
        obj.name = name
        obj._con = self._con
        self._resources.append(obj)
