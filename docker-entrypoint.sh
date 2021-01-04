#!/bin/bash

/usr/local/bin/python /opt/jarvis/manage.py migrate --no-input

/usr/local/bin/gunicorn --config /opt/jarvis/etc/gunicorn.py jarvis.wsgi:application