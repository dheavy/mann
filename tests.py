"""Test suite for Mann."""
# -*- coding: utf-8 -*-
import os
import sys
import unittest
from io import StringIO
from mock import patch
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


class FileTestCase(unittest.TestCase):
    """Test file logger outputs to file."""

    def runTest(self): # noqa
        info_expected = 'Fendouille'
        error_expected = 'Loola'

        info_log = 'info.log'
        error_log = 'error.log'

        logger = Mann(file={'info': info_log, 'error': error_log})
        logger.log(info_expected)
        logger.log(error_expected, error=True)

        info_file = open(info_log, 'r')
        error_file = open(error_log, 'r')
        info_file.seek(0)
        error_file.seek(0)

        self.assertIn(info_expected, info_file.read())
        self.assertIn(error_expected, error_file.read())

        os.unlink(info_log)
        os.unlink(error_log)


class EmailTestCase(unittest.TestCase):
    """Test email logger sends an email."""

    def runTest(self): # noqa
        with patch('smtplib.SMTP') as mock_smtp:
            from_address = 'sender@mypleasu.re'
            to_address = 'recipient@mypleasu.re'
            expected = 'Fendouille'

            logger = Mann(email={'from': from_address, 'to': to_address})
            logger.log(expected)

            mocked = mock_smtp.return_value

            self.assertTrue(mocked.sendmail.called)
            self.assertEqual(mocked.sendmail.call_count, 1)
            mocked.sendmail.assert_called_once_with(
                from_address, [to_address], expected
            )


class SlackTestCase(unittest.TestCase):
    """Test logger sends Slack message."""

    def runTest(self): # noqa
        with patch('slacker.Slacker') as mock_slack:
            expected_msg = 'Fendouille, la dernière fille Mallé.'
            expected_channel = '#plougastel'

            logger = Mann(slack={'key': '', 'channel': '#plougastel'})
            logger.log(expected_msg)

            mocked = mock_slack.return_value
            self.assertTrue(mocked.chat.post_message.called)
            self.assertEqual(mocked.chat.post_message.call_count, 1)
            mocked.chat.post_message.assert_called_once_with(
                expected_channel, expected_msg
            )


def suite():
    """Compose and return test suite."""
    suite = unittest.TestSuite()
    suite.addTest(ConsoleTestCase())
    suite.addTest(FileTestCase())
    suite.addTest(EmailTestCase())
    suite.addTest(SlackTestCase())
    return suite

if __name__ == '__main__':
    runner = crunner.ColourTextTestRunner()
    runner.run(suite())
