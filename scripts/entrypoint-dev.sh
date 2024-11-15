#!/bin/sh
source .env

export DATA_DIR=$HOME/$DATA

pipenv run python manage.py runserver 0.0.0.0:8000
