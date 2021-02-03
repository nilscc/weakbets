import sys

# irc library
import irc.bot

# importlib is used for dynamically reloading modules
import importlib

# main modules entry
import weakbets.modules

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

    def on_pubmsg(self, c, e):
        n = self.connection.get_nickname()
        a = e.arguments[0].split(':', 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(n):
            self.do_command(e, ' '.join(a[1:]).strip())

    def do_command(self, e, cmd):
        con = self.connection

        if cmd == 'reload':
            self.reload(e)
        else:
            try:
                weakbets.modules.handle(self, e, cmd)
            except Exception as exc:
                print(exc, file=sys.stderr)
                con.privmsg(e.target, 'idk?')

    def reload(self, e):
        con = self.connection
        try:
            importlib.reload(weakbets.modules)
            weakbets.modules.reload()
            con.privmsg(e.target, 'Reload successful.')
        except:
            con.privmsg(e.target, 'Reload failed.')
