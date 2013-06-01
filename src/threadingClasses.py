# -*- coding: utf_8 -*-

'''
Created on May 31, 2013

@author: Siye/Sye/Student
@copyright: Copyright 2013 Siye/Sye/Student - All Rights Reserved.
@summary: Holds class definitions for threads
'''

# Import python libs
import Queue

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

        # Let's construct our bot with our session data
        self.bot = TwitchBot(self, self.session['channel'], self.session['nickname'], self.session['server'], self.session['port'], self.session['password'])

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
                    import traceback
                    print "TWITCHBOT ERROR:", sys.exc_info()[:-1], traceback.print_tb(sys.exc_info()[2], file=sys.stdout)
                    self.running = False
                else:
                    time.sleep(3)
            else:
                self.running = False

    def _run(self):
        ''' Main function of thread. Runs the twitch bot main loop '''

        print "Enter"
        self.bot.start()
        print "Exit"

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
