
import re
from setuptools import setup
import ast

_version_re = re.compile(r'__version__=(.*)')

import jolla

setup(
    name='jolla',
    keywords=['back-end','framework','RESTful','gevent'],
    version=jolla.__version__,
    description='high performance RESTful framework',
    author='aljun',
    author_email='salamer_gaga@163.com',
    license='Apache',
    url='https://github.com/salamer/jolla',
    download_url='https://github.com/salamer/jolla',

    install_requires=[
        'gevent'
    ]

    classifiers=[
        "Development Status :: 1.0 - Production/Stable",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: Web",
         "Programming Language :: Python :: 2.7",
         'Topic :: Internet :: WWW/HTTP',
         'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)