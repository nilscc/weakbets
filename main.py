# imports for logging
import argparse
import jaraco.logging

# imports for SSL support
import ssl
import irc.connection

# the main bot
import weakbets.bot


def main():

    # use SSL
    ssl_factory = irc.connection.Factory(wrapper=ssl.wrap_socket)

    # configure logging
    parser = argparse.ArgumentParser()
    jaraco.logging.add_arguments(parser)
    args = parser.parse_args()
    jaraco.logging.setup(args)

    # start the bot
    bot = weakbets.bot.WeakBets(connect_factory=ssl_factory)
    bot.start()


if __name__ == '__main__':
    main()
