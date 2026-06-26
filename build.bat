@echo off

pyinstaller ^
-F ^
-w ^
-n WhisperLRC-Pro ^
--icon app/resources/icon.ico ^
main.py

pause
