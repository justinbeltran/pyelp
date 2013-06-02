#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

packages = [
    'pyelp'
]

requires = []

setup(
    name='pyelp',
    version=1.0
    description='Python Wrapper for Yelp API',
    author='Justin Beltran',
    packages=packages,
    package_dir={'pyelp': 'pyelp'}
)