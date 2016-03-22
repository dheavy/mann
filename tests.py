"""Test suite for Mann."""
# -*- coding: utf-8 -*-
import unittest
from colour_runner import runner as crunner
# from mypleasure.mann import Mann


class ConsoleTestCase(unittest.TestCase):
    """Test console logger."""

    def runTest(self): # noqa
        pass


def suite():
    """Compose and return test suite."""
    suite = unittest.TestSuite()
    suite.addTest(ConsoleTestCase())
    return suite

if __name__ == '__main__':
    runner = crunner.ColourTextTestRunner()
    runner.run(suite())
