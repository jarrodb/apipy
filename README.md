apipy
=====

Top-down model:

Api -> Engine -> Resource

example
-------

from apipy import Apipy, Engine, Resource


class Domain(Resource):
    pass


class Postfix(Engine):
    user = Resource()
    domain = Domain()

    class _Meta:
        url = 'http://127.0.0.1:8887'
        token = '<removed>'
        secret = 'removed'
        version = 1


class Api(Apipy):
    postfix = Postfix()

##########################################

Python 2.7.2 (default, Jun 20 2012, 16:23:33)
>>> from postfix import Api
>>> papi = Api()
>>> papi.postfix
<Engine(postfix)>
>>> papi.postfix.user
<Resource(user)>

### Create user resource
>>> papi.postfix.user.create(
...     email='somebody@ipglobal.net',
...     password='s0m3b0dy'
... )
{u'response': {u'comment': None, u'id': 1839, u'password': u's0m3b0dy', u'email': u'somebody@ipglobal.net', u'quota': 500000000}}

## Fetch user resource by ID
>>> papi.postfix.user.get(id=1839)
{u'response': [{u'comment': None, u'id': 1839, u'password': u's0m3b0dy', u'email': u'somebody@ipglobal.net', u'quota': 500000000}]}

## Fetch user resource by e-mail
>>> papi.postfix.user.get(email='somebody@ipglobal.net')
{u'response': [{u'comment': None, u'id': 1839, u'password': u's0m3b0dy', u'email': u'somebody@ipglobal.net', u'quota': 500000000}]}

## Fetch domain resource by name
>>> papi.postfix.domain.get(domain='ipglobal.net')
{u'response': [{u'date': u'2012-10-08T00:00:00', u'domain': u'ipglobal.net', u'id': 38}]}
