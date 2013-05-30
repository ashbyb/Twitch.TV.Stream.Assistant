@Echo off

REM Clear the screen before we start
cls

REM Written by Siye, Copyright 2013 | All Rights Reserved

REM Set the color of the CMD terminal
color 0A

REM Show initial header dialog
Echo +---------------------------------------+
Echo ^|       Siye's Twitch Bot Compiler      ^|
Echo ^|                                       ^|
Echo ^|               [Notice]                ^|
Echo ^| All paths in this folder are absolute ^|
Echo ^|   Modify them to work on your system  ^|
Echo ^|                                       ^|
Echo ^|   ... Press any key to continue ...   ^|                   
Echo +---------------------------------------+

REM Wait for user input
pause > nul

REM Compile the Main window ".ui" file to a valid ".py" file
Echo +------------------------------+
Echo ^| Now Compiling Main Window... ^|
Echo +------------------------------+

"C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" "C:\Users\morro_000\workspace\TwitchChatBot\MainWindow_v1.ui" -o "C:\Users\morro_000\workspace\TwitchChatBot\MainWindow_v1.py"

REM Compile the Account Management window ".ui" file to a valid ".py" file
Echo +---------------------------------------------+
Echo ^| Now Compiling Accounts Management Window... ^|
Echo +---------------------------------------------+

"C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py" "C:\Users\morro_000\workspace\TwitchChatBot\AccountManagementWindow_v1.ui" -o "C:\Users\morro_000\workspace\TwitchChatBot\AccountManagementWindow_v1.py"

REM Compile the icons recourse file ".ui" to a valid ".py" file so the GUI can use the contained assets
Echo +---------------------------------+
Echo ^| Now Compiling Image Assets...   ^|
Echo +---------------------------------+

"C:\Python27\Lib\site-packages\PyQt4\pyrcc4.exe" "C:\Users\morro_000\workspace\TwitchChatBot\media.qrc" -o "C:\Users\morro_000\workspace\TwitchChatBot\media_rc.py"

Echo +----------------------+
Echo ^|  Finished Compiling! ^|
Echo +----------------------+

pause

REM Some final clean up (Fix colors, and clear screen)
cls
color

Rem EOF


AccountManagementWindow_v1