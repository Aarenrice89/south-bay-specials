#!/bin/bash

python manage.py migrate

python manage.py runscript create_default_admin

python manage.py runscript load_specials_from_file

python manage.py collectstatic --no-input
