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

# Import our threading classes
from threadingClasses import threadIdSpooler, twitchBotThread


# Create a class for our main window
class Main(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self, None)

        # Create persistent settings object
        self.persistentSettings = QtCore.QSettings(QtCore.QSettings.IniFormat, QtCore.QSettings.UserScope, "OpposingOpinions Products", "TwitchBot v%s" % VERSION)

        # Create class to maintain / distribute unique thread IDs
        self.threadIdSpooler = threadIdSpooler(self)

        # Create the main window class layout
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Create child window classes
        self.accounts = Account_Management_Dialog(self)

        # Load persistent session data
        self.loadPersistentSettings()

    def loadPersistentSettings(self):
        ''' Called on startup. Loads all settings that should persist from session to session across all UI elements '''

        self.persistentSettings.beginGroup("MainWindow")
        self.resize(self.persistentSettings.value("size", QtCore.QSize(260, 228)).toSize())
        self.move(self.persistentSettings.value("pos", QtCore.QPoint(200, 200)).toPoint())
        self.importMainWindowPersistentItems(self.persistentSettings.value("persistentItems", {}).toMap())
        self.persistentSettings.endGroup()

        self.persistentSettings.beginGroup("AccountsWindow")
        self.accounts.loadAccountList(self.persistentSettings.value("accountList", []).toList())
        self.persistentSettings.endGroup()

    def savePersistentSettings(self):
        ''' Called at shutdown of app. Saves all settings that should persist from session to session for all UI elements '''

        self.persistentSettings.beginGroup("MainWindow")
        self.persistentSettings.setValue("size", self.size())
        self.persistentSettings.setValue("pos", self.pos())
        self.persistentSettings.setValue("persistentItems", QtCore.QVariant(self.exportMainWindowPersistentItems()))
        self.persistentSettings.endGroup()

        self.persistentSettings.beginGroup("AccountsWindow")
        self.persistentSettings.setValue("accountList", QtCore.QVariant(self.accounts.exportAccountList()))
        self.persistentSettings.endGroup()

    def exportMainWindowPersistentItems(self):
        ''' Called on program close. Saves any setting in the main window that need to be loaded on next startup '''

        pass

    def importMainWindowPersistentItems(self, data):
        ''' Called on start of program. Settings saved from previous program's close are now loaded into the UI '''

        pass

    def closeEvent(self, event):
        '''
        This event is thrown when a close event is created (File>Exit or clicking the 'X' symbol in the window manager)
        A simple "Are you sure" dialog is presented. If 'no' the event is ignored.
        Saving persistent settings to the resident OS ini file is done if "yes" is given. This is done right before the window closes.
        '''

        if QtGui.QMessageBox.question(self, 'Alert', "Are you sure you want to quit?", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No) == QtGui.QMessageBox.Yes:
            self.savePersistentSettings()
            event.accept()
        else:
            event.ignore()

    @QtCore.pyqtSignature("")
    def on_commandLinkButton_manage_accounts_clicked(self):
        ''' Called when we click the manage accounts button '''

        self.accounts.exec_()  # Blocking window

    @QtCore.pyqtSignature("")
    def on_commandLinkButton_authenticate_clicked(self):
        ''' Called when we click the authenticate button '''

        # Disable buttons until we fail or succeed
        self.ui.frame_buttons.setEnabled(False)

        # Update while we wait to authenticate, let the user know what we are doing
        self.ui.commandLinkButton_authenticate.setText("Authenticating Bot...")
        self.ui.commandLinkButton_authenticate.setDescription("")

        # Spawn bot thread (only 1 at a time for now) TODO: allow for many bots?
        self.twitchBotThread = twitchBotThread(self, self.threadIdSpooler.requestID(), self.accounts.requestSession())
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("finished()"), self.threadIdSpooler.returnID)
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("finished()"), self.handleTwitchBotThreadDeath)
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("anIRCMessage"), self.handleTwitchBotIRCMessage)
        QtCore.QObject.connect(self.twitchBotThread, QtCore.SIGNAL("IRCAuthenticationSuccess"), self.handleTwitchBotAuthenticationSuccess)
        self.twitchBotThread.start()

    def handleTwitchBotIRCMessage(self, data):
        ''' SLOT. Called by twitch bot thread when an IRC message was seen '''

        print data

        strings_chat = QtCore.QStringList()
        strings_chat.append(str(datetime.datetime.now().strftime("%H:%M:%S")))
        strings_chat.append(data[0])
        strings_chat.append(data[1])
        QtGui.QTreeWidgetItem(self.ui.treeWidget_chat, strings_chat)

    def handleTwitchBotAuthenticationSuccess(self):
        ''' SLOT. Called by twitch bot thread when it was able to successfully join an irc server '''

        self.ui.stackedWidget_main.setCurrentIndex(1) # Set to chat interface

    def handleTwitchBotThreadDeath(self):
        ''' SLOT. Called by twitch bot thread when it has terminated '''

        # TODO: This logic is simple and only works when we are using 1 bot at a time. If we start using multiple bots at once, then this needs to be modified

        self.ui.commandLinkButton_authenticate.setEnabled(True)
        self.ui.stackedWidget_main.setCurrentIndex(0) # Set to program start-up interface        

def main():

    # Start up main PyQT Application loop
    app = QtGui.QApplication(sys.argv)

    # Build and show main window
    window = Main()
    window.show()

    # Exit program when our window is closed.
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
