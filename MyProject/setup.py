try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'This is My First Project for Python.',
    'author': '69N',
    'url': 'http://fatned.blog.163.com/',
    'download_url': 'http://fatned.blog.163.com/',
    'author_email': 'fatned@yeah.net',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['MyProject'],
    'scripts': [],
    'name': 'MyProject'
}

setup(**config)
