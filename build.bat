@echo off
REM Set the path to your Python script and FFmpeg executable
set SCRIPT_PATH=path\to\your\script.py
set FFMPEG_PATH=path\to\ffmpeg.exe

REM Add FFmpeg to the PATH
set PATH=%PATH%;%FFMPEG_PATH%

REM Use PyInstaller to build the Python script
pyinstaller --onefile %SCRIPT_PATH%

REM Copy FFmpeg to the dist directory
set SCRIPT_NAME=%~nSCRIPT_PATH%
copy %FFMPEG_PATH% dist\%SCRIPT_NAME%\ffmpeg.exe

echo Build completed.
pause