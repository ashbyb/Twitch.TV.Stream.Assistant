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

    ^helloworld :   OpOpBot will say hello to the channel
    ^stats      :   OpOpBot will print stats on all the rooms and users it can see to the room (assume one room for now)
'''

# Import core modules from python IRC library
import irc.bot
import irc.strings
from irc.client import ip_numstr_to_quad, ip_quad_to_numstr

# For signal emitting
from PyQt4 import QtCore


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, parent, channel, nickname, server, port, password):
        self.parent = parent
        self.channel = channel
        serverSpec = irc.bot.ServerSpec(server, port, password)
        irc.bot.SingleServerIRCBot.__init__(self, [serverSpec], nickname, nickname, reconnection_interval=0)

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        print "yar"
        self.parent.emit(QtCore.SIGNAL("IRCAuthenticationSuccess"))
        c.join(self.channel)

    def on_privmsg(self, c, e):
        pass

    def on_pubmsg(self, c, e):
        self.parent.emit(QtCore.SIGNAL("anIRCMessage"), [e.source.nick, e.arguments[0]])
        if len(e.arguments[0]) > 1 and irc.strings.lower(e.arguments[0][0]) == irc.strings.lower('^'):
            self.do_command(e, e.arguments[0][1:].strip())
        return

    def do_command(self, e, cmd):
        nick = self.channel
        c = self.connection

        if cmd == "disconnect":
            self.disconnect()
        elif cmd == "die":
            self.die()
        elif cmd == "stats":
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
            c.privmsg(nick, "Hello World. I am OpOpBot.")
        else:
            pass
