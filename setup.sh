#!/bin/bash
set -e

# check Python 3
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed. Install it before running this script."
    exit 1
fi

# create virtual env if not exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Upgrading pip..."
python3 -m pip install --upgrade pip --break-system-packages

echo "Installing dependencies..."
python3 -m pip install pygame --break-system-packages

echo "Setup complete!"
