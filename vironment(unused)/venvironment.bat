@echo on
 set VENV_DIR=..\virenvproject

if not exist "%VENV_DIR%" (
    echo Creating virtual environment...
    python -m venv %VENV_DIR%
    echo Virtual environment created.
)

echo Activating virtual environment...
..\virenvproject\Scripts\activate

echo Installing requirements...
pip install -r %VENV_DIR%\requirements.txt
echo Requirements installed.

echo Virtual environment setup completed.

pause > nul
