#!/usr/bin/env bash

# Exit immediately if a command fails

set -e

echo "Activating virtual environment..."

#activate the virtual environment
if [ -d "venv" ]; then 
    source venv/Scripts/activate
else
    echo "Virtual environment not found"
    exit 1
fi


echo "Running test suite...."

#running pytest

pytest

#if the pytest exits with 0, then tests has successfully passed 
echo "All tests are passed successfully"
exit 0
