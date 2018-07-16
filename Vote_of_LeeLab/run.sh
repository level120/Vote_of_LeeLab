#!/bin/bash
pip3 install -r requirements.txt
python3 manage.py migrate
service apache2 restart
