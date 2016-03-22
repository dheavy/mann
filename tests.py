"""Test suite for Mann."""
# -*- coding: utf-8 -*-
import sys
import unittest
from io import StringIO
from colour_runner import runner as crunner
from mypleasure.mann import Mann


class ConsoleTestCase(unittest.TestCase):
    """Test console logger."""

    def runTest(self): # noqa
        try:
            out = StringIO()
            sys.stdout = out

            logger = Mann(console=True)
            logger.log('foo')

            output = out.getvalue().strip()

            self.assertEqual(output, 'foo')
        finally:
            sys.stdout = sys.__stdout__

        try:
            out = StringIO()
            sys.stdout = out

            logger = Mann()
            logger.log('foo')

            output = out.getvalue().strip()

            self.assertEqual(output, '')
        finally:
            sys.stdout = sys.__stdout__


def suite():
    """Compose and return test suite."""
    suite = unittest.TestSuite()
    suite.addTest(ConsoleTestCase())
    return suite

if __name__ == '__main__':
    runner = crunner.ColourTextTestRunner()
    runner.run(suite())
