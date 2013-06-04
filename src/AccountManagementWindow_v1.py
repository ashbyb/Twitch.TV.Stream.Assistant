# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '..\ui\AccountManagementWindow_v1.ui'
#
# Created: Mon Jun 03 22:27:56 2013
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog_Account_Management(object):
    def setupUi(self, Dialog_Account_Management):
        Dialog_Account_Management.setObjectName(_fromUtf8("Dialog_Account_Management"))
        Dialog_Account_Management.resize(327, 291)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/Gnome-Input-Gaming.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog_Account_Management.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(Dialog_Account_Management)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog_Account_Management)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Close)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 4, 1, 1, 1)
        self.listWidget_accounts = QtGui.QListWidget(Dialog_Account_Management)
        self.listWidget_accounts.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.listWidget_accounts.setAlternatingRowColors(True)
        self.listWidget_accounts.setObjectName(_fromUtf8("listWidget_accounts"))
        self.gridLayout.addWidget(self.listWidget_accounts, 0, 0, 5, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)
        self.groupBox = QtGui.QGroupBox(Dialog_Account_Management)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEdit_username = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_username.setObjectName(_fromUtf8("lineEdit_username"))
        self.verticalLayout_2.addWidget(self.lineEdit_username)
        self.lineEdit_password = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_password.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password.setObjectName(_fromUtf8("lineEdit_password"))
        self.verticalLayout_2.addWidget(self.lineEdit_password)
        self.lineEdit_password_confirm = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_password_confirm.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_password_confirm.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_password_confirm.setObjectName(_fromUtf8("lineEdit_password_confirm"))
        self.verticalLayout_2.addWidget(self.lineEdit_password_confirm)
        self.lineEdit_default_channel = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_default_channel.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_default_channel.setObjectName(_fromUtf8("lineEdit_default_channel"))
        self.verticalLayout_2.addWidget(self.lineEdit_default_channel)
        self.pushButton_add = QtGui.QPushButton(self.groupBox)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/Gnome-Colors-Emblem-Green.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_add.setIcon(icon1)
        self.pushButton_add.setObjectName(_fromUtf8("pushButton_add"))
        self.verticalLayout_2.addWidget(self.pushButton_add)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 2, 1)
        self.groupBox_edit_account = QtGui.QGroupBox(Dialog_Account_Management)
        self.groupBox_edit_account.setEnabled(False)
        self.groupBox_edit_account.setObjectName(_fromUtf8("groupBox_edit_account"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_edit_account)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.pushButton_remove = QtGui.QPushButton(self.groupBox_edit_account)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/assets/icons/Gnome-Colors-Emblem-Desktop-Red.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_remove.setIcon(icon2)
        self.pushButton_remove.setObjectName(_fromUtf8("pushButton_remove"))
        self.gridLayout_2.addWidget(self.pushButton_remove, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_edit_account, 2, 1, 1, 1)

        self.retranslateUi(Dialog_Account_Management)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog_Account_Management.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog_Account_Management.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Account_Management)

    def retranslateUi(self, Dialog_Account_Management):
        Dialog_Account_Management.setWindowTitle(_translate("Dialog_Account_Management", "Account Management", None))
        self.groupBox.setTitle(_translate("Dialog_Account_Management", "Add Bot Account", None))
        self.lineEdit_username.setPlaceholderText(_translate("Dialog_Account_Management", "Username", None))
        self.lineEdit_password.setPlaceholderText(_translate("Dialog_Account_Management", "Password", None))
        self.lineEdit_password_confirm.setPlaceholderText(_translate("Dialog_Account_Management", "Confirm Password", None))
        self.lineEdit_default_channel.setPlaceholderText(_translate("Dialog_Account_Management", "IRC Channel e.g. #rpigamer", None))
        self.pushButton_add.setText(_translate("Dialog_Account_Management", "Add Account", None))
        self.groupBox_edit_account.setTitle(_translate("Dialog_Account_Management", "Edit Account", None))
        self.pushButton_remove.setText(_translate("Dialog_Account_Management", "Remove Selected Account", None))

import media_rc
