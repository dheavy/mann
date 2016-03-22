"""Test suite for Mann."""
# -*- coding: utf-8 -*-
import unittest
import colour_runner
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
    runner = colour_runner.runner.ColourTextTestRunner()
    runner.run(suite())
