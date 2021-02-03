import irc.bot

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
        pass
