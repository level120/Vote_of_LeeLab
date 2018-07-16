#!/bin/bash
pip3 install -r requirements.txt
python3 Vote_of_LeeLab/manage.py migrate
service apache2 restart
