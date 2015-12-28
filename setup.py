import re
from setuptools import find_packages, setup
import sys


with open('m.py', 'r') as fd:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
        fd.read(),
        re.MULTILINE
    ).group(1)

try:
    from semantic_release import setup_hook
    setup_hook(sys.argv)
except ImportError:
    pass

setup(
    name='test-python-semantic-release',
    version=version,
    url='http://github.com/relekang/test-python-semantic-release',
    author='Rolf Erik Lekang',
    author_email='me@rolflekang.com',
    packages=find_packages(exclude='tests'),
    license='MIT',
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ]
)
