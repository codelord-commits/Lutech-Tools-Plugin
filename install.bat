@echo off
chcp 65001 >nul
REM Double-click de cai plugin lutech-tools.
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0install.ps1" %*
echo.
pause
