import os

__version__ = '1.2.7'


def travis():
    assert os.environ.get('TRAVIS') == 'true'


def circle():
    assert os.environ.get('CIRCLECI') == 'true'


def codeship():
    assert os.environ.get('CI_NAME') ==	'codeship'


def semaphore():
    assert os.environ.get('SEMAPHORE') == 'true'


if __name__ == '__main__':
    print(os.environ.get("CI_PULL_REQUEST"))
    circle()
