#!/bin/bash
rm /var/www/db.sqlite3
find /var/www/ -path "*/migrations/*.py" -not -name "__init__.py" -delete
find /var/www/ -path "*/migrations/*.pyc" -delete

python3 ~/django/Vote_of_LeeLab/manage.py makemigrations
python3 ~/django/Vote_of_LeeLab/manage.py migrate

docker exec django /bin/bash docker_run.sh
