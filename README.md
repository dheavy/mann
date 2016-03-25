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
        'port': <smtp-port-defaults-to-587>,
        'sendername': <human-friendly-sender-name>,
        'from': <email-from-address>,
        'to': <email-to-address>,
        'subject': <subject-line>,
        'user': <smtp-user>,
        'password': <smtp-password>
    },
    'slack': {
        'key': <api-key>,
        'channel': <api-channel>,
        'username': <bot-name>
    },
    'trello': {
        'key': <api-key>,
        'token': <oauth-token>,
        'list': '<list-id>',
        'cardname': <optional-card-name>
        'members': <string-id-or-tuple-of-member-ids-to-add>
    }
}
```

## Usage

#### Printing to console
```python
logger = Mann(console=True)

# Outputs in console "Fendi is a good dog.".
logger.log('Fendi is a good dog.')

# Outputs in console "[ERROR] Fendi is a moody dog.".
logger.log('Fendi is a moody dog.', error=True)
```

#### Logging to file(s)
```python
# Create a log file for 'info' level.
logger = Mann(file={'info': 'info_file_name.log'})

# Creates file 'info_file_name.log'
# and echoes 'Loola is a nice puppy.' inside it.
logger.log('Loola is a nice puppy.')

# Nothing happens! 'info_file_name.log' is untouched...
logger.log('Loola barks a lot!', error=True)

# Create a log file for 'error' level.
logger = Mann(file={'error': 'error_file_name.log'})

# Nothing happens! 'info_file_name.log' is untouched,
# and neither is 'error_file_name.log'...
logger.log('Loola is a nice puppy.')

# Creates file 'error_file_name.log'
# and echoes 'Loola barks a lot!' inside it.
logger.log('Loola barks a lot!', error=True)

# You can create both files at the same time.
# The proper file will be written on call to 'log'
# depending on whether 'error=True' or not.
logger = Mann(file={
    'info': 'info_file_name.log',
    'error': 'error_file_name.log'
})
```

#### Sending log by email
```python
logger = Mann(email={
    'server': smtp.example.com,
    'port': 587,               # optional - defaults to 587
    'sendername': 'Loola',     # optional - defaults to ''
    'from': 'loola@example.com',
    'to': 'fendi@example.com',
    'subject': 'Waff! Waff!',  # optional - defaults to ''
    'user': 'server_username',
    'password': 'server_username_password'
})

logger.log('Slurp! Slurp!')
```

#### Sending log as Slack message

The message sender appears as a bot :dog:, obviously.

```python
logger = Mann(slack={
    'key': 'my-slack-app-key',
    'channel': '#plougastel',    # optional - defaults to '#random'
    'username': 'FendouilleBot'  # optional - defaults to 'Bot'
})

logger.log('Slurp! Slurp!')
```

#### Sending log as Trello card

Perfect for creating task and assigning members on it, say,
when the logger bubbled up an exception ("_Davy, go fix that bug :sob:_").

Get your **key** [here](https://trello.com/app-key) and generate your token using your key and the following URL:
`https://trello.com/1/authorize?expiration=never&scope=read,write,account&response_type=token&name=<YOUR-APP-NAME>&key=<YOUR-KEY>`.

Fiddle with the [Trello Developer Sandbox](https://developers.trello.com/sandbox) and read the [API docs](https://developers.trello.com/advanced-reference/) to extract `ID`s for your `list` and `member`s.

```python
logger = Mann(trello={
    'key': 'trello-key',
    'token': 'trello-token',
    'list': 'trello-list-id',
    'cardname': 'Please feed the dogs while I am gone.'
    'members': 'member-id'  # optional|mixed - can be set to user id
                            # as string or a tuple of user ids as strings
})

# Create a Trello card. The log message is set a card description,
# and becomes the card title (name) if 'cardname' wasn't set.
# If 'members' were added, they will be assigned to the card.
logger.log('The food is in the drawer. Love, mum.')
```

#### Mix it all up!

You can mix several (or all) methods to log and notify everywhere you want at once.

```python
file = {
    'info': 'mum_asked_politely.log',
    'error': 'sisters_didnt_listen.log'
}

email = {
    'server': smtp.example.com,
    'sendername': 'Mum',
    'from': 'mum@example.com',
    'to': 'sisters@example.com',
    'subject': 'I SAID FEED THE DOGS NOW!',
    'user': 'server_username',
    'password': 'server_username_password'
}

slack = {
    'key': 'my-slack-app-key',
    'channel': '#plougastel',
    'username': 'Mum'
}

trello = {
    'key': 'trello-key',
    'token': 'trello-token',
    'list': 'trello-list-id',
    'cardname': 'I SAID FEED THE DOGS NOW!'
    'members': ('marion-id', 'morgane-id')
}

logger = Mann(
    console=True,
    file=file,
    email=email,
    slack=slack,
    trello=trello
)

logger.log(
    "Les filles, vous commencez à me plaire là... \
    DON'T MAKE ME COME TELL YOU FACE TO FACE OR ELSE..."
)
```

## Trivia

Like all software-based services on MyPleasure, **Mann** is named after
an [Interstellar](https://en.wikipedia.org/wiki/Interstellar_(film))
character, Dr Mann, who transmits logs with promising data to lure
 _Endurance_'s crew member into visiting his planet. :space_invader:

Also, **Fendi** and **Loola** are our favorite dogs :dog:. And [**Plougastel-Daoulas**](https://en.wikipedia.org/wiki/Plougastel-Daoulas) our favorite place in **Brittany**:heart:.

## License

#### MIT
