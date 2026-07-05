@echo off
set "SCRIPT_DIR=%~dp0"

where py >nul 2>nul
if %errorlevel%==0 (
  py -3 "%SCRIPT_DIR%slackbox_cli.py" init %*
  exit /b %errorlevel%
)

where python >nul 2>nul
if %errorlevel%==0 (
  python "%SCRIPT_DIR%slackbox_cli.py" init %*
  exit /b %errorlevel%
)

echo Slackbox setup requires Python 3. Install Python 3 and try again. 1>&2
exit /b 127
