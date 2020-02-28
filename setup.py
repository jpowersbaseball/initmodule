# -*- coding: utf-8 -*-

import setuptools
import os
from io import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
  readme_contents = f.read()

setuptools.setup(
  name='initmodule',
  version='0.0.1',
  description='Initialize a new Python project centered around a module',
  long_description=readme_contents,
  long_description_content_type='text/x-rst',
  author='Joshua Powers',
  author_email='jpowersbaseball@gmail.com',
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Customers',
    'Topic :: Python Packaging',
    'Programming Language :: Python :: 3.7'
  ],
  keywords='packaging',
  packages=setuptools.find_packages(),
  python_requires='>=3.7',
  entry_points = {'console_scripts': ['initmodule=initmodule.__main__:main']}
)
