@echo off

REM
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM
if '%errorlevel%' NEQ '0' (
    echo Please run as admin!
    timeout 3
    exit
) else ( goto uninstall )


:uninstall

pushd "%CD%"
CD /D "%~dp0"
regsvr32 /u "UnityCaptureFilter32bit.dll"
regsvr32 /u "UnityCaptureFilter64bit.dll"