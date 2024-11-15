#!/bin/sh
source .env

export STATIC_DIR=$HOME/$STATIC
export DATA_DIR=$HOME/$DATA

pipenv run python src/manage.py makemigrations
pipenv run python src/manage.py migrate
pipenv run python src/manage.py collectstatic --clear
