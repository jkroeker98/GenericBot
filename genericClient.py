# File    : bookClub.py
# Author  : Joseph Kroeker
# Purpose : Automate book club functionality
# Changes : 03/05/2022 - Created class with message and help capability

import discord as ds


class GenericClient(ds.Client):
    def __init__(self):
        super(GenericClient, self).__init__()
        self.response = ''

    async def on_ready(self):
        # Function : on_ready
        # Purpose  : Output debug information when the bot starts up
        # Inputs   : self - Generic Client class
        print(f'{self.user} has connected to Discord!\n')

    async def on_message(self, msg):
        # Function : on_message
        # Purpose  : Respond to messages that are directed towards the bot
        # Inputs   : self - Generic Client class
        #            message - message that was received
        if msg.author == self.user:                             # No reason to read my own messages
            return

        if msg.content == '!helpme' or msg.content == '!h': # List all generic messages here
            self.response = self.help_msg()
        else:
            self.response = self.parse_msg(msg)

        if self.response:                                           # If a message is in the queue send it out and clear queue
            await msg.channel.send(self.response)
            self.response = ''

    def help_msg(self):
        # Function : help_msg
        # Purpose  : Generic help message that will be output when needed
        # Inputs   : self - Generic Client class
        return "There is no defined help for this bot at the moment"

    def parse_msg(self, msg):
        # Function : parse_msg
        # Purpose  : Respond to non generic messages that are directed towards the bot
        # Inputs   : self - Generic Client class
        #            msg - message that was received
        return ''



