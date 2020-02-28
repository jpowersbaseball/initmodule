# -*- coding: utf-8 -*-

import sys
import datetime

def insertName(content, name):
  retval = content.strip().replace('%NAME%', name)
  retval = retval.replace('%UPPER%', name.upper())
  retval = retval.replace('%YEAR%', str(datetime.datetime.now().year))
  return retval

confpy_template = """
# -*- coding: utf-8 -*-
"""

indexrst_template = """

"""

resource_template = """
ID,Label,Feature
1,Entity,Uppercase
2,Quantity,Numeric
"""

modinit_template = """
# -*- coding: utf-8 -*-
\"\"\" %NAME% module

Import the %NAME% core file module to perform actions:

  >>> import %NAME%.core as %UPPER%
  >>> results = %UPPER%.doSomething()
\"\"\"

__version__ = "0.0.1"
"""

modmain_template = """
# -*- coding: utf-8 -*-
\"\"\" %NAME% module

Run --help for more specific instructions

Version:
--------
- %NAME% v0.0.1
\"\"\"

# Standard library imports
import logging
import argparse

# %NAME% imports
import %NAME%.core as %UPPER%

# python -m %NAME% --input testin.txt --output testout.txt
def main(): # type: () -> None
  logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.ERROR)
  leParser = argparse.ArgumentParser()
  leParser.add_argument('--input', help='A text file with your input')
  leParser.add_argument('--output', help='The file you want the results in')
  lesArgs = leParser.parse_args()
  if lesArgs.input is None or lesArgs.output is None:
    logging.error('%NAME% needs an input file and an output file')
    leParser.print_help()
    sys.exit(2)
  with open(lesArgs.input, 'r') as inFile:
    data = inFile.read().strip()
  results = %UPPER%.doSomething(data)
  with open(lesArgs.output, 'w') as outFile:
    outFile.write(results + '\\n')

if __name__ == '__main__':
  main()
"""

modcore_template = """
# -*- coding: utf-8 -*-
\"\"\"%%NAME%% library\"\"\"

# Standard library imports
import logging

# %NAME% imports
from . import helpers

class Something:
  \"\"\" Something to hold data and results in \"\"\"

  def __init__(self, data): # type: (str) -> None
    \"\"\"
    Initialize the analysis with data

    :param data: the data
    :type data: str
    \"\"\"

    self.dataStr = data

  def __eq__(self, other): # type: (Something) -> bool
    \"\"\"
    Override default equality with a comparison of data

    :param other: the other something to compare
    :type other: Something
    :return: if these somethings are equal
    :rtype: bool
    \"\"\"

    return self.dataStr.lower() == other.dataStr.lower()

  def __ne__(self, other): # type: (Something) -> bool
    \"\"\"
    Override default inequality with reference to equality

    :param other: the other something to compare
    :type other: Something
    :return: if these somethings are not equal
    :rtype: bool
    \"\"\"

    return not self.__eq__(other)

  def datalen(self): # type () -> int
    \"\"\"
    Calculate the length of the data

    :return: the length of the data
    :rtype: int
    \"\"\"
    return len(self.dataStr)

def doSomething(inData): # type: (str) -> str
  \"\"\"
  Do something to some data

  :param inData: the data
  :type inData: str
  :return: results
  :rtype: str
  \"\"\"
  theWork = Something(inData)
  results = theWork.datalen()
  logging.info('Finished doing something')
  return str(results)
"""

modhelp_template = """
# -*- coding: utf-8 -*-

# Standard library imports
import os
import csv

refData = []

# Initialization loads reference data from resources CSV.
this_dir, this_filename = os.path.split(__file__)
refPath = os.path.join(this_dir, 'resources', 'reference.csv')
if (os.path.isfile(refPath)):
  with open(refPath) as refFile:
    refData = [{colName: str(cellValue) for colName, cellValue in row.items()}
               for row in csv.DictReader(refFile, skipinitialspace=True)]
"""

testinit_template = """
# -*- coding: utf-8 -*-
"""

testbasic_template = """
# -*- coding: utf-8 -*-
\"\"\" Test %NAME% library. \"\"\"

# Standard library imports
import unittest

# %NAME% imports
import %NAME%.core as %UPPER%

class BasicTest(unittest.TestCase):
  \"\"\" Perform a test on data which is basic functionality. \"\"\"
  def test(self):
    testResult = %UPPER%.doSomething('Easy')
    self.assertEqual(testResult, '4')

if __name__ == '__main__':
  unittest.main()
"""

testadv_template = """
# -*- coding: utf-8 -*-
\"\"\" Test %NAME% library. \"\"\"

# Standard library imports
import unittest

# %NAME% imports
import %NAME%.core as %UPPER%

class AdvancedTest(unittest.TestCase):
  \"\"\" Perform a test on data which is advanced functionality. \"\"\"
  def test(self):
    testResult = %UPPER%.doSomething('Difficult')
    self.assertEqual(testResult, '9')

if __name__ == '__main__':
  unittest.main()
"""

gitignore_template = """
# Byte-compiled
*.pyc
*.pyo
*.pyd

# Scripts
*.sh
*.bat

# IDE
.spyproject/
.spyderproject/
.idea/

# Test results
.coverage
"""

cli_template = """
# -*- coding: utf-8 -*-
from %NAME%.__main__ import main

if __name__ == '__main__':
  main()
"""

license_template = """
Copyright (c) %YEAR%, %NAME%
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the %NAME% project.
"""

readme_template = """
********************************
%NAME% Library
********************************

A Python library for doing something.

To run CLI, install the %NAME%/%NAME% folder into your site-packages,
then get the usage instructions by running
python -m %NAME% --help

To test, best to make sure coverage and unittest are installed, then from the
parent directory, run
coverage run --source %NAME% -m unittest tests.test_basic

To create a Windows executable, make sure pyinstaller is installed and run
pyinstaller cli.py --name %NAME% --onefile

'%NAME% <https://www.example.com>'_
"""

requirements_template = """
setuptools
"""

setup_template = """
# -*- coding: utf-8 -*-

import setuptools
import os
from io import open

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.rst'), encoding='utf-8') as f:
  readme_contents = f.read()

setuptools.setup(
  name='%NAME%',
  version='0.0.1',
  description='%NAME% library',
  long_description=readme_contents,
  long_description_content_type='text/x-rst',
  author='John Doe',
  author_email='jdoe@example.com',
  install_requires=[],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Customers',
    'Topic :: Analytics',
    'Programming Language :: Python :: 3.7'
  ],
  keywords='analytics',
  packages=setuptools.find_packages(),
  python_requires='>=3.7',
  entry_points = {'console_scripts': ['%NAME%=%NAME%.__main__:main']}
)
"""

testbat_template = """
@echo off

coverage run --source %NAME% -m unittest tests.test_basic
coverage report -m
python -m unittest tests.test_advanced
"""

testsh_template = """
#!/bin/bash

coverage run --source %NAME% -m unittest tests.test_basic
coverage report -m
python -m unittest tests.test_advanced
"""
