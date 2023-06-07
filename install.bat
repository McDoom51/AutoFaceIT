@echo off

REM Check if the script is running with admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :runasadmin
) else (
    echo Please run this script as Administrator.
    pause
    exit /b
)

:runasadmin
REM Get the source path as the current directory
set "source=%~dp0your_script.py"

REM Set the destination path
set "destination=C:\AutoFaceIT\your_script.py"

REM Move the script to the destination folder
move "%source%" "%destination%"

REM Create the system service
sc create AutoFaceIT binPath= "pythonw.exe %destination%"

REM Start the service
sc start AutoFaceIT

exit /b
