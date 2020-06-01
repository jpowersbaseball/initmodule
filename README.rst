********************************
Initialize Module
********************************

Initialize a new Python project centered around a module.

To run CLI, install the initmodule/initmodule folder into your site-packages,
then get the usage instructions by running
python -m initmodule --help

To run tests on the new module you have created, best to make sure coverage
and unittest are installed, then from the top level directory that was
created, run:
coverage run --source initmodule -m unittest tests.test_basic
This command is also executed by the test.bat and test.sh scripts that
are created automatically.

To create a Windows executable, make sure pyinstaller is installed and run
pyinstaller cli.py --name initmodule --onefile

`Initialize Module <https://packaging.python.org/tutorials/packaging-projects/>`_
