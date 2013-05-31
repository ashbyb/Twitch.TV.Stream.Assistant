#Written by FirelementalNE ported from ashbyb/student/Siye, Copyright 2013 | All Rights Reserved
#make sure you have correct stuff pyqt4-dev-tools
if ! pyuic > /dev/null; then
   echo -e "Command not found! Install? (y/n) \c"
   read
   if "$REPLY" = "y"; then
      sudo apt-get install pyqt4-dev-tools
   fi
fi

TWPYDIR=../..
TWUIDIR=../ui
MAINUI=${TWUIDIR}/MainWindow_v1.ui
MAINPY=${TWPYDIR}/src/MainWindow_v1.py
ACCTUI=${TWUIDIR}/AccountManagementWindow_v1.ui
ACCTPY=${TWPYDIR}/src/AccountManagementWindow_v1.py

#Show initial header dialog
echo "+---------------------------------------+"
echo "|       Siye\'s Twitch Bot Compiler     |"
echo "|                                       |"
echo "|               [Notice]                |"
echo "| All paths in this folder are absolute |"
echo "|   Modify them to work on your system  |"
echo "|                                       |"
echo "|   ... Press any key to continue ...   |"                   
echo "+---------------------------------------+"

# Wait for user input
read READIT1

#Compile the Main window ".ui" file to a valid ".py" file
echo "+------------------------------+"
echo "| Now Compiling Main Window... |"
echo "+------------------------------+"

sudo pyuic4 ${MAINUI} -o ${MAINPY}

#Compile the Account Management window ".ui" file to a valid ".py" file
echo "+---------------------------------------------+"
echo "| Now Compiling Accounts Management Window... |"
echo "+---------------------------------------------+"

sudo pyuic4 ${ACCTUI} -o ${ACCTPY}

# Compile the icons resource file ".qrc" to a valid ".py" file so the GUI can use the contained assets
echo "+---------------------------------+"
echo "| Now Compiling Image Assets...   |"
echo "+---------------------------------+"

sudo pyrcc4 ${TWPYDIR}/src/mediaLinux.qrc -o ${TWPYDIR}/src/media_rc.py

echo "+----------------------+"
echo "|  Finished Compiling! |"
echo "+----------------------+"

