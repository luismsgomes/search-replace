from setuptools import setup
from os import path
import re


def packagefile(*relpath):
    return path.join(path.dirname(__file__), *relpath)


def read(*relpath):
    with open(packagefile(*relpath)) as f:
        return f.read()


def get_version(*relpath):
    match = re.search(
        r'''^__version__ = ['"]([^'"]*)['"]''',
        read(*relpath),
        re.M
    )
    if not match:
        raise RuntimeError('Unable to find version string.')
    return match.group(1)


setup(
    name='search-replace',
    version=get_version('search_replace.py'),
    description='A convenience script to search and replace strings in files.',
    long_description=read('README.rst'),
    url='https://github.com/luismsgomes/search-replace',
    author='Luís Gomes',
    author_email='luismsgomes@gmail.com',
    license='MIT',
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='convenience',
    install_requires=[
        'docopt',
        'openfile',
    ],
    package_dir={'': '.'},
    py_modules=['search_replace'],
    entry_points={
        'console_scripts': [
            'search-replace=search_replace:main',
        ],
    },
)
