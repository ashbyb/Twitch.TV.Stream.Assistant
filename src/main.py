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

import time
import datetime

# Import Core Qt modules
from PyQt4 import QtCore, QtGui

# Import the compiled UI module for main
from MainWindow_v1 import Ui_MainWindow

# Import Classes for child dialogs
from AccountManagementClass_v1 import Account_Management_Dialog

# Import out IRC Bot class
from bot import TwitchBot

# Import our threading classes
from Threading import threadIdSpooler, twitchBotThread


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
