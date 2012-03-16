#!/usr/bin/env python
"""
StatHat
======

A Python library for `StatHat <http://www.stathat.com/>`_ that implements the EZ API and Classic API
with progressive support for asynchronous requests via gevent.
"""

from setuptools import setup

setup(
    name='python-stathat',
    version='0.2.0',
    author='Matt Robenolt',
    author_email='matt@ydekproductions.com',
    url='https://github.com/mattrobenolt/python-stathat',
    description='A better Python library for StatHat',
    long_description=__doc__,
    py_modules=['stathat'],
    extras_require={
        'async': ['gevent']
    },
    zip_safe=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
