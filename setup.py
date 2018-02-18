from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

#with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
#    long_description = f.read()

setup(
    name='indana',
    version='0.1.0',
    description='provides some helpers to easier create interactive elements in IPython Notebooks',
#    long_description=long_description,
    author='Christian Schwarz',
    author_email='schwarz-chr@web.de',
    install_requires=['pandas', "jupyter"],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
)