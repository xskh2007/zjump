#!/bin/bash
export C_FORCE_ROOT="true"

python manage.py celery worker -c 4 --loglevel=info

