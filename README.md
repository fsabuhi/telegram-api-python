# telegram-api-python

`telegram-api-python` is a Python library for interacting with the Telegram Bot API. It provides a simple and easy-to-use interface for sending messages, sending files, and creating polls.

## Installation

To install `telegram-api-python`, you can clone the repository and install the dependencies:

```
git clone https://github.com/yourusername/telegram-api-python.git
cd telegram-api-python
pip install -r requirements.txt
```

Alternatively, you can download the source code from the repository and install the dependencies manually.

## Usage

To use `telegram-api-python`, you will need to create a new bot on Telegram and obtain its API token. You can do this by following the instructions on the Telegram website: https://core.telegram.org/bots#6-botfather

Once you have a bot token, you can create a new instance of the `TelegramBot` class:

```python
from telegram_api import TelegramBot

bot = TelegramBot('YOUR_BOT_TOKEN')
```

You can then use the `bot` object to interact with the Telegram Bot API. For example, to send a message to a chat, you can use the `send_message` method:

```python
bot.send_message(chat_id='YOUR_CHAT_ID', text='Hello, world!')
```

You can also send files using the `send_document`, `send_photo`, and `send_video` methods:

```python
bot.send_document(chat_id='YOUR_CHAT_ID', document=open('document.pdf', 'rb'))
bot.send_photo(chat_id='YOUR_CHAT_ID', photo=open('photo.jpg', 'rb'))
bot.send_video(chat_id='YOUR_CHAT_ID', video=open('video.mp4', 'rb'))
```

To create a poll, you can use the `create_poll` method:

```python
bot.create_poll(chat_id='YOUR_CHAT_ID', question='What is your favorite color?', options=['Red', 'Green', 'Blue'])
```

For more information on the available methods, please refer to the `telegram_api.py` file.

## Contributing

If you would like to contribute to `telegram-api-python`, please fork the repository, make your changes, and submit a pull request.

## Acknowledgments

`telegram-api-python` uses the `requests` library for making HTTP requests.
