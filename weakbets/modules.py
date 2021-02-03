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

    parser = argparse.ArgumentParser(
            prog=con.get_nickname(),
            add_help=False,
            exit_on_error=False,
        )

    parser.add_argument('numbers', type=int, nargs='?')

    try:
        args = parser.parse_args(cmd)
        con.privmsg(e.target, f'ok: {args.numbers}')
    except argparse.ArgumentError as err:
        con.privmsg(e.target, f'failed: {err}')
