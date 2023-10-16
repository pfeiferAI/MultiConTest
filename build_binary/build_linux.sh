#!/bin/bash
# Build app for Linux with pyinstaller
# This script must be run on Linux

# Check if output directory argument is provided
if [ -z "$1" ]
    then
        echo "Error: Output directory argument is missing"
        exit 1
fi

# Create dist and build folders in output directory
mkdir -p "$1/dist"
mkdir -p "$1/build"

# Run pyinstaller on linuxApp.spec
pyinstaller linuxApp.spec --distpath="$1/dist" --workpath="$1/build" --clean

# Check if pyinstaller ran successfully
if [ $? -eq 0 ]
    then
        echo "Pyinstaller ran successfully"
        exit 0
    else
        echo "Pyinstaller failed"
        exit 1
fi