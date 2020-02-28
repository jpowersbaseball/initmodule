# -*- coding: utf-8 -*-
"""Initialize a new Python project centered around a module

Run --help for more specific instructions.

Version:
--------

- initmodule v0.0.1
"""

# Standard library imports
import logging
import argparse
import sys

# Initmodule imports
import initmodule.core as INITMOD

# Force argparse to be helpful
class InitModuleHelpParser(argparse.ArgumentParser):
  def error(self, message):
    logging.error('error: ' + message + '\n')
    self.print_help()
    sys.exit(2)

# python -m initmodule --basepath d:\dev\python --name mymodule
def main(): # type: () -> None
  logging.basicConfig(format='%(asctime)-15s %(message)s', level=logging.ERROR)
  leParser = InitModuleHelpParser()
  leParser.add_argument('--basepath', help='A folder where the new module will be written')
  leParser.add_argument('--name', help='The name of the new module')
  lesArgs = leParser.parse_args()
  if lesArgs.basepath is None or lesArgs.name is None:
    logging.error('error: initmodule needs a basepath and a name for your new module')
    leParser.print_help()
    sys.exit(2)
  INITMOD.createModule(lesArgs.basepath, lesArgs.name)

if __name__ == '__main__':
  main()
