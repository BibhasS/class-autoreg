@echo off
set BRAVE="C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
REM Use a dedicated profile so the debug window is separate from your normal one
set USERDATA=%USERPROFILE%\BraveDebugProfile

REM If Brave is already running, close that window first (the debug window is separate)
REM You can comment the next line out if you don't want it to kill existing Brave:
REM taskkill /IM brave.exe /F >NUL 2>&1

start "" %BRAVE% --remote-debugging-port=9222 --user-data-dir="%USERDATA%"
