# -*- coding: utf_8 -*-

'''
Created on May 31, 2013

@author: Siye/Sye/Student
@copyright: Copyright 2013 Siye/Sye/Student - All Rights Reserved.
@summary: Holds class definitions for threads
'''

# Import python libs
import Queue
import time

# Import Core Qt modules
from PyQt4 import QtCore, QtGui

# Import out IRC Bot class
from bot import TwitchBot


# Thread class for running the main processEvents loop of the twitch bot class
class twitchBotThread(QtCore.QThread):
    def __init__(self, parent, ident, session, running=True, failureThreshold=5):
        super(twitchBotThread, self).__init__(parent)
        self.parent = parent
        self.id = ident
        self.session = session
        self.running = running
        self.failureThreshold = failureThreshold

        # Bind parent event for talking through us to chat room
        QtCore.QObject.connect(self.parent, QtCore.SIGNAL("sendIRCMessageToRoom"), self.talk)

    def stop(self):
        self.running = False

    def run(self):

        failures = 0

        while self.running:
            try:
                self._run()
            except:
                failures += 1
                if failures > self.failureThreshold:
                    self.running = False
                else:
                    self.emit(QtCore.SIGNAL("botThreadPartialFailure"), failures, self.failureThreshold)
                    time.sleep(1)
            else:
                self.running = False

    def _run(self):
        ''' Main function of thread. Runs the twitch bot main loop '''

        try:
            # Build and run bot in _run, so failures in both commands can be caught in failure threshold logic
            self.bot = TwitchBot(self, self.session['channel'], self.session['nickname'], self.session['server'], self.session['port'], self.session['password'])
            self.bot.start()
        except Exception,e:
            print str(e)

    def talk(self, msg):
        ''' SLOT. Called by GUI when user is talking to IRC chatroom from UI '''

        self.bot.talk(msg)

# Class that handles giving threads IDs (PyQt does not implement this natively)
class threadIdSpooler(QtCore.QObject):
    def __init__(self, parent):
        super(threadIdSpooler, self).__init__(parent)
        self.curID = 0
        self.pool = Queue.Queue()

    def requestID(self):
        if self.pool.empty():
            self.curID += 1
            return self.curID - 1
        else:
            return self.pool.get_nowait()

    def returnID(self):
        returningID = self.sender().id
        self.pool.put_nowait(returningID)
