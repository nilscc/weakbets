import irc.bot
import irc.client

import argparse
import jaraco.logging

import ssl

NICKNAME='weakbets'
REALNAME=NICKNAME

SRV_FREENODE = irc.bot.ServerSpec('irc.freenode.net', port=7070)
CHANNEL = '##weakpots'

class WeakBets(irc.bot.SingleServerIRCBot):
    def __init__(self, nickname=NICKNAME, realname=REALNAME, server_list=[SRV_FREENODE], channel=CHANNEL, **kwargs):
        super().__init__(server_list=server_list, nickname=nickname, realname=realname, **kwargs)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + '_')

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_privmsg(self, c, e):
        print('PRIVMSG', c, e)

    def on_pubmsg(self, c, e):
        print('PUBMSG', c, e)

def main():

    # use SSL
    ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)

    # configure logging
    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)

    # start the bot
    bot = WeakBets(connect_factory=ssl_factory)
    bot.start()

if __name__ == '__main__':
    main()
