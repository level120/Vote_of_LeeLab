#!/bin/bash
pip3 install -r /var/www/requirements.txt
#rm /var/www/db.sqlite3
#find . -path "/var/www/*/migrations/*.py" -not -name "__init__.py" -delete
#find . -path "/var/www/*/migrations/*.pyc"  -delete
python3 /var/www/manage.py makemigrations
python3 /var/www/manage.py migrate
service apache2 restart
