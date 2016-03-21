import os

__version__ = '1.3.4'


def travis():
    assert os.environ.get('TRAVIS') == 'true'


def circle():
    assert os.environ.get('CIRCLECI') == 'true'


def codeship():
    assert os.environ.get('CI_NAME') == 'codeship'


def semaphore():
    assert os.environ.get('SEMAPHORE') == 'true'


def snap():
    assert os.environ.get('SNAP_CI') == 'true'


def frigg():
    assert os.environ.get('FRIGG_CI') == 'true'


if __name__ == '__main__':
    semaphore()
