# clevercord
Discord bot to chat with Cleverbot. Uses the cleverbotfree library to <br />
communicate via a headless Firefox browser. Also does some other cool stuff. <br />


## Requirments
- Ubuntu >= 18.04
- wget >= 1.19.4
- Mozilla Firefox >= 79.0
- Python >= 3.6.9
- python3-pip >= 20.2.2
    - cleverbotfree>=1.2.4
    - discord.py>=1.4.0
    - requests>=2.24.0
    - selenium>=3.141.0
    - zxcvbn>=4.4.28


## Installation

<b>Drivers</b>

Selenium requires a driver to interface with the headless browser. Firefox <br />
requires **geckodriver**, which needs to be installed before this module can be <br />
used. Make sure it’s in your **PATH**, e.g., place it in `/usr/bin` or `/usr/local/bin`. <br />

You can download geckodriver at https://github.com/mozilla/geckodriver/releases <br />

Failure to observe this step will give you an  error like: <br />
`"Message: ‘geckodriver’ executable needs to be in PATH."` <br />


<b>Discord</b>

Head over to [DiscordApp](https://discordapp.com/developers/applications/me "DiscordApp") and create a new app. <br />
Record your *Client_ID*. On the left, click **Bot**, and then **Add Bot**. <br />
Once you are done setting up your bot, save your *Client_ID*, *Token*, and *Client Secret* in a safe place. <br />


<b>Environment Variables</b>

Add to your **.bashrc** file:
```
export DISCORD_TOKEN=<Token>
export DISCORD_CLIENT_ID=<Client_ID>
```


## Docker
To build the docker container, clone this repository and set your ENV variables in the **Dockerfile**. <br />
From inside the main directory run: <br />
`docker build -t clevercord .` <br />
To run the container: <br />
`docker run clevercord`


## Usage
When bot is active in server, type `&help` for a list of commands, <br />
or type `&chat [message]` to talk to the bot.
