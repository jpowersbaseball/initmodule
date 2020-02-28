# -*- coding: utf-8 -*-
""" Test generic library """

# Standard library imports
import unittest

# Generic imports
import initmodule.core as INITMOD

class FancyTest(unittest.TestCase):
  """ Perform a test on data which is either complex or resource-intensive. """
  def test(self):
    self.assertEqual(19, 19)

if __name__ == '__main__':
  unittest.main()
