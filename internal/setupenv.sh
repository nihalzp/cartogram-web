#!/bin/bash

VIRTUALENV_LOCATION=${VIRTUALENV_LOCATION:=venv}
PYTHON=${PYTHON:="/usr/bin/python3"}

if [ ! -d "$VIRTUALENV_LOCATION" ]; then

    echo "Setting up Python virtualenv..."

    virtualenv -p "$PYTHON" "$VIRTUALENV_LOCATION/"

fi

source "$VIRTUALENV_LOCATION/bin/activate"

echo "Installing software components..."

pip install -r requirements.txt

echo -n "Setting environment variables... "

source ./envsettings.sh

if [ $? -eq 0 ]; then

    echo "OK"
else

    echo "FAIL"
    echo
    echo "Please make sure that envsettings.sh exists."
    deactivate
fi

echo "Done."
