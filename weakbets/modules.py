import argparse

def handle(bot, e, cmd):
    print('Handle command:', cmd, e)

    base = cmd.split()[0]
    args = cmd.split()[1:]
    print(base, args)

    if base == 'test':
        do_test(bot, e, args)
    else:
        bot.connection.privmsg(e.target, f'No such module: {base}')

def do_test(bot, e, cmd):
    con = bot.connection
    chn = e.target

    parser = argparse.ArgumentParser(
            prog=con.get_nickname(),
            add_help=False,
            exit_on_error=False,
        )

    parser.add_argument('number', type=int, nargs='?')

    try:
        args = parser.parse_args(cmd)
        if args.number == 69:
            con.privmsg(chn, f'nice: {args.number}')
        else:
            con.privmsg(chn, f'ok: {args.number}')
    except argparse.ArgumentError as err:
        con.privmsg(chn, f'failed: {err}')
