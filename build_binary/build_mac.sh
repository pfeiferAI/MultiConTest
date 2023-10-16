#!/bin/bash
# Build app for macOS with pyinstaller and optionally package it into a DMG
# This script must be run on macOS and requires create-dmg to be installed
# This scipt will not generate a universal2 binary -> run it each target architecture separately!

# Check if output directory argument is provided
if [ -z "$1" ]
    then
        echo "Error: Output directory argument is missing"
        exit 1
fi

# Check if package argument is provided and set PACKAGE variable
if [ -z "$2" ]
    then
        PACKAGE=False
    else
        PACKAGE=True
fi

# Create dist and build folders in output directory
mkdir -p "$1/dist"
mkdir -p "$1/build"

# Run pyinstaller on macApp.spec
# (cd "../mulicontest"; pyinstaller macApp.spec --distpath="$1/dist" --workpath="$1/build" --clean -y)
pyinstaller macApp.spec --distpath="$1/dist" --workpath="$1/build" --clean -y

# Check if pyinstaller ran successfully
if [ $? -eq 0 ]
    then
        echo "Pyinstaller ran successfully"
    else
        echo "Pyinstaller failed"
        exit 1
fi

# Exit if package argument is not provided
if [ "$PACKAGE" = False ]
    then
        exit 0
fi

# read the 'app = ' section from macApp.spec and look for 'name=' and 'icon=' to define APP_NAME and APP_ICON
APP_NAME=$(sed -n '/app = /,$p' macApp.spec | grep 'name=' | tr -d ' ' | cut -d '=' -f 2 | tr -d "'" | tr -d ',')
APP_ICON=$(sed -n '/app = /,$p' macApp.spec | grep 'icon=' | tr -d ' ' | cut -d '=' -f 2 | tr -d "'" | tr -d ',')

# run build_dmg.sh
./build_dmg.sh "$1/dist" "$APP_NAME" "$APP_ICON"