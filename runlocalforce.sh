#!/bin/bash
ps ax | grep "0.0.0.0:9999" | grep -v grep | awk '{print $1}' | xargs kill
clear
echo "......................................................................"
echo "By AppFactory..."
echo "Run local server SEED..."
python3 manage.py runserver 0.0.0.0:9999 --settings=seed.settings.local

