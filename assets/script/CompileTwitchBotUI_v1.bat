@Echo off

REM Clear the screen before we start
cls

REM Written by ashbyb/student/Siye, Copyright 2013 | All Rights Reserved

REM Set the color of the CMD terminal
color 0A

SET PYUIC4=C:\Python27\Lib\site-packages\PyQt4\uic\pyuic.py
SET PYRCC4=C:\Python27\Lib\site-packages\PyQt4\pyrcc4.exe
SET TWPYDIR=..\..\src
SET TWUIDIR=..\ui
SET MAINUI=%TWUIDIR%\MainWindow_v1.ui
SET MAINPY=%TWPYDIR%\MainWindow_v1.py
SET ACCTUI=%TWUIDIR%\AccountManagementWindow_v1.ui
SET ACCTPY=%TWPYDIR%\AccountManagementWindow_v1.py
SET MEDIAQRC=%TWPYDIR%\media.qrc
SET MEDIAPY=%TWPYDIR%\media_rc.py


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

C:\Python27\python.exe %PYUIC4% %MAINUI% -o %MAINPY%

REM Compile the Account Management window ".ui" file to a valid ".py" file
Echo +---------------------------------------------+
Echo ^| Now Compiling Accounts Management Window... ^|
Echo +---------------------------------------------+

C:\Python27\python.exe %PYUIC4% %ACCTUI% -o %ACCTPY%

REM Compile the icons resource file ".qrc" to a valid ".py" file so the GUI can use the contained assets
Echo +---------------------------------+
Echo ^| Now Compiling Image Assets...   ^|
Echo +---------------------------------+

%PYRCC4% %TWPYDIR%\media.qrc -o %TWPYDIR%\media_rc.py

Echo +----------------------+
Echo ^|  Finished Compiling! ^|
Echo +----------------------+

pause

REM Some final clean up (Fix colors, and clear screen)
cls
color

Rem EOF
