#!/bin/sh
import httplib
import requests


class Connection(object):
    BASE_URL = '%s/api/%s/%s/%s' # Bad place?

    def __init__(self, url, engine, version=1, headers={}):
        self.url = url
        self.engine = engine
        self.version = version
        self.headers = headers
        self._requests = requests

    def get(self, resource, payload, headers=None):
        return self._method('get', resource, payload, headers)

    def post(self, resource, payload, headers=None):
        return self._method('post', resource, payload, headers)

    def put(self, resource, payload, headers=None):
        return self._method('put', resource, payload, headers)

    def delete(self, resource, payload, headers=None):
        return self._method('delete', resource, payload, headers)

    def _method(self, method, resource, payload, headers):
        headers = self._headers(headers)
        url = self._get_api_url(resource)
        r_method = getattr(self._requests, method)
        r = r_method(url, params=payload, headers=headers)
        return self._handle_response(r)

    def _handle_response(self, r_obj):
        if r_obj.status_code == 200:
            return r_obj.json
        error = r_obj.json.get('error', None) if r_obj.json else 'error'
        return {
            'error': error,
            'status_code': r_obj.status_code,
            }

    def _get_api_url(self, resource):
        return self.BASE_URL % (
            self.url,
            self.version,
            self.engine,
            resource,
            )

    def _headers(self, headers):
        return headers if headers else self.headers

