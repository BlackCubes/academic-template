#!/bin/sh
source .env

export STATIC_DIR=$HOME/$STATIC
export DATA_DIR=$HOME/$DATA

pipenv run python src/manage.py runserver 0.0.0.0:8000
