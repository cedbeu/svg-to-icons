#!/bin/sh

# Check if the script is sourced
if [ "$(basename -- "$0")" = "$(basename -- "$BASH_SOURCE")" ]; then
    echo "Warning: This script is not sourced. The virtual environment will not remain active after execution."
fi

# Create the virtual environment if it does not exist
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate the virtual environment
. venv/bin/activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment setup complete."

# Message for sourced execution
if [ "$(basename -- "$0")" != "$(basename -- "$BASH_SOURCE")" ]; then
    echo "Virtual environment is now active."
    echo "Use 'deactivate' to exit the virtual environment."
else
    echo "Run 'source venv/bin/activate' to activate the virtual environment."
fi
