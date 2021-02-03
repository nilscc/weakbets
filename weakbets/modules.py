import argparse
import weakbets.alphavantage.api

def reload():
    # reloading of modules
    import importlib
    importlib.reload(weakbets.alphavantage.api)
    weakbets.alphavantage.api.reload()

def handle(bot, e, cmd):
    print('Handle command:', cmd, e)

    base = cmd.split()[0]
    args = cmd.split()[1:]
    print(base, args)

    if base == 'quote':
        do_quote(bot, e, args)
    else:
        bot.connection.privmsg(e.target, f'No such module: {base}')

def do_quote(bot, e, cmd):
    con = bot.connection
    chn = e.target
    nck = e.source.nick

    parser = argparse.ArgumentParser(
            prog=con.get_nickname(),
            add_help=False,
            exit_on_error=False,
        )

    parser.add_argument('symbol', type=str)

    try:
        args = parser.parse_args(cmd)

        # get global quote from AlphaVantage
        res = weakbets.alphavantage.api.global_quote(args.symbol)

        con.privmsg(chn, f'{res}')

    except argparse.ArgumentError as err:
        con.privmsg(chn, f'Invalid arguments: {err}')
