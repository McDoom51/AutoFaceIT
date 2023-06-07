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
REM Stop and delete the system service
sc stop AutoFaceIT
sc delete AutoFaceIT

REM Remove the destination folder
set "destination=C:\AutoFaceIT"
if exist "%destination%" (
    rmdir /s /q "%destination%"
)

REM Remove the Python installer
del python-installer.exe

REM Remove the log files
set "logs_folder=%~dp0Logs"
if exist "%logs_folder%" (
    del /q "%logs_folder%\*"
    rmdir /s /q "%logs_folder%"
)

REM Get the source path as the current directory
set "source=%~dp0AutoFaceIT.py"

REM Set the destination path
set "destination=%~dp0AutoFaceIT.py"

REM Move the script to the destination folder
move "%source%" "%destination%"

REM Delete the script itself
del "%~f0"

echo Cleanup completed.

exit /b
