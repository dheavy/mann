Mann
====

### Logger and notifier util.

It both logs to console and files, and can notify these logs via emails, Slack and Trello.

Instantiate it passing booleans in *args specifying
the logger and notifiers to use.
Use the `log` method to log/notify.

Default were set to simplify configuration (_i.e. file logging uses RotatingFileHandler with 'ab' write mode,
max bytes size of 2000, a backup count of 100 and UTF-8 encoding_).

- **console** - print in console if exists
- **file**    - logs to file if exists, using provided file handlers
- **email**   - send log via email if exists
- **slack**   - sends Slack message if exists
- **trello**  - create Trello task based on log, if exists

```python
**kwargs:
{
    'console': True,
    'file': {
        'info': <info-outfile-handle>,
        'error': <error-outfile-handle>,
    },
    'email': {
        'server': <smtp-server>,
        'port': <smtp-port>,
        'sendername': <human-friendly-sender-name>,
        'from': <email-from-address>,
        'to': <email-to-address>,
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

Like all software-based services on MyPleasure, **Mann** is named after
an [Interstellar](https://en.wikipedia.org/wiki/Interstellar_(film))
character, Dr Mann, who transmits logs with promising data to lure
 _Endurance_'s crew member into visiting his planet.
