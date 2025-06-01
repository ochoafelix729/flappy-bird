#!/bin/bash
set -e

echo 'Creating virtual environment...'
python3 -m venv venv

echo 'Activating virtual environment...'

echo 'Installing dependencies...'
pip install pygame

echo 'Setup complete! Your system is ready.'