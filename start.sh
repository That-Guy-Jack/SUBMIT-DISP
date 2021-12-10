#!/bin/bash 

#git pull https://github.com/That-Guy-Jack/SUBMIT-DISP

python gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app