#!/bin/bash
pip3 install -r /var/www/requirements.txt
service apache2 restart
