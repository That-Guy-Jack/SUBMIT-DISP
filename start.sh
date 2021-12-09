#!/bin/bash 

#it pull https://github.com/That-Guy-Jack/SUBMIT-DISP

pyhton gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi:app