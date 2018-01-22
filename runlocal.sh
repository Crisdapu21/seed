#!/bin/bash
clear
echo "......................................................................"
echo "By AppFactory..."
echo "Run local server SEED..."
python3 manage.py runserver 0.0.0.0:9999 --settings=seed.settings.local

