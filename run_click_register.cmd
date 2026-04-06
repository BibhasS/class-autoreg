@echo off
title Class Auto-Register
cd /d %~dp0

echo.
echo ==============================
echo [%date% %time%] Running auto-register...
echo ==============================

call ".venv\Scripts\activate.bat"
python ".\brave_click_register.py" >> ".\auto_reg.log" 2>&1

echo.
echo ---- Last 5 log entries ----
powershell -NoProfile -Command "Get-Content -Path '.\auto_reg.log' -Tail 5"
echo ---------------------------
echo [%date% %time%] Done.
echo.
