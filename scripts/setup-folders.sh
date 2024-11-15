#!/bin/sh
source .env

printf "%s\n"
echo 'Setting up folders...'
printf "%s\n"

sleep 2

export DATA_DIR=$HOME/$DATA

printf "%s\n"
echo 'Data directory...'
printf "%s\n"

sleep 1

mkdir -p $DATA_DIR

printf "%s\n"
echo 'Images directory...'
printf "%s\n"

sleep 1

mkdir -p $DATA_DIR/images

printf "%s\n"
echo 'Grades directory...'
printf "%s\n"

sleep 1

mkdir -p $DATA_DIR/grades

printf "%s\n"
echo 'Complete!'
printf "%s\n"
