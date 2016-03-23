"""Test suite for Mann."""
# -*- coding: utf-8 -*-
import os
import sys
import unittest
from io import StringIO
from colour_runner import runner as crunner
from mypleasure.mann import Mann


class ConsoleTestCasePrintsOutputToConsole(unittest.TestCase):
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


class FileTestCaseLogsToFile(unittest.TestCase):
    """Test file logger outputs to file."""

    def runTest(self): # noqa
        info_excepted = 'Fendouille'
        error_excepted = 'Loola'

        info_log = 'info.log'
        error_log = 'error.log'

        logger = Mann(file={'info': info_log, 'error': error_log})
        logger.log(info_excepted)
        logger.log(error_excepted, error=True)

        info_file = open(info_log, 'r')
        error_file = open(error_log, 'r')
        info_file.seek(0)
        error_file.seek(0)

        self.assertIn(info_excepted, info_file.read())
        self.assertIn(error_excepted, error_file.read())

        os.unlink(info_log)
        os.unlink(error_log)


class FileTestCaseRaiseExceptionOnWriteErrorIfAllowed(unittest.TestCase):
    """Test file logger raises an exception on error, if allowed."""

    def runTest(self): # noqa
        pass


def suite():
    """Compose and return test suite."""
    suite = unittest.TestSuite()
    suite.addTest(ConsoleTestCasePrintsOutputToConsole())
    suite.addTest(FileTestCaseLogsToFile())
    suite.addTest(FileTestCaseRaiseExceptionOnWriteErrorIfAllowed())
    return suite

if __name__ == '__main__':
    runner = crunner.ColourTextTestRunner()
    runner.run(suite())
