#/bin/bash 

git pull https://github.com/That-Guy-Jack/SUBMIT-DISP

gunicorn --bind 0.0.0.0:5000 wsgi:app