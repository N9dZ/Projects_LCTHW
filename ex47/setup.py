try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project for ex47',
    'author': '69N',
    'url': 'http://fatned.blog.163.com/',
    'download_url': 'http://fatned.blog.163.com/',
    'author_email': 'fatned@yeah.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)