#!/bin/bash
pip3 install -r requirements.txt
python3 /var/www/manage.py makemigrations
python3 /var/www/manage.py migrate
service apache2 restart
