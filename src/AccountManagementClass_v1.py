'''
Created on May 18, 2013

@author: student
'''

# Import Qt modules
from PyQt4 import QtCore, QtGui

#Import .ui to .py generated layout
from AccountManagementWindow_v1 import Ui_Dialog_Account_Management


# Let's build a simple class to hold information on our accounts
class BotAccount(object):
    def __init__(self, username, password, channel):
        self.username = username
        self.password = password
        self.channel = channel

    def __repr__(self):
        return "%s:%s:%s" % (self.username, self.password, self.channel)


class Account_Management_Dialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        # Create our account window
        self.accounts = Ui_Dialog_Account_Management()
        self.accounts.setupUi(self)

        # List of all accounts
        self.accountsDict = {}

    @QtCore.pyqtSignature("")
    def on_pushButton_add_clicked(self):
        # Simple checks of input
        if self.accounts.lineEdit_username.text() == '' or self.accounts.lineEdit_username.text() in self.accountsDict:
            self.accounts.lineEdit_username.selectAll()
            self.accounts.lineEdit_username.setFocus()
        elif self.accounts.lineEdit_password.text() == '':
            self.accounts.lineEdit_password.selectAll()
            self.accounts.lineEdit_password.setFocus()
        elif self.accounts.lineEdit_password.text() != self.accounts.lineEdit_password_confirm.text():
            self.accounts.lineEdit_password_confirm.selectAll()
            self.accounts.lineEdit_password_confirm.setFocus()
        elif self.accounts.lineEdit_default_channel.text() == '' or self.accounts.lineEdit_default_channel.text()[0] != '#':
            self.accounts.lineEdit_default_channel.selectAll()
            self.accounts.lineEdit_default_channel.setFocus()
        else:
            # Input is good
            self.accountsDict[self.accounts.lineEdit_username.text()] = BotAccount(self.accounts.lineEdit_username.text(), self.accounts.lineEdit_password.text(), self.accounts.lineEdit_default_channel.text())
            item = QtGui.QListWidgetItem(self.accounts.lineEdit_username.text(), self.accounts.listWidget_accounts)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.accounts.lineEdit_username.setText("")
            self.accounts.lineEdit_password.setText("")
            self.accounts.lineEdit_password_confirm.setText("")
            self.accounts.lineEdit_default_channel.setText("")
        
    def on_listWidget_accounts_currentItemChanged(self, item, olditem):
        if item is not None:
            self.accounts.groupBox_edit_account.setEnabled(True)

    @QtCore.pyqtSignature("")
    def on_pushButton_remove_clicked(self):
        item = self.accounts.listWidget_accounts.takeItem(self.accounts.listWidget_accounts.currentRow())
        del self.accountsDict[item.text()]
        if self.accounts.listWidget_accounts.currentRow() < 0 and self.accounts.listWidget_accounts.count() > 0:
            self.accounts.listWidget_accounts.setCurrentItem(self.accounts.listWidget_accounts.item(0))
            self.accounts.listWidget_accounts.setFocus()
        elif self.accounts.listWidget_accounts.count() > 0:
            self.accounts.listWidget_accounts.setCurrentItem(self.accounts.listWidget_accounts.item(self.accounts.listWidget_accounts.currentRow()))
            self.accounts.listWidget_accounts.setFocus()
        else:
            self.accounts.groupBox_edit_account.setEnabled(False)

    def requestSession(self):
        ''' Called when credentials (session data) needed to authenticate a bot '''

        # TODO: Implement selecting a specific acount on request and not default to the first item in the list

        return {'nickname': 'opopbot', 'channel': '#rpigamer', 'port': 6667, 'server': 'rpigamer.jtvirc.com', 'password': ''}

    def exportAccountList(self):
        '''
        Provides a method to convert all accounts to a list, for exporting / session persistence
        '''

        tmplist = []
        for i in range(self.accounts.listWidget_accounts.count()):
            tmplist.append(self.accounts.listWidget_accounts.item(i).text() + ':' + self.passwords[self.accounts.listWidget_accounts.item(i).text()])
        return tmplist

    def loadAccountList(self, accountlist):
        '''
        Provides a method to fill our account list with username:password pairs provided in a list
        '''

        for item in accountlist:
            strings_account = QtCore.QStringList()
            strings_account.append(str(datetime.datetime.now().strftime("%H:%M:%S")))
            strings_chat.append(data[1])
            strings_chat.append(data[0])
            QtGui.QTreeWidgetItem(self.ui.treeWidget_chat, strings_chat)
            appendedItem = QtGui.QListWidgetItem(item.toString().split(':')[0], self.accounts.listWidget_accounts)
            appendedItem.setTextAlignment(QtCore.Qt.AlignCenter)
            self.passwords[item.toString().split(':')[0]] = item.toString().split(':')[1]

    def exportLayoutDefaults(self):
        '''
        Provides a method to convert all the setting UI states to a dict for exporting / session persistence
        '''

        settings = {}

        # TODO: Add things to be saved here

        return settings

    def importLayoutDefaults(self, data):
        '''
        Provides a method to set all the setting UI states according to a passed in dict of their states.
        Used in session persistence.
        '''

        pass
