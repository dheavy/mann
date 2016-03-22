"""Mann is a logger and notifier util."""
# -*- coding: utf-8 -*-
# import logging
# import logging.handlers
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

        Use boolean *args to specify which service you want to use,
        and set special services' data in **kwargs.

        Default were set to simplify configuration.
        i.e. File logging uses RotatingFileHandler with 'ab' write mode,
        max bytes size of 2000 and backup count of 100.

        *args:
            console - print in console if True
            file    - logs to file if True
            email   - send log via email if True
            slack   - sends Slack message if True
            trello  - create Trello task based on log, if True

        **kwargs:
            {
                'file': {
                    'debug': <path-to-debug-log>,
                    'error': <path-to-error-log>
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
        self.has_enabled_console = bool(args.get('console', None))
        self.has_enabled_file = bool(args.get('file', None))
        self.has_enabled_email = bool(args.get('email', None))
        self.has_enabled_slack = bool(args.get('slack', None))
        self.has_enabled_trello = bool(args.get('trello', None))
        self.apis_config = kwargs

    def log(self, msg=''):
        """Log file into desired outputs."""
        def unit(value, use):
            return value and use or None

        def bind(v, f):
            return f(v) and v or None

        bind(unit(msg, self.has_enabled_console), self.console)
        bind(unit(msg, self.has_enabled_file), self.file)
        bind(unit(msg, self.has_enabled_email), self.email)
        bind(unit(msg, self.has_enabled_slack), self.slack)
        bind(unit(msg, self.has_enabled_trello), self.trello)

    def console(self, msg):
        """Print message in console."""
        pass

    def file(self, msg):
        """Log message to file."""
        pass

    def email(self, msg):
        """Email message."""
        pass

    def slack(self, msg):
        """Send as Slack message."""
        pass

    def trello(self, msg):
        """Turn message to Trello card."""
        pass
