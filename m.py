import os

__version__ = '1.2.6'


def travis():
    assert os.environ.get('TRAVIS') == 'true'


def circle():
    assert os.environ.get('CIRCLECI') == 'true'

if __name__ == '__main__':
    circle()
