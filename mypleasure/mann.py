"""Mann is a logger and notifier util."""
# -*- coding: utf-8 -*-
import logging
import logging.handlers
# import smtplib
# from socket import gaierror
# from datetime import datetime
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# from email.utils import formataddr


class Mann(object):
    """
    Mann is a logger and notifier util.

    Named after Dr. Mann from Interstellar,
    it logs message and errors, and even send them away
    as Slack messages, Trello tasks and emails.

    It was created to notify quickly of possible problems
    occuring on side project apps such as MyPleasure (https://mypleasu.re).
    """

    def __init__(self, *args, **kwargs):
        """
        Mann is a logger and notifier util.

        It both logs to console and files, and can notify
        these logs via emails, Slack and Trello.

        Instantiate it passing booleans in *args specifying
        the logger and notifiers to use.
        Use the `log` method to log/notify.

        Default were set to simplify configuration.
        i.e. File logging uses RotatingFileHandler with 'ab' write mode,
        max bytes size of 2000, a backup count of 100 and UTF-8 encoding.

        console - print in console if exists
        file    - logs to file if exists
        email   - send log via email if exists
        slack   - sends Slack message if exists
        trello  - create Trello task based on log, if exists

        Add `raise_exception` and set it to True if you don't want
        Mann to fail silently if an error occurs.

        **kwargs:
            {
                'console': True,
                'raise_exception': True
                'file': {
                    'info': <info-outfile-handle>,
                    'error': <error-outfile-handle>
                },
                'email': {
                    'server': <smtp-server>,
                    'port': <smtp-port>,
                    'recipient': <email-recipient-address>,
                    'user': <smtp-user>,
                    'password': <smtp-password>
                },
                'slack': {
                    'key': <api-key>,
                    'channel': <api-channel>
                },
                'trello': {
                    'key': <api-key>,
                    'token': <oauth-token>,
                    'board': '<board-id>',
                    'list': '<list-id>'
                }
            }
        """
        self.config = kwargs
        self.has_enabled_console = bool(self.config.get('console', None))
        self.has_enabled_file = bool(self.config.get('file', None))
        self.has_enabled_email = bool(self.config.get('email', None))
        self.has_enabled_slack = bool(self.config.get('slack', None))
        self.has_enabled_trello = bool(self.config.get('trello', None))
        self.should_raise_exception = bool(self.config.get(
            'raise_exception', None
        ))

    def log(self, msg='', error=False):
        """
        Log file into desired outputs.

        Args:
            msg:   A serialized message to output.
            error: Used to branch out output types
                   for services aware of it (i.e. file).
        """
        def unit(value, use):
            return (use is not False and value is not None) and value or None

        def bind(v, f, err=False):
            return bool(v) is not False and f(v, err) or None

        bind(unit(msg, self.has_enabled_console), self.console)
        bind(unit(msg, self.has_enabled_file), self.file, err=error)
        bind(unit(msg, self.has_enabled_email), self.email)
        bind(unit(msg, self.has_enabled_slack), self.slack)
        bind(unit(msg, self.has_enabled_trello), self.trello)

    def console(self, msg, error=False):
        """Print message in console."""
        print(msg)

    def file(self, msg, error=False):
        """Log message to file."""
        self.__set_file_handlers()

        if error is False:
            self.info_log.info(msg)
        else:
            self.error_log.error(msg)

    def email(self, msg, error=False):
        """Email message."""
        pass

    def slack(self, msg, error=False):
        """Send as Slack message."""
        pass

    def trello(self, msg, error=False):
        """Turn message to Trello card."""
        pass

    def __set_file_handlers(self):

        if not hasattr(self, 'info_log') or not hasattr(self, 'error_log'):
            self.__fh_info = None
            self.__fh_error = None
            self.info_log = logging.getLogger(__name__ + '.info')
            self.error_log = logging.getLogger(__name__ + '.error')

            def prepare_handler(logger, prop, key, level):
                fmt = logging.Formatter(
                    '%(asctime)s - %(levelname)s - %(message)s'
                )
                if not hasattr(self, prop):
                    f = self.config.get('file').get(key, None)
                    if f:
                        handler = logging.handlers.RotatingFileHandler(
                            f, mode='ab', maxBytes=2000,
                            backupCount=100, encoding='utf-8'
                        )
                        setattr(self, prop, handler)
                        getattr(self, prop).setFormatter(fmt)
                        logger.setLevel(level)
                        logger.addHandler(handler)

            prepare_handler(self.info_log, '__fh_info', 'info', logging.INFO)
            prepare_handler(
                self.error_log, '__fh_error', 'error', logging.ERROR
            )
