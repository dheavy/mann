Mann
====

### Logger and notifier util.

It both logs to console and files, and can notify these logs via emails, Slack and Trello.

Instantiate it passing booleans in *args specifying
the logger and notifiers to use.
Use the `log` method to log/notify.

Default were set to simplify configuration.
i.e. File logging uses RotatingFileHandler with 'ab' write mode,
max bytes size of 2000 and backup count of 100.

**console** - print in console if exists
**file**    - logs to file if exists
**email**   - send log via email if exists
**slack**   - sends Slack message if exists
**trello**  - create Trello task based on log, if exists

```python
**kwargs:
{
    'console': True,
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
```
