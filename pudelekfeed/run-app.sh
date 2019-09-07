#!/bin/bash
echo "Creating virtual env..."
python -m venv env
echo "Starting using virtual env..."
source env/bin/activate
echo "Upgrading pip..."
python -m pip install --upgrade pip
echo "Installing pika..."
pip install pika
echo "Installing bs4"
pip install bs4
echo "Runinng app.py..."
python app.py