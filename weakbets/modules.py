def handle(bot, e, cmd):
    print('Handle command:', cmd)

    nck = e.source.nick
    chn = e.target
    con = bot.connection

    con.privmsg(chn, f'Hello {nck}!')
