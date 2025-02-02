#!/bin/bash

# Navigate to the project directory
cd /Users/kaani/Desktop/tomurcuk/src || exit

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf dist/ build/ __pycache__/ *.spec

# Run pyinstaller to build the project
echo "Running PyInstaller..."
pyinstaller --onefile --add-binary "ffmpeg:." main.py

echo "Build completed successfully!"
