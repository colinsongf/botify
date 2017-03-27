from setuptools import setup

_version = '0.1.0'

install_requires = []

setup(name='botify',
      version=_version,
      description='One line description.',
      install_requires=install_requires,
      long_description=open('README.rst', 'rt').read(),
      author='Priyam Singh',
      author_email='priyamsingh.22296@gmail.com',
      packages=['botify'],
      license='MIT',
)
