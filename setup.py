"""xmlrpclib-cookie provides a transport class that helps retain cookie/session.

"""
from setuptools import setup

__version__ = '0.01'

setup(name='xmlrpclib-cookie',
      version=__version__,
      license='MIT',
      author='Stewart Park',
      author_email='stewartpark92@gmail.com',
      description=__doc__.split('\n')[0],
      long_description=__doc__,
      py_modules=['xmlrpclib_cookie'],
      zip_safe=False,
      platforms='any',
      install_requires=['xmlrpclib']
)
