@echo off
cd /d %~dp0
call ".venv\Scripts\activate.bat"

:loop
echo [%date% %time%] Running test...
python ".\brave_click_register.py"
echo Waiting 45 seconds...
timeout /t 45 >nul
goto loop
