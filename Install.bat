@echo off

REM Check if the script is running with admin rights
net session >nul 2>&1
if %errorLevel% == 0 (
    goto :runasadmin
) else (
    echo Set objShell = CreateObject("Shell.Application") > "%temp%\runas.vbs"
    echo args = "" >> "%temp%\runas.vbs"
    echo For Each arg in WScript.Arguments >> "%temp%\runas.vbs"
    echo   args = args & " " & arg >> "%temp%\runas.vbs"
    echo Next >> "%temp%\runas.vbs"
    echo objShell.ShellExecute "cmd.exe", "/c """ & WScript.ScriptFullName & """ " & args, "", "runas" >> "%temp%\runas.vbs"
    cscript //nologo "%temp%\runas.vbs" %* >nul 2>&1
    del "%temp%\runas.vbs"
    exit /b
)

:runasadmin
REM Check if Python is installed
python --version >nul 2>&1
if %errorLevel% NEQ 0 (
    echo Python is not installed. Installing Python...
    REM Download the latest Python installer
    curl -Lo python-installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe

    REM Install Python
    echo Installing Python. Please wait...
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0
    if %errorLevel% NEQ 0 (
        echo Failed to install Python. Exiting...
        pause
        exit /b
    )

    REM Remove the Python installer
    del python-installer.exe
    echo Python installation completed.
)

REM Install required Python libraries
echo Installing required Python libraries...
pip install psutil
pip install subprocess.run
pip install logging
if %errorLevel% NEQ 0 (
    echo Failed to install required libraries. Exiting...
    pause
    exit /b
)

REM Get the source path as the current directory
set "source=%~dp0AutoFaceIT.py"

REM Set the destination path
set "destination=C:\AutoFaceIT\AutoFaceIT.py"

REM Move the script to the destination folder
move "%source%" "%destination%"

REM Create the system service
sc create AutoFaceIT binPath= "pythonw.exe %destination%"

REM Start the service
sc start AutoFaceIT

exit /b
