#!/bin/bash
set -e

# check for Python 3
if ! command -v python3 &> /dev/null; then
    echo "Python3 is not installed."
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# activate the virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# upgrade pip safely inside venv
echo "Upgrading pip inside virtual environment..."
python -m pip install --upgrade pip

# install dependencies
echo "Installing pygame into virtual environment..."
python -m pip install pygame

echo "Setup complete!"

