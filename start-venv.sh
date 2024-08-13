DIRECTORY=venv
if [ ! -d "$DIRECTORY" ]; then
    py -m venv venv
else 
    echo "venv folder exists, skip creating"
fi
echo "Run:: source $DIRECTORY/Scripts/activate to enable virtual environment, deactivate to disable it."
source $DIRECTORY/Scripts/activate