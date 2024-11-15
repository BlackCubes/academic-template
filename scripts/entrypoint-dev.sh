#!/bin/sh
source .env

export PROJECT_DIR=$PROJECT_DIR
export DATA_DIR=$DATA_DIR
export STATIC_DIR=$STATIC_DIR

mkdir -p $PROJECT_DIR
mkdir -p $DATA_DIR
mkdir -p $STATIC_DIR

mkdir -p $DATA_DIR/images
mkdir -p $DATA_DIR/grades

pipenv run python manage.py makemigrations
pipenv run python manage.py migrate

pipenv run python manage.py runserver 0.0.0.0:8000
