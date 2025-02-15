@echo off
setlocal

:: Check if the script is run directly or sourced
if "%~0"=="%~f0" (
    echo Warning: This script is not sourced. The virtual environment will not remain active after execution.
)

:: Check if the virtual environment exists
if not exist venv (
    python -m venv venv
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt

echo Environment setup complete.

:: Message for sourced execution
if "%~0" neq "%~f0" (
    echo Virtual environment is now active.
    echo Use 'deactivate' to exit the virtual environment.
) else (
    echo Run 'venv\Scripts\activate' to activate the virtual environment.
)

endlocal
