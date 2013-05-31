#Written by FirelementalNE ported from ashbyb/student/Siye, Copyright 2013 | All Rights Reserved

PATH1=/usr/lib/python2.7/dist-packages/PyQt4/uic/pyuic.py
TWPYDIR=~/Twitch.TV.Stream.Assistant/src
TWUIDIR=~/Twitch.TV.Stream.Assistant/assets/ui
MAINUI=${TWUIDIR}/MainWindow_v1.ui
MAINPY=${TWPYDIR}/MainWindow_v1.py
ACCTUI=${TWUIDIR}/AccountManagementWindow_v1.ui
ACCTPY=${TWPYDIR}/AccountManagementWindow_v1.py
MEDIAQRC=${TWPYDIR}/media.qrc
MEDIAPY=${TWPYDIR}/media_rc.py

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

sudo python ${PATH1} ${MAINUI} -o ${MAINPY}

#Compile the Account Management window ".ui" file to a valid ".py" file
echo "+---------------------------------------------+"
echo "| Now Compiling Accounts Management Window... |"
echo "+---------------------------------------------+"

sudo python ${PATH1} ${ACCTUI} -o ${ACCTPY}

# Compile the icons resource file ".qrc" to a valid ".py" file so the GUI can use the contained assets
echo "+---------------------------------+"
echo "| Now Compiling Image Assets...   |"
echo "+---------------------------------+"

sudo python ${PATH1} ${MEDIAQRC} -o ${MEDIAPY}

echo "+----------------------+"
echo "|  Finished Compiling! |"
echo "+----------------------+"

