'''
Created on May 18, 2013

@author: student
'''

# Import Qt modules
from PyQt4 import QtCore, QtGui

#Import .ui to .py generated layout
from AccountManagementWindow_v1 import Ui_Dialog_Account_Management


class Account_Management_Dialog(QtGui.QDialog):
    def __init__(self, parent):
        QtGui.QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)

        #Create our account window
        self.accounts = Ui_Dialog_Account_Management()
        self.accounts.setupUi(self)

        # Maintain password in a dict (There is no intention to store these passwords securly, so don't even start. >:| )
        self.passwords = {}

    @QtCore.pyqtSignature("")
    def on_pushButton_add_clicked(self):
        if self.accounts.lineEdit_username.text() != '' and self.accounts.lineEdit_username.text() not in self.passwords and self.accounts.lineEdit_password.text() != '' and (self.accounts.lineEdit_password.text() == self.accounts.lineEdit_password_confirm.text()):
            self.passwords[self.accounts.lineEdit_username.text()] = self.accounts.lineEdit_password.text()
            item = QtGui.QListWidgetItem(self.accounts.lineEdit_username.text(), self.accounts.listWidget_accounts)
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.accounts.lineEdit_username.setText("")
            self.accounts.lineEdit_password.setText("")
            self.accounts.lineEdit_password_confirm.setText("")
        elif self.accounts.lineEdit_username.text() == '' or self.accounts.lineEdit_username.text() in self.passwords:
            self.accounts.lineEdit_username.selectAll()
            self.accounts.lineEdit_username.setFocus()
        elif self.accounts.lineEdit_password.text() == '':
            self.accounts.lineEdit_password.selectAll()
            self.accounts.lineEdit_password.setFocus()
        else:
            self.accounts.lineEdit_password_confirm.selectAll()
            self.accounts.lineEdit_password_confirm.setFocus()

    def on_listWidget_accounts_currentItemChanged(self, item, olditem):
        if item is not None:
            self.accounts.groupBox_2.setEnabled(True)

    @QtCore.pyqtSignature("")
    def on_pushButton_remove_clicked(self):
        item = self.accounts.listWidget_accounts.takeItem(self.accounts.listWidget_accounts.currentRow())
        del self.passwords[item.text()]
        if self.accounts.listWidget_accounts.currentRow() < 0 and self.accounts.listWidget_accounts.count() > 0:
            self.accounts.listWidget_accounts.setCurrentItem(self.accounts.listWidget_accounts.item(0))
            self.accounts.listWidget_accounts.setFocus()
        elif self.accounts.listWidget_accounts.count() > 0:
            self.accounts.listWidget_accounts.setCurrentItem(self.accounts.listWidget_accounts.item(self.accounts.listWidget_accounts.currentRow()))
            self.accounts.listWidget_accounts.setFocus()
        else:
            self.accounts.groupBox_2.setEnabled(False)

    def requestSession(self):
        ''' Called when credentials (session data) needed to authenticate a bot '''

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
