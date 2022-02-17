@echo off

REM 
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM
if '%errorlevel%' NEQ '0' (
    echo Please run as admin!
    timeout 3
    exit
) else ( goto install )


:install

pushd "%CD%"
CD /D "%~dp0"

set UCCAPNAME=IPCamera
echo Installing capture device named '%UCCAPNAME%' ...
regsvr32 "UnityCaptureFilter32bit.dll" "/i:UnityCaptureName=%UCCAPNAME%"
regsvr32 "UnityCaptureFilter64bit.dll" "/i:UnityCaptureName=%UCCAPNAME%"
echo "Done"