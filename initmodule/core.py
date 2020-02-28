# -*- coding: utf-8 -*-
"""Initialize a new Python project centered around a module"""

# Standard library imports
import logging
import os

# Initmodule imports
from . import helpers

def createModule(basepath, name): # type: (str, str) -> None
  """
  Initialize a new Python project centered around a module.

  Will create a standard folder structure with basic details filled in.
  A main class will be populated, as well as shells for unit tests, setup.py
  and documentation.

  :param basepath: A folder where the new module will be written
  :type basepath: str
  :param name: The name of the new module
  :type name: str
  """

  parentPath = os.path.join(basepath, name)
  # Create parent folder
  if not os.path.isdir(parentPath):
    os.makedirs(parentPath)
  # Create docs folder
  os.makedirs(os.path.join(parentPath, 'docs'))
  # Create conf.py
  with open(os.path.join(parentPath, 'docs', 'conf.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.confpy_template, name) + '\n')
  # Create index.rst
  with open(os.path.join(parentPath, 'docs', 'index.rst'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.indexrst_template, name) + '\n')
  # Create module folder
  os.makedirs(os.path.join(parentPath, name))
  # Create resources folder
  os.makedirs(os.path.join(parentPath, name, 'resources'))
  # Create dummy resource.csv
  with open(os.path.join(parentPath, name, 'resources', 'reference.csv'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.resource_template, name) + '\n')
  # Create __init__.py
  with open(os.path.join(parentPath, name, '__init__.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.modinit_template, name) + '\n')
  # Create __main__.py
  with open(os.path.join(parentPath, name, '__main__.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.modmain_template, name) + '\n')
  # Create core.py
  with open(os.path.join(parentPath, name, 'core.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.modcore_template, name) + '\n')
  # Create helpers.py
  with open(os.path.join(parentPath, name, 'helpers.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.modhelp_template, name) + '\n')
  # Create tests folder
  os.makedirs(os.path.join(parentPath, 'tests'))
  # Create tests/__init__.py
  with open(os.path.join(parentPath, 'tests', '__init__.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.testinit_template, name) + '\n')
  # Create test_basic.py
  with open(os.path.join(parentPath, 'tests', 'test_basic.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.testbasic_template, name) + '\n')
  # Create test_advanced.py
  with open(os.path.join(parentPath, 'tests', 'test_advanced.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.testadv_template, name) + '\n')
  # Create .gitignore
  with open(os.path.join(parentPath, '.gitignore'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.gitignore_template, name) + '\n')
  # Create cli.py
  with open(os.path.join(parentPath, 'cli.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.cli_template, name) + '\n')
  # Create LICENSE
  with open(os.path.join(parentPath, 'LICENSE'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.license_template, name) + '\n')
  # Create README.rst
  with open(os.path.join(parentPath, 'README.rst'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.readme_template, name) + '\n')
  # Create requirements.txt
  with open(os.path.join(parentPath, 'requirements.txt'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.requirements_template, name) + '\n')
  # Create setup.py
  with open(os.path.join(parentPath, 'setup.py'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.setup_template, name) + '\n')
  # Create test.bat
  with open(os.path.join(parentPath, 'test.bat'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.testbat_template, name) + '\n')
  # Create test.sh
  with open(os.path.join(parentPath, 'test.sh'), 'w') as outFile:
    outFile.write(helpers.insertName(helpers.testsh_template, name) + '\n')
