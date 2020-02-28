# -*- coding: utf-8 -*-
""" Test generic library. """

# Standard library imports
import unittest

# Generic imports
import initmodule.core as INITMOD

class BasicTest(unittest.TestCase):
  """ Perform a test on data which is basic functionality. """
  def test(self):
    self.assertEqual(4, 4)

if __name__ == '__main__':
  unittest.main()
