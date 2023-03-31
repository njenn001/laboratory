""" Prebuilt imports. """
import os
import sys 
from setuptools import setup
import distutils.core
from distutils.command.install import install

""" Reads the readme file. 

@param fname : The readme file. 
@type fname : str
"""
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

""" Set different application identifiers.

@return null 
"""
setup(
    name = "TC Laboratory API",
    version = "0.0.0",
    author = "Noah Jennings",
    author_email = "ntjennings1@odu.edu",
    description = ("REST API to utilize pre-exiting modules"),
    license = "MIT",
    url = "http://packages.python.org/an_example_pypi_project",
    packages=['flaskr', 'tests'],
    long_description=read('README.md'),
    install_requires = [
        'numpy', 
        'cython',
        'pyspark',
        'kafka-python',
        'flask',
    ]
)
