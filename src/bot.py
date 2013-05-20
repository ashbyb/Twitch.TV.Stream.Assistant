# -*- coding: utf_8 -*-

'''
Modified on May 18, 2013

@originalauthor: Joel Rosdahl <joel@rosdahl.net>
@modifiedby: student
@summary: An IRC bot, modified to talk on twitch.tv's servers.

This bot uses the SingleServerIRCBot class from irc.bot.
The bot enters a channel and listens for commands.

To talk to the bot:

    ^command <arguments>

The known commands are:

    TBD
'''

# Import core modules from python IRC library
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

# For signal emitting
from PyQt4 import QtCore


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, parent, channel, nickname, server, port=6667, password=''):
        self.parent = parent
        if password == '':
            password = open('../assests/temp/pw.txt', 'r').readlines()[0].strip()
        serverSpec = irc.bot.ServerSpec(server, port, password)
        irc.bot.SingleServerIRCBot.__init__(self, [serverSpec], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        self.parent.emit(QtCore.SIGNAL("IRCAuthenticationSuccess"))
        c.join(self.channel)

    def on_privmsg(self, c, e):
        self.do_command(e, e.arguments[0])

    def on_pubmsg(self, c, e):
        self.parent.emit(QtCore.SIGNAL("anIRCMessage"), [e.arguments[0], e.source.nick])
        a = e.arguments[0].split(":", 1)
        if len(a) > 1 and irc.strings.lower(a[0]) == irc.strings.lower(self.connection.get_nickname()):
            self.do_command(e, a[1].strip())
        return

    def do_command(self, e, cmd):
        nick = e.source.nick
        target = self.channels.keys()[0]
        c = self.connection

        if cmd == "disconnect":
            self.disconnect()
        elif cmd == "die":
            self.die()
        elif cmd == "stats":
            nick = "#rpigamer"
            for chname, chobj in self.channels.items():
                c.privmsg(nick, "--- Channel statistics ---")
                c.privmsg(nick, "Channel: " + chname)
                users = chobj.users()
                users.sort()
                c.privmsg(nick, "Users: " + ", ".join(users))
                opers = chobj.opers()
                opers.sort()
                c.privmsg(nick, "Opers: " + ", ".join(opers))
                voiced = chobj.voiced()
                voiced.sort()
                c.privmsg(nick, "Voiced: " + ", ".join(voiced))
        elif cmd == "helloworld":
            print "trying to talk"
            c.send_raw("Hello World I am OpOpBot.")
            c.notice("#rpigamer", "test3Test")
            c.notice("#rpigamer", "test2Test")
            c.privmsg("#rpigamer", "test1Test")
        else:
            pass


def main():
    import sys
    if len(sys.argv) != 5:
        print "Usage: testbot <server[:port]> <channel> <nickname> <password>"
        sys.exit(1)

    s = sys.argv[1].split(":", 1)
    server = s[0]
    if len(s) == 2:
        try:
            port = int(s[1])
        except ValueError:
            print "Error: Erroneous port."
            sys.exit(1)
    else:
        port = 6667
    channel = sys.argv[2]
    nickname = sys.argv[3]
    password = sys.argv[4]

    bot = TwitchBot(channel, nickname, server, port, password)
    bot.start()

if __name__ == "__main__":
    main()
