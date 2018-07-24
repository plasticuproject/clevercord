# clevercord
Discord bot to chat with Cleverbot. Uses the cleverbotfree library to <br />
communicate via a headless Firefox browser.

## Requirments
Python 3.x, pip, and the latest version of Firefox browser installed. <br />
```
pip install cleverbotfree
pip install -U https://github.com/Rapptz/discord.py/archive/rewrite.zip
```

## Installation
<b>Drivers</b>

Selenium requires a driver to interface with the headless browser. Firefox <br />
requires geckodriver, which needs to be installed before this module can be <br />
used. Make sure it’s in your PATH, e. g., place it in /usr/bin or /usr/local/bin. <br />

You can download the geckodriver at https://github.com/mozilla/geckodriver/releases <br />

Failure to observe this step will give you the error <br />
"Message: ‘geckodriver’ executable needs to be in PATH." <br />

<b>Discord</b>

Head over to https://discordapp.com/developers/applications/me and create a new app. <br />
Click on "Create Bot User". <br />
Once done, you can get the secret bot token. <br />

In cleverbot.py replace all <...> with appropriate information. <br />

To start bot, run:
```
python cleverbot.py
```
To add bot to server add your CLIENT_ID to this URL and visit in browser:  <br />
"https://discordapp.com/oauth2/authorize?client_id=<YOUR_BOT_CLIENT_ID_GOES_HERE>&scope=bot" <br />

## Usage
When bot is active in server, just type "&chat" followed by what you want to send to Cleverbot <br />.
