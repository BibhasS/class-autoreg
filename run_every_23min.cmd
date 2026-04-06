@echo off
setlocal EnableExtensions
title Class Auto-Register (every 23 min)
cd /d "%~dp0"
call ".venv\Scripts\activate.bat"

:loop
echo.
echo ==============================
echo [%date% %time%] Running auto-register...
echo ==============================

python ".\brave_click_register.py" >> ".\auto_reg.log" 2>&1

echo ---- Last 5 log entries ----
powershell -NoProfile -Command "Get-Content -Path '.\auto_reg.log' -Tail 5"
echo ---------------------------
echo [%date% %time%] Cycle complete. Sleeping 23 minutes...

REM Use PowerShell sleep instead of TIMEOUT to avoid that syntax error
powershell -NoProfile -Command "Start-Sleep -Seconds 1380"

goto loop
