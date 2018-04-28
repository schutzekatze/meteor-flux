#!/bin/bash

sudo uwsgi --ini ../uwsgi.ini --uid=$USER --gid=$USER
