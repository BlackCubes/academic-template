#!/bin/sh
source .env

export DATA_DIR=$HOME/$DATA

pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py collectstatic --clear
