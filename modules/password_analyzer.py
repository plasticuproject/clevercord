from zxcvbn import zxcvbn
from zxcvbn.matching import add_frequency_lists
import discord

with open('data/xato-net-10-million-passwords.txt', 'r') as infile:
    xato = infile.read().split('\n')
add_frequency_lists({
    'xato': xato
})


class Analyze:
    """A realistic password strength estimator"""


    # location of file with help string
    helpFile = 'docs/password_analyzer.md'


    # reads help file
    def getHelp():
        with open(Analyze.helpFile, 'r') as fp:
            return fp.read()


    # prints help message if switch is used
    def isHelp(message):
        if message == '-h' or message == '--help':
            return True
        return False


    # analyze a given password
    def check_password(message):
        splitMessage = message.split(' ')

        if len(splitMessage) == 1 or Analyze.isHelp(splitMessage[1]):
            return Analyze.getHelp()

        # set variables
        passwd = ' '.join(splitMessage[1:])
        result = zxcvbn(passwd)
        score = result['score']
        scoreColor = [0xFF0000, 0xFF4500, 0xFFA500, 0xFFFF00, 0x008000]
        time = result['crack_times_display']['offline_slow_hashing_1e4_per_second']
        warning = result['feedback']['warning']
        suggestions = result['feedback']['suggestions']

        # built output
        embed = discord.Embed(color=scoreColor[score])
        embed.add_field(name='Estimated Cracking Time', value=time)
        if warning != '':
            embed.add_field(name='Warning', value=warning)
        if len(suggestions) > 0:
            for suggest in suggestions:
                embed.add_field(name='Suggestion', value=suggest)

        return embed

