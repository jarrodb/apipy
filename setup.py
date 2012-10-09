#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name = 'apipy',
    version = '0.01',
    description = 'RESTful API framework for modular engines and resources',
    author = 'Jarrod Baumann',
    author_email = 'jarrod@ipglobal.net',
    url = 'https://github.com/jarrodb/apipy',
    license = "http://www.apache.org/licenses/LICENSE-2.0",
    packages = find_packages(),
    package_dir={'mypkg': 'src/mypkg'},
    install_requires = ['nose'],
    )

