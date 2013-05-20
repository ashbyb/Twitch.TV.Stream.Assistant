# -*- coding: utf_8 -*-

'''
Created on May 18, 2013
How is it already this late in May?


@author: Siye/Sye/Student
@copyright: Copyright 2013 Siye/Sye/Student - All Rights Reserved.
@summary: This is the main file for the Twitch IRC Bot
'''

# Define some globals
DEBUG = True
VERSION = 0.1

# Standard python lib imports
import sys
import Queue
import time
import datetime

# Import Core Qt modules
from PyQt4 import QtCore, QtGui

# Import the compiled UI module for main
from MainWindow_v1 import Ui_MainWindow

# Import Classes for child dialogs
from AccountManagementClass_v1 import Account_Management_Dialog

# Import out bot class
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
                #self.emit(QtCore.SIGNAL("bidsCountQueryThreadResults"), self.bids)
                self.running = False

    def _run(self):
        ''' Main function of thread. Runs the twitch bot main loop '''

        self.bot.start()


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


# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, None)

        # Create persistent settings object
        self.persistentSettings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, "Sye Products", "TwitchBot v%s" % VERSION)

        # Create class to maintain / distribute unique thread IDs
        self.threadIdSpooler = threadIdSpooler(self)

        # Create database interface
        #self.db = db(self, self.persistentSettings.fileName())

        # Create the main window class layout
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Create child window classes
        self.accounts = Account_Management_Dialog(self)

        # Signal Slot Connects for various UI elements to status log
        #QtCore.QObject.connect(self, QtCore.SIGNAL("appendLog"), self.log.appendLog)

        #################################
        # Final Calls to UI before Boot #
        #################################

        # Load persistent session data
        #self.loadPersistentSettings()

        # Emit Ready state
        #self.emit(QtCore.SIGNAL("appendLog"), "Twitch Bot Interface has booted. Ready to Work!")

    @QtCore.pyqtSignature("")
    def on_pushButton_manage_accounts_clicked(self):
        ''' Called when we click the manage accounts button '''

        self.accounts.show()

    @QtCore.pyqtSignature("")
    def on_commandLinkButton_authenticate_clicked(self):
        ''' Called when we click the authenticate button '''

        # Spawn bot thread (only 1 at a time for now) TODO: allow for many bots?
        self.twitchBotThread = twitchBotThread(self, self.threadIdSpooler.requestID(), self.accounts.requestSession())
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("finished()"), self.threadIdSpooler.returnID)
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("anIRCMessage"), self.handleTwitchBotIRCMessage)
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("IRCAuthenticationSuccess"), self.handleTwitchBotAuthenticationSuccess)
        self.twitchBotThread.start()

    def handleTwitchBotIRCMessage(self, data):
        ''' SLOT. Called by twitch bot thread when an IRC message was seen '''

        print data

        strings_chat = QtCore.QStringList()
        strings_chat.append(str(datetime.datetime.now().strftime("%H:%M:%S")))
        strings_chat.append(data[1])
        strings_chat.append(data[0])
        QtGui.QTreeWidgetItem(self.ui.treeWidget_chat, strings_chat)

    def handleTwitchBotAuthenticationSuccess(self):
        ''' SLOT. Called by twitch bot thread when it was able to successfully join an irc server '''

        self.ui.stackedWidget_main.setCurrentIndex(1) # Set to chat interface


def main():

    # Start up main PyQT Application loop
    app = QtGui.QApplication(sys.argv)

    # Build main window
    window = Main()
    window.show()

    #Exit program when our window is closed.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
