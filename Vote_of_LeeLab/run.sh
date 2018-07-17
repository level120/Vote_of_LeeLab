#!/bin/bash
rm ~/django/Vote_of_LeeLab/db.sqlite3
find ~/django/Vote_of_LeeLab/ -path "*/migrations/*.py" -not -name "__init__.py" -delete
find ~/django/Vote_of_LeeLab/ -path "*/migrations/*.pyc" -delete

python3 ~/django/Vote_of_LeeLab/manage.py makemigrations
python3 ~/django/Vote_of_LeeLab/manage.py migrate

docker exec django /bin/bash docker_run.sh
