@echo off
title BlackHole V6 Launcher (Interactive)
cd /d %~dp0

set /p mode=Enter mode (encrypt/decrypt): 
set /p message=Enter message or path to .bhex file: 
set /p password=Enter password: 

echo Running BlackHole with mode: %mode%
python main.py --mode %mode% --message "%message%" --password "%password%"

pause
